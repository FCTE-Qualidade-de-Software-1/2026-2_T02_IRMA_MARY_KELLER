import csv
from datetime import datetime, timedelta, timezone
import json
import os
import re
import ssl
import urllib.request

import mkdocs_gen_files

TZ_BR = timezone(timedelta(hours=-3))

INTEGRANTES = {
    "camilasilvac": {
        "github": "CamilaSilvaC",
        "nome": "Camila Silva Cavalcante",
        "matricula": "232013944",
    },
    "geovannaumbelino": {
        "github": "GeovannaUmbelino",
        "nome": "Geovanna Alves Umbelino",
        "matricula": "232014450",
    },
    "jaugustom": {
        "github": "JAugustoM",
        "nome": "José Augusto Alves de Moraes",
        "matricula": "231026429",
    },
    "luisa12ll": {
        "github": "luisa12ll",
        "nome": "Luísa de Souza Ferreira",
        "matricula": "232014807",
    },
    "menali17": {
        "github": "menali17",
        "nome": "Enzo Menali Vettorato Toledo",
        "matricula": "241011054",
    },
    "pwdrinho": {
        "github": "Pwdrinho",
        "nome": "Pedro Lucas Barbosa da Silva",
        "matricula": "241025710",
    },
}

REPO_API_URL = "https://api.github.com/repos/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues?state=all&per_page=100"
URL_ISSUES = "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/"
URL_COMMITS = "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author="
CACHE_FILE = ".cache/github_issues.json"


def get_ssl_context():
    """Retorna um contexto SSL configurado com certificados locais comuns em Linux."""
    ca_candidates = [
        os.environ.get("SSL_CERT_FILE"),
        "/etc/ssl/certs/ca-bundle.crt",
        "/etc/ssl/certs/ca-certificates.crt",
        "/etc/pki/tls/certs/ca-bundle.crt",
    ]
    for ca in ca_candidates:
        if ca and os.path.exists(ca):
            return ssl.create_default_context(cafile=ca)
    return ssl.create_default_context()


def fetch_github_issues():
    """Obtém as issues do repositório via API REST do GitHub com suporte a token e cache."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    attempts = []
    if token:
        attempts.append({"User-Agent": "mkdocs-gen-files", "Authorization": f"Bearer {token}"})
    attempts.append({"User-Agent": "mkdocs-gen-files"})

    data = None
    for headers in attempts:
        try:
            req = urllib.request.Request(REPO_API_URL, headers=headers)
            with urllib.request.urlopen(req, context=get_ssl_context(), timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
                with open(CACHE_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f)
                break
        except Exception:
            continue

    if data is None and os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = None

    issues_map = {}
    if not data:
        return issues_map

    for item in data:
        if "pull_request" in item:
            continue
        num = str(item.get("number"))
        body = item.get("body") or ""

        # Extração de estimativa original (He) e janela prevista
        est_match = re.search(
            r"(?:estimativa(?:\s+original)?|horas?\s+estimadas?)\s*[*_]*\s*(?:\([^)]*\)\s*)?[:\|]\s*[*_]*\s*([0-9]+(?:[\.,][0-9]+)?)",
            body,
            re.IGNORECASE,
        )
        estimativa = float(est_match.group(1).replace(",", ".")) if est_match else None

        jan_match = re.search(
            r"(?:janela(?:\s*(?:prevista|original))?|entrega(?:\s*prevista)?)\s*[*_]*\s*[:\|]\s*[*_]*\s*([0-9]{1,2}/[0-9]{1,2}(?:/[0-9]{2,4})?|[0-9]{4}-[0-9]{2}-[0-9]{2})",
            body,
            re.IGNORECASE,
        )
        janela = jan_match.group(1).strip() if jan_match else None

        issues_map[num] = {
            "title": item.get("title", f"Issue #{num}"),
            "state": item.get("state", "open"),
            "closed_at": item.get("closed_at"),
            "estimativa": estimativa,
            "janela": janela,
            "labels": [lbl.get("name") for lbl in item.get("labels", [])],
        }

    return issues_map


def parse_closed_date(closed_at_str):
    """Converte a data ISO de fechamento do GitHub para DD/MM/AAAA no horário de Brasília."""
    if not closed_at_str:
        return "Em andamento"
    try:
        dt = datetime.fromisoformat(closed_at_str.replace("Z", "+00:00")).astimezone(TZ_BR)
        return dt.strftime("%d/%m/%Y")
    except Exception:
        return closed_at_str[:10]


def format_planned_date(janela_raw):
    """Normaliza formatos de data prevista (ex: 21/10 ou 2026-10-21) para DD/MM/AAAA."""
    if not janela_raw:
        return "-"
    janela_raw = janela_raw.strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", janela_raw):
        p = janela_raw.split("-")
        return f"{p[2]}/{p[1]}/{p[0]}"
    if re.match(r"^\d{1,2}/\d{1,2}$", janela_raw):
        p = janela_raw.split("/")
        return f"{int(p[0]):02d}/{int(p[1]):02d}/2026"
    if re.match(r"^\d{1,2}/\d{1,2}/\d{2,4}$", janela_raw):
        p = janela_raw.split("/")
        ano = p[2] if len(p[2]) == 4 else f"20{p[2]}"
        return f"{int(p[0]):02d}/{int(p[1]):02d}/{ano}"
    return janela_raw


def load_hours_data():
    """Carrega e valida os lançamentos dos CSVs de horas de cada integrante."""
    membro_dados = {}
    totais_por_membro = {}
    totais_por_issue = {}

    for arquivo, membro in INTEGRANTES.items():
        caminho = f"assets/dados/gestao/horas/{arquivo}.csv"
        linhas = []
        total_membro = 0.0

        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for raw_row in reader:
                    row = {k.strip(): v.strip() for k, v in raw_row.items() if k}
                    data_str = row.get("data", "")
                    atividade = row.get("atividade", "").lstrip("#").strip()
                    try:
                        horas = float(row.get("horas", 0))
                    except ValueError:
                        horas = 0.0

                    linhas.append({
                        "data": data_str,
                        "atividade": atividade,
                        "horas": horas,
                    })
                    total_membro += horas
                    if atividade:
                        totais_por_issue[atividade] = totais_por_issue.get(atividade, 0.0) + horas

        membro_dados[arquivo] = linhas
        totais_por_membro[arquivo] = total_membro

    return membro_dados, totais_por_membro, totais_por_issue


# Execução da consolidação
issues_api = fetch_github_issues()
membro_dados, totais_por_membro, totais_por_issue = load_hours_data()

# 1. Cálculos de RC1 (Esforço de desenvolvimento)
esforco_total = sum(totais_por_membro.values())
num_membros = len(INTEGRANTES)
media_por_membro = (esforco_total / num_membros) if num_membros > 0 else 0.0

# 2. Cálculos de Pa (Cobertura de registro de esforço)
# Conjunto de issues fechadas na API (Ac)
issues_concluidas = {num: info for num, info in issues_api.items() if info["state"] == "closed"}
total_concluidas = len(issues_concluidas)
issues_com_horas = set(totais_por_issue.keys())
concluidas_com_horas = set(issues_concluidas.keys()) & issues_com_horas

pa_cobertura = (len(concluidas_com_horas) / total_concluidas * 100) if total_concluidas > 0 else 0.0
pa_status = "Adequado (≥ 90%)" if pa_cobertura >= 90.0 else "Com ressalva (< 90%)"

# 3. Cálculos de RC2 (Variação do esforço estimado vs realizado em Ac)
ee_total = 0.0
er_total = 0.0
issues_avaliadas_rc2 = 0

for num, info in issues_concluidas.items():
    if info["estimativa"] is not None and info["estimativa"] > 0:
        ee_total += info["estimativa"]
        er_total += totais_por_issue.get(num, 0.0)
        issues_avaliadas_rc2 += 1

if ee_total > 0:
    ve_percentual = (abs(er_total - ee_total) / ee_total) * 100
    if ve_percentual <= 10.0:
        ve_status = "Adequado (≤ 10%)"
    elif ve_percentual <= 20.0:
        ve_status = "Bom (10% a 20%)"
    else:
        ve_status = "Insuficiente (> 20%)"
    ve_str = f"{ve_percentual:.1f}%"
else:
    ve_str = "Sem dados"
    ve_status = "Sem estimativas numéricas em issues fechadas"


# Geração do artefato Markdown
with mkdocs_gen_files.open("gestao/horas_consolidadas.md", "w") as f:
    print("# Registro e Consolidação de Horas\n", file=f)
    print(
        "Este artefato consolida as horas trabalhadas pela equipe e acompanha os indicadores de "
        "**Recursos e Custos** ([RC1, RC2 e Pa](plano_de_medicao.md#objetivo-3)), integrados "
        "às issues do GitHub via API REST conforme as convenções do [Plano de Medição](plano_de_medicao.md). "
        "As instruções de lançamento individual estão descritas em [Registro de Horas](horas.md).\n",
        file=f,
    )

    print("---\n", file=f)
    print("## 1. Indicadores Consolidados (RC1, RC2 e Pa)\n", file=f)
    print(
        "Quadro sintético de controle de esforço. Para interpretação teórica e limiares, consulte a "
        "[Seção 3.3 do Plano de Medição](plano_de_medicao.md#objetivo-3).\n",
        file=f,
    )
    print("| Indicador | Medida Base / Fórmula | Valor | Referência | Situação |", file=f)
    print("| :--- | :--- | :---: | :---: | :---: |", file=f)
    print(f"| **RC1: Esforço Total** | $Et = \\sum Hr$ | **{esforco_total:.2f} h** | Informativo | Informativo |", file=f)
    print(f"| **RC1: Média por Integrante** | $Hm = Et \\div n$ | **{media_por_membro:.2f} h** | Informativo | Informativo |", file=f)
    print(f"| **RC2: Variação de Estimativa** | $Ve = (\\lvert Er - Ee \\rvert \\div Ee) \\times 100$ | **{ve_str}** | $\\le 10\\%$ | {ve_status} |", file=f)
    print(f"| **Pa: Cobertura de Dados** | $Pa = (Ar \\div Ac) \\times 100$ | **{pa_cobertura:.1f}%** | $\\ge 90\\%$ | {pa_status} |", file=f)
    print("\n---\n", file=f)

    print("## 2. Esforço por Integrante (RC1)\n", file=f)
    print(
        "Acompanha o volume de trabalho individual ($Hi$) e o equilíbrio em relação à média da equipe ($Hm$). "
        "Conforme a [Tabela 8 do Plano de Medição](plano_de_medicao.md#regras), disparidades superiores "
        "a $\\pm 50\\%$ demandam análise da causa e rebalanceamento das próximas atribuições.\n",
        file=f,
    )
    print("| Integrante | Matrícula | Horas ($Hi$) | Relação ($Hi \\div Hm$) | Desvio da Média | Situação |", file=f)
    print("| :--- | :---: | :---: | :---: | :---: | :---: |", file=f)

    for arquivo, membro in INTEGRANTES.items():
        hi = totais_por_membro.get(arquivo, 0.0)
        if media_por_membro > 0:
            relacao = hi / media_por_membro
            desvio = ((hi - media_por_membro) / media_por_membro) * 100
            rel_str = f"{relacao:.2f}"
            desvio_str = f"{desvio:+.1f}%"
            equilibrado = abs(desvio) <= 50.0
            sit_str = "Equilibrado (dentro de ±50%)" if equilibrado else "Desequilibrado (> ±50%)"
        else:
            rel_str = "-"
            desvio_str = "-"
            sit_str = "Sem dados"

        nome_link = f"[{membro['nome']}]({URL_COMMITS}{membro['github']})"
        print(f"| {nome_link} | {membro['matricula']} | {hi:.2f} h | {rel_str} | {desvio_str} | {sit_str} |", file=f)

    print("\n---\n", file=f)
    print("## 3. Esforço por Atividade e Estimativas (RC2)\n", file=f)
    print(
        "Compara o esforço estimado original ($He$) com o realizado ($Hr$) por atividade. "
        "Conforme o [Plano de Medição](plano_de_medicao.md#unidade-de-trabalho), o indicador formal "
        "do RC2 incide sobre issues concluídas ($Ac$).\n",
        file=f,
    )
    print("| Issue | Estado | Janela Prevista | Conclusão Real | Estimado ($He$) | Realizado ($Hr$) | Desvio ($Hr - He$) | Situação |", file=f)
    print("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |", file=f)

    # Identificar todas as issues conhecidas (da API ou dos lançamentos de horas)
    todas_issues_chaves = sorted(
        set(issues_api.keys()) | set(totais_por_issue.keys()),
        key=lambda x: int(x) if x.isdigit() else 9999,
    )

    for chave in todas_issues_chaves:
        info = issues_api.get(chave, {})
        titulo = info.get("title", f"Issue #{chave}")
        estado_api = info.get("state", "aberta")
        estado_str = "Concluída" if estado_api == "closed" else "Em andamento"
        previsto_str = format_planned_date(info.get("janela"))
        real_str = parse_closed_date(info.get("closed_at")) if estado_api == "closed" else "Em andamento"
        he = info.get("estimativa")
        hr = totais_por_issue.get(chave, 0.0)

        link_issue = f"[#{chave} - {titulo}]({URL_ISSUES}{chave})" if chave.isdigit() else chave
        he_str = f"{he:.2f} h" if he is not None else "-"
        hr_str = f"{hr:.2f} h"

        if he is not None:
            desvio = hr - he
            desvio_str = f"{desvio:+.2f} h"
            if he > 0:
                ve_item = (abs(hr - he) / he) * 100
                if ve_item <= 10.0:
                    sit_item = "Adequado (≤ 10%)"
                elif ve_item <= 20.0:
                    sit_item = "Bom (10% a 20%)"
                else:
                    sit_item = "Insuficiente (> 20%)"
            else:
                sit_item = "Estimativa zero"
        else:
            desvio_str = "-"
            sit_item = "Sem estimativa formal"

        print(
            f"| {link_issue} | {estado_str} | {previsto_str} | {real_str} | {he_str} | {hr_str} | {desvio_str} | {sit_item} |",
            file=f,
        )

    print("\n---\n", file=f)
    print("## 4. Detalhamento dos Lançamentos Individuais\n", file=f)
    print(
        "Registros diários individuais extraídos dos arquivos CSV versionados em `assets/dados/gestao/horas/`.\n",
        file=f,
    )

    for arquivo, membro in INTEGRANTES.items():
        print(
            f"### [{membro['nome']}]({URL_COMMITS}{membro['github']}) - {membro['matricula']}\n",
            file=f,
        )
        print("| Data | Horas | Atividade / Issue |", file=f)
        print("| :-: | :-: | :--- |", file=f)

        linhas = membro_dados.get(arquivo, [])
        if not linhas:
            print("| - | 0.00 h | Nenhum lançamento registrado |", file=f)
        else:
            for row in linhas:
                data_partes = row["data"].split("-")
                data_formatada = (
                    f"{data_partes[2]}/{data_partes[1]}/{data_partes[0]}"
                    if len(data_partes) == 3
                    else row["data"]
                )
                act = row["atividade"]
                if act in issues_api:
                    titulo_act = issues_api[act]["title"]
                    issue_link = f"[Issue #{act}: {titulo_act}]({URL_ISSUES}{act})"
                elif act.isdigit():
                    issue_link = f"[Issue #{act}]({URL_ISSUES}{act})"
                else:
                    issue_link = act or "Não especificada"

                print(f"| {data_formatada} | {row['horas']:.2f} h | {issue_link} |", file=f)

        print(file=f)
