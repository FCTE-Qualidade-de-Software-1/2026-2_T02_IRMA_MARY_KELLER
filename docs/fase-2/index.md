# Fase 2: Especificação da avaliação (GQM)

**Versão 1.4**

A Fase 2 transforma as características priorizadas na [Fase 1](../fase-1/index.md) em uma estrutura de medição por meio do método *Goal–Question–Metric* (GQM) [S5](#s5). Cada objetivo de medição é desdobrado em questões de avaliação, relacionadas a hipóteses de investigação e respondidas por métricas. Para interpretar as medidas, também são previstos níveis de pontuação e critérios de julgamento.

Nesta etapa, são especificados **3 [objetivos](objetivos.md#objetivo) (G1–G3), 11 [questões](questoes-hipoteses.md) (Q1–Q11), 11 [hipóteses](questoes-hipoteses.md) (H1–H11) e 14 métricas (M1–M14)**. A Fase 2 estabelece como a qualidade será avaliada; os resultados das medições permanecem **a coletar na Fase 4**.

## Organização da Fase 2

A **Tabela 1** apresenta os temas da documentação, a pessoa responsável pela issue de especificação GQM e o acesso a cada página.

| **Tema** | **Responsável** | **Página** |
| :--- | :--- | :--- |
| Objetivos de medição (G1–G3) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Objetivos de medição](objetivos.md) |
| Questões e hipóteses (Q1–Q11 / H1–H11) | [Camila Cavalcante](https://github.com/CamilaSilvaC)  | [Questões e hipóteses](questoes-hipoteses.md) |
| Especificação das métricas (M1–M14) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Métricas](metricas.md) |
| Níveis de pontuação e critérios de julgamento | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) e [Camila Cavalcante](https://github.com/CamilaSilvaC)  | [Critérios de julgamento](criterios-julgamento.md) |
| Hierarquia e representação gráfica GQM | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) e [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Gráfico GQM](grafico-gqm.md) |

*Tabela 1. Organização e responsáveis pela documentação da Fase 2. Fonte: Elaborada por: [Camila Cavalcante](https://github.com/CamilaSilvaC)*

A indicação de responsabilidade refere-se à elaboração principal de cada artefato; as contribuições e revisões posteriores permanecem registradas nos respectivos históricos de versões.

## Delimitação e relação com a Fase 1

A avaliação da Khan Academy foi proposta, na Fase 1, para apoiar um cenário hipotético de decisão de uma coordenação de escola pública sobre adoção e condições de acesso à plataforma. O estudo considera restrições de recursos computacionais e necessidades específicas de estudantes, por meio de avaliação externa (*caixa-preta*).

As características de qualidade priorizadas, com base na **ISO/IEC 25010:2011** [S3](#s3), são **eficiência de desempenho**, **portabilidade** e **usabilidade**. Elas se desdobram nos seguintes requisitos:

- **R1 — Comportamento temporal** e **R2 — Utilização de recursos**, associados ao objetivo **G1**;
- **R3 — Adaptabilidade**, associado ao objetivo **G2**;
- **R4 — Acessibilidade** e **R5 — Apreensibilidade**, associados ao objetivo **G3**.

Conforme o [escopo da Fase 1](../fase-1/escopo-da-avaliacao.md), a avaliação contempla **somente a versão web em computadores**, sem aplicativos nativos ou navegadores de dispositivos móveis. Os fluxos são [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) (navegação em cursos), [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) (videoaulas), [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) (exercícios) e [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos) (consulta ao progresso pelo próprio estudante). G1 e G3 avaliam [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) a [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos); G2 avalia [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) a [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos). Painéis de pais, responsáveis, professores e administradores permanecem fora do objeto. Os ambientes direcionados são [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) (Windows e Chrome), [`A2`](../fase-1/escopo-da-avaliacao.md#ambientes) (Windows e Firefox), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) (macOS e Safari) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) (Ubuntu e Firefox), com NVDA, VoiceOver, Orca e navegação por teclado nas combinações previstas. As condições detalhadas de coleta serão confirmadas no planejamento dos ensaios.

As métricas da Fase 2 são **adaptações propostas tomando a ISO/IEC 25023:2016 como referência** [S4](#s4). Seus nomes e fórmulas não devem ser interpretados como transcrições literais da norma. A correspondência com medidas normativas específicas ainda precisa de conferência documental.

## Referências

<a id="s1"></a>

> [S1] Requisitos de avaliação — Fase 1. Matriz de requisitos R1–R5, stakeholders e decisões documentadas pela equipe. Disponível em: [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md).

<a id="s2"></a>

> [S2] Escopo da avaliação — Fase 1. Plataformas, módulos, ambientes e limites do estudo. Disponível em: [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md).

<a id="s3"></a>

> [S3] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.

<a id="s4"></a>

> [S4] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality. Genebra: ISO, 2016. 

<a id="s5"></a>

> [S5] BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. In: **Encyclopedia of Software Engineering**. John Wiley & Sons, 1994. p. 528–532. 

<a id="s6"></a>

> [S6] Critérios de avaliação da Fase 2. Disciplina Qualidade de Software 1, UnB/FGA, 2026/2. Disponível em: [Critérios de avaliação da Fase 2](../criterios/fase2.md).


## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 17/10/2026 | Estruturação da Fase 2, apresentação da metodologia GQM e organização das seções da documentação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |[Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 20/10/2026 | Ajustes na especificação e organização | [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.2 | 21/10/2026 | Alinhamento da visão geral aos fluxos, ambientes e exclusões definidos na Fase 1. | [Enzo Menali](https://github.com/menali17) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.3 | 21/10/2026 | Ajustes na padronização | [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.4 | 26/10/2026 | Padronização do artefato | [Pedro Lucas](https://github.com/Pwdrinho) | [Camila Cavalcante](https://github.com/CamilaSilvaC) |