[← Visão geral da Fase 2](index.md)

# Escala de julgamento e limiares

Propõe-se uma **escala de julgamento comum**, sujeita à aprovação da equipe antes da coleta. A escala qualitativa abaixo **não constitui limiares numéricos já aprovados**. Como M1, M2 medem grandezas físicas e M3–M5 medem percentuais, **não é válido aplicar os mesmos cortes brutos a todas elas**. A solução metodológica proposta é normalizar o julgamento em uma escala ordinal comum, utilizando limiares próprios por métrica, definidos previamente e justificados.

A **Tabela 7** estabelece os níveis comuns de julgamento a serem utilizados quando os limites quantitativos forem fundamentados.

**Tabela 7 — Escala única de pontuação proposta e situação dos limiares por métrica.**

| Nível comum | Interpretação | Regra quantitativa aplicável a M1–M5 |
|---|---|---|
| 0 | Crítico | Pendente de critérios e limiares fundamentados |
| 1 | Insuficiente | Pendente de critérios e limiares fundamentados |
| 2 | Satisfatório | Pendente de critérios e limiares fundamentados |
| 3 | Bom | Pendente de critérios e limiares fundamentados |
| Sem pontuação | Ausência de dados válidos ou métrica não avaliável | Não emitir julgamento |

*Fonte: elaboração para a Fase 2. A escala não é uma tabela normativa da ISO/IEC 25023 e ainda requer aprovação da equipe.*

A Tabela 7 apresenta os níveis ordinais, mas as **faixas de cada métrica ainda não têm valores justificáveis no material recebido**. Para M1, o corte depende do prazo aceitável para abertura e conclusão de cada fluxo; para M2, dos limites por recurso e da instrumentação; para M3–M5, do nível mínimo de cobertura, acessibilidade ou conclusão autônoma requerido pelos tomadores de decisão. Esses limiares devem ser aprovados e documentados *antes da Fase 4*. Não é metodologicamente válido usar a matriz de priorização da Fase 1 (notas 12 a 18) como faixas de qualidade de resultados, pois aquela matriz classifica **prioridades de avaliação**, não desempenho observado.

A **Tabela 8** explicita as lacunas de fundamentação para cada métrica. Os campos pendentes não representam resultados nem faixas aprovadas.

**Tabela 8 — Limiares de pontuação a definir para cada métrica.**

| Métrica | Sentido desejável | Faixa 0 | Faixa 1 | Faixa 2 | Faixa 3 | Fundamentação necessária |
|---|---|---|---|---|---|---|
| M1 (s) | Menor | A definir | A definir | A definir | A definir | Tempo máximo aceitável por fluxo e rede |
| M2 (CPU/RAM/tráfego) | Menor, mantendo o fluxo funcional | A definir | A definir | A definir | A definir | Referência por recurso, VM e tipo de fluxo |
| M3 (%) | Maior | A definir | A definir | A definir | A definir | Cobertura mínima de ambientes essenciais |
| M4 (%) | Maior | A definir | A definir | A definir | A definir | Criticidade das barreiras e tarefas essenciais |
| M5 (%) | Maior | A definir | A definir | A definir | A definir | Nível mínimo de autonomia para dispensar orientação inicial |

*Fonte: elaboração para a Fase 2 a partir dos requisitos R1–R5.*

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | 
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 18/10/2026 | Estruturação da escala de pontuação e dos critérios de julgamento das métricas, com identificação dos limiares pendentes de fundamentação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho)| 


---

[Navegar pela Fase 2](index.md)
