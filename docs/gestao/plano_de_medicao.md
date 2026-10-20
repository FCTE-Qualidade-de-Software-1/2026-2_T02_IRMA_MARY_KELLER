# Plano de medição PSM/CID

Versão 1.2

---

## 1. Finalidade

Acompanhar a execução do projeto, como os marcos principais sendo Entrega 1 (26/10/2026) e Entrega 2 (18/11/2026), passando pelos pontos de controle PC1({19 - 21}/10/2026) e PC2({04 - 09}/11/2026) com medidas do modelo PSM/CID nas três categorias exigidas: *Calendário e Progresso*, *Desempenho dos Processos* e *Recursos e Custos*. Cada medição é registrada com sua interpretação e com as decisões de gestão que ela provocou (ver [Medições e decisões](medicoes.md)).

## 2. Necessidades de informação

No PSM/CID, a medição parte de uma necessidade de informação e não das medidas disponíveis. Por isso, cada *objetivo de medição* (O1 a O3) está associado a uma *categoria* e a uma *pergunta de gestão* (pergunta orientadora), que serve de guia para escolher as medidas da seção 3. A Tabela 1 reúne esses elementos.

| Objetivo | Categoria | Pergunta de gestão |
|---|---|---|
| [O1](#objetivo-1) | Calendário e Progresso | Vamos entregar os slides do Pontos de Controle e a Entregas no ritmo planejado? |
| [O2](#objetivo-2) | Desempenho dos Processos | O processo de produzir e revisar gera entregas que atendem aos critérios da professora, sem muito retrabalho? |
| [O3](#objetivo-3) | Recursos e Custos | O esforço gasto confere com o planejado e está equilibrado entre os membros? |

*Tabela 1. Necessidades de informação por objetivo de medição. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

## 3. Medidas e indicadores por categoria

Esta seção detalha como cada objetivo de medição será respondido. Em cada categoria há um objetivo (O1 a O3) e uma tabela que parte do atributo observado, passa pelas medidas base e pela medida derivada, apresenta a fórmula de cálculo e termina no indicador, que traduz o resultado em um nível de julgamento. A seção se divide em três subseções, uma por categoria do PSM/CID: [3.1 Calendário e Progresso (O1)](#31-calendário-e-progresso), [3.2 Desempenho dos Processos (O2)](#32-desempenho-dos-processos) e [3.3 Recursos e Custos (O3)](#33-recursos-e-custos). Os termos usados nas fórmulas são definidos na [seção 4](#unidade-de-trabalho) e a justificativa das medidas e dos limiares está na [seção 5](#justificativa).

### 3.1 Calendário e Progresso

Trata do ritmo de execução: se as atividades planejadas estão sendo concluídas (`CP1`) e se estão sendo concluídas dentro do prazo (`CP2`).

<a id="objetivo-1"></a>

#### O1: verificar se a equipe está concluindo as atividades planejadas dentro do prazo.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Progresso das atividades (`CP1`) | [Atividades](#unidade-de-trabalho) concluídas (`Ac`) <br> [Atividades](#unidade-de-trabalho) planejadas (`Ap`) | Percentual de progresso planejado cumprido. (`Ppc`) | `Ppc = (Ac ÷ Ap) × 100`	|Adequado: `90% ≤ Ppc ≤ 100%` <br> Bom: `80% ≤ Ppc < 90%` <br> Insuficiente: `60% ≤ Ppc < 80%` <br> Crítico: `Ppc < 60%` |
| Cumprimento do prazo (`CP2`) | [Atividades](#unidade-de-trabalho) concluídas no prazo (`Acp`) <br> [Atividades](#unidade-de-trabalho) concluídas (`Ac`) | Percentual de atividades com registro de esforço. (`PaRe`) | `PaRe = (Acp ÷ Ac) × 100` | Adequado: `90% ≤ PaRe ≤ 100%` <br> Bom: `80% ≤ PaRe < 90%` <br> Insuficiente: `60% ≤ PaRe < 80%` <br> Crítico: `PaRe < 60%` |

*Tabela 2. Medidas e indicadores de Calendário e Progresso (O1). Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

### 3.2 Desempenho dos Processos

Trata de como o trabalho é produzido: o retrabalho que o processo gera (`DP1`) e o quanto as entregas atendem aos critérios da rubrica (`DP2`).

<a id="objetivo-2"></a>

#### O2: verificar a eficiência, a efetividade e a conformidade dos processos de trabalho da equipe.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Eficiência do processo (`DP1`) | Issue reaberta (`Ir`) <br> Issue com label `correção` (`Ic`) <br> Issue fechada (`If`) | Percentual de issues fechadas que apresentaram retrabalho (`Prt`) | `Prt = [(Ir v Ic) ÷ If] × 100` | Adequado: `Prt ≤ 15%` <br> Bom: `15% < Ptr ≤ 35%` <br> Insuficiente: `35% < Prt < 50%` <br> Crítico: `Prt ≥ 50%` |
| Efetividade do processo (`DP2`) | Critérios avaliados como {Insuficiente (`Ci`) <br>  Regular (`Cr`) <br> Satisfatório (`Cs`) <br> Excelente (`Ce`)} <br> Total de critérios avaliados (`Ct`) | Quantidade de critérios iguais ou abaixo de Regular (`Ciar`) <br> Percentual de critérios no nível Excelente (`Pce`) | `Ciar = Ci + Cr` <br> `Pce = (Ce ÷ Ct) × 100` | Adequado: `Ciar ≤ 0`  <br> Bom: `1 ≤ Ciar ≤ 2` <br> Insuficiente: `Ciar > 3` <br> Adequado: `90% ≤ Pce ≤ 100%` <br> Bom: `75% ≤ Pce < 90%` <br> Insuficiente: `Pce < 75%` |

*Tabela 3. Medidas e indicadores de Desempenho dos Processos (O2). Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

### 3.3 Recursos e Custos

Trata do esforço da equipe: horas dedicadas (`RC1`), variação em relação ao estimado (`RC2`) e cobertura do registro de horas (`RC3`).

<a id="objetivo-3"></a>

#### O3: monitorar o esforço dedicado ao desenvolvimento do projeto e estimar seu custo com base nas horas trabalhadas.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Esforço de desenvolvimento (`RC1`) | Horas estimadas por atividade (`He`) <br> Horas efetivamente trabalhadas por atividade (`Hr`) | Esforço total realizado (`Et`) | `Et = Σ Hr` | Informativo: registrar o total de horas da equipe e a distribuição por atividade e integrante. |
| Variação do esforço estimado (`RC2`) | Esforço estimado total (`Ee`) <br> Esforço realizado total (`Er`) | Variação percentual do esforço (`Ve`) | `Ve = ( |Er − Ee| ÷ Ee ) × 100` | Adequado: `Ve ≤ 10%` <br> Bom: `10% < Ve ≤ 20%` <br> Insuficiente: `Ve > 20%` |
| Cobertura do registro de esforço (`RC3`) | Atividades concluídas com horas registradas (`Ar`) <br> Total de atividades concluídas (`Ac`) | Percentual de atividades com esforço registrado (`Pa`) | `Pa = (Ar ÷ Ac) × 100` | Adequado: `90% ≤ Pa ≤ 100%` <br> Bom: `75% ≤ Pa < 90%` <br> Insuficiente: `60% ≤Pa < 75%` <br> Crítico: `Pa < 60%` |

*Tabela 4. Medidas e indicadores de Recursos e Custos (O3). Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

**Procedimento de coleta:** cada integrante registra as horas dedicadas às atividades em andamento e concluídas (ver [Registro de Horas](horas.md)), vinculando-as às respectivas issues. A equipe consolida os registros periodicamente, compara o esforço real com o estimado e utiliza o valor de referência da hora profissional apenas para calcular o custo equivalente do trabalho.

## 4. Unidade de trabalho e convenções

Esta seção fixa as regras que tornam as medições repetíveis: o que conta como unidade de trabalho, como cada termo das fórmulas é interpretado e como os níveis dos indicadores se traduzem em cores. Assim, qualquer integrante chega ao mesmo valor ao calcular uma medida.
 
<a id="unidade-de-trabalho"></a>
 
### 4.1 Unidade de trabalho
 
A unidade de trabalho é a **issue** do GitHub. O corpo da issue traz **Janela** (data prevista de conclusão), **Estimativa** (horas) e o(os) ID dos critérios (por exemplo, `F1-02`). Uma issue sem ID, sem Janela ou sem Estimativa não entra nas medições de forma confiável e deve ser corrigida antes da próxima medição.
 
### 4.2 Definições operacionais

A Tabela 5 define, de forma operacional, os termos usados nas fórmulas da [seção 3](#3-medidas-e-indicadores-por-categoria).
 
| Termo | Definição operacional |
|---|---|
| Planejada até a data (`Ap`) | Issue dos milestones das entregas cuja Janela é igual ou anterior à data da medição |
| Concluída (`Ac`) | Issue fechada com os critérios de aceite atendidos e com revisão do revisor registrada no pull request. Issue fechada sem revisão não conta como concluída |
| Concluída no prazo (`Acp`) | Issue concluída em data igual ou anterior à sua **Janela original** |
| Janela original | Valor da Janela no momento da criação da issue. Quando o prazo é revisto, a nova data vai em comentário (`Janela revista`) e serve só ao replanejamento. O `CP2` sempre compara com a original, para que o atraso não desapareça da medição |
| Retrabalho (`Ir`, `Ic`) | Issue reaberta depois de fechada (`Ir`) ou issue com a label `correcao` (`Ic`). A issue que cumpre as duas condições conta uma vez só (união) |
| Estimativa congelada | A Estimativa registrada na criação da issue é a usada no `RC2`. Reestimativas vão em comentário e não sobrescrevem o valor original |
| Esforço realizado (`Hr`, `Hi`) | Horas registradas em `assets/dados/gestao/horas/<usuario>.csv`, em múltiplos de 0,25 h, ligadas ao ID da issue. Em trabalho em dupla, cada integrante lança as próprias horas |
| Escopo do `RC2` | Calculado apenas sobre issues concluídas (`Ee` e `Er` do mesmo conjunto), para que issues em andamento não distorçam a comparação. As horas de issues em andamento entram no `RC1` |
| Horas sem issue | Reuniões e atividades de gestão também precisam de issue de apoio, com Estimativa. Horas sem ID válido não são atribuídas a nenhuma atividade e reduzem o `RC3` |
| Denominador zero | Se `Ap`, `Ac`, `If`, `Ee` ou `Ct` for zero na data, a medida é registrada como "sem dados" e não recebe nível |
 
*Tabela 5. Definições operacionais dos termos usados nas medições. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

### 4.3 Níveis e cores
 
Os indicadores usam níveis; as regras de decisão [(seção 6)](#regras) usam as cores correspondentes para preenchimento no planilha de controle.

| Nível | Cor | Significado |
|---|---|---|
| Adequado e Bom | Verde | Sem ação obrigatória; registrar a medição |
| Insuficiente | Amarelo | Ação corretiva conforme a seção 6 |
| Crítico | Vermelho | Ação corretiva imediata conforme a seção 6 |
| Informativo | Sem cor | Apenas registrar e acompanhar |

*Tabela 6. Níveis dos indicadores, cores e significado. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*
 
Nos indicadores que não têm nível Crítico (`DP2`, `RC2` e o equilíbrio do `RC1`), o pior nível possível é Insuficiente (amarelo).
 
<a id="justificativa"></a>

## 5. Justificativa das medições e dos indicadores

Esta seção explica por que cada medida e cada indicador foram escolhidos, quais limitações precisam ser consideradas na interpretação e de onde vêm os limiares usados.
 
### 5.1 Lógica de escolha
 
O PSM parte da necessidade de informação, não da medida disponível. Por isso há uma pergunta de gestão para cada categoria [(seção 2)](#2-necessidades-de-informação) e um conjunto pequeno de medidas que a responde diretamente. Foram preferidas medidas que o próprio fluxo de trabalho já produz (issues, pull requests, horas e autoavaliação), para que a coleta não vire uma tarefa à parte e possa ser conferida no repositório.
 
### 5.2 Medidas e indicadores

A Tabela 7 apresenta, para cada medida, a razão da escolha, a razão das faixas do indicador e a limitação a considerar.

| Medida | Por que foi escolhida | Por que este indicador | Limitação a considerar |
|---|---|---|---|
| `CP1` Progresso | Responde diretamente ao [O1](#objetivo-1): compara o que deveria estar pronto na data com o que está | Faixas de `90/80/60%` são critério da equipe. `90%` admite uma pendência em cerca de dez atividades; abaixo de `60%` o prazo de uma entrega fica ameaçado | Todas as issues pesam igual, independentemente do tamanho. Com poucas issues, cada uma vale muitos pontos percentuais: interpretar junto com os valores de `Ac` e `Ap` |
| `CP2` Prazo | Complementa o `CP1`: uma issue pode estar concluída, mas fora do prazo. O `CP1` mostra quanto foi feito; o `CP2`, se foi feito na hora certa | Mesmas faixas do `CP1`, por consistência da categoria | Compara com a Janela original; replanejar não "limpa" o atraso, o que é intencional |
| `DP1` Eficiência | Retrabalho (issue reaberta ou corrigida) é um indício direto de que o processo de produzir e revisar não acertou de primeira | Faixas de `15/35/50%` são critério da equipe, mais tolerantes que as de prazo porque revisão faz parte de um trabalho acadêmico | Depende da disciplina de reabrir a issue ou usar a label `correcao`. <br> Retrabalho feito dentro do pull request antes do fechamento não aparece |
| `DP2` Efetividade | Responde à parte do [O2](#objetivo-2) sobre atender aos critérios da professora. A nota real só chega depois da entrega, então a equipe se autoavalia nos critérios da rubrica a cada fase | Dois indicadores porque medem coisas distintas: `Ciar` destaca os critérios mais fracos (gera ação); `Pce` mede a proximidade do objetivo de alcançar a última opção em cada critério. Com a rubrica atual (11 critérios na [Fase 1](../criterios/fase1.md) e 12 na [Fase 2](../criterios/fase2.md)), `Pce ≥ 90%` admite no máximo um critério abaixo de Excelente | Autoavaliação é subjetiva. <br> Mitigação: quem avalia é o revisor, não o autor, e cada nível exige evidência no `autoavaliacao.csv` |
| `RC1` Esforço | Base do [O3](#objetivo-3): sem o total e a distribuição das horas não há como falar de custo nem de equilíbrio entre os membros | O total é informativo porque não há valor de referência confiável de "esforço certo". | A média esconde diferenças de tipo de tarefa (escrita, revisão, código), a faixa é ampla de propósito para não gerar alerta por variações normais |
| `RC2` Variação | Responde à parte do [O3](#objetivo-3) sobre o esforço conferir com o planejado e alimenta a reestimativa das próximas issues | Faixas de `10/20%` são critério da equipe, razoáveis para estimativas de estudantes sem histórico prévio | O valor absoluto perde o sentido da variação (subestimou ou superestimou) <br> Registra o sentido na interpretação |
| `RC3` Cobertura | Valida o `RC1` e o `RC2`: se muitas issues concluídas não têm horas, esses valores não são confiáveis | Faixas de `90/75/60%` um pouco mais brandas que as de prazo, porque o lançamento é manual | Mede se há registro, não se o registro é correto |

*Tabela 7. Justificativa das medidas e dos indicadores. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

### 5.3 Origem e revisão dos limiares
 
O PSM/CID não prescreve valores de limiar e não foi encontrada referência normativa a citar. Os limiares acima são **critérios definidos pela equipe**, assumidos como hipóteses de trabalho. Serão reavaliados em [M-2](#pontos), com os primeiros dados reais. Qualquer mudança é registrada no histórico de versões, e as medições anteriores ficam marcadas com a versão do plano sob a qual foram feitas.
 
<a id="regras"></a>

## 6. Regras de decisão

Esta seção define o que a equipe faz quando uma medida cai em amarelo ou vermelho, para que a medição leve a uma decisão e não apenas a um registro. A Tabela 8 relaciona cada situação à decisão correspondente.
 
Toda decisão é registrada em `docs/gestao/medicoes.md`, com data, responsável e prazo, e vira issue de ação quando houver trabalho a fazer.

| Situação | Decisão |
|---|---|
| `CP2` amarelo | Os responsáveis das issues atrasadas informa nova Janela na própria issue (comentário `Janela revista`), registra a causa do atraso e reordena o trabalho em até 24 horas |
| `CP2` vermelho ou `CP1` vermelho | Reunião de 15 minutos em até 24 horas; replanejar cortando ou adiando o que não pesa nos critérios, redistribuir issues entre equipe e reestimar as issues que dependem das atrasadas; registrar a decisão |
| `DP1` amarelo ou vermelho | Reforçar o critério de aceite e exigir revisão antes de fechar a issue |
| `DP2` com `Ciar ≥ 1` | Abrir uma issue `correcao` por critério Regular ou Insuficiente e priorizá-las antes de qualquer trabalho novo |
| `DP2` com `Pce < 75%` | Revisar na reunião seguinte o que impede os critérios de chegar a Excelente e incluir as ações nas issues `correcao` |
| `RC1` com `Hi` fora de ±50% de `Hm` | Rebalancear as próximas issues entre as duplas |
| `RC2` amarelo (`Ve > 20%`) | Reestimar issues parecidas e registrar o motivo do desvio e o sentido (subestimou ou superestimou) |
| `RC3` amarelo ou vermelho | Lançar as horas pendentes no mesmo dia e repetir o cálculo; enquanto o `RC3` estiver abaixo de 75%, marcar `RC1` e `RC2` como "com ressalva" |
 
*Tabela 8. Regras de decisão por situação de medição. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

A regra de que nenhuma issue é fechada sem revisão é uma convenção permanente ([seção 4.2](#unidade-de-trabalho), definição de "Concluída"), e não uma condição de medição.
 
## 7. Procedimento de medição

Esta seção descreve como a medição é executada: quais dados entram, o passo a passo de cada rodada e em que datas ela ocorre.
 
<a id="responsavel"></a>

**Responsável pela execução:** Rodízio a definir pelo grupo. Todos os membros lançam as horas até as 12h do dia da medição.
 
### 7.1 Dados de entrada

A Tabela 9 lista os dados necessários, onde ficam, quem os alimenta e quais medidas dependem deles.
 
| Dado | Fonte | Quem alimenta | Quando | Medidas que usam |
|---|---|---|---|---|
| ID, Janela, Estimativa, estado, datas de fechamento e reabertura, labels | Issues e pull requests do GitHub | Responsável pela issue | Ao criar, fechar ou reabrir a issue | `CP1`, `CP2`, `DP1`, `RC2`, `RC3` |
| Horas por integrante e por issue | `assets/dados/gestao/horas/<usuario>.csv` (colunas `data,atividade,horas`; ver [Registro de Horas](horas.md)) | Cada integrante | Até 12h do dia da medição | `RC1`, `RC2`, `RC3` |
| Nível por critério da rubrica | `assets/dados/gestao/autoavaliacao.csv` (colunas `data,criterio,nivel,evidencia`) | Revisor | Em [M-3](#pontos) | `DP2` |
| Uso de IA | [Uso de IA](uso_de_ia.md) | Quem usou a ferramenta | No momento do uso | Evidência para os critérios de uso de IA na autoavaliação (`DP2`) |
 
*Tabela 9. Dados de entrada das medições. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*
 
No `autoavaliacao.csv`, `criterio` é o código da rubrica (por exemplo, `F1-C6`) e `nivel` é um de Insuficiente, Regular, Satisfatório ou Excelente, que correspondem, nesta ordem, às quatro opções da rubrica da professora, da primeira à última.
 
### 7.2 Passos

Os passos abaixo são seguidos a cada ponto de medição.
 
1. Até as 12h do dia da medição, cada membro lança suas horas no seu CSV.
2. O [Responsável](#responsavel) confere as pré-condições: issues fechadas com Janela, Estimativa e revisão registrada; horas sem ID válido; labels `correcao` aplicadas onde devidas. Pendências são cobradas das duplas donas antes do cálculo.
3. A [Responsável](#responsavel) roda `python3 scripts/coletar_psm.py --data AAAA-MM-DD` na raiz do repositório. O script deve implementar as fórmulas da [seção 3](#3-medidas-e-indicadores-por-categoria). A cada medição, conferir à mão ao menos uma medida (por exemplo, o `CP1`) contra o resultado do script.
4. O [Responsável](#responsavel) cola a tabela no registro de `docs/gestao/medicoes.md`, com, para cada medida: ponto de medição, data, valores das medidas base, valor derivado, nível e cor.
5. Em [M-2 e M-3](#pontos), o revisor, preenche o `autoavaliacao.csv` para a fase correspondente, com um nível e uma evidência (link para o trecho do artigo, da GitPage ou do repositório) por critério. Antes disso, o [Responsável](#responsavel) confere o [registro de uso de IA](uso_de_ia.md).
6. O [Responsável](#responsavel) interpreta cada medida amarela ou vermelha: registra causa provável e decisão conforme a [seção 6](#regras), e abre issue de ação quando houver trabalho a fazer.
7. Medidas "sem dados" ou "com ressalva" são registradas como tal, com o motivo.
8. O resultado é comunicado ao grupo no mesmo dia e commitado por pull request.

<a id="pontos"></a>

### 7.3 Pontos de medição

A Tabela 10 apresenta as datas das medições, sua finalidade e as medidas calculadas em cada uma. Até o momento as datas estão referentes apenas a entrega 1.    

| Id da issue | Data | Finalidade | Medidas |
|---|---|---|---|
| M-1 | 20/10 (ter) | Primeira medição, para os slides do PC1 | `CP1`, `CP2`, `DP1`, `RC1`, `RC2`, `RC3` |
| M-2 | 22/10 (qui) | Após o PC1: replanejar com o feedback; inclui DP2 da Fase 1 | Todas, com `DP2` (Fase 1) |
| M-3 | 25/10 (dom) | Pré-entrega | `CP1`, `CP2`, `DP1`, `RC1`, `RC2`, `RC3` |
| M-4 | 26/10 (seg) | Fechamento e lições para a Entrega 2 | `CP1`, `CP2`, `DP1`, `RC1`, `RC2`, `RC3` |

*Tabela 10. Pontos de medição previstos. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

As medições de M-1 usam poucas issues concluídas e podem cair em "sem dados" ou oscilar muito; isso é esperado e deve constar na interpretação.
 
## 8. Evidências no Git

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

> BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. In: MARCINIAK, John J. (ed.). *Encyclopedia of Software Engineering*. v. 1. New York: John Wiley & Sons, 1994. p. 528-532.

> ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*. Geneva: ISO, 2023.

> ISO/IEC/IEEE 15939:2017. *Systems and software engineering — Measurement process*. Geneva: ISO, 2017.

> MCGARRY, John et al. *Practical Software Measurement: Objective Information for Decision Makers*. Boston: Addison-Wesley, 2002.

> PRACTICAL SOFTWARE AND SYSTEMS MEASUREMENT. *PSM: Practical Software and Systems Measurement*. Disponível em: https://www.psmsc.com. Acesso em: 15 out. 2026.

---
<a id="historico-de-versoes"></a>

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|---|---|---|---|---|
| 1.0 | 15/10/2026 | Criação do Plano de Medição | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.1 | 15/10/2026 | Atualização do Plano de Medição | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.2 | 16/10/2026 | Padronização das tabelas e estruturação dos textos das seções | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.3 | 19/10/2026 | Corrige datas e numero das tabelas | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |