# Registro e Consolidação de Horas

Este artefato consolida as horas trabalhadas pela equipe e acompanha os indicadores de **Recursos e Custos** ([RC1, RC2 e Pa](plano_de_medicao.md#objetivo-3)), integrados às issues do GitHub via API REST conforme as convenções do [Plano de Medição](plano_de_medicao.md). As instruções de lançamento individual estão descritas em [Registro de Horas](horas.md).

---

## 1. Indicadores Consolidados (RC1, RC2 e Pa)

Quadro sintético de controle de esforço. Para interpretação teórica e limiares, consulte a [Seção 3.3 do Plano de Medição](plano_de_medicao.md#objetivo-3).

| Indicador | Medida Base / Fórmula | Valor | Referência | Situação |
| :--- | :--- | :---: | :---: | :---: |
| **RC1: Esforço Total** | $Et = \sum Hr$ | **32.00 h** | Informativo | Informativo |
| **RC1: Média por Integrante** | $Hm = Et \div n$ | **5.33 h** | Informativo | Informativo |
| **RC2: Variação de Estimativa** | $Ve = (\lvert Er - Ee \rvert \div Ee) \times 100$ | **37.5%** | $\le 10\%$ | Insuficiente (> 20%) |
| **Pa: Cobertura de Dados** | $Pa = (Ar \div Ac) \times 100$ | **84.6%** | $\ge 90\%$ | Com ressalva (< 90%) |

---

## 2. Esforço por Integrante (RC1)

Acompanha o volume de trabalho individual ($Hi$) e o equilíbrio em relação à média da equipe ($Hm$). Conforme a [Tabela 8 do Plano de Medição](plano_de_medicao.md#regras), disparidades superiores a $\pm 50\%$ demandam análise da causa e rebalanceamento das próximas atribuições.

| Integrante | Matrícula | Horas ($Hi$) | Relação ($Hi \div Hm$) | Desvio da Média | Situação |
| :--- | :---: | :---: | :---: | :---: | :---: |
| [Camila Silva Cavalcante](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=CamilaSilvaC) | 232013944 | 4.50 h | 0.84 | -15.6% | Equilibrado (dentro de ±50%) |
| [Geovanna Alves Umbelino](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=GeovannaUmbelino) | 232014450 | 7.50 h | 1.41 | +40.6% | Equilibrado (dentro de ±50%) |
| [José Augusto Alves de Moraes](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=JAugustoM) | 231026429 | 5.00 h | 0.94 | -6.2% | Equilibrado (dentro de ±50%) |
| [Luísa de Souza Ferreira](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=luisa12ll) | 232014807 | 2.50 h | 0.47 | -53.1% | Desequilibrado (> ±50%) |
| [Enzo Menali Vettorato Toledo](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=menali17) | 241011054 | 4.50 h | 0.84 | -15.6% | Equilibrado (dentro de ±50%) |
| [Pedro Lucas Barbosa da Silva](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=Pwdrinho) | 241025710 | 8.00 h | 1.50 | +50.0% | Desequilibrado (> ±50%) |

---

## 3. Esforço por Atividade e Estimativas (RC2)

Compara o esforço estimado original ($He$) com o realizado ($Hr$) por atividade. Conforme o [Plano de Medição](plano_de_medicao.md#unidade-de-trabalho), o indicador formal do RC2 incide sobre issues concluídas ($Ac$).

| Issue | Estado | Janela Prevista | Conclusão Real | Estimado ($He$) | Realizado ($Hr$) | Desvio ($Hr - He$) | Situação |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [#1 - Setup do repositório, GitPage e registro de gestão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) | Concluída | 19/10/2026 | 21/10/2026 | 4.00 h | 5.50 h | +1.50 h | Insuficiente (> 20%) |
| [#2 - Levantamento do produto e do contexto de uso](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/2) | Concluída | 16/10/2026 | 18/10/2026 | - | 3.00 h | - | Sem estimativa formal |
| [#3 - Requisitos de avaliação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/3) | Concluída | 16/10/2026 | 18/10/2026 | - | 2.00 h | - | Sem estimativa formal |
| [#4 - Referencial teórico: primeira versão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/4) | Concluída | 16/10/2026 | 24/10/2026 | - | 0.00 h | - | Sem estimativa formal |
| [#5 - Escopo, profundidade e objetos de avaliação / ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/5) | Concluída | 16/10/2026 | 18/10/2026 | - | 1.50 h | - | Sem estimativa formal |
| [#6 - GQM Conceitual e Quantitativo: Objetivos e Métricas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/6) | Concluída | 17/10/2026 | 21/10/2026 | - | 2.50 h | - | Sem estimativa formal |
| [#7 - Definir questões e hipóteses com critérios de julgamento](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/7) | Concluída | 17/10/2026 | 21/10/2026 | - | 1.50 h | - | Sem estimativa formal |
| [#12 - Refatoração das métricas de medição PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/12) | Concluída | 21/10/2026 | 21/10/2026 | - | 3.50 h | - | Sem estimativa formal |
| [#13 - Revisão F1-C1 Propósito da avaliação e uso pretendido e F1-C2 Requisitante e Partes Interessadas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/13) | Concluída | 21/10/2026 | 20/10/2026 | - | 0.00 h | - | Sem estimativa formal |
| [#14 - Revisão F1-C3 Tipo de produto e descrição estruturada do software e F1-C4 Modelo de qualidade (adaptação + representação gráfica)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/14) | Concluída | 21/10/2026 | 21/10/2026 | - | 2.50 h | - | Sem estimativa formal |
| [#15 - Revisão F1-C5 Seleção e priorização de características F1-C6 Escopo, profundidade e objetos de avaliação e F1-C7 ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/15) | Concluída | 21/10/2026 | 20/10/2026 | - | 2.00 h | - | Sem estimativa formal |
| [#16 - Revisão F2-C1 Definição de Objetivo(s) de Medição (Nível Conceitual), F2-C2: Definição de Questões (Nível Operacional) e F2-C3: Definição de Hipóteses (Nível Operacional)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/16) | Concluída | 21/10/2026 | 21/10/2026 | - | 5.50 h | - | Sem estimativa formal |
| [#17 - Revisão F2-C4: Seleção de Métricas (Nível Quantitativo), F2-C5: Estabelecimento de Níveis de Pontuação e Critérios de Julgamento e F2-C6: Representação da Hierarquia GQM (Gráfico GQM)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/17) | Concluída | 21/10/2026 | 21/10/2026 | - | 2.50 h | - | Sem estimativa formal |

---

## 4. Detalhamento dos Lançamentos Individuais

Registros diários individuais extraídos dos arquivos CSV versionados em `assets/dados/gestao/horas/`.

### [Camila Silva Cavalcante](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=CamilaSilvaC) - 232013944

| Data | Horas | Atividade / Issue |
| :-: | :-: | :--- |
| 19/10/2026 | 1.50 h | [Issue #7: Definir questões e hipóteses com critérios de julgamento](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/7) |
| 20/10/2026 | 1.00 h | [Issue #16: Revisão F2-C1 Definição de Objetivo(s) de Medição (Nível Conceitual), F2-C2: Definição de Questões (Nível Operacional) e F2-C3: Definição de Hipóteses (Nível Operacional)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/16) |
| 20/10/2026 | 0.50 h | [Issue #17: Revisão F2-C4: Seleção de Métricas (Nível Quantitativo), F2-C5: Estabelecimento de Níveis de Pontuação e Critérios de Julgamento e F2-C6: Representação da Hierarquia GQM (Gráfico GQM)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/17) |
| 21/10/2026 | 1.50 h | [Issue #16: Revisão F2-C1 Definição de Objetivo(s) de Medição (Nível Conceitual), F2-C2: Definição de Questões (Nível Operacional) e F2-C3: Definição de Hipóteses (Nível Operacional)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/16) |

### [Geovanna Alves Umbelino](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=GeovannaUmbelino) - 232014450

| Data | Horas | Atividade / Issue |
| :-: | :-: | :--- |
| 18/10/2026 | 2.50 h | [Issue #6: GQM Conceitual e Quantitativo: Objetivos e Métricas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/6) |
| 20/10/2026 | 3.00 h | [Issue #16: Revisão F2-C1 Definição de Objetivo(s) de Medição (Nível Conceitual), F2-C2: Definição de Questões (Nível Operacional) e F2-C3: Definição de Hipóteses (Nível Operacional)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/16) |
| 20/10/2026 | 2.00 h | [Issue #17: Revisão F2-C4: Seleção de Métricas (Nível Quantitativo), F2-C5: Estabelecimento de Níveis de Pontuação e Critérios de Julgamento e F2-C6: Representação da Hierarquia GQM (Gráfico GQM)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/17) |

### [José Augusto Alves de Moraes](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=JAugustoM) - 231026429

| Data | Horas | Atividade / Issue |
| :-: | :-: | :--- |
| 18/10/2026 | 1.50 h | [Issue #5: Escopo, profundidade e objetos de avaliação / ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/5) |
| 20/10/2026 | 2.00 h | [Issue #14: Revisão F1-C3 Tipo de produto e descrição estruturada do software e F1-C4 Modelo de qualidade (adaptação + representação gráfica)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/14) |
| 22/10/2026 | 1.50 h | [Issue #12: Refatoração das métricas de medição PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/12) |

### [Luísa de Souza Ferreira](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=luisa12ll) - 232014807

| Data | Horas | Atividade / Issue |
| :-: | :-: | :--- |
| 16/10/2026 | 0.50 h | [Issue #3: Requisitos de avaliação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/3) |
| 17/10/2026 | 1.50 h | [Issue #3: Requisitos de avaliação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/3) |
| 20/10/2026 | 0.50 h | [Issue #15: Revisão F1-C5 Seleção e priorização de características F1-C6 Escopo, profundidade e objetos de avaliação e F1-C7 ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/15) |

### [Enzo Menali Vettorato Toledo](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=menali17) - 241011054

| Data | Horas | Atividade / Issue |
| :-: | :-: | :--- |
| 18/10/2026 | 3.00 h | [Issue #2: Levantamento do produto e do contexto de uso](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/2) |
| 20/10/2026 | 1.50 h | [Issue #15: Revisão F1-C5 Seleção e priorização de características F1-C6 Escopo, profundidade e objetos de avaliação e F1-C7 ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/15) |

### [Pedro Lucas Barbosa da Silva](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=Pwdrinho) - 241025710

| Data | Horas | Atividade / Issue |
| :-: | :-: | :--- |
| 14/10/2026 | 0.50 h | [Issue #1: Setup do repositório, GitPage e registro de gestão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) |
| 15/10/2026 | 3.00 h | [Issue #1: Setup do repositório, GitPage e registro de gestão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) |
| 16/10/2026 | 2.00 h | [Issue #1: Setup do repositório, GitPage e registro de gestão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) |
| 20/10/2026 | 0.50 h | [Issue #14: Revisão F1-C3 Tipo de produto e descrição estruturada do software e F1-C4 Modelo de qualidade (adaptação + representação gráfica)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/14) |
| 21/10/2026 | 2.00 h | [Issue #12: Refatoração das métricas de medição PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/12) |

