# Plano de medição PSM/CID

Versão 1.1

---

## 1. Finalidade

Acompanhar a execução do projeto, como os marcos principais sendo Entrega 1 (26/10/2026) e Entrega 2 (18/11/2026), passando pelos pontos de controle PC1({19 - 21}/10/2026) e PC2({04 - 09}/11/2026) com medidas do modelo PSM/CID nas três categorias exigidas: *Calendário e Progresso*, *Desempenho dos Processos* e *Recursos e Custos*. Cada medição é registrada com sua interpretação e com as decisões de gestão que ela provocou (ver [Medições e decisões](medicoes.md)).

## 2. Necessidades de informação

| Objetivo | Categoria | Pergunta de gestão |
|---|---|---|
| [O1](#objetivo-1) | Calendário e Progresso | Vamos entregar os slides do Pontos de Controle e a Entregas no ritmo planejado? |
| [O2](#objetivo-2) | Desempenho dos Processos | O processo de produzir e revisar gera entregas que atendem aos critérios da professora, sem muito retrabalho? |
| [O3](#objetivo-3) | Recursos e Custos | O esforço gasto confere com o planejado e está equilibrado entre os membros? |


## 3. Medições ...

... texto

### 3.1 Calendário e Progresso

<a id="objetivo-1"></a>
#### O1: verificar se a equipe está concluindo as atividades planejadas dentro do prazo.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Progresso das atividades (`CP1`) | [Atividades](#unidade-de-trabalho) concluídas (`Ac`) <br> [Atividades](#unidade-de-trabalho) planejadas (`Ap`) | Percentual de progresso planejado cumprido. (`Ppc`) | `Ppc = (Ac ÷ Ap) × 100`	|Adequado: 90% ≤ Ppc ≤ 100% <br> Bom: `80% ≤ Ppc < 90%` <br> Insuficiente: `60% ≤ Ppc < 80%` <br> Crítico: `Ppc < 60%` |
| Cumprimento do prazo (`CP2`) | [Atividades](#unidade-de-trabalho) concluídas no prazo (`Acp`) <br> [Atividades](#unidade-de-trabalho) concluídas (`Ac`) | Percentual de atividades com registro de esforço. (`PaRe`) | `PaRe = (Acp ÷ Ac) × 100` | Adequado: `90% ≤ PaRe ≤ 100%` <br> Bom: `80% ≤ PaRe < 90%` <br> Insuficiente: `60% ≤ PaRe < 80%` <br> Crítico: `PaRe < 60%` |

### 3.2 Desempenho dos Processos

<a id="objetivo-2"></a>
#### O2: verificar a eficiência, a efetividade e a conformidade dos processos de trabalho da equipe.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Eficiência do processo (`DP1`) | Issue reaberta (`Ir`) <br> Issue com label `correção` (`Ic`) <br> Issue fechada (`If`) | Percentual de issues fechadas que apresentaram retrabalho (`Prt`) | `Prt = [(Ir v Ic) ÷ If] × 100` | Adequado: `Prt ≤ 15%` <br> Bom: `15% < Ptr ≤ 35%` <br> Insuficiente: `35% < Prt < 50%` <br> Crítico: `Prt ≥ 50%` |
| Efetividade do processo (`DP2`) | Critérios avaliados como {Insuficiente (`Ci`) <br>  Regular (`Cr`) <br> Satisfatório (`Cs`) <br> Excelente (`Ce`)} <br> Total de critérios avaliados (`Ct`) | Quantidade de critérios iguais ou abaixo de Regular (`Ciar`) <br> Percentual de critérios no nível Excelente (`Pce`) | `Ciar = Ci + Cr` <br> `Pce = (Ce ÷ Ct) × 100` | Adequado: `Ciar ≤ 0`  <br> Bom: `1 ≤ Ciar ≤ 2` <br> Insuficiente: `Ciar > 3` <br> Adequado: `90% ≤ Pce ≤ 100%` <br> Bom: `75% ≤ Pce < 90%` <br> Insuficiente: `Pce < 75%` |

### 3.3 Recursos e Custos

<a id="objetivo-3"></a>
#### O3: monitorar o esforço dedicado ao desenvolvimento do projeto e estimar seu custo com base nas horas trabalhadas.

| Atributo | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Esforço de desenvolvimento (`RC1`) | Horas estimadas por atividade (`He`) <br> Horas efetivamente trabalhadas por atividade (`Hr`) | Esforço total realizado (`Et`) | `Et = Σ Hr` | Informativo: registrar o total de horas da equipe e a distribuição por atividade e integrante. |
| Variação do esforço estimado (`RC2`) | Esforço estimado total (`Ee`) <br> Esforço realizado total (`Er`) | Variação percentual do esforço (`Ve`) | `Ve = ( |Er − Ee| ÷ Ee ) × 100` | Adequado: `Ve ≤ 10%` <br> Bom: `10% < Ve ≤ 20%` <br> Insuficiente: `Ve > 20%` |
| Cobertura do registro de esforço (`RC3`) | Atividades concluídas com horas registradas (`Ar`) <br> Total de atividades concluídas (`Ac`) | Percentual de atividades com esforço registrado (`Pa`) | `Pa = (Ar ÷ Ac) × 100` | Adequado: `90% ≤ Pa ≤ 100%` <br> Bom: `75% ≤ Pa < 90%` <br> Insuficiente: `60% ≤Pa < 75%` <br> Crítico: `Pa < 60%` |

**Procedimento de coleta:** cada integrante registra as horas dedicadas às atividades em andamento e concluídas (ver [Registro de Horas](horas.md)), vinculando-as às respectivas issues. A equipe consolida os registros periodicamente, compara o esforço real com o estimado e utiliza o valor de referência da hora profissional apenas para calcular o custo equivalente do trabalho.
## 4. Unidade de trabalho e convenções
 
<a id="unidade-de-trabalho"></a>
 
### 4.1 Unidade de trabalho
 
A unidade de trabalho é a **issue** do GitHub. O ID vai no título (por exemplo, `[F1-02]`) e o corpo traz **Janela** (data prevista de conclusão) e **Estimativa** (horas). Uma issue sem ID, sem Janela ou sem Estimativa não entra nas medições de forma confiável e deve ser corrigida antes da próxima medição.
 
### 4.2 Definições operacionais
 
| Termo | Definição operacional |
|---|---|
| Planejada até a data (`Ap`) | Issue dos milestones das entregas cuja Janela é igual ou anterior à data da medição |
| Concluída (`Ac`) | Issue fechada com os critérios de aceite atendidos e com revisão da dupla revisora registrada no pull request. Issue fechada sem revisão não conta como concluída |
| Concluída no prazo (`Acp`) | Issue concluída em data igual ou anterior à sua **Janela original** |
| Janela original | Valor da Janela no momento da criação da issue. Quando o prazo é revisto, a nova data vai em comentário (`Janela revista`) e serve só ao replanejamento. O `CP2` sempre compara com a original, para que o atraso não desapareça da medição |
| Retrabalho (`Ir`, `Ic`) | Issue reaberta depois de fechada (`Ir`) ou issue com a label `correcao` (`Ic`). A issue que cumpre as duas condições conta uma vez só (união) |
| Estimativa congelada | A Estimativa registrada na criação da issue é a usada no `RC2`. Reestimativas vão em comentário e não sobrescrevem o valor original |
| Esforço realizado (`Hr`, `Hi`) | Horas registradas em `assets/dados/gestao/horas/<usuario>.csv`, em múltiplos de 0,25 h, ligadas ao ID da issue. Em trabalho de dupla, cada integrante lança as próprias horas |
| Escopo do `RC2` | Calculado apenas sobre issues concluídas (`Ee` e `Er` do mesmo conjunto), para que issues em andamento não distorçam a comparação. As horas de issues em andamento entram no `RC1` |
| Horas sem issue | Reuniões e atividades de gestão também precisam de issue de apoio, com Estimativa. Horas sem ID válido não são atribuídas a nenhuma atividade e reduzem o `RC3` |
| Valor de referência da hora (`Vh`) | Usado só para o custo equivalente: `custo = Et × Vh`. Valor e fonte **a definir pela equipe**; enquanto não definidos, o custo não é calculado. Não é indicador e não tem limiar |
| Denominador zero | Se `Ap`, `Ac`, `If`, `Ee` ou `Ct` for zero na data, a medida é registrada como "sem dados" e não recebe nível |
 
### 4.3 Níveis e cores
 
Os indicadores usam níveis; as regras de decisão (seção 6) usam as cores correspondentes.
 
| Nível | Cor | Significado |
|---|---|---|
| Adequado e Bom | Verde | Sem ação obrigatória; registrar a medição |
| Insuficiente | Amarelo | Ação corretiva conforme a seção 6 |
| Crítico | Vermelho | Ação corretiva imediata conforme a seção 6 |
| Informativo | Sem cor | Apenas registrar e acompanhar |
 
Nos indicadores que não têm nível Crítico (`DP2`, `RC2` e o equilíbrio do `RC1`), o pior nível possível é Insuficiente (amarelo).
 
<a id="justificativa"></a>
## 5. Justificativa das medições e dos indicadores
 
### 5.1 Lógica de escolha
 
O PSM parte da necessidade de informação, não da medida disponível. Por isso há uma pergunta de gestão para cada categoria (seção 2) e um conjunto pequeno de medidas que a responde diretamente. Foram preferidas medidas que o próprio fluxo de trabalho já produz (issues, pull requests, horas e autoavaliação), para que a coleta não vire uma tarefa à parte e possa ser conferida no repositório.
 
### 5.2 Medidas e indicadores
 
| Medida | Por que foi escolhida | Por que este indicador | Limitação a considerar |
|---|---|---|---|
| `CP1` Progresso | Responde diretamente ao O1: compara o que deveria estar pronto na data com o que está | Faixas de 90/80/60% são critério da equipe. 90% admite uma pendência em cerca de dez atividades; abaixo de 60% o prazo de uma entrega fica ameaçado | Todas as issues pesam igual, independentemente do tamanho. Com poucas issues, cada uma vale muitos pontos percentuais: interpretar junto com os valores de `Ac` e `Ap` |
| `CP2` Prazo | Complementa o `CP1`: uma issue pode estar concluída, mas fora do prazo. O `CP1` mostra quanto foi feito; o `CP2`, se foi feito na hora certa | Mesmas faixas do `CP1`, por consistência da categoria | Compara com a Janela original; replanejar não "limpa" o atraso, o que é intencional |
| `DP1` Eficiência | Retrabalho (issue reaberta ou corrigida) é um indício direto de que o processo de produzir e revisar não acertou de primeira | Faixas de 15/35/50% são critério da equipe, mais tolerantes que as de prazo porque revisão faz parte de um trabalho acadêmico | Depende da disciplina de reabrir a issue ou usar a label `correcao`; retrabalho feito dentro do pull request antes do fechamento não aparece |
| `DP2` Efetividade | Responde à parte do O2 sobre atender aos critérios da professora. A nota real só chega depois da entrega, então a equipe se autoavalia nos critérios da rubrica a cada fase | Dois indicadores porque medem coisas distintas: `Ciar` destaca os critérios mais fracos (gera ação); `Pce` mede a proximidade do objetivo de alcançar a última opção em cada critério. Com a rubrica atual (11 critérios na Fase 1 e 12 na Fase 2), `Pce ≥ 90%` admite no máximo um critério abaixo de Excelente | Autoavaliação é subjetiva. Mitigação: quem avalia é a dupla revisora, não a autora, e cada nível exige evidência no `autoavaliacao.csv` |
| `RC1` Esforço | Base do O3: sem o total e a distribuição das horas não há como falar de custo nem de equilíbrio entre os membros | O total é informativo porque não há valor de referência confiável de "esforço certo". O equilíbrio usa a faixa de ±50% da média, definida pela equipe como limite para rebalancear issues | A média esconde diferenças de tipo de tarefa (escrita, revisão, código); a faixa é ampla de propósito para não gerar alerta por variações normais |
| `RC2` Variação | Responde à parte do O3 sobre o esforço conferir com o planejado e alimenta a reestimativa das próximas issues | Faixas de 10/20% são critério da equipe, razoáveis para estimativas de estudantes sem histórico prévio | O valor absoluto perde o sentido da variação (subestimou ou superestimou); registrar o sentido na interpretação |
| `RC3` Cobertura | Valida o `RC1` e o `RC2`: se muitas issues concluídas não têm horas, esses valores não são confiáveis | Faixas de 90/75/60% um pouco mais brandas que as de prazo, porque o lançamento é manual | Mede se há registro, não se o registro é correto |
 
### 5.3 Origem e revisão dos limiares
 
O PSM/CID não prescreve valores de limiar e não foi encontrada referência normativa a citar. Os limiares acima são **critérios definidos pela equipe**, assumidos como hipóteses de trabalho. Serão reavaliados em M-2, com os primeiros dados reais. Qualquer mudança é registrada no histórico de versões, e as medições anteriores ficam marcadas com a versão do plano sob a qual foram feitas.
 
## 6. Regras de decisão
 
Toda decisão é registrada em `docs/gestao/medicoes.md`, com data, responsável e prazo, e vira issue de ação quando houver trabalho a fazer.
 
| Situação | Decisão |
|---|---|
| `CP2` amarelo | A dupla dona das issues atrasadas informa nova Janela na própria issue (comentário `Janela revista`), registra a causa do atraso e reordena o trabalho em até 24 horas |
| `CP2` vermelho ou `CP1` vermelho | Reunião de 15 minutos em até 24 horas; replanejar cortando ou adiando o que não pesa nos critérios, redistribuir issues entre duplas e reestimar as issues que dependem das atrasadas; registrar a decisão |
| `DP1` amarelo ou vermelho | Reforçar o critério de aceite e exigir revisão da dupla revisora antes de fechar a issue |
| `DP2` com `Ciar ≥ 1` | Abrir uma issue `correcao` por critério Regular ou Insuficiente e priorizá-las antes de qualquer trabalho novo |
| `DP2` com `Pce < 75%` | Revisar na reunião seguinte o que impede os critérios de chegar a Excelente e incluir as ações nas issues `correcao` |
| `RC1` com `Hi` fora de ±50% de `Hm` | Rebalancear as próximas issues entre as duplas |
| `RC2` amarelo (`Ve > 20%`) | Reestimar issues parecidas e registrar o motivo do desvio e o sentido (subestimou ou superestimou) |
| `RC3` amarelo ou vermelho | Lançar as horas pendentes no mesmo dia e repetir o cálculo; enquanto o `RC3` estiver abaixo de 75%, marcar `RC1` e `RC2` como "com ressalva" |
 
A regra de que nenhuma issue é fechada sem revisão da dupla revisora é uma convenção permanente (seção 4.2, definição de "Concluída"), e não uma condição de medição.
 
## 7. Procedimento de medição
 
**Responsável pela execução:** Dupla C. Todos os membros lançam as horas até as 12h do dia da medição.
 
### 7.1 Dados de entrada
 
| Dado | Fonte | Quem alimenta | Quando | Medidas que usam |
|---|---|---|---|---|
| ID, Janela, Estimativa, estado, datas de fechamento e reabertura, labels | Issues e pull requests do GitHub | Dupla dona da issue | Ao criar, fechar ou reabrir a issue | `CP1`, `CP2`, `DP1`, `RC2`, `RC3` |
| Horas por integrante e por issue | `assets/dados/gestao/horas/<usuario>.csv` (colunas `data,atividade,horas`; ver [Registro de Horas](horas.md)) | Cada integrante | Até 12h do dia da medição | `RC1`, `RC2`, `RC3` |
| Nível por critério da rubrica | `assets/dados/gestao/autoavaliacao.csv` (colunas `data,criterio,nivel,evidencia`) | Dupla revisora | Em M-2 (Fase 1) e M-3 (Fase 2) | `DP2` |
| Uso de IA | [Uso de IA](uso_de_ia.md) | Quem usou a ferramenta | No momento do uso | Evidência para os critérios de uso de IA na autoavaliação (`DP2`) |
 
No `autoavaliacao.csv`, `criterio` é o código da rubrica (por exemplo, `F1-C6`) e `nivel` é um de Insuficiente, Regular, Satisfatório ou Excelente, que correspondem, nesta ordem, às quatro opções da rubrica da professora, da primeira à última.
 
### 7.2 Passos
 
1. Até as 12h do dia da medição, cada membro lança suas horas no seu CSV.
2. A Dupla C confere as pré-condições: issues fechadas com Janela, Estimativa e revisão registrada; horas sem ID válido; labels `correcao` aplicadas onde devidas. Pendências são cobradas das duplas donas antes do cálculo.
3. A Dupla C roda `python3 scripts/coletar_psm.py --data AAAA-MM-DD` na raiz do repositório. O script deve implementar as fórmulas da seção 3. A cada medição, conferir à mão ao menos uma medida (por exemplo, o `CP1`) contra o resultado do script.
4. A Dupla C cola a tabela no registro de `docs/gestao/medicoes.md`, com, para cada medida: ponto de medição, data, valores das medidas base, valor derivado, nível e cor.
5. Em M-2 e M-3, a dupla revisora preenche o `autoavaliacao.csv` para a fase correspondente, com um nível e uma evidência (link para o trecho do artigo, da GitPage ou do repositório) por critério. Antes disso, a Dupla C confere o [registro de uso de IA](uso_de_ia.md).
6. A Dupla C interpreta cada medida amarela ou vermelha: registra causa provável e decisão conforme a seção 6, e abre issue de ação quando houver trabalho a fazer.
7. Medidas "sem dados" ou "com ressalva" são registradas como tal, com o motivo.
8. O resultado é comunicado ao grupo no mesmo dia e commitado por pull request.
### 7.3 Pontos de medição
 
| Id da issue | Data | Finalidade | Medidas |
|---|---|---|---|
| M-1 | 17/10 (sáb) | Primeira medição, para os slides do PC1 | `CP1`, `CP2`, `DP1`, `RC1`, `RC2`, `RC3` |
| M-2 | 21/10 (qua) | Após o PC1: replanejar com o feedback; inclui DP2 da Fase 1 | Todas, com `DP2` (Fase 1) |
| M-3 | 23/10 (sex) | Congelamento de conteúdo; inclui DP2 da Fase 2 | Todas, com `DP2` (Fase 2) |
| M-4 | 25/10 (dom) | Pré-entrega | `CP1`, `CP2`, `DP1`, `RC1`, `RC2`, `RC3` |
| M-5 | 26/10 (seg) | Fechamento e lições para a Entrega 2 | `CP1`, `CP2`, `DP1`, `RC1`, `RC2`, `RC3` |
 
As medições de M-1 usam poucas issues concluídas e podem cair em "sem dados" ou oscilar muito; isso é esperado e deve constar na interpretação.
 
## 8. Evidências no Git
 
| Evidência | Onde |
|---|---|
| Issues | GitHub: Issues e suas respectivas labels |
| Commits e pull requests com revisão | GitHub: Pull requests |
| Horas, esforço planejado e autoavaliação | `assets/dados/gestao/` |
| Registro de Horas (consolidado) | `docs/gestao/horas.md` |
| Medições, interpretações e decisões | `docs/gestao/medicoes.md` |
| Script de coleta | `scripts/coletar_psm.py` |
| Uso de IA | `docs/gestao/uso_de_ia.md` |

<a id="historico-de-versoes"></a>
## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | Commit |
|---|---|---|---|---|---|
| 1.0 | 15/10/2026 | Criação do Plano de Medição | [Pedro Lucas](https://github.com/Pwdrinho) | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |
| 1.1 | 15/10/2026 | Atualização do Plano de Medição | [Pedro Lucas](https://github.com/Pwdrinho) | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |