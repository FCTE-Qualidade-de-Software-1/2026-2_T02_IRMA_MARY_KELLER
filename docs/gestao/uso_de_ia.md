# Uso de IA

Versão 1.1

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
| `2026-10-15` | [Pedro Lucas](https://github.com/Pwdrinho) | Claude | Estruturação dos artefatos | [#1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1) |  |  |
| `2026-10-16` | [Pedro Lucas](https://github.com/Pwdrinho) | Claude | Formatação dos Critérios para tabela | [#1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/1)   |  |  |  |
| `2026-10-18` | [Luisa de Souza](https://github.com/luisa12ll) | Claude | Correção de erros ortográfico e sugestão de estrutura | [#3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/3), `docs/fase-1/requisitos-de-avaliacao.md` | | |
| `2026-10-18` | [José Augusto](https://github.com/JAugustoM) | Gemini | Ajuda na estruturação do documento de escopo e correções ortográficas | [#5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/5) | | |
| `2026-10-18` | [Enzo Menali](https://github.com/menali17) | Codex | Cruzamento de documentos e formatação do MkDocs | [#2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/2), `docs/fase-1/produto-contexto.md` | | |
| `2026-10-18` | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | ChatGPT (OpenAI) |  Apoio na estruturação e organização dos arquivos, especialmente na formatação das tabelas e revisão textual.   |[#6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/6), `docs/fase-2` |  |  |
| `2026-10-19` | [Camila Silva](https://github.com/CamilaSilvaC) | ChatGPT (OpenAI) | Ajuda na estruturação dos documentos e correções| [#7](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/7), `docs/fase-2` |  |  |

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

<!-- A Conferir-->
O resultado dessa conferência é a evidência usada pela dupla revisora para atribuir o nível dos critérios F1-C10 e F2-C9 no `autoavaliacao.csv`.

## 4. Declaração para o artigo

Preencher em 23/10 (issue A-06), a partir da tabela acima. Modelo de estrutura, em que todo campo entre colchetes deve ser substituído por informação do registro:

> Declaração de uso de IA. Foram utilizadas as ferramentas [ferramenta(s)] para [tarefa(s)] em [seções ou artefatos]. A equipe conferiu [o que foi conferido] com base em [fontes] e ajustou [o que foi alterado] antes de incorporar o resultado. Nenhum conteúdo foi incorporado sem revisão por membro da equipe.

A última frase só deve permanecer se o registro a sustentar integralmente.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | Commit |
|---|---|---|---|---|---|
| 1.0 | 14/10/2026 | Criação do registro | [Pedro Lucas](https://github.com/Pwdrinho) | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |
| 1.1 | 15/10/2026 | Colunas de issue e revisor, regras de preenchimento, conferência antes das medições e modelo de declaração | [Pedro Lucas](https://github.com/Pwdrinho) | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |
