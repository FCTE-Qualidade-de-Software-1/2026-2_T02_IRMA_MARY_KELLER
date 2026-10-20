[← Visão geral da Fase 2](index.md)

# Especificação das métricas — nível quantitativo

As **Tabelas 2 a 6** detalham cada métrica em formato padronizado, incluindo cálculo, unidade, fontes, coleta e critérios de interpretação.

**Todas as observações, os numeradores, os denominadores, os tempos, as medições de recursos e os resultados finais estão _a coletar na Fase 4_.** Procedimentos detalhados, ambiente, repetições e elegibilidade deverão constar do plano da Fase 3. Não preencher resultados fictícios.

## M1 — Tempo observado de execução de fluxo (Q1)

intervalo entre o marco inicial e o marco final observáveis de um fluxo previamente descrito (por exemplo, solicitação de abertura de aula e conclusão de seu carregamento observável). Cada fluxo precisa ter marcos definidos antes da coleta.

M1 verifica H1 com medianas por etapa, fluxo, ambiente e rede, sem incluir o tempo pedagógico. Registrar bloqueios essenciais separadamente: uma mediana aceitável não elimina um bloqueio atribuível ao produto.

**Tabela 2 — Especificação da métrica M1.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q1 / H1 |
| Cálculo | para cada execução válida, `T = t_fim − t_início`; para resumo de execuções comparáveis, `T_mediano = mediana(T1, …, Tn)`. |
| Unidade | segundos (s). |
| Fonte dos dados | marcações de tempo e registros de execução produzidos nos testes da interface; ferramentas de desenvolvedor do navegador (DevTools), previstas no escopo, e registros de execução; procedimentos exatos a especificar na Fase 3. |
| Forma de coleta | executar fluxo nos ambientes e condições de rede definidos na Fase 3; registrar eventos inicial/final, falhas, ambiente e repetições; não transformar falha de carregamento em tempo zero. |
| Interpretação | menor tempo é preferível **para o mesmo fluxo e condições comparáveis**; comparar com limite de aceitação **pendente de definição fundamentada**. Execuções não concluídas devem ser relatadas separadamente. |
| Simplicidade, objetividade e validade | cálculo simples; marcos registrados tornam a medida replicável; mede comportamento temporal observável, mas não explica causas de lentidão do backend. **Validade condicionada** a marcos consistentes e controle do ambiente. |
| Situação da medição | a coletar na Fase 4. |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M2 — Consumo de recursos por fluxo (Q2–Q4)

quantidade de um recurso consumida durante fluxo definido. **CPU, memória e tráfego de rede são medidas diferentes e não serão somadas.** A seleção exata do recurso disponível para cada ambiente fica condicionada ao plano de coleta.

M2 produz três resultados independentes. Para H2, comparar CPU_média ao orçamento de processamento e registrar a série, picos e duração de sobrecargas conforme protocolo; a média isolada não verifica a ausência de sobrecarga impeditiva. Documentar ferramenta, processos, intervalo de amostragem e significado do percentual. Para H3, comparar RAM_pico de cada execução válida ao orçamento da sessão: nenhuma média ou mediana substitui os picos ou oculta violações individuais. Registrar interrupções e evidências de atribuição ao esgotamento. Para H4, comparar D por fluxo padronizado ao orçamento de dados, controlando cache, duração e qualidade dos vídeos. Tráfego baixo de execução interrompida não representa eficiência. Orçamentos e critérios de atribuição permanecem pendentes.

**Tabela 3 — Especificação da métrica M2.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q2 / H2 (CPU); Q3 / H3 (memória); Q4 / H4 (tráfego) |
| Cálculo | tráfego transferido `D = bytes_recebidos + bytes_enviados` no intervalo do fluxo; memória observada `RAM_pico = max(RAM(t))`; CPU observada `CPU_média = (Σ CPU_i)/n`, desde que a ferramenta explicite o significado de cada amostra. |
| Unidades | bytes ou MB para tráfego e memória; percentual (%) para uso de CPU quando compatível com a ferramenta. |
| Fonte dos dados | medições de ferramentas do navegador ou do sistema operacional, DevTools e monitoramento do sistema/VM previstos na Fase 1; instrumento e configuração exatos a registrar na Fase 3. |
| Forma de coleta | medir apenas os recursos que a equipe conseguir isolar e registrar; guardar ferramenta, versão, fluxo, instante, condições de fundo e dados brutos. Se o consumo atribuível à sessão web não puder ser obtido de modo confiável, marcar **não avaliável naquele ambiente**. |
| Interpretação | menor consumo pode ser preferível quando comparados fluxos equivalentes; nenhuma faixa aceitável está documentalmente fixada. A comparação exige ambiente e ferramenta equivalentes. |
| Simplicidade, objetividade e validade | fórmulas simples; dependem de ferramentas identificadas; têm validade apenas para o recurso e o ambiente realmente instrumentados, não para toda a plataforma. **Validação da instrumentação pendente**. |
| Situação da medição | a coletar na Fase 4. |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M3 — Proporção de combinações ambiente–fluxo executáveis (Q5–Q6)

percentual de combinações elegíveis de ambiente de acesso e fluxo essencial que podem ser concluídas sem modificar o produto, segundo critérios de conclusão especificados antes do teste.

Aplicar a fórmula separadamente: Q5/H5 usa combinações SO–navegador–fluxo, com registro de ajustes extraordinários; Q6/H6 usa ambiente–tamanho de janela–fluxo, com dimensões registradas e evidências de preservação dos conteúdos e controles. Não misturar denominadores nem contar a mesma observação duas vezes dentro da mesma questão. Manter a matriz individual, o conjunto essencial planejado e as lacunas: o percentual das combinações testadas não comprova cobertura. H5 e H6 exigem sucesso de todas as combinações essenciais correspondentes; qualquer falha essencial impede sustentação, e cobertura incompleta sem evidência suficiente torna o julgamento inconclusivo.

**Tabela 4 — Especificação da métrica M3.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q5 / H5; Q6 / H6, separadamente |
| Cálculo | `M3 = 100 × C / N`, com `C` = combinações executadas com sucesso e `N` = combinações elegíveis efetivamente testadas. Falhas observadas permanecem no denominador. |
| Unidade | %. |
| Fonte dos dados | matriz de ambientes e roteiros de teste com evidências de execução. |
| Forma de coleta | repetir fluxos equivalentes em ambientes determinados pela Fase 1/3, documentar sucesso/falha e evidência. Restringir as combinações ao escopo web e registrar impossibilidades técnicas (por exemplo, navegadores incompatíveis com determinado SO); não contar combinações inviáveis como falhas de produto. |
| Interpretação | quanto maior, maior a proporção de combinações executáveis **na amostra testada**; não generalizar a outros dispositivos. Se `N = 0`, sem dados. |
| Simplicidade, objetividade e validade | cálculo simples e binário; depende de critérios de sucesso por fluxo; mede a adaptação nos ambientes da amostra, não uma garantia universal de portabilidade. |
| Situação da medição | a coletar na Fase 4. |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M4 — Proporção de tarefas executáveis com recursos de acessibilidade (Q7–Q10)

percentual de combinações elegíveis entre tarefas e recursos de acessibilidade selecionados que permitem realizar o resultado esperado, segundo roteiro prévio.

Calcular A/N separadamente para Q7/H7 (teclado, sem mouse, sem armadilhas ou controles necessários inacessíveis), Q8/H8 (leitor de tela e informação percebida), Q9/H9 (ampliação, mecanismo e configuração, preservando conteúdo e funcionalidade) e Q10/H10 (checklist dos critérios de contraste selecionados e usabilidade em alto contraste). Registrar ambiente, tarefa, recurso, versão, configuração e cada achado. Alto contraste não substitui a medição dos critérios de contraste; ampliação não se confunde com janela em Q6. A classificação binária deve ser sustentada pelas evidências de cada condição. H7–H9 exigem todas as combinações essenciais; H10 exige os elementos necessários conformes aos critérios selecionados e utilizáveis em alto contraste. Percentuais agregados não ocultam falhas; lacunas de cobertura ou parâmetros tornam o julgamento inconclusivo quando faltam evidências suficientes.

**Tabela 5 — Especificação da métrica M4.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q7 / H7 (teclado); Q8 / H8 (leitor de tela); Q9 / H9 (ampliação); Q10 / H10 (contraste) |
| Cálculo | `M4 = 100 × A / N`, com `A` = combinações que atendem ao critério de execução acessível e `N` = combinações testadas; registrar barreiras qualitativas à parte. |
| Unidade | %. |
| Fonte dos dados | observações e registros de testes com leitor de tela, ampliação ou alto contraste, incluindo NVDA, VoiceOver e Orca conforme previsto na Fase 1, somente nas combinações efetivamente viáveis. |
| Forma de coleta | executar roteiros reproduzíveis, registrar recurso usado e versão, obstáculo observado, resultado e evidência; verificações automáticas, se utilizadas, são complementares e não equivalem sozinhas à execução acessível. |
| Interpretação | maior percentual indica menos barreiras nos cenários testados; uma falha crítica pode exigir análise separada mesmo se o percentual agregado for elevado. Limiar quantitativo de aceitação pendente. |
| Simplicidade, objetividade e validade | razão simples; objetividade requer regra verificável de sucesso; validade limitada às tarefas, tecnologias assistivas e perfis efetivamente examinados. |
| Situação da medição | a coletar na Fase 4. |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*


## M5 — Taxa de conclusão autônoma por estudantes novos (Q11)

percentual de tentativas elegíveis em que participantes sem experiência prévia conseguem concluir tarefa especificada após a instrução inicial padronizada, sem ajuda adicional.

Para H11, considerar somente a primeira tentativa de cada par participante–tarefa após instrução padronizada. Aplicar a fórmula por tarefa essencial e também ao conjunto, sem ocultar tarefas abaixo do patamar. Registrar ajuda, intervenções e janela de observação; patamares por tarefa e conjunto, elegibilidade e janela permanecem a definir antes da coleta.

**Tabela 6 — Especificação da métrica M5.**

| Campo | Especificação |
|---|---|
| Questão e hipótese | Q11 / H11 |
| Cálculo | `M5 = 100 × S / N`, com `S` = tentativas concluídas autonomamente e `N` = tentativas elegíveis realizadas. Falhas e pedidos de ajuda não contam como sucesso autônomo. |
| Unidade | %. |
| Fonte dos dados | protocolos de observação, formulários e registros consentidos dos testes com participantes; perfis e recrutamento **a definir**. |
| Forma de coleta | definir instrução e tarefa antes do teste, registrar experiência declarada do participante, conclusão, intervenções e contexto; proteger identificação dos participantes. |
| Interpretação | maior percentual sugere melhor apreensibilidade nos fluxos testados, mas não caracteriza toda a população estudantil; limite para decisão sobre aula introdutória **pendente de justificativa**. |
| Simplicidade, objetividade e validade | cálculo simples; autonomia depende de regra explícita sobre intervenções; validade condicionada à definição de “estudante novo” e às condições comparáveis de instrução. |
| Situação da medição | a coletar na Fase 4. |

*Fonte: elaboração para a Fase 2 a partir dos requisitos de avaliação R1–R5 e das definições metodológicas desta seção. A coleta ainda não foi realizada.*

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | 
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 17/10/2026 | Especificação das métricas de qualidade, incluindo definições, fórmulas, fontes de dados, procedimentos de coleta e critérios de interpretação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) | 
| 1.1 | 20/10/2026 | Sincronização de M1–M5 com 11 hipóteses e condições de verificação por componente. | [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Pedro Lucas](https://github.com/Pwdrinho) |


---

[Navegar pela Fase 2](index.md)
