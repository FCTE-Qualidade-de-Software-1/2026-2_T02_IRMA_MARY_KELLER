"""
Renderização do painel PSM/CID (Markdown com blocos HTML) com Jinja2 + tabulate.

- O layout/prosa fica em `assets/templates/horas_consolidadas.md.jinja`.
- Este módulo apenas prepara o contexto (indicadores, tabelas, gráficos e conferências) e renderiza.
"""

from datetime import datetime
from html import escape
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from tabulate import tabulate

from .config import INTEGRANTES, TZ_BR, URL_COMMITS, URL_ISSUES, format_date_display
from .graficos import AZUL, AZUL_CLARO, barras_agrupadas, barras_horizontais_com_media

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"
TEMPLATE_NAME = "horas_consolidadas.md.jinja"

TOLERANCIA_EQUILIBRIO = 0.5
ORDEM_DAS_FASES = {"Fase 1": 1, "Fase 2": 2, "Fase 3": 3, "Fase 4": 4}

NIVEIS = {
    "adequado": "Adequado",
    "bom": "Bom",
    "insuficiente": "Insuficiente",
    "crítico": "Crítico",
    "com ressalva": "Com ressalva",
    "informativo": "Informativo",
}

CLASSE_DO_NIVEL = {
    "Adequado": "adequado",
    "Bom": "bom",
    "Insuficiente": "insuficiente",
    "Com ressalva": "insuficiente",
    "Crítico": "critico",
    "Informativo": "informativo",
}


def _num(valor: float, casas: int = 1) -> str:
    return f"{valor:.{casas}f}".replace(".", ",")


def _horas(valor: float) -> str:
    return f"{_num(valor, 2)}\u00a0h"


def _nivel(status: str) -> str:
    status_minusculo = (status or "").lower()
    for prefixo, nome in NIVEIS.items():
        if status_minusculo.startswith(prefixo):
            return nome
    return "Sem dados"


def _selo(status: str, rotulo: str | None = None) -> str:
    nivel = _nivel(status)
    classe = CLASSE_DO_NIVEL.get(nivel, "sem-dados")
    return f'<span class="nivel nivel--{classe}" title="{escape(status or nivel)}">{rotulo or nivel}</span>'


def _md_table(headers, rows, aligns):
    return tabulate(rows, headers=headers, tablefmt="pipe", colalign=aligns, disable_numparse=True)


def _issue_link(chave, titulo):
    return f"[#{chave} {escape(titulo.lstrip('# ').strip())}]({URL_ISSUES}{chave})" if chave.isdigit() else chave


def _linha_painel(categoria, indicador, formula, valor, meta, situacao):
    return {"categoria": categoria, "indicador": indicador, "formula": formula, "valor": valor,
            "meta": meta, "meta_math": meta.startswith("\\"), "situacao": situacao}


def _painel(m):
    return [
        _linha_painel("Calendário e Progresso", "CP1: Progresso do Planejado",
                      "\\(Ppp = (Ac \\div Ap) \\times 100\\)", m["cp1_str"], "\\(\\ge 90\\%\\)", m["cp1_status"]),
        _linha_painel("Calendário e Progresso", "CP2: Cumprimento do Prazo",
                      "\\(Pacp = (Acp \\div Ac) \\times 100\\)", m["cp2_str"], "\\(\\ge 90\\%\\)", m["cp2_status"]),
        _linha_painel("Desempenho dos Processos", "DP1: Eficiência (Retrabalho)",
                      "\\(Pri = [(Ir \\cup Ic) \\div If] \\times 100\\)", m["dp1_str"], "\\(\\le 15\\%\\)", m["dp1_status"]),
        _linha_painel("Desempenho dos Processos", "DP2: Critérios Fracos",
                      "\\(Qcic = Ci + Cc\\)", m["dp2_qcic_str"], "\\(\\le 0\\)", m["qcic_status"]),
        _linha_painel("Desempenho dos Processos", "DP2: Critérios Adequados",
                      "\\(PCa = (Ca \\div Ct) \\times 100\\)", m["dp2_pca_str"], "\\(\\ge 90\\%\\)", m["pca_status"]),
        _linha_painel("Recursos e Custos", "RC1: Esforço Total",
                      "\\(Et = \\sum Hr\\)", _horas(m["esforco_total"]), "Informativo", "Informativo"),
        _linha_painel("Recursos e Custos", "RC1: Média por Membro",
                      "\\(Hm = Et \\div n\\)", _horas(m["media_por_membro"]), "Informativo", "Informativo"),
        _linha_painel("Recursos e Custos", "RC2: Variação de Estimativa",
                      "\\(Ve = (\\lvert Er - Ee \\rvert \\div Ee) \\times 100\\)", m["ve_str"], "\\(\\le 10\\%\\)", m["ve_status"]),
        _linha_painel("Recursos e Custos", "Pa: Cobertura de Dados",
                      "\\(Pa = (Ar \\div Ac) \\times 100\\)", f"{_num(m['pa_cobertura'])}%", "\\(\\ge 90\\%\\)", m["pa_status"]),
    ]


def _fases_ordenadas(nomes):
    return sorted(nomes, key=lambda nome: (ORDEM_DAS_FASES.get(nome, 99), nome))


def _progresso_por_fase(m):
    data_corte = m["data_corte"]
    por_fase = {}
    for info in m["issues_api"].values():
        fase = info.get("milestone") or "Outras atividades"
        contagem = por_fase.setdefault(fase, {"planejadas": 0, "concluidas": 0, "total": 0})
        contagem["total"] += 1
        if info["janela_date"] is not None and info["janela_date"] <= data_corte:
            contagem["planejadas"] += 1
        if info["state"] == "closed":
            contagem["concluidas"] += 1
    return [(fase, por_fase[fase]) for fase in _fases_ordenadas(por_fase)]


def _grafico_progresso(m):
    fases = _progresso_por_fase(m)
    return barras_agrupadas(
        "Issues planejadas até a data e concluídas por fase",
        [fase for fase, _ in fases],
        [
            ("Planejadas até a data (Ap)", AZUL_CLARO, [float(c["planejadas"]) for _, c in fases]),
            ("Concluídas (Ac)", AZUL, [float(c["concluidas"]) for _, c in fases]),
        ],
    )


def _tabela_cp2(m):
    issues_api = m["issues_api"]
    rows = []
    for chave in sorted((k for k in issues_api if k.isdigit()), key=int):
        info = issues_api[chave]
        if info["state"] != "closed":
            continue
        janela = (format_date_display(info["janela_date"]) if info["janela_date"]
                  else info.get("janela_raw") or "Não definida")
        fechamento = format_date_display(info["closed_date"]) if info["closed_date"] else "Em aberto"
        no_prazo = m["detalhes_cp2"].get(chave, {}).get("no_prazo")
        if no_prazo is True:
            pontualidade = "No prazo"
        elif no_prazo is False:
            pontualidade = "**Atrasada**"
        else:
            pontualidade = "Sem Janela"
        rows.append([_issue_link(chave, info.get("title", f"Issue #{chave}")),
                     (info.get("milestone") or "Geral").replace(" ", "\u00a0"), janela, fechamento, pontualidade])
    return _md_table(["Issue", "Fase", "Janela original", "Fechamento", "Pontualidade"],
                     rows, ("left", "center", "center", "center", "center"))


def _issues_com_janela_vencida(m):
    data_corte = m["data_corte"]
    vencidas = []
    for chave, info in m["issues_api"].items():
        if info["state"] != "closed" and info["janela_date"] and info["janela_date"] < data_corte:
            atraso = (data_corte - info["janela_date"]).days
            vencidas.append((info["janela_date"], chave, info, atraso))
    vencidas.sort()
    return [
        f"{_issue_link(chave, info.get('title', ''))}: Janela em {format_date_display(janela)}, "
        f"{atraso} dia{'s' if atraso != 1 else ''} de atraso"
        for janela, chave, info, atraso in vencidas
    ]


def _tabela_retrabalho(m):
    rows = []
    for num, info in sorted(m["issues_retrabalho"].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
        rows.append([
            f"[#{num}]({URL_ISSUES}{num})",
            info["title"],
            f"#{info['issue_origem']}" if info.get("issue_origem") else "-",
            info.get("causa_retrabalho") or "Correção ou revisão registrada",
            ", ".join(info.get("criterios", [])) or "-",
        ])
    return _md_table(["Issue", "Título", "Origem", "Causa declarada", "Critérios afetados"],
                     rows, ("center", "left", "center", "left", "center"))


def _tabela_autoavaliacao(m):
    rows = []
    for reg in m["autoavaliacao_registros"]:
        evidencia = reg["evidencia"]
        evidencia_md = f"[Evidência]({evidencia})" if evidencia.startswith("http") else (evidencia or "-")
        rows.append([format_date_display(_data_iso(reg["data"])) if reg["data"] else "-", reg["fase"],
                     f"`{reg['criterio']}`", _nivel(reg["nivel"]), evidencia_md])
    return _md_table(["Data", "Fase", "Critério", "Nível", "Evidência"],
                     rows, ("center", "center", "center", "center", "left"))


def _data_iso(texto: str):
    try:
        return datetime.strptime(texto, "%Y-%m-%d").date()
    except ValueError:
        return None


def _situacao_equilibrio(horas_integrante: float, media: float) -> tuple[str, str, str]:
    if media <= 0:
        return "-", "-", "Sem dados"
    desvio = (horas_integrante - media) / media * 100
    situacao = ("Equilibrado"
                if abs(desvio) <= TOLERANCIA_EQUILIBRIO * 100
                else "**Fora da faixa**")
    return _num(horas_integrante / media, 2), f"{'+' if desvio >= 0 else ''}{_num(desvio)}%", situacao


def _tabela_equilibrio(m):
    media = m["media_por_membro"]
    rows = []
    for chave, membro in INTEGRANTES.items():
        horas_integrante = m["totais_por_membro"].get(chave, 0.0)
        relacao, desvio, situacao = _situacao_equilibrio(horas_integrante, media)
        rows.append([f"[{membro['nome']}]({URL_COMMITS}{membro['github']})", membro["matricula"],
                     _horas(horas_integrante), relacao, desvio, situacao])
    return _md_table(["Integrante", "Matrícula", "Horas (Hi)", "Hi ÷ Hm", "Desvio da média", "Situação"],
                     rows, ("left", "center", "center", "center", "center", "center"))


def _grafico_equilibrio(m):
    return barras_horizontais_com_media(
        "Horas registradas por integrante, com a média da equipe e a faixa de 50%",
        [membro["apelido"] for membro in INTEGRANTES.values()],
        [m["totais_por_membro"].get(chave, 0.0) for chave in INTEGRANTES],
        m["media_por_membro"],
        TOLERANCIA_EQUILIBRIO,
    )


def _estimado_realizado_por_fase(m):
    totais = m["totais_por_issue"]
    por_fase = {}
    for chave, info in m["issues_api"].items():
        if info["state"] != "closed" or not info.get("estimativa"):
            continue
        fase = info.get("milestone") or "Outras atividades"
        soma = por_fase.setdefault(fase, {"estimado": 0.0, "realizado": 0.0})
        soma["estimado"] += info["estimativa"]
        soma["realizado"] += totais.get(chave, 0.0)
    return [(fase, por_fase[fase]) for fase in _fases_ordenadas(por_fase)]


def _grafico_estimativa(m):
    fases = _estimado_realizado_por_fase(m)
    if not fases:
        return ""
    return barras_agrupadas(
        "Horas estimadas e realizadas nas issues concluídas, por fase",
        [fase for fase, _ in fases],
        [
            ("Estimado (Ee)", AZUL_CLARO, [soma["estimado"] for _, soma in fases]),
            ("Realizado (Er)", AZUL, [soma["realizado"] for _, soma in fases]),
        ],
        unidade=" h",
    )


def _situacao_item(he, hr):
    if he is None:
        return "-", "Sem estimativa"
    desvio = f"{'+' if hr - he >= 0 else ''}{_horas(hr - he)}"
    if he <= 0:
        return desvio, "Estimativa zero"
    variacao = abs(hr - he) / he * 100
    if variacao <= 10.0:
        return desvio, "Adequado"
    if variacao <= 20.0:
        return desvio, "Bom"
    return desvio, "**Insuficiente**"


def _milestones(m):
    issues_api, totais = m["issues_api"], m["totais_por_issue"]
    chaves = sorted(set(issues_api) | set(totais), key=lambda x: int(x) if x.isdigit() else 9999)
    por_fase = {}
    for chave in chaves:
        por_fase.setdefault(issues_api.get(chave, {}).get("milestone") or "Outras atividades", []).append(chave)

    resultado = []
    for nome in _fases_ordenadas(por_fase):
        rows = []
        for chave in por_fase[nome]:
            info = issues_api.get(chave, {})
            concluida = info.get("state", "open") == "closed"
            previsto = (format_date_display(info["janela_date"]) if info.get("janela_date")
                        else info.get("janela_raw") or "-")
            real = format_date_display(info.get("closed_date")) if concluida else "Em andamento"
            he, hr = info.get("estimativa"), totais.get(chave, 0.0)
            desvio, situacao = _situacao_item(he, hr)
            rows.append([
                _issue_link(chave, info.get("title", f"Issue #{chave}")),
                "Concluída" if concluida else "Em andamento", previsto, real,
                _horas(he) if he is not None else "-", _horas(hr), desvio, situacao,
            ])
        tabela = _md_table(
            ["Issue", "Estado", "Janela", "Conclusão", "Estimado (He)", "Realizado (Hr)", "Hr - He", "Situação"],
            rows, ("left",) + ("center",) * 7,
        )
        resultado.append({"nome": nome, "horas": _horas(sum(totais.get(c, 0.0) for c in por_fase[nome])),
                          "quantidade": len(por_fase[nome]), "tabela": tabela})
    return resultado


def _conferencia_por_integrante(m):
    total_equipe = m["esforco_total"]
    rows = []
    for chave, membro in INTEGRANTES.items():
        lancamentos = m["membro_dados"].get(chave, [])
        horas_integrante = m["totais_por_membro"].get(chave, 0.0)
        issues_distintas = {registro["atividade"] for registro in lancamentos}
        dias_distintos = {registro["data"] for registro in lancamentos}
        datas = sorted(dias_distintos)
        periodo = (f"{format_date_display(_data_iso(datas[0]))} a {format_date_display(_data_iso(datas[-1]))}"
                   if datas else "-")
        participacao = f"{_num(horas_integrante / total_equipe * 100, 0)}%" if total_equipe else "-"
        rows.append([membro["apelido"], str(len(lancamentos)), str(len(issues_distintas)), str(len(dias_distintos)),
                     periodo, _horas(horas_integrante), participacao])
    rows.append(["**Total**", str(sum(len(m["membro_dados"].get(c, [])) for c in INTEGRANTES)), "", "", "",
                 f"**{_horas(total_equipe)}**", "100%"])
    return _md_table(["Integrante", "Lançamentos", "Issues", "Dias com registro", "Período", "Horas", "% do total"],
                     rows, ("left", "center", "center", "center", "center", "center", "center"))


def _verificacoes(m):
    issues_api = m["issues_api"]
    fora_da_equipe, repetidos, fora_do_multiplo = [], [], []
    for chave in sorted(issues_api, key=lambda x: int(x) if x.isdigit() else 9999):
        vistos = set()
        for registro in issues_api[chave].get("tabela_contribuicao", []):
            referencia = f"[#{chave}]({URL_ISSUES}{chave})"
            usuario = registro.get("usuario_raw", "").strip() or "sem usuário"
            if registro.get("membro") is None:
                fora_da_equipe.append(f"{referencia}: `{usuario}` em {registro['data']}, {_horas(registro['horas'])}")
            identificador = (registro.get("membro"), registro.get("data"))
            if identificador in vistos:
                repetidos.append(f"{referencia}: `{usuario}` em {registro['data']}")
            vistos.add(identificador)
            if round(registro["horas"] * 4, 6) % 1:
                fora_do_multiplo.append(f"{referencia}: `{usuario}` lançou {_horas(registro['horas'])}")

    concluidas_sem_horas, sem_estimativa, sem_janela = [], [], []
    for chave in sorted((k for k in issues_api if k.isdigit()), key=int):
        info = issues_api[chave]
        link = _issue_link(chave, info.get("title", ""))
        if info["state"] == "closed" and not m["totais_por_issue"].get(chave):
            concluidas_sem_horas.append(link)
        if info.get("estimativa") is None:
            sem_estimativa.append(link)
        if info.get("janela_date") is None:
            sem_janela.append(link)

    soma_por_issue = sum(m["totais_por_issue"].values())
    diferenca = soma_por_issue - m["esforco_total"]
    return [
        {"titulo": "Horas de usuários fora da equipe",
         "explicacao": "Entram na soma por issue (RC2), mas não no esforço por integrante (RC1). "
                       "Corrigir o usuário na Tabela de Contribuição.",
         "itens": fora_da_equipe},
        {"titulo": "Lançamentos repetidos (mesma pessoa, mesma issue, mesmo dia)",
         "explicacao": "A convenção é uma linha por integrante e dia. Conferir se não é o mesmo trabalho contado duas vezes.",
         "itens": repetidos},
        {"titulo": "Horas fora dos múltiplos de 0,25 h",
         "explicacao": "O Registro de horas pede lançamentos em múltiplos de 0,25 h.",
         "itens": fora_do_multiplo},
        {"titulo": "Issues concluídas sem horas registradas",
         "explicacao": "Reduzem a cobertura Pa e deixam RC1 e RC2 com ressalva.",
         "itens": concluidas_sem_horas},
        {"titulo": "Issues sem Estimativa",
         "explicacao": "Ficam fora do RC2. Pela seção 4.1 do Plano de medição, devem ser corrigidas antes da próxima medição.",
         "itens": sem_estimativa},
        {"titulo": "Issues sem Janela",
         "explicacao": "Ficam fora do CP1 e do CP2. Pela seção 4.1 do Plano de medição, devem ser corrigidas.",
         "itens": sem_janela},
    ], {"soma_por_issue": _horas(soma_por_issue), "soma_por_integrante": _horas(m["esforco_total"]),
        "diferenca": _horas(diferenca), "confere": abs(diferenca) < 0.01}


def _lancamentos(m):
    issues_api = m["issues_api"]
    resultado = []
    for chave, membro in INTEGRANTES.items():
        rows = []
        for registro in m["membro_dados"].get(chave, []):
            atividade = registro["atividade"]
            if atividade in issues_api:
                link = _issue_link(atividade, issues_api[atividade]["title"])
            elif atividade.isdigit():
                link = f"[Issue #{atividade}]({URL_ISSUES}{atividade})"
            else:
                link = atividade or "Não especificada"
            rows.append([format_date_display(_data_iso(registro["data"])) if _data_iso(registro["data"])
                         else registro["data"], _horas(registro["horas"]), link])
        if not rows:
            rows = [["-", _horas(0), "Nenhum lançamento registrado"]]
        resultado.append({
            "titulo": f"{membro['nome']} ({membro['matricula']}): {_horas(m['totais_por_membro'].get(chave, 0.0))}",
            "tabela": _md_table(["Data", "Horas", "Issue"], rows, ("center", "center", "left")),
        })
    return resultado


_env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    undefined=StrictUndefined,
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
)


def render_markdown(metrics: dict, output_file) -> None:
    """Renderiza o painel completo e o escreve em `output_file`."""
    m = metrics
    verificacoes, somas = _verificacoes(m)
    total_lancamentos = sum(len(info.get("tabela_contribuicao", [])) for info in m["issues_api"].values())
    contexto = {
        "m": m,
        "atualizado_em": datetime.now(TZ_BR).strftime("%d/%m/%Y às %H:%M"),
        "total_issues": len(m["issues_api"]),
        "total_lancamentos": total_lancamentos,
        "painel": _painel(m),
        "selo": _selo,
        "num": _num,
        "horas": _horas,
        "grafico_progresso": _grafico_progresso(m),
        "tabela_cp2": _tabela_cp2(m),
        "janelas_vencidas": _issues_com_janela_vencida(m),
        "tabela_retrabalho": _tabela_retrabalho(m) if m["issues_retrabalho"] else None,
        "tabela_autoavaliacao": _tabela_autoavaliacao(m) if m["autoavaliacao_registros"] else None,
        "grafico_equilibrio": _grafico_equilibrio(m),
        "tabela_equilibrio": _tabela_equilibrio(m),
        "grafico_estimativa": _grafico_estimativa(m),
        "milestones": _milestones(m),
        "conferencia_integrantes": _conferencia_por_integrante(m),
        "verificacoes": verificacoes,
        "somas": somas,
        "lancamentos": _lancamentos(m),
    }
    output_file.write(_env.get_template(TEMPLATE_NAME).render(**contexto))
