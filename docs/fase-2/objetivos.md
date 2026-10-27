# Objetivos de Medição (GQM)

**Versão 1.3**

Este documento apresenta os objetivos de medição da [Fase 2](index.md) da avaliação da qualidade da Khan Academy, estruturados com base na abordagem Goal–Question–Metric (GQM). Sua elaboração considera as características de qualidade e os requisitos priorizados na Fase 1, bem como as definições estabelecidas no Escopo da avaliação.

## 1. Visão geral e rastreabilidade (Fase 1 → Fase 2)

A Fase 2 formaliza os objetivos de medição a partir das características priorizadas na [Fase 1](../fase-1/index.md), utilizando a abordagem *Goal–Question–Metric* (GQM) [S1](#s1). Cada objetivo especifica o objeto de avaliação, o propósito da medição, o foco de qualidade, o ponto de vista dos interessados e o contexto em que a avaliação será realizada.

A definição dos objetivos segue o escopo de observação externa (*caixa-preta*) da Khan Academy em sua **versão web, acessada por navegadores em computadores**. Os fluxos considerados são [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) (navegação em cursos), [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) (videoaulas), [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) (exercícios) e [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos) (consulta ao progresso pelo próprio estudante). Aplicativos nativos, navegadores de dispositivos móveis e painéis de pais, responsáveis, professores ou administradores não integram o objeto da avaliação.

Conforme os [requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md), foram priorizadas três características da ISO/IEC 25010:2011 [S3](#s3): **eficiência de desempenho**, **portabilidade** e **usabilidade**, desdobradas em cinco subcaracterísticas. Os pontos de vista foram extraídos dos interessados associados aos requisitos [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) a [`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade), sem criar novos perfis ou responsabilidades.

A presença de responsáveis entre os pontos de vista de [`G1`](#objetivo) e [`G3`](#objetivo) decorre dos requisitos [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e [`R4`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e da decisão [`D2`](../fase-1/requisitos-de-avaliacao.md#requisitante). Ela representa interesse nos resultados e não inclui o painel desse papel entre os fluxos avaliados.

## 2. Matriz de Rastreabilidade

A **Tabela 1** sintetiza a correspondência entre as escolhas da Fase 1 e os objetivos GQM.

| Característica (Fase 1) | Norma do modelo de qualidade | Subcaracterísticas priorizadas | Referência para medição | Foco de qualidade (GQM) | Ponto de vista (*stakeholders*) | Requisitos | Objetivo |
|---|---|---|---|---|---|---|---|
| **Eficiência de desempenho** | **ISO/IEC 25010:2011** [S3](#s3) | Comportamento temporal; utilização de recursos | ISO/IEC 25023:2016 [S2](#s2) | Tempos observáveis dos fluxos e consumo de recursos durante a execução | Estudantes; coordenação e professores; responsáveis, conforme [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) | [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade), [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) | [`G1`](#objetivo) |
| **Portabilidade** | **ISO/IEC 25010:2011** [S3](#s3) | Adaptabilidade | ISO/IEC 25023:2016 [S2](#s2) | Execução dos fluxos previstos nos ambientes web selecionados, sem ajustes na plataforma | Estudantes; coordenação e professores | [`R3`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) | [`G2`](#objetivo) |
| **Usabilidade** | **ISO/IEC 25010:2011** [S3](#s3) | Acessibilidade; apreensibilidade | ISO/IEC 25023:2016 [S2](#s2) | Execução dos fluxos com recursos de acessibilidade e aprendizagem do uso por estudantes novos | Estudantes com baixa visão ou usuários de leitor de tela; estudantes novos; professores; responsáveis | [`R4`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade), [`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) | [`G3`](#objetivo) |

*Tabela 1. Rastreabilidade entre características, normas de referência, stakeholders e objetivos GQM. Fonte: Elaborada por: [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino), considerando as normas [S3](#s3) e [S2](#s2).*

A **ISO/IEC 25010:2011** [S3](#s3) orienta a seleção e a definição das características e subcaracterísticas de qualidade. E a **ISO/IEC 25023:2016** [S2](#s2) é utilizada como referência para a especificação das medidas na Fase 2; isso não significa que as fórmulas adaptadas sejam reproduções literais da norma.

<a id="objetivo"></a>

## 3. Objetivos de medição estruturados (template GQM)

Os objetivos abaixo foram descritos segundo os **cinco elementos explícitos do template GQM**. As características e os pontos de vista correspondem aos requisitos priorizados pela equipe na [Fase 1](../fase-1/index.md).

### 3.1  Objetivo G1 — Eficiência de desempenho

<a id="g1"></a>

- **Analisar:** Os fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) (navegação em cursos),[`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) (videoaulas) e [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) (exercícios) da plataforma web Khan Academy.
- **Com o propósito de:** Avaliar o desempenho observável desses fluxos em condições de uso definidas para o estudo.
- **Com respeito a:** Eficiência de desempenho, especificamente **comportamento temporal** e **utilização de recursos**.
- **Do ponto de vista de:** Estudantes; coordenação escolar e professores; e responsáveis, conforme os interessados associados aos requisitos [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) da [Fase 1](../fase-1/index.md).
- **No contexto de:** Avaliação externa (*caixa-preta*) da versão web da Khan Academy em computadores e navegadores incluídos no escopo, com as restrições de hardware e as condições de rede documentadas nos ensaios.

**Rastreabilidade:** requisitos [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) (comportamento temporal) e [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) (utilização de recursos); decisão [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante). O objetivo se desdobra nas questões [`Q1`](questoes-hipoteses.md#3-g1-eficiencia-de-desempenho) a [`Q4`](questoes-hipoteses.md#34-q4-consumo-de-dados-de-rede), respondidas pelos indicadores [`M1`](metricas.md#1-metricas-detalhadas) a [`M5`](metricas.md#1-metricas-detalhadas).

### 3.2 Objetivo G2 — Portabilidade

<a id="g2"></a>

- **Analisar:** Os fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) a [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos) da plataforma web Khan Academy executados nos ambientes de navegador e sistema operacional selecionados.
- **Com o propósito de:** Avaliar a possibilidade de executar os fluxos previstos nos diferentes ambientes contemplados pela avaliação.
- **Com respeito a:** Portabilidade, especificamente **adaptabilidade**.
- **Do ponto de vista de:** Estudantes; coordenação escolar e professores, conforme o requisito [`R3`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) da [Fase 1](../fase-1/index.md).
- **No contexto de:** Avaliação externa da Khan Academy em navegadores web e sistemas operacionais de computadores definidos no escopo, considerando somente as combinações efetivamente viáveis e registradas nos testes.

**Rastreabilidade:** requisito [`R3`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) (adaptabilidade); decisão [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante). O objetivo se desdobra nas questões [`Q5`](questoes-hipoteses.md#41-q5-adaptacao-entre-sistemas-operacionais-e-navegadores) e [`Q6`](questoes-hipoteses.md#42-q6-adaptacao-a-tamanhos-de-janela), respondidas pelos indicadores [`M6`](metricas.md#1-metricas-detalhadas) e [`M7`](metricas.md#1-metricas-detalhadas).

### 3.3 Objetivo G3 — Usabilidade

<a id="g3"></a>

- **Analisar:** Os fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) (navegação em cursos), [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) (videoaulas) e [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) (exercícios) da plataforma web Khan Academy.
- **Com o propósito de:** Avaliar as condições de utilização dos fluxos por pessoas com necessidades de acessibilidade e por estudantes que estão aprendendo a usar a plataforma.
- **Com respeito a:** Usabilidade, especificamente **acessibilidade** e **apreensibilidade**.
- **Do ponto de vista de:** Estudantes com baixa visão ou que utilizam leitores de tela; estudantes novos; professores e responsáveis, conforme os requisitos [`R4`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e [`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) da [Fase 1](../fase-1/index.md).
- **No contexto de:** Avaliação externa da versão web em computadores, com navegação por teclado e leitores de tela previstos no escopo (NVDA, VoiceOver e Orca, conforme as combinações viáveis), além da observação de tarefas executadas por estudantes novos segundo procedimentos e participantes a definir no plano de avaliação.

**Rastreabilidade:** requisitos [`R4`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) (acessibilidade) e [`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) (apreensibilidade); decisões [`D2`](../fase-1/requisitos-de-avaliacao.md#requisitante) e [`D3`](../fase-1/requisitos-de-avaliacao.md#requisitante). O objetivo se desdobra nas questões [`Q7`](questoes-hipoteses.md#51-q7-navegacao-por-teclado) a [`Q11`](questoes-hipoteses.md#55-q11-apreensibilidade), respondidas pelos indicadores [`M8`](metricas.md#1-metricas-detalhadas) a [`M14`](metricas.md#1-metricas-detalhadas).

## Referências

<a id="s1"></a>

> [S1] BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. In: **Encyclopedia of Software Engineering**. John Wiley & Sons, 1994. p. 528–532.

<a id="s2"></a>

> [S2] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality. Genebra: ISO, 2016. 

<a id="s3"></a>

> [S3] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 17/10/2026 | Definição dos objetivos GQM com base nas características de qualidade e nos requisitos priorizados na Fase 1. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) | 
| 1.1 | 20/10/2026 | Reestruturação dos objetivos com matriz de rastreabilidade | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Camila Cavalcante](https://github.com/CamilaSilvaC) |
| 1.2 | 21/10/2026 | Alinhamento dos objetos de G1 a G3 aos fluxos FL1 a FL4 e aos cortes definidos na Fase 1. | [Enzo Menali](https://github.com/menali17) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.3 | 26/10/2026 | Padronização e inserção da introdução | [Pedro Lucas](https://github.com/Pwdrinho) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |