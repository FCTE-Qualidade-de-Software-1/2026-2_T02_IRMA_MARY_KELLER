import argparse
import csv
from datetime import datetime, timedelta, timezone
import json
import os
import re
import ssl
import sys
import urllib.request

try:
    import mkdocs_gen_files
    HAS_MKDOCS_GEN_FILES = True
except ImportError:
    HAS_MKDOCS_GEN_FILES = False

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
AUTOAVALIACAO_FILE = "assets/dados/gestao/autoavaliacao.csv"


def load_env_file():
    """Carrega variáveis de ambiente de um arquivo .env na raiz do projeto."""
    candidates = [
        ".env",
        os.path.join(os.path.dirname(__file__), "..", "..", ".env"),
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#") or "=" not in line:
                            continue
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip("'\"")
                        if k and k not in os.environ:
                            os.environ[k] = v
                break
            except Exception:
                pass


load_env_file()


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


def parse_date_string(date_raw):
    """Converte formatos de data (ex: 21/10, 21/10/2026, 2026-10-21) para datetime.date."""
    if not date_raw:
        return None
    date_raw = date_raw.strip()

    # Formato ISO AAAA-MM-DD
    m_iso = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})", date_raw)
    if m_iso:
        try:
            return datetime(int(m_iso.group(1)), int(m_iso.group(2)), int(m_iso.group(3))).date()
        except ValueError:
            return None

    # Formato DD/MM ou DD/MM/AAAA
    m_br = re.match(r"^(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?", date_raw)
    if m_br:
        dia = int(m_br.group(1))
        mes = int(m_br.group(2))
        ano_str = m_br.group(3)
        ano = int(ano_str) if ano_str else 2026
        if ano < 100:
            ano += 2000
        try:
            return datetime(ano, mes, dia).date()
        except ValueError:
            return None

    return None


def format_date_display(dt):
    """Formata datetime.date ou datetime para DD/MM/AAAA."""
    if not dt:
        return "-"
    if isinstance(dt, datetime):
        return dt.strftime("%d/%m/%Y")
    return dt.strftime("%d/%m/%Y")


def parse_closed_datetime(closed_at_str):
    """Converte a data ISO de fechamento do GitHub para objeto date no horário de Brasília."""
    if not closed_at_str:
        return None
    try:
        dt = datetime.fromisoformat(closed_at_str.replace("Z", "+00:00")).astimezone(TZ_BR)
        return dt.date()
    except Exception:
        return None


def fetch_github_issues():
    """Obtém as issues do repositório via API REST do GitHub com suporte a token (.env) e cache."""
    load_env_file()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    attempts = []
    if token:
        attempts.append({"User-Agent": "mkdocs-gen-files", "Authorization": f"Bearer {token}"})
    attempts.append({"User-Agent": "mkdocs-gen-files"})

    data = None
    last_error = None
    for headers in attempts:
        try:
            req = urllib.request.Request(REPO_API_URL, headers=headers)
            with urllib.request.urlopen(req, context=get_ssl_context(), timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
                with open(CACHE_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f)
                break
        except urllib.error.HTTPError as e:
            last_error = e
            if e.code == 403:
                # Rate limit ou falta de permissão
                continue
        except Exception as e:
            last_error = e
            continue

    if data is None and os.path.exists(CACHE_FILE):
        if last_error and getattr(last_error, "code", None) == 403:
            print(
                "[AVISO] Limite de requisições da API do GitHub atingido (HTTP 403 Rate Limit).\n"
                "        Utilizando cache local '.cache/github_issues.json'.\n"
                "        Para atualizar em tempo real, defina GITHUB_TOKEN no arquivo .env da raiz do projeto.",
                file=sys.stderr,
            )
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

        # Extração de estimativa original (He)
        est_match = re.search(
            r"(?:estimativa(?:\s+original)?|horas?\s+estimadas?)\s*[*_]*\s*(?:\([^)]*\)\s*)?[:\|]\s*[*_]*\s*([0-9]+(?:[\.,][0-9]+)?)",
            body,
            re.IGNORECASE,
        )
        estimativa = float(est_match.group(1).replace(",", ".")) if est_match else None

        # Extração de janela original
        jan_match = re.search(
            r"(?:janela(?:\s*(?:prevista|original))?|entrega(?:\s*prevista)?)\s*[*_]*\s*[:\|]\s*[*_]*\s*([0-9]{1,2}/[0-9]{1,2}(?:/[0-9]{2,4})?|[0-9]{4}-[0-9]{2}-[0-9]{2})",
            body,
            re.IGNORECASE,
        )
        janela_raw = jan_match.group(1).strip() if jan_match else None
        janela_date = parse_date_string(janela_raw)

        # Milestone e labels
        ms = item.get("milestone")
        ms_title = ms.get("title") if ms else None
        labels = [lbl.get("name") for lbl in item.get("labels", [])]
        labels_lower = [lbl.lower() for lbl in labels]

        if not ms_title:
            if "Fase-1" in labels or "fase-1" in labels_lower:
                ms_title = "Fase 1"
            elif "Fase-2" in labels or "fase-2" in labels_lower:
                ms_title = "Fase 2"
            elif "Fase-3" in labels or "fase-3" in labels_lower:
                ms_title = "Fase 3"
            elif "Fase-4" in labels or "fase-4" in labels_lower:
                ms_title = "Fase 4"
            else:
                ms_title = "Outras atividades"

        closed_at = item.get("closed_at")
        closed_date = parse_closed_datetime(closed_at)

        # Extração de critérios associados (ex: F1-C1, F2-C4, F3-C2)
        criterios_encontrados = sorted(list(set(re.findall(r"\bF[1-4]-C\d+\b", body, re.IGNORECASE))))

        # Detecção de Retrabalho (DP1)
        # Critérios de retrabalho:
        # 1. Label de correção ('correcao', 'correção', 'retrabalho', 'bug', 'fix')
        # 2. Marcação explícita no corpo da issue
        # 3. Issue reaberta
        tem_label_correcao = any(
            lbl in ["correcao", "correção", "retrabalho", "bug", "fix"] for lbl in labels_lower
        )
        tem_texto_retrabalho = bool(
            re.search(
                r"(?:retrabalho\s*[*_]*\s*[:\|]\s*[*_]*\s*(?:sim|true|s|yes)|tipo\s*[*_]*\s*[:\|]\s*[*_]*\s*(?:corre[çc][aã]o|retrabalho)|classifica[çc][aã]o\s*[*_]*\s*[:\|][^\n]*retrabalho|\[x\]\s*(?:corre[çc][aã]o|retrabalho))",
                body,
                re.IGNORECASE,
            )
        )
        is_retrabalho = tem_label_correcao or tem_texto_retrabalho

        # Extração de issue de origem e causa do retrabalho se disponível
        origem_match = re.search(
            r"(?:issue\s+de\s+origem|origem)\s*[*_]*\s*[:\|]\s*[*_]*\s*#?([0-9]+)",
            body,
            re.IGNORECASE,
        )
        issue_origem = origem_match.group(1) if origem_match else None

        causa_match = re.search(
            r"(?:causa(?:\s+raiz)?(?:\s+do\s+retrabalho)?)\s*[*_]*\s*[:\|]\s*[*_]*\s*([^\n]+)",
            body,
            re.IGNORECASE,
        )
        causa_retrabalho = causa_match.group(1).strip() if causa_match else None

        issues_map[num] = {
            "title": item.get("title", f"Issue #{num}"),
            "state": item.get("state", "open"),
            "closed_at": closed_at,
            "closed_date": closed_date,
            "estimativa": estimativa,
            "janela_raw": janela_raw,
            "janela_date": janela_date,
            "milestone": ms_title,
            "labels": labels,
            "criterios": criterios_encontrados,
            "is_retrabalho": is_retrabalho,
            "issue_origem": issue_origem,
            "causa_retrabalho": causa_retrabalho,
        }

    return issues_map


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


def load_autoavaliacao_data():
    """Carrega as avaliações por critério de assets/dados/gestao/autoavaliacao.csv."""
    registros = []
    contagens = {"Adequado": 0, "Bom": 0, "Insuficiente": 0, "Crítico": 0}

    if not os.path.exists(AUTOAVALIACAO_FILE):
        return registros, contagens

    with open(AUTOAVALIACAO_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            item = {k.strip(): v.strip() for k, v in row.items() if k}
            criterio = item.get("criterio", "")
            nivel_raw = item.get("nivel", "")
            fase = item.get("fase", "")
            data_av = item.get("data", "")
            evidencia = item.get("evidencia", "")

            # Normalização de níveis
            nivel_normalizado = None
            if re.search(r"adequado|excelente", nivel_raw, re.IGNORECASE):
                nivel_normalizado = "Adequado"
            elif re.search(r"bom|satisfat[oó]rio", nivel_raw, re.IGNORECASE):
                nivel_normalizado = "Bom"
            elif re.search(r"insuficiente|regular", nivel_raw, re.IGNORECASE):
                nivel_normalizado = "Insuficiente"
            elif re.search(r"cr[ií]tico", nivel_raw, re.IGNORECASE):
                nivel_normalizado = "Crítico"

            if nivel_normalizado:
                contagens[nivel_normalizado] += 1

            registros.append({
                "data": data_av,
                "fase": fase,
                "criterio": criterio,
                "nivel": nivel_normalizado or nivel_raw or "Não avaliado",
                "evidencia": evidencia,
            })

    return registros, contagens


def consolidate_metrics(data_corte=None):
    """Consolida todas as medições do Plano de Medição (CP1, CP2, DP1, DP2, RC1, RC2, Pa)."""
    issues_api = fetch_github_issues()
    membro_dados, totais_por_membro, totais_por_issue = load_hours_data()
    autoavaliacao_registros, autoavaliacao_contagens = load_autoavaliacao_data()

    if data_corte is None:
        data_corte = datetime.now(TZ_BR).date()

    # ----------------------------------------------------
    # 1. CP1 - Progresso das atividades
    # Ac = Atividades concluídas
    # Ap = Atividades planejadas cuja janela <= data da medição
    # Ppp = (Ac / Ap) * 100
    # ----------------------------------------------------
    issues_concluidas = {num: info for num, info in issues_api.items() if info["state"] == "closed"}
    ac_total = len(issues_concluidas)

    issues_planejadas_ate_data = {
        num: info for num, info in issues_api.items()
        if info["janela_date"] is not None and info["janela_date"] <= data_corte
    }
    ap_total = max(len(issues_planejadas_ate_data), ac_total)

    if ap_total > 0:
        ppp = (ac_total / ap_total) * 100.0
        if ppp >= 90.0:
            cp1_status = "Adequado (≥ 90%)"
            cp1_cor = "Verde"
        elif ppp >= 80.0:
            cp1_status = "Bom (80% a 90%)"
            cp1_cor = "Verde"
        elif ppp >= 60.0:
            cp1_status = "Insuficiente (60% a 80%)"
            cp1_cor = "Amarelo"
        else:
            cp1_status = "Crítico (< 60%)"
            cp1_cor = "Vermelho"
        cp1_str = f"{ppp:.1f}%"
    else:
        cp1_str = "Sem dados"
        cp1_status = "Sem atividades planejadas até a data"
        cp1_cor = "Sem cor"
        ppp = None

    # ----------------------------------------------------
    # 2. CP2 - Cumprimento do prazo
    # Acp = Atividades concluídas no prazo (closed_date <= janela_date)
    # Ac = Atividades concluídas com janela avaliável
    # Pacp = (Acp / Ac) * 100
    # ----------------------------------------------------
    acp_total = 0
    concluidas_com_janela = 0
    detalhes_cp2 = {}

    for num, info in issues_concluidas.items():
        j_date = info["janela_date"]
        c_date = info["closed_date"]

        if j_date and c_date:
            concluidas_com_janela += 1
            no_prazo = c_date <= j_date
            if no_prazo:
                acp_total += 1
            detalhes_cp2[num] = {
                "no_prazo": no_prazo,
                "janela_date": j_date,
                "closed_date": c_date,
            }
        else:
            detalhes_cp2[num] = {
                "no_prazo": None,
                "janela_date": j_date,
                "closed_date": c_date,
            }

    if concluidas_com_janela > 0:
        pacp = (acp_total / concluidas_com_janela) * 100.0
        if pacp >= 90.0:
            cp2_status = "Adequado (≥ 90%)"
            cp2_cor = "Verde"
        elif pacp >= 80.0:
            cp2_status = "Bom (80% a 90%)"
            cp2_cor = "Verde"
        elif pacp >= 60.0:
            cp2_status = "Insuficiente (60% a 80%)"
            cp2_cor = "Amarelo"
        else:
            cp2_status = "Crítico (< 60%)"
            cp2_cor = "Vermelho"
        cp2_str = f"{pacp:.1f}%"
    else:
        cp2_str = "Sem dados"
        cp2_status = "Nenhuma issue concluída com janela definida"
        cp2_cor = "Sem cor"
        pacp = None

    # ----------------------------------------------------
    # 3. DP1 - Eficiência do processo (Retrabalho em Issues)
    # If = issues fechadas
    # Ir = issues reabertas
    # Ic = issues com label 'correcao' ou texto padrão no corpo
    # Pri = [(Ir ∪ Ic) / If] * 100
    # ----------------------------------------------------
    if_total = ac_total
    issues_retrabalho = {num: info for num, info in issues_api.items() if info["is_retrabalho"]}
    retrabalho_fechadas = {num: info for num, info in issues_retrabalho.items() if info["state"] == "closed"}
    ir_ic_count = len(retrabalho_fechadas)

    if if_total > 0:
        pri = (ir_ic_count / if_total) * 100.0
        if pri <= 15.0:
            dp1_status = "Adequado (≤ 15%)"
            dp1_cor = "Verde"
        elif pri <= 35.0:
            dp1_status = "Bom (15% a 35%)"
            dp1_cor = "Verde"
        elif pri < 50.0:
            dp1_status = "Insuficiente (35% a 50%)"
            dp1_cor = "Amarelo"
        else:
            dp1_status = "Crítico (≥ 50%)"
            dp1_cor = "Vermelho"
        dp1_str = f"{pri:.1f}%"
    else:
        dp1_str = "Sem dados"
        dp1_status = "Sem issues fechadas"
        dp1_cor = "Sem cor"
        pri = None

    # ----------------------------------------------------
    # 4. DP2 - Efetividade do processo (Critérios da Rubrica)
    # Ca, Cb, Ci, Cc
    # Qcic = Ci + Cc
    # PCa = (Ca / Ct) * 100
    # ----------------------------------------------------
    ca = autoavaliacao_contagens["Adequado"]
    cb = autoavaliacao_contagens["Bom"]
    ci = autoavaliacao_contagens["Insuficiente"]
    cc = autoavaliacao_contagens["Crítico"]
    ct = ca + cb + ci + cc

    if ct > 0:
        qcic = ci + cc
        if qcic <= 0:
            qcic_status = "Adequado (≤ 0)"
            qcic_cor = "Verde"
        elif qcic <= 2:
            qcic_status = "Bom (1 a 2)"
            qcic_cor = "Verde"
        else:
            qcic_status = "Insuficiente (≥ 3)"
            qcic_cor = "Amarelo"

        pca = (ca / ct) * 100.0
        if pca >= 90.0:
            pca_status = "Adequado (≥ 90%)"
            pca_cor = "Verde"
        elif pca >= 75.0:
            pca_status = "Bom (75% a 90%)"
            pca_cor = "Verde"
        else:
            pca_status = "Insuficiente (< 75%)"
            pca_cor = "Amarelo"

        dp2_qcic_str = f"{qcic}"
        dp2_pca_str = f"{pca:.1f}%"
    else:
        qcic = None
        pca = None
        dp2_qcic_str = "Sem dados"
        qcic_status = "Autoavaliação pendente em autoavaliacao.csv"
        qcic_cor = "Sem cor"
        dp2_pca_str = "Sem dados"
        pca_status = "Autoavaliação pendente em autoavaliacao.csv"
        pca_cor = "Sem cor"

    # ----------------------------------------------------
    # 5. RC1 - Esforço de desenvolvimento
    # Et = Σ Hr
    # ----------------------------------------------------
    esforco_total = sum(totais_por_membro.values())
    num_membros = len(INTEGRANTES)
    media_por_membro = (esforco_total / num_membros) if num_membros > 0 else 0.0

    # ----------------------------------------------------
    # 6. Pa - Cobertura de registro de esforço
    # Pa = (Ar / Ac) * 100
    # ----------------------------------------------------
    issues_com_horas = set(totais_por_issue.keys())
    concluidas_com_horas = set(issues_concluidas.keys()) & issues_com_horas
    pa_cobertura = (len(concluidas_com_horas) / ac_total * 100) if ac_total > 0 else 0.0
    pa_status = "Adequado (≥ 90%)" if pa_cobertura >= 90.0 else "Com ressalva (< 90%)"
    pa_cor = "Verde" if pa_cobertura >= 90.0 else "Amarelo"

    # ----------------------------------------------------
    # 7. RC2 - Variação do esforço estimado vs realizado em Ac
    # Ve = (|Er - Ee| / Ee) * 100
    # ----------------------------------------------------
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
            ve_cor = "Verde"
        elif ve_percentual <= 20.0:
            ve_status = "Bom (10% a 20%)"
            ve_cor = "Verde"
        else:
            ve_status = "Insuficiente (> 20%)"
            ve_cor = "Amarelo"
        ve_str = f"{ve_percentual:.1f}%"
    else:
        ve_str = "Sem dados"
        ve_status = "Sem estimativas numéricas em issues fechadas"
        ve_cor = "Sem cor"

    return {
        "data_corte": data_corte,
        "issues_api": issues_api,
        "membro_dados": membro_dados,
        "totais_por_membro": totais_por_membro,
        "totais_por_issue": totais_por_issue,
        "autoavaliacao_registros": autoavaliacao_registros,
        "autoavaliacao_contagens": autoavaliacao_contagens,
        # CP1
        "ac_total": ac_total,
        "ap_total": ap_total,
        "cp1_str": cp1_str,
        "cp1_status": cp1_status,
        "cp1_cor": cp1_cor,
        # CP2
        "acp_total": acp_total,
        "concluidas_com_janela": concluidas_com_janela,
        "detalhes_cp2": detalhes_cp2,
        "cp2_str": cp2_str,
        "cp2_status": cp2_status,
        "cp2_cor": cp2_cor,
        # DP1
        "if_total": if_total,
        "ir_ic_count": ir_ic_count,
        "issues_retrabalho": issues_retrabalho,
        "retrabalho_fechadas": retrabalho_fechadas,
        "dp1_str": dp1_str,
        "dp1_status": dp1_status,
        "dp1_cor": dp1_cor,
        # DP2
        "ca": ca,
        "cb": cb,
        "ci": ci,
        "cc": cc,
        "ct": ct,
        "dp2_qcic_str": dp2_qcic_str,
        "qcic_status": qcic_status,
        "qcic_cor": qcic_cor,
        "dp2_pca_str": dp2_pca_str,
        "pca_status": pca_status,
        "pca_cor": pca_cor,
        # RC1
        "esforco_total": esforco_total,
        "media_por_membro": media_por_membro,
        # Pa
        "pa_cobertura": pa_cobertura,
        "pa_status": pa_status,
        "pa_cor": pa_cor,
        # RC2
        "ee_total": ee_total,
        "er_total": er_total,
        "ve_str": ve_str,
        "ve_status": ve_status,
        "ve_cor": ve_cor,
    }


def render_markdown(metrics, output_file):
    """Gera o artefato completo em Markdown com todos os indicadores do PSM/CID."""
    m = metrics
    issues_api = m["issues_api"]
    totais_por_issue = m["totais_por_issue"]
    totais_por_membro = m["totais_por_membro"]
    membro_dados = m["membro_dados"]

    print("# Painel Consolidado de Medição PSM/CID e Registro de Horas\n", file=output_file)
    print(
        "Este artefato consolida a medição contínua do projeto integrando os modelos **PSM (Practical Software Measurement)** "
        "e a norma **ISO/IEC/IEEE 15939:2017**, conforme estabelecido no [Plano de Medição](plano_de_medicao.md) e no "
        "[Procedimento de Medição](medicoes.md). Os dados de progresso e esforço são sincronizados automaticamente com "
        "as issues do GitHub e com os registros diários de horas em CSV.\n",
        file=output_file,
    )
    print(f"**Data de referência da consolidação:** {format_date_display(m['data_corte'])}\n", file=output_file)
    print("---\n", file=output_file)

    # ----------------------------------------------------
    # Tabela Sintética Geral
    # ----------------------------------------------------
    def render_row(cor, categoria, indicador, formula, valor, meta, situacao):
        if cor == "Verde":
            bg = "#dff0d8"
            color = "#2b542c"
            cls = "success"
        elif cor == "Amarelo":
            bg = "#fcf8e3"
            color = "#66512c"
            cls = "warning"
        elif cor == "Vermelho":
            bg = "#f2dede"
            color = "#843534"
            cls = "danger"
        else:
            bg = "#ffffff"
            color = "#333333"
            cls = ""

        td_l = f'style="background-color: {bg} !important; color: {color} !important;"'
        td_c = f'style="background-color: {bg} !important; color: {color} !important; text-align: center;"'

        meta_rendered = f'<span class="arithmatex">{meta}</span>' if meta.startswith("\\") or "(" in meta else meta

        return (
            f'<tr class="{cls}">\n'
            f'  <td {td_l}><strong>{categoria}</strong></td>\n'
            f'  <td {td_l}><strong>{indicador}</strong></td>\n'
            f'  <td {td_l}><span class="arithmatex">{formula}</span></td>\n'
            f'  <td {td_c}><strong>{valor}</strong></td>\n'
            f'  <td {td_c}>{meta_rendered}</td>\n'
            f'  <td {td_c}>{situacao}</td>\n'
            f'</tr>'
        )

    print("## 1. Painel Geral de Indicadores PSM/CID\n", file=output_file)
    print(
        "Síntese executiva de todas as medidas das três categorias do plano. A coloração de cada linha reflete "
        "o nível operacional atingido pelo indicador (Verde: Adequado/Bom; Amarelo: Insuficiente/Com ressalva; Vermelho: Crítico). "
        "Para justificativas e regras de decisão, consulte as seções correspondentes do [Plano de Medição](plano_de_medicao.md).\n",
        file=output_file,
    )
    print('<table class="table table-bordered">', file=output_file)
    print("<thead>", file=output_file)
    print("<tr>", file=output_file)
    print("  <th>Categoria</th>", file=output_file)
    print("  <th>Indicador</th>", file=output_file)
    print("  <th>Medida Base / Fórmula</th>", file=output_file)
    print('  <th style="text-align: center;">Valor</th>', file=output_file)
    print('  <th style="text-align: center;">Meta / Referência</th>', file=output_file)
    print('  <th style="text-align: center;">Situação Operacional</th>', file=output_file)
    print("</tr>", file=output_file)
    print("</thead>", file=output_file)
    print("<tbody>", file=output_file)

    # 1. CP1
    print(render_row(m["cp1_cor"], "Calendário e Progresso", "CP1: Progresso do Planejado", "\\(Ppp = (Ac \\div Ap) \\times 100\\)", m["cp1_str"], "\\(\\ge 90\\%\\)", m["cp1_status"]), file=output_file)
    # 2. CP2
    print(render_row(m["cp2_cor"], "Calendário e Progresso", "CP2: Cumprimento do Prazo", "\\(Pacp = (Acp \\div Ac) \\times 100\\)", m["cp2_str"], "\\(\\ge 90\\%\\)", m["cp2_status"]), file=output_file)
    # 3. DP1
    print(render_row(m["dp1_cor"], "Desempenho dos Processos", "DP1: Eficiência (Retrabalho)", "\\(Pri = [(Ir \\cup Ic) \\div If] \\times 100\\)", m["dp1_str"], "\\(\\le 15\\%\\)", m["dp1_status"]), file=output_file)
    # 4. DP2 Qcic
    print(render_row(m["qcic_cor"], "Desempenho dos Processos", "DP2: Critérios Fracos", "\\(Qcic = Ci + Cc\\)", m["dp2_qcic_str"], "\\(\\le 0\\)", m["qcic_status"]), file=output_file)
    # 5. DP2 PCa
    print(render_row(m["pca_cor"], "Desempenho dos Processos", "DP2: Critérios Adequados", "\\(PCa = (Ca \\div Ct) \\times 100\\)", m["dp2_pca_str"], "\\(\\ge 90\\%\\)", m["pca_status"]), file=output_file)
    # 6. RC1 Total
    print(render_row("Informativo", "Recursos e Custos", "RC1: Esforço Total", "\\(Et = \\sum Hr\\)", f"{m['esforco_total']:.2f} h", "Informativo", "Informativo"), file=output_file)
    # 7. RC1 Média
    print(render_row("Informativo", "Recursos e Custos", "RC1: Média por Membro", "\\(Hm = Et \\div n\\)", f"{m['media_por_membro']:.2f} h", "Informativo", "Informativo"), file=output_file)
    # 8. RC2
    print(render_row(m["ve_cor"], "Recursos e Custos", "RC2: Variação de Estimativa", "\\(Ve = (\\lvert Er - Ee \\rvert \\div Ee) \\times 100\\)", m["ve_str"], "\\(\\le 10\\%\\)", m["ve_status"]), file=output_file)
    # 9. Pa
    print(render_row(m["pa_cor"], "Recursos e Custos", "Pa: Cobertura de Dados", "\\(Pa = (Ar \\div Ac) \\times 100\\)", f"{m['pa_cobertura']:.1f}%", "\\(\\ge 90\\%\\)", m["pa_status"]), file=output_file)

    print("</tbody>", file=output_file)
    print("</table>\n", file=output_file)
    print("\n---\n", file=output_file)

    # ----------------------------------------------------
    # Seção 2: Calendário e Progresso (CP1 e CP2)
    # ----------------------------------------------------
    print("## 2. Calendário e Progresso (CP1 e CP2)\n", file=output_file)
    print(
        "Acompanha o ritmo volumétrico de execução frente ao planejado (**CP1**) e a pontualidade na conclusão em relação "
        "à Janela original (**CP2**). Conforme a regra da Seção 4.2 do plano, adiamentos registrados em comentários mantêm "
        "a comparação atrelada à linha de base original para garantir a transparência histórica.\n",
        file=output_file,
    )
    print(f"- **Atividades concluídas ($Ac$):** {m['ac_total']}", file=output_file)
    print(f"- **Atividades planejadas até a data ($Ap$):** {m['ap_total']}", file=output_file)
    print(f"- **Atividades concluídas no prazo original ($Acp$):** {m['acp_total']}", file=output_file)
    print(f"- **Índice de Progresso ($Ppp$):** {m['cp1_str']} — Situação: **{m['cp1_status']}**", file=output_file)
    print(f"- **Índice de Pontualidade ($Pacp$):** {m['cp2_str']} — Situação: **{m['cp2_status']}**\n", file=output_file)

    print("### Rastreamento de Pontualidade por Issue (CP2)\n", file=output_file)
    print("| Issue | Milestone | Janela Original | Fechamento Real | Pontualidade |", file=output_file)
    print("| :--- | :---: | :---: | :---: | :---: |", file=output_file)

    todas_chaves_num = sorted(
        [k for k in issues_api.keys() if k.isdigit()],
        key=lambda x: int(x),
    )

    for chave in todas_chaves_num:
        info = issues_api[chave]
        if info["state"] != "closed":
            continue
        titulo = info.get("title", f"Issue #{chave}")
        link = f"[#{chave} - {titulo}]({URL_ISSUES}{chave})"
        ms = info.get("milestone") or "Geral"
        jan_str = format_date_display(info["janela_date"]) if info["janela_date"] else info.get("janela_raw") or "Não definida"
        real_str = format_date_display(info["closed_date"]) if info["closed_date"] else "Em aberto"

        status_prazo = m["detalhes_cp2"].get(chave, {}).get("no_prazo")
        if status_prazo is True:
            pont_str = "No prazo"
        elif status_prazo is False:
            pont_str = "Atrasada"
        else:
            pont_str = "Sem janela formal"

        print(f"| {link} | {ms} | {jan_str} | {real_str} | {pont_str} |", file=output_file)

    print("\n---\n", file=output_file)

    # ----------------------------------------------------
    # Seção 3: Desempenho dos Processos (DP1 e DP2)
    # ----------------------------------------------------
    print("## 3. Desempenho dos Processos (DP1 e DP2)\n", file=output_file)
    print(
        "Avalia a estabilidade do fluxo de trabalho contra retrabalho (**DP1**) e a conformidade das entregas "
        "frente à rubrica acadêmica (**DP2**).\n",
        file=output_file,
    )

    print("### 3.1 Eficiência do Processo e Retrabalho (DP1)\n", file=output_file)
    print(
        "O retrabalho ($Pri$) contabiliza issues reabertas ($Ir$) e issues com label `correcao` ou metadados de retrabalho ($Ic$), "
        "divididas pelo total de issues fechadas ($If$). A união previne dupla contagem.\n",
        file=output_file,
    )
    print(f"- **Issues fechadas ($If$):** {m['if_total']}", file=output_file)
    print(f"- **Issues identificadas com retrabalho ($Ir \\cup Ic$):** {m['ir_ic_count']}", file=output_file)
    print(f"- **Percentual de Retrabalho ($Pri$):** {m['dp1_str']} — Situação: **{m['dp1_status']}**\n", file=output_file)

    if m["issues_retrabalho"]:
        print("| Issue | Título | Origem | Causa Raiz Declarada | Critérios Afetados |", file=output_file)
        print("| :---: | :--- | :---: | :--- | :---: |", file=output_file)
        for num, info in sorted(m["issues_retrabalho"].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
            link = f"[#{num}]({URL_ISSUES}{num})"
            origem = f"#{info['issue_origem']}" if info.get("issue_origem") else "-"
            causa = info.get("causa_retrabalho") or "Correção/Revisão registrada"
            crits = ", ".join(info.get("criterios", [])) or "-"
            print(f"| {link} | {info['title']} | {origem} | {causa} | {crits} |", file=output_file)
        print(file=output_file)
    else:
        print("> [!NOTE]\n> Nenhuma issue foi sinalizada com label `correcao` ou marcação de retrabalho até o momento.\n", file=output_file)

    print("### 3.2 Efetividade do Processo e Rubrica Acadêmica (DP2)\n", file=output_file)
    print(
        "Mede a aderência qualitativa das entregas contra a rubrica docente, baseada nas avaliações registradas em "
        "`assets/dados/gestao/autoavaliacao.csv`.\n",
        file=output_file,
    )
    print(f"- **Critérios avaliados ($Ct$):** {m['ct']}", file=output_file)
    print(f"- **Distribuição:** Adequado: {m['ca']} | Bom: {m['cb']} | Insuficiente: {m['ci']} | Crítico: {m['cc']}", file=output_file)
    print(f"- **Critérios Fracos ($Qcic = Ci + Cc$):** {m['dp2_qcic_str']} — Situação: **{m['qcic_status']}**", file=output_file)
    print(f"- **Percentual Adequado ($PCa$):** {m['dp2_pca_str']} — Situação: **{m['pca_status']}**\n", file=output_file)

    if m["autoavaliacao_registros"]:
        print("| Data | Fase | Critério | Nível de Avaliação | Evidência Documentada |", file=output_file)
        print("| :---: | :---: | :---: | :---: | :--- |", file=output_file)
        for reg in m["autoavaliacao_registros"]:
            ev_str = f"[Link de Evidência]({reg['evidencia']})" if reg['evidencia'].startswith("http") else (reg['evidencia'] or "-")
            print(f"| {reg['data']} | {reg['fase']} | **{reg['criterio']}** | {reg['nivel']} | {ev_str} |", file=output_file)
        print(file=output_file)

    print("\n---\n", file=output_file)

    # ----------------------------------------------------
    # Seção 4: Recursos e Custos (RC1, RC2 e Pa)
    # ----------------------------------------------------
    print("## 4. Recursos e Custos (RC1, RC2 e Pa)\n", file=output_file)
    print(
        "Acompanha o volume de trabalho individual ($Hi$) e o equilíbrio em relação à média da equipe ($Hm$). "
        "Conforme a Tabela 8 do Plano de Medição, disparidades superiores a $\\pm 50\\%$ demandam análise da causa "
        "e rebalanceamento das próximas atribuições.\n",
        file=output_file,
    )
    print("| Integrante | Matrícula | Horas ($Hi$) | Relação ($Hi \\div Hm$) | Desvio da Média | Situação de Equilíbrio |", file=output_file)
    print("| :--- | :---: | :---: | :---: | :---: | :---: |", file=output_file)

    for arquivo, membro in INTEGRANTES.items():
        hi = totais_por_membro.get(arquivo, 0.0)
        if m["media_por_membro"] > 0:
            relacao = hi / m["media_por_membro"]
            desvio = ((hi - m["media_por_membro"]) / m["media_por_membro"]) * 100
            rel_str = f"{relacao:.2f}"
            desvio_str = f"{desvio:+.1f}%"
            equilibrado = abs(desvio) <= 50.0
            sit_str = "Equilibrado (dentro de ±50%)" if equilibrado else "Desequilibrado (> ±50%)"
        else:
            rel_str = "-"
            desvio_str = "-"
            sit_str = "Sem dados"

        nome_link = f"[{membro['nome']}]({URL_COMMITS}{membro['github']})"
        print(f"| {nome_link} | {membro['matricula']} | {hi:.2f} h | {rel_str} | {desvio_str} | {sit_str} |", file=output_file)

    print("\n---\n", file=output_file)

    # ----------------------------------------------------
    # Seção 5: Esforço por Atividade e Estimativas (RC2)
    # ----------------------------------------------------
    print("## 5. Esforço por Atividade e Estimativas (RC2)\n", file=output_file)
    print(
        "Compara o esforço estimado original ($He$) com o realizado ($Hr$) por atividade, agrupadas por "
        "milestone (fase do projeto). Conforme o Plano de Medição, o indicador formal do RC2 incide sobre issues concluídas ($Ac$).\n",
        file=output_file,
    )

    todas_issues_chaves = sorted(
        set(issues_api.keys()) | set(totais_por_issue.keys()),
        key=lambda x: int(x) if x.isdigit() else 9999,
    )

    issues_por_milestone = {}
    for chave in todas_issues_chaves:
        info = issues_api.get(chave, {})
        ms_nome = info.get("milestone") or "Outras atividades"
        issues_por_milestone.setdefault(ms_nome, []).append(chave)

    def milestone_sort_key(ms_name):
        ordem_padrao = {
            "Fase 1": 1,
            "Fase 2": 2,
            "Fase 3": 3,
            "Fase 4": 4,
        }
        return (ordem_padrao.get(ms_name, 99), ms_name)

    milestones_ordenados = sorted(issues_por_milestone.keys(), key=milestone_sort_key)

    for ms_nome in milestones_ordenados:
        chaves_ms = issues_por_milestone[ms_nome]
        horas_ms = sum(totais_por_issue.get(c, 0.0) for c in chaves_ms)

        print(f"### {ms_nome}\n", file=output_file)
        print(f"**Total de horas realizadas:** {horas_ms:.2f} h\n", file=output_file)
        print(
            "| Issue | Estado | Janela Prevista | Conclusão Real | Estimado ($He$) | Realizado ($Hr$) | Desvio ($Hr - He$) | Situação |",
            file=output_file,
        )
        print("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |", file=output_file)

        for chave in chaves_ms:
            info = issues_api.get(chave, {})
            titulo = info.get("title", f"Issue #{chave}")
            estado_api = info.get("state", "aberta")
            estado_str = "Concluída" if estado_api == "closed" else "Em andamento"
            previsto_str = format_date_display(info.get("janela_date")) if info.get("janela_date") else (info.get("janela_raw") or "-")
            real_str = format_date_display(info.get("closed_date")) if estado_api == "closed" else "Em andamento"
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
                file=output_file,
            )
        print(file=output_file)

    print("\n---\n", file=output_file)

    # ----------------------------------------------------
    # Seção 6: Detalhamento dos Lançamentos Individuais
    # ----------------------------------------------------
    print("## 6. Detalhamento dos Lançamentos Individuais\n", file=output_file)
    print(
        "Registros diários individuais extraídos dos arquivos CSV versionados em `assets/dados/gestao/horas/`.\n",
        file=output_file,
    )

    for arquivo, membro in INTEGRANTES.items():
        print(
            f"### [{membro['nome']}]({URL_COMMITS}{membro['github']}) - {membro['matricula']}\n",
            file=output_file,
        )
        print("| Data | Horas | Atividade / Issue |", file=output_file)
        print("| :-: | :-: | :--- |", file=output_file)

        linhas = membro_dados.get(arquivo, [])
        if not linhas:
            print("| - | 0.00 h | Nenhum lançamento registrado |", file=output_file)
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

                print(f"| {data_formatada} | {row['horas']:.2f} h | {issue_link} |", file=output_file)

        print(file=output_file)


def is_docs_build_active():
    """Detecta se o script está sendo executado pelo plugin de build (ProperDocs ou MkDocs)."""
    if HAS_MKDOCS_GEN_FILES:
        try:
            import mkdocs_gen_files.editor
            if getattr(mkdocs_gen_files.editor.FilesEditor, "_current", None) is not None:
                return True
        except Exception:
            pass
    return any(tool in arg for arg in sys.argv[:2] for tool in ["properdocs", "mkdocs"])


def main():
    parser = argparse.ArgumentParser(description="Consolida medições do Plano de Medição (PSM/CID).")
    parser.add_argument("--data", dest="data_corte", help="Data de corte no formato AAAA-MM-DD", default=None)
    parser.add_argument("--out", dest="out_path", help="Caminho de saída para o markdown gerado", default=None)
    args, unknown = parser.parse_known_args()

    dt_corte = parse_date_string(args.data_corte) if args.data_corte else None
    metrics = consolidate_metrics(data_corte=dt_corte)

    in_docs_build = is_docs_build_active()

    if in_docs_build and HAS_MKDOCS_GEN_FILES and not args.out_path:
        # Durante o build do ProperDocs ou MkDocs: gera apenas o arquivo virtual em memória
        with mkdocs_gen_files.open("gestao/horas_consolidadas.md", "w") as f:
            render_markdown(metrics, f)
    else:
        # Apenas quando executado manualmente fora do build (ex: CLI scripts/coletar_psm.py)
        out_file = args.out_path or "docs/gestao/horas_consolidadas.md"
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        with open(out_file, "w", encoding="utf-8") as f:
            render_markdown(metrics, f)

        # Resumo executivo no terminal
        print("\n" + "=" * 65)
        print("         PAINEL CONSOLIDADO DE MEDIÇÃO PSM/CID")
        print("=" * 65)
        print(f"Data de corte: {format_date_display(metrics['data_corte'])}")
        print(f"CP1 (Progresso Planejado):    {metrics['cp1_str']:>8} | Situação: {metrics['cp1_status']}")
        print(f"CP2 (Cumprimento do Prazo):   {metrics['cp2_str']:>8} | Situação: {metrics['cp2_status']}")
        print(f"DP1 (Taxa de Retrabalho):      {metrics['dp1_str']:>8} | Situação: {metrics['dp1_status']}")
        print(f"DP2 (Critérios Fracos Qcic):  {metrics['dp2_qcic_str']:>8} | Situação: {metrics['qcic_status']}")
        print(f"DP2 (Critérios Adequados PCa):{metrics['dp2_pca_str']:>8} | Situação: {metrics['pca_status']}")
        print(f"RC1 (Esforço Total Equipe):  {metrics['esforco_total']:>7.2f}h | Média/membro: {metrics['media_por_membro']:.2f}h")
        print(f"RC2 (Variação Estimativa):    {metrics['ve_str']:>8} | Situação: {metrics['ve_status']}")
        print(f"Pa  (Cobertura de Dados):     {metrics['pa_cobertura']:>7.1f}% | Situação: {metrics['pa_status']}")
        print("=" * 65)
        print(f"Artefato gerado com sucesso em: {out_file}\n")


if __name__ in ("__main__", "<run_path>") or is_docs_build_active():
    main()
