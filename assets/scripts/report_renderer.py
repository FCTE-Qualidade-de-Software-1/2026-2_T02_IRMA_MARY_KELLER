"""
Renderização do relatório consolidado (Markdown) com Jinja2 + tabulate.

- O layout/prosa fica em `assets/templates/horas_consolidadas.md.jinja`.
- Este módulo apenas prepara o contexto (linhas de tabelas, formatações) e renderiza.
"""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from tabulate import tabulate

from .config import INTEGRANTES, URL_COMMITS, URL_ISSUES, format_date_display

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"
TEMPLATE_NAME = "horas_consolidadas.md.jinja"

_CORES = {
    "Verde": ("#dff0d8", "#2b542c", "success"),
    "Amarelo": ("#fcf8e3", "#66512c", "warning"),
    "Vermelho": ("#f2dede", "#843534", "danger"),
}


def _md_table(headers, rows, aligns):
    """Gera tabela Markdown (pipe) com alinhamento por coluna."""
    return tabulate(rows, headers=headers, tablefmt="pipe", colalign=aligns, disable_numparse=True)


def _painel_row(cor, categoria, indicador, formula, valor, meta, situacao):
    bg, fg, cls = _CORES.get(cor, ("#ffffff", "#333333", ""))
    return {
        "cls": cls,
        "bg": bg,
        "fg": fg,
        "categoria": categoria,
        "indicador": indicador,
        "formula": formula,
        "valor": valor,
        "meta": meta,
        "meta_math": meta.startswith("\\"),
        "situacao": situacao,
    }


def _painel(m):
    return [
        _painel_row(m["cp1_cor"], "Calendário e Progresso", "CP1: Progresso do Planejado",
                    "\\(Ppp = (Ac \\div Ap) \\times 100\\)", m["cp1_str"], "\\(\\ge 90\\%\\)", m["cp1_status"]),
        _painel_row(m["cp2_cor"], "Calendário e Progresso", "CP2: Cumprimento do Prazo",
                    "\\(Pacp = (Acp \\div Ac) \\times 100\\)", m["cp2_str"], "\\(\\ge 90\\%\\)", m["cp2_status"]),
        _painel_row(m["dp1_cor"], "Desempenho dos Processos", "DP1: Eficiência (Retrabalho)",
                    "\\(Pri = [(Ir \\cup Ic) \\div If] \\times 100\\)", m["dp1_str"], "\\(\\le 15\\%\\)", m["dp1_status"]),
        _painel_row(m["qcic_cor"], "Desempenho dos Processos", "DP2: Critérios Fracos",
                    "\\(Qcic = Ci + Cc\\)", m["dp2_qcic_str"], "\\(\\le 0\\)", m["qcic_status"]),
        _painel_row(m["pca_cor"], "Desempenho dos Processos", "DP2: Critérios Adequados",
                    "\\(PCa = (Ca \\div Ct) \\times 100\\)", m["dp2_pca_str"], "\\(\\ge 90\\%\\)", m["pca_status"]),
        _painel_row("Informativo", "Recursos e Custos", "RC1: Esforço Total",
                    "\\(Et = \\sum Hr\\)", f"{m['esforco_total']:.2f} h", "Informativo", "Informativo"),
        _painel_row("Informativo", "Recursos e Custos", "RC1: Média por Membro",
                    "\\(Hm = Et \\div n\\)", f"{m['media_por_membro']:.2f} h", "Informativo", "Informativo"),
        _painel_row(m["ve_cor"], "Recursos e Custos", "RC2: Variação de Estimativa",
                    "\\(Ve = (\\lvert Er - Ee \\rvert \\div Ee) \\times 100\\)", m["ve_str"], "\\(\\le 10\\%\\)", m["ve_status"]),
        _painel_row(m["pa_cor"], "Recursos e Custos", "Pa: Cobertura de Dados",
                    "\\(Pa = (Ar \\div Ac) \\times 100\\)", f"{m['pa_cobertura']:.1f}%", "\\(\\ge 90\\%\\)", m["pa_status"]),
    ]


def _issue_link(chave, titulo):
    return f"[#{chave} - {titulo}]({URL_ISSUES}{chave})" if chave.isdigit() else chave


def _tabela_cp2(m):
    issues_api = m["issues_api"]
    rows = []
    for chave in sorted((k for k in issues_api if k.isdigit()), key=int):
        info = issues_api[chave]
        if info["state"] != "closed":
            continue
        jan = (format_date_display(info["janela_date"]) if info["janela_date"]
               else info.get("janela_raw") or "Não definida")
        real = format_date_display(info["closed_date"]) if info["closed_date"] else "Em aberto"
        prazo = m["detalhes_cp2"].get(chave, {}).get("no_prazo")
        pont = "No prazo" if prazo is True else "Atrasada" if prazo is False else "Sem janela formal"
        rows.append([
            _issue_link(chave, info.get("title", f"Issue #{chave}")),
            info.get("milestone") or "Geral", jan, real, pont,
        ])
    return _md_table(
        ["Issue", "Milestone", "Janela Original", "Fechamento Real", "Pontualidade"],
        rows, ("left", "center", "center", "center", "center"),
    )


def _tabela_retrabalho(m):
    rows = []
    for num, info in sorted(m["issues_retrabalho"].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
        rows.append([
            f"[#{num}]({URL_ISSUES}{num})",
            info["title"],
            f"#{info['issue_origem']}" if info.get("issue_origem") else "-",
            info.get("causa_retrabalho") or "Correção/Revisão registrada",
            ", ".join(info.get("criterios", [])) or "-",
        ])
    return _md_table(
        ["Issue", "Título", "Origem", "Causa Raiz Declarada", "Critérios Afetados"],
        rows, ("center", "left", "center", "left", "center"),
    )


def _tabela_autoavaliacao(m):
    rows = []
    for reg in m["autoavaliacao_registros"]:
        ev = reg["evidencia"]
        ev_str = f"[Link de Evidência]({ev})" if ev.startswith("http") else (ev or "-")
        rows.append([reg["data"], reg["fase"], f"**{reg['criterio']}**", reg["nivel"], ev_str])
    return _md_table(
        ["Data", "Fase", "Critério", "Nível de Avaliação", "Evidência Documentada"],
        rows, ("center", "center", "center", "center", "left"),
    )


def _tabela_equilibrio(m):
    media = m["media_por_membro"]
    rows = []
    for arquivo, membro in INTEGRANTES.items():
        hi = m["totais_por_membro"].get(arquivo, 0.0)
        if media > 0:
            desvio = (hi - media) / media * 100
            rel, dev = f"{hi / media:.2f}", f"{desvio:+.1f}%"
            sit = "Equilibrado (dentro de ±50%)" if abs(desvio) <= 50.0 else "Desequilibrado (> ±50%)"
        else:
            rel = dev = "-"
            sit = "Sem dados"
        rows.append([f"[{membro['nome']}]({URL_COMMITS}{membro['github']})",
                     membro["matricula"], f"{hi:.2f} h", rel, dev, sit])
    return _md_table(
        ["Integrante", "Matrícula", "Horas ($Hi$)", "Relação ($Hi \\div Hm$)", "Desvio da Média", "Situação de Equilíbrio"],
        rows, ("left", "center", "center", "center", "center", "center"),
    )


def _situacao_item(he, hr):
    if he is None:
        return "-", "Sem estimativa formal"
    desvio = f"{hr - he:+.2f} h"
    if he <= 0:
        return desvio, "Estimativa zero"
    ve = abs(hr - he) / he * 100
    if ve <= 10.0:
        return desvio, "Adequado (≤ 10%)"
    if ve <= 20.0:
        return desvio, "Bom (10% a 20%)"
    return desvio, "Insuficiente (> 20%)"


def _milestones(m):
    issues_api, totais = m["issues_api"], m["totais_por_issue"]
    chaves = sorted(set(issues_api) | set(totais), key=lambda x: int(x) if x.isdigit() else 9999)
    por_ms = {}
    for chave in chaves:
        por_ms.setdefault(issues_api.get(chave, {}).get("milestone") or "Outras atividades", []).append(chave)

    ordem = {"Fase 1": 1, "Fase 2": 2, "Fase 3": 3, "Fase 4": 4}
    resultado = []
    for nome in sorted(por_ms, key=lambda n: (ordem.get(n, 99), n)):
        rows = []
        for chave in por_ms[nome]:
            info = issues_api.get(chave, {})
            concluida = info.get("state", "aberta") == "closed"
            previsto = (format_date_display(info["janela_date"]) if info.get("janela_date")
                        else info.get("janela_raw") or "-")
            real = format_date_display(info.get("closed_date")) if concluida else "Em andamento"
            he, hr = info.get("estimativa"), totais.get(chave, 0.0)
            desvio, sit = _situacao_item(he, hr)
            rows.append([
                _issue_link(chave, info.get("title", f"Issue #{chave}")),
                "Concluída" if concluida else "Em andamento", previsto, real,
                f"{he:.2f} h" if he is not None else "-", f"{hr:.2f} h", desvio, sit,
            ])
        tabela = _md_table(
            ["Issue", "Estado", "Janela Prevista", "Conclusão Real", "Estimado ($He$)",
             "Realizado ($Hr$)", "Desvio ($Hr - He$)", "Situação"],
            rows, ("left",) + ("center",) * 7,
        )
        resultado.append({"nome": nome, "horas": sum(totais.get(c, 0.0) for c in por_ms[nome]), "tabela": tabela})
    return resultado


def _lancamentos(m):
    issues_api = m["issues_api"]
    resultado = []
    for arquivo, membro in INTEGRANTES.items():
        rows = []
        for row in m["membro_dados"].get(arquivo, []):
            partes = row["data"].split("-")
            data = f"{partes[2]}/{partes[1]}/{partes[0]}" if len(partes) == 3 else row["data"]
            act = row["atividade"]
            if act in issues_api:
                link = f"[Issue #{act}: {issues_api[act]['title']}]({URL_ISSUES}{act})"
            elif act.isdigit():
                link = f"[Issue #{act}]({URL_ISSUES}{act})"
            else:
                link = act or "Não especificada"
            rows.append([data, f"{row['horas']:.2f} h", link])
        if not rows:
            rows = [["-", "0.00 h", "Nenhum lançamento registrado"]]
        resultado.append({
            "titulo": f"[{membro['nome']}]({URL_COMMITS}{membro['github']}) - {membro['matricula']}",
            "tabela": _md_table(["Data", "Horas", "Atividade / Issue"], rows, ("center", "center", "left")),
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
    """Renderiza o relatório consolidado completo e o escreve em `output_file`."""
    m = metrics
    contexto = {
        "m": m,
        "data_corte": format_date_display(m["data_corte"]),
        "painel": _painel(m),
        "tabela_cp2": _tabela_cp2(m),
        "tabela_retrabalho": _tabela_retrabalho(m) if m["issues_retrabalho"] else None,
        "tabela_autoavaliacao": _tabela_autoavaliacao(m) if m["autoavaliacao_registros"] else None,
        "tabela_equilibrio": _tabela_equilibrio(m),
        "milestones": _milestones(m),
        "lancamentos": _lancamentos(m),
    }
    output_file.write(_env.get_template(TEMPLATE_NAME).render(**contexto))
