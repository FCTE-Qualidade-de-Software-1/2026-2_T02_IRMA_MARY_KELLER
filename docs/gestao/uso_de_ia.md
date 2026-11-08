# Uso de IA

Versão 1.5

## 1. Para que serve

Registro de cada uso de ferramenta de IA no projeto. Serve de base para a declaração de uso de IA do artigo (ferramenta, tarefa e como a equipe conferiu e ajustou o resultado) e de evidência para a autoavaliação dos critérios de uso de IA da rubrica (F1-C10 e F2-C9), que alimenta a medição `DP2` do [Plano de medição](plano_de_medicao.md). Todo texto gerado por IA é revisado e reescrito pela equipe antes de entrar nos documentos, e nenhum documento contém emojis, figurinhas ou ícones.

## 2. Como registrar

Registre **no momento do uso**, não no fim do projeto: reconstruir o que foi feito semanas depois leva a declarações genéricas, que a rubrica pontua no nível mais baixo. Uma linha por tarefa e por issue.

| Coluna | O que preencher |
|---|---|
| Data | `AAAA-MM-DD` |
| Quem usou | Nome ou usuário do GitHub de quem usou a ferramenta |
| Ferramenta | Nome e, se souber, modelo ou versão |
| Tarefa | Uma das opções: revisão de texto; sugestão de estrutura; rascunho de texto; resumo de fonte; código ou script; diagrama; formatação LaTeX; outra (descrever) |
| Entregável ou issue | ID da issue e seção ou arquivo afetado (por exemplo, `#2`, seção de Metodologia) |
| Revisor | Outro membro, diferente de quem usou, que conferiu o resultado |
| Como a equipe conferiu e ajustou | De uma a duas frases concretas: o que foi conferido (fonte, norma, número, definição) e o que foi alterado |

## 3. Registro

| Data | Quem usou | Ferramenta | Tarefa | Entregável ou issue | Revisor | Como a equipe conferiu e ajustou |
|---|---|---|---|---|---|---|
| `2026-10-15` | [Pedro Lucas](https://github.com/Pwdrinho) | Claude | Estruturação dos artefatos | [#1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) | [Camila Cavalcante](https://github.com/CamilaSilvaC) | Foi conferida a estrutura de pastas e páginas com as entregas pedidas no Aprender3, e os nomes das seções foram ajustados ao padrão da disciplina. |
| `2026-10-16` | [Pedro Lucas](https://github.com/Pwdrinho) | Claude | Formatação dos Critérios para tabela | [#1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | Foi conferida cada linha da tabela com o texto original dos critérios no Aprender3, e os IDs e níveis que não batiam foram corrigidos. |
| `2026-10-18` | [Luisa de Souza](https://github.com/luisa12ll) | Claude | Correção de erros ortográfico e sugestão de estrutura | [#3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/3), `docs/fase-1/requisitos-de-avaliacao.md` | [José Augusto](https://github.com/JAugustoM) | Foram conferidas as correções contra o texto original para garantir que o sentido não mudou, e a estrutura sugerida foi adaptada aos requisitos R1 a R5. |
| `2026-10-18` | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | ChatGPT (OpenAI) | Apoio na estruturação e organização dos arquivos, especialmente na formatação das tabelas e revisão textual. | [#6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/6), `docs/fase-2` | [Pedro Lucas](https://github.com/Pwdrinho) | Foram conferidas as tabelas reformatadas contra o conteúdo original da Fase 2, e as definições foram reescritas com base na ISO/IEC 25023. |
| `2026-10-18` | [José Augusto](https://github.com/JAugustoM) | Gemini | Ajuda na estruturação do documento de escopo e correções ortográficas | [#5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/5) | [Pedro Lucas](https://github.com/Pwdrinho) | Foi conferido o escopo contra o propósito e os requisitos da Fase 1, e os trechos sugeridos foram reescritos para manter só a versão web em computadores. |
| `2026-10-18` | [Enzo Menali](https://github.com/menali17) | Codex | Cruzamento de documentos e formatação do MkDocs | [#2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/2), `docs/fase-1/produto-contexto.md` | [Luisa de Souza](https://github.com/luisa12ll) | Foram conferidos os links e as referências cruzadas no site gerado, e a formatação do MkDocs foi ajustada onde as tabelas quebravam. |
| `2026-10-18` | [Camila Cavalcante](https://github.com/CamilaSilvaC) | ChatGPT (OpenAI) | Apoio na estruturação, revisão ortográfica e verificação de links| [#7](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/7) `docs/fase-2`| [Enzo Menali](https://github.com/menali17) | Foram conferidos os links no site gerado e as correções ortográficas contra o texto original. |
| `2026-10-20` | [Enzo Menali](https://github.com/menali17) | Codex | Revisão crítica de priorização, escopo, ODS e recorte para o artigo | [#15](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/15), `docs/fase-1/requisitos-de-avaliacao.md`, `docs/fase-1/escopo-da-avaliacao.md` e artigo | [José Augusto](https://github.com/JAugustoM) | Foi conferida a priorização com a matriz da Fase 1 e os ODS com as metas oficiais da ONU, e os pontos sugeridos foram reescritos antes de entrar no artigo. |
| `2026-10-20` | [Enzo Menali](https://github.com/menali17) | Codex | Revisão da consistência entre propósito, stakeholders, decisões e recorte para o artigo | [#13](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/13), `docs/fase-1/produto-e-contexto.md` e artigo | [Luisa de Souza](https://github.com/luisa12ll) | Foi conferida a coerência entre propósito, stakeholders e decisões D1 a D3 nos dois documentos e no artigo, e as divergências apontadas foram corrigidas manualmente. |
| `2026-10-20` | [Enzo Menali](https://github.com/menali17) | Codex | Sugestão de estrutura e redação da visão geral da Fase 1 | `docs/fase-1/index.md` | [José Augusto](https://github.com/JAugustoM) | Foi conferida a visão geral com os documentos da Fase 1, e o texto foi reescrito para não antecipar conteúdo que não estava nas páginas. |
| `2026-10-20` | [Pedro Lucas](https://github.com/Pwdrinho) | NotebookLm(gemini) | Utilizei como fonte de analise de consistência do plano de medição com a PSM/CID, para evitar refatoração maior que o necessário | [#12](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/12) | [Camila Cavalcante](https://github.com/CamilaSilvaC) | Foram conferidos os apontamentos contra o guia PSM/CID e a ISO/IEC/IEEE 15939, e só as inconsistências confirmadas nas fontes foram corrigidas no plano. |
| `2026-11-06` | [Luisa de Souza](https://github.com/luisa12ll) | Claude Code (Claude Opus 5.5) | Código e script: automação do painel PSM/CID, com gráficos, diagrama do fluxo e conferência dos lançamentos | [#27](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/27), `assets/scripts/`, `assets/templates/horas_consolidadas.md.jinja` | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | Foram conferidos os valores do painel com as issues e com as fórmulas do Plano de medição. O texto gerado foi descartado e o texto original da equipe foi mantido. |
| `2026-11-07` | [Luisa de Souza](https://github.com/luisa12ll) | Claude Code (Claude Opus 5.5) | Revisão de texto: coerência entre páginas, links quebrados, numeração de tabelas, frases de pendência e erros de português | [#27](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/27), `docs/fase-1`, `docs/fase-2`, `docs/gestao` | [José Augusto](https://github.com/JAugustoM) | Foi conferida cada correção contra o Plano de medição, a WCAG 2.1 e os critérios de julgamento. Pontos que dependem de decisão da equipe não foram alterados. |
### 3.1 Regras

- Nunca incorporar texto, figura ou tabela gerados sem revisão e reescrita pela equipe.
- Dados, medições, referências e valores de limiares não podem vir da IA sem confirmação em fonte. Se a fonte não foi encontrada, o item fica como "a coletar".
- Trecho literal de qualquer fonte vai entre aspas e com citação.
- Não colocar nas ferramentas dados pessoais de entrevistados ou material de entrevista que identifique pessoas (LGPD).
- O tempo gasto conferindo o resultado da IA conta nas horas da issue (ver [Registro de Horas](horas.md)).

### 3.2 Como escrever a última coluna

Exemplos de redação com o nível de detalhe esperado. Não são registros reais.

- Insuficiente: "Revisado." / "Ficou bom."
- Esperado: "Conferimos as definições contra o texto da norma citada e reescrevemos dois parágrafos que usavam termos que não se aplicam ao produto."

O resultado dessa conferência é a evidência usada pela dupla revisora para atribuir o nível dos critérios F1-C10 e F2-C9 no `autoavaliacao.csv`.

## 4. Declaração para o artigo

A declaração do artigo é montada a partir da tabela acima, com a estrutura abaixo. Cada campo entre colchetes é substituído pela informação do registro:

> Declaração de uso de IA. Foram utilizadas as ferramentas [ferramenta(s)] para [tarefa(s)] em [seções ou artefatos]. A equipe conferiu [o que foi conferido] com base em [fontes] e ajustou [o que foi alterado] antes de incorporar o resultado. Nenhum conteúdo foi incorporado sem revisão por membro da equipe.

A última frase só deve permanecer se o registro a sustentar integralmente.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|---|---|---|---|---|
| 1.0 | 14/10/2026 | Criação do registro | [Pedro Lucas](https://github.com/Pwdrinho) | [Enzo Menali](https://github.com/menali17) |
| 1.1 | 15/10/2026 | Colunas de issue e revisor, regras de preenchimento, conferência antes das medições e modelo de declaração | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.2 | 20/10/2026 | Registro do apoio de IA na revisão da priorização, do escopo, dos ODS e do recorte para o artigo | [Enzo Menali](https://github.com/menali17) | [Luisa de Souza](https://github.com/luisa12ll) |
| 1.3 | 20/10/2026 | Registro do apoio de IA na revisão do propósito, dos stakeholders e do recorte para o artigo | [Enzo Menali](https://github.com/menali17) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.4 | 20/10/2026 | Registro do apoio de IA na estruturação da visão geral da Fase 1 | [Enzo Menali](https://github.com/menali17) | [Camila Cavalcante](https://github.com/CamilaSilvaC) |
| 1.5 | 07/11/2026 | Registro do apoio de IA no tema da GitPage, no painel PSM/CID, na revisão de coerência e no README; remoção de anotações internas | [Luisa de Souza](https://github.com/luisa12ll) | [Pedro Lucas](https://github.com/Pwdrinho) |
