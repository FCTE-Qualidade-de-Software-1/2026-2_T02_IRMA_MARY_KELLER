# Plano de medição PSM/CID

Versão 1.6

---

## 1. Finalidade

Este artefato estabelece o Plano de Medição do projeto de avaliação de qualidade de software, integrando as diretrizes do modelo *Practical Software and Systems Measurement* (PSM) [S1](#s1), [S3](#s3), [S4](#s4) e a norma *ISO/IEC/IEEE 15939:2017* [S2](#s2). O objetivo é acompanhar a execução do projeto ao longo dos marcos principais: **Entrega 1** (26/10/2026) e **Entrega 2** (18/11/2026), além dos pontos de controle **PC1** (19 a 21/10/2026) e **PC2** (04 a 09/11/2026). A medição atua como um sistema de controle por realimentação (*feedback control system*) [S1](#s1), [S2](#s2), estruturado em três categorias essenciais: [**Calendário e Progresso**](#31-calendário-e-progresso), [**Desempenho dos Processos**](#32-desempenho-dos-processos) e [**Recursos e Custos**](#33-recursos-e-custos). Cada medição realizada é registrada com sua interpretação técnica e com as [decisões corretivas e preventivas](#6-regras-de-decisão) de gestão provocadas pelos indicadores.

## 2. Necessidades de informação

Em conformidade com a abordagem *Goal Question Metric* (GQM) [S5](#s5) e os princípios do PSM [S1](#s1), [S3](#s3), a medição deriva de necessidades concretas de informação, e não da disponibilidade fortuita de dados. Cada objetivo de medição (**O1** a **O3**) apresentados na Tabela 1, vincula-se a uma categoria e a uma pergunta orientadora de gestão que serve de guia para escolher as medidas da [seção 3](#3-medidas-e-indicadores-por-categoria).

| Objetivo | Categoria | Pergunta orientadora de gestão |
|---|---|---|
| [O1](#objetivo-1) | Calendário e Progresso | Vamos entregar os slides do Pontos de Controle e a Entregas no ritmo planejado? |
| [O2](#objetivo-2) | Desempenho dos Processos | O processo de produzir e revisar gera entregas que atendem aos critérios da professora, sem muito retrabalho? |
| [O3](#objetivo-3) | Recursos e Custos | O esforço gasto confere com o planejado e está equilibrado entre os membros? |

*Tabela 1. Necessidades de informação por objetivo de medição. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

## 3. Medidas e indicadores por categoria

Esta seção detalha como cada objetivo de medição será respondido. A estrutura operacional segue a cadeia analítica da ISO/IEC/IEEE 15939 [S2](#s2): mapeamento do **Atributo**, definição das **Medidas Base (QME)**, cálculo da **Medida Derivada**, aplicação da **Fórmula** e enquadramento no **Indicador** de julgamento. 

A seção se divide em três subseções, uma por categoria do PSM/CID: [3.1 Calendário e Progresso (O1)](#31-calendário-e-progresso), [3.2 Desempenho dos Processos (O2)](#32-desempenho-dos-processos) e [3.3 Recursos e Custos (O3)](#33-recursos-e-custos). Os termos usados nas fórmulas são definidos na [seção 4](#unidade-de-trabalho) e a justificativa teóricas e operacionais das medidas encontram-se na [seção 5](#justificativa).

### 3.1 Calendário e Progresso

Mede o ritmo de execução volumétrico (`CP1`) e a pontualidade em relação à linha de base original de cronograma (`CP2`) [S3](#s3), que podem ser observados na Tabela 2.

<a id="objetivo-1"></a>

#### O1: verificar se a equipe está concluindo as atividades planejadas dentro do prazo.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Progresso das atividades (`CP1`) | [Atividades](#unidade-de-trabalho) concluídas (`Ac`) <br> [Atividades](#unidade-de-trabalho) planejadas (`Ap`) | Percentual de Progresso do Planejado. (`Ppp`) | `Ppp = (Ac ÷ Ap) × 100`	|Adequado: `Ppp ≥ 90%` <br> Bom: `80% ≤ Ppp < 90%` <br> Insuficiente: `60% ≤ Ppp < 80%` <br> Crítico: `Ppp < 60%` |
| Cumprimento do prazo (`CP2`) | [Atividades](#unidade-de-trabalho) concluídas no prazo (`Acp`) <br> [Atividades](#unidade-de-trabalho) concluídas (`Ac`) | Percentual de Atividades Concluídas no Prazo (`Pacp`) | `Pacp = (Acp ÷ Ac) × 100` | Adequado: `90% ≤ Pacp ≤ 100%` <br> Bom: `80% ≤ Pacp < 90%` <br> Insuficiente: `60% ≤ Pacp < 80%` <br> Crítico: `Pacp < 60%` |

*Tabela 2. Medidas e indicadores de Calendário e Progresso (O1). Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

### 3.2 Desempenho dos Processos

Avalia a estabilidade técnica do fluxo de trabalho em relação ao retrabalho (`DP1`) e a efetividade das entregas frente à rubrica acadêmica (`DP2`) [S4](#s4), que podem ser observados na Tabela 3.

<a id="objetivo-2"></a>

#### O2: verificar a eficiência, a efetividade e a conformidade dos processos de trabalho da equipe.


| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Eficiência do processo (`DP1`) | Issue reaberta (`Ir`) <br> Issue com label `correcao` (`Ic`) <br> Issue fechada (`If`) | Percentual de Retrabalho em Issues (`Pri`) | `Pri = [(Ir ∪ Ic) ÷ If] × 100` | Adequado: `Pri ≤ 15%` <br> Bom: `15% < Pri ≤ 35%` <br> Insuficiente: `35% < Pri < 50%` <br> Crítico: `Pri ≥ 50%` |
| Efetividade do processo (`DP2`) | Critérios avaliados como {Crítico (`Cc`) <br>  Insuficiente (`Ci`) <br> Bom (`Cb`) <br> Adequado (`Ca`)} <br> Total de critérios avaliados (`Ct`) | Quantidade de Critérios Insuficientes/Críticos (`Qcic`) <br> Percentual Critérios Adequados (`PCa`) | `Qcic = Ci + Cc` <br> `Pce = (Ca ÷ Ct) × 100` | Adequado: `Qcic ≤ 0`  <br> Bom: `1 ≤ Qcic ≤ 2` <br> Insuficiente: `Qcic ≥ 3` <br> Adequado: `90% ≤ PCa ≤ 100%` <br> Bom: `75% ≤ PCa < 90%` <br> Insuficiente: `PCa < 75%` |

*Tabela 3. Medidas e indicadores de Desempenho dos Processos (O2). Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

### 3.3 Recursos e Custos

Trata da alocação do esforço humano da equipe (`RC1`) e da precisão das estimativas de tempo (`RC2`), garantindo o acompanhamento de custos e o equilíbrio da carga de trabalho [S1](#s1), [S3](#s3), que podem ser observados na Tabela 3.

<a id="objetivo-3"></a>

#### O3: monitorar o esforço dedicado ao desenvolvimento do projeto e estimar seu custo com base nas horas trabalhadas.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Esforço de desenvolvimento (`RC1`) | Horas estimadas por atividade (`He`) <br> Horas efetivamente trabalhadas por atividade (`Hr`) | Esforço total realizado (`Et`) | `Et = Σ Hr` | Informativo: registrar o total de horas da equipe e a distribuição por atividade e integrante. |
| Variação do esforço estimado (`RC2`) | Esforço estimado total em concluídas (`Ee`) <br> Esforço realizado total nas mesmas (`Er`) | Variação percentual do esforço (`Ve`) | `Ve = ( |Er − Ee| ÷ Ee ) × 100` | Adequado: `Ve ≤ 10%` <br> Bom: `10% < Ve ≤ 20%` <br> Insuficiente: `Ve > 20%` |

*Tabela 4. Medidas e indicadores de Recursos e Custos (O3). Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

**Procedimento de coleta:** Cada integrante registra as horas dedicadas às atividades em seu arquivo CSV individual. A equipe consolida os registros periodicamente e avalia a estabilidade das estimativas [S1](#s1). Conforme a norma ISO/IEC/IEEE 15939 [S2](#s2), a verificação de presença do registro de horas (taxa de cobertura `Pa ≥ 90%`) atua como pré-condição operacional de qualidade dos dados, garantindo a confiabilidade dos indicadores `RC1` e `RC2`.

## 4. Unidade de trabalho e convenções

Esta seção fixa as regras que tornam as medições repetíveis conforme a norma ISO/IEC/IEEE 15939:2017 [S2](#s2): o que conta como unidade de trabalho, como cada termo das fórmulas é interpretado e como os níveis dos indicadores se traduzem em cores.
 
<a id="unidade-de-trabalho"></a>
 
### 4.1 Unidade de trabalho
 
A unidade de trabalho é a **issue** do GitHub. O corpo da issue traz **Janela** (data prevista de conclusão), **Estimativa** (horas em múltiplos de 0,25 h) e o(s) ID dos critérios (por exemplo, `F1-02`). Uma issue sem ID, sem Janela ou sem Estimativa não entra nas medições de forma confiável e deve ser corrigida antes da próxima medição.
 
### 4.2 Definições operacionais

A Tabela 5 define, de forma operacional, os termos e variáveis utilizados tanto nas fórmulas das medidas da [seção 3](#3-medidas-e-indicadores-por-categoria) quanto nas regras de decisão e governança da [seção 6](#regras) [S2](#s2).
 
| Termo | Definição operacional |
|---|---|
| Planejada até a data (`Ap`) | Issue dos milestones das entregas cuja Janela é igual ou anterior à data da medição. |
| Concluída (`Ac`) | Issue fechada com os critérios de aceite atendidos e com revisão do revisor registrada no pull request. Issue fechada sem revisão não conta como concluída. |
| Concluída no prazo (`Acp`) | Issue concluída em data igual ou anterior à sua **Janela original** |
| Janela original | Valor da Janela no momento da criação da issue. Quando o prazo é revisto, a nova data vai em comentário (`Janela revista`) e serve só ao replanejamento. O `CP2` sempre compara com a original, para que o atraso não desapareça da medição[S3](#s3). |
| Retrabalho (`Ir`, `Ic`) | Issue reaberta depois de fechada (`Ir`) ou issue com a label `correcao` (`Ic`). A união (\`Ir ∪ Ic\`) previne dupla contagem. |
| Estimativa congelada | A Estimativa registrada na criação da issue é a usada no `RC2`. Reestimativas vão em comentário e não sobrescrevem o valor original |
| Esforço realizado (`Hr`, `Hi`) | Horas registradas em `assets/dados/gestao/horas/<usuario>.csv`, em múltiplos de 0,25 h, ligadas ao ID da issue. Em trabalho em dupla, cada integrante lança as próprias horas |
| Escopo do `RC2` | Calculado apenas sobre issues concluídas (`Ee` e `Er` do mesmo conjunto `Ac`), para que issues em andamento não distorçam a comparação. As horas de issues em andamento entram no `RC1` |
| Cobertura de dados (`Pa`) | Porcentagem de atividades concluídas com horas registradas no CSV (`Pa = (Ar ÷ Ac) × 100`). Atua como indicador de higiene dos dados. | 
| Horas sem issue | Atividades sem ID de issue válido reduzem a taxa de cobertura do registro (`Pa`). | 
| Denominador zero | Se `Ap`, `Ac`, `If`, `Ee` ou `Ct` for zero na data, a medida é registrada como "sem dados" e não recebe nível |
 
*Tabela 5. Definições operacionais dos termos usados nas medições. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

### 4.3 Níveis e cores
 
Os indicadores apresentados na Tabela 6 usam níveis de desempenho e cores correspondentes para as regras de decisão [(seção 6)](#regras), cores essas que auxiliam o preenchimento na planilha e nos relatórios de controle.

| Nível | Cor | Significado |
|---|---|---|
| Adequado e Bom | Verde | Sem ação obrigatória; registrar a medição |
| Insuficiente | Amarelo | Ação corretiva conforme a [regras](#regras) |
| Crítico | Vermelho | Ação corretiva imediata conforme a [regras](#regras) |
| Informativo | Sem cor | Apenas registrar e acompanhar |

*Tabela 6. Níveis dos indicadores, cores e significado. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*
 
Nos indicadores que não têm nível Crítico (`DP2`, `RC2` e o equilíbrio do `RC1`), o pior nível possível é Insuficiente (amarelo).
 
<a id="justificativa"></a>

## 5. Justificativa das medições e dos indicadores

Esta seção explica a lógica de escolha das medidas, as adaptações contextuais (*tailoring*) em relação ao modelo PSM/CID tradicional, os fundamentos teóricos de cada indicador e a origem dos limiares operacionais [S1](#s1), [S2](#s2), [S3](#s3), [S4](#s4), [S5](#s5).
 
### 5.1 Lógica de escolha
 
O PSM parte da necessidade de informação, não da medida disponível[S1](#s1),[S5](#s5). Por isso há uma pergunta de gestão para cada categoria [(seção 2)](#2-necessidades-de-informação) e um conjunto pequeno de medidas que a responde diretamente. Foram preferidas medidas que o próprio fluxo de trabalho já produz (issues, pull requests, horas), para que a coleta não vire uma tarefa à parte e possa ser conferida no repositório[S3](#s3).

Para adequar o modelo PSM/CID [S1](#s1), [S3](#s3) e a ISO/IEC/IEEE 15939:2017 [S2](#s2) ao contexto acadêmico, realizaram-se quatro adaptações (\*tailoring\*):

1. **Unidade de Trabalho:** Adotou-se a *issue* do GitHub (com Janela, Estimativa e ID do critério) em vez de pacotes de trabalho ou pontos de função complexos do PSM industrial [S1](#s1), [S3](#s3).
2. **Categoria de Custos:** Substituiu-se o controle financeiro/orçamentário pelo rastreamento do esforço em horas trabalhadas por integrante [S1](#s1), [S3](#s3). 
3. **Origem dos Limiares:** Os limiares foram definidos pela própria equipe como hipóteses operacionais iniciais [S1](#s1), a serem calibradas com dados reais no ponto [Mg-2](medicoes.md#pontos). 
4. **Qualidade do Produto:** Traduziu-se a qualidade por meio da autoavaliação fundamentada em evidências contra a rubrica da disciplina (`DP2`), em vez de medições puramente técnicas de código [S4](#s4).
 
### 5.2 Medidas e indicadores

A Tabela 7 apresenta, para cada medida, a razão da escolha, a fundamentação dos limiares e a limitação a considerar.

| Medida | Por que foi escolhida | Por que este indicador | Limitação a considerar |
|---|---|---|---|
| `CP1` Progresso | Responde ao [O1](#objetivo-1): compara o volume de trabalho entregue até a data com o planejado[S3](#s3). | Faixas de `90/80/60%` são critério da equipe. Abaixo de `60%` o prazo de uma entrega fica ameaçado | Issues possuem portes diferentes. Mitigação: interpretar junto com os valores de `Ac` e `Ap`. |
| `CP2` Prazo | Complementa o `CP1`: avalia se a conclusão ocorreu dentro da linha de base de tempo original [S3](#s3). | Mesmas faixas do `CP1`, por consistência da categoria | Compara com a Janela original <br> Replanejar não "limpa" o atraso, o que é intencional |
| `DP1` Eficiência | Retrabalho (issue reaberta ou corrigida) é um indício direto de instabilidade no processo de elaboração ou revisão [S4](#s4). | Faixas de `15/35/50%` são critério da equipe, mais tolerantes que as de prazo porque revisão faz parte de um trabalho acadêmico normais. Acima de `50%` indica processo ineficaz. | Depende da disciplina de reabrir a issue ou usar a label `correcao`. <br> Retrabalho feito dentro do pull request antes do fechamento não aparece |
| `DP2` Efetividade | Responde à parte do [O2](#objetivo-2), avalia a aderência qualitativa e técnica das entregas frente aos critérios da rubrica acadêmica [S4](#s4). | `Qcic` destaca os critérios mais fracos (gera ação), `Qcic ≤ 0` garante ausência de critérios fracos. <br> `Pce` mede a proximidade do objetivo de alcançar a última opção em cada critério  `PCa ≥ 90%` busca a excelência acadêmica. | Autoavaliação possui subjetividade. <br> Mitigação: exige revisão por pares e evidência no `autoavaliacao.csv` |
| `RC1` Esforço | Base do [O3](#objetivo-3): fornece visibilidade sobre o volume total de trabalho e o equilíbrio de carga entre membros [S1](#s1). | O total é informativo porque não há valor de referência confiável de "esforço certo". | Horas totais não medem complexidade isoladamente. |
| `RC2` Variação | Avalia a acurácia das estimativas de tempo e a maturidade de dimensionamento da equipe [S3](#s3). | Faixas de `10/20%` são critério da equipe, razoáveis para estimativas de estudantes sem histórico prévio | O valor absoluto perde o sentido da variação (subestimou ou superestimou).|

*Tabela 7. Justificativa das medidas e dos indicadores. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

---

<a id="regras"></a>

## 6. Regras de decisão

Esta seção define as ações de governança quando uma medida atinge o nível amarelo ou vermelho, garantindo o ciclo de controle do PSM [S1](#s1). A Tabela 8 relaciona cada situação à decisão correspondente.
 
Toda decisão é registrada em `docs/gestao/medicoes.md`, com data, responsável e prazo, e vira issue de ação quando houver trabalho a fazer.

| Situação | Decisão |
|---|---|
| `CP2` amarelo | Os responsáveis das issues atrasadas informa nova Janela na própria issue (`Janela revista`), registra a causa do atraso e reordena o trabalho em até 24 horas |
| `CP2` vermelho ou `CP1` vermelho | Reunião emergencial (15 minutos) em até 24 horas. <br> Replanejar cortando ou adiando o que não pesa nos critérios, redistribuir issues entre equipe e reestimar as issues que dependem das atrasadas. |
| `DP1` amarelo ou vermelho | Reforçar o critério de aceite e exigir verificação rigorosa antes de fechar qualquer issue. |
| `DP2` com `Qcic ≥ 1` | Abrir uma issue `correcao` por critério Regular ou Insuficiente e priorizá-las antes de qualquer trabalho novo |
| `DP2` com `Pce < 75%` | Revisar na reunião seguinte o que impede os critérios de chegar a Adequado e incluir as ações nas issues `correcao` |
| `RC1` desequilibrado | Se esforço de um integrante (`Hi`) variar mais de 50% em relação á média do grupo (`Hm`), analisar a causa da disparidade e rebalancear a atribuição das próximas *issues* entre as duplas.|
| `RC2` amarelo (`Ve > 20%`) | Reestimar issues parecidas e registrar o motivo do desvio e o sentido (subestimou ou superestimou) |
| Cobertura de Dados Amarela (`Pa < 90%`) | Lançar as horas pendentes no mesmo dia; enquanto `Pa < 90%`, marcar `RC1` e `RC2` "com ressalva". |

 
*Tabela 8. Regras de decisão por situação de medição. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

A regra de que nenhuma issue é fechada sem revisão é uma convenção permanente ([seção 4.2](#unidade-de-trabalho), definição de "Concluída"), e não uma condição de medição.
 
## 7. Evidências no Git

Esta seção indica onde ficam armazenadas as evidências que permitem conferir as medições no repositório (Tabela 11).

| Evidência | Onde |
|---|---|
| [Issues](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues) | GitHub: Issues e suas respectivas labels |
| [Commits](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commits/main/) e [pull requests](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/pulls) com revisão | GitHub: Pull requests |
| [Horas, esforço planejado e autoavaliação](../../assets/dados/gestao/) | `assets/dados/gestao/` |
| [Registro de Horas (consolidado)](../gestao/horas.md) | `docs/gestao/horas.md` |
| [Medições, interpretações e decisões](../gestao/medicoes.md) | `docs/gestao/medicoes.md` |
| [Script de coleta](../../src/coletar_psm.py) | `scripts/coletar_psm.py` |
| [Uso de IA](../gestao/uso_de_ia.md) | `docs/gestao/uso_de_ia.md` |

*Tabela 11. Evidências das medições e sua localização. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

## Referências

<a id="s1"></a>

> MCGARRY, John et al. Practical Software Measurement: Objective Information for Decision Makers. Version 4.0. Naval Undersea Warfare Center Division, 2001.

<a id="s2"></a>

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. *ISO/IEC/IEEE 15939:2017: Systems and software engineering — Measurement process*. Geneva: ISO, 2017.

<a id="s3"></a>

> JONES, Cheryl L. et al. *Practical Software and Systems Measurement: Continuous Iterative Development Measurement Framework — Part 1*. Version 2.1. PSM; NDIA; INCOSE, 2021.

<a id="s4"></a>

> JONES, Cheryl L. et al. *Practical Software and Systems Measurement: Continuous Iterative Development Measurement Framework — Part 2: Measurement Specifications and Enterprise Measures*. Version 2.1. PSM; NDIA; INCOSE, 2021.

<a id="s5"></a>

> BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. In: MARCINIAK, John J. (ed.). *Encyclopedia of Software Engineering*. v. 1. New York: John Wiley & Sons, 1994. p. 528–532.

---

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|---|---|---|---|---|
| 1.0 | 15/10/2026 | Criação do Plano de Medição | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.1 | 15/10/2026 | Atualização do Plano de Medição | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.2 | 16/10/2026 | Padronização das tabelas e estruturação dos textos das seções | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.3 | 19/10/2026 | Corrige datas e numero das tabelas | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.4 | 19/10/2026 | Correções nas métricas e algumas nomeclaturas | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.5 | 21/10/2026 | Refatoração do Plano de Medição para adequação à PSM/CID | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.6 | 21/10/2026 | Remoção do processo de medição | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |