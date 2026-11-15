# Procedimentos de avaliação de eficiência de desempenho (M1 a M5)

**Versão 1.0**

Este artefato define e padroniza os métodos, instrumentos, roteiros e critérios para a avaliação da **eficiência de desempenho** da versão web da Khan Academy em computadores. A eficiência de desempenho, englobando as subcaracterísticas de **comportamento temporal** e **utilização de recursos** no modelo da ISO/IEC 25010:2011 [S1](#s1), foi estabelecida como prioridade máxima na [Fase 1](../fase-1/index.md) [S4](#s4), respondendo aos requisitos [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) e subsidiando a decisão [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante).

O documento especifica os procedimentos operacionais para obtenção das métricas:
- [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) — Tempo observável por etapa (mediana e P90);
- [`M2`](../fase-2/metricas.md#12-m2-taxa-de-conclusao-dos-fluxos) — Taxa de conclusão dos fluxos;
- [`M3`](../fase-2/metricas.md#13-m3-utilizacao-de-cpu) — Utilização de CPU (média e picos);
- [`M4`](../fase-2/metricas.md#14-m4-pico-de-memoria) — Pico de memória;
- [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos) — Volume de dados transferidos.

Essas métricas respondem diretamente às questões [`Q1`](../fase-2/questoes-hipoteses.md#31-q1-comportamento-temporal), [`Q2`](../fase-2/questoes-hipoteses.md#32-q2-utilizacao-de-cpu), [`Q3`](../fase-2/questoes-hipoteses.md#33-q3-utilizacao-de-memoria) e [`Q4`](../fase-2/questoes-hipoteses.md#34-q4-consumo-de-dados-de-rede), confrontando as hipóteses [`H1` a `H4`](../fase-2/questoes-hipoteses.md#3-g1-eficiencia-de-desempenho) do objetivo [`G1`](../fase-2/objetivos.md#g1) [S6](#s6), estruturado pela abordagem *Goal–Question–Metric* (GQM) [S3](#s3) com referência nas diretrizes de medição da ISO/IEC 25023:2016 [S2](#s2).

O artefato cumpre integralmente os requisitos da issue #25 (*[Fase 3] Definição dos procedimentos de avaliação de desempenho e adaptabilidade*) [S11](#s11) e opera sobre o [ambiente de testes](ambiente-de-testes.md) [S10](#s10). 

**Situação:** especificação de procedimentos, **sem resultados coletados**. A execução oficial das medições e a análise estatística dos dados pertencem à Fase 4. As faixas quantitativas e os limiares de julgamento seguem estritamente as definições aprovadas em [Critérios de julgamento](../fase-2/criterios-julgamento.md) [S9](#s9).

## 1. Escopo e princípios da avaliação de desempenho

- **Objeto da avaliação:** A avaliação concentra-se nos três fluxos centrais da jornada do estudante: [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) (navegação em cursos), [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) (videoaulas) e [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) (exercícios). O fluxo secundário `FL4` (progresso) é avaliado exclusivamente sob adaptabilidade (`M6`/`M7`), não integrando a bateria de desempenho, conforme delimitado no escopo da Fase 1 [S5](#s5). A avaliação é externa e caixa-preta, sem acesso ao código-fonte, banco de dados ou infraestrutura de servidores da Khan Academy.
- **Ambiente de referência exclusivo (`A1`):** Conforme definido na seção 2.3 do [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md#ambientes), todas as medições de desempenho são realizadas no **ambiente `A1`** (Windows 11 Pro virtualizado com Docker/Winboat, navegador Google Chrome, motor Blink, alocação estrita de 4 GB de memória RAM e 4 vCPUs). Essa restrição isola o comportamento da plataforma em um ambiente padronizado que simula os computadores de escolas públicas.
- **Condições de conectividade de rede:** Cada fluxo é testado sob duas condições experimentais:
  1. *Conexão normal:* conexão do laboratório sem limitações artificiais;
  2. *Conexão limitada:* perfil controlado e emulado via *Network Throttling* do Google Chrome DevTools (1.500 kbps de download, 750 kbps de upload e 150 ms de RTT adicional), representando conexões modestas ou compartilhadas de escolas públicas.
- **Aquecimento e repetições válidas:** Para cada tarefa e condição de rede, realiza-se **uma execução prévia de aquecimento (*warm-up*)**, cujo resultado é descartado da análise estatística, seguida de **cinco repetições válidas consecutivas**. As repetições reduzem o impacto de flutuações pontuais de rede ou serviço e garantem significância às medidas de tendência central.
- **Exclusão do tempo pedagógico:** A medição temporal restringe-se ao tempo observável de carregamento e resposta da interface (`t_fim − t_início`). O tempo gasto pelo estudante ou avaliador na leitura do enunciado, reflexão, resolução matemática de exercícios ou na assistência contínua do vídeo pedagógico é rigorosamente excluído das medições de M1.
- **Instrumentação e auditoria complementar:** Além dos painéis nativos do DevTools (Network, Console e Performance) e do monitor de recursos do sistema/navegador, a ferramenta **Lighthouse** é utilizada como instrumento de auditoria complementar em condições de laboratório para avaliar os indicadores de carregamento das páginas de entrada dos fluxos.

### 1.1 Justificativa das decisões metodológicas

A Tabela 1 sintetiza as decisões metodológicas adotadas para a avaliação de desempenho e as justificativas técnicas correspondentes.

| Decisão metodológica | Justificativa técnica | Origem |
|---|---|---|
| Medição concentrada no ambiente `A1` | Evita confundir variações de desempenho do produto com diferenças entre sistemas operacionais ou sobrecargas de diferentes hipervisores; `A1` é a combinação mais representativa do cenário de referência | [Escopo, seção 2.3](../fase-1/escopo-da-avaliacao.md#ambientes); [Q1–Q4](../fase-2/questoes-hipoteses.md#3-g1-eficiencia-de-desempenho) |
| Duas condições de rede (Normal e Limitada) | O cenário de escola pública convive com banda compartilhada e instabilidade; comparar as duas condições evidencia a sensibilidade da interface ao tráfego de dados e latência | [Requisitos R1 e R2](../fase-1/requisitos-de-avaliacao.md#rastreabilidade); [Escopo, seção 2.3](../fase-1/escopo-da-avaliacao.md#ambientes) |
| Execução de aquecimento (*warm-up*) não contabilizada | Estabiliza resoluções de DNS, conexões TLS e mecanismos de cache prévio, eliminando anomalias associadas ao primeiro contato na sessão | [Escopo, profundidade](../fase-1/escopo-da-avaliacao.md#profundidade); boas práticas de engenharia de desempenho |
| Cinco repetições válidas por condição | Minimiza o efeito de ruídos transitórios da infraestrutura de produção e fornece uma amostra confiável para apuração da mediana e do percentil 90 (P90) | [Escopo, profundidade](../fase-1/escopo-da-avaliacao.md#profundidade); [Ficha de M1](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) |
| Adoção da mediana e P90 para M1 | A mediana é imune a *outliers* causados por engasgos momentâneos da internet pública; o P90 retrata a cauda longa de espera vivenciada pelos usuários mais penalizados | [Ficha de M1](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa); [Critérios, seção 3](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) |
| Exclusão do tempo pedagógico de vídeo e exercício | A eficiência de desempenho avalia a capacidade de resposta do software, e não o ritmo de aprendizagem ou a duração didática dos materiais educacionais | [Questão Q1](../fase-2/questoes-hipoteses.md#31-q1-comportamento-temporal); [Ficha de M1](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) |
| Controle de cache (*Disable cache*) para M5 | Permite mensurar com precisão o volume bruto de dados requerido pelo fluxo sem mascarar o consumo por transferências pré-existentes na sessão | [Ficha de M5](../fase-2/metricas.md#15-m5-dados-transferidos); [Critérios, seção 3](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) |
| Uso complementar do Lighthouse | Fornece métricas padronizadas da indústria (FCP, LCP, TBT) em ambiente sintético de laboratório, fortalecendo a repetibilidade e o diagnóstico de gargalos | Critério `F3-C1` [S5](#s5); auditoria de qualidade web |

*Tabela 1. Decisões metodológicas da avaliação de desempenho e justificativas. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 2. Rastreabilidade com as Fases 1 e 2

A Tabela 2 apresenta a cadeia de rastreabilidade completa, conectando os requisitos da Fase 1, os objetivos, questões, hipóteses e métricas da Fase 2, os critérios de julgamento e os procedimentos e formulários de registro desta fase.

| Requisito (Fase 1) | Objetivo | Questão | Hipótese | Métrica | Critério de julgamento (Fase 2) | Procedimento | Registro |
|---|---|---|---|---|---|---|---|
| [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) / [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante) | [`G1`](../fase-2/objetivos.md#g1) | [`Q1`](../fase-2/questoes-hipoteses.md#31-q1-comportamento-temporal) — Espera nas etapas dos fluxos | H1 | [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa) — Tempo observável por etapa | Mediana ≤ 1 s (Exc.), 1–3 s (Alvo), 3–10 s (Mín.), > 10 s (Inaceitável) | [Seção 4.1](#41-procedimento-de-m1-tempo-observavel-por-etapa) e [Seção 5](#5-roteiros-passo-a-passo-com-marcos-temporais) | [Registro M1](registro-desempenho.md#registro-m1) |
| [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) / [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante) | [`G1`](../fase-2/objetivos.md#g1) | [`Q1`](../fase-2/questoes-hipoteses.md#31-q1-comportamento-temporal) — Conclusão sem bloqueios | H1 | [`M2`](../fase-2/metricas.md#12-m2-taxa-de-conclusao-dos-fluxos) — Taxa de conclusão das tentativas | 100% (Exc.), 90–100% (Alvo), 75–90% (Mín.), < 75% (Inaceitável) | [Seção 4.2](#42-procedimento-de-m2-taxa-de-conclusao-das-tentativas) | [Registro M2](registro-desempenho.md#registro-m2) |
| [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) / [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante) | [`G1`](../fase-2/objetivos.md#g1) | [`Q2`](../fase-2/questoes-hipoteses.md#32-q2-utilizacao-de-cpu) — Processamento disponível | H2 | [`M3`](../fase-2/metricas.md#13-m3-utilizacao-de-cpu) — Utilização de CPU | Média ≤ 25% (Exc.), 25–50% (Alvo), 50–75% (Mín.), > 75% (Inaceitável) | [Seção 4.3](#43-procedimento-de-m3-utilizacao-de-cpu) | [Registro M3](registro-desempenho.md#registro-m3) |
| [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) / [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante) | [`G1`](../fase-2/objetivos.md#g1) | [`Q3`](../fase-2/questoes-hipoteses.md#33-q3-utilizacao-de-memoria) — Memória disponível | H3 | [`M4`](../fase-2/metricas.md#14-m4-pico-de-memoria) — Pico de memória | Pico ≤ 512 MiB (Exc.), 512–1024 MiB (Alvo), 1024–2048 MiB (Mín.), > 2048 MiB (Inaceitável) | [Seção 4.4](#44-procedimento-de-m4-pico-de-memoria) | [Registro M4](registro-desempenho.md#registro-m4) |
| [`R2`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) / [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante) | [`G1`](../fase-2/objetivos.md#g1) | [`Q4`](../fase-2/questoes-hipoteses.md#34-q4-consumo-de-dados-de-rede) — Orçamento de acesso | H4 | [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos) — Dados transferidos | Tráfego ≤ 5 MiB (Exc.), 5–10 MiB (Alvo), 10–20 MiB (Mín.), > 20 MiB (Inaceitável) | [Seção 4.5](#45-procedimento-de-m5-dados-transferidos) | [Registro M5](registro-desempenho.md#registro-m5) |

*Tabela 2. Cadeia de rastreabilidade R1/R2 → G1 → Q1–Q4 → H1–H4 → M1–M5 → Procedimentos. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

A Tabela 3 detalha a operacionalização das diretrizes herdadas das fases anteriores em parâmetros executáveis.

| Origem | Diretriz herdada | Parâmetro operacional na Fase 3 |
|---|---|---|
| [Escopo, Tabela 2 e seção 2.3](../fase-1/escopo-da-avaliacao.md#ambientes) | Medições de desempenho exclusivamente no ambiente de referência `A1` | Execuções realizadas estritamente em Windows 11 Pro com Chrome Blink ([Seção 3.1](#31-ambiente-de-referencia-a1)) |
| [Escopo, Tabela 3](../fase-1/escopo-da-avaliacao.md#profundidade) | 1 execução de aquecimento e 5 repetições válidas por tarefa e condição de rede | Bateria de 1 aquecimento + 5 repetições para Rede Normal e 1 aquecimento + 5 repetições para Rede Limitada ([Seção 6](#6-protocolo-experimental-aquecimento-e-repeticoes)) |
| [Escopo, Tabela 3](../fase-1/escopo-da-avaliacao.md#profundidade) | Marcações de início e fim, exportações de rede e planilha de resultados brutos | Protocolo instrumental de marcas temporais e formulários em Markdown ([Seção 5](#5-roteiros-passo-a-passo-com-marcos-temporais) e [8](#8-formularios-e-modelos-de-registro)) |
| [Escopo, Tabela 5](../fase-1/escopo-da-avaliacao.md#limites-de-validade) | Resultados não generalizáveis para toda a internet; variações externas registradas | Critérios de descarte de execução inválida por causa externa e gravação de logs ([Seção 7](#7-validade-sucesso-falha-e-interrupcao)) |
| [Fichas M1 a M5](../fase-2/metricas.md#1-metricas-detalhadas) | Mediana/P90 (M1), % de conclusão (M2), CPU média e picos (M3), pico de RAM (M4) e tráfego total (M5) | Fórmulas, instrumentos de extração e critérios de cálculo consolidados ([Seção 4](#4-procedimentos-especificos-por-metrica) e [Seção 9](#9-calculo-interpretacao-e-julgamento)) |
| [Critérios, Tabela 3](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) | Limiares: 1/3/10 s (M1), 25/50/75% (M3), 512/1024/2048 MiB (M4), 5/10/20 MiB (M5) | Tabelas formais de pontuação e matrizes de conversão em notas de 0 a 3 ([Seção 9.2](#92-conversao-em-notas-e-tabelas-de-julgamento)) |
| [Questões e hipóteses H1–H4](../fase-2/questoes-hipoteses.md#3-g1-eficiencia-de-desempenho) | Metas de H1 (mediana ≤ 3 s, conclusão ≥ 90%), H2 (CPU média ≤ 50%), H3 (RAM pico ≤ 1024 MiB), H4 (tráfego ≤ 10 MiB) | Regras explícitas de sustentação ou refutação das hipóteses ([Seção 9.3](#93-julgamento-das-questoes-q1-a-q4-e-hipoteses-h1-a-h4)) |

*Tabela 3. Diretrizes das Fases 1 e 2 operacionalizadas nos procedimentos de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 3. Ambiente de teste, instrumentos e preparação

### 3.1 Ambiente de referência (`A1`)

Em conformidade com a Tabela 1 do [Ambiente de testes](ambiente-de-testes.md) [S10](#s10), o ambiente `A1` possui a seguinte especificação:
- **Sistema Operacional:** Windows 11 Pro 64-bit;
- **Navegador:** Google Chrome, versão estável 157.0 (motor Blink);
- **Modalidade de Execução:** Virtualizado sob Docker gerenciado pela interface Winboat;
- **Recursos Alocados:** 4 GB de memória RAM dedicada e 4 vCPUs;
- **Resolução de Tela e Janela:** `J2` = 1920 × 1080 pixels, janela maximizada, nível de zoom fixo em 100%.

### 3.2 Perfis de conectividade de rede

As medições são conduzidas alternando entre dois perfis controlados de conectividade:

| Perfil de rede | Mecanismo de aplicação | Taxa de download | Taxa de upload | Latência adicional (RTT) | Justificativa |
|---|---|:---:|:---:|:---:|---|
| **Rede Normal** | Conexão local direta | Ilimitada (banda nominal do host) | Ilimitada (banda nominal do host) | < 15 ms | Linha de base de desempenho sob condições ideais de laboratório |
| **Rede Limitada** | DevTools *Network Throttling* | 1.500 kbps (1,5 Mbps) | 750 kbps (0,75 Mbps) | 150 ms | Emulação do cenário escolar de banda compartilhada e acesso restrito [S9](#s9) |

*Tabela 4. Perfis de conectividade de rede para os ensaios de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 3.3 Instrumentos de medição e diagnóstico

Para assegurar precisão e repetibilidade, são utilizados os seguintes instrumentos:

1. **Google Chrome DevTools (Painel Network):**
   - Configurado com a opção *Disable cache* permanentemente marcada durante os testes;
   - Coleta de: tempo de resposta da rede, código de status HTTP de cada recurso, volume de bytes transferidos (enviados e recebidos) e dados descompactados;
   - Exportação do arquivo de tráfego de rede no formato padrão HTTP Archive (`.har`) para arquivo e auditoria de cada repetição.
2. **Google Chrome DevTools (Painel Console / Navigation Timing API):**
   - Execução de comandos padronizados em JavaScript para obtenção de marcas temporais de alta precisão via `performance.now()` e da *Navigation Timing API* (`window.performance.timing` ou `performance.getEntriesByType('navigation')`).
3. **Google Chrome Task Manager (`Shift+Esc`):**
   - Monitoramento do consumo percentual de CPU e de memória privada (*Private Memory Footprint*) do processo da aba e do processo da GPU dedicados à Khan Academy.
4. **Monitor de Recursos do Windows / Task Manager do SO:**
   - Monitoramento da carga global de CPU e de memória do sistema virtualizado para certificar que nenhum processo espúrio do Windows comprometa os testes.
5. **Lighthouse (Auditoria Complementar):**
   - Ferramenta de auditoria automatizada executada via DevTools nas páginas de entrada dos fluxos, gerando relatórios com os indicadores de laboratório: *Performance Score*, *First Contentful Paint* (FCP), *Largest Contentful Paint* (LCP), *Total Blocking Time* (TBT) e *Speed Index*.
6. **Utilitário de Gravação e Captura de Tela:**
   - Gravação contínua em vídeo de cada bateria de repetições e captura de tela ao final de cada etapa concluída para composição das evidências brutas.

### 3.4 Preparação do ambiente (Checklist PD-1 a PD-10)

Antes de iniciar qualquer rodada de medições, a equipe executa as verificações da Tabela 5. Todas as verificações são registradas na tabela de preparação do [registro de execuções de desempenho](registro-desempenho.md#registro-preparacao).

| ID | Verificação de preparação | Critério de conformidade |
|---|---|---|
| `PD-1` | Atualização do SO e navegador | Sistema Windows e Chrome atualizados; data e *builds* registradas |
| `PD-2` | Congelamento de versões | Atualizações automáticas do navegador e do Windows temporariamente suspensas |
| `PD-3` | Perfil limpo de testes | Criação de perfil novo no Chrome, sem complementos, temas ou extensões |
| `PD-4` | Isolamento de processos | Fechamento de abas não relacionadas, programas concorrentes e processos em segundo plano |
| `PD-5` | Configuração de tela e zoom | Resolução confirmada em 1920 × 1080 (`J2`), zoom fixado em 100%, janela maximizada |
| `PD-6` | Autenticação padronizada | Login prévio com a conta de teste congelada `D6` |
| `PD-7` | Idioma e localidade | Plataforma Khan Academy configurada em português do Brasil (`pt-BR`) |
| `PD-8` | Aceite único de termos | Aceite de cookies e termos de uso realizado uma única vez no perfil novo |
| `PD-9` | Disponibilidade da massa de dados | Confirmação prévia de acesso à disciplina `D1`, curso `D2`, aula `D3`, vídeo `D4` e exercício `D5` |
| `PD-10` | Calibração de rede | Medição da largura de banda basal do laboratório para registro de conformidade |

*Tabela 5. Verificações de preparação do ambiente de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 3.5 Massa de dados congelada (`D1` a `D6`)

Para garantir que todas as execuções de desempenho sejam rigorosamente equivalentes, utiliza-se a massa de dados da Tabela 6, cujos valores são congelados na etapa de preparação da Fase 4.

| ID | Elemento de teste | Requisito de equivalência | Valor congelado |
|---|---|---|---|
| `D1` | Disciplina | Disciplina curricular ativa na versão brasileira da Khan Academy | *a congelar* |
| `D2` | Curso | Curso estruturado com lista completa de unidades e lições | *a congelar* |
| `D3` | Unidade e aula | Aula padronizada contendo a videoaula de teste | *a congelar* |
| `D4` | Videoaula | Vídeo padronizado com duração conhecida, legendas e transcrição disponíveis | *a congelar (URL)* |
| `D5` | Exercício | Lista de exercícios com suporte a dicas e verificação imediata | *a congelar (URL)* |
| `D6` | Conta de teste | Conta de usuário sem dados pessoais, com histórico compatível | *a congelar* |

*Tabela 6. Massa de dados para os ensaios de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 3.6 Conhecimento exigido do avaliador

Em atendimento ao critério `F3-C2` [S5](#s5), os ensaios exigem do avaliador:
1. Conhecimento básico operacional do Windows e do navegador Chrome;
2. Habilidade para abrir e operar o Chrome DevTools (`F12` ou `Ctrl+Shift+I`), alternar entre os painéis *Network*, *Console* e *Lighthouse*, ativar o *throttling* de rede e exportar arquivos `.har`;
3. Capacidade de abrir o Gerenciador de Tarefas do Chrome (`Shift+Esc`) e realizar a leitura de CPU e memória do processo renderizador;
4. Execução estrita dos passos do roteiro, abstendo-se de interações extras durante as medições de tempo.

## 4. Procedimentos específicos por métrica

### 4.1 Procedimento de M1: Tempo observável por etapa

- **Definição operacional:** O tempo observável por etapa é o intervalo transcorrido entre a ação inicial do usuário (disparo da requisição ou clique em controle interativo) e o momento em que a interface conclui a renderização visual e torna-se novamente utilizável, sem incluir a duração pedagógica da atividade.
- **Instrumentação:** 
  - Para carregamento de páginas inteiras: extração via *Navigation Timing API* no console DevTools:
    ```javascript
    // Tempo total de carregamento da navegação observável (ms):
    const nav = performance.getEntriesByType("navigation")[0];
    const tempoCarregamento = Math.round(nav.loadEventEnd - nav.startTime);
    console.log("Tempo observável de etapa (ms):", tempoCarregamento);
    ```
  - Para ações interativas em página única (SPAs) e disparos de controle (ex: abrir dica, enviar resposta, play de vídeo): acionamento manual de cronometragem no Console via `performance.now()` ou inspeção da marcação temporal de término da requisição no painel Network somada à estabilização de layout no painel Performance.
- **Cálculo da métrica:**
  - Para cada etapa e condição de rede, computa-se o tempo decorrido $\Delta t_i = t_{\text{fim}, i} - t_{\text{início}, i}$ nas cinco repetições válidas ($i = 1, \dots, 5$);
  - Apuram-se a **mediana** e o **percentil 90 (P90)** dos tempos obtidos;
  - A mediana é adotada como indicador principal para confronto com os níveis de pontuação de M1 na [Tabela 3 da Fase 2](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos).

### 4.2 Procedimento de M2: Taxa de conclusão das tentativas

- **Definição operacional:** Proporção de tentativas iniciadas que concluem com êxito todas as etapas do roteiro padronizado sem interrupções impeditivas, bloqueios da plataforma ou ocorrência de *timeouts*.
- **Fórmula de cálculo:**
  $$M2 = 100 \times \frac{C}{N}$$
  onde $C$ é o número de tentativas concluídas com sucesso e $N$ é o total de tentativas elegíveis iniciadas (incluindo tentativas que falharam ou sofreram timeout decorrente da plataforma).
- **Critério de Timeout:** Fixa-se o limiar de **30 segundos** de inatividade ou espera sem resposta da interface como critério operacional de *timeout*. Tentativas que excedam 30 s sem retorno são classificadas como Falha por Timeout (`F-TO`).
- **Universo de observação:** Para cada fluxo e condição de rede, $N$ totaliza as tentativas elegíveis executadas para a obtenção das 5 repetições válidas.

### 4.3 Procedimento de M3: Utilização de CPU

- **Definição operacional:** Percentual médio de CPU demandado pelo processo da aba e subprocessos associados à sessão da Khan Academy durante o percurso do fluxo, acompanhado pelo registro do pico instantâneo de processamento e detecção de sobrecarga.
- **Instrumentação:**
  - O avaliador mantém aberta a janela do Gerenciador de Tarefas do Chrome (`Shift+Esc`) posicionada de forma não sobreposta à área de visualização;
  - Durante o percurso do fluxo, registram-se amostras da utilização de CPU da aba a cada 2 segundos;
  - Alternativamente, registra-se uma sessão de *profiling* no painel *Performance* do DevTools, calculando-se o tempo ocupado pela *thread* principal em relação à duração total do fluxo:
    $$\text{CPU}_{\text{média}} = \frac{\text{Tempo Total de Processamento da Thread Principal}}{\text{Duração Total do Fluxo}} \times 100$$
- **Detecção de Sobrecarga:** Episódios em que o consumo de CPU atinja ou supere **75%** são anotados como evento de alta demanda de processamento.

### 4.4 Procedimento de M4: Pico de memória

- **Definição operacional:** Maior consumo de memória RAM privada (*Private Memory Footprint* / *Commit Size*) atribuído à aba e aos processos de renderização da Khan Academy durante o percurso do fluxo.
- **Instrumentação:**
  - Leitura do valor de "Espaço de memória privada" (*Memory Footprint*) no Gerenciador de Tarefas do Chrome (`Shift+Esc`);
  - O valor de pico observado durante a execução $\text{RAM}_{\text{pico}} = \max(\text{RAM}(t))$ é registrado em Megabytes (MiB);
  - Ao término de cada repetição, o consumo final é anotado e a aba é fechada para evitar que o acúmulo de *garbage collection* contamine a repetição seguinte.

### 4.5 Procedimento de M5: Dados transferidos

- **Definição operacional:** Volume total de dados digitais transmitidos pela rede (soma dos bytes recebidos e bytes enviados) para concluir integralmente o fluxo padronizado.
- **Instrumentação:**
  - O painel DevTools *Network* deve estar com a opção *Disable cache* ativada;
  - Ao iniciar a repetição, clica-se em *Clear* (limpar histórico de rede);
  - Ao concluir a última etapa do fluxo, lê-se o resumo no rodapé do painel *Network*:
    $$\text{Dados Transferidos (MiB)} = \frac{\text{bytes transferidos (Network payload)}}{1.048.576}$$
  - Registra-se também o volume descompactado dos recursos (*resources*) para fins de análise complementar;
  - O arquivo `.har` é salvo com a nomenclatura padrão da evidência.

### 4.6 Procedimento de auditoria complementar com Lighthouse

- **Finalidade:** Obter diagnósticos independentes e consolidados de laboratório para as páginas de entrada dos fluxos, gerando subsídios adicionais à análise de qualidade.
- **Passos de execução:**
  1. Abrir a URL congelada da página de entrada (`D2` para FL1, `D4` para FL2, `D5` para FL3) em uma aba privativa limpa no ambiente `A1`;
  2. Abrir o DevTools e selecionar a aba **Lighthouse**;
  3. Configurar os parâmetros:
     - *Mode:* Navigation (Padrão);
     - *Device:* Desktop;
     - *Categories:* Marcar apenas **Performance**;
  4. Executar a auditoria sob as duas condições de rede (Normal e com throttling simulado do Lighthouse);
  5. Exportar o relatório no formato JSON/HTML e registrar na tabela de auditoria complementar:
     - *Performance Score* (0 a 100);
     - *First Contentful Paint* (FCP, em s);
     - *Largest Contentful Paint* (LCP, em s);
     - *Total Blocking Time* (TBT, em ms);
     - *Speed Index* (em s).

## 5. Roteiros passo a passo com marcos temporais

Para cada um dos fluxos `FL1`, `FL2` e `FL3`, define-se uma sequência padronizada de etapas contendo os marcos operacionais de início (`t_início`) e término (`t_fim`). O avaliador segue o roteiro sem desvios.

### 5.1 Roteiro FL1 — Navegação em cursos

O fluxo `FL1` avalia o comportamento temporal e o consumo de recursos na navegação da estrutura educacional até a abertura do conteúdo da aula.

| Etapa | Ação do avaliador | Marco de início (`t_início`) | Marco de término (`t_fim`) | O que se observa em M1 |
|:---:|---|---|---|---|
| **E1.1** | Carregamento da página inicial / menu de disciplinas | Clique no botão de navegação ou acionamento da URL base | Renderização completa dos cursos e menu de disciplinas interativo | Tempo de renderização do catálogo inicial |
| **E1.2** | Seleção da disciplina `D1` e abertura do curso `D2` | Clique sobre o card/link do curso `D2` | Exibição completa da grade de unidades e lições do curso | Tempo de resposta para estruturação da grade curricular |
| **E1.3** | Seleção da unidade e abertura da aula `D3` | Clique sobre o link da aula `D3` | Apresentação completa da página de aula (saída observável de `FL1`) | Tempo de carregamento do ambiente da aula selecionada |

*Tabela 7. Roteiro passo a passo e marcos de medição para FL1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 5.2 Roteiro FL2 — Videoaulas

O fluxo `FL2` avalia o comportamento temporal e os recursos demandados pelo reprodutor de vídeo e suas ferramentas de acessibilidade.

| Etapa | Ação do avaliador | Marco de início (`t_início`) | Marco de término (`t_fim`) | O que se observa em M1 |
|:---:|---|---|---|---|
| **E2.1** | Carregamento da página da videoaula `D4` | Clique no link da videoaula `D4` | Reprodutor de vídeo renderizado com controles disponíveis | Tempo de montagem da interface do player de vídeo |
| **E2.2** | Disparo da reprodução da videoaula | Clique no botão "Play" / Iniciar reprodução | Primeiro *frame* de vídeo em movimento e áudio/tempo correndo | Tempo de *buffer* e início efetivo da reprodução (*excluída a duração do vídeo*) |
| **E2.3** | Acionamento da legenda | Clique no botão de alternar legendas (*CC*) | Exibição visual das legendas sobre o vídeo | Tempo de requisição e renderização da faixa de legenda |
| **E2.4** | Abertura da transcrição | Clique no controle de transcrição da aula | Exibição completa do painel textual da transcrição | Tempo de renderização do texto sincronizado da aula |

*Tabela 8. Roteiro passo a passo e marcos de medição para FL2. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

> [!IMPORTANT]
> **Isolamento do tempo pedagógico:** Após a verificação do início da reprodução na etapa E2.2 e a contagem de pelo menos 5 segundos de execução para constatação de fluidez, o avaliador deve **pausar o vídeo**. O tempo em que a videoaula permanece em execução pedagógica **não é contabilizado** nas métricas de tempo observável de resposta M1.

### 5.3 Roteiro FL3 — Exercícios

O fluxo `FL3` avalia a agilidade da plataforma na prestação de auxílio pedagógico (dica) e no envio e validação de respostas interativas.

| Etapa | Ação do avaliador | Marco de início (`t_início`) | Marco de término (`t_fim`) | O que se observa em M1 |
|:---:|---|---|---|---|
| **E3.1** | Carregamento da página do exercício `D5` | Clique no link do exercício `D5` | Enunciado e área de resposta renderizados e operáveis | Tempo de carregamento da interface interativa de exercícios |
| **E3.2** | Solicitação de dica pedagógica | Clique no botão "Obter dica" / "Ver passo a passo" | Apresentação visual completa do texto/imagem da dica | Tempo de resposta para recuperação e exibição da dica |
| **E3.3** | Envio de resposta preenchida | Clique no botão "Verificar" / "Enviar resposta" | Exibição visual do retorno da plataforma (correto ou tente novamente) | Tempo de validação e feedback do exercício (*excluído o tempo de cálculo do aluno*) |
| **E3.4** | Acionamento de continuidade | Clique no botão "Próxima questão" ou "Continuar" | Limpeza e apresentação do exercício seguinte (saída de `FL3`) | Tempo de transição de estado da atividade |

*Tabela 9. Roteiro passo a passo e marcos de medição para FL3. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

> [!NOTE]
> Para o cálculo de M1 na etapa E3.3, o tempo de digitação ou resolução mental do problema pelo avaliador é mantido fora da medição: o cronômetro inicia estritamente no clique de envio e cessa no feedback retornado pela interface.

## 6. Protocolo experimental (Aquecimento e repetições)

### 6.1 Execução de aquecimento (*warm-up*)

Antes das repetições oficiais válidas, é realizada **uma execução completa do fluxo (etapas E.1 a E.4) denominada aquecimento (`W`)**, tanto sob rede normal quanto sob rede limitada. 
- **Objetivo:** Estabelecer conexões de socket seguras (TLS Handshake), povoar tabelas de resolução de nomes (DNS) e amortecer efeitos de *cold start* da infraestrutura remota;
- **Tratamento dos dados:** Os tempos e recursos medidos na execução de aquecimento são anotados na linha `W` do registro com a marcação "Descartado da Análise Estatística", não entrando no cálculo da mediana, do P90 ou das médias de CPU/RAM.

### 6.2 As cinco repetições válidas consecutivas

Para cada combinação de **fluxo** e **condição de rede**, são coletadas **cinco repetições válidas consecutivas** (`R1`, `R2`, `R3`, `R4`, `R5`).
- Caso uma repetição sofra anomalia externa não atribuível à plataforma (queda de internet externa ou erro do operador), ela é rotulada como Inválida (`X`), descartada e imediatamente refeita até totalizar cinco execuções válidas;
- Se a anomalia for decorrente da Khan Academy (erro HTTP 500, página travada, script congelado), a repetição é rotulada como Falha (`F`) e computada no denominador de M2.

### 6.3 Ordem e sequência de ensaios

Para mitigar efeitos cruzados e garantir padronização, a ordem dos ensaios segue estritamente a sequência:
1. **Bateria FL1 — Rede Normal:** 1 Aquecimento (`W-FL1-NORM`) + 5 Repetições Válidas (`R1` a `R5`);
2. **Bateria FL1 — Rede Limitada:** 1 Aquecimento (`W-FL1-LIM`) + 5 Repetições Válidas (`R1` a `R5`);
3. **Bateria FL2 — Rede Normal:** 1 Aquecimento (`W-FL2-NORM`) + 5 Repetições Válidas (`R1` a `R5`);
4. **Bateria FL2 — Rede Limitada:** 1 Aquecimento (`W-FL2-LIM`) + 5 Repetições Válidas (`R1` a `R5`);
5. **Bateria FL3 — Rede Normal:** 1 Aquecimento (`W-FL3-NORM`) + 5 Repetições Válidas (`R1` a `R5`);
6. **Bateria FL3 — Rede Limitada:** 1 Aquecimento (`W-FL3-LIM`) + 5 Repetições Válidas (`R1` a `R5`).

Totalizam-se 36 execuções no ambiente `A1` (6 de aquecimento e 30 válidas).

### 6.4 Higienização entre repetições

Entre repetições sucessivas da mesma bateria:
1. O arquivo `.har` e as leituras de CPU/RAM da repetição anterior são salvos;
2. A aba do navegador em que o fluxo foi executado é **fechada**;
3. O avaliador aguarda 5 segundos para estabilização de CPU e liberação de memória pelo sistema operacional;
4. Uma nova aba é aberta no mesmo perfil, garantindo que o histórico de rede seja limpo (*Clear Network*), mantendo a opção *Disable cache* ativada.

## 7. Validade, sucesso, falha e interrupção

### 7.1 Critérios de validade de uma execução

Uma execução é considerada válida e elegível quando atende cumulativamente aos seguintes critérios:
1. Ambiente de teste `A1` operando dentro das especificações de virtualização (4 GB RAM, 4 vCPUs);
2. Perfil de rede confirmado (Normal ou Limitada com 1.500/750 kbps e 150 ms RTT);
3. Execução realizada sem aplicativos de terceiros consumindo CPU em segundo plano;
4. Massa de dados utilizada correspondente exatamente aos valores congelados `D1` a `D6`;
5. Roteiro passo a passo percorrido na íntegra, sem desvios operacionais.

Se qualquer uma dessas pré-condições for violada, a tentativa é marcada com o código `X` (Inválida) e descartada.

### 7.2 Critérios de sucesso e falha

- **Concluída (`C`):** Todas as etapas do fluxo atingiram seus respectivos marcos de término sem interrupções impeditivas, as informações e retornos foram renderizados corretamente e nenhum erro impeditivo foi registrado;
- **Falha por Bloqueio (`F-BLQ`):** Ocorreu erro técnico da plataforma (ex: tela branca, quebra de script, erro HTTP 5xx, reprodutor incapaz de iniciar o vídeo mesmo com rede operante) que impossibilitou avançar para a etapa seguinte;
- **Falha por Timeout (`F-TO`):** A plataforma permaneceu mais de 30 segundos sem fornecer retorno visual observável ou concluir o carregamento da etapa;
- **Falha por Sobrecarga (`F-SOB`):** O processo da plataforma travou o navegador ou consumiu 100% de CPU de forma contínua por mais de 15 segundos inviabilizando a interação.

### 7.3 Interrupção e cancelamento

A execução é imediatamente interrompida e classificada como Inválida (`X`) quando ocorrer:
- Queda geral de conectividade física ou falha no provedor de internet do laboratório;
- Travamento do sistema operacional hospedeiro ou do hipervisor de virtualização;
- Interrupção provocada pelo operador.

### 7.4 Protocolo de atribuição de causa

Para garantir a integridade dos dados coletados, toda anomalia observada é classificada segundo a Tabela 10.

| Atribuição | Evidência observada | Tratamento operacional |
|---|---|---|
| **Plataforma Khan Academy** | Erro de script no Console, falha em requisição de API com HTTP 500/503, congelamento reproduzível | Classificada como Falha (`F`) e computada no denominador de M2 |
| **Ambiente de Testes / Virtualização** | Falha de alocação de memória no host Docker/Winboat, erro de driver gráfico do sistema convidado | Descartada (`X`); reiniciar a máquina virtual e repetir |
| **Operador / Avaliador** | Clique em elemento incorreto, desvio de rota, atraso na cronometragem manual | Descartada (`X`); repetir a execução com atenção ao roteiro |
| **Conexão Externa da Instituição** | Perda total de conectividade com serviços externos fora do escopo da Khan Academy | Descartada (`X`); aguardar o restabelecimento da rede |

*Tabela 10. Protocolo de atribuição de causa das divergências. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 8. Formulários e modelos de registro

Todos os dados brutos e consolidados da avaliação de desempenho são registrados no documento [Registro de execuções de eficiência de desempenho (M1 a M5)](registro-desempenho.md) [S12](#s12). 

A Tabela 11 apresenta a organização das seções de registro.

| Seção do registro | Descrição e conteúdo | Responsável pelo preenchimento |
|---|---|---|
| [1. Preparação de A1](registro-desempenho.md#registro-preparacao) | Dados de hardware, versões congeladas e checklist `PD-1` a `PD-10` | Avaliador / Executor |
| [2. Dados congelados](registro-desempenho.md#registro-dados) | Valores e URLs fixadas de `D1` a `D6` | Avaliador / Executor |
| [3. Condições de rede](registro-desempenho.md#registro-rede) | Registro de calibração da rede Normal e parâmetros do Throttling da rede Limitada | Avaliador / Executor |
| [4. Execuções de FL1](registro-desempenho.md#registro-fl1) | Registros brutos das etapas E1.1–E1.3, M1 a M5, aquecimento e 5 repetições (Normal e Limitada) | Avaliador e Observador |
| [5. Execuções de FL2](registro-desempenho.md#registro-fl2) | Registros brutos das etapas E2.1–E2.4, M1 a M5, aquecimento e 5 repetições (Normal e Limitada) | Avaliador e Observador |
| [6. Execuções de FL3](registro-desempenho.md#registro-fl3) | Registros brutos das etapas E3.1–E3.4, M1 a M5, aquecimento e 5 repetições (Normal e Limitada) | Avaliador e Observador |
| [7. Auditoria Lighthouse](registro-desempenho.md#registro-lighthouse) | Indicadores de laboratório (Performance Score, FCP, LCP, TBT, Speed Index) para `D2`, `D4` e `D5` | Avaliador / Observador |
| [8. Ocorrências](registro-desempenho.md#registro-ocorrencias) | Registro detalhado de qualquer falha ou anomalia (`OC-DES-001`, ...) | Avaliador / Observador |
| [9. Resumo e julgamento](registro-desempenho.md#registro-resumo) | Consolidação estatística (medianas, médias, picos, taxas de conclusão), notas de 0 a 3 e desfecho de D1 | Equipe avaliadora |

*Tabela 11. Organização das seções do registro de execuções de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

**Nomenclatura das evidências:** Os arquivos de evidência gerados durante a coleta seguem o padrão padronizado:
- Arquivo de tráfego de rede: `DES_<fluxo>_<condicao>_<repeticao>_<data>.har` (ex: `DES_FL1_NORM_R1_20261112.har`);
- Captura de tela: `DES_<fluxo>_<etapa>_<condicao>_<repeticao>_<data>.png` (ex: `DES_FL1_E1.3_NORM_R1_20261112.png`);
- Relatório Lighthouse: `LH_<fluxo>_<condicao>_<data>.json` (ex: `LH_FL2_LIM_20261112.json`).

## 9. Cálculo, interpretação e julgamento

### 9.1 Fórmulas e consolidação estatística

A Tabela 12 reúne as fórmulas aplicadas sobre as repetições válidas para consolidação dos resultados de cada métrica.

| Métrica | Indicador estatístico | Fórmula matemática | Interpretação |
|---|---|---|---|
| `M1` | Mediana do tempo observável por etapa | $\text{Mediana}(\Delta t_1, \dots, \Delta t_5)$ | Valor central que separa a metade superior da inferior dos tempos de resposta da etapa |
| `M1` (apoio) | Percentil 90 do tempo observável | $\text{P90}(\Delta t_1, \dots, \Delta t_5)$ | Tempo abaixo do qual se situam 90% das respostas observadas |
| `M2` | Taxa de conclusão das tentativas | $100 \times \frac{C}{N}$ | Percentual de tentativas iniciadas que foram concluídas sem falhas |
| `M3` | Utilização média de CPU | $\text{CPU}_{\text{média}} = \frac{1}{n} \sum_{i=1}^n \text{CPU}_i$ | Carga média demandada da CPU durante o percurso da tarefa |
| `M3` (apoio) | Pico de utilização de CPU | $\max(\text{CPU}(t))$ | Maior percentual instantâneo demandado durante a execução |
| `M4` | Pico de utilização de memória | $\max(\text{RAM}(t))$ | Maior volume em MiB alocado para a aba e processo de renderização |
| `M5` | Volume de dados transferidos | $D = \frac{\text{Bytes Recebidos} + \text{Bytes Enviados}}{1.048.576}$ | Volume total de tráfego de rede gerado para concluir o fluxo |

*Tabela 12. Fórmulas de consolidação estatística das métricas de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.2 Conversão em notas e tabelas de julgamento

A conversão dos indicadores consolidados nas notas de 0 a 3 obedece rigorosamente aos [Critérios de julgamento da Fase 2](../fase-2/criterios-julgamento.md) [S9](#s9). A Tabela 13 sintetiza as faixas quantitativas aplicadas.

| Métrica | Excelente (3) | Alvo (2) | Mínimo aceitável (1) | Inaceitável (0) |
|---|---:|---:|---:|---:|
| **M1 — Tempo observável por etapa** (mediana) | $\le 1\text{ s}$ | $> 1\text{ a } 3\text{ s}$ | $> 3\text{ a } 10\text{ s}$ | $> 10\text{ s}$ |
| **M2 — Taxa de conclusão dos fluxos** | $100\%$ | $90\% \le x < 100\%$ | $75\% \le x < 90\%$ | $x < 75\%$ |
| **M3 — Utilização de CPU** (média do fluxo) | $\le 25\%$ | $> 25\text{ a } 50\%$ | $> 50\text{ a } 75\%$ | $> 75\%$ |
| **M4 — Pico de memória** | $\le 512\text{ MiB}$ | $> 512\text{ a } 1024\text{ MiB}$ | $> 1024\text{ a } 2048\text{ MiB}$ | $> 2048\text{ MiB}$ |
| **M5 — Dados transferidos** (por fluxo) | $\le 5\text{ MiB}$ | $> 5\text{ a } 10\text{ MiB}$ | $> 10\text{ a } 20\text{ MiB}$ | $> 20\text{ MiB}$ |

*Tabela 13. Níveis de pontuação das métricas de desempenho (M1 a M5). Fonte: Reproduzida de [Critérios de julgamento da Fase 2](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos)*

### 9.3 Julgamento das questões Q1 a Q4 e hipóteses H1 a H4

Conforme a seção 5 de [Critérios de julgamento](../fase-2/criterios-julgamento.md#5-regra-de-julgamento) e a seção 6 de [Questões e hipóteses](../fase-2/questoes-hipoteses.md#6-interpretacao-das-hipoteses):

1. **Questão Q1 e Hipótese H1 (Comportamento temporal):**
   - **H1:** Prevê que no ambiente `A1`, em cada etapa e condição de rede, o tempo mediano de resposta será de até 3 s e pelo menos 90% das tentativas elegíveis serão concluídas, sem bloqueio de etapa essencial.
   - **Classificação de H1:** 
     - *Sustentada na amostra:* se para todas as etapas dos fluxos `FL1` a `FL3`, em ambas as condições de rede, a mediana de M1 $\le 3\text{ s}$, M2 $\ge 90\%$ e não ocorrer bloqueio essencial atribuível à plataforma;
     - *Não sustentada:* se qualquer etapa apresentar mediana de M1 $> 3\text{ s}$, M2 $< 90\%$ ou houver bloqueio essencial;
     - *Inconclusiva:* se houver insuficiência de dados válidos.
   - **Atendimento de Q1:** Considerada atendida quando M1 e M2 alcançarem nota 2 ou 3 em todas as tarefas e nenhuma etapa essencial estiver impedida.
2. **Questão Q2 e Hipótese H2 (Utilização de CPU):**
   - **H2:** Prevê que no ambiente `A1`, a utilização média de CPU será de até 50% em cada execução válida de `FL1` a `FL3`, sem interrupção impeditiva associada a sobrecarga.
   - **Classificação de H2:** Sustentada se a média de M3 $\le 50\%$ em todas as execuções e não houver travamento por processamento; caso contrário, não sustentada.
   - **Atendimento de Q2:** Atendida quando M3 atingir nota 2 ou 3.
3. **Questão Q3 e Hipótese H3 (Utilização de memória):**
   - **H3:** Prevê que no ambiente `A1`, o pico de memória da sessão/processo monitorado será de até 1.024 MiB em cada execução válida de `FL1` a `FL3`, sem esgotamento de memória.
   - **Classificação de H3:** Sustentada se o pico individual de M4 em cada repetição for $\le 1024\text{ MiB}$; se qualquer repetição exceder 1.024 MiB, H3 é não sustentada.
   - **Atendimento de Q3:** Atendida quando M4 obtiver nota 2 ou 3.
4. **Questão Q4 e Hipótese H4 (Consumo de dados de rede):**
   - **H4:** Prevê que no ambiente `A1`, cada execução concluída do trecho padronizado de navegação e carregamento transferirá no máximo 10 MiB, com política de cache constante.
   - **Classificação de H4:** Sustentada se M5 $\le 10\text{ MiB}$ em cada fluxo concluído; caso contrário, não sustentada.
   - **Atendimento de Q4:** Atendida quando M5 obtiver nota 2 ou 3.

### 9.4 Julgamento do objetivo G1 (Eficiência de desempenho)

O objetivo **G1 — Eficiência de Desempenho** é considerado **atendido** se e somente se **todas as quatro questões (`Q1`, `Q2`, `Q3` e `Q4`) forem atendidas** (nota 2 ou 3 em seus indicadores principais e nenhuma tarefa essencial impedida). Caso qualquer questão receba nota 0 ou 1, G1 é considerado não atendido ou atendido apenas no nível mínimo aceitável.

### 9.5 Consistência metodológica com as Fases 1 e 2

A Tabela 14 demonstra a estrita consistência entre as especificações conceituais e os métodos executáveis estabelecidos neste artefato, atendendo ao critério `F3-C8` [S5](#s5).

| Elemento da Fase 1 ou 2 | Especificação de origem | Operacionalização na Fase 3 | Avaliação de consistência |
|---|---|---|---|
| **Escopo de fluxos** | `FL1`, `FL2` e `FL3` como centrais de desempenho | Exclusão de `FL4` dos procedimentos de M1–M5 | Consistência total com o Escopo da Fase 1 [S5](#s5) |
| **Ambiente de ensaio** | Ambiente de referência `A1` em computador com 4 GB RAM | Virtualização Winboat/Docker com perfil fixo de 4 GB RAM e 4 vCPUs | Consistência total com os Requisitos [S4](#s4) e Ambiente [S10](#s10) |
| **Massa de testes** | 1 aquecimento + 5 repetições por tarefa e rede | Bateria de 1 aquecimento descartado e 5 repetições válidas em rede Normal e Limitada | Atendimento rigoroso ao cronograma amostral |
| **Fichas M1 a M5** | Definições, fórmulas, fontes e unidades da Fase 2 | Instrumentação direta no DevTools e Task Manager com as mesmas fórmulas | Coerência matemática e operacional idêntica |
| **Critérios e limiares** | Faixas de 1/3/10 s, 25/50/75%, 512/1024/2048 MiB, 5/10/20 MiB | Adoção direta dos limiares da Tabela 3 da Fase 2 para pontuação de 0 a 3 | Rastreabilidade total sem divergência de faixas |
| **Regras de hipóteses** | Estados: Sustentada, Não sustentada, Inconclusiva | Aplicação explícita dos estados de interpretação da seção 6 da Fase 2 | Conformidade integral |

*Tabela 14. Matriz de consistência metodológica entre as Fases 1, 2 e 3. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.6 Da medição à decisão D1 e ações para o requisitante

Em alinhamento ao propósito prático da avaliação [S4](#s4), a Tabela 15 mapeia como os resultados obtidos nas medições de desempenho se convertem em desfechos da decisão `D1` e orientam ações para a coordenação escolar.

| Resultado consolidado de G1 | Desfecho para a Decisão `D1` | Ação prática recomendada à coordenação escolar |
|---|---|---|
| **Q1 a Q4 atendidas plenamente** (Notas 2 ou 3 em rede Normal e Limitada) | **Recomendar sem ressalvas de desempenho** | Adotar a plataforma no laboratório e autorizar o uso pedagógico inclusive em horários de pico de rede |
| **Q1 a Q4 atendidas em rede Normal, mas com limitações (Nota 1) em rede Limitada** | **Recomendar com ressalvas de conectividade** | Adotar a plataforma, mas instruir os professores a não rodar videoaulas simultâneas em turmas grandes ou escalonar o uso |
| **Falha em Q1 (M1 > 10 s ou falhas recorrentes em rede limitada)** | **Recomendar com restrições severas** | Restringir o uso aos exercícios (`FL3`), desaconselhando o uso de videoaulas (`FL2`) na infraestrutura da escola |
| **Falha em Q2 ou Q3 (Esgotamento de CPU ou memória > 2048 MiB)** | **Não recomendar nos computadores atuais** | Suspender a adoção da plataforma web até que a escola realize *upgrade* de hardware ou adote outro método |
| **Dados inconclusivos ou ensaios incompletos** | **Inconclusivo** | Não tomar decisão de adoção antes de concluir as baterias de teste |

*Tabela 15. Conversão dos resultados de desempenho em desfechos de D1 e ações escolares. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 10. Rastreabilidade com a issue #25 e critérios QSW

A Tabela 16 relaciona as tarefas e critérios de aceite de desempenho da issue #25 [S11](#s11) ao atendimento neste artefato.

| Item da Tarefa 1 da issue #25 | Atendimento neste artefato |
|---|---|
| Definir procedimentos para avaliação dos fluxos FL1, FL2 e FL3 | [Seção 1](#1-escopo-e-principios-da-avaliacao-de-desempenho) e [Seção 5](#5-roteiros-passo-a-passo-com-marcos-temporais) |
| Especificar métodos e instrumentos para M1 (Tempo observável) | [Seção 4.1](#41-procedimento-de-m1-tempo-observavel-por-etapa) e [Seção 5](#5-roteiros-passo-a-passo-com-marcos-temporais) |
| Especificar métodos e instrumentos para M2 (Taxa de conclusão) | [Seção 4.2](#42-procedimento-de-m2-taxa-de-conclusao-das-tentativas) |
| Especificar métodos e instrumentos para M3 (Utilização de CPU) | [Seção 4.3](#43-procedimento-de-m3-utilizacao-de-cpu) |
| Especificar métodos e instrumentos para M4 (Utilização de memória) | [Seção 4.4](#44-procedimento-de-m4-pico-de-memoria) |
| Especificar métodos e instrumentos para M5 (Dados transferidos) | [Seção 4.5](#45-procedimento-de-m5-dados-transferidos) |
| Descrever instruções de execução (preparação, início, término, registro) | [Seção 3.4](#34-preparacao-do-ambiente-checklist-pd-1-a-pd-10), [Seção 5](#5-roteiros-passo-a-passo-com-marcos-temporais) e [Seção 6](#6-protocolo-experimental-aquecimento-e-repeticoes) |
| Definir procedimentos para DevTools, Lighthouse e monitores de recursos | [Seção 3.3](#33-instrumentos-de-medicao-e-diagnostico) e [Seção 4.6](#46-procedimento-de-auditoria-complementar-com-lighthouse) |
| Documentar condições de rede normal e limitada | [Seção 3.2](#32-perfis-de-conectividade-de-rede) (Tabela 4) |
| Especificar execução de aquecimento e 5 repetições válidas | [Seção 6.1](#61-execucao-de-aquecimento-warm-up) e [Seção 6.2](#62-as-cinco-repeticoes-validas-consecutivas) |
| Definir critérios de validade, sucesso, falha e interrupção | [Seção 7](#7-validade-sucesso-falha-e-interrupcao) |
| Roteiros passo a passo por grupo de testes | [Seção 5](#5-roteiros-passo-a-passo-com-marcos-temporais) (Tabelas 7, 8 e 9) |
| Formulários e modelos de registro | [Seção 8](#8-formularios-e-modelos-de-registro) e artefato [registro-desempenho.md](registro-desempenho.md) |
| Rastreabilidade com Q1–Q4, H1–H4 e M1–M5 | [Seção 2](#2-rastreabilidade-com-as-fases-1-e-2) (Tabelas 2 e 3) e [Seção 9.3](#93-julgamento-das-questoes-q1-a-q4-e-hipoteses-h1-a-h4) |
| Cálculo e interpretação conforme critérios de julgamento | [Seção 9.1](#91-formulas-e-consolidacao-estatistica) e [Seção 9.2](#92-conversao-em-notas-e-tabelas-de-julgamento) |
| Consistência com o escopo da Fase 1 | [Seção 1](#1-escopo-e-principios-da-avaliacao-de-desempenho) e [Seção 9.5](#95-consistencia-metodologica-com-as-fases-1-e-2) |

*Tabela 16. Rastreabilidade com os itens da Tarefa 1 da issue #25. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

A Tabela 17 detalha como os critérios de avaliação formal QSW da Fase 3 [S5](#s5) e da Fase 4 [S13](#s13) são contemplados.

| Critério QSW | Contribuição deste artefato | Seção correspondente |
|---|---|---|
| `F3-C1` Método e repetibilidade | Instruções passo a passo precisas, marcos de temporização objetivos, regras inequívocas de sucesso e descarte | [Seções 4](#4-procedimentos-especificos-por-metrica), [5](#5-roteiros-passo-a-passo-com-marcos-temporais), [6](#6-protocolo-experimental-aquecimento-e-repeticoes) e [7](#7-validade-sucesso-falha-e-interrupcao) |
| `F3-C2` Recursos e ambiente | Especificação minuciosa do ambiente virtualizado `A1`, perfis de rede calibrados, instrumentos detalhados e massa de dados | [Seção 3](#3-ambiente-de-teste-instrumentos-e-preparacao) e [Ambiente de testes](ambiente-de-testes.md) |
| `F3-C3` Cronograma | Cronograma de trabalho realista integrado à Fase 4 e à Entrega 2 | [Seção 12](#12-cronograma-de-execucao) |
| `F3-C7` GitPage da equipe | Integração navegável na GitPage, hiperlinks estruturados com Fases 1, 2 e 3, ausência de ícones informais | Estrutura geral do documento |
| `F3-C8` Consistência Fases 2 e 3 | Matriz de consistência demonstrando perfeita aderência às métricas, questões e limiares da Fase 2 | [Seção 9.5](#95-consistencia-metodologica-com-as-fases-1-e-2) (Tabela 14) |
| `F4-C1` Obtenção das medidas | Procedimentos padronizados para execução fiel por qualquer avaliador na Fase 4 | [Seção 4](#4-procedimentos-especificos-por-metrica) e [Seção 5](#5-roteiros-passo-a-passo-com-marcos-temporais) |
| `F4-C2` Registro e dados brutos | Modelos de planilhas em Markdown indexadas por repetição com vínculos de evidências (`.har`, capturas) | [Registro de desempenho](registro-desempenho.md) |
| `F4-C3` Análise estatística e GQM | Fórmulas explícitas de mediana, P90, média, pico e regras de julgamento de H1 a H4 | [Seção 9](#9-calculo-interpretacao-e-julgamento) |

*Tabela 17. Contribuição deste artefato aos critérios de avaliação QSW. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 11. Pontos pendentes e decisões da equipe

A Tabela 18 consolida os pontos operacionais identificados que devem ser ratificados pela equipe avaliadora antes do início da coleta oficial na Fase 4.

| ID | Ponto em aberto | Impacto na medição | Proposta de encaminhamento |
|---|---|---|---|
| `PD-P1` | Definição exata das URLs da massa congelada `D1` a `D5` | Equivalência dos testes de FL1, FL2 e FL3 | Congelar as URLs na sessão de preparação conjunta em 09/11 |
| `PD-P2` | Armazenamento dos arquivos `.har` e vídeos brutos | Volume de armazenamento e auditoria da Fase 4 | Criar diretório dedicado no repositório ou pasta em nuvem compartilhada e indexar nas tabelas |
| `PD-P3` | Política de buffer de vídeo em FL2 (YouTube player) | Variação de dados transferidos em M5 | Pausar rigorosamente aos 5 segundos de execução para impedir download em segundo plano do restante do vídeo |
| `PD-P4` | Validação do perfil de limitação emulada | Fidelidade ao cenário escolar | Executar teste piloto com o Throttling do DevTools e validar taxas no painel Network |

*Tabela 18. Pontos pendentes de desempenho e decisões da equipe. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## 12. Cronograma de execução

A Tabela 19 detalha a distribuição das atividades de eficiência de desempenho integradas ao cronograma geral da Fase 4.

| Data prevista | Atividade de avaliação | Entregável / Produto | Responsáveis |
|---|---|---|---|
| 09/11/2026 | Resolução dos pontos pendentes (`PD-P1` a `PD-P4`) e congelamento da massa `D1`–`D6` | Tabela de dados congelados preenchida | Toda a equipe |
| 10/11/2026 | Ensaio piloto não oficial no ambiente `A1` para calibração das ferramentas e roteiros | Roteiros validados e ajustes operacionais finalizados | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) |
| 11/11/2026 | Execução oficial das baterias de `FL1` e `FL2` sob Rede Normal (aquecimento + 5 repetições) | Registros brutos, arquivos `.har` e capturas | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) |
| 12/11/2026 | Execução oficial das baterias de `FL3` sob Rede Normal e `FL1` sob Rede Limitada | Registros brutos, arquivos `.har` e capturas | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) |
| 13/11/2026 | Execução oficial das baterias de `FL2` e `FL3` sob Rede Limitada e auditoria complementar Lighthouse | Registros brutos e relatórios Lighthouse exportados | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) |
| 14/11/2026 | Repetição de ensaios com anomalias externas (se houver) e consolidação da planilha bruta | Planilha de dados brutos consolidada | Toda a equipe |
| 15/11/2026 | Consolidação estatística: cálculo das medianas, P90, médias de CPU, picos de RAM e tráfego M5 | Resumo estatístico e notas de 0 a 3 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) |
| 16/11/2026 | Confronto com H1–H4, julgamento de Q1–Q4 e G1 e redação dos desfechos para D1 | Texto analítico para o artigo científico da disciplina | Toda a equipe |
| 17/11/2026 | Revisão por pares, cruzamento de dados com a adaptabilidade e fechamento dos relatórios | Documentos finalizados | Toda a equipe |
| 18/11/2026 | **Entrega 2 da disciplina** | Artigo e GitPage completos | Toda a equipe |

*Tabela 19. Cronograma de execução da avaliação de desempenho na Fase 4. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## Referências

<a id="s1"></a>

> [S1] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.

<a id="s2"></a>

> [S2] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality. Genebra: ISO, 2016.

<a id="s3"></a>

> [S3] BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. In: **Encyclopedia of Software Engineering**. John Wiley & Sons, 1994. p. 528–532.

<a id="s4"></a>

> [S4] Requisitos de avaliação — Fase 1. Requisitos R1–R5 e decisões D1–D4. Disponível em: [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md).

<a id="s5"></a>

> [S5] Escopo da avaliação — Fase 1. Fluxos, ambientes, profundidade e limites de validade. Disponível em: [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md).

<a id="s6"></a>

> [S6] Objetivos de medição — Fase 2. Objetivo G1. Disponível em: [Objetivos de medição](../fase-2/objetivos.md#g1).

<a id="s7"></a>

> [S7] Questões e hipóteses — Fase 2. Questões Q1–Q4 e Hipóteses H1–H4. Disponível em: [Questões e hipóteses](../fase-2/questoes-hipoteses.md#3-g1-eficiencia-de-desempenho).

<a id="s8"></a>

> [S8] Métricas — Fase 2. Fichas de M1 a M5. Disponível em: [Métricas](../fase-2/metricas.md#1-metricas-detalhadas).

<a id="s9"></a>

> [S9] Níveis de pontuação e critérios de julgamento — Fase 2. Disponível em: [Critérios de julgamento](../fase-2/criterios-julgamento.md).

<a id="s10"></a>

> [S10] Ambiente de testes e ferramentas de avaliação — Fase 3. Disponível em: [Ambiente de testes](ambiente-de-testes.md).

<a id="s11"></a>

> [S11] FCTE-QUALIDADE-DE-SOFTWARE-1. **[Fase 3] Definição dos procedimentos de avaliação de desempenho e adaptabilidade**. Issue #25. Disponível em: <https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/issues/25>.

<a id="s12"></a>

> [S12] Registro de execuções de eficiência de desempenho (M1 a M5) — Fase 3. Disponível em: [Registro de desempenho](registro-desempenho.md).

<a id="s13"></a>

> [S13] Critérios de avaliação QSW — Fase 4. Disponível em: [Critérios da Fase 4](../criterios/fase4.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 08/11/2026 | Elaboração inicial dos procedimentos de eficiência de desempenho (M1 a M5), abrangendo os fluxos FL1 a FL3, métodos, instrumentos, perfis de rede, roteiros, critérios de validade e rastreabilidade total com as Fases 1 e 2. | [José Augusto](https://github.com/JAugustoM) | [Pedro Lucas](https://github.com/Pwdrinho) |
