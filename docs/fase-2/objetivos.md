[← Visão geral da Fase 2](index.md)

# Fase 2 —  Objetivos de Medição (GQM)


---

## 1. Visão geral e rastreabilidade (Fase 1 → Fase 2)

A Fase 2 formaliza os objetivos de medição a partir das características priorizadas na Fase 1, utilizando a abordagem *Goal–Question–Metric* (GQM). Cada objetivo especifica o objeto de avaliação, o propósito da medição, o foco de qualidade, o ponto de vista dos interessados e o contexto em que a avaliação será realizada.

A definição dos objetivos segue o escopo de observação externa (*caixa-preta*) da Khan Academy em sua **versão web, acessada por navegadores em computadores**. Os fluxos considerados abrangem cursos (videoaulas e exercícios), acompanhamento do progresso no painel do aluno e consulta ao painel dos pais ou responsáveis. Não se incluem aplicativos móveis nativos na especificação desta Fase 2.

Conforme os [requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md), foram priorizadas três características da ISO/IEC 25010:2011: **eficiência de desempenho**, **portabilidade** e **usabilidade**, desdobradas em cinco subcaracterísticas. Os pontos de vista foram extraídos dos interessados associados aos requisitos R1–R5, sem criar novos perfis ou responsabilidades.

## Matriz de Rastreabilidade

A **Tabela 1** sintetiza a correspondência entre as escolhas da Fase 1 e os objetivos GQM.

**Tabela 1 — Rastreabilidade entre características, normas de referência, stakeholders e objetivos GQM.**

| Característica (Fase 1) | Norma do modelo de qualidade | Subcaracterísticas priorizadas | Referência para medição | Foco de qualidade (GQM) | Ponto de vista (*stakeholders*) | Requisitos | Objetivo |
|---|---|---|---|---|---|---|---|
| **Eficiência de desempenho** | **ISO/IEC 25010:2011** | Comportamento temporal; utilização de recursos | ISO/IEC 25023:2016 | Tempos observáveis dos fluxos e consumo de recursos durante a execução | Estudantes; coordenação e professores; responsáveis, conforme R1 e R2 | R1, R2 | **G1** |
| **Portabilidade** | **ISO/IEC 25010:2011** | Adaptabilidade | ISO/IEC 25023:2016 | Execução dos fluxos previstos nos ambientes web selecionados, sem ajustes na plataforma | Estudantes; coordenação e professores | R3 | **G2** |
| **Usabilidade** | **ISO/IEC 25010:2011** | Acessibilidade; apreensibilidade | ISO/IEC 25023:2016 | Execução dos fluxos com recursos de acessibilidade e aprendizagem do uso por estudantes novos | Estudantes com baixa visão ou usuários de leitor de tela; estudantes novos; professores; responsáveis | R4, R5 | **G3** |

*Fonte: elaboração para a Fase 2 com base em `docs/fase-1/requisitos-de-avaliacao.md` e `docs/fase-1/escopo-da-avaliacao.md`, considerando as normas ISO/IEC 25010:2011 e ISO/IEC 25023:2016.*

A **ISO/IEC 25010:2011** orienta a seleção e a definição das características e subcaracterísticas de qualidade. A **ISO/IEC 25023:2016** é utilizada como referência para a especificação das medidas na Fase 2; isso não significa que as fórmulas adaptadas sejam reproduções literais da norma.

## 2. Objetivos de medição estruturados (template GQM)

Os objetivos abaixo foram descritos segundo os **cinco elementos explícitos do template GQM**. As características e os pontos de vista correspondem aos requisitos priorizados pela equipe na Fase 1.

### Objetivo G1 — Eficiência de desempenho

- **Analisar:** Os fluxos da plataforma web Khan Academy referentes ao acesso a cursos, videoaulas, exercícios e painéis do aluno e dos pais ou responsáveis.
- **Com o propósito de:** Avaliar o desempenho observável desses fluxos em condições de uso definidas para o estudo.
- **Com respeito a:** Eficiência de desempenho, especificamente **comportamento temporal** e **utilização de recursos**.
- **Do ponto de vista de:** Estudantes; coordenação escolar e professores; e responsáveis, conforme os interessados associados aos requisitos R1 e R2 da Fase 1.
- **No contexto de:** Avaliação externa (*caixa-preta*) da versão web da Khan Academy em computadores e navegadores incluídos no escopo, com as restrições de hardware e as condições de rede documentadas nos ensaios.

**Rastreabilidade:** requisitos **R1** (comportamento temporal) e **R2** (utilização de recursos); decisão **D1**. O objetivo se desdobra nas questões **Q1–Q4**, respondidas pelos indicadores **M1–M5**.

### Objetivo G2 — Portabilidade

- **Analisar:** Os fluxos de cursos, exercícios e painéis da plataforma web Khan Academy executados nos ambientes de navegador e sistema operacional selecionados.
- **Com o propósito de:** Avaliar a possibilidade de executar os fluxos previstos nos diferentes ambientes contemplados pela avaliação.
- **Com respeito a:** Portabilidade, especificamente **adaptabilidade**.
- **Do ponto de vista de:** Estudantes; coordenação escolar e professores, conforme o requisito R3 da Fase 1.
- **No contexto de:** Avaliação externa da Khan Academy em navegadores web e sistemas operacionais de computadores definidos no escopo, considerando somente as combinações efetivamente viáveis e registradas nos testes.

**Rastreabilidade:** requisito **R3** (adaptabilidade); decisão **D1**. O objetivo se desdobra nas questões **Q5** e **Q6**, respondidas pelos indicadores **M6** e **M7**.

### Objetivo G3 — Usabilidade

- **Analisar:** Os fluxos de cursos, videoaulas, exercícios, painel do aluno e painel dos pais ou responsáveis da plataforma web Khan Academy.
- **Com o propósito de:** Avaliar as condições de utilização dos fluxos por pessoas com necessidades de acessibilidade e por estudantes que estão aprendendo a usar a plataforma.
- **Com respeito a:** Usabilidade, especificamente **acessibilidade** e **apreensibilidade**.
- **Do ponto de vista de:** Estudantes com baixa visão ou que utilizam leitores de tela; estudantes novos; professores e responsáveis, conforme os requisitos R4 e R5 da Fase 1.
- **No contexto de:** Avaliação externa da versão web em computadores, com navegação por teclado e leitores de tela previstos no escopo (NVDA, VoiceOver e Orca, conforme as combinações viáveis), além da observação de tarefas executadas por estudantes novos segundo procedimentos e participantes a definir no plano de avaliação.

**Rastreabilidade:** requisitos **R4** (acessibilidade) e **R5** (apreensibilidade); decisões **D2** e **D3**. O objetivo se desdobra nas questões **Q7–Q11**, respondidas pelos indicadores **M8–M14**.


## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 17/10/2026 | Definição dos objetivos GQM com base nas características de qualidade e nos requisitos priorizados na Fase 1. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho)| 
| 1.1 | 20/10/2026 | Reestruturação dos objetivos com matriz de rastreabilidade | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Camila Cavalcante](https://github.com/CamilaSilvaC)  | [Questões e hipóteses](questoes-hipoteses.md)  |



---

[Navegar pela Fase 2](index.md)
