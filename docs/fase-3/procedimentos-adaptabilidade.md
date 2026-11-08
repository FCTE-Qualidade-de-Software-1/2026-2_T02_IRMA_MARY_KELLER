# Procedimentos de avaliação de adaptabilidade (M6 e M7)

**Versão 1.0**

Este artefato define como será avaliada a **adaptabilidade** da versão web da Khan Academy em computadores, a característica de **portabilidade** priorizada na [Fase 1](../fase-1/index.md). Ele especifica os procedimentos de obtenção das métricas [`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) (execução por ambiente) e [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) (adaptação ao tamanho da janela), que respondem às questões [`Q5`](../fase-2/questoes-hipoteses.md#41-q5-adaptacao-entre-sistemas-operacionais-e-navegadores) e [`Q6`](../fase-2/questoes-hipoteses.md#42-q6-adaptacao-a-tamanhos-de-janela) do objetivo [`G2`](../fase-2/objetivos.md#g2).

O documento atende à parte de adaptabilidade da issue #25 (*[Fase 3] Definição dos procedimentos de avaliação de desempenho e adaptabilidade*) e usa o [ambiente de testes](ambiente-de-testes.md) da Fase 3. Os procedimentos de desempenho (M1–M5) são tratados em artefato próprio, mas compartilham com este as condições de preparação da [seção 3](#3-ambiente-de-teste-e-instrumentos).

**Situação:** especificação de procedimentos, **sem resultados coletados**. A execução oficial e a análise das medições pertencem à Fase 4. Os limiares e as regras de julgamento são os de [Critérios de julgamento](../fase-2/criterios-julgamento.md), que devem ser aprovados pela equipe antes da coleta; as regras operacionais propostas aqui e ainda não ratificadas estão reunidas na [seção 11](#11-pontos-pendentes-e-decisoes-da-equipe).

## 1. Escopo e princípios

- **Objeto:** fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) a [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos) da plataforma web, sem alterar o produto e sem acesso interno (avaliação externa, caixa-preta).
- **Ambientes:** combinações [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) a [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) da matriz direcionada da Fase 1. Os demais sistemas do ambiente de testes são tratados como complementares ([seção 3.2](#32-ambientes-complementares)).
- **Dimensões:** duas resoluções de referência, `J1` = 1366 × 768 e `J2` = 1920 × 1080, com zoom de 100%. Zoom de 200% e alto contraste pertencem a G3 ([`M10`](../fase-2/metricas.md#110-m10-preservacao-com-ampliacao) e [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste)) e **não** entram aqui.
- **Rede:** conexão sem limitação artificial. Os perfis de rede normal e limitada aplicam-se apenas a M1–M5 em `A1`.
- **Reprodutibilidade:** um segundo avaliador deve conseguir repetir cada execução apenas com este documento, os dados de teste congelados e o [registro de execuções](registro-adaptabilidade.md), descrito na [seção 8](#8-formularios-e-modelos-de-registro).

### 1.1 Justificativa do método

| Decisão metodológica | Justificativa | Origem |
|---|---|---|
| Execução funcional dirigida, uma combinação por vez | Adaptabilidade pergunta se o fluxo se conclui em outro ambiente, não qual é a distribuição de tempos; por isso o roteiro é fixo e o resultado é binário por combinação | [Escopo, profundidade](../fase-1/escopo-da-avaliacao.md#profundidade); [ficha de M6](../fase-2/metricas.md#16-m6-execucao-por-ambiente) |
| Roteiro único para M6 e M7 | Mantém o mesmo conteúdo e os mesmos pontos de verificação em todos os ambientes e dimensões, o que torna os resultados comparáveis e rastreáveis | Q5 e Q6 |
| Contagens absolutas junto ao percentual | Com 16 e 32 combinações, cada falha pesa 6,25% e 3,1%; o percentual sozinho esconderia isso | [Critérios de julgamento, seção 2](../fase-2/criterios-julgamento.md#2-metricas-percentuais) |
| Falha confirmada em 2 de 3 execuções | Reduz o peso de eventos isolados em um serviço de produção fora do controle da equipe. É escolha da equipe, não prescrição de norma | [Escopo, limites de validade](../fase-1/escopo-da-avaliacao.md#limites-de-validade) |
| Perfil novo, versões congeladas e sem extensões | Evita que estado acumulado ou atualização no meio da coleta explique diferenças entre ambientes e impede ajuste extraordinário | [Q5, verificação](../fase-2/questoes-hipoteses.md#41-q5-adaptacao-entre-sistemas-operacionais-e-navegadores) |
| Janela maximizada sob a resolução configurada | Liga a "resolução de referência" da Fase 1 à "dimensão da janela" da ficha de M7 com condição reproduzível | [Escopo, profundidade](../fase-1/escopo-da-avaliacao.md#profundidade); [ficha de M7](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) |
| Zoom fixo em 100% | Separa Q6 (janela) de Q9 (ampliação), como exige a Fase 2 | [Q6, verificação](../fase-2/questoes-hipoteses.md#42-q6-adaptacao-a-tamanhos-de-janela) |
| Gravidade `G2` conta como falha | A ficha de M7 exige conteúdo **e** controles preservados, não apenas tarefa concluída | [Ficha de M7](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) |

*Tabela 1. Decisões metodológicas e justificativas. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## 2. Rastreabilidade com as Fases 1 e 2

A Tabela 2 liga cada métrica à cadeia que a justifica e aos pontos deste documento que a operacionalizam.

| Requisito / decisão (Fase 1) | Objetivo | Questão | Hipótese | Métrica | Critério de julgamento (Fase 2) | Procedimento | Registro |
|---|---|---|---|---|---|---|---|
| [`R3`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) / [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante) | [`G2`](../fase-2/objetivos.md#g2) | [`Q5`](../fase-2/questoes-hipoteses.md#41-q5-adaptacao-entre-sistemas-operacionais-e-navegadores) — execução entre ambientes | H5 | [`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) | [Tabela 2](../fase-2/criterios-julgamento.md#2-metricas-percentuais) (maior é melhor) e [regra de julgamento](../fase-2/criterios-julgamento.md#5-regra-de-julgamento) | [Seção 4](#4-procedimento-de-m6) e roteiros da [seção 6](#6-roteiros-passo-a-passo) | [Registro de M6](registro-adaptabilidade.md#registro-m6) |
| [`R3`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) / [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante) | [`G2`](../fase-2/objetivos.md#g2) | [`Q6`](../fase-2/questoes-hipoteses.md#42-q6-adaptacao-a-tamanhos-de-janela) — conteúdo e controles nas janelas | H6 | [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) | [Tabela 2](../fase-2/criterios-julgamento.md#2-metricas-percentuais) (maior é melhor) e [regra de julgamento](../fase-2/criterios-julgamento.md#5-regra-de-julgamento) | [Seção 5](#5-procedimento-de-m7) e roteiros da [seção 6](#6-roteiros-passo-a-passo) | [Registro de M7](registro-adaptabilidade.md#registro-m7) |

*Tabela 2. Cadeia de rastreabilidade R3 → G2 → Q5/Q6 → H5/H6 → M6/M7 → procedimento. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

A Tabela 3 mostra como cada exigência da Fase 1 e da Fase 2 foi convertida em parâmetro de procedimento.

| Origem | Exigência herdada | Parâmetro neste documento |
|---|---|---|
| [Escopo, Tabela 2](../fase-1/escopo-da-avaliacao.md#ambientes) | Matriz `A1`–`A4`; sem produto cartesiano completo | Universo de 16 combinações em M6 e 32 em M7 ([4.1](#41-unidade-de-observacao-e-universo), [5.1](#51-unidade-de-observacao-e-universo)) |
| [Escopo, Tabela 3](../fase-1/escopo-da-avaliacao.md#profundidade) | Execução funcional dirigida em 1366 × 768 e 1920 × 1080, com lista de verificação, capturas e divergências reproduzíveis | Roteiros com pontos de verificação, captura obrigatória e ocorrências ([6](#6-roteiros-passo-a-passo), [8](#8-formularios-e-modelos-de-registro)) |
| [Escopo, Tabela 5](../fase-1/escopo-da-avaliacao.md#limites-de-validade) | Serviço externo pode influenciar; resultados valem só para ambientes e versões registrados | Execução inválida por causa externa, registro de versões e atribuição de causa ([7](#7-validade-atribuicao-e-interrupcao)) |
| [Ficha M6](../fase-2/metricas.md#16-m6-execucao-por-ambiente) | `100 × C/N` sobre combinações SO–navegador–fluxo; roteiros iguais; registrar sucesso, falha e evidência | [4.1](#41-unidade-de-observacao-e-universo), [4.3](#43-passos-de-execucao), [9.1](#91-formulas) |
| [Ficha M7](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) | `100 × C/N` sobre combinações ambiente–dimensão–fluxo com conteúdo e controles preservados; capturas | [5.1](#51-unidade-de-observacao-e-universo), [5.4](#54-inventario-de-controles-essenciais), [9.1](#91-formulas) |
| [Q5, verificação prevista](../fase-2/questoes-hipoteses.md#41-q5-adaptacao-entre-sistemas-operacionais-e-navegadores) | Distinguir preparação normal de ajuste extraordinário; combinações inviáveis tratadas no planejamento | [4.4](#44-preparacao-normal-e-ajuste-extraordinario) e [4.5](#45-combinacoes-inviaveis) |
| [Q6, verificação prevista](../fase-2/questoes-hipoteses.md#42-q6-adaptacao-a-tamanhos-de-janela) | Dimensão na identificação da combinação; sem dupla contagem entre Q5 e Q6 | [5.2](#52-relacao-com-m6-e-m10-sem-dupla-contagem) |
| [Critérios, seção 5](../fase-2/criterios-julgamento.md#5-regra-de-julgamento) | Questão atendida com nota 2 ou 3 e nenhuma tarefa essencial impedida; contagens absolutas | [4.7](#47-calculo-e-julgamento-de-q5-e-h5), [5.6](#56-calculo-e-julgamento-de-q6-e-h6) |

*Tabela 3. Exigências das Fases 1 e 2 convertidas em parâmetros de procedimento. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## 3. Ambiente de teste e instrumentos

### 3.1 Ambientes da matriz (A1–A4)

A Tabela 4 associa cada ambiente da Fase 1 aos dados do [ambiente de testes](ambiente-de-testes.md).

| ID | Sistema operacional | Navegador (motor) | Versão do navegador | Modalidade | Recursos | Situação |
|---|---|---|---|---|---|---|
| `A1` | Windows 11 Pro | Google Chrome (Blink) | 157.0 | Virtualizado (Docker, Winboat) | 4 GB, 4 vCPUs | Definido |
| `A2` | Windows 11 Pro | Mozilla Firefox (Gecko) | 159.1 | Virtualizado (Docker, Winboat) | 4 GB, 4 vCPUs | Definido |
| `A3` | macOS (versão a registrar) | Apple Safari (WebKit) | A registrar | Computador real | A registrar | **Pendente** (macOS e Safari sem versão) |
| `A4` | Ubuntu 26.04 | Mozilla Firefox (Gecko) | 159.0 | Virtualizado (QEMU/KVM, Gnome Boxes) | 4 GB, 4 vCPUs | Definido |

*Tabela 4. Ambientes `A1`–`A4` e dados de configuração. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [ambiente de testes](ambiente-de-testes.md)*

As versões acima estão na data do quadro do ambiente de testes e devem ser **reconfirmadas e congeladas** na preparação ([3.4](#34-preparacao-do-ambiente)).

### 3.2 Ambientes complementares

O ambiente de testes inclui três distribuições Linux além do Ubuntu. Como a Fase 1 e a hipótese H5 delimitam `A1`–`A4`, essas distribuições **não entram no denominador de M6 nem na nota de Q5**. Se a equipe decidir executá-las ([ponto P2](#11-pontos-pendentes-e-decisoes-da-equipe)), seus resultados são relatados à parte, como evidência complementar de adaptabilidade.

| ID proposto | Sistema operacional | Chrome | Firefox | Execução proposta |
|---|---|---|---|---|
| `AC1` | Fedora 44 | 156.0 | 159.0 | FL1–FL4, em `J2`, nos dois navegadores |
| `AC2` | Arch Linux (sem versão fixa) | 156.0 | 159.0 | FL1–FL4, em `J2`, nos dois navegadores |
| `AC3` | openSUSE Leap 16.1 | 156.0 | 153.5 | FL1–FL4, em `J2`, nos dois navegadores |

*Tabela 5. Ambientes complementares propostos (24 execuções). Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [ambiente de testes](ambiente-de-testes.md)*

### 3.3 Instrumentos

| Instrumento | Uso |
|---|---|
| Navegador do ambiente (console de desenvolvedor) | Registrar a resolução da tela, o viewport e o `devicePixelRatio` ([3.5](#35-resolucao-e-janela)) |
| Captura de tela nativa do sistema operacional | Evidência obrigatória do ponto final de cada roteiro e de cada ocorrência |
| [Registro de execuções](registro-adaptabilidade.md) (tabelas em Markdown) | Registro de preparação, execuções, resultados e ocorrências |
| Gravação de tela | Recomendada em todas as sessões em `J2` e obrigatória para falhas ([ponto P10](#11-pontos-pendentes-e-decisoes-da-equipe)); evidência de execução para a Fase 4 |

*Tabela 6. Instrumentos de coleta de M6 e M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

O Lighthouse listado no ambiente de testes **não** é instrumento de M6 nem de M7. Os leitores de tela também não são usados nesta avaliação.

### 3.4 Preparação do ambiente

Cada ambiente passa pelas verificações abaixo antes da primeira execução oficial. O responsável preenche, por ambiente, as tabelas de [preparação](registro-adaptabilidade.md#registro-preparacao) do registro.

| ID | Verificação |
|---|---|
| PA-1 | Atualizar o sistema e o navegador pelo gerenciador de pacotes e **registrar a data**. Esse registro substitui o `dia X` do quadro de versões do ambiente de testes. |
| PA-2 | Registrar versão e *build* do sistema operacional e do navegador (por exemplo, `chrome://version`, `about:support`, `winver`, `lsb_release -a`, "Sobre este Mac" e "Sobre o Safari"). |
| PA-3 | **Desativar a atualização automática** do navegador até o fim da coleta, para que a versão registrada seja a executada. |
| PA-4 | Criar um **perfil novo** do navegador, sem extensões, sem bloqueadores de anúncio e sem configurações alteradas. |
| PA-5 | Definir o idioma da plataforma como português do Brasil e entrar com a conta de teste (`D6`). |
| PA-6 | Confirmar zoom do navegador em 100%, janela **maximizada** (não em tela cheia) e escala do sistema conforme [3.5](#35-resolucao-e-janela). |
| PA-7 | Confirmar conexão sem limitação artificial e fechar aplicativos concorrentes. |
| PA-8 | Em máquinas virtuais, registrar vCPUs, memória e modalidade. Em `A3`, registrar o hardware. |
| PA-9 | Aceitar avisos de consentimento e cookies **uma única vez** no perfil novo. Isso é preparação normal ([4.4](#44-preparacao-normal-e-ajuste-extraordinario)). |
| PA-10 | Confirmar que o conteúdo congelado em `D1`–`D5` continua disponível. |

*Tabela 7. Verificações de preparação do ambiente. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

**Dados de teste.** Como o conteúdo da plataforma pode mudar, a equipe fixa os itens abaixo na preparação e usa **os mesmos** em todos os ambientes e resoluções.

| ID | Dado | Critério de escolha | Valor |
|---|---|---|---|
| `D1` | Disciplina | Disponível em português do Brasil e com cursos, vídeos e exercícios | *a congelar* |
| `D2` | Curso | Com unidades e aulas listadas | *a congelar* |
| `D3` | Unidade e aula | Aula que contenha o vídeo `D4` | *a congelar* |
| `D4` | Videoaula | Com legenda e transcrição disponíveis, para que FL2 seja idêntico em todos os ambientes | *a congelar (URL)* |
| `D5` | Exercício | Com dica disponível; a resposta enviada pode ser qualquer uma, pois o teste observa o retorno da plataforma, não o acerto | *a congelar (URL)* |
| `D6` | Conta de teste | Controlada pela equipe, sem dados pessoais de menores ([escopo, seção 1.2](../fase-1/escopo-da-avaliacao.md#fluxos)); com histórico mínimo de progresso para que `FL4` exiba informação | *a congelar* |

*Tabela 8. Dados de teste a congelar antes da coleta. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

### 3.5 Resolução e janela

A Fase 1 define resoluções de referência e a ficha de M7 fala em dimensão da janela. Para unificar os dois termos, a **dimensão avaliada é a janela maximizada do navegador sob a resolução configurada no sistema**, conforme a Tabela 9.

| ID | Resolução da tela | Zoom do navegador |
|---|---|---|
| `J1` | 1366 × 768 | 100% |
| `J2` | 1920 × 1080 | 100% |

*Tabela 9. Dimensões de referência de M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [escopo](../fase-1/escopo-da-avaliacao.md#profundidade)*

Em cada execução, o avaliador roda o comando abaixo no console e anota o resultado na [tabela de resolução verificada](registro-adaptabilidade.md#registro-resolucao) do registro. A resolução é considerada configurada quando `sw` e `sh` coincidem com a dimensão nominal em pixels CSS. O `dpr` é apenas registrado, pois telas de alta densidade podem ter valor diferente de 1.

```js
JSON.stringify({sw: screen.width, sh: screen.height, iw: innerWidth, ih: innerHeight, dpr: devicePixelRatio})
```

O modo de design responsivo ou de emulação de dispositivo do navegador **não** substitui a resolução real do ambiente.

### 3.6 Requisitos, conhecimento do avaliador e massa de dados

**Recursos de hardware e software.**

| Item | Requisito | Fonte |
|---|---|---|
| Máquinas virtuais | 4 GB de memória e 4 vCPUs por ambiente; disco a registrar na preparação | [Ambiente de testes](ambiente-de-testes.md) |
| Virtualização | QEMU/KVM com Gnome Boxes (Linux) e Docker com Winboat (Windows); o host precisa de virtualização por hardware | [Ambiente de testes](ambiente-de-testes.md) |
| Navegadores | Versões das Tabelas 4 e 5, congeladas em PA-3 | [3.1](#31-ambientes-da-matriz-a1a4), [3.2](#32-ambientes-complementares) |
| Rede | Conexão sem limitação artificial; como referência, a Khan Academy sugere cerca de 1,5 Mbps por dispositivo para vídeo em definição padrão | Central de ajuda da Khan Academy [S3](#s3) |
| Acesso a serviços | Segundo a central de ajuda, os vídeos são hospedados no YouTube, que deve estar acessível na rede de teste | Central de ajuda da Khan Academy [S3](#s3) |
| Suporte declarado pelo produto | A plataforma declara suporte às versões mais recentes de Chrome, Firefox, Edge e Safari, em Windows, Mac e Chromebook | Central de ajuda da Khan Academy [S1](#s1), [S2](#s2) |

*Tabela 10. Requisitos de hardware e software da avaliação de adaptabilidade. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base em [ambiente de testes](ambiente-de-testes.md) e na central de ajuda da Khan Academy*

O suporte declarado não inclui Linux nem o Edge. Isso não altera a matriz da Fase 1 nem os critérios, mas é contexto para interpretar falhas em `A4` e nos ambientes complementares ([ponto P12](#11-pontos-pendentes-e-decisoes-da-equipe)).

**Conhecimento exigido do avaliador.**

| Aspecto | Nível exigido | Como é atendido |
|---|---|---|
| Informática | Operar o navegador e o sistema: abrir o console, capturar a tela, ajustar a resolução e consultar versões | Guia de operações da [3.7](#37-guia-de-operacoes-por-ambiente) |
| Domínio da aplicação | Nenhum além do roteiro; não é necessário conhecer o conteúdo pedagógico | Roteiros da [seção 6](#6-roteiros-passo-a-passo) e dados `D1`–`D6` |
| Preparação do avaliador | Ler este documento e participar do ensaio piloto em `A1` | [Seção 12](#12-cronograma-de-execucao) |

*Tabela 11. Conhecimento exigido do avaliador. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

**Massa de dados.** Os dados `D1`–`D6` da [Tabela 8](#34-preparacao-do-ambiente) existem para dois fins: manter o conteúdo idêntico em todas as execuções e dispensar a procura por conteúdo a cada sessão, que seria fonte de variação e de atraso. A conta `D6` deve ser preparada uma única vez, com histórico mínimo de progresso, para que `FL4` apresente informação desde a primeira execução. O volume é pequeno (um curso, uma aula, um vídeo, um exercício e uma conta) porque M6 e M7 não medem tempo nem consumo de recursos, o que dispensa grandes massas de dados.

### 3.7 Guia de operações por ambiente

O guia reduz o conhecimento prévio exigido do avaliador. Rótulos de menu podem variar entre versões e devem ser anotados quando diferirem.

| Operação | Windows (`A1`, `A2`) | macOS (`A3`) | Ubuntu (`A4`) e demais Linux |
|---|---|---|---|
| Abrir o console | Chrome: `Ctrl+Shift+J`. Firefox: `Ctrl+Shift+K` | Safari: ativar o menu Desenvolver nos ajustes avançados e usar `Cmd+Option+C` | Firefox: `Ctrl+Shift+K`. Chrome: `Ctrl+Shift+J` |
| Capturar a tela | `Win+Shift+S` | `Cmd+Shift+3`, `4` ou `5` | `PrtSc` ou ferramenta de captura do ambiente gráfico |
| Ajustar a resolução | Configurações, Sistema, Tela | Ajustes do Sistema, Telas | Configurações, Telas, no sistema convidado |
| Maximizar a janela | Botão de maximizar | Duplo clique na barra de título, pois o botão verde entra em tela cheia | Botão de maximizar |
| Versão do navegador | `chrome://version` ou `about:support` | Menu Safari, Sobre o Safari | `chrome://version` ou `about:support` |
| Versão do sistema | `winver` | Menu Apple, Sobre este Mac | `lsb_release -a` ou `/etc/os-release` |

*Tabela 12. Guia de operações por ambiente. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## 4. Procedimento de M6

<a id="m6"></a>

### 4.1 Unidade de observação e universo

A unidade de observação é a combinação **ambiente–fluxo** (`M6-<ambiente>-<fluxo>`). O universo planejado tem **16 combinações**: `A1`–`A4` × `FL1`–`FL4`. As execuções de M6 usam a resolução `J2`, que é a condição de referência.

### 4.2 Papéis

Cada execução tem um **executor**, que segue o roteiro, e um **observador**, que confere os pontos de verificação, confirma a captura e preenche o registro. Executor e observador podem ser da mesma dupla.

### 4.3 Passos de execução

1. Conferir a preparação do ambiente (PA-1 a PA-10) e abrir uma sessão limpa, sem abas extras.
2. Configurar `J2`, maximizar a janela e registrar o resultado do comando de [3.5](#35-resolucao-e-janela) ([guia de operações](#37-guia-de-operacoes-por-ambiente)).
3. Registrar data e hora de início e seguir o roteiro do fluxo na [seção 6](#6-roteiros-passo-a-passo), sem desvios.
4. A cada ponto de verificação, o observador marca atendido ou não atendido. Em caso de não atendimento, registra a ocorrência com a captura de tela.
5. Ao final, registrar a hora de término e a captura do estado final do fluxo (saída observável da [Tabela 1 da Fase 1](../fase-1/escopo-da-avaliacao.md#fluxos)).
6. Classificar o resultado da tentativa conforme a Tabela 13.
7. Se houver falha, aplicar a reprodução de [4.6](#46-reproducao-de-falhas).
8. Preencher a linha da combinação na [tabela de M6](registro-adaptabilidade.md#registro-m6) do registro.

| Código | Resultado | Condição |
|---|---|---|
| `C` | Concluída | Todos os pontos de verificação atendidos, sem ajuste extraordinário |
| `F` | Falha | Algum ponto não atendido (`F-BLQ`, etapa bloqueada) ou conclusão possível só com ajuste extraordinário (`F-AJ`) |
| `I` | Inviável | Combinação excluída no planejamento por incompatibilidade documentada ([4.5](#45-combinacoes-inviaveis)); sai do denominador |
| `X` | Inválida | Execução afetada por causa externa à plataforma ([seção 7](#7-validade-atribuicao-e-interrupcao)); deve ser repetida |

*Tabela 13. Códigos de resultado de uma execução de M6. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

### 4.4 Preparação normal e ajuste extraordinário

A Fase 2 exige distinguir a preparação normal do ensaio de um ajuste extraordinário necessário para usar o produto.

| Preparação normal (permitida) | Ajuste extraordinário (a combinação vira `F-AJ`) |
|---|---|
| Instalar o navegador e atualizá-lo | Alterar sinalizadores (`flags`) ou `about:config` |
| Entrar com a conta de teste | Mudar o *user agent* ou usar modo de compatibilidade |
| Aceitar consentimento e cookies | Instalar extensões ou complementos para a plataforma funcionar |
| Permitir recursos solicitados pela própria página, como reprodução de mídia | Desativar recursos de segurança do navegador ou do sistema |
| Usar o idioma padrão do navegador | Trocar de navegador ou de motor para concluir a tarefa |

*Tabela 14. Preparação normal e ajuste extraordinário. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

### 4.5 Combinações inviáveis

Uma combinação é `I` somente quando a incompatibilidade entre **ferramentas e sistema** é conhecida e documentada **antes** da coleta, com justificativa. O que foi descoberto durante a execução e atribuído à plataforma é `F`. A combinação `I` não é automaticamente falha da plataforma e reduz `N`. Se o conjunto `FL1`–`FL3` de algum ambiente `A1`–`A4` ficar inviável, o julgamento de Q5 nesse ambiente é **inconclusivo** e o percentual é apresentado como parcial.

### 4.6 Reprodução de falhas

Para evitar que um evento isolado decida o resultado, uma falha observada é repetida **até duas vezes**, cada uma em sessão nova e com o mesmo perfil. A falha é **confirmada** quando ocorre em pelo menos 2 das 3 execuções. Se ocorrer em apenas uma, é registrada como intermitente, a combinação é `C` e a ocorrência fica anotada para a discussão. As três tentativas ficam nas colunas `T1` a `T3` da tabela de M6 do registro.

### 4.7 Cálculo e julgamento de Q5 e H5

A fórmula é a da [ficha de M6](../fase-2/metricas.md#16-m6-execucao-por-ambiente), `M6 = 100 × C/N`, em que `C` é o número de combinações com resultado final `C` e `N`, o de combinações elegíveis testadas (16 menos as `I`). A Tabela 15 converte contagens em notas para `N = 16`, conforme a [Tabela 2 de Critérios de julgamento](../fase-2/criterios-julgamento.md#2-metricas-percentuais).

| Nota | Nível | Percentual | Combinações concluídas (`N = 16`) |
|:---:|---|---:|---:|
| 3 | Excelente | 100% | 16 |
| 2 | Alvo | 90% ≤ x < 100% | 15 |
| 1 | Mínimo aceitável | 75% ≤ x < 90% | 12 a 14 |
| 0 | Inaceitável | x < 75% | 11 ou menos |

*Tabela 15. Notas de M6 em contagens absolutas. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base em [Critérios de julgamento](../fase-2/criterios-julgamento.md#2-metricas-percentuais)*

- **H5** é sustentada na amostra quando ao menos 90% das combinações são concluídas (15 de 16 com `N = 16`) e atende às condições de verificação de Q5. Caso contrário é não sustentada, ou inconclusiva se faltarem dados válidos ou cobertura ([estados da hipótese](../fase-2/questoes-hipoteses.md#6-interpretacao-das-hipoteses)).
- **Q5** é atendida quando M6 tem nota 2 ou 3 **e** nenhum fluxo essencial é impedido. Para essa regra, tratam-se como essenciais `FL1`–`FL3`, que a Fase 1 define como a jornada central de estudo; `FL4` é secundário. Uma falha confirmada em `FL1`–`FL3` em qualquer ambiente impede o atendimento de Q5, mesmo com percentual alto.
- Registrar sempre as contagens absolutas e a matriz ambiente × fluxo.

## 5. Procedimento de M7

<a id="m7"></a>

### 5.1 Unidade de observação e universo

A unidade de observação é a combinação **ambiente–dimensão–fluxo** (`M7-<ambiente>-<dimensão>-<fluxo>`). O universo planejado tem **32 combinações**: `A1`–`A4` × `J1`, `J2` × `FL1`–`FL4`.

### 5.2 Relação com M6 e M10 (sem dupla contagem)

- **M6 e M7 usam a mesma sessão em `J2`, com critérios e denominadores separados.** A execução em `J2` responde a M6 pela conclusão do roteiro e a M7 pela preservação de conteúdo e controles. Os resultados ficam em colunas e arquivos distintos e nunca são somados. Uma combinação pode passar em M6 e falhar em M7.
- **M7 e M10:** M7 avalia a janela com zoom de 100%. Ampliação de texto e zoom de 200% pertencem a [`Q9`/`M10`](../fase-2/metricas.md#110-m10-preservacao-com-ampliacao) e não são testados aqui.

### 5.3 Passos de execução

1. Conferir a preparação (PA-1 a PA-10).
2. Configurar a dimensão (`J1` ou `J2`), maximizar a janela e registrar o resultado do comando de [3.5](#35-resolucao-e-janela).
3. Percorrer o roteiro do fluxo ([seção 6](#6-roteiros-passo-a-passo)).
4. Em **cada ponto de verificação**, conferir o inventário de controles essenciais ([5.4](#54-inventario-de-controles-essenciais)): o conteúdo está visível e legível e o controle está presente e operável sem recurso externo ao uso normal.
5. Registrar cada problema como ocorrência, com a gravidade da Tabela 17 e a captura de tela.
6. Classificar a combinação (`C` ou `F`) e preencher a linha da combinação na [tabela de M7](registro-adaptabilidade.md#registro-m7) do registro.

Uma combinação é `C` quando o roteiro é concluído e **nenhum** problema de gravidade `G2` ou `G3` é registrado. Os códigos `I` e `X` e a reprodução em 2 de 3 seguem [4.3](#43-passos-de-execucao), [4.5](#45-combinacoes-inviaveis) e [4.6](#46-reproducao-de-falhas).

### 5.4 Inventário de controles essenciais

A Tabela 16 lista o conteúdo e os controles que M7 exige preservados. A descrição é funcional, pois os rótulos da interface podem mudar. O avaliador registra o rótulo real de cada item na [tabela de rótulos](registro-adaptabilidade.md#registro-rotulos) do registro, durante a preparação.

| Fluxo | ID | Conteúdo ou controle essencial |
|---|---|---|
| `FL1` | CE1.1 | Menu ou busca para localizar a disciplina |
| `FL1` | CE1.2 | Item do curso-alvo |
| `FL1` | CE1.3 | Lista de unidades e aulas do curso |
| `FL1` | CE1.4 | Conteúdo da aula selecionada (título e área principal) |
| `FL2` | CE2.1 | Área do vídeo e barra de reprodução |
| `FL2` | CE2.2 | Controle de iniciar e pausar |
| `FL2` | CE2.3 | Controle de legenda |
| `FL2` | CE2.4 | Acesso à transcrição |
| `FL3` | CE3.1 | Enunciado e área de resposta |
| `FL3` | CE3.2 | Controle de dica |
| `FL3` | CE3.3 | Controle de envio da resposta |
| `FL3` | CE3.4 | Área de retorno da plataforma e controle de continuidade |
| `FL4` | CE4.1 | Acesso à área do estudante |
| `FL4` | CE4.2 | Informações de progresso |

*Tabela 16. Conteúdo e controles essenciais por fluxo. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base nas saídas observáveis do [escopo](../fase-1/escopo-da-avaliacao.md#fluxos)*

### 5.5 Problemas de adaptação e gravidade

Rolagem vertical normal da página **não** é problema. O que se registra é perda ou prejuízo de conteúdo e de controles essenciais.

| Gravidade | Definição | Exemplos | Efeito em M7 |
|:---:|---|---|---|
| `G3` Bloqueante | Impede concluir o roteiro ou acionar um controle essencial | Botão de envio fora da área alcançável; menu que não abre; sobreposição que cobre o controle | `F` |
| `G2` Maior | Perda parcial de conteúdo ou controle essencial, sem impedir a conclusão | Texto cortado; controle parcialmente sobreposto; necessidade de rolagem horizontal para alcançar um controle essencial | `F` |
| `G1` Menor | Defeito visual sem perda de conteúdo ou controle essencial | Alinhamento ou espaçamento irregular | `C`, com ocorrência anotada |

*Tabela 17. Gravidade dos problemas de adaptação à janela. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

Para a mesma regra, em M6, um impedimento é um ponto de verificação não atendido que bloqueia a etapa seguinte do roteiro (`F-BLQ`).

### 5.6 Cálculo e julgamento de Q6 e H6

A fórmula é a da [ficha de M7](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela), `M7 = 100 × C/N`, com `N = 32` menos as `I`. A Tabela 18 converte contagens em notas.

| Nota | Nível | Percentual | Combinações preservadas (`N = 32`) | Subconjunto essencial `FL1`–`FL3` (`N = 24`) |
|:---:|---|---:|---:|---:|
| 3 | Excelente | 100% | 32 | 24 |
| 2 | Alvo | 90% ≤ x < 100% | 29 a 31 | 22 e 23 |
| 1 | Mínimo aceitável | 75% ≤ x < 90% | 24 a 28 | 18 a 21 |
| 0 | Inaceitável | x < 75% | 23 ou menos | 17 ou menos |

*Tabela 18. Notas de M7 em contagens absolutas. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base em [Critérios de julgamento](../fase-2/criterios-julgamento.md#2-metricas-percentuais)*

- A **nota de M7** usa as 32 combinações, como na ficha da métrica.
- **H6** fala em "combinações essenciais". Por isso é verificada no subconjunto `FL1`–`FL3` (24 combinações), em que são necessárias ao menos 22 combinações preservadas, e o resultado dos dois recortes é apresentado ([ponto P4](#11-pontos-pendentes-e-decisoes-da-equipe)).
- **Q6** é atendida quando M7 tem nota 2 ou 3 **e** nenhum fluxo essencial é impedido (`G3` em `FL1`–`FL3`).

## 6. Roteiros passo a passo

Cada roteiro é único e serve às duas métricas: em M6 conta a conclusão de todos os pontos de verificação (`P`); em M7 conta também a presença e a operabilidade dos controles essenciais (`CE`) em cada ponto. O ponto de partida é a página inicial da plataforma, com a conta `D6` autenticada.

### 6.1 Roteiro `FL1` — navegação em cursos

| Passo | Ação | Ponto de verificação | Controles (M7) |
|:---:|---|---|---|
| 1 | Abrir a página inicial | `P1`: página carregada e navegação visível | CE1.1 |
| 2 | Localizar a disciplina `D1` pelo menu ou pela busca | `P2`: disciplina e seus cursos apresentados | CE1.1, CE1.2 |
| 3 | Abrir o curso `D2` | `P3`: página do curso com unidades e aulas listadas | CE1.3 |
| 4 | Selecionar a unidade e a aula `D3` | `P4`: conteúdo da aula apresentado (saída observável de `FL1`) | CE1.3, CE1.4 |

*Tabela 19. Roteiro de FL1. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [escopo](../fase-1/escopo-da-avaliacao.md#fluxos)*

### 6.2 Roteiro `FL2` — videoaulas

| Passo | Ação | Ponto de verificação | Controles (M7) |
|:---:|---|---|---|
| 1 | Abrir a videoaula `D4` | `P1`: reprodutor visível com seus controles | CE2.1, CE2.2 |
| 2 | Iniciar a reprodução | `P2`: estado de reprodução e tempo avançando por pelo menos 5 s | CE2.1, CE2.2 |
| 3 | Pausar a reprodução | `P3`: estado pausado e tempo parado | CE2.2 |
| 4 | Acionar a legenda | `P4`: legenda apresentada | CE2.3 |
| 5 | Abrir a transcrição | `P5`: transcrição apresentada (saída observável de `FL2`) | CE2.4 |

*Tabela 20. Roteiro de FL2. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [escopo](../fase-1/escopo-da-avaliacao.md#fluxos)*

O avanço do tempo, e não o áudio, comprova a reprodução, pois ambientes virtuais podem não ter dispositivo de som. Como `D4` é escolhido com legenda e transcrição, a ausência delas em um ambiente é falha de ponto de verificação, não "não disponível".

### 6.3 Roteiro `FL3` — exercícios

| Passo | Ação | Ponto de verificação | Controles (M7) |
|:---:|---|---|---|
| 1 | Abrir o exercício `D5` | `P1`: enunciado e área de resposta visíveis | CE3.1 |
| 2 | Solicitar uma dica | `P2`: dica apresentada | CE3.2 |
| 3 | Informar uma resposta e enviá-la | `P3`: retorno da plataforma sobre a resposta apresentado | CE3.1, CE3.3, CE3.4 |
| 4 | Acionar a continuidade da atividade | `P4`: continuidade apresentada (saída observável de `FL3`) | CE3.4 |

*Tabela 21. Roteiro de FL3. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [escopo](../fase-1/escopo-da-avaliacao.md#fluxos)*

### 6.4 Roteiro `FL4` — progresso do estudante

| Passo | Ação | Ponto de verificação | Controles (M7) |
|:---:|---|---|---|
| 1 | A partir da página inicial, abrir a área do estudante | `P1`: área do estudante exibida | CE4.1 |
| 2 | Localizar e abrir a informação de progresso | `P2`: informações de progresso da conta `D6` apresentadas (saída observável de `FL4`) | CE4.2 |

*Tabela 22. Roteiro de FL4. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [escopo](../fase-1/escopo-da-avaliacao.md#fluxos)*

Os pontos de verificação são comuns a todos os ambientes. O roteiro deve ser validado em um ensaio piloto não oficial em `A1`, cujos resultados **não** entram nas métricas, e lido por um avaliador que não o escreveu ([seção 10](#10-rastreabilidade-com-a-issue-25)).

## 7. Validade, atribuição e interrupção

### 7.1 Validade de uma execução

Uma execução é válida quando: (a) a versão do navegador e do sistema coincide com a registrada na preparação; (b) o perfil é novo e sem extensões; (c) a resolução confere com [3.5](#35-resolucao-e-janela); (d) os dados `D1`–`D6` são os congelados; (e) há executor, observador, data, hora e captura de tela do estado final; e (f) a plataforma estava disponível. Falhando algum item, a execução é `X` e deve ser refeita.

### 7.2 Atribuição de causa

Só falhas atribuídas à plataforma contam como `F`.

| Atribuição | Indício | Tratamento |
|---|---|---|
| Plataforma | Falha reproduzida em 2 de 3 execuções, em perfil novo e configuração padrão, sem erro externo | `F` |
| Ambiente de teste | Falha ligada à máquina virtual, a *driver*, a codec ou a dispositivo ausente | Corrigir a preparação e refazer (`X`), ou tratar como `I` conforme [4.5](#45-combinacoes-inviaveis) |
| Executor | Passo do roteiro executado incorretamente | `X`; refazer |
| Serviço externo ou rede | Página de erro do servidor, queda de conexão, indisponibilidade temporária | `X`; refazer em outro horário |

*Tabela 23. Atribuição de causa das falhas. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

Distribuições Linux podem não incluir codecs de mídia por padrão, o que afeta `FL2`. Antes da coleta, a equipe decide se a instalação de codecs conta como preparação normal do ambiente e registra a decisão ([ponto P5](#11-pontos-pendentes-e-decisoes-da-equipe)).

### 7.3 Interrupção

A execução é interrompida e marcada `X` em caso de perda de conexão, travamento da máquina virtual, sessão expirada por inatividade do avaliador ou indisponibilidade do serviço. Uma falha da própria plataforma, como o travamento do navegador reproduzido em 2 de 3 execuções, não é interrupção: é `F`.

## 8. Formulários e modelos de registro

Os formulários são tabelas em Markdown na página [Registro de execuções (M6 e M7)](registro-adaptabilidade.md), editadas por *pull request* durante a Fase 4. Isso mantém os dados brutos no repositório e visíveis na GitPage, sem depender de planilhas externas.

| Parte do registro | Conteúdo | Linhas |
|---|---|---:|
| [Preparação dos ambientes](registro-adaptabilidade.md#registro-preparacao) | Identificação, versões, modalidade, recursos e verificações PA-1 a PA-10 por ambiente | 4 |
| [Dados de teste e rótulos](registro-adaptabilidade.md#registro-rotulos) | Valores congelados de `D1`–`D6` e rótulos reais dos controles `CE` | 6 e 14 |
| [Resolução verificada](registro-adaptabilidade.md#registro-resolucao) | Resultado do comando de 3.5 por ambiente e dimensão | 8 |
| [Registro de M6](registro-adaptabilidade.md#registro-m6) | Uma linha por combinação, com as três tentativas, resultado final, tipo de falha, ocorrência e evidência | 16 |
| [Registro de M7](registro-adaptabilidade.md#registro-m7) | Uma linha por combinação, com resultado, gravidade máxima, controles afetados, ocorrência e evidência | 32 |
| [Ocorrências](registro-adaptabilidade.md#registro-ocorrencias) | Uma linha por problema, com passos de reprodução, gravidade e atribuição | variável |
| [Resumo e julgamento](registro-adaptabilidade.md#registro-resumo) | Matrizes de resultado, notas, estado de H5 e H6 e decisão | 4 tabelas |

*Tabela 24. Partes do registro de execuções. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

**Evidências e rastreabilidade do dado bruto à métrica.** Todo registro é indexado pelo identificador da combinação (`M6-A1-FL2`, `M7-A1-J1-FL2`). Cada captura segue o padrão `<id_combinacao>_<tentativa>_<AAAAMMDD>.png`, por exemplo, `M6-A1-FL2_t1_20261112.png`, e a coluna de evidência cita esse nome. A coluna de ocorrência cita o `id_ocorrencia`, que também aparece na tabela de ocorrências. Assim, é possível ir da métrica calculada à linha de registro, à captura ou gravação e à ocorrência. O local de armazenamento das evidências deve ser definido antes da coleta ([ponto P7](#11-pontos-pendentes-e-decisoes-da-equipe)).

## 9. Cálculo, interpretação e relato

### 9.1 Fórmulas

| Métrica | Fórmula | `C` | `N` |
|---|---|---|---|
| [`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) | `100 × C/N` | Combinações ambiente–fluxo com resultado final `C` | 16 menos as `I` |
| [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) | `100 × C/N` | Combinações ambiente–dimensão–fluxo com resultado `C` | 32 menos as `I` |

*Tabela 25. Fórmulas de M6 e M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base nas [fichas das métricas](../fase-2/metricas.md)*

### 9.2 Interpretação

1. Calcular M6 e M7 a partir das tabelas do registro, conferindo à mão ao menos uma linha de cada.
2. Converter o percentual em nota pela Tabela 15 e pela Tabela 18.
3. Verificar a regra de fluxo essencial impedido ([4.7](#47-calculo-e-julgamento-de-q5-e-h5), [5.6](#56-calculo-e-julgamento-de-q6-e-h6)).
4. Classificar H5 e H6 como sustentada, não sustentada ou inconclusiva.
5. Relatar as matrizes ambiente × fluxo (M6) e ambiente × dimensão × fluxo (M7), as contagens absolutas, as ocorrências por gravidade e as versões testadas.
6. Redigir as conclusões dentro dos [limites de validade](../fase-1/escopo-da-avaliacao.md#limites-de-validade): valem para os ambientes, versões e período registrados, não para outros navegadores, sistemas ou dispositivos móveis.

Se a equipe não aprovar os critérios antes da coleta, o resultado permanece inconclusivo, conforme [Critérios de julgamento](../fase-2/criterios-julgamento.md#5-regra-de-julgamento).

### 9.3 Consistência entre os métodos desta fase e a especificação da Fase 2

A Tabela 26 explicita a coerência entre o que a Fase 2 especifica e o que a Fase 3 usa para obter e julgar cada métrica.

| Elemento da Fase 2 | Método e recurso desta fase | Coerência |
|---|---|---|
| Ficha de M6: `100 × C/N` sobre combinações SO–navegador–fluxo; fonte: matriz de execução, navegador, SO, fluxo e evidência | Tabela de M6 do registro, uma linha por combinação, com resultado `C`/`F`/`I`/`X` e captura | Mesma unidade, fórmula e fonte; `N` exclui só combinações inviáveis documentadas |
| Ficha de M7: `100 × C/N` sobre combinações ambiente–dimensão–fluxo; fonte: roteiro com dimensões, capturas e resultado por fluxo | Roteiro único, inventário de controles `CE`, gravidade e capturas; `J1` e `J2` | Mesma unidade, fórmula e fonte; "preservado" operacionalizado por `CE` e gravidade |
| Níveis de pontuação: 100%, 90% e 75% para M6 e M7 | Tabelas de conversão em contagens ([4.7](#47-calculo-e-julgamento-de-q5-e-h5), [5.6](#56-calculo-e-julgamento-de-q6-e-h6)) | Mesmas faixas, convertidas em números de combinações |
| Regra de julgamento: nota 2 ou 3 e nenhuma tarefa essencial impedida | `FL1`–`FL3` tratados como essenciais; falha confirmada em qualquer um impede o atendimento da questão | Aplicação literal da regra, com a definição de "essencial" explicitada |
| Q5: distinguir preparação de ajuste extraordinário; inviabilidades no planejamento | [4.4](#44-preparacao-normal-e-ajuste-extraordinario) e [4.5](#45-combinacoes-inviaveis) | Exigência atendida |
| Q6: dimensão na identificação; sem dupla contagem | [5.2](#52-relacao-com-m6-e-m10-sem-dupla-contagem) e identificadores `M7-<amb>-<J>-<FL>` | Exigência atendida |
| H5 e H6: estados sustentada, não sustentada e inconclusiva | [9.2](#92-interpretacao) | Estados idênticos aos de [Questões e hipóteses](../fase-2/questoes-hipoteses.md#6-interpretacao-das-hipoteses) |
| Ambientes `A1`–`A4` e fluxos `FL1`–`FL4` | [3.1](#31-ambientes-da-matriz-a1a4) e [seção 6](#6-roteiros-passo-a-passo) | Coerente, com `A3` pendente de versões ([P6](#11-pontos-pendentes-e-decisoes-da-equipe)) |

*Tabela 26. Consistência entre a especificação da Fase 2 e os métodos da Fase 3. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

Três pontos exigem alinhamento formal porque a Fase 3 não pode contradizer as fases anteriores: o conjunto de ambientes (P1), a virtualização do Windows (P3) e o sentido de "essenciais" em H6 (P4). Eles estão na [seção 11](#11-pontos-pendentes-e-decisoes-da-equipe).

### 9.4 Da medição à decisão e às ações

O propósito da Fase 1 é apoiar a decisão [`D1`](../fase-1/requisitos-de-avaliacao.md#requisitante). A Tabela 27 indica como cada resultado de M6 e M7 se traduz no desfecho de `D1` e em uma ação para a coordenação. A decisão final também depende de M1–M5.

| Resultado observado | Desfecho de `D1` quanto à adaptabilidade | Ação para o requisitante |
|---|---|---|
| Q5 e Q6 atendidas, sem falha confirmada em `A1`–`A4` | Sem ressalvas | Manter como configuração recomendada os sistemas, navegadores e resoluções testados, informando as versões |
| Falha confirmada só em `FL4` ou apenas com gravidade `G2` em uma dimensão | Com ressalva | Orientar o uso da outra dimensão ou ambiente e registrar a ocorrência no canal de suporte da plataforma |
| Falha confirmada em `FL1`–`FL3` em um ambiente | Apenas nos ambientes que concluíram | Restringir o uso nos computadores da escola aos navegadores e sistemas que concluíram os fluxos |
| Falha confirmada em `FL1`–`FL3` em todos os ambientes de um mesmo navegador ou dimensão | Não recomendar naquela condição | Excluir o navegador ou a resolução da orientação à escola |
| Dados insuficientes ou combinações essenciais não executadas | Inconclusivo | Completar a execução antes de decidir |

*Tabela 27. Tradução dos resultados de M6 e M7 em desfechos de D1 e ações. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base nos desfechos de [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md#requisitante)*

## 10. Rastreabilidade com a issue #25

A Tabela 28 relaciona as tarefas e os critérios de aceite da parte de adaptabilidade da issue ao local onde são atendidos.

| Item da issue #25 | Atendimento |
|---|---|
| Definir procedimentos de execução de FL1–FL4 em A1–A4 | [3.1](#31-ambientes-da-matriz-a1a4), [4.3](#43-passos-de-execucao), [6](#6-roteiros-passo-a-passo) |
| Especificar testes de compatibilidade entre sistemas operacionais e navegadores | [4](#4-procedimento-de-m6), [3.2](#32-ambientes-complementares) |
| Definir procedimentos nas resoluções 1366 × 768 e 1920 × 1080 | [3.5](#35-resolucao-e-janela), [5](#5-procedimento-de-m7) |
| Estabelecer critérios para identificar problemas de adaptação e impedimentos | [4.3](#43-passos-de-execucao), [4.4](#44-preparacao-normal-e-ajuste-extraordinario), [5.5](#55-problemas-de-adaptacao-e-gravidade), [7](#7-validade-atribuicao-e-interrupcao) |
| Documentar procedimentos de coleta para M6 e M7 | [4](#4-procedimento-de-m6), [5](#5-procedimento-de-m7) |
| Roteiros passo a passo | [6](#6-roteiros-passo-a-passo) |
| Formulários e modelos de registro | [8](#8-formularios-e-modelos-de-registro) |
| Relacionar a Q5–Q6, H5–H6 e M6–M7 | [2](#2-rastreabilidade-com-as-fases-1-e-2), Tabelas 2 e 3 |
| Explicitar cálculo e interpretação conforme os critérios de julgamento | [4.7](#47-calculo-e-julgamento-de-q5-e-h5), [5.6](#56-calculo-e-julgamento-de-q6-e-h6), [9](#9-calculo-interpretacao-e-relato) |
| Revisar a consistência com o escopo da Fase 1 | [3.1](#31-ambientes-da-matriz-a1a4), [11](#11-pontos-pendentes-e-decisoes-da-equipe) |
| Critério de aceite: instrumentos, condições e dados de teste identificados | [3.3](#33-instrumentos), [3.4](#34-preparacao-do-ambiente), [3.6](#36-requisitos-conhecimento-do-avaliador-e-massa-de-dados) |
| Critério de aceite: outro avaliador reproduz os procedimentos | Roteiros, guia de operações ([3.7](#37-guia-de-operacoes-por-ambiente)) e registro; validação pelo ensaio piloto de [6.4](#64-roteiro-fl4-progresso-do-estudante) |
| Critério de aceite: rastreabilidade explícita com métricas e critérios da Fase 2 | [2](#2-rastreabilidade-com-as-fases-1-e-2) |

*Tabela 28. Rastreabilidade entre a issue #25 (adaptabilidade) e este artefato. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

A Tabela 29 relaciona os critérios de avaliação das Fases 3 e 4 ([Fase 3](../criterios/fase3.md) e [Fase 4](../criterios/fase4.md)) ao que este artefato oferece.

| Critério | Como este artefato contribui | Onde |
|---|---|---|
| `F3-C1` Método e repetibilidade | Método justificado, roteiros com pontos de verificação, regras de classificação e guia de operações que dispensam conhecimento prévio | [1.1](#11-justificativa-do-metodo), [3.7](#37-guia-de-operacoes-por-ambiente), [4](#4-procedimento-de-m6) a [6](#6-roteiros-passo-a-passo) |
| `F3-C2` Recursos e ambiente | Requisitos de hardware e software, conhecimento do avaliador, massa de dados justificada | [3](#3-ambiente-de-teste-e-instrumentos), [3.6](#36-requisitos-conhecimento-do-avaliador-e-massa-de-dados) |
| `F3-C3` Cronograma | Cronograma de execução proposto, alinhado à Fase 4 | [12](#12-cronograma-de-execucao) |
| `F3-C7` GitPage | Página no menu da Fase 3, com *links* cruzados para as Fases 1 e 2 e histórico de versões | [Visão geral da Fase 3](index.md) |
| `F3-C8` Consistência entre Fases 2 e 3 | Matriz de consistência e tabelas de conversão dos níveis de pontuação | [9.3](#93-consistencia-entre-os-metodos-desta-fase-e-a-especificacao-da-fase-2) |
| `F4-C1` Obtenção das medidas | Roteiros únicos e registro por combinação, para execução fiel ao método | [6](#6-roteiros-passo-a-passo), [8](#8-formularios-e-modelos-de-registro) |
| `F4-C2` Dados brutos | Registro indexado por combinação, nomenclatura de evidências e gravação de sessões | [8](#8-formularios-e-modelos-de-registro), [3.3](#33-instrumentos) |
| `F4-C3` Análise e respostas GQM | Fórmulas, conversão em notas, estados de H5 e H6 e tabelas de resumo | [9](#9-calculo-interpretacao-e-relato), [resumo do registro](registro-adaptabilidade.md#registro-resumo) |
| `F4-C4` Coerência com o propósito | Ligação dos resultados ao desfecho de `D1` | [9.4](#94-da-medicao-a-decisao-e-as-acoes) |
| `F4-C5` Julgamento e sugestões | Ações concretas para a coordenação por tipo de resultado | [9.4](#94-da-medicao-a-decisao-e-as-acoes) |

*Tabela 29. Contribuição deste artefato aos critérios das Fases 3 e 4. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## 11. Pontos pendentes e decisões da equipe

Estes pontos aparecem na comparação entre o ambiente de testes, a Fase 1 e a Fase 2. Os que afetam a coleta devem ser resolvidos antes da Fase 4.

| ID | Ponto | Onde afeta | Proposta |
|---|---|---|---|
| P1 | O ambiente de testes lista **seis sistemas operacionais**, mas a Fase 1 e H5 delimitam `A1`–`A4` (Windows com Chrome e Firefox, macOS com Safari, Ubuntu com Firefox) | Denominador de M6, H5 | Manter `A1`–`A4` como universo formal. Se a equipe quiser incluir as demais distribuições no julgamento, atualizar Fase 1 (escopo), H5 e `M6` antes da coleta |
| P2 | Executar ou não os ambientes complementares `AC1`–`AC3` | Esforço (24 execuções) | Executar somente se houver tempo, relatando à parte |
| P3 | A Fase 1 (seção 2.2) prevê Windows e macOS em **computadores reais**, mas o ambiente de testes **virtualiza o Windows** (Winboat/Docker) | Escopo, seção 2.2; condição de `A1` e `A2` | Atualizar o escopo para refletir a virtualização, registrando-a como limite de validade. Não comparar consumo de recursos entre máquinas distintas |
| P4 | H6 fala em combinações "essenciais" e a ficha de M7 em combinações "testadas" | Julgamento de H6 | Nota de M7 nas 32 combinações; H6 no subconjunto `FL1`–`FL3`; relatar os dois |
| P5 | Codecs de mídia em Linux (Fedora, openSUSE) e ausência de som em máquinas virtuais | `FL2` em `A4` e em `AC1`–`AC3` | Decidir se a instalação de codecs é preparação normal e registrar |
| P6 | `A3`: versão do macOS e do Safari ausentes (marcadas `X`); a linha do Safari não existe no quadro de versões; hardware sem registro | Existência de `A3`, que cobre o motor WebKit | Completar o quadro. Confirmar se o computador dispõe de `J1` e `J2`; se não, registrar a configuração mais próxima como desvio de protocolo |
| P7 | Local de armazenamento das evidências (capturas e gravações) | Seção 8 | Definir pasta no repositório ou repositório externo antes da coleta |
| P8 | Regras de falha confirmada (2 de 3), de gravidade `G2` como falha e de essencial como `FL1`–`FL3` | Julgamento de M6 e M7 | Aprovar com os demais critérios antes da coleta, como exige a Fase 2 |
| P9 | Ajustes editoriais no ambiente de testes: data da atualização (`dia X`), "propietários", "maquinas"; Chrome do Windows (157.0) em versão diferente do Chrome Linux (156.0); Firefox do openSUSE em 153.5, abaixo dos demais | Registro de versões | Corrigir o texto, preencher a data e registrar as diferenças de versão na discussão |
| P10 | Gravação de vídeo das sessões: o critério `F4-C2` menciona vídeos de testes | Esforço e armazenamento | Gravar todas as sessões em `J2` (16) e toda sessão com falha; decidir onde guardar os arquivos |
| P11 | Datas do cronograma da seção 12 | Entrega 2 em 18/11 | Ajustar ao cronograma geral da Fase 4 e à execução de M1–M5 em `A1` |
| P12 | O suporte declarado pela Khan Academy não inclui Linux nem o Edge | Interpretação de falhas em `A4` e em `AC1`–`AC3` | Registrar o dado na discussão dos resultados, sem alterar a matriz nem os critérios |

*Tabela 30. Pontos pendentes e decisões da equipe. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## 12. Cronograma de execução

O cronograma abaixo é uma **proposta** para alinhar a execução de M6 e M7 à Fase 4 e à Entrega 2 de 18/11/2026, mantendo margem de revisão. As datas devem ser ajustadas ao cronograma geral e à execução de M1–M5 em `A1` ([ponto P11](#11-pontos-pendentes-e-decisoes-da-equipe)).

| Data | Atividade | Produto | Seção |
|---|---|---|---|
| 09/11 | Resolver os pontos P1 a P9 e aprovar critérios e regras de julgamento | Decisões registradas e versões ajustadas | [11](#11-pontos-pendentes-e-decisoes-da-equipe) |
| 09 a 10/11 | Preparar os ambientes e congelar `D1`–`D6`; completar o quadro de versões | Preparação do registro preenchida | [3.4](#34-preparacao-do-ambiente) |
| 10/11 | Ensaio piloto em `A1` e revisão do roteiro por quem não o escreveu | Roteiros ajustados; resultados não contados | [6](#6-roteiros-passo-a-passo) |
| 11 a 13/11 | Execução oficial: 16 sessões em `J2` (M6 e M7) e 16 em `J1` (M7), um ambiente ou par de ambientes por dupla | Registro de M6 e M7, capturas e gravações | [4](#4-procedimento-de-m6), [5](#5-procedimento-de-m7) |
| 14/11 | Reprodução das falhas e, se decidido, ambientes complementares | Falhas confirmadas ou intermitentes | [4.6](#46-reproducao-de-falhas), [3.2](#32-ambientes-complementares) |
| 14 a 15/11 | Consolidar o registro e calcular M6 e M7 | Tabelas de resumo | [9](#9-calculo-interpretacao-e-relato) |
| 16/11 | Julgar H5 e H6, relacionar a `D1` e redigir as ações | Texto de análise para o artigo | [9.4](#94-da-medicao-a-decisao-e-as-acoes) |
| 17/11 | Revisão de conteúdo e de formatação | Versão final | |
| 18/11 | Entrega 2 | Fases 3 e 4 e artigo completo | |

*Tabela 31. Cronograma de execução proposto para M6 e M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## Referências

<a id="s1"></a>

> [S1] KHAN ACADEMY. **Which browsers are supported?** Help Center. Disponível em: <https://support.khanacademy.org/hc/en-us/articles/204795660-Supported-browsers>. Acesso em: 7 nov. 2026.

<a id="s2"></a>

> [S2] KHAN ACADEMY. **What devices and browsers work best for Khan Academy?** Help Center. Disponível em: <https://support.khanacademy.org/hc/en-us/articles/204795430>. Acesso em: 7 nov. 2026.

<a id="s3"></a>

> [S3] KHAN ACADEMY. **What devices and specifications work best with Khan Academy Districts?** Help Center. Disponível em: <https://support.khanacademy.org/hc/nl/articles/360048672692>. Acesso em: 7 nov. 2026.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality. Genebra: ISO, 2016.

> BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The Goal Question Metric Approach. In: **Encyclopedia of Software Engineering**. John Wiley & Sons, 1994. p. 528–532.

Artefatos do projeto: [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md), [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md), [Objetivos](../fase-2/objetivos.md), [Questões e hipóteses](../fase-2/questoes-hipoteses.md), [Métricas](../fase-2/metricas.md), [Critérios de julgamento](../fase-2/criterios-julgamento.md) e [Ambiente de testes](ambiente-de-testes.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 07/11/2026 | Elaboração dos procedimentos de M6 e M7, com rastreabilidade com as Fases 1 e 2, requisitos e massa de dados, consistência com a Fase 2, cronograma e registro em Markdown. | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | A definir |