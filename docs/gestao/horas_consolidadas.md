# Painel Consolidado de Medição PSM/CID e Registro de Horas

Este artefato consolida a medição contínua do projeto integrando os modelos **PSM (Practical Software Measurement)** e a norma **ISO/IEC/IEEE 15939:2017**, conforme estabelecido no [Plano de Medição](plano_de_medicao.md) e no [Procedimento de Medição](medicoes.md). Os dados de progresso e esforço são sincronizados automaticamente com as issues do GitHub e com os registros diários de horas em CSV.

**Data de referência da consolidação:** 02/11/2026

---

## 1. Painel Geral de Indicadores PSM/CID

Síntese executiva de todas as medidas das três categorias do plano. A coloração de cada linha reflete o nível operacional atingido pelo indicador (Verde: Adequado/Bom; Amarelo: Insuficiente/Com ressalva; Vermelho: Crítico). Para justificativas e regras de decisão, consulte as seções correspondentes do [Plano de Medição](plano_de_medicao.md).

<table class="table table-bordered">
<thead>
<tr>
  <th>Categoria</th>
  <th>Indicador</th>
  <th>Medida Base / Fórmula</th>
  <th style="text-align: center;">Valor</th>
  <th style="text-align: center;">Meta / Referência</th>
  <th style="text-align: center;">Situação Operacional</th>
</tr>
</thead>
<tbody>
<tr class="success">
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>Calendário e Progresso</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>CP1: Progresso do Planejado</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><span class="arithmatex">\(Ppp = (Ac \div Ap) \times 100\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><strong>100.0%</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><span class="arithmatex">\(\ge 90\%\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;">Adequado (≥ 90%)</td>
</tr>
<tr class="success">
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>Calendário e Progresso</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>CP2: Cumprimento do Prazo</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><span class="arithmatex">\(Pacp = (Acp \div Ac) \times 100\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><strong>100.0%</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><span class="arithmatex">\(\ge 90\%\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;">Adequado (≥ 90%)</td>
</tr>
<tr class="warning">
  <td style="background-color: #fcf8e3 !important; color: #66512c !important;"><strong>Desempenho dos Processos</strong></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important;"><strong>DP1: Eficiência (Retrabalho)</strong></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important;"><span class="arithmatex">\(Pri = [(Ir \cup Ic) \div If] \times 100\)</span></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important; text-align: center;"><strong>46.2%</strong></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important; text-align: center;"><span class="arithmatex">\(\le 15\%\)</span></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important; text-align: center;">Insuficiente (35% a 50%)</td>
</tr>
<tr class="success">
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>Desempenho dos Processos</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>DP2: Critérios Fracos</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><span class="arithmatex">\(Qcic = Ci + Cc\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><strong>0</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><span class="arithmatex">\(\le 0\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;">Adequado (≤ 0)</td>
</tr>
<tr class="success">
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>Desempenho dos Processos</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>DP2: Critérios Adequados</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><span class="arithmatex">\(PCa = (Ca \div Ct) \times 100\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><strong>100.0%</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><span class="arithmatex">\(\ge 90\%\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;">Adequado (≥ 90%)</td>
</tr>
<tr class="">
  <td style="background-color: #ffffff !important; color: #333333 !important;"><strong>Recursos e Custos</strong></td>
  <td style="background-color: #ffffff !important; color: #333333 !important;"><strong>RC1: Esforço Total</strong></td>
  <td style="background-color: #ffffff !important; color: #333333 !important;"><span class="arithmatex">\(Et = \sum Hr\)</span></td>
  <td style="background-color: #ffffff !important; color: #333333 !important; text-align: center;"><strong>32.00 h</strong></td>
  <td style="background-color: #ffffff !important; color: #333333 !important; text-align: center;">Informativo</td>
  <td style="background-color: #ffffff !important; color: #333333 !important; text-align: center;">Informativo</td>
</tr>
<tr class="">
  <td style="background-color: #ffffff !important; color: #333333 !important;"><strong>Recursos e Custos</strong></td>
  <td style="background-color: #ffffff !important; color: #333333 !important;"><strong>RC1: Média por Membro</strong></td>
  <td style="background-color: #ffffff !important; color: #333333 !important;"><span class="arithmatex">\(Hm = Et \div n\)</span></td>
  <td style="background-color: #ffffff !important; color: #333333 !important; text-align: center;"><strong>5.33 h</strong></td>
  <td style="background-color: #ffffff !important; color: #333333 !important; text-align: center;">Informativo</td>
  <td style="background-color: #ffffff !important; color: #333333 !important; text-align: center;">Informativo</td>
</tr>
<tr class="success">
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>Recursos e Custos</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><strong>RC2: Variação de Estimativa</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important;"><span class="arithmatex">\(Ve = (\lvert Er - Ee \rvert \div Ee) \times 100\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><strong>0.0%</strong></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;"><span class="arithmatex">\(\le 10\%\)</span></td>
  <td style="background-color: #dff0d8 !important; color: #2b542c !important; text-align: center;">Adequado (≤ 10%)</td>
</tr>
<tr class="warning">
  <td style="background-color: #fcf8e3 !important; color: #66512c !important;"><strong>Recursos e Custos</strong></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important;"><strong>Pa: Cobertura de Dados</strong></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important;"><span class="arithmatex">\(Pa = (Ar \div Ac) \times 100\)</span></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important; text-align: center;"><strong>84.6%</strong></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important; text-align: center;"><span class="arithmatex">\(\ge 90\%\)</span></td>
  <td style="background-color: #fcf8e3 !important; color: #66512c !important; text-align: center;">Com ressalva (< 90%)</td>
</tr>
</tbody>
</table>


---

## 2. Calendário e Progresso (CP1 e CP2)

Acompanha o ritmo volumétrico de execução frente ao planejado (**CP1**) e a pontualidade na conclusão em relação à Janela original (**CP2**). Conforme a regra da Seção 4.2 do plano, adiamentos registrados em comentários mantêm a comparação atrelada à linha de base original para garantir a transparência histórica.

- **Atividades concluídas ($Ac$):** 13
- **Atividades planejadas até a data ($Ap$):** 13
- **Atividades concluídas no prazo original ($Acp$):** 13
- **Índice de Progresso ($Ppp$):** 100.0% — Situação: **Adequado (≥ 90%)**
- **Índice de Pontualidade ($Pacp$):** 100.0% — Situação: **Adequado (≥ 90%)**

### Rastreamento de Pontualidade por Issue (CP2)

| Issue | Milestone | Janela Original | Fechamento Real | Pontualidade |
| :--- | :---: | :---: | :---: | :---: |
| [#1 - Setup do repositório, GitPage e registro de gestão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) | Fase 1 | 28/10/2026 | 21/10/2026 | No prazo |
| [#2 - Levantamento do produto e do contexto de uso](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/2) | Fase 1 | 28/10/2026 | 18/10/2026 | No prazo |
| [#3 - Requisitos de avaliação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/3) | Fase 1 | 28/10/2026 | 18/10/2026 | No prazo |
| [#4 - Referencial teórico: primeira versão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/4) | Fase 2 | 28/10/2026 | 24/10/2026 | No prazo |
| [#5 - Escopo, profundidade e objetos de avaliação / ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/5) | Fase 1 | 28/10/2026 | 18/10/2026 | No prazo |
| [#6 - GQM Conceitual e Quantitativo: Objetivos e Métricas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/6) | Fase 2 | 28/10/2026 | 21/10/2026 | No prazo |
| [#7 - Definir questões e hipóteses com critérios de julgamento](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/7) | Fase 2 | 28/10/2026 | 21/10/2026 | No prazo |
| [#12 - Refatoração das métricas de medição PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/12) | Fase 1 | 28/10/2026 | 21/10/2026 | No prazo |
| [#13 - Revisão F1-C1 Propósito da avaliação e uso pretendido e F1-C2 Requisitante e Partes Interessadas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/13) | Fase 1 | 28/10/2026 | 20/10/2026 | No prazo |
| [#14 - Revisão F1-C3 Tipo de produto e descrição estruturada do software e F1-C4 Modelo de qualidade (adaptação + representação gráfica)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/14) | Fase 1 | 28/10/2026 | 21/10/2026 | No prazo |
| [#15 - Revisão F1-C5 Seleção e priorização de características F1-C6 Escopo, profundidade e objetos de avaliação e F1-C7 ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/15) | Fase 1 | 28/10/2026 | 20/10/2026 | No prazo |
| [#16 - Revisão F2-C1 Definição de Objetivo(s) de Medição (Nível Conceitual), F2-C2: Definição de Questões (Nível Operacional) e F2-C3: Definição de Hipóteses (Nível Operacional)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/16) | Fase 2 | 28/10/2026 | 21/10/2026 | No prazo |
| [#17 - Revisão F2-C4: Seleção de Métricas (Nível Quantitativo), F2-C5: Estabelecimento de Níveis de Pontuação e Critérios de Julgamento e F2-C6: Representação da Hierarquia GQM (Gráfico GQM)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/17) | Fase 2 | 28/10/2026 | 21/10/2026 | No prazo |

---

## 3. Desempenho dos Processos (DP1 e DP2)

Avalia a estabilidade do fluxo de trabalho contra retrabalho (**DP1**) e a conformidade das entregas frente à rubrica acadêmica (**DP2**).

### 3.1 Eficiência do Processo e Retrabalho (DP1)

O retrabalho ($Pri$) contabiliza issues reabertas ($Ir$) e issues com label `correcao` ou metadados de retrabalho ($Ic$), divididas pelo total de issues fechadas ($If$). A união previne dupla contagem.

- **Issues fechadas ($If$):** 13
- **Issues identificadas com retrabalho ($Ir \cup Ic$):** 6
- **Percentual de Retrabalho ($Pri$):** 46.2% — Situação: **Insuficiente (35% a 50%)**

| Issue | Título | Origem | Causa Raiz Declarada | Critérios Afetados |
| :---: | :--- | :---: | :--- | :---: |
| [#12](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/12) | Refatoração das métricas de medição PSM/CID | #1 | Ajuste após feedback da professora no ponto de controle 1 | - |
| [#13](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/13) | Revisão F1-C1 Propósito da avaliação e uso pretendido e F1-C2 Requisitante e Partes Interessadas | #2 | Ajuste após feedback da professora no ponto de controle 1 | F1-C1, F1-C2 |
| [#14](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/14) | Revisão F1-C3 Tipo de produto e descrição estruturada do software e F1-C4 Modelo de qualidade (adaptação + representação gráfica) | #3 | Ajuste após feedback da professora no ponto de controle 1 | F1-C1, F1-C2, F1-C3, F1-C4 |
| [#15](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/15) | Revisão F1-C5 Seleção e priorização de características F1-C6 Escopo, profundidade e objetos de avaliação e F1-C7 ODS, metas e indicadores relacionados | #5 | Ajuste após feedback da professora no ponto de controle 1 | F1-C5, F1-C6, F1-C7 |
| [#16](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/16) | Revisão F2-C1 Definição de Objetivo(s) de Medição (Nível Conceitual), F2-C2: Definição de Questões (Nível Operacional) e F2-C3: Definição de Hipóteses (Nível Operacional) | #7 | Ajuste após feedback da professora no ponto de controle 1 | F2-C1, F2-C2, F2-C3 |
| [#17](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/17) | Revisão F2-C4: Seleção de Métricas (Nível Quantitativo), F2-C5: Estabelecimento de Níveis de Pontuação e Critérios de Julgamento e F2-C6: Representação da Hierarquia GQM (Gráfico GQM) | #6 | Ajuste após feedback da professora no ponto de controle 1 | F2-C4, F2-C5, F2-C6 |

### 3.2 Efetividade do Processo e Rubrica Acadêmica (DP2)

Mede a aderência qualitativa das entregas contra a rubrica docente, baseada nas avaliações registradas em `assets/dados/gestao/autoavaliacao.csv`.

- **Critérios avaliados ($Ct$):** 23
- **Distribuição:** Adequado: 23 | Bom: 0 | Insuficiente: 0 | Crítico: 0
- **Critérios Fracos ($Qcic = Ci + Cc$):** 0 — Situação: **Adequado (≤ 0)**
- **Percentual Adequado ($PCa$):** 100.0% — Situação: **Adequado (≥ 90%)**

| Data | Fase | Critério | Nível de Avaliação | Evidência Documentada |
| :---: | :---: | :---: | :---: | :--- |
| 2026-10-26 | Fase 1 | **F1-C1** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/requisitos-de-avaliacao/#proposito-da-avaliacao) |
| 2026-10-26 | Fase 1 | **F1-C2** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/requisitos-de-avaliacao/#partes-interessadas) |
| 2026-10-26 | Fase 1 | **F1-C3** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/produto-e-contexto/) |
| 2026-10-26 | Fase 1 | **F1-C4** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/requisitos-de-avaliacao/#modelo-de-qualidade) |
| 2026-10-26 | Fase 1 | **F1-C5** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/requisitos-de-avaliacao/#caracteristicas-de-qualidade) |
| 2026-10-26 | Fase 1 | **F1-C6** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/escopo-da-avaliacao/) |
| 2026-10-26 | Fase 1 | **F1-C7** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/requisitos-de-avaliacao/#ods-relacionados) |
| 2026-10-26 | Fase 1 | **F1-C8** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-1/) |
| 2026-10-26 | Fase 1 | **F1-C9** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/gestao/artigo/) |
| 2026-10-26 | Fase 1 | **F1-C10** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/gestao/uso_de_ia/) |
| 2026-10-26 | Fase 1 | **F1-C11** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/) |
| 2026-10-26 | Fase 2 | **F2-C1** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/objetivos/) |
| 2026-10-26 | Fase 2 | **F2-C2** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/questoes-hipoteses/) |
| 2026-10-26 | Fase 2 | **F2-C3** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/questoes-hipoteses/#hipoteses) |
| 2026-10-26 | Fase 2 | **F2-C4** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/metricas/) |
| 2026-10-26 | Fase 2 | **F2-C5** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/criterios-julgamento/) |
| 2026-10-26 | Fase 2 | **F2-C6** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/grafico-gqm/) |
| 2026-10-26 | Fase 2 | **F2-C7** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/) |
| 2026-10-26 | Fase 2 | **F2-C8** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/gestao/artigo/) |
| 2026-10-26 | Fase 2 | **F2-C9** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/gestao/uso_de_ia/) |
| 2026-10-26 | Fase 2 | **F2-C10** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/) |
| 2026-10-26 | Fase 2 | **F2-C11** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/objetivos/#alinhamento-com-a-fase-1) |
| 2026-10-26 | Fase 2 | **F2-C12** | Adequado | [Link de Evidência](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_IRMA_MARY_KELLER/fase-2/criterios-julgamento/) |


---

## 4. Recursos e Custos (RC1, RC2 e Pa)

Acompanha o volume de trabalho individual ($Hi$) e o equilíbrio em relação à média da equipe ($Hm$). Conforme a Tabela 8 do Plano de Medição, disparidades superiores a $\pm 50\%$ demandam análise da causa e rebalanceamento das próximas atribuições.

| Integrante | Matrícula | Horas ($Hi$) | Relação ($Hi \div Hm$) | Desvio da Média | Situação de Equilíbrio |
| :--- | :---: | :---: | :---: | :---: | :---: |
| [Camila Silva Cavalcante](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=CamilaSilvaC) | 232013944 | 4.50 h | 0.84 | -15.6% | Equilibrado (dentro de ±50%) |
| [Geovanna Alves Umbelino](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=GeovannaUmbelino) | 232014450 | 7.50 h | 1.41 | +40.6% | Equilibrado (dentro de ±50%) |
| [José Augusto Alves de Moraes](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=JAugustoM) | 231026429 | 5.00 h | 0.94 | -6.2% | Equilibrado (dentro de ±50%) |
| [Luísa de Souza Ferreira](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=luisa12ll) | 232014807 | 2.50 h | 0.47 | -53.1% | Desequilibrado (> ±50%) |
| [Enzo Menali Vettorato Toledo](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=menali17) | 241011054 | 4.50 h | 0.84 | -15.6% | Equilibrado (dentro de ±50%) |
| [Pedro Lucas Barbosa da Silva](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/?author=Pwdrinho) | 241025710 | 8.00 h | 1.50 | +50.0% | Desequilibrado (> ±50%) |

---

## 5. Esforço por Atividade e Estimativas (RC2)

Compara o esforço estimado original ($He$) com o realizado ($Hr$) por atividade, agrupadas por milestone (fase do projeto). Conforme o Plano de Medição, o indicador formal do RC2 incide sobre issues concluídas ($Ac$).

### Fase 1

**Total de horas realizadas:** 20.00 h

| Issue | Estado | Janela Prevista | Conclusão Real | Estimado ($He$) | Realizado ($Hr$) | Desvio ($Hr - He$) | Situação |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [#1 - Setup do repositório, GitPage e registro de gestão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) | Concluída | 28/10/2026 | 21/10/2026 | 4.00 h | 5.50 h | +1.50 h | Insuficiente (> 20%) |
| [#2 - Levantamento do produto e do contexto de uso](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/2) | Concluída | 28/10/2026 | 18/10/2026 | 3.00 h | 3.00 h | +0.00 h | Adequado (≤ 10%) |
| [#3 - Requisitos de avaliação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/3) | Concluída | 28/10/2026 | 18/10/2026 | 2.00 h | 2.00 h | +0.00 h | Adequado (≤ 10%) |
| [#5 - Escopo, profundidade e objetos de avaliação / ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/5) | Concluída | 28/10/2026 | 18/10/2026 | 2.00 h | 1.50 h | -0.50 h | Insuficiente (> 20%) |
| [#12 - Refatoração das métricas de medição PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/12) | Concluída | 28/10/2026 | 21/10/2026 | 3.00 h | 3.50 h | +0.50 h | Bom (10% a 20%) |
| [#13 - Revisão F1-C1 Propósito da avaliação e uso pretendido e F1-C2 Requisitante e Partes Interessadas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/13) | Concluída | 28/10/2026 | 20/10/2026 | 2.00 h | 0.00 h | -2.00 h | Insuficiente (> 20%) |
| [#14 - Revisão F1-C3 Tipo de produto e descrição estruturada do software e F1-C4 Modelo de qualidade (adaptação + representação gráfica)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/14) | Concluída | 28/10/2026 | 21/10/2026 | 2.00 h | 2.50 h | +0.50 h | Insuficiente (> 20%) |
| [#15 - Revisão F1-C5 Seleção e priorização de características F1-C6 Escopo, profundidade e objetos de avaliação e F1-C7 ODS, metas e indicadores relacionados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/15) | Concluída | 28/10/2026 | 20/10/2026 | 2.00 h | 2.00 h | +0.00 h | Adequado (≤ 10%) |

### Fase 2

**Total de horas realizadas:** 12.00 h

| Issue | Estado | Janela Prevista | Conclusão Real | Estimado ($He$) | Realizado ($Hr$) | Desvio ($Hr - He$) | Situação |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [#4 - Referencial teórico: primeira versão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/4) | Concluída | 28/10/2026 | 24/10/2026 | 2.00 h | 0.00 h | -2.00 h | Insuficiente (> 20%) |
| [#6 - GQM Conceitual e Quantitativo: Objetivos e Métricas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/6) | Concluída | 28/10/2026 | 21/10/2026 | 3.00 h | 2.50 h | -0.50 h | Bom (10% a 20%) |
| [#7 - Definir questões e hipóteses com critérios de julgamento](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/7) | Concluída | 28/10/2026 | 21/10/2026 | 3.00 h | 1.50 h | -1.50 h | Insuficiente (> 20%) |
| [#16 - Revisão F2-C1 Definição de Objetivo(s) de Medição (Nível Conceitual), F2-C2: Definição de Questões (Nível Operacional) e F2-C3: Definição de Hipóteses (Nível Operacional)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/16) | Concluída | 28/10/2026 | 21/10/2026 | 2.00 h | 5.50 h | +3.50 h | Insuficiente (> 20%) |
| [#17 - Revisão F2-C4: Seleção de Métricas (Nível Quantitativo), F2-C5: Estabelecimento de Níveis de Pontuação e Critérios de Julgamento e F2-C6: Representação da Hierarquia GQM (Gráfico GQM)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/17) | Concluída | 28/10/2026 | 21/10/2026 | 2.00 h | 2.50 h | +0.50 h | Insuficiente (> 20%) |

### Fase 3

**Total de horas realizadas:** 0.00 h

| Issue | Estado | Janela Prevista | Conclusão Real | Estimado ($He$) | Realizado ($Hr$) | Desvio ($Hr - He$) | Situação |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [#25 - [Fase 3] Definição dos procedimentos de avaliação de desempenho e adaptabilidade](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/25) | Em andamento | - | Em andamento | - | 0.00 h | - | Sem estimativa formal |
| [#26 - [Fase 3] Definição dos procedimentos de avaliação de acessibilidade e apreensibilidade](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/26) | Em andamento | - | Em andamento | - | 0.00 h | - | Sem estimativa formal |
| [#27 - # [Fase 3] Especificação dos recursos, consolidação do Plano de Avaliação e atualização da GitPage](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/27) | Em andamento | - | Em andamento | - | 0.00 h | - | Sem estimativa formal |


---

## 6. Detalhamento dos Lançamentos Individuais

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

