[← Visão geral da Fase 2](index.md)

# Especificação das métricas — nível quantitativo

As **Tabelas 1 a 5** detalham cada métrica em formato padronizado, incluindo cálculo, unidade, fontes, coleta e critérios de interpretação.

**Todas as observações, os numeradores, os denominadores, os tempos, as medições de recursos e os resultados finais estão _a coletar na Fase 4_.** Procedimentos detalhados, ambiente, repetições e elegibilidade deverão constar do plano da Fase 3. Não preencher resultados fictícios.

## M1 — Tempo observado de execução de fluxo (Q1)

intervalo entre o marco inicial e o marco final observáveis de um fluxo previamente descrito (por exemplo, solicitação de abertura de aula e conclusão de seu carregamento observável). Cada fluxo precisa ter marcos definidos antes da coleta.

**Tabela 1 — Especificação da métrica M1.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q1 / H1 |
| Cálculo | para cada execução válida, `T = t_fim − t_início`; para resumo de execuções comparáveis, `T_mediano = mediana(T1, …, Tn)`. |
| Unidade | segundos (s). |
| Fonte dos dados | marcações de tempo e registros de execução produzidos nos testes da interface; ferramentas de desenvolvedor do navegador (DevTools), previstas no escopo, e registros de execução; procedimentos exatos a especificar na Fase 3. |
| Forma de coleta | executar fluxo nos ambientes e condições de rede definidos na Fase 3; registrar eventos inicial/final, falhas, ambiente e repetições; não transformar falha de carregamento em tempo zero. |
| Interpretação | Aplicar as [regras de julgamento](criterios-julgamento.md), por grupo de julgamento e com cobertura obrigatória completa. Falhas permanecem visíveis; ausência de dados ou parâmetros aprovados implica resultado inconclusivo. |
| Simplicidade, objetividade e validade | cálculo simples; marcos registrados tornam a medida replicável; mede comportamento temporal observável, mas não explica causas de lentidão do backend. **Validade condicionada** a marcos consistentes e controle do ambiente. |
| Situação da medição | a coletar (F4). |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M2 — Consumo de recursos por fluxo (Q2)

quantidade de um recurso consumida durante fluxo definido. **CPU, memória e tráfego de rede são medidas diferentes e não serão somadas.** Os três recursos são previstos; limitações da instrumentação devem ser registradas como lacunas de cobertura obrigatória.

**Tabela 2 — Especificação da métrica M2.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q2.1–Q2.3 / H2.1–H2.3 |
| Cálculo | tráfego transferido `D = bytes_recebidos + bytes_enviados` no intervalo do fluxo; memória observada `RAM_pico = max(RAM(t))`; CPU observada `CPU_média = (Σ CPU_i)/n`, desde que a ferramenta explicite o significado de cada amostra. |
| Unidades | MiB para memória; bytes para tráfego (ou conversão declarada); % da capacidade total disponibilizada à VM para CPU. |
| Fonte dos dados | medições de ferramentas do navegador ou do sistema operacional, DevTools e monitoramento do sistema/VM previstos na Fase 1; instrumento e configuração exatos a registrar na Fase 3. |
| Forma de coleta | medir apenas os recursos que a equipe conseguir isolar e registrar; guardar ferramenta, versão, fluxo, instante, condições de fundo e dados brutos. Se o consumo atribuível à sessão web não puder ser obtido de modo confiável, marcar **não avaliável naquele ambiente**. |
| Interpretação | Aplicar as [regras de julgamento](criterios-julgamento.md), por grupo de julgamento e com cobertura obrigatória completa. Falhas permanecem visíveis; ausência de dados ou parâmetros aprovados implica resultado inconclusivo. |
| Simplicidade, objetividade e validade | fórmulas simples; dependem de ferramentas identificadas; têm validade apenas para o recurso e o ambiente realmente instrumentados, não para toda a plataforma. **Validação da instrumentação pendente**. |
| Situação da medição | a coletar (F4). |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M3 — Proporção de combinações ambiente–fluxo executáveis (Q3)

M3 representa o percentual de combinações elegíveis entre ambientes de acesso e fluxos previstos no plano de avaliação que podem ser concluídas sem modificar o produto. As combinações são classificadas previamente como essenciais ou complementares. M3.AMB considera ambiente–fluxo; M3.JAN considera ambiente–janela–fluxo. Cada desdobramento é calculado separadamente, conforme os grupos de julgamento definidos nesta página. Não há percentual único que misture M3.AMB e M3.JAN. A cobertura do plano é apresentada separadamente dos percentuais observados.

**Tabela 3 — Especificação da métrica M3.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q3.1–Q3.2 / H3.1–H3.2 |
| Cálculo | `100 × C / N`, separadamente para M3.AMB e M3.JAN em cada grupo; `C` = combinações distintas bem-sucedidas e `N` = combinações distintas elegíveis efetivamente avaliadas com todas as repetições obrigatórias válidas, essenciais e complementares. Falhas observadas permanecem no denominador; repetições não criam combinações adicionais. Com `N = 0`, o resultado é inconclusivo. |
| Unidade | %. |
| Fonte dos dados | matriz de ambientes e roteiros de teste com evidências de execução. |
| Forma de coleta | repetir fluxos equivalentes em ambientes determinados pela Fase 1/3, documentar sucesso/falha e evidência. Restringir as combinações ao escopo web e registrar impossibilidades técnicas (por exemplo, navegadores incompatíveis com determinado SO); não contar combinações inviáveis como falhas de produto. |
| Interpretação | Aplicar as [regras de julgamento](criterios-julgamento.md), por grupo de julgamento e com cobertura obrigatória completa. Falhas permanecem visíveis; ausência de dados ou parâmetros aprovados implica resultado inconclusivo. |
| Simplicidade, objetividade e validade | cálculo simples e binário; depende de critérios de sucesso por fluxo; mede a adaptação nos ambientes da amostra, não uma garantia universal de portabilidade. |
| Situação da medição | a coletar (F4). |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M4 — Proporção de tarefas executáveis com recursos de acessibilidade (Q4)

percentual de combinações elegíveis entre tarefas e recursos de acessibilidade selecionados que permitem realizar o resultado esperado, segundo roteiro prévio.

**Tabela 4 — Especificação da métrica M4.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q4.1–Q4.4 / H4.1–H4.4 |
| Cálculo | `M4 = 100 × A / N`, com `A` = combinações que atendem ao critério de execução acessível e `N` = combinações testadas; registrar barreiras qualitativas à parte. |
| Unidade | %. |
| Fonte dos dados | observações e registros de testes com leitor de tela, ampliação ou alto contraste, incluindo NVDA, VoiceOver e Orca conforme previsto na Fase 1, somente nas combinações efetivamente viáveis. |
| Forma de coleta | executar roteiros reproduzíveis, registrar recurso usado e versão, obstáculo observado, resultado e evidência; verificações automáticas, se utilizadas, são complementares e não equivalem sozinhas à execução acessível. |
| Interpretação | Aplicar as [regras de julgamento](criterios-julgamento.md), por grupo de julgamento e com cobertura obrigatória completa. Falhas permanecem visíveis; ausência de dados ou parâmetros aprovados implica resultado inconclusivo. |
| Simplicidade, objetividade e validade | razão simples; objetividade requer regra verificável de sucesso; validade limitada às tarefas, tecnologias assistivas e perfis efetivamente examinados. |
| Situação da medição | a coletar (F4). |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M5 — Taxa de conclusão autônoma por estudantes novos (Q5)

percentual de pares participante–tarefa elegíveis em que participantes sem experiência prévia conseguem concluir tarefa especificada após a instrução inicial padronizada, sem ajuda adicional.

**Tabela 5 — Especificação da métrica M5.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q5 / H5 |
| Cálculo | `M5 = 100 × S / N`, com `S` = pares participante–tarefa concluídos autonomamente e `N` = pares elegíveis validamente observados. Falhas e pedidos de ajuda não contam como sucesso autônomo. |
| Unidade | %. |
| Fonte dos dados | protocolos de observação, formulários e registros consentidos dos testes com participantes; perfis e recrutamento **a definir**. |
| Forma de coleta | definir instrução e tarefa antes do teste, registrar experiência declarada do participante, conclusão, intervenções e contexto; proteger identificação dos participantes. |
| Interpretação | Aplicar as [regras de julgamento](criterios-julgamento.md), por grupo de julgamento e com cobertura obrigatória completa. Falhas permanecem visíveis; ausência de dados ou parâmetros aprovados implica resultado inconclusivo. |
| Simplicidade, objetividade e validade | cálculo simples; autonomia depende de regra explícita sobre intervenções; validade condicionada à definição de “estudante novo” e às condições comparáveis de instrução. |
| Situação da medição | a coletar (F4). |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*

## Desdobramentos e regras de sucesso

A Tabela 6 complementa as fichas, preservando M1–M5 como famílias.

**Tabela 6 — Operacionalização das famílias M1–M5.**

| ID | Cálculo e unidade | Cuidados e regra de sucesso |
|---|---|---|
| M1 | `T = t_fim − t_inicio` em segundos; mediana por etapa/ambiente/rede | Separar carregamento de página, início de vídeo e resposta a exercício. Não incluir duração pedagógica de assistir ou resolver no tempo de resposta do sistema. Fixar marcos, timeout e repetições antes da coleta. Falha não vira zero nem é descartada. |
| M2.CPU | Média de amostras de CPU ao longo da janela padronizada, em % da capacidade total disponibilizada à VM | Amostragem em intervalos iguais ou média ponderada pelo tempo; declarar normalização por núcleos, processos incluídos e ferramenta. Registrar saturação e bloqueios, sem inferir causa somente por correlação. |
| M2.RAM | Máximo da memória atribuível à sessão no intervalo, em MiB | Registrar processos incluídos, coleta de memória compartilhada e linha de base. Usar o mesmo método em ambientes comparados. |
| M2.REDE | Bytes enviados + recebidos no intervalo, convertidos para unidade declarada | Definir camada da medição para evitar dupla contagem; mesma duração de vídeo, qualidade, cache e tarefas. Falhas que transferem poucos dados não indicam eficiência. |
| M3.AMB | `100 × C/N`, por ambiente e no conjunto | Unidade de observação: ambiente–fluxo. Sucesso: resultado esperado sem ajuste extraordinário. Falha observada fica em N. Ambiente não executado não é sucesso nem desaparece da cobertura planejada. |
| M3.JAN | `100 × C/N`, por tamanho de janela e no conjunto | Unidade: ambiente–janela–fluxo. Sucesso requer resultado esperado e controles/conteúdo essenciais utilizáveis. Tamanhos definidos antes do teste. |
| M4.TEC, M4.LEI, M4.AMP, M4.CON | Cada uma conserva `100 × A/N` da família M4, calculada separadamente | Unidade: ambiente–recurso–tarefa. A exige conclusão e atendimento ao checklist aplicável ao atributo. Falha de qualquer item aplicável impede contar a combinação como sucesso. Registrar critério WCAG, elemento e evidência. |
| M5 | `100 × S/N`, por tarefa e no conjunto | Unidade: participante–tarefa elegível. S exige conclusão após instrução padronizada, sem ajuda adicional, dentro da janela de observação previamente definida. Falha e pedido de ajuda ficam no denominador. |

*Fonte: adaptação das fichas da branch; proposta metodológica para manter rastreabilidade e comparabilidade.*

M2.CPU, M2.RAM e M2.REDE não são somadas: têm unidades diferentes. M4.CON não deve misturar “quantidade de elementos com contraste adequado” com “quantidade de tarefas executáveis” no mesmo denominador. O checklist por elemento sustenta a classificação binária de cada tarefa; guardar também seus achados individuais.

Em M3/M4, guardar numerador e denominador de cada grupo de julgamento. Em M5, guardar também número de participantes únicos e tentativas por tarefa: várias tentativas da mesma pessoa não representam várias pessoas independentes. Definir estudante novo por critério de elegibilidade anterior ao recrutamento; não excluir depois participantes que tiveram dificuldade.

Em todos os casos, **resultados: a coletar na Fase 4**. Um piloto pode fundamentar viabilidade e orçamentos, mas deve ser identificado, documentado e separado da avaliação final se os critérios forem ajustados a partir dele.

## Unidades de observação e grupos de julgamento

Uma observação é o registro individual do ensaio. Um grupo de julgamento reúne observações comparáveis e recebe pontuação. Em M3/M4, a escala se aplica ao conjunto de combinações do grupo, conforme a Tabela 7. A questão recebe a menor pontuação de seus grupos obrigatórios com cobertura completa.

**Tabela 7 — Observações e grupos de julgamento.**

| Medida | Uma observação | Grupo de julgamento |
|---|---|---|
| M1 | Uma execução de etapa em ambiente e rede definidos. | Execuções comparáveis da mesma etapa–ambiente–rede. |
| M2.CPU / M2.RAM / M2.REDE | Uma medida de recurso em execução padronizada. | Execuções comparáveis do recurso–fluxo–configuração–rede. |
| M3.AMB | Uma combinação ambiente–fluxo. | Fluxos planejados para um ambiente. |
| M3.JAN | Uma combinação ambiente–janela–fluxo. | Fluxos planejados para um ambiente e tamanho de janela. |
| Cada M4 | Uma combinação ambiente–recurso assistivo–tarefa. | Tarefas planejadas para um ambiente e recurso de acessibilidade. |
| M5 | Um par participante–tarefa na primeira tentativa elegível. | Pares elegíveis de uma tarefa; também apresentar o conjunto. |

*Fonte: especificação GQM desta fase, derivada dos requisitos R1–R5.*

Em M3/M4, `N` conta combinações distintas elegíveis com todas as repetições obrigatórias validamente avaliadas, incluindo falhas observadas do produto; combinações com cobertura incompleta ficam discriminadas à parte. Em M5, conta pares participante–tarefa validamente observados, incluindo falhas e pedidos de ajuda. Com `N = 0`, não há percentual nem pontuação: o resultado é inconclusivo. Numerador, denominador e cobertura do plano são apresentados separadamente. Uma combinação planejada não executada não desaparece da cobertura.

M5 considera somente a primeira tentativa elegível de cada participante em cada tarefa. Repetições são registradas separadamente e não entram novamente no cálculo da aprendizagem inicial. A elegibilidade de estudante novo é definida antes do recrutamento.

## Repetições, resumos e falhas

Em M3 e M4, cada combinação elegível tem identidade única e entra no denominador uma única vez. A regra conservadora proposta, a ratificar antes da coleta final, classifica uma combinação como bem-sucedida somente quando todas as repetições planejadas forem validamente realizadas e atenderem ao critério de sucesso. Uma falha observada do produto impede o sucesso da combinação. As execuções individuais e suas evidências permanecem registradas. Uma repetição obrigatória ausente ou inválida deixa a cobertura da combinação incompleta; falhas já observadas são relatadas como achados parciais.

Com cobertura completa da combinação, ela conta uma vez em `N` e, quando bem-sucedida, uma vez em `C` (M3) ou `A` (M4). Repetições não são novas combinações. Combinações incompletas têm resultados e lacunas apresentados separadamente; o grupo afetado não recebe nota completa. O percentual parcial utiliza somente combinações completamente avaliadas e é identificado como parcial, acompanhado da cobertura do plano.

Exemplo exclusivamente lógico, sem dados do projeto: uma combinação ambiente–fluxo com uma execução bem-sucedida e uma falha de produto, ambas válidas e correspondentes a todas as repetições previstas, conta como uma combinação avaliada e não bem-sucedida, e não como duas combinações com 50% de sucesso. A quantidade de repetições, sua justificativa e condições comparáveis são fixadas no protocolo antes dos resultados; essa regra não é uma exigência da ISO.

M1 utiliza a mediana dos tempos concluídos do grupo. Uma execução sem marco final é registrada como falha, com instante de interrupção ou timeout e evidência; não recebe tempo zero. O resumo acompanha o total de execuções, sucessos, falhas e registros inválidos. Bloqueio de etapa essencial atribuído ao produto segundo o protocolo aciona a regra impeditiva, independentemente da mediana dos sucessos.

Em M2, cada execução produz separadamente média temporal de CPU, pico de memória e tráfego total. O resumo de execuções válidas e comparáveis é a mediana dos valores de cada recurso, com valores individuais e maior valor observado. Para RAM, esse resumo é a **mediana dos picos entre sessões**, distinta do maior pico de todo o ensaio. Essa opção metodológica requer ratificação antes da coleta e não é uma determinação da ISO. Se o orçamento de RAM for um limite rígido de capacidade, o protocolo deverá estabelecer previamente a regra para violações individuais; essa pendência impede fechar o julgamento correspondente.

CPU usa amostragem em intervalos iguais ou média ponderada pela duração. O protocolo registra significado do percentual, normalização pela capacidade total da VM e processos incluídos. CPU, RAM e rede não são somadas. Uma falha que reduz o tráfego não comprova eficiência.

O protocolo versionado fixa etapa, fluxo, ambiente, rede, recurso, instrumento, janela de observação, número de repetições, marcos, timeout e elegibilidade antes do ensaio final. Os registros incluem valores individuais, resumo, falhas, invalidações e evidências. Interrupção externa ou instrumentação inválida representa dado ausente/inválido, sem comprovar falha do produto. A ausência de observações obrigatórias torna a nota completa inconclusiva, preservando achados parciais. As regras e definições de cobertura estão nos [critérios de julgamento](criterios-julgamento.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | 
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 17/10/2026 | Especificação das métricas de qualidade, incluindo definições, fórmulas, fontes de dados, procedimentos de coleta e critérios de interpretação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) | 
| 1.1 | 19/10/2026 | Sincronização das fichas com os desdobramentos, grupos de julgamento, elegibilidade, falhas e critérios de julgamento. | Camila Silva (apoio de Codex) | Revisão humana pendente |
| 1.2 | 19/10/2026 | Ajustes complementares da issue #7: observações e grupos, repetições, cobertura, hipóteses e figuras sincronizadas, com apoio de Codex. | Camila Silva | Revisão humana pendente |
| 1.3 | 19/10/2026 | Alinhamento de M3 a combinações essenciais/complementares e definição de identidade única, sucesso e cobertura em repetições de M3/M4. | Camila Silva | Revisão humana pendente |


---

[Navegar pela Fase 2](index.md)
