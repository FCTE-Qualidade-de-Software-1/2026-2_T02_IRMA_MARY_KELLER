# Fase 2 — Especificação da avaliação (GQM)

A Fase 2 transforma as características priorizadas na [Fase 1](../fase-1/index.md) em uma estrutura de medição por meio do método *Goal–Question–Metric* (GQM). Cada objetivo de medição é desdobrado em questões de avaliação, relacionadas a hipóteses de investigação e respondidas por métricas. Para interpretar as medidas, também são previstos níveis de pontuação e critérios de julgamento.

Nesta etapa, são especificados **3 objetivos (G1–G3), 11 questões (Q1–Q11), 11 hipóteses (H1–H11) e 14 métricas (M1–M14)**. A Fase 2 estabelece como a qualidade será avaliada; os resultados das medições permanecem **a coletar na Fase 4**.

## Organização da Fase 2

A **Tabela 1** apresenta os temas da documentação, a pessoa responsável pela issue de especificação GQM e o acesso a cada página.

**Tabela 1 — Organização e responsáveis pela documentação da Fase 2.**

| **Tema** | **Responsável** | **Página** |
| :--- | :--- | :--- |
| Objetivos de medição (G1–G3) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Objetivos de medição](objetivos.md) |
| Questões e hipóteses (Q1–Q11 / H1–H11) | [Camila Cavalcante](https://github.com/CamilaSilvaC)  | [Questões e hipóteses](questoes-hipoteses.md) |
| Especificação das métricas (M1–M14) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Métricas](metricas.md) |
| Níveis de pontuação e critérios de julgamento | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) e [Camila Cavalcante](https://github.com/CamilaSilvaC)  | [Critérios de julgamento](criterios-julgamento.md) |
| Hierarquia e representação gráfica GQM | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) e [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Gráfico GQM](grafico-gqm.md) |


*Fonte: organização da documentação das [issues](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues).* A indicação de responsabilidade refere-se à elaboração da documentação desta issue; não substitui a revisão coletiva nem atribui a outras pessoas tarefas não confirmadas.

## Delimitação e relação com a Fase 1

A avaliação da Khan Academy foi proposta, na Fase 1, para apoiar um cenário hipotético de decisão de uma coordenação de escola pública sobre adoção e condições de acesso à plataforma. O estudo considera restrições de recursos computacionais e necessidades específicas de estudantes, por meio de avaliação externa (*caixa-preta*).

As características de qualidade priorizadas, com base na **ISO/IEC 25010:2011**, são **eficiência de desempenho**, **portabilidade** e **usabilidade**. Elas se desdobram nos seguintes requisitos:

- **R1 — Comportamento temporal** e **R2 — Utilização de recursos**, associados ao objetivo **G1**;
- **R3 — Adaptabilidade**, associado ao objetivo **G2**;
- **R4 — Acessibilidade** e **R5 — Apreensibilidade**, associados ao objetivo **G3**.

Conforme o [escopo da Fase 1](../fase-1/escopo-da-avaliacao.md), a avaliação contempla **somente a versão web em computadores**, sem aplicativos nativos ou navegadores de dispositivos móveis. Os fluxos são `FL1` (navegação em cursos), `FL2` (videoaulas), `FL3` (exercícios) e `FL4` (consulta ao progresso pelo próprio estudante). G1 e G3 avaliam `FL1` a `FL3`; G2 avalia `FL1` a `FL4`. Painéis de pais, responsáveis, professores e administradores permanecem fora do objeto. Os ambientes direcionados são `A1` (Windows e Chrome), `A2` (Windows e Firefox), `A3` (macOS e Safari) e `A4` (Ubuntu e Firefox), com NVDA, VoiceOver, Orca e navegação por teclado nas combinações previstas. As condições detalhadas de coleta serão confirmadas no planejamento dos ensaios.

As métricas da Fase 2 são **adaptações propostas tomando a ISO/IEC 25023:2016 como referência**. Seus nomes e fórmulas não devem ser interpretados como transcrições literais da norma. A correspondência com medidas normativas específicas ainda precisa de conferência documental.


## Referências

- [Requisitos de avaliação — Fase 1](../fase-1/requisitos-de-avaliacao.md). Matriz de requisitos R1–R5, stakeholders e decisões documentadas pela equipe.
- [Escopo da avaliação — Fase 1](../fase-1/escopo-da-avaliacao.md). Plataformas, módulos, ambientes e limites do estudo.
- **ISO/IEC 25010:2011** — *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*.
- **ISO/IEC 25023:2016** — *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality*.
- **Basili, V. R.; Caldiera, G.; Rombach, H. D. (1994).** *The Goal Question Metric Approach*. Referência metodológica para a estrutura GQM.
- [Critérios de avaliação da Fase 2](../criterios/fase2.md), disciplina Qualidade de Software 1, UnB/FGA, 2026/2.


## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 17/10/2026 | Estruturação da Fase 2, apresentação da metodologia GQM e organização das seções da documentação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |[Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 20/10/2026 | Ajustes na especificação e organização | [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.2 | 21/10/2026 | Alinhamento da visão geral aos fluxos, ambientes e exclusões definidos na Fase 1. | [Enzo Menali](https://github.com/menali17) | |
