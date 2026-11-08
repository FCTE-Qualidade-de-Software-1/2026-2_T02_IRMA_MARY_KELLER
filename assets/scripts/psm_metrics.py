"""
Cálculo dos indicadores e métricas do Plano de Medição (PSM/CID):
- CP1: Progresso do Planejado (Ppp)
- CP2: Cumprimento do Prazo (Pacp)
- DP1: Eficiência do Processo e Taxa de Retrabalho (Pri)
- DP2: Efetividade do Processo e Rubrica Acadêmica (Qcic, PCa)
- RC1: Esforço de Desenvolvimento Total e Individual (Et, Hm, Hi)
- RC2: Variação de Estimativa de Esforço (Ve)
- Pa: Cobertura de Dados do Processo (Pa)
"""

import csv
from datetime import datetime
import os
import re

from .config import AUTOAVALIACAO_FILE, INTEGRANTES, TZ_BR


def extract_hours_from_issues(issues_api: dict[str, dict]) -> tuple[dict, dict, dict]:
    """
    Consolida as horas trabalhadas a partir das tabelas de contribuição contidas nas issues.
    Substitui a leitura física de CSVs pela fonte única de verdade nas issues do repositório.

    Retorna:
        - membro_dados: dict com a lista cronológica de lançamentos por integrante
        - totais_por_membro: dict com o total de horas de cada integrante
        - totais_por_issue: dict com o total de horas realizadas por issue
    """
    membro_dados = {chave: [] for chave in INTEGRANTES}
    totais_por_membro = {chave: 0.0 for chave in INTEGRANTES}
    totais_por_issue = {}

    for num, info in issues_api.items():
        tabela = info.get("tabela_contribuicao", [])
        for reg in tabela:
            membro = reg.get("membro")
            data_str = reg.get("data", "")
            horas = reg.get("horas", 0.0)

            if membro in membro_dados:
                membro_dados[membro].append({
                    "data": data_str,
                    "atividade": str(num),
                    "horas": horas,
                })
                totais_por_membro[membro] += horas

            totais_por_issue[str(num)] = totais_por_issue.get(str(num), 0.0) + horas

    # Ordena os lançamentos de cada membro por data
    for chave in membro_dados:
        membro_dados[chave].sort(key=lambda r: r["data"])

    return membro_dados, totais_por_membro, totais_por_issue


def load_autoavaliacao_data(filepath: str = AUTOAVALIACAO_FILE) -> tuple[list, dict]:
    """Carrega as avaliações por critério do arquivo CSV de autoavaliação."""
    registros = []
    contagens = {"Adequado": 0, "Bom": 0, "Insuficiente": 0, "Crítico": 0}

    if not os.path.exists(filepath):
        return registros, contagens

    with open(filepath, "r", encoding="utf-8") as f:
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


def calculate_psm_metrics(
    issues_api: dict[str, dict],
    membro_dados: dict,
    totais_por_membro: dict,
    totais_por_issue: dict,
    autoavaliacao_registros: list,
    autoavaliacao_contagens: dict,
    data_corte=None,
) -> dict:
    """Calcula todos os indicadores das três categorias do Plano de Medição."""
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
    pa_status = "Adequado (≥ 90%)" if pa_cobertura >= 90.0 else "Insuficiente (< 90%)"
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
