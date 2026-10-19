[← Visão geral da Fase 2](index.md)

# Escala de julgamento e limiares

A escala de produto permanece **0 — Crítico, 1 — Insuficiente, 2 — Satisfatório, 3 — Bom**. Ela difere da rubrica acadêmica da professora. Regras e agregação abaixo são propostas, com revisão humana pendente.

## Parâmetros e condições de aplicação

Os limiares precisam de justificativa; o [registro de IA](../gestao/uso_de_ia.md) também exige confirmação em fonte para valores de referência. Não há no material consultado fonte para um tempo universal, um consumo universal ou um percentual mínimo de autonomia. Portanto, **não preencher esses campos com números arbitrários**.

As regras abaixo são explícitas, mas parametrizadas. Elas se tornam critérios executáveis assim que a equipe preencher a Tabela 1 com valores sustentados em fonte ou decisão documentada do cenário. Não apresentar esta seção como atendimento completo do F2-C5 enquanto houver parâmetro obrigatório vazio. A Fase 3 pode detalhar instrumentos e protocolos; não deve adiar a justificativa das faixas exigidas na Fase 2 até depois de medir resultados finais.

**Tabela 1 — Parâmetros que precisam ser fundamentados antes da coleta final.**

| Aplicação | Valores a registrar | Evidência exigida |
|---|---|---|
| M1, cada etapa/rede | `B < A < L`: limite de bom desempenho, máximo aceitável e máximo tolerável | Prazo de uso aceito para o cenário ou literatura aplicável à mesma interação, com justificativa de adaptação; marcos e unidade. |
| M2.CPU/RAM/REDE, cada fluxo/configuração | `B < A < L`, na unidade da medida | Capacidade disponível e reserva operacional para CPU/RAM; orçamento de acesso e conteúdo padronizado para rede. Registrar responsável pela decisão e cálculo. |
| M3.AMB/JAN | Lista de combinações essenciais e complementares | Matriz de escopo acordada antes de testar, com justificativa e responsáveis. |
| M4, cada recurso | Lista de combinações essenciais, complementares e checklist aplicável | R4, escopo, critérios WCAG selecionados e tecnologias assistivas efetivamente viáveis. |
| M5, por tarefa e conjunto | `I < A < B`, em %, dentro de 0 a 100 | Menor autonomia tolerável, autonomia aceitável para D3 e meta de bom desempenho; decisão documentada do cenário ou evidência aplicável. |
| Todas | Plano obrigatório, repetições, participantes, timeout e validade | Protocolo aprovado e versionado antes da coleta; registrar ausências e exclusões. |

*Fonte: lacunas reais da branch e proposta de decisão prévia, sem atribuição de limiares de produto à ISO.*

Para cada linha preenchida, registrar valor, unidade, fonte exata, justificativa, data, responsável e revisor. Como o cenário escolar é hipotético, uma decisão da equipe deve ser identificada como **critério proposto para o cenário hipotético**, não como requisito recebido de uma escola real.

## Plano e cobertura

Planejado é o conjunto completo de ensaios previstos. Essencial é a combinação cujo sucesso é necessário para considerar a questão atendida. Complementar é a combinação adicional que diferencia atendimento satisfatório de bom desempenho; sua avaliação também é obrigatória no plano aprovado. Cobertura completa exige todas as observações previstas validamente obtidas, inclusive complementares e repetições. A classificação é fixada antes dos testes; um resultado desfavorável não autoriza retirar combinações do plano.

Cada grupo M3/M4 contém pelo menos uma combinação essencial. Grupos exclusivamente complementares exigiriam regra própria previamente aprovada e não recebem automaticamente esta escala. Os grupos são definidos na [Tabela 7 das métricas](metricas.md#unidades-de-observacao-e-grupos-de-julgamento).

## Regras por métrica

Quando houver repetições em M3/M4, a classificação de cada combinação segue a [regra de repetições das métricas](metricas.md#repeticoes-resumos-e-falhas). A pontuação do grupo utiliza combinações distintas já classificadas; execuções repetidas não são somadas ao denominador como combinações adicionais. A cobertura incompleta mantém a nota completa inconclusiva, sem ocultar falhas parciais. A regra impeditiva de M4 preserva sua precedência.

A Tabela 2 define intervalos sem sobreposição. Em M1/M2, `x` é a mediana do grupo conforme as fichas; em M5, `p` é o percentual válido por tarefa ou conjunto. A regra de limite rígido de RAM, quando aplicável, precisa estar definida no protocolo antes da pontuação. M1/M2 usam “menor é preferível” apenas quando o fluxo é funcional e comparável.

**Tabela 2 — Conversão de resultados válidos em pontuação.**

| Medida | 0 — Crítico | 1 — Insuficiente | 2 — Satisfatório | 3 — Bom |
|---|---|---|---|---|
| M1, M2.CPU, M2.RAM, M2.REDE, por grupo de julgamento | `x > L`, ou bloqueio impeditivo do fluxo relacionado ao atributo e documentado | `A < x ≤ L` | `B < x ≤ A` | `x ≤ B` |
| M3.AMB, M3.JAN, cada M4 | Nenhuma combinação essencial bem-sucedida, com ao menos uma essencial validamente ensaiada | Alguma essencial bem-sucedida e alguma essencial falhou | Todas as essenciais bem-sucedidas, mas há falha em complementar | Todas as combinações do plano aprovado bem-sucedidas |
| M5, por tarefa e conjunto | `p < I` | `I ≤ p < A` | `A ≤ p < B` | `p ≥ B` |

*Fonte: proposta de regras de decisão para a escala já presente no projeto. Os parâmetros não são limites normativos nem resultados coletados.*

M3/M4 exigem pelo menos uma combinação essencial por grupo de julgamento aplicável. Se não houver complementares, o sucesso de todas as essenciais dá 3. Os percentuais continuam sendo apresentados, mas, nesses casos, o julgamento considera também **quais combinações falharam**. Um percentual alto não compensa uma barreira em tarefa essencial.

M4 recebe 0 no grupo se uma barreira documentada impede completamente uma tarefa essencial para o perfil assistivo em avaliação. Essa regra prevalece sobre o percentual. A gravidade da barreira deve ser definida no protocolo; não classificar todo defeito cosmético como impeditivo.

Não atribuir automaticamente falha de produto a indisponibilidade do laboratório, incompatibilidade entre SO e ferramenta ou interrupção externa. Registrar dados inválidos/incompletos e tratar como inconclusivo. Falha de execução efetivamente observada na plataforma não é dado ausente e permanece no denominador. Para tempo, reportar falhas junto à mediana: uma mediana rápida dos sucessos não anula fluxo essencial que não conclui.

## Ordem de aplicação das regras

1. Conferir validade, parâmetros aprovados, elegibilidade e cobertura de cada grupo. Com `N = 0` em M3–M5 não se calcula percentual ou pontuação; sem execuções válidas em M1/M2, o grupo também é inconclusivo.
2. Aplicar primeiro as regras impeditivas documentadas ao atributo: bloqueio de etapa essencial atribuível ao produto em M1/M2 ou bloqueio completo de tarefa essencial para o perfil assistivo em M4 recebe 0 no grupo com cobertura completa. Outros defeitos seguem a Tabela 2.
3. Nos demais grupos completos, aplicar as faixas ao resumo M1/M2, às combinações de M3/M4 ou ao percentual M5; depois agregar pelo mínimo.
4. Com dados obrigatórios ausentes, a nota completa do grupo, questão ou objetivo afetado permanece inconclusiva. Um bloqueio ou grupo com nota 0 já demonstrado é relatado como **não atendimento demonstrado em resultado parcial**; a lacuna não oculta essa evidência nem autoriza nota final 0 com cobertura incompleta.

## Agregação: medidas → questões → objetivos

A agregação proposta utiliza o mínimo das pontuações para evitar compensação entre atributos essenciais. A escala é ordinal: não calcular uma média de notas e tratá-la como distância física entre níveis.

1. Calcular cada medida por grupo de julgamento obrigatório, preservando valores brutos, falhas e cobertura.
2. O escore de uma subquestão é o mínimo dos escores dos seus grupos obrigatórios. Aplicar as regras impeditivas antes da agregação.
3. `S(Q1) = min(escores M1 de todas as etapas, ambientes e redes obrigatórios)`.
4. `S(Q2) = min(S(Q2.1), S(Q2.2), S(Q2.3))`.
5. `S(Q3) = min(S(Q3.1), S(Q3.2))`.
6. `S(Q4) = min(S(Q4.1), S(Q4.2), S(Q4.3), S(Q4.4))`.
7. `S(Q5) = min(escores M5 de cada tarefa essencial e do conjunto)`.
8. `S(G1) = min(S(Q1), S(Q2))`; `S(G2) = S(Q3)`; `S(G3) = min(S(Q4), S(Q5))`.

Se faltar dado obrigatório válido, o resultado completo da questão e do objetivo é **inconclusivo**. É possível informar resultados parciais e uma falha já demonstrada, mas sem calcular nota final ignorando a lacuna. Dimensão genuinamente não aplicável precisa ser justificada e retirada do plano antes da coleta; não retirar atributo difícil de medir depois de ver o resultado.

Tradução comum: **3 ou 2 = atende; 1 = atende parcialmente; 0 = não atende; sem pontuação = inconclusivo**. Em nota 1, “atende parcialmente” não autoriza recomendação irrestrita: explicitar a restrição observada. Não produzir uma nota global única da plataforma; a issue pede julgamento por objetivo.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | 
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 18/10/2026 | Estruturação da escala de pontuação e dos critérios de julgamento das métricas, com identificação dos limiares pendentes de fundamentação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho)| 
| 1.1 | 19/10/2026 | Formalização das regras parametrizadas, barreiras impeditivas, cobertura e agregação por objetivo; limiares ainda pendentes. | Camila Silva (apoio de Codex) | Revisão humana pendente |
| 1.2 | 19/10/2026 | Ajustes complementares da issue #7: observações e grupos, repetições, cobertura, hipóteses e figuras sincronizadas, com apoio de Codex. | Camila Silva | Revisão humana pendente |
| 1.3 | 19/10/2026 | Vinculação da pontuação de M3/M4 à classificação prévia das combinações repetidas. | Camila Silva | Revisão humana pendente |


---

[Navegar pela Fase 2](index.md)
