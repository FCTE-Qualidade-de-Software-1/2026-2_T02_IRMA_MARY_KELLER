# Fase 2 — Especificação da avaliação

Nesta fase, são especificados os objetivos, questões, hipóteses e métricas que orientarão a avaliação da Khan Academy. As definições partem das características priorizadas na Fase 1 e são aplicáveis somente à plataforma web acessada em computadores. Os resultados serão obtidos na Fase 4; portanto, esta página descreve o planejamento das medições, não conclusões sobre a qualidade do produto.

**Situação:** especificação sujeita à revisão da equipe. **Resultados de medição:** a coletar na Fase 4.

**Base documental:** [Requisitos de avaliação — Fase 1](../fase-1/requisitos-de-avaliacao.md), [Escopo da avaliação — Fase 1](../fase-1/escopo-da-avaliacao.md) e [critérios da Fase 2](../criterios/fase2.md).

## Delimitação e relação com a Fase 1

A Fase 1 define como propósito examinar a Khan Academy em condições de recursos limitados e necessidades específicas, para apoiar o cenário hipotético de decisão de uma coordenação de escola pública sobre adoção e forma de acesso. A avaliação foi concebida como observação externa (caixa-preta); **não representa uma avaliação já executada**.

Os requisitos priorizados na Fase 1 são: `R1` comportamento temporal (alta), `R2` utilização de recursos (alta), `R3` adaptabilidade (alta), `R4` acessibilidade (alta) e `R5` apreensibilidade (média). A matriz de rastreabilidade associa `R1` e `R2` a `G1`, `R3` a `G2` e `R4` e `R5` a `G3`. O [escopo da Fase 1](../fase-1/escopo-da-avaliacao.md) delimita a avaliação à **plataforma web** em navegador, em quatro módulos: cursos (vídeos), cursos (exercícios), painel do aluno e painel dos pais/responsáveis. Prevê Chrome, Firefox e Safari nos sistemas operacionais de computadores Windows, macOS, Ubuntu, Fedora, Arch Linux e OpenSUSE. Também prevê máquinas virtuais com até 4 GB de RAM e 6 vCPUs, testes com NVDA, VoiceOver e Orca e observação caixa-preta. O escopo efetivamente testável e as combinações realizáveis deverão ser confirmados no planejamento da Fase 3. Não se pressupõe que todas as combinações entre SO, navegador e leitor de tela sejam viáveis.



As métricas a seguir são **especificações operacionais propostas com referência à ISO/IEC 25023:2016**, adaptadas ao contexto da plataforma. Seus nomes e fórmulas não devem ser interpretados como transcrições literais da norma. A correspondência com medidas normativas específicas permanece pendente de conferência documental.


## Organização da Fase 2

Os documentos abaixo compõem a especificação GQM. Os resultados ainda não foram coletados.

| Página | Conteúdo |
|---|---|
| [Objetivos de medição](objetivos.md) | G1–G3 e seus cinco elementos GQM, derivados da Fase 1. |
| [Questões e hipóteses](questoes-hipoteses.md) | Q1–Q5 e H1–H5 vinculadas aos objetivos. |
| [Especificação das métricas](metricas.md) | M1–M5 em tabelas, com definição, cálculo, fonte, coleta, interpretação e análise de validade. |
| [Critérios de julgamento](criterios-julgamento.md) | Escala comum, faixas ainda pendentes de fundamentação. |
| [Gráfico GQM](grafico-gqm.md) | Figura 1 com as relações entre G, Q e M. |
| [Rastreabilidade](rastreabilidade.md) | Correspondência entre R1–R5, stakeholders e elementos GQM. |

A especificação reúne três objetivos, cinco questões, cinco hipóteses e cinco métricas. As fichas das métricas não trazem resultados de testes, pois esses valores devem ser coletados na Fase 4.



## Referências

- Fase 1 do projeto: `docs/fase-1/requisitos-de-avaliacao.md` (matriz de requisitos R1–R5, stakeholders e decisões D1–D4).
- ISO/IEC 25010:2011 — modelo de qualidade do produto, versão declarada na Fase 1.
- ISO/IEC 25023:2016 — referência geral para medidas de qualidade, condicionada à conferência das medidas específicas adotadas.
- Enunciado e critérios de avaliação da Fase 2 da disciplina Qualidade de Software 1, semestre 2026/2.


## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | 
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 17/10/2026 | Estruturação da Fase 2, apresentação da metodologia GQM e organização das seções da documentação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |[Pedro Lucas](https://github.com/Pwdrinho) | 