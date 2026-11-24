# Ambientes e recursos de avaliação

**Versão 1.2**

Este documento define e descreve a infraestrutura de ambientes, virtualização, navegadores e ferramentas utilizadas na condução dos ensaios de avaliação da versão web da Khan Academy em computadores. Ele operacionaliza os requisitos da [Fase 1](../fase-1/index.md) [S1](#s1) (especialmente o [escopo da avaliação](../fase-1/escopo-da-avaliacao.md#ambientes) [S2](#s2) e os [requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md) [S3](#s3)), fornece a base instrumental para as métricas da [Fase 2](../fase-2/index.md) [S4](#s4) e atende aos critérios de avaliação da Fase 3 ([Critérios QSW — Fase 3](../criterios/fase3.md), com destaque para [`F3-C2`](../criterios/fase3.md) e [`F3-C8`](../criterios/fase3.md)) [S5](#s5).

O ambiente aqui especificado atende conjuntamente aos [Procedimentos de avaliação de adaptabilidade (M6 e M7)](procedimentos-adaptabilidade.md) [S6](#s6) e aos [Procedimentos de avaliação de eficiência de desempenho (M1 a M5)](procedimentos-desempenho.md) [S7](#s7), estabelecendo condições controladas, reprodutíveis e auditáveis para os testes da Fase 4.

## 1. Escopo e organização dos ambientes

A avaliação contempla uma matriz direcionada de ambientes ([`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) a [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes)), conforme delimitado no escopo da Fase 1 [S2](#s2).

1. Ambiente de referência para eficiência de desempenho ([`A1`](../fase-1/escopo-da-avaliacao.md#ambientes)): Todas as medições de eficiência de desempenho (comportamento temporal e utilização de recursos, métricas [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) a [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos)) são executadas exclusivamente no ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) (Windows 11 Pro com Google Chrome), submetido a duas condições de rede controladas (normal e limitada).
2. Matriz principal de adaptabilidade ([`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) a [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes)): Os testes de adaptabilidade entre sistemas operacionais e navegadores ([`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente)) e de adaptação ao tamanho da janela ([`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela)) utilizam as quatro combinações principais:
   - [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes): Windows 11 Pro + Google Chrome (motor Blink);
   - [`A2`](../fase-1/escopo-da-avaliacao.md#ambientes): Windows 11 Pro + Mozilla Firefox (motor Gecko);
   - [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes): macOS + Apple Safari (motor WebKit);
   - [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes): Ubuntu 26.04/26.10 + Mozilla Firefox (motor Gecko).

A cobertura formal de [`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) e [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) utiliza [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) a [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes). A navegação por teclado e por leitor de tela ([`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) e [`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela)) é avaliada em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes). Em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), a resolução de 1366 × 768 é utilizada para o ensaio de ampliação a 200% e as verificações separadas de contraste textual e alto contraste ([`M10`](../fase-2/metricas.md#110-m10-preservacao-com-ampliacao) e [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste)). As sessões de apreensibilidade ([`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos) a [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma)) também utilizam [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) [S10](#s10).

## 2. Virtualização e padronização dos recursos de hardware

Com o objetivo de garantir a padronização e a comparabilidade dos recursos de hardware aos quais cada sistema convidado tem acesso — simulando de forma controlada computadores com recursos limitados típicos do cenário de escolas públicas [S1](#s1) —, todos os ambientes, com exceção do macOS, são executados sob virtualização.

- `Recursos alocados:` Cada ambiente virtualizado recebe estritamente a cota padronizada de `4 GB de memória RAM` e `4 vCPUs`, mantendo coerência com o perfil de computador com recursos limitados estabelecido nos [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md) [S3](#s3) e nas justificativas de [Critérios de julgamento](../fase-2/criterios-julgamento.md) [S8](#s8).
- `Ambiente Linux` ([`A4`](../fase-1/escopo-da-avaliacao.md#ambientes)): A gestão da virtualização é provida pelo hipervisor `QEMU/KVM`, com interface de gerenciamento via [GNOME Boxes](https://apps.gnome.org/pt-BR/Boxes/).
- Ambientes Windows ([`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A2`](../fase-1/escopo-da-avaliacao.md#ambientes)): A execução virtualizada do Windows 11 Pro utiliza conteinerização orientada pelo Docker, com interface de gerenciamento via [Winboat](https://www.winboat.app/).
- Ambiente macOS ([`A3`](../fase-1/escopo-da-avaliacao.md#ambientes)): Em virtude de restrições de licenciamento e suporte de virtualização para a plataforma Apple, o ambiente [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) é executado em máquina física dedicada, cujas especificações de processador e memória são devidamente anotadas no registro de preparação.

## 3. Sistemas operacionais e navegadores

A Tabela 1 apresenta a lista dos sistemas operacionais e as versões dos navegadores estáveis vigentes utilizadas durante os ensaios.

| Identificador | Sistema operacional | Navegador | Motor de renderização | Versão do navegador | Modalidade de execução | Recursos de hardware |
|:---:|---|---|---|:---:|---|---|
| [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Windows 11 Pro | Google Chrome | Blink | 157.0 | Virtualizado (Docker / Winboat) | 4 GB RAM, 4 vCPUs |
| [`A2`](../fase-1/escopo-da-avaliacao.md#ambientes) | Windows 11 Pro | Mozilla Firefox | Gecko | 159.1 | Virtualizado (Docker / Winboat) | 4 GB RAM, 4 vCPUs |
| [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) | macOS (a registrar) | Apple Safari | WebKit | A registrar | Máquina física | A registrar na preparação |
| [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) | Ubuntu 26.04 | Mozilla Firefox | Gecko | 159.0 | Virtualizado (QEMU/KVM / GNOME Boxes) | 4 GB RAM, 4 vCPUs |

*Tabela 1. Sistemas operacionais, navegadores e recursos por ambiente. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

As máquinas virtuais e seus respectivos navegadores são atualizados via gerenciador de pacotes na etapa de preparação formal antes do início das medições oficiais (verificação [`PA-1`](procedimentos-adaptabilidade.md#33-preparacao-do-ambiente) / [`PD-1`](procedimentos-desempenho.md#34-preparacao-do-ambiente-checklist-pd-1-a-pd-10)), congelando-se a data e desativando-se atualizações automáticas durante a coleta de dados da Fase 4.

## 4. Ferramentas de medição, diagnóstico e apoio aos ensaios

Para a condução dos testes de eficiência de desempenho, adaptabilidade e acessibilidade, a equipe utiliza um conjunto integrado de ferramentas de instrumentação, inspeção e diagnóstico. A Tabela 2 relaciona essas ferramentas, especificando sua finalidade e sua aplicação no estudo. Conforme diretriz do plano de testes, as ferramentas são empregadas em suas distribuições nativas ou integradas aos ambientes, sem fixação antecipada de versões isoladas.

| Ferramenta | Categoria | Finalidade no estudo | Métricas e atributos relacionados | Ambiente de aplicação |
|---|---|---|---|---|
| `Lighthouse` | Auditoria automatizada de desempenho | Avaliação e diagnóstico de desempenho em laboratório nas páginas de entrada dos fluxos, gerando indicadores de carregamento (Performance Score, FCP, LCP, TBT, Speed Index) para análise complementar de qualidade | Apoio diagnóstico a [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) e [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos) | Ambiente de referência [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) (Chrome) |
| `Google Chrome DevTools (Painel Network / Rede)` | Inspetor de rede e tráfego | Registro do volume de dados transferidos (enviados e recebidos) em execuções completas dos fluxos padronizados, com controle estrito de cache e emulação de perfis de rede | [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos) (Dados transferidos), perfil de rede limitada | Ambiente de referência [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Google Chrome DevTools (Painel Console e APIs de temporização)` | Temporização instrumental | Execução de comandos de extração de marcas temporais de navegação (*Navigation Timing API* e `performance.now()`), garantindo precisão milimétrica na medição do tempo observável por etapa | [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) (Tempo observável por etapa) | Ambiente de referência [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Google Chrome DevTools (Painel Performance / Desempenho)` | Profiling de execução | Rastreamento da atividade da *thread* principal, identificação de tarefas longas (*Long Tasks*) e análise de gargalos de renderização e scripts durante a execução dos fluxos | Diagnóstico de [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) e [`M3`](../fase-2/metricas.md#13-m3-utilizacao-de-cpu) | Ambiente de referência [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Gerenciador de Tarefas do Chrome (Shift+Esc)` | Monitor de recursos por processo | Leitura isolada do consumo percentual de CPU e de memória privada/comprometida da aba e do processo renderizador correspondente à Khan Academy | [`M3`](../fase-2/metricas.md#13-m3-utilizacao-de-cpu) (Utilização de CPU) e [`M4`](../fase-2/metricas.md#14-m4-pico-de-memoria) (Pico de memória) | Ambiente de referência [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Monitores de Recursos do Sistema Operacional (Task Manager / Resource Monitor)` | Monitor do sistema operacional | Monitoramento da carga global de CPU e de memória do sistema operacional convidado, prevenindo interferências de processos de segundo plano e registrando sobrecargas do sistema | [`M3`](../fase-2/metricas.md#13-m3-utilizacao-de-cpu) (Utilização de CPU) e [`M4`](../fase-2/metricas.md#14-m4-pico-de-memoria) (Pico de memória) | Ambientes virtualizados e máquina física |
| `Utilitários Linux de Monitoramento (top, htop, systemd-cgtop)` | Monitores do sistema Linux | Monitoramento de consumo de recursos no ambiente Linux para verificação da estabilidade do sistema convidado | Verificação de integridade operacional | Ambiente [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Emulador de Limitação de Rede (Network Throttling)` | Controlador de conectividade | Simulação padronizada e reproduzível do perfil de conexão limitada (largura de banda, latência RTT) diretamente na camada de rede do navegador | [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa), [`M2`](../fase-2/metricas.md#12-m2-taxa-de-conclusao-dos-fluxos) e [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos) sob condição limitada | Ambiente de referência [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Tecnologias Assistivas (NVDA, VoiceOver, Orca)` | Leitores de tela | Execução de testes de acessibilidade para avaliar a navegação e a percepção de conteúdos por estudantes com deficiência visual | [`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela) (leitor de tela) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) (NVDA), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) (VoiceOver), [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) (Orca) |
| `Utilitários Nativos de Captura e Gravação de Tela` | Registro de evidências | Produção de capturas de tela (*screenshots*) dos pontos finais dos fluxos e gravação de tela conforme o procedimento aplicável para auditoria e comprovação das medições | Evidências brutas para todas as métricas | Todos os ambientes |
| `Navegadores e registro de adaptabilidade` | Execução e registro | Execução dos fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) a [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos) em `J2` (1920 × 1080) para [`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) e em `J1` (1366 × 768) e `J2` para [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela), com zoom de 100% e registro de conclusão e ocorrências no [formulário de adaptabilidade](../fase-4/registro-adaptabilidade.md) | [`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) e [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) a [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Teclado e ampliação do navegador` | Inspeção manual | Execução das tarefas com navegação exclusiva por teclado e, em ensaio separado, com zoom de 200%. Formulário [`F5`](procedimentos-acessibilidade-apreensibilidade.md#f5-registro-dos-testes-manuais-de-acessibilidade) e evidências de tela | [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) e [`M10`](../fase-2/metricas.md#110-m10-preservacao-com-ampliacao) | Teclado em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes). Ampliação em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Lighthouse e axe DevTools (axe-core)` | Inspeção automatizada de acessibilidade | Identificação de ocorrências para orientar os testes manuais. Os achados são registrados no formulário [`F1`](procedimentos-acessibilidade-apreensibilidade.md#f1-registro-da-inspecao-automatizada) como evidência complementar | Apoio a [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) a [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| `Colour Contrast Analyser e tema de alto contraste do Windows` | Inspeção de contraste | Medição das razões de contraste textual ([`F6`](procedimentos-acessibilidade-apreensibilidade.md#f6-checklist-de-contraste)) e execução separada das tarefas com o tema de alto contraste ([`F5`](procedimentos-acessibilidade-apreensibilidade.md#f5-registro-dos-testes-manuais-de-acessibilidade)) | [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |
| Cartões de tarefa, cronômetro e formulários [`F2`](procedimentos-acessibilidade-apreensibilidade.md#f2-triagem-e-consentimento-dos-voluntarios) a [`F4`](procedimentos-acessibilidade-apreensibilidade.md#f4-percepcao-ao-final-da-sessao) | Sessão com participantes | Triagem e consentimento ([`F2`](procedimentos-acessibilidade-apreensibilidade.md#f2-triagem-e-consentimento-dos-voluntarios)), registro de tentativas, tempos e erros ([`F3`](procedimentos-acessibilidade-apreensibilidade.md#f3-registro-por-tarefa-dos-voluntarios)) e percepção ao final da sessão ([`F4`](procedimentos-acessibilidade-apreensibilidade.md#f4-percepcao-ao-final-da-sessao)) | [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos) a [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) |

*Tabela 2. Ferramentas de medição, diagnóstico e apoio aos ensaios. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 5. Condições de conectividade e perfis de rede

Em conformidade com o escopo da Fase 1 [S2](#s2) e os requisitos de avaliação [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) [S3](#s3), a avaliação de eficiência de desempenho no ambiente de referência [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) é conduzida sob duas condições de conectividade distintas:

1. `Conexão normal (sem limitação artificial):` Utiliza a conexão de banda larga padrão do ambiente de teste, sem imposição de restrições de taxa de transferência ou latência adicional. A velocidade de *download*, *upload* e a latência de referência são registradas antes de cada sessão de teste.
2. `Conexão limitada (perfil escolar controlado):` Emulada por meio do recurso de *Network Throttling* do Google Chrome DevTools no ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), simulando o cenário de acesso compartilhado em laboratórios de informática ou salas de aula de escolas públicas, conforme recomendado na central de suporte da Khan Academy [S9](#s9):
   - `Taxa de transferência de download:` 1.500 kbps (1,5 Mbps);
   - `Taxa de transferência de upload:` 750 kbps (0,75 Mbps);
   - `Latência adicional (RTT):` 150 ms;
   - `Perda de pacotes:` 0%.

Essa padronização assegura que os resultados das métricas temporais ([`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa)), de conclusão ([`M2`](../fase-2/metricas.md#12-m2-taxa-de-conclusao-dos-fluxos)) e de dados transferidos ([`M5`](../fase-2/metricas.md#15-m5-dados-transferidos)) reflitam com precisão o impacto das restrições de infraestrutura sobre a experiência do estudante.

## 6. Dados de teste e preparação da coleta

Devem ser preparados uma conta de estudante, um curso e uma unidade definidos, uma videoaula, um exercício e um estado inicial de progresso adequado à consulta em [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos). Os títulos, endereços e estados iniciais dos conteúdos devem ser registrados, mantendo-se a mesma massa de teste nas execuções comparáveis. Antes da coleta, deve-se conferir o acesso à conta, a disponibilidade do conteúdo e, para [`T1`](procedimentos-acessibilidade-apreensibilidade.md#41-tarefas-de-referencia) a [`T3`](procedimentos-acessibilidade-apreensibilidade.md#41-tarefas-de-referencia), a disponibilidade de legenda, transcrição e dica, conforme o roteiro [S10](#s10). As credenciais devem permanecer restritas.

Na preparação dos ambientes, devem ser registrados a identificação do ambiente, a data, o sistema operacional e seu build, as versões do navegador, das ferramentas e dos leitores de tela, a resolução e as características de hardware. Nos ambientes virtualizados, registram-se também hipervisor, vCPUs, memória, disco e modo de rede. Devem ser verificados o áudio e as tecnologias assistivas em [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes), incluindo o funcionamento do Orca na máquina virtual. Em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), as medições de desempenho usam 1920 × 1080, janela maximizada e zoom de 100%, em perfil de navegador sem extensões que interfiram nos ensaios. Para cada tarefa e condição de rede, realiza-se uma execução de aquecimento, excluída dos cálculos, seguida de cinco repetições válidas [S7](#s7). Após os ensaios de usabilidade, devem ser restauradas as condições de referência antes de uma nova medição de desempenho.

A verificação-piloto deve confirmar a disponibilidade dos fluxos, o funcionamento dos instrumentos, a clareza dos roteiros e a possibilidade de registrar as evidências. Conforme o [Plano de Avaliação](plano-de-avaliacao.md#5-verificacao-dos-instrumentos-e-dos-dados-de-teste), os ajustes de conteúdo, configuração ou instrumento devem ser justificados e documentados antes da coleta oficial. Os dados do piloto ficam fora das métricas oficiais.

Para os ensaios de apreensibilidade, devem ser preparados cartões com as tarefas [`T1`](procedimentos-acessibilidade-apreensibilidade.md#41-tarefas-de-referencia) a [`T3`](procedimentos-acessibilidade-apreensibilidade.md#41-tarefas-de-referencia), instrução inicial padronizada, termo de consentimento, cronômetro e formulários. São previstas sessões em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) com três a cinco participantes adultos sem experiência anterior com a plataforma, com limite de cinco minutos por tarefa. Devem ser registrados os horários, resultados, erros operacionais e pedidos de ajuda. Os participantes são identificados por códigos. Quando autorizada, a gravação se limita à tela e ao áudio do computador. Sem autorização para gravação, o registro da execução é feito no formulário [`F3`](procedimentos-acessibilidade-apreensibilidade.md#f3-registro-por-tarefa-dos-voluntarios). A publicação utiliza dados agregados [S10](#s10).

## Referências

<a id="s1"></a>

> [S1] Fase 1: visão geral. Disponível em: [Visão geral da Fase 1](../fase-1/index.md).

<a id="s2"></a>

> [S2] Escopo da avaliação — Fase 1. Fluxos, ambientes, profundidade e limites de validade. Disponível em: [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md).

<a id="s3"></a>

> [S3] Requisitos de avaliação — Fase 1. Requisitos [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade)–[`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e decisões [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante)–[`D4`](../fase-1/requisitos-de-avaliacao.md#requisitante). Disponível em: [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md).

<a id="s4"></a>

> [S4] Fase 2: visão geral. Disponível em: [Visão geral da Fase 2](../fase-2/index.md).

<a id="s5"></a>

> [S5] Critérios de avaliação QSW — Fase 3. Disponível em: [Critérios da Fase 3](../criterios/fase3.md).

<a id="s6"></a>

> [S6] Procedimentos de avaliação de adaptabilidade ([`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) e [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela)) — Fase 3. Disponível em: [Procedimentos de adaptabilidade](procedimentos-adaptabilidade.md).

<a id="s7"></a>

> [S7] Procedimentos de avaliação de eficiência de desempenho ([`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) a [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos)) — Fase 3. Disponível em: [Procedimentos de desempenho](procedimentos-desempenho.md).

<a id="s8"></a>

> [S8] Níveis de pontuação e critérios de julgamento — Fase 2. Disponível em: [Critérios de julgamento](../fase-2/criterios-julgamento.md).

<a id="s9"></a>

> [S9] KHAN ACADEMY. **What devices and specifications work best with Khan Academy Districts?** Help Center. Disponível em: <https://support.khanacademy.org/hc/nl/articles/360048672692>. Acesso em: 7 nov. 2026.

<a id="s10"></a>

> [S10] Procedimentos de acessibilidade e apreensibilidade ([`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) a [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma)). Disponível em: [Preparação comum](procedimentos-acessibilidade-apreensibilidade.md#2-preparacao-comum), [testes com voluntários](procedimentos-acessibilidade-apreensibilidade.md#5-testes-com-voluntarios) e [instrumentos de coleta](procedimentos-acessibilidade-apreensibilidade.md#8-instrumentos-de-coleta).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 04/11/2026 | Estruturação inicial do ambiente de testes e quadro básico de ferramentas e versões. | [José Augusto](https://github.com/JAugustoM) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 08/11/2026 | Adequação do estilo aos padrões da Fase 3, detalhamento das modalidades de virtualização, especificação dos perfis de rede e expansão das ferramentas de medição (Lighthouse, DevTools, monitores) sem fixação prévia de versões. | [José Augusto](https://github.com/JAugustoM) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.2 | 15/11/2026 | Consolidação de Ambientes e recursos, com cobertura de acessibilidade e apreensibilidade, preparação da coleta, instrumentos e revisão dos links. | [Camila Silva](https://github.com/CamilaSilvaC) e [Geovanna Alves](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
