# Ambiente de testes e ferramentas de avaliação

**Versão 1.1**

Este documento define e descreve a infraestrutura de ambientes, virtualização, navegadores e ferramentas utilizadas na condução dos ensaios de avaliação da versão web da Khan Academy em computadores. Ele operacionaliza os requisitos da [Fase 1](../fase-1/index.md) [S1](#s1) (especialmente o [escopo da avaliação](../fase-1/escopo-da-avaliacao.md#ambientes-de-teste) [S2](#s2) e os [requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md) [S3](#s3)), fornece a base instrumental para as métricas da [Fase 2](../fase-2/index.md) [S4](#s4) e atende aos critérios de avaliação da Fase 3 ([Critérios QSW — Fase 3](../criterios/fase3.md), com destaque para `F3-C2` e `F3-C8`) [S5](#s5).

O ambiente aqui especificado atende conjuntamente aos [Procedimentos de avaliação de adaptabilidade (M6 e M7)](procedimentos-adaptabilidade.md) [S6](#s6) e aos [Procedimentos de avaliação de eficiência de desempenho (M1 a M5)](procedimentos-desempenho.md) [S7](#s7), estabelecendo condições controladas, reprodutíveis e auditáveis para os testes da Fase 4.

## 1. Escopo e organização dos ambientes

A avaliação contempla uma matriz direcionada de ambientes (`A1` a `A4`), complementada por ambientes adicionais no ecossistema Linux para fins de portabilidade, conforme delimitado no escopo da Fase 1 [S2](#s2).

1. **Ambiente de referência para eficiência de desempenho (`A1`):** Todas as medições de eficiência de desempenho (comportamento temporal e utilização de recursos, métricas `M1` a `M5`) são executadas **exclusivamente no ambiente `A1`** (Windows 11 Pro com Google Chrome), submetido a duas condições de rede controladas (normal e limitada).
2. **Matriz principal de adaptabilidade (`A1` a `A4`):** Os testes de adaptabilidade entre sistemas operacionais e navegadores (`M6`) e de adaptação ao tamanho da janela (`M7`) utilizam as quatro combinações principais:
   - `A1`: Windows 11 Pro + Google Chrome (motor Blink);
   - `A2`: Windows 11 Pro + Mozilla Firefox (motor Gecko);
   - `A3`: macOS + Apple Safari (motor WebKit);
   - `A4`: Ubuntu 26.04 LTS + Mozilla Firefox (motor Gecko).
3. **Ambientes Linux complementares (`AC1` a `AC3`):** Para aprofundar a observação da adaptabilidade em sistemas abertos amplamente utilizados no ambiente desktop, são preparadas distribuições Linux adicionais (Fedora, Arch Linux e openSUSE Leap). Seus resultados são relatados de forma complementar, sem alterar o denominador formal de cálculo de `M6` definido na Fase 2 [S4](#s4).

## 2. Virtualização e padronização dos recursos de hardware

Com o objetivo de garantir a padronização e a comparabilidade dos recursos de hardware aos quais cada sistema convidado tem acesso — simulando de forma controlada computadores com recursos limitados típicos do cenário de escolas públicas [S1](#s1) —, todos os ambientes, com exceção do macOS, são executados sob virtualização.

- **Recursos alocados:** Cada ambiente virtualizado recebe estritamente a cota padronizada de **4 GB de memória RAM** e **4 vCPUs**, mantendo coerência com o perfil de computador com recursos limitados estabelecido nos [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md) [S3](#s3) e nas justificativas de [Critérios de julgamento](../fase-2/criterios-julgamento.md) [S8](#s8).
- **Ambientes Linux:** A gestão da virtualização é provida pelo hipervisor **QEMU/KVM**, com interface de gerenciamento via [GNOME Boxes](https://apps.gnome.org/pt-BR/Boxes/).
- **Ambientes Windows (`A1` e `A2`):** A execução virtualizada do Windows 11 Pro utiliza conteinerização orientada pelo Docker, com interface de gerenciamento via [Winboat](https://www.winboat.app/).
- **Ambiente macOS (`A3`):** Em virtude de restrições de licenciamento e suporte de virtualização para a plataforma Apple, o ambiente `A3` é executado em máquina física dedicada, cujas especificações de processador e memória são devidamente anotadas no registro de preparação.

## 3. Sistemas operacionais e navegadores

A Tabela 1 apresenta a lista dos sistemas operacionais e as versões dos navegadores estáveis vigentes utilizadas durante os ensaios. O Arch Linux, por adotar modelo de atualização contínua (*rolling release*), não possui numeração fixa de versão do sistema.

| Identificador | Sistema operacional | Navegador | Motor de renderização | Versão do navegador | Modalidade de execução | Recursos de hardware |
|:---:|---|---|---|:---:|---|---|
| `A1` | Windows 11 Pro | Google Chrome | Blink | 157.0 | Virtualizado (Docker / Winboat) | 4 GB RAM, 4 vCPUs |
| `A2` | Windows 11 Pro | Mozilla Firefox | Gecko | 159.1 | Virtualizado (Docker / Winboat) | 4 GB RAM, 4 vCPUs |
| `A3` | macOS (a registrar) | Apple Safari | WebKit | A registrar | Máquina física | A registrar na preparação |
| `A4` | Ubuntu 26.04 | Mozilla Firefox | Gecko | 159.0 | Virtualizado (QEMU/KVM / GNOME Boxes) | 4 GB RAM, 4 vCPUs |
| `AC1` | Fedora 44 | Chrome / Firefox | Blink / Gecko | 156.0 / 159.0 | Virtualizado (QEMU/KVM / GNOME Boxes) | 4 GB RAM, 4 vCPUs |
| `AC2` | Arch Linux (*rolling*) | Chrome / Firefox | Blink / Gecko | 156.0 / 159.0 | Virtualizado (QEMU/KVM / GNOME Boxes) | 4 GB RAM, 4 vCPUs |
| `AC3` | openSUSE Leap 16.1 | Chrome / Firefox | Blink / Gecko | 156.0 / 153.5 | Virtualizado (QEMU/KVM / GNOME Boxes) | 4 GB RAM, 4 vCPUs |

*Tabela 1. Sistemas operacionais, navegadores e recursos por ambiente. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

As máquinas virtuais e seus respectivos navegadores são atualizados via gerenciador de pacotes na etapa de preparação formal antes do início das medições oficiais (verificação `PA-1` / `PD-1`), congelando-se a data e desativando-se atualizações automáticas durante a coleta de dados da Fase 4.

## 4. Ferramentas de medição, diagnóstico e apoio aos ensaios

Para a condução dos testes de eficiência de desempenho, adaptabilidade e acessibilidade, a equipe utiliza um conjunto integrado de ferramentas de instrumentação, inspeção e diagnóstico. A Tabela 2 relaciona essas ferramentas, especificando sua finalidade e sua aplicação no estudo. Conforme diretriz do plano de testes, as ferramentas são empregadas em suas distribuições nativas ou integradas aos ambientes, sem fixação antecipada de versões isoladas.

| Ferramenta | Categoria | Finalidade no estudo | Métricas e atributos relacionados | Ambiente de aplicação |
|---|---|---|---|---|
| **Lighthouse** | Auditoria automatizada de desempenho | Avaliação e diagnóstico de desempenho em laboratório nas páginas de entrada dos fluxos, gerando indicadores de carregamento (Performance Score, FCP, LCP, TBT, Speed Index) para análise complementar de qualidade | Apoio diagnóstico a M1 e M5 | Ambiente de referência `A1` (Chrome) |
| **Google Chrome DevTools (Painel Network / Rede)** | Inspetor de rede e tráfego | Registro do volume de dados transferidos (enviados e recebidos) em execuções completas dos fluxos padronizados, com controle estrito de cache e emulação de perfis de rede | `M5` (Dados transferidos), perfil de rede limitada | Ambiente de referência `A1` |
| **Google Chrome DevTools (Painel Console e APIs de temporização)** | Temporização instrumental | Execução de comandos de extração de marcas temporais de navegação (*Navigation Timing API* e `performance.now()`), garantindo precisão milimétrica na medição do tempo observável por etapa | `M1` (Tempo observável por etapa) | Ambiente de referência `A1` |
| **Google Chrome DevTools (Painel Performance / Desempenho)** | Profiling de execução | Rastreamento da atividade da *thread* principal, identificação de tarefas longas (*Long Tasks*) e análise de gargalos de renderização e scripts durante a execução dos fluxos | Diagnóstico de M1 e M3 | Ambiente de referência `A1` |
| **Gerenciador de Tarefas do Chrome (`Shift+Esc`)** | Monitor de recursos por processo | Leitura isolada do consumo percentual de CPU e de memória privada/comprometida da aba e do processo renderizador correspondente à Khan Academy | `M3` (Utilização de CPU) e `M4` (Pico de memória) | Ambiente de referência `A1` |
| **Monitores de Recursos do Sistema Operacional (Task Manager / Resource Monitor)** | Monitor do sistema operacional | Monitoramento da carga global de CPU e de memória do sistema operacional convidado, prevenindo interferências de processos de segundo plano e registrando sobrecargas do sistema | `M3` (Utilização de CPU) e `M4` (Pico de memória) | Ambientes virtualizados e máquina física |
| **Utilitários Linux de Monitoramento (`top`, `htop`, `systemd-cgtop`)** | Monitores do sistema Linux | Monitoramento de consumo de recursos nos ambientes Linux para verificação da estabilidade dos sistemas convidados | Verificação de integridade operacional | Ambientes `A4` e complementares (`AC1`–`AC3`) |
| **Emulador de Limitação de Rede (*Network Throttling*)** | Controlador de conectividade | Simulação padronizada e reproduzível do perfil de conexão limitada (largura de banda, latência RTT) diretamente na camada de rede do navegador | `M1`, `M2` e `M5` sob condição limitada | Ambiente de referência `A1` |
| **Tecnologias Assistivas (NVDA, VoiceOver, Orca)** | Leitores de tela | Execução de testes de acessibilidade para avaliar a navegação e a percepção de conteúdos por estudantes com deficiência visual | `M8` e `M9` (acessibilidade) | `A1` (NVDA), `A3` (VoiceOver), `A4` (Orca) |
| **Utilitários Nativos de Captura e Gravação de Tela** | Registro de evidências | Produção de capturas de tela (*screenshots*) dos pontos finais dos fluxos e gravação contínua de vídeo das sessões de teste para auditoria e comprovação das medições | Evidências brutas para todas as métricas | Todos os ambientes |

*Tabela 2. Ferramentas de medição, diagnóstico e apoio aos ensaios. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 5. Condições de conectividade e perfis de rede

Em conformidade com o escopo da Fase 1 [S2](#s2) e os requisitos de avaliação `R1` e `R2` [S3](#s3), a avaliação de eficiência de desempenho no ambiente de referência `A1` é conduzida sob duas condições de conectividade distintas:

1. **Conexão normal (sem limitação artificial):** Utiliza a conexão de banda larga padrão do ambiente de teste, sem imposição de restrições de taxa de transferência ou latência adicional. A velocidade de *download*, *upload* e a latência de referência são registradas antes de cada sessão de teste.
2. **Conexão limitada (perfil escolar controlado):** Emulada por meio do recurso de *Network Throttling* do Google Chrome DevTools no ambiente `A1`, simulando o cenário de acesso compartilhado em laboratórios de informática ou salas de aula de escolas públicas, conforme recomendado na central de suporte da Khan Academy [S9](#s9):
   - **Taxa de transferência de download:** 1.500 kbps (1,5 Mbps);
   - **Taxa de transferência de upload:** 750 kbps (0,75 Mbps);
   - **Latência adicional (RTT):** 150 ms;
   - **Perda de pacotes:** 0%.

Essa padronização assegura que os resultados das métricas temporais (`M1`), de conclusão (`M2`) e de dados transferidos (`M5`) reflitam com precisão o impacto das restrições de infraestrutura sobre a experiência do estudante.

## Referências

<a id="s1"></a>

> [S1] Fase 1: visão geral. Disponível em: [Visão geral da Fase 1](../fase-1/index.md).

<a id="s2"></a>

> [S2] Escopo da avaliação — Fase 1. Fluxos, ambientes, profundidade e limites de validade. Disponível em: [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md).

<a id="s3"></a>

> [S3] Requisitos de avaliação — Fase 1. Requisitos R1–R5 e decisões D1–D4. Disponível em: [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md).

<a id="s4"></a>

> [S4] Fase 2: visão geral. Disponível em: [Visão geral da Fase 2](../fase-2/index.md).

<a id="s5"></a>

> [S5] Critérios de avaliação QSW — Fase 3. Disponível em: [Critérios da Fase 3](../criterios/fase3.md).

<a id="s6"></a>

> [S6] Procedimentos de avaliação de adaptabilidade (M6 e M7) — Fase 3. Disponível em: [Procedimentos de adaptabilidade](procedimentos-adaptabilidade.md).

<a id="s7"></a>

> [S7] Procedimentos de avaliação de eficiência de desempenho (M1 a M5) — Fase 3. Disponível em: [Procedimentos de desempenho](procedimentos-desempenho.md).

<a id="s8"></a>

> [S8] Níveis de pontuação e critérios de julgamento — Fase 2. Disponível em: [Critérios de julgamento](../fase-2/criterios-julgamento.md).

<a id="s9"></a>

> [S9] KHAN ACADEMY. **What devices and specifications work best with Khan Academy Districts?** Help Center. Disponível em: <https://support.khanacademy.org/hc/nl/articles/360048672692>. Acesso em: 7 nov. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 04/11/2026 | Estruturação inicial do ambiente de testes e quadro básico de ferramentas e versões. | [José Augusto](https://github.com/JAugustoM) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 08/11/2026 | Adequação do estilo aos padrões da Fase 3, detalhamento das modalidades de virtualização, especificação dos perfis de rede e expansão das ferramentas de medição (Lighthouse, DevTools, monitores) sem fixação prévia de versões. | [José Augusto](https://github.com/JAugustoM) | [Pedro Lucas](https://github.com/Pwdrinho) |
