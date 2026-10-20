[← Visão geral da Fase 2](index.md)

# Questões e hipóteses — nível operacional

Para detalhar os três objetivos GQM definidos para a avaliação da Khan Academy, formulamos cinco questões de avaliação. Cada questão está associada a uma hipótese de trabalho e à métrica que será utilizada para respondê-la.

As hipóteses foram definidas **antes da coleta** e devem orientar a interpretação dos resultados, mas **não representam conclusões sobre a qualidade real da plataforma**. Quando houver necessidade de limiares quantitativos para sustentação ou rejeição das hipóteses, esses valores deverão estar justificados e aprovados antes da execução da Fase 4.

**Tabela 1 — Relação entre objetivos, questões, hipóteses e métricas da Fase 2.**

| **Objetivo** | **Questão** | **Hipótese** | **Métrica** |
|---|---|---|---|
| [G1 — Eficiência de desempenho](objetivos.md) | **Q1 — Tempo observado de execução.** Em que medida os tempos observados nos fluxos educacionais definidos permitem caracterizar o comportamento temporal da plataforma nas condições avaliadas? | **H1:** os fluxos avaliados tendem a apresentar tempos de execução compatíveis com o uso regular da plataforma nas condições de teste, segundo critérios a definir antes da coleta. | [M1](metricas.md) |
| [G1 — Eficiência de desempenho](objetivos.md) | **Q2 — Consumo de recursos.** Qual é o consumo observável de recursos durante a execução dos fluxos previstos? | **H2:** o consumo de recursos durante os fluxos avaliados tende a permanecer em níveis operacionais aceitáveis para o contexto de uso considerado, conforme limites a definir e justificar pela equipe. | [M2](metricas.md) |
| [G2 — Portabilidade](objetivos.md) | **Q3 — Execução entre ambientes.** Em quais ambientes avaliados os fluxos permanecem executáveis sem alteração da plataforma? | **H3:** a maioria das combinações ambiente–fluxo previstas no escopo tende a permanecer executável sem necessidade de ajustes adicionais na plataforma. | [M3](metricas.md) |
| [G3 — Usabilidade](objetivos.md) | **Q4 — Acessibilidade dos fluxos principais.** Em que medida os fluxos principais permanecem executáveis com os recursos de acessibilidade considerados na Fase 1? | **H4:** os fluxos principais tendem a ser executáveis, ao menos em parte, com as tecnologias assistivas e formas de navegação previstas no escopo, embora possam surgir barreiras pontuais a serem registradas. | [M4](metricas.md) |
| [G3 — Usabilidade](objetivos.md) | **Q5 — Aprendizagem de estudantes novos.** Em que medida estudantes novos conseguem aprender a executar os fluxos definidos sem auxílio adicional? | **H5:** estudantes novos tendem a conseguir executar os fluxos definidos com autonomia predominante, ainda que dificuldades de navegação ou interpretação possam ocorrer em etapas específicas. | [M5](metricas.md) |

*Fonte: elaboração da equipe para a Fase 2, com base em `docs/fase-1/requisitos-de-avaliacao.md` e `docs/fase-1/escopo-da-avaliacao.md`.*

## G1 — Eficiência de desempenho

### Q1 — Em que medida os tempos observados nos fluxos educacionais definidos permitem caracterizar o comportamento temporal da plataforma nas condições avaliadas?

A questão Q1 investiga o comportamento temporal observável da Khan Academy nos fluxos delimitados na Fase 1, como navegação em cursos com vídeos, exercícios e acesso aos painéis previstos no escopo. A análise será conduzida por meio da [M1](metricas.md), que registra o intervalo entre marcos previamente definidos de início e fim de cada execução válida.

A hipótese H1 expressa a expectativa de que os tempos observados sejam compatíveis com o uso regular da plataforma no contexto avaliado. Como os critérios quantitativos ainda dependem de fundamentação da equipe, a sustentação dessa hipótese ficará condicionada aos limiares que forem formalizados antes da coleta.

### Q2 — Qual é o consumo observável de recursos durante a execução dos fluxos previstos?

A questão Q2 complementa a análise de desempenho ao observar o consumo de recursos computacionais durante a execução dos fluxos escolhidos. Dependendo da instrumentação disponível, poderão ser registradas medidas de CPU, memória e tráfego de rede, sem agregá-las indevidamente em uma única medida.

A [M2](metricas.md) será utilizada para descrever esse comportamento. A hipótese H2 considera que o consumo de recursos tende a permanecer em níveis operacionais adequados ao contexto de uso definido na Fase 1, mas a equipe ainda precisa documentar os limites de interpretação para cada tipo de recurso efetivamente observado.

## G2 — Portabilidade

### Q3 — Em quais ambientes avaliados os fluxos permanecem executáveis sem alteração da plataforma?

A questão Q3 trata da adaptabilidade da plataforma web da Khan Academy nos ambientes delimitados pela Fase 1. A intenção é verificar em quais combinações de sistema operacional e navegador os fluxos selecionados podem ser executados sem necessidade de modificações na plataforma ou de procedimentos extraordinários.

A [M3](metricas.md) registrará a proporção de combinações ambiente–fluxo consideradas executáveis na amostra efetivamente testada. A hipótese H3 expressa a expectativa de que a maior parte dessas combinações permaneça utilizável, respeitando-se os limites práticos do escopo e das combinações realmente avaliáveis na Fase 3.

## G3 — Usabilidade

### Q4 — Em que medida os fluxos principais permanecem executáveis com os recursos de acessibilidade considerados na Fase 1?

A questão Q4 focaliza a acessibilidade dos fluxos principais, levando em conta as tecnologias assistivas e formas de navegação previstas na Fase 1, como navegação por teclado e uso de leitores de tela nas combinações viáveis. O interesse está em observar barreiras perceptíveis durante a realização dos fluxos, sem extrapolar os resultados para toda a plataforma ou para todos os perfis de usuário.

A [M4](metricas.md) será utilizada para registrar a proporção de fluxos executáveis nas combinações de acessibilidade consideradas. A hipótese H4 admite que a plataforma tende a permitir a execução de parte relevante dos fluxos, embora a própria avaliação possa revelar barreiras específicas que deverão ser relatadas.

### Q5 — Em que medida estudantes novos conseguem aprender a executar os fluxos definidos sem auxílio adicional?

A questão Q5 aborda a apreensibilidade, isto é, a facilidade com que estudantes sem familiaridade prévia com a plataforma conseguem compreender e executar os fluxos definidos no escopo. A observação deverá se concentrar nas interações necessárias para concluir tarefas básicas de navegação e uso, em contexto compatível com a avaliação externa prevista.

A [M5](metricas.md) indicará a proporção de participantes ou execuções em que houve conclusão autônoma dos fluxos definidos. A hipótese H5 expressa a expectativa de que estudantes novos consigam realizar essas tarefas com autonomia predominante, ainda que dificuldades pontuais possam ser identificadas e registradas.

## Interpretação das hipóteses

Consideraremos uma hipótese **sustentada** quando a métrica correspondente indicar resultado compatível com o critério previamente definido para a questão, desde que haja dados suficientes e condições de coleta adequadas. Quando o resultado não atender ao critério estabelecido, a hipótese será considerada **não sustentada**. Na ausência de dados suficientes, de combinações viáveis ou de condições mínimas de avaliação, o resultado deverá ser registrado como **inconclusivo**.

A interpretação final de cada hipótese dependerá da métrica calculada, das exclusões justificadas, do ambiente de teste, da amostra observada e dos critérios de julgamento definidos pela equipe. Esses elementos devem permanecer coerentes com a [rastreabilidade da Fase 2](objetivos.md) e com os [critérios de julgamento](criterios-julgamento.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 18/10/2026 | Elaboração das questões e hipóteses GQM e organização da tabela de correspondência com os objetivos e métricas. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho)| 

---

[Navegar pela Fase 2](index.md)
