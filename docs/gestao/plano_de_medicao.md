# Plano de medição PSM/CID

Versão 1.0

## 1. Finalidade

Acompanhar a execução do projeto, como os marcos principais sendo Entrega 1 (26/10/2026) e Entrega 2 (18/11/2026), passando pelos pontos de controle PC1({19 - 21}/10/2026) e PC2({04 - 09}/11/2026) com medidas do modelo PSM/CID nas três categorias exigidas: *Calendário e Progresso*, *Desempenho dos Processos* e *Recursos e Custos*. Cada medição é registrada com sua interpretação e com as decisões de gestão que ela provocou (ver [Medições e decisões](medicoes.md)).

## 2. Necessidades de informação

| Objetivo | Categoria | Pergunta de gestão |
|---|---|---|
| O1 | Calendário e Progresso | Vamos entregar os slides do Pontos de Controle e a Entregas no ritmo planejado? |
| O2 | Desempenho dos Processos | O processo de produzir e revisar gera entregas que atendem aos critérios da professora, sem muito retrabalho? |
| O3 | Recursos e Custos | O esforço gasto confere com o planejado e está equilibrado entre os membros? |


### 2.1 Calendário e Progresso

#### O1: verificar se a equipe está concluindo as atividades planejadas dentro do prazo.

|Categoria | Medida Base QME | Medida Derivada | Fórmula | Indicador |
|---|---|---|---|---|
| Progresso das atividades | [Atividades](#unidade-de-trabalho) concluídas (Ac) <br> [Atividades](#unidade-de-trabalho) planejadas (Ap) | Percentual de progresso planejado cumprido. (Ppc) | Ppc = (Ac ÷ Ap)  × 100	|Adequado: 90% <= Ppc <= 100% <br> Bom: 80% <= Ppc < 90% <br> Insuficiente: 60% <= Ppc < 80% <br> Crítico: Ppc < 60% |
| Cumprimento do prazo | [Atividades](#unidade-de-trabalho) concluídas no prazo ÷ [Atividades](#unidade-de-trabalho) concluídas × 100 | Adequado: 90% - 100% ao fim do projeto <br> Bom: 80% -90% ao fim do projeto <br> Insuficiente: 60% - 70% ao fim do projeto <br> Crítico: Menos de 60% ao fim do projeto |
| Desvio de prazo | Data real de conclusão − data planejada	0 dias para marcos críticos
| Entregas concluídas | versus comprometidas	Itens aceitos ÷ itens previstos para o período × 100	≥ 90% em cada revisão

## 3. Unidade de trabalho e convenções

<a id="unidade-de-trabalho"></a>

- A unidade de trabalho é a **issue** do GitHub. O ID vai no título (por exemplo, `[F1-02]`), e o corpo traz **Janela** (data prevista) e **Estimativa** (horas)
- Marcos: **PC1 (slides 18/10)** e **E1 26/10**.

- Equipe em três duplas (A, B e C). A revisão é em anel: o trabalho da Dupla A é revisado pela B, o da B pela C e o da C pela A.
- Custo monetário: nenhum. O custo é medido em horas-pessoa.









## 4. Medidas

Os nomes dos conceitos mensuráveis seguem o catálogo do PSM; confirmar com o material da disciplina. Os limiares são propostas iniciais da equipe e podem ser revistos com registro na tabela de decisões.

| Id | Categoria | Conceito mensurável | Entidade | Medida base | Medida derivada | Indicador e limiares | Coleta |
|---|---|---|---|---|---|---|---|
| CP1 | Calendário e Progresso | Milestone Completion | Marco (PC1, E1) | data de conclusão do marco (fechamento da última issue); data prevista | marcos concluídos no prazo / marcos com prazo vencido | Verde: 100%. Vermelho: abaixo de 100% | Automática |
| CP2 | Calendário e Progresso | Work Unit Progress | Issue | issues fechadas; issues previstas até a data (campo Janela) | fechadas / previstas até a data | Verde: 100% ou mais. Amarelo: 80 a 99%. Vermelho: abaixo de 80% | Automática |
| CP3 | Calendário e Progresso | Milestone Completion (desvio de prazo) | Issue | data real de fechamento; data prevista | desvio em dias por issue (média, máximo, quantas passam de 1 dia) | Verde: nenhuma acima de 1 dia. Amarelo: 1 a 2. Vermelho: 3 ou mais | Automática |
| DP1 | Desempenho dos Processos | Process Efficiency | Issue | issues reabertas; issues com label `correcao`; issues fechadas | (reabertas + correção) / fechadas | Verde: abaixo de 20%. Amarelo: 20 a 39%. Vermelho: 40% ou mais | Automática |
| DP2 | Desempenho dos Processos | Process Effectiveness | Critério da professora (F1-C1 a C11; F2-C1 a C12) | nível atingido na autoavaliação (1 Insuficiente, 2 Satisfatório, 3 Bom, 4 Excelente) | critérios abaixo de Bom; critérios no nível Excelente (%), por fase | Verde: nenhum abaixo de Bom. Amarelo: 1 a 2. Vermelho: 3 ou mais. Meta da equipe: 100% no nível Excelente na E1 | Semiautomática (CSV preenchido na revisão) |
| DP3 | Desempenho dos Processos | Process Compliance | Pull request | PRs integrados; PRs integrados com revisão de outra pessoa | revisados / integrados | Verde: 100%. Amarelo: 80 a 99%. Vermelho: abaixo de 80% | Automática |
| RC1 | Recursos e Custos | Personnel Effort | Issue | horas reais; horas planejadas | desvio = reais / planejadas menos 1, nas issues concluídas | Verde: nenhuma fora de ±20%. Amarelo: 1 a 2. Vermelho: 3 ou mais | Automática |
| RC2 | Recursos e Custos | Personnel Effort | Membro | horas por membro | percentual do total e desvio em relação à média | Verde: ninguém além de ±50% da média. Amarelo: 1 pessoa. Vermelho: 2 ou mais | Automática (base da Tabela de contribuição) |

Notas:

- **DP2** é cobrada a partir de 21/10 para a Fase 1 e de 23/10 para a Fase 2. Antes disso a autoavaliação ainda não existe.
- **DP3** só existe se a equipe trabalhar com pull requests; o fluxo está definido nas issues G-01 e G-04.
- **RC2** alimenta o percentual de esforço da Tabela de contribuição, que precisa somar 100%.

## 5. Regras de decisão

| Situação | Decisão |
|---|---|
| CP2 amarelo | A dupla dona das issues atrasadas informa novo prazo na própria issue e reordena o trabalho em até 24 horas |
| CP2 vermelho ou CP1 vermelho | Reunião de 15 minutos em até 24 horas; replanejar cortando ou adiando o que não pesa nos critérios, e redistribuir issues entre duplas; registrar a decisão |
| CP3 amarelo ou vermelho | Registrar a causa do atraso e reestimar as issues que dependem da atrasada |
| DP1 amarelo ou vermelho | Reforçar o critério de aceite e exigir revisão antes de fechar a issue |
| DP2 com critério abaixo de Bom | Abrir issue `correcao` por critério e priorizá-las antes de qualquer trabalho novo |
| DP3 abaixo de 100% | Nenhuma issue é fechada sem revisão da dupla revisora; pendências revisadas no mesmo dia |
| RC1 fora de ±20% | Reestimar issues parecidas e registrar o motivo do desvio |
| RC2 fora de ±50% da média | Rebalancear as próximas issues entre as duplas |

## 6. Procedimento de medição

Responsável pela execução: Dupla C. Todos os membros lançam as horas até as 12h do dia da medição.

1. Cada membro registra suas horas em `assets/dados/gestao/horas/<usuario>.csv` (colunas `data,atividade,horas`; atividade é o ID da issue).
2. A Dupla C roda `python3 scripts/coletar_psm.py --data AAAA-MM-DD` na raiz do repositório e cola a tabela no registro de `docs/gestao/medicoes.md`.
3. Na revisão dos critérios, as duplas registram os níveis em `assets/dados/gestao/autoavaliacao.csv` (colunas `data,criterio,nivel,evidencia`).
4. A Dupla C interpreta cada medida amarela ou vermelha e registra a decisão na tabela de decisões, abrindo uma issue de ação quando houver trabalho a fazer.
5. O resultado é comunicado ao grupo no mesmo dia e commitado por pull request.

Pontos de medição:

| Id da issue | Data | Finalidade |
|---|---|---|
| M-1 | 17/10 (sáb) | Primeira medição, para os slides do PC1 |
| M-2 | 21/10 (qua) | Após o PC1: replanejar com o feedback; inclui DP2 da Fase 1 |
| M-3 | 23/10 (sex) | Congelamento de conteúdo; inclui DP2 da Fase 2 |
| M-4 | 25/10 (dom) | Pré-entrega |
| M-5 | 26/10 (seg) | Fechamento e lições para a Entrega 2 |

## 7. Evidências no Git

| Evidência | Onde |
|---|---|
| Issues, milestones e quadro de acompanhamento | GitHub: Issues, Milestones e Projects (quadro "Entrega 1") |
| Commits e pull requests com revisão | GitHub: Pull requests |
| Horas, esforço planejado e autoavaliação | `assets/dados/gestao/` |
| Medições, interpretações e decisões | `docs/gestao/medicoes.md` |
| Script de coleta | `scripts/coletar_psm.py` |
| Uso de IA | `docs/gestao/uso_de_ia.md` |

## 8. Limitações das medidas

- A equipe tem 6 pessoas e a janela é curta: com poucas issues fechadas, os percentuais oscilam muito. Interpretar sempre junto com os dados brutos.
- As horas são autodeclaradas.
- A granularidade das issues pode esconder progresso parcial.
- A DP2 é autoavaliação e tende a ser otimista; a revisão cruzada por outra dupla reduz esse viés.
- Os limiares são propostas iniciais, ainda não calibradas com dados do projeto.

<a id="historico-de-versoes"></a>
## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | Commit |
|---|---|---|---|---|---|
| 1.0 | 15/10/2026 | Criação do Plano de Medição | [Pedro Lucas](https://github.com/Pwdrinho) | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |
|  |  |  |  | | |