[← Visão geral da Fase 2](index.md)

# Questões e hipóteses

As questões desta seção desdobram os [objetivos de medição](objetivos.md) da avaliação da Khan Academy em atributos observáveis de qualidade. A especificação reúne **11 questões (Q1–Q11)** e **11 hipóteses (H1–H11)**, associadas aos três objetivos GQM e aos requisitos R1–R5 da Fase 1.

As questões investigam a adequação dos fluxos às condições de uso, sem antecipar fórmulas de cálculo. Cada hipótese expressa o resultado esperado para a questão correspondente e indica a base utilizada para sua formulação. As expectativas são **propostas de trabalho sujeitas à ratificação da equipe**, formuladas antes da coleta final; não representam conclusões sobre a qualidade real da plataforma.


## 1. Delimitação e relação com os objetivos

A avaliação mantém o escopo de observação externa (*caixa-preta*) da **versão web da Khan Academy em computadores**. G1 e G3 abrangem `FL1` (navegação em cursos), `FL2` (videoaulas) e `FL3` (exercícios); G2 também abrange `FL4` (consulta ao progresso pelo próprio estudante). Painéis de pais, responsáveis, professores ou administradores permanecem fora do objeto. Responsáveis participam apenas como interessados nos resultados associados a R2, R4 e D2. As combinações de sistema operacional, navegador, configuração e recurso de acessibilidade deverão ser viáveis e previamente estabelecidas no plano de avaliação.

As questões derivam dos seguintes focos:

- **G1 — Eficiência de desempenho:** comportamento temporal e utilização de recursos, conforme R1 e R2.
- **G2 — Portabilidade:** adaptabilidade entre ambientes e tamanhos de janela, conforme R3.
- **G3 — Usabilidade:** acessibilidade e apreensibilidade, conforme R4 e R5.

## 2. Relação entre objetivos, atributos, questões e métricas

A **Tabela 1** sintetiza a cobertura dos atributos e o vínculo com as métricas especificadas. As hipóteses possuem o mesmo número das questões correspondentes.

**Tabela 1 — Rastreabilidade entre requisitos, objetivos, atributos, questões, hipóteses e métricas.**

| Requisito | Objetivo | Atributo observado | Questão | Hipótese | Métrica(s) |
|---|---|---|---|---|---|
| R1 | G1 | Comportamento temporal | Q1 — Espera nas etapas dos fluxos | H1 | M1 (tempo) e M2 (conclusão) |
| R2 | G1 | Utilização de CPU | Q2 — Processamento disponível | H2 | M3 |
| R2 | G1 | Utilização de memória | Q3 — Memória disponível | H3 | M4 |
| R2 | G1 | Consumo de dados de rede | Q4 — Orçamento de acesso | H4 | M5 |
| R3 | G2 | Adaptação entre sistemas operacionais e navegadores | Q5 — Execução entre ambientes | H5 | M6 |
| R3 | G2 | Adaptação a tamanhos de janela | Q6 — Conteúdo e controles nas janelas avaliadas | H6 | M7 |
| R4 | G3 | Navegação por teclado | Q7 — Conclusão por teclado | H7 | M8 |
| R4 | G3 | Utilização com leitor de tela | Q8 — Informação e conclusão com leitor de tela | H8 | M9 |
| R4 | G3 | Utilização com ampliação | Q9 — Preservação de conteúdo e funcionalidade | H9 | M10 |
| R4 | G3 | Contraste e alto contraste | Q10 — Distinção de informações e controles | H10 | M11 |
| R5 | G3 | Apreensibilidade | Q11 — Autonomia de estudantes novos | H11 | M12 (autonomia), M13 (erros) e M14 (tempo) |

*Fonte: elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) para a Fase 2*


## 3. G1: Eficiência de desempenho

O objetivo G1 analisa os fluxos web do ponto de vista de estudantes, coordenação escolar, professores e responsáveis, considerando os requisitos R1 e R2. As quatro questões seguintes distinguem a espera observada e os diferentes recursos necessários à execução.

### 3.1 Q1: Comportamento temporal

**Questão:** A espera para carregar páginas, iniciar videoaulas e obter respostas dos exercícios permite utilizar os fluxos sem prejudicar a continuidade da atividade nos ambientes avaliados?

**H1:** No ambiente A1, em cada etapa e condição de rede prevista, o tempo mediano de resposta será de até 3 segundos. Pelo menos 90% das tentativas elegíveis de cada tarefa e condição serão concluídas, sem bloqueio de etapa essencial atribuível à plataforma. O tempo pedagógico de assistir à videoaula ou resolver o exercício será excluído da medição de resposta.

**Fundamentação:** R1 identifica a espera como possível barreira à continuidade do estudo, especialmente sob restrições de hardware e rede. Essa necessidade fundamenta a investigação, a expectativa de atendimento é uma suposição proposta para a equipe, sem evidência preliminar de desempenho.

**Verificação prevista:** utilizar M1 por etapa, ambiente e condição de rede, com marcos de início e fim definidos previamente. Comparar os tempos medianos com limites fundamentados e registrar separadamente falhas e interrupções. O tempo pedagógico de assistir à aula ou resolver o exercício não deve ser confundido com a espera por resposta do sistema.

### 3.2 Q2: Utilização de CPU

**Questão:** Os fluxos podem ser concluídos sem sobrecarregar a capacidade de processamento disponível nos computadores avaliados?

**H2:** No ambiente A1, a utilização média de CPU será de até 50% em cada execução válida dos fluxos FL1 a FL3, sem interrupção impeditiva associada à sobrecarga de processamento segundo o protocolo de evidências. O percentual será interpretado conforme o processo monitorado e a capacidade representada pelo instrumento.

**Fundamentação:** R2 e as restrições computacionais previstas no escopo justificam examinar a utilização de processamento. A expectativa de consumo aceitável é uma suposição proposta, a ser ratificada pela equipe.

**Verificação prevista:** utilizar o M3, com ferramenta, processos monitorados e significado do percentual documentados. Comparar o resultado definido na ficha da medida com o orçamento correspondente e registrar ocorrências de sobrecarga. A coincidência entre CPU elevada e interrupção não demonstra, isoladamente, uma relação de causa; a classificação deverá seguir o protocolo de evidências.

### 3.3 Q3: Utilização de memória

**Questão:** Os fluxos permanecem utilizáveis dentro da memória disponível, sem interrupções associadas ao esgotamento desse recurso?

**H3:** No ambiente A1, o pico de memória do processo ou da sessão monitorada será de até 1.024 MiB em cada execução válida dos fluxos FL1 a FL3, sem interrupção associada ao esgotamento de memória segundo o protocolo de evidências.

**Fundamentação:** R2 e a disponibilidade limitada de memória dos ambientes de teste justificam verificar se a sessão pode funcionar sem esgotar o recurso. 

**Verificação prevista:** utilizar o M4 e registrar os picos de cada execução válida. O orçamento deverá considerar a capacidade disponível e as necessidades do sistema operacional e dos processos de apoio. Como H3 trata dos picos, uma média ou mediana não poderá ocultar violações individuais do orçamento sem revisão explícita da hipótese e do critério de julgamento.

### 3.4 Q4: Consumo de dados de rede

**Questão:** O volume de dados necessário para utilizar os fluxos é compatível com o orçamento de acesso definido para as condições avaliadas?

**H4:** No ambiente A1, cada execução concluída do trecho padronizado de navegação e carregamento transferirá, somando envio e recebimento, no máximo 10 MiB, com política de cache constante.

**Fundamentação:** R2 relaciona o consumo de dados às condições de acesso dos estudantes. 

**Verificação prevista:** utilizar o M5, mantendo comparáveis a duração e a qualidade dos vídeos, as tarefas e a configuração de cache. Comparar o tráfego com o orçamento previamente justificado. Uma execução interrompida que transfira poucos dados não deverá ser interpretada como uso eficiente.

## 4. G2: Portabilidade

O objetivo G2 analisa a adaptabilidade dos fluxos do ponto de vista de estudantes, coordenação escolar e professores. As questões distinguem as combinações de sistema operacional e navegador das variações de tamanho de janela no recorte web em computadores.

### 4.1 Q5: Adaptação entre sistemas operacionais e navegadores

**Questão:** Os fluxos essenciais podem ser concluídos nas combinações selecionadas de sistema operacional e navegador, sem ajustes extraordinários na plataforma?

**H5:** Pelo menos 90% das combinações de ambiente (A1–A4) e fluxo (FL1–FL4) selecionadas para o teste permitirão concluir todas as etapas do roteiro e alcançar o resultado esperado, sem alterar a plataforma.

**Fundamentação:** R3 e G2 estabelecem a necessidade de continuidade de uso entre os ambientes selecionados. 

**Verificação prevista:** utilizar M6 com identificação individual de ambiente e fluxo. O protocolo deverá distinguir a preparação normal do ensaio de um ajuste extraordinário necessário para utilizar o produto. Combinações inviáveis por incompatibilidade conhecida entre ferramentas e sistemas deverão ser tratadas no planejamento, sem serem registradas automaticamente como falhas da plataforma.

### 4.2 Q6: Adaptação a tamanhos de janela

**Questão:** O conteúdo e os controles necessários permanecem utilizáveis nos tamanhos de janela definidos para os computadores avaliados?

**H6:** Em 90% das combinações essenciais de ambiente, tamanho de janela e fluxo selecionadas, as tarefas serão concluídas com acesso a todas as informações e controles necessários definidos no roteiro.

**Fundamentação:** a adaptabilidade a diferentes tamanhos de tela aparece entre os atributos de R3 na Fase 1. 

**Verificação prevista:** utilizar M7 com o tamanho de janela incluído na identificação da combinação. Registrar sucesso ou falha da tarefa e evidências de controles ou conteúdos inacessíveis. As combinações utilizadas em Q5 e Q6 deverão ser distinguidas no plano, sem dupla contagem indevida ou mistura dos resultados que respondem a questões diferentes.

## 5. G3: Usabilidade

O objetivo G3 reúne acessibilidade e apreensibilidade, contemplando estudantes com baixa visão ou usuários de leitor de tela, estudantes novos, professores e responsáveis. As quatro primeiras questões tratam dos recursos de acessibilidade; a última aborda a aprendizagem inicial com autonomia.

### 5.1 Q7: Navegação por teclado

**Questão:** Uma pessoa que utiliza apenas teclado consegue identificar e acionar os controles necessários para concluir os fluxos essenciais, sem bloqueios de navegação?

**H7:** Em 90% das combinações essenciais selecionadas nos ambientes A1, A3 e A4, as tarefas dos fluxos FL1–FL3 serão concluídas utilizando apenas o teclado, com foco visível e sem bloqueios de navegação.

**Fundamentação:** R4 e os critérios de acessibilidade selecionados pelo projeto justificam avaliar a operação por teclado. 

**Verificação prevista:** utilizar M8 nas combinações de ambiente e tarefa previstas para teclado. Registrar a sequência de navegação, os controles utilizados e eventuais bloqueios. A conclusão deverá ocorrer sem substituir a operação por teclado pelo uso do mouse durante a tarefa avaliada.

### 5.2 Q8: Utilização com leitor de tela

**Questão:** Uma pessoa que utiliza leitor de tela recebe as informações necessárias e consegue concluir os fluxos essenciais nas combinações avaliadas?

**H8:** Em 90% das combinações essenciais selecionadas com NVDA em A1, VoiceOver em A3 e Orca em A4, o leitor anunciará as informações e identificará os controles definidos no checklist como necessários à tarefa, permitindo concluí-la sem consulta visual à interface.

**Fundamentação:** R4 e G3 incluem pessoas que utilizam leitores de tela. A avaliação se apoia nos critérios de acessibilidade selecionados e nas combinações viáveis dos leitores previstos no escopo.

**Verificação prevista:** utilizar M9 com leitor de tela, navegador, sistema operacional e tarefa identificados. Registrar informações anunciadas, identificação dos controles e barreiras à conclusão.

### 5.3 Q9: Utilização com ampliação

**Questão:** A ampliação do texto permite continuar lendo o conteúdo e utilizando os controles necessários aos fluxos essenciais, sem perda de informação ou funcionalidade?

**H9:** No ambiente A1, na resolução de 1366 × 768, 90% das tarefas essenciais selecionadas serão concluídas com zoom de 200%, sem perda das informações ou dos controles necessários definidos no roteiro.

**Fundamentação:** R4 contempla estudantes com baixa visão e a utilização de recursos de ampliação. Os critérios de acessibilidade selecionados orientam as condições do ensaio. 

**Verificação prevista:** utilizar M10 nas condições de ampliação previamente estabelecidas. Registrar o mecanismo utilizado, sua configuração e os efeitos sobre leitura e operação dos controles. Diferenciar a ampliação de Q9 da simples alteração de tamanho de janela de Q6. A avaliação deverá verificar a tarefa, além de produzir evidências visuais.

### 5.4 Q10: Contraste e alto contraste

**Questão:** A apresentação visual permite distinguir informações e controles necessários aos fluxos essenciais, inclusive na configuração de alto contraste selecionada?

**H10:** Todos os textos aplicáveis inspecionados atenderão ao contraste mínimo de 4,5:1 para texto comum e 3:1 para texto grande, respeitando as definições e exceções adotadas. Separadamente, 90% das tarefas essenciais selecionadas serão concluídas em A1 com o alto contraste do Windows ativado, sem desativar essa configuração

**Fundamentação:** as necessidades de baixa visão previstas em R4 e os critérios de contraste selecionados para o estudo fundamentam a investigação. 

**Verificação prevista:** utilizar M11 com um checklist aplicável aos elementos necessários à tarefa e com registro da configuração de alto contraste. A ativação de alto contraste não substitui a verificação dos critérios de contraste selecionados. O checklist deverá sustentar a classificação da combinação como bem-sucedida ou não, mantendo os achados individuais disponíveis.

### 5.5 Q11: Apreensibilidade

**Questão:** Estudantes novos conseguem compreender como iniciar e concluir as tarefas essenciais após a instrução inicial, sem orientação adicional?

**H11:** No ambiente A1, pelo menos 90% das primeiras tentativas elegíveis de cada tarefa essencial e do conjunto avaliado serão concluídas pelos participantes adultos novos na plataforma, após a instrução inicial padronizada e sem ajuda adicional.

**Fundamentação:** R5 e a decisão D3 relacionam a aprendizagem inicial à necessidade de planejar orientação sobre o uso da plataforma.

**Verificação prevista:** utilizar M12 com estudantes elegíveis e instrução inicial padronizada. Registrar a primeira tentativa de cada par participante–tarefa, a conclusão e os pedidos de ajuda ou intervenções. Definir previamente os patamares de autonomia e a janela de observação.

## 6. Interpretação das hipóteses

A interpretação deverá confrontar os dados válidos com a afirmação específica de cada hipótese, conforme os [critérios de julgamento](criterios-julgamento.md) aprovados antes da coleta final. A **Tabela 2** estabelece os estados de interpretação, sem antecipar resultados ou limiares ainda não definidos.

**Tabela 2 — Estados de interpretação das hipóteses.**

| Estado | Condição |
|---|---|
| **Sustentada na amostra** | Os dados válidos, com cobertura suficiente conforme o plano, atendem integralmente à expectativa e às condições de verificação da hipótese. |
| **Não sustentada na amostra** | Os dados válidos e suficientes para o julgamento não atendem à expectativa estabelecida. A divergência deverá ser acompanhada da evidência correspondente. |
| **Inconclusiva** | Faltam parâmetros fundamentados, dados válidos ou cobertura necessária para aplicar o critério de verificação. Achados parciais permanecem registrados. |

*Fonte: elaborada por [Camila Cavalcante](https://github.com/CamilaSilvaC)*

## Referências

## Referências

> **Objetivos de medição — Fase 2**. Disponível em: [Objetivos de medição](objetivos.md).
> **Requisitos de avaliação — Fase 1**. Requisitos R1–R5 e decisões D1–D3. Disponível em: [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md).
> **Escopo da avaliação — Fase 1**. Disponível em: [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md).
> **Especificação das métricas — Fase 2**. Disponível em: [Especificação das métricas](metricas.md).
> **Critérios de julgamento — Fase 2**. Disponível em: [Critérios de julgamento](criterios-julgamento.md).
> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.
> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality. Genebra: ISO, 2016.
> WORLD WIDE WEB CONSORTIUM (W3C). **Web Content Accessibility Guidelines (WCAG) 2.1**. W3C Recommendation, 5 jun. 2018. Disponível em: <https://www.w3.org/TR/2018/REC-WCAG21-20180605/>. Acesso em: 19 out. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Elaboração das questões e hipóteses GQM e organização da tabela de correspondência com os objetivos e métricas. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) | 
| 1.1 | 20/10/2026 | Proposta de desdobramento dos objetivos em 11 questões e hipóteses, com cobertura por atributo, fundamentação e condições de verificação. | [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.2 | 21/10/2026 | Alinhamento da delimitação das questões aos fluxos e exclusões definidos na Fase 1. | [Enzo Menali](https://github.com/menali17) | |
| 1.3 | 21/10/2026 | Padronização do endereço oficial da WCAG 2.1 com a referência adotada na Fase 1. | [Enzo Menali](https://github.com/menali17) | |
| 1.4 | 21/10/2026 | Ajustes nas questões e hipóteses | [Camila Cavalcante](https://github.com/CamilaSilvaC) | |

---

[Navegar pela Fase 2](index.md)
