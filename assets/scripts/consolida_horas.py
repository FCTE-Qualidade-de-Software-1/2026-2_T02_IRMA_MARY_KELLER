"""
Script de consolidação de medições do Plano de Medição (PSM/CID) e registro de horas.
Executado dinamicamente durante o build do ProperDocs através do plugin gen-files.
"""

import os
import sys

# Garante a resolução dos módulos auxiliares locais
_scripts_dir = os.path.dirname(os.path.abspath(__file__))
_repo_root = os.path.abspath(os.path.join(_scripts_dir, "..", ".."))
for _p in (_repo_root, _scripts_dir):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mkdocs_gen_files

from assets.scripts.github_data import fetch_github_issues
from assets.scripts.psm_metrics import (
    calculate_psm_metrics,
    extract_hours_from_issues,
    load_autoavaliacao_data,
)
from assets.scripts.report_renderer import render_markdown


def main():
    # 1. Coleta e extração dos dados diretamente das issues do GitHub
    issues_api = fetch_github_issues()
    membro_dados, totais_por_membro, totais_por_issue = extract_hours_from_issues(issues_api)
    autoavaliacao_registros, autoavaliacao_contagens = load_autoavaliacao_data()

    # 2. Cálculo dos indicadores do Plano de Medição
    metrics = calculate_psm_metrics(
        issues_api=issues_api,
        membro_dados=membro_dados,
        totais_por_membro=totais_por_membro,
        totais_por_issue=totais_por_issue,
        autoavaliacao_registros=autoavaliacao_registros,
        autoavaliacao_contagens=autoavaliacao_contagens,
    )

    # 3. Escrita virtual em memória para o ProperDocs
    with mkdocs_gen_files.open("gestao/horas_consolidadas.md", "w") as f:
        render_markdown(metrics, f)


main()
