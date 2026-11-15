# Rastreabilidade da avaliação

A rastreabilidade permite verificar como cada medida responde às questões e aos objetivos definidos na Fase 2. A matriz relaciona **objetivos GQM, questões, métricas, fluxos, ambientes, procedimentos, registros e critérios de julgamento**. Assim, cada resultado produzido na Fase 4 poderá ser interpretado a partir de uma definição previamente estabelecida, sem criar indicadores ou regras de julgamento após a coleta.

## 1. Organização das medidas

| Objetivo | Foco | Questões | Métricas |
|---|---|---|---|
| **G1** | Eficiência de desempenho | Q1–Q4 | M1–M5 |
| **G2** | Adaptabilidade | Q5–Q6 | M6–M7 |
| **G3** | Acessibilidade e apreensibilidade | Q7–Q11 | M8–M14 |

*Tabela 1: Hierarquia GQM considerada no planejamento. Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

## 2. Correspondência entre métricas e procedimentos

A tabela apresenta a relação entre cada medida, os fluxos observados e o procedimento correspondente. Os métodos de cálculo e as condições específicas de interpretação constam das [fichas de métricas](../fase-2/metricas.md), dos [critérios de julgamento](../fase-2/criterios-julgamento.md) e dos roteiros técnicos.

| Objetivo | Questão | Métrica | Fluxos | Ambiente | Procedimento | Critério de julgamento |
|---|---|---|---|---|---|---|
| G1 | Q1 | [M1](../fase-2/metricas.md) | FL1–FL3 | A1 | [Desempenho](procedimentos-desempenho.md) §4.1 e §5 | [Faixas de tempo](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos); mediana ≤ 3 s para H1 |
| G1 | Q1 | [M2](../fase-2/metricas.md) | FL1–FL3 | A1 | [Desempenho](procedimentos-desempenho.md) §4.2 e §7 | [Faixas percentuais](../fase-2/criterios-julgamento.md#2-metricas-percentuais) |
| G1 | Q2 | [M3](../fase-2/metricas.md) | FL1–FL3 | A1 | [Desempenho](procedimentos-desempenho.md) §4.3 | [Faixas de recursos](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) |
| G1 | Q3 | [M4](../fase-2/metricas.md) | FL1–FL3 | A1 | [Desempenho](procedimentos-desempenho.md) §4.4 | [Faixas de recursos](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) |
| G1 | Q4 | [M5](../fase-2/metricas.md) | FL1–FL3 | A1 | [Desempenho](procedimentos-desempenho.md) §4.5 | [Faixas de recursos](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) |
| G2 | Q5 | [M6](../fase-2/metricas.md) | FL1–FL4 | A1–A4 | [Adaptabilidade](procedimentos-adaptabilidade.md) §4 e §6 | [Faixas percentuais](../fase-2/criterios-julgamento.md#2-metricas-percentuais) e [regra de julgamento](../fase-2/criterios-julgamento.md#5-regra-de-julgamento); FL1–FL3 essenciais |
| G2 | Q6 | [M7](../fase-2/metricas.md) | FL1–FL4 | A1–A4 × J1, J2 | [Adaptabilidade](procedimentos-adaptabilidade.md) §5 e §6 | [Faixas percentuais](../fase-2/criterios-julgamento.md#2-metricas-percentuais) e regra de julgamento |
| G3 | Q7 | [M8](../fase-2/metricas.md) | FL1–FL3 | A1, A3, A4 | Acessibilidade e apreensibilidade §4.3 | [Faixas](../fase-2/criterios-julgamento.md#2-metricas-percentuais) e regra de bloqueio |
| G3 | Q8 | [M9](../fase-2/metricas.md) | FL1–FL3 | A1 (NVDA), A3 (VoiceOver), A4 (Orca) | Acessibilidade e apreensibilidade §4.4 | [Faixas](../fase-2/criterios-julgamento.md#2-metricas-percentuais) e regra de bloqueio |
| G3 | Q9 | [M10](../fase-2/metricas.md) | FL1–FL3 | A1, 1366 × 768, zoom 200% | Acessibilidade e apreensibilidade §4.5 | Faixas e [WCAG 1.4.4](../fase-2/criterios-julgamento.md#4-criterios-tecnicos-de-acessibilidade) |
| G3 | Q10 | [M11](../fase-2/metricas.md) | FL1–FL3 | A1 | Acessibilidade e apreensibilidade §4.6 | [WCAG 1.4.3 e 1.4.6](../fase-2/criterios-julgamento.md#4-criterios-tecnicos-de-acessibilidade) |
| G3 | Q11 | [M12](../fase-2/metricas.md) | FL1–FL3 | A1 | Acessibilidade e apreensibilidade §5 | [Faixas](../fase-2/criterios-julgamento.md#2-metricas-percentuais) |
| G3 | Q11 | [M13](../fase-2/metricas.md) | FL1–FL3 | A1 | Acessibilidade e apreensibilidade §5 | [Faixas, menor é melhor](../fase-2/criterios-julgamento.md#2-metricas-percentuais) |
| G3 | Q11 | [M14](../fase-2/metricas.md) | FL1–FL3 | A1 | Acessibilidade e apreensibilidade §5 | [Faixas de tempo](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) |

*Tabela 2: Relação entre objetivos, questões, métricas e condições de avaliação. Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

Para M8 a M14, os procedimentos e os formulários F1 a F7 estão especificados no roteiro de acessibilidade e apreensibilidade, em correspondência com as fichas da Fase 2.

## 3. Cobertura por fluxo e ambiente

| Família | Fluxos | Ambientes e condições | Observação |
|---|---|---|---|
| M1–M5 | FL1–FL3 | A1 | Cinco repetições válidas por tarefa/condição |
| M6–M7 | FL1–FL4 | A1–A4; 1366 × 768 e 1920 × 1080 para M7 | Matriz de avaliação definida para A1–A4 |
| M8–M9 | FL1–FL3 | A1, A3 e A4 | Teclado e leitores de tela; formulário F5 |
| M10–M11 | FL1–FL3 | A1 | Zoom, contraste e alto contraste, com métodos separados |
| M12–M14 | FL1–FL3 | A1; 3–5 participantes iniciantes | Sessões com formulários F2–F4 e dados anonimizados |

*Tabela 3. Cobertura planejada por fluxo e ambiente. Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 14/11/2026 | Mapeamento das métricas M1 a M14 aos objetivos, questões, fluxos, ambientes, procedimentos e critérios de julgamento. | [Camila Silva](https://github.com/CamilaSilvaC) e [Geovanna Alves](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
