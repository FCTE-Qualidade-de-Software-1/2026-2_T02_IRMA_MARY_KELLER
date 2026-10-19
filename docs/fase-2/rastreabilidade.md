[← Visão geral da Fase 2](index.md)

# Rastreabilidade Fase 1 → Fase 2

A Tabela 1 explicita a origem de cada objetivo e atende à rastreabilidade exigida no F2-C11. Os stakeholders, prioridades e decisões foram extraídos da matriz de requisitos da Fase 1, não de medições.

**Tabela 1 — Rastreabilidade entre requisitos, stakeholders, decisões e elementos GQM.**

| Fase 1 | Característica: subcaracterística | Prioridade da F1 | Stakeholders documentados | Decisão da F1 | Objetivo / Questão / Hipótese / Métrica |
|---|---|---|---|---|---|
| R1 | Eficiência de desempenho: comportamento temporal | Alta | Estudantes; coordenação e professores | D1 | G1 / Q1 / H1 / M1 |
| R2 | Eficiência de desempenho: utilização de recursos | Alta | Estudantes; responsáveis | D1 | G1 / Q2.1–Q2.3 / H2.1–H2.3 / M2.CPU, M2.RAM, M2.REDE |
| R3 | Portabilidade: adaptabilidade | Alta | Estudantes; coordenação e professores | D1 | G2 / Q3.1–Q3.2 / H3.1–H3.2 / M3.AMB, M3.JAN |
| R4 | Usabilidade: acessibilidade | Alta | Estudantes com baixa visão ou leitor de tela; professores; responsáveis | D2 | G3 / Q4.1–Q4.4 / H4.1–H4.4 / M4.TEC, M4.LEI, M4.AMP, M4.CON |
| R5 | Usabilidade: apreensibilidade | Média | Estudantes novos; professores | D3 | G3 / Q5 / H5 / M5 |

*Fonte: `docs/fase-1/requisitos-de-avaliacao.md`, seção 4; associação G/Q/M especificada nesta Fase 2.* A equipe avaliadora é interessada transversal na decisão D4, conforme registrado na Fase 1.



**Limitação de D1:** o escopo é web em computadores. Os resultados não permitem decidir entre aplicativo e navegador nem generalizar para celulares. A divergência com o cenário móvel da Fase 1 precisa ser revista pela equipe; esta proposta não amplia o escopo.

## Relação com a rubrica acadêmica

A Tabela 2 relaciona evidências propostas e condições restantes; não declara aceite.

**Tabela 2 — Relação entre os critérios da Fase 2, as evidências documentais e as pendências.**

| Critério | Evidência documental | Condição restante |
|---|---|---|
| F2-C1 | G1–G3 preservados e associados à Fase 1 | Revisar coerência do contexto web com cenário de D1. |
| F2-C2 | [Questões e hipóteses](questoes-hipoteses.md): questões qualitativas por atributo | Ratificar cobertura e subidentificadores. |
| F2-C3 | Hipótese por atributo e fundamentação individual; verificação quantitativa condicionada aos parâmetros | Equipe assumir ou ajustar expectativas antes de medir. |
| F2-C4 | [Fichas M](metricas.md) com campos completos | Conferir instrumentos e correspondência normativa específica. |
| F2-C5 | [Critérios de julgamento](criterios-julgamento.md) e regras de agregação | Preencher e fundamentar todos os parâmetros obrigatórios; sem isso, não marcar concluído. |
| F2-C6 | [Figuras 1–4 e matriz](grafico-gqm.md) | Conferir a legibilidade das quatro figuras na página publicada. |
| F2-C7/F2-C8 | Navegação, títulos, chamadas, numeração, legendas e fontes | Conferir a numeração local das tabelas, as chamadas no texto e a renderização final. |
| F2-C9 | Registro objetivo de IA | Revisão humana real e descrição concreta dos ajustes. |
| F2-C10 | Menu sem duplicação e páginas sincronizadas | Build local executado com sucesso em 19/10/2026, com MkDocs 1.6.1. Há avisos preexistentes de links fora da Fase 2. Publicação autorizada pela equipe e conferência final de links e figuras no endereço publicado permanecem pendentes. |
| F2-C11 | R1→Q1, R2→Q2, R3→Q3, R4→Q4, R5→Q5 e interessados existentes | Equipe decidir sobre a divergência de D1; limitação já declarada. |
| F2-C12 | Termos operacionais do contexto Khan Academy | Remover alegações normativas ou generalizações não sustentadas. |

*Fonte: `docs/criterios/fase2.md` e especificação GQM desta fase.*

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | 
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 18/10/2026 | Elaboração da matriz de rastreabilidade entre os requisitos da Fase 1, stakeholders, características de qualidade e elementos GQM da Fase 2. |[Geovanna Umbelino](https://github.com/GeovannaUmbelino) |[Pedro Lucas](https://github.com/Pwdrinho) | 
| 1.1 | 19/10/2026 | Detalhamento dos desdobramentos, limitação de D1 e evidências/pendências da rubrica. | Camila Silva (apoio de Codex) | Revisão humana pendente |
| 1.2 | 19/10/2026 | Ajustes complementares da issue #7: observações e grupos, repetições, cobertura, hipóteses e figuras sincronizadas, com apoio de Codex. | Camila Silva | Revisão humana pendente |
| 1.3 | 19/10/2026 | Atualização das pendências de numeração local e da evidência do build MkDocs 1.6.1. | Camila Silva | Revisão humana pendente |

---

[Navegar pela Fase 2](index.md)
