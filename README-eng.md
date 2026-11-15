🇧🇷 [Português](README.md) | 🇺🇸 **English**

<h1 align="center">Khan Academy Quality Evaluation</h1>

<p align="center">
  Performance efficiency, portability and usability of the web platform,<br>
  evaluated with the SQuaRE product evaluation process.
</p>

<p align="center">
  <a href="https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/"><img src="https://img.shields.io/badge/GitHub%20Pages-0B2149?style=for-the-badge&logo=github&logoColor=white" alt="GitPage"></a>
  <a href="https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/gestao/horas_consolidadas/"><img src="https://img.shields.io/badge/PSM%2FCID%20dashboard-1865F2?style=for-the-badge&logo=googleanalytics&logoColor=white" alt="Painel PSM/CID"></a>
  <a href="docs/artigo/QSW_Aval_Qualidade_de_Produto_Khan_Academy_Entrega_1.pdf"><img src="https://img.shields.io/badge/Paper%20PDF-14BF96?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Artigo"></a>
  <a href="https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/actions/workflows/deploy.yml"><img src="https://img.shields.io/github/actions/workflow/status/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/deploy.yml?branch=main&style=for-the-badge&label=deploy&logo=githubactions&logoColor=white" alt="Deploy"></a>
</p>

<p align="center"><sub>FGA0315 Software Quality 1 · UnB FCTE · Class 02 · 2026/2 · Prof. Cristiane Ramos</sub></p>

---

## About

A public school needs to decide whether to recommend Khan Academy to students with limited computers, unstable internet or accessibility needs. Team **Irmã Mary Keller** evaluates the web platform to support that decision: Phase 1 defines what matters and why, and Phase 2 turns it into goals, questions and metrics with the GQM method.

The team's own work is measured too. Every time the site is published, [`consolida_horas.py`](assets/scripts/consolida_horas.py) reads the repository issues, adds up each member's hours and computes the measurement plan indicators on the [PSM/CID dashboard](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/gestao/horas_consolidadas/). No number is typed by hand: to fix a value, fix the issue.

## Installation

**Language:** Python 3.12<br>
**Framework:** ProperDocs (MkDocs) with the Material theme<br>

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export GITHUB_TOKEN=$(gh auth token)
properdocs serve
```

The site opens at http://127.0.0.1:8000/2026-2_T02_IRMA_MARY_KELLER/. The GitHub token avoids the rate limit when reading the issues.

## Usage

1. **Read the evaluation:** the top tabs lead to each phase, and the sidebar lists the pages in order.
2. **Log hours:** each member logs their own hours in the issue's contribution table, one row per day.
3. **Check the dashboard:** it rebuilds itself on every push, whenever an issue changes and every day at 9 a.m.

## Other

```text
docs/               site pages (Phase 1, Phase 2, Management and criteria)
overrides/          theme header and sidebar
assets/scripts/     consolida_horas.py, which builds the PSM/CID dashboard
assets/templates/   dashboard page template
.github/workflows/  automatic deploy to GitHub Pages
```

The site content is written in Portuguese.

---

## Contributors

| [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Enzo Menali](https://github.com/menali17) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [José Augusto](https://github.com/JAugustoM) | [Luísa Ferreira](https://github.com/luisa12ll) | [Pedro Lucas](https://github.com/Pwdrinho) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| <img src="https://github.com/CamilaSilvaC.png" alt="Camila Cavalcante" width="90"> | <img src="https://github.com/menali17.png" alt="Enzo Menali" width="90"> | <img src="https://github.com/GeovannaUmbelino.png" alt="Geovanna Umbelino" width="90"> | <img src="https://github.com/JAugustoM.png" alt="José Augusto" width="90"> | <img src="https://github.com/luisa12ll.png" alt="Luísa Ferreira" width="90"> | <img src="https://github.com/Pwdrinho.png" alt="Pedro Lucas" width="90"> |
