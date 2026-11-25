# Registro de execuções de acessibilidade (M8 a M11)

Este documento reúne a preparação dos ambientes, sessões e formulários de coleta de acessibilidade da versão web da **Khan Academy**, no recorte de `M8` (teclado), `M9` (leitores de tela), `M10` (ampliação a 200%) e `M11` (contraste textual e alto contraste).

**Base metodológica:** [procedimentos de acessibilidade da Fase 3](../fase-3/procedimentos-acessibilidade-apreensibilidade.md), [métricas da Fase 2](../fase-2/metricas.md), [questões e hipóteses](../fase-2/questoes-hipoteses.md) e [critérios de julgamento](../fase-2/criterios-julgamento.md). Este documento contém observações da amostra e não certifica conformidade integral da plataforma com a WCAG.

**Legenda de classificação:** `S` = sucesso; `SB` = sucesso com barreira não essencial; `F` = falha; `IMP` = impedimento por barreira da plataforma; `X` = execução inválida. `S` e `SB` entram no numerador das taxas de conclusão; `F` e `IMP` somente no denominador.



---

<a id="registro-preparacao"></a>

## 1. Preparação dos ambientes

A Tabela 1 identifica os ambientes físicos utilizados, distinguindo-os de eventuais máquinas virtuais empregadas em avaliações de adaptabilidade. A data de preparação só é apresentada como tal quando foi registrada; as demais datas correspondem às sessões.

| ID | Sistema operacional | Navegador | Versão | Modalidade | Recursos | Data da preparação | Responsável | Build / kernel |
|---|---|---|---|---|---|---|---|---|
| `A1` | Windows 11, 25H2 | Google Chrome | 157.0.8103.79 | Computador real, Samsung Galaxy Book4 360 | Intel Core 7 150U; 16 GB RAM | Sessões em 17/11/2026 e 21/11/2026 | [Enzo Menali](https://github.com/menali17) | Build 26200.9974 |
| `A3` | macOS Tahoe | Apple Safari | 26.5.2 (21624.2.5.11.8) | Computador real, MacBook Pro M4 | 32 GB RAM; 10 núcleos | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | Build 27.2.1 |
| `A4` | Ubuntu 26.10 | Mozilla Firefox | 160.0.1 | Computador real, Samsung Galaxy Book4 360 (dual boot) | Intel Core 7 150U; 16 GB RAM | Não registrada separadamente; sessões em 21/11/2026 | [Enzo Menali](https://github.com/menali17) | Kernel informado: 7.3.0-10 |

*Tabela 1. Identificação dos ambientes avaliados. Fonte: registros de execução de [Enzo Menali](https://github.com/menali17)  e  [Luisa de Souza](https://github.com/luisa12ll)*

### 1.1 A1 — Windows/Chrome

| Parâmetro | Valor especificado no protocolo | Valor registrado | Situação |
|---|---|---|:---:|
| Sistema e build | Identificar Windows e build | Windows 11 25H2, build 26200.9974 | Conforme |
| Navegador | Chrome e versão | Chrome 157.0.8103.79 | Conforme |
| Processador | Registrar modelo | Intel Core 7 150U | Registrado |
| Memória | Registrar capacidade | 16 GB | Registrado |
| Modalidade | Computador real ou VM identificada | Galaxy Book4 360, computador real | Conforme |
| Resolução do ensaio | 1366 × 768 | 1366 × 768 | Conforme |
| Zoom em M8/M9 | 100%, conforme preparação comum | Configuração padrão utilizada | Conforme |
| Zoom em M10 | 200% | 200% | Conforme |
| Tema de contraste em M11 | Registrar tema | Céu noturno | Conforme |
| Leitor de tela em M9 | NVDA; voz em português | NVDA 2026.3.1 | Versão registrada |
| Idioma da plataforma | Português do Brasil | Conteúdos e interface em português nas evidências | Observado |
| Perfil do navegador | Sem extensões, salvo ferramentas autorizadas | Não documentado individualmente | Verificado |
| Notificações | Desativadas | Não documentado individualmente | Verificado |
| Conta utilizada | Conta de teste controlada pela equipe | Conta pessoal autenticada durante os ensaios | Verificado |

*Tabela 2. Verificação do ambiente A1. Fonte: registros de execução de [Enzo Menali](https://github.com/menali17) .*

### 1.2 A3 — macOS/Safari

A tabela abaixo foi **preservada do documento da avaliadora**, inclusive as lacunas que já existiam nos campos não preenchidos e a não conformidade registrada para a conta de teste.

| Parâmetro de configuração | Valor especificado | Valor verificado no ensaio | Situação |
|---|---|---|:---:|
| Sistema operacional | macOS Tahoe | macOS Tahoe | Conforme|
| *Build* exata do sistema | 27.2.1 | 27.2.1 | |
| Navegador | Apple Safari 26.5.2 | Apple Safari 26.5.2 (21624.2.5.11.8) | Conforme |
| Modalidade de execução | Computador real | Computador real |Conforme |
| Memória RAM | 32 GB | 32 GB | Conforme|
| Processador | 10 núcleos (computador real) | 10 núcleos (computador real) |Conforme |
| Resolução da tela | Registrar a resolução usada | 1470 × 956 (padrão; Retina 2560 × 1664), janela maximizada |Conforme|
| Nível de zoom | 100% | |Conforme|
| Idioma da plataforma | Português do Brasil | |Conforme |
| Perfil do navegador | Sem extensões | Janela privada do Safari, sem extensões | Conforme |
| Navegação por Tab no Safari | "Pressionar Tab para destacar cada item" ativado | Ativado | Conforme |
| Navegação pelo teclado no macOS | Ativada | | Conforme |
| Notificações do sistema | Desativadas (Não Perturbe) | |Conforme |
| Conta de teste | Mesma conta das demais sessões, autenticada antes da tarefa | Conta da avaliadora | Não conforme |
| Leitor de tela ([`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela)) | VoiceOver, voz em português, velocidade padrão | | |
| Gravação de áudio ([`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela)) | Áudio do VoiceOver audível na gravação | | |

*Tabela 3. Verificação do ambiente A3. Fonte: [Luisa de Souza](https://github.com/luisa12ll).*

### 1.3 A4 — Ubuntu/Firefox

| Parâmetro | Valor especificado no protocolo | Valor registrado | Situação |
|---|---|---|:---:|
| Sistema operacional | Ubuntu LTS segundo escopo da Fase 1 | Ubuntu 26.10 (não LTS) | Divergência documentada |
| Kernel | Registrar versão | 7.3.0-10 (informado na coleta) | Registrado |
| Navegador | Firefox e versão | Firefox 160.0.1 | Conforme |
| Modalidade | Computador real ou VM identificada | Galaxy Book4 360, dual boot | Conforme |
| Processador | Registrar modelo | Intel Core 7 150U | Registrado |
| Memória | Registrar capacidade | 16 GB | Registrado |
| Resolução | Registrar resolução usada | 1920 × 1080 | Conforme |
| Escala/orientação | Registrar configuração | 100%, paisagem | Registrado |
| Zoom em M8/M9 | 100% conforme preparação comum | Configuração padrão utilizada | Informado; não aferido isoladamente |
| Leitor de tela em M9 | Orca, voz em português | Orca 46.1 | Versão registrada |
| Idioma da plataforma | Português do Brasil | Conteúdos e interface em português nas evidências | Observado |
| Perfil do navegador | Sem extensões, salvo ferramentas autorizadas | Não documentado individualmente | Não verificado |
| Notificações | Desativadas | Não documentado individualmente | Não verificado |
| Conta utilizada | Conta de teste controlada pela equipe | Equivalência entre as sessões não comprovada | Não verificado |

*Tabela 4. Verificação do ambiente A4. Fonte: registros de execução de [Enzo Menali](https://github.com/menali17).*

**Nota de comparabilidade:** A4 foi executado em Ubuntu 26.10, ao passo que o [escopo da Fase 1](../fase-1/escopo-da-avaliacao.md#ambientes) especifica Ubuntu LTS. Os dados refletem o ambiente efetivamente utilizado; essa divergência deve acompanhar a interpretação dos resultados, sem substituição retroativa da versão do sistema.

<a id="registro-sessoes"></a>

## 2. Registro das sessões — Formulário F7

Os IDs de `A3` foram mantidos como no documento original. Os IDs adicionais de `A1`/`A4` foram estabelecidos **nesta consolidação** como referências de sessão; os nomes dos arquivos brutos permanecem inalterados.

| Sessão | Data | Avaliador | Observador | Ambiente | Métrica | Sistema / navegador | Recurso / configuração | Resolução |
|---|---|---|---|---|---|---|---|---|
| `AC-20261117-01` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | Não identificado | `A1` | M8 | Windows 11 25H2 / Chrome 157.0.8103.79 | Exclusivamente teclado; configuração-base | 1366 × 768 |
| `AC-20261117-02` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | Não identificado | `A1` | M10 | Windows 11 25H2 / Chrome 157.0.8103.79 | Zoom de 200% | 1366 × 768 |
| `AC-20261117-03` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | Não identificado | `A1` | M11 — texto | Windows 11 25H2 / Chrome 157.0.8103.79 | CCA; inspeções Lighthouse/axe; tema padrão | 1366 × 768 |
| `AC-20261117-04` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | Não identificado | `A1` | M11 — alto contraste | Windows 11 25H2 / Chrome 157.0.8103.79 | Tema Céu noturno | 1366 × 768 |
| `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | Não indicado | `A3` | M8 | macOS Tahoe / Safari 26.5.2 | Exclusivamente teclado; zoom 100% | 1470 × 956 |
| `AC-20261121-02` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | Não identificado | `A1` | M9 | Windows 11 25H2 / Chrome 157.0.8103.79 | NVDA 2026.3.1 | 1366 × 768 |
| `AC-20261121-03` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | Não identificado | `A4` | M8 | Ubuntu 26.10 / Firefox 160.0.1 | Exclusivamente teclado | 1920 × 1080 |
| `AC-20261121-04` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | Não identificado | `A4` | M9 | Ubuntu 26.10 / Firefox 160.0.1 | Orca 46.1 | 1920 × 1080 |
| `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | Não indicado | `A3` | M9 | macOS Tahoe / Safari 26.5.2 | VoiceOver, voz em português; zoom 100% | 1470 × 956 |

*Tabela 5. Registro das sessões, adaptação do F7. Fonte: [Enzo Menali](https://github.com/menali17) .*

**Dados adicionais do F7:** no `M8-A4-T1`, a execução começou na seção **Meus cursos**, em vez da página inicial; as sessões de `A3` utilizaram conta da avaliadora, conforme a Tabela 3. Valores como `Clear storage`, URLs finais por estado e configurações que não foram anotadas não devem ser preenchidos por inferência. As auditorias de P1–P6 e os testes com tecnologias assistivas são registros de naturezas distintas.

### 2.1 Conteúdo das tarefas — cartão executado

| Tarefa | Fluxo | Conteúdo-base | Variações efetivamente registradas |
|---|---|---|---|
| `T1` | `FL1` | Curso Matemática EF: 6º Ano; primeira unidade *Números: sistema de numeração decimal* | Em `M8-A4-T1`, o ponto inicial foi **Meus cursos**; no macOS, o curso já constava dessa área. |
| `T2` | `FL2` | Videoaula *História dos números*; iniciar, pausar e ativar legenda/transcrição quando disponível | Na execução `M9-A3-T2`, a avaliadora selecionou outra videoaula (*Exemplo de conversão de algarismos romanos*). A barreira registrada foi a impossibilidade de acessar/reproduzir o conteúdo com VoiceOver, não a escolha da aula. |
| `T3` | `FL3` | Exercício *Semelhanças e diferenças entre sistemas de numeração*; abrir, selecionar/preencher, enviar e observar retorno | `A1`/`A4` encontraram alternativas SIM/NÃO. Em `M8-A3-T3`, apareceram listas suspensas de sistemas posicionais; em `M9-A3-T3`, questão para converter `XXXI` para decimal; resposta de teste `122`, com retorno anunciado *Não é dessa vez*. |

**Link do exercício-base:** [Semelhanças e diferenças entre sistemas de numeração — Khan Academy](https://pt.khanacademy.org/math/6-ano-matematica/numeros-sistema-de-numeracao-decimal-6ano/os-numeros/e/semelhancas-e-diferencas-entre-sistemas-de-numeracao).

*Tabela 6. Conteúdo e variações observadas. Fonte: registros originais de A3 e execução em A1/A4.*

**Nota metodológica:** variações de pergunta ou videoaula não são tratadas como ausência de registro. No julgamento, elas delimitam a comparabilidade entre as combinações de acordo com a [seção 4.1 do procedimento](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#41-tarefas-de-referencia).

<a id="registro-m8"></a>

## 3. Registro de M8 — navegação por teclado (Formulário F5)

Teste de T1–T3 nos ambientes A1, A3 e A4, com foco, acionamento, ordem de navegação e conclusão registrados. **As 10 linhas do macOS abaixo reproduzem as observações da avaliadora, com links para os vídeos incorporados ao repositório.**

| ID | Tarefa | Etapa | Observação | Barreira | Evidência |
|---|---|---|---|---|---|
| `M8-A1-T1-E1` | `T1` | Localizar curso | Curso localizado pela navegação do teclado, com foco visível e ordem lógica no caminho observado | — | [M8_A1_Piloto_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T1_FL1.mp4) |
| `M8-A1-T1-E2` | `T1` | Abrir curso | Acesso realizado pelo teclado | — | [M8_A1_Piloto_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T1_FL1.mp4) |
| `M8-A1-T1-E3` | `T1` | Abrir unidade | Primeira unidade alcançada, sem armadilha de foco identificada | — | [M8_A1_Piloto_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T1_FL1.mp4) |
| `M8-A1-T2-E1` | `T2` | Abrir videoaula | Videoaula *História dos números* localizada; navegação extensa por Tab registrada na execução | — | [M8_A1_Piloto_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T2_FL2.mp4) |
| `M8-A1-T2-E2` | `T2` | Reproduzir | Reprodução acionada pelo teclado | — | [M8_A1_Piloto_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T2_FL2.mp4) |
| `M8-A1-T2-E3` | `T2` | Pausar | Reprodução pausada pelo teclado | — | [M8_A1_Piloto_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T2_FL2.mp4) |
| `M8-A1-T2-E4` | `T2` | Legenda/transcrição | Recurso acionado conforme registro da execução, com acesso funcional ao estado de conclusão | — | [M8_A1_Piloto_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T2_FL2.mp4) |
| `M8-A1-T3-E1` | `T3` | Abrir exercício | Exercício acessado utilizando o teclado | — | [M8_A1_Piloto_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T3_FL3.mp4) |
| `M8-A1-T3-E2` | `T3` | Solicitar dica, quando disponível | Ação de dica não individualizada na evidência de conclusão; não atribuir sucesso/falha à etapa opcional | — | [M8_A1_Piloto_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T3_FL3.mp4) |
| `M8-A1-T3-E3` | `T3` | Selecionar resposta | Alternativas SIM/NÃO não alcançadas nem acionadas pelos comandos convencionais tentados | `B-09` | [M8_A1_Piloto_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T3_FL3.mp4) |
| `M8-A1-T3-E4` | `T3` | Enviar resposta | Etapa essencial bloqueada pela impossibilidade de selecionar as alternativas | `B-09` | [M8_A1_Piloto_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T3_FL3.mp4) |
| `M8-A3-T1-E1` | `T1` | Localizar o curso | Foco visível em todos os itens e ordem coerente com a ordem visual; 19 Tabs a partir da barra de endereço até a área do curso em "Meus cursos" | --- | [`AC-20261121-01_M8-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T1.mov) |
| `M8-A3-T1-E2` | `T1` | Abrir o curso | O título "Matemática EF: 6º Ano" é texto e não recebe foco, assim como não é clicável com o mouse; o foco passa por "Ver tudo (10)" e segue para a primeira unidade, por onde o curso é acessado | --- | [`AC-20261121-01_M8-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T1.mov) |
| `M8-A3-T1-E3` | `T1` | Abrir a primeira unidade | Enter em "Números: sistema de numeração decimal" abriu a lista de aulas; sem armadilha de foco. A tarefa foi repetida três vezes na mesma gravação, com o mesmo comportamento, retornando à página inicial pelo logotipo com Tab | --- | [`AC-20261121-01_M8-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T1.mov) |
| `M8-A3-T2-E1` | `T2` | Abrir a videoaula | Foco visível e ordem coerente; 63 Tabs da barra de endereço até "História dos números" | `B-03` | [`AC-20261121-01_M8-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2.mov) |
| `M8-A3-T2-E2` | `T2` | Iniciar a reprodução | 40 Tabs até o player; Espaço inicia a reprodução | `B-03` | [`AC-20261121-01_M8-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2.mov) |
| `M8-A3-T2-E3` | `T2` | Pausar | Espaço pausa a reprodução | --- | [`AC-20261121-01_M8-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2.mov) |
| `M8-A3-T2-E4` | `T2` | Ativar legenda ou transcrição | Os controles do player (volume, CC e configurações) só aparecem e recebem foco com o ponteiro sobre o vídeo; pausado pelo teclado, continuam ocultos e fora da ordem do Tab. Com os controles visíveis, Enter no CC ativa a legenda. O menu de configurações prende o foco: Tab, Shift+Tab, setas e Esc não saem dele. A transcrição é acessível pelo teclado: Tab até a aba "Sobre" e seta para a direita até "Transcrição". Na gravação principal a avaliadora usou o **trackpad** para exibir os controles; o caminho somente por teclado foi demonstrado na gravação de verificação | `B-01`, `B-02` | [`AC-20261121-01_M8-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2.mov), [`AC-20261121-01_M8-A3-T2-verificacao`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2-verificacao.mov) |
| `M8-A3-T3-E1` | `T3` | Abrir o exercício | 34 Tabs até "Vamos lá"; Enter abre a primeira pergunta. Foco visível e ordem coerente | `B-03` | [`AC-20261121-01_M8-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T3.mov) |
| `M8-A3-T3-E2` | `T3` | Solicitar a dica | Botão de dica recebe foco e Enter exibe as dicas | --- | [`AC-20261121-01_M8-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T3.mov) |
| `M8-A3-T3-E3` | `T3` | Selecionar a resposta de teste | 45 Tabs até a primeira lista suspensa; Enter abre a lista, o foco fica visível na opção e Enter confirma a seleção. As duas listas são acessíveis pelo teclado | `B-03` | [`AC-20261121-01_M8-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T3.mov) |
| `M8-A3-T3-E4` | `T3` | Enviar e visualizar o retorno | 5 Tabs da última seleção até "Verificar"; Enter envia e o retorno da plataforma é exibido. Sem armadilha de foco e sem uso do **trackpad** | --- | [`AC-20261121-01_M8-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T3.mov) |
| `M8-A4-T1-E1` | `T1` | Localizar curso | Curso localizado pelo teclado; partida em **Meus cursos**, e não na página inicial | — | [M8_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T1_FL1.webm) |
| `M8-A4-T1-E2` | `T1` | Abrir curso | Acesso realizado pelo teclado | — | [M8_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T1_FL1.webm) |
| `M8-A4-T1-E3` | `T1` | Abrir unidade | Primeira unidade acessada | — | [M8_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T1_FL1.webm) |
| `M8-A4-T2-E1` | `T2` | Abrir videoaula | *História dos números* localizada | — | [M8_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T2_FL2.webm) |
| `M8-A4-T2-E2` | `T2` | Reproduzir | Reprodução iniciada | — | [M8_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T2_FL2.webm) |
| `M8-A4-T2-E3` | `T2` | Pausar | Reprodução pausada | — | [M8_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T2_FL2.webm) |
| `M8-A4-T2-E4` | `T2` | Legenda/transcrição | Etapa relatada como concluída na execução | — | [M8_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T2_FL2.webm) |
| `M8-A4-T3-E1` | `T3` | Abrir exercício | Exercício acessado | — | [M8_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T3_FL3.webm) |
| `M8-A4-T3-E2` | `T3` | Solicitar dica, quando disponível | Dica não individualizada na evidência; etapa opcional sem classificação própria | — | [M8_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T3_FL3.webm) |
| `M8-A4-T3-E3` | `T3` | Selecionar resposta | Tab, Shift+Tab, setas e Espaço não permitiram acionar as alternativas SIM/NÃO | `B-10` | [M8_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T3_FL3.webm) |
| `M8-A4-T3-E4` | `T3` | Enviar resposta | Etapa essencial não alcançada devido a B-10 | `B-10` | [M8_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T3_FL3.webm) |

*Tabela 7. Registro das etapas de M8 (A1, A3 e A4). Fonte: registros de [Enzo Menali](https://github.com/menali17) e [Luisa de Souza](https://github.com/luisa12ll).*

**Nota sobre `M8-A3-T2`:** a gravação principal contém uso de trackpad para revelar controles, enquanto a gravação complementar demonstra alternativa de transcrição acessível somente pelo teclado. A classificação original `SB` foi mantida na matriz de resultados, com a divergência metodológica descrita na análise.

**Nome do arquivo:** na pasta recebida, T3 está identificado como [M8_A1_Piloto_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T3_FL3.mp4). O nome do arquivo foi preservado.

<a id="registro-m9"></a>

## 4. Registro de M9 — leitores de tela (Formulário F5)

Leitores e ambientes: NVDA 2026.3.1/Chrome/Windows (A1), VoiceOver/Safari/macOS (A3) e Orca 46.1/Firefox/Ubuntu (A4). A coluna de anúncio distingue fala efetiva do leitor de observações visuais; sem transcrição literal, registra-se apenas o comportamento sustentado pelos relatos. **As 11 linhas originais de A3 foram preservadas.**

| ID | Tarefa | Etapa | O que foi anunciado / interação | Observação | Barreira | Evidência |
|---|---|---|---|---|---|---|
| `M9-A1-T1-E1` | `T1` | Localizar curso | Curso localizado pelo NVDA | Anúncios funcionais de navegação conforme o ensaio, sem transcrição literal completa disponível | — | [M9_A1_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T1_FL1.mp4) |
| `M9-A1-T1-E2` | `T1` | Abrir curso | Acesso realizado com o NVDA | Controles navegáveis e identificados pelo leitor | — | [M9_A1_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T1_FL1.mp4) |
| `M9-A1-T1-E3` | `T1` | Abrir primeira unidade | Lista da unidade acessada | Navegação por estrutura/rótulos do NVDA concluída | — | [M9_A1_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T1_FL1.mp4) |
| `M9-A1-T2-E1` | `T2` | Abrir videoaula | Videoaula acessada | Informações de navegação identificadas pelo NVDA | — | [M9_A1_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T2_FL2.mp4) |
| `M9-A1-T2-E2` | `T2` | Reproduzir | Reprodução iniciada | Sobreposição dos anúncios do NVDA com o áudio da videoaula | `B-11` | [M9_A1_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T2_FL2.mp4) |
| `M9-A1-T2-E3` | `T2` | Pausar | Reprodução pausada | Persistência de dificuldade de escuta durante a interação | `B-11` | [M9_A1_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T2_FL2.mp4) |
| `M9-A1-T2-E4` | `T2` | Legenda/transcrição | Etapa concluída no ensaio | Sobreposição sonora afetou a clareza dos anúncios | `B-11` | [M9_A1_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T2_FL2.mp4) |
| `M9-A1-T3-E1` | `T3` | Abrir exercício | Exercício acessado utilizando NVDA | Leitor anunciou elementos estruturais; enunciado em tabela demandou navegação por comandos próprios | — | [M9_A1_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T3_FL3.mp4) |
| `M9-A1-T3-E2` | `T3` | Solicitar dica, quando disponível | Dica não individualizada no relato final | Sem transcrição literal do anúncio | — | [M9_A1_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T3_FL3.mp4) |
| `M9-A1-T3-E3` | `T3` | Selecionar resposta | Comandos de navegação específicos do NVDA permitiram chegar às alternativas SIM/NÃO | Rótulos podem ser soletrados; a navegação exclusivamente por Tab havia falhado em M8 | — | [M9_A1_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T3_FL3.mp4) |
| `M9-A1-T3-E4` | `T3` | Enviar resposta | Resposta enviada, com retorno visual *Bom trabalho!* | Não se atribui anúncio literal do retorno ao NVDA sem comprovação de áudio | — | [M9_A1_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T3_FL3.mp4) |
| `M9-A3-T1-E1` | `T1` | Localizar o curso | Rotor (VO+U), lista de links: "Pular para o conteúdo principal", "Cursos", "Ver tudo (10)", "Números: sistema de numeração decimal" e demais unidades | Nomes dos links claros. O título "Matemática EF: 6º Ano" não é anunciado na lista de links, e "Números: sistema de numeração decimal" aparece duas vezes sem indicar o curso; foi escolhida a primeira ocorrência | --- | [`AC-20261122-02_M9-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T1.mov) |
| `M9-A3-T1-E2` | `T1` | Abrir o curso | --- | O curso é acessado pela unidade, como em `M8` | --- | [`AC-20261122-02_M9-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T1.mov) |
| `M9-A3-T1-E3` | `T1` | Abrir a primeira unidade | Nenhum anúncio após o Enter; o cursor do VoiceOver para em um elemento vazio acima de "Sobre esta unidade". Com VO+seta, a leitura fica nos quadrados da barra de progresso da unidade, lidos um a um e soletrados | A mudança de página não é anunciada e o cursor do VoiceOver não avança da barra de progresso até "Sobre esta unidade" e às aulas. A avaliadora consultou a tela para entender o estado da página | `B-04`, `B-05` | [`AC-20261122-02_M9-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T1.mov), [`AC-20261122-02_M9-A3-T1-verificacao`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T1-verificacao.mov) |
| `M9-A3-T2-E1` | `T2` | Abrir a videoaula | Nenhum anúncio após o Enter no link "História dos números" do rotor. Ao reabrir o rotor, o link do vídeo é indicado como página atual | A página do vídeo abre, mas a mudança não é anunciada; a avaliadora confirmou a localização pelo rotor | `B-04` | [`AC-20261122-02_M9-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T2.mov) |
| `M9-A3-T2-E2` | `T2` | Iniciar a reprodução | Com VO+seta para a direita, a leitura percorre a navegação lateral com as demais aulas, sem chegar ao player | Espaço e VO+seta não levam ao vídeo; não foi possível iniciar a reprodução | `B-06` | [`AC-20261122-02_M9-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T2.mov) |
| `M9-A3-T2-E3` | `T2` | Pausar | --- | Etapa não alcançada | `B-06` | [`AC-20261122-02_M9-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T2.mov) |
| `M9-A3-T2-E4` | `T2` | Ativar legenda ou transcrição | "Sobre" e "Transcrição" não foram anunciados | Etapa não alcançada. A avaliadora consultou a tela no fim para confirmar onde estava; sem uso do **trackpad** | `B-06` | [`AC-20261122-02_M9-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T2.mov) |
| `M9-A3-T3-E1` | `T3` | Abrir o exercício | "Vamos lá" anunciado e acionado | A pergunta sorteada foi de digitar: escrever XXXI na forma decimal | --- | [`AC-20261122-02_M9-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T3.mov) |
| `M9-A3-T3-E2` | `T3` | Solicitar a dica | Botão de dica alcançado com Tab e acionado após o retorno da resposta; o texto da dica não foi lido | A dica aparece na tela, mas o conteúdo não é anunciado | `B-08` | [`AC-20261122-02_M9-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T3.mov) |
| `M9-A3-T3-E3` | `T3` | Selecionar a resposta de teste | Campo anunciado como caixa de texto para digitar a resposta; o enunciado "Escreva o número na forma decimal" e a expressão "XXXI" não foram lidos | Sem o enunciado, a avaliadora digitou uma resposta sem saber a pergunta (122) | `B-07` | [`AC-20261122-02_M9-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T3.mov) |
| `M9-A3-T3-E4` | `T3` | Enviar e ouvir o retorno | Após "Verificar", anunciou "Não é dessa vez" | Retorno da resposta anunciado, o que conclui a tarefa somente pelo áudio. A avaliadora consultou a tela depois do retorno e da tentativa de ouvir a dica; sem uso do **trackpad** | --- | [`AC-20261122-02_M9-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T3.mov) |
| `M9-A4-T1-E1` | `T1` | Localizar curso | Curso localizado com Orca | Navegação estrutural do leitor permitiu identificar o curso | — | [M9_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T1_FL1.webm) |
| `M9-A4-T1-E2` | `T1` | Abrir curso | Curso acessado com Orca | Estado de navegação concluído | — | [M9_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T1_FL1.webm) |
| `M9-A4-T1-E3` | `T1` | Abrir primeira unidade | Lista de aulas da unidade acessada | Resultado classificado `S` na coleta | — | [M9_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T1_FL1.webm) |
| `M9-A4-T2-E1` | `T2` | Abrir videoaula | Videoaula localizada e aberta | Leitor ativo e interagindo com a página | — | [M9_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T2_FL2.webm) |
| `M9-A4-T2-E2` | `T2` | Reproduzir | Reprodução iniciada | Sobreposição do áudio de aula e anúncios do Orca | `B-12` | [M9_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T2_FL2.webm) |
| `M9-A4-T2-E3` | `T2` | Pausar | Reprodução pausada | Clareza do leitor prejudicada durante o vídeo | `B-12` | [M9_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T2_FL2.webm) |
| `M9-A4-T2-E4` | `T2` | Legenda/transcrição | Etapa relatada como concluída | Sobreposição de áudio persistiu como dificuldade não impeditiva | `B-12` | [M9_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T2_FL2.webm) |
| `M9-A4-T3-E1` | `T3` | Abrir exercício | Exercício acessado | Enunciado fragmentado ou soletrado, dificultando a compreensão | `B-14` | [M9_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T3_FL3.webm) |
| `M9-A4-T3-E2` | `T3` | Solicitar dica, quando disponível | Etapa opcional não individualizada na gravação | Sem anúncio literal documentado | — | [M9_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T3_FL3.webm) |
| `M9-A4-T3-E3` | `T3` | Selecionar resposta | Alternativas SIM/NÃO não puderam ser acionadas pelos comandos usados com Orca | Nomes das opções foram pronunciados letra a letra | `B-13`, `B-14` | [M9_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T3_FL3.webm) |
| `M9-A4-T3-E4` | `T3` | Enviar resposta | Não foi possível atingir o envio | Impedimento em controle essencial | `B-13` | [M9_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T3_FL3.webm) |

*Tabela 8. Registro das etapas de M9 (A1, A3 e A4). Fonte: registros de [Enzo Menali](https://github.com/menali17) e [Luisa de Souza](https://github.com/luisa12ll).*

**Nota sobre `M9-A3-T2`:** a videoaula escolhida durante a sessão foi diferente da videoaula-base. O impedimento registrado refere-se à navegação/ativação do player com VoiceOver; não se considera a escolha de conteúdo, por si só, uma falha da plataforma.

**Nota sobre `M9-A3-T3`:** a avaliadora conseguiu enviar a resposta e ouvir *Não é dessa vez*, mas o VoiceOver não anunciou a expressão `XXXI` nem o enunciado. O registro original a classifica como `SB`, e essa classificação foi **preservada**, com análise adicional do requisito de percepção de informação essencial na seção 9.

**Nome do arquivo:** na pasta recebida, T2 está identificado como [M9_A1_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T2_FL2.mp4).

<a id="registro-m10"></a>

## 5. Registro de M10 — ampliação de 200% (Formulário F5)

**Condição:** A1, Chrome em 1366 × 768, zoom do navegador em 200%. A tarefa poderia ser conduzida com mouse e teclado, sem voltar ao zoom padrão. As capturas pertencem ao pacote `Coletas de Qualidade.zip`.

| ID | Tarefa | Etapa | Observação | Barreira | Evidência |
|---|---|---|---|---|---|
| `M10-A1-T1-E1` | `T1` | Localizar curso | Curso localizado a 200%, sem redução de zoom | — | [M10_A1_T1_02_MeusCursos.png](evidencias/acessibilidade/A1/M10_A1_T1_02_MeusCursos.png) |
| `M10-A1-T1-E2` | `T1` | Abrir curso | Curso acessado preservando ampliação | — | [M10_A1_T1_03_Unidade1.png](evidencias/acessibilidade/A1/M10_A1_T1_03_Unidade1.png) |
| `M10-A1-T1-E3` | `T1` | Abrir unidade | Lista de aulas da primeira unidade exibida e acessada | — | [M10_A1_T1_04_ListaDeAulas.png](evidencias/acessibilidade/A1/M10_A1_T1_04_ListaDeAulas.png) |
| `M10-A1-T2-E1` | `T2` | Abrir videoaula | Videoaula *História dos números* acessada | — | [M10_A1_T2_01_Videoaula.png](evidencias/acessibilidade/A1/M10_A1_T2_01_Videoaula.png) |
| `M10-A1-T2-E2` | `T2` | Iniciar reprodução | Reprodução iniciada; enquadramento do vídeo limitado a 200% | `B-15` | [M10_A1_T2_02_Reproducao.png](evidencias/acessibilidade/A1/M10_A1_T2_02_Reproducao.png) |
| `M10-A1-T2-E3` | `T2` | Pausar | Etapa de pausa concluída conforme relato; não há captura isolada com esse nome | `B-15` | [M10_A1_T2_02_Reproducao.png](evidencias/acessibilidade/A1/M10_A1_T2_02_Reproducao.png) |
| `M10-A1-T2-E4` | `T2` | Legenda/transcrição | Legendas visíveis e acessíveis | — | [M10_A1_T2_02_Legendas.png](evidencias/acessibilidade/A1/M10_A1_T2_02_Legendas.png) |
| `M10-A1-T3-E1` | `T3` | Abrir exercício | Exercício aberto com zoom de 200% | — | [M10_A1_T3_01_Exercicio.png](evidencias/acessibilidade/A1/M10_A1_T3_01_Exercicio.png) |
| `M10-A1-T3-E2` | `T3` | Dica, quando disponível | Ação de dica não capturada isoladamente; não imputar falha a recurso opcional | — | [M10_A1_T3_01_Exercicio.png](evidencias/acessibilidade/A1/M10_A1_T3_01_Exercicio.png) |
| `M10-A1-T3-E3` | `T3` | Selecionar resposta | Resposta selecionada | — | [M10_A1_T3_02_Resposta.png](evidencias/acessibilidade/A1/M10_A1_T3_02_Resposta.png) |
| `M10-A1-T3-E4` | `T3` | Enviar e verificar retorno | Retorno *Bom trabalho!* exibido | — | [M10_A1_T3_03_Retorno.png](evidencias/acessibilidade/A1/M10_A1_T3_03_Retorno.png) |

*Tabela 9. Registro das etapas de M10 em A1. Fonte: execução e capturas de [Enzo Menali](https://github.com/menali17).*

**Resultado por tarefa:** `M10-A1-T1 = S`; `M10-A1-T2 = SB` (B-15); `M10-A1-T3 = S`. As três tarefas foram concluídas. O vídeo apresentou enquadramento limitado, mas os controles utilizados permaneceram operáveis; o percentual funcional não constitui, isoladamente, certificação WCAG 1.4.4.

<a id="registro-m11"></a>

## 6. Registro de M11 — contraste textual e alto contraste

### 6.1 Alto contraste — Formulário F5

**Condição:** A1/Windows, tema de contraste **Céu noturno** ativado durante toda a execução de T1–T3. A conclusão funcional é registrada separadamente da medição textual.

| ID | Tarefa | Etapa | Observação | Barreira | Evidência |
|---|---|---|---|---|---|
| `M11-A1-T1-E1` | `T1` | Localizar curso | Página inicial com tema Céu noturno; curso localizado | — | [M11_A1_T1_01_PaginaInicial.png](evidencias/acessibilidade/A1/M11_A1_T1_01_PaginaInicial.png) |
| `M11-A1-T1-E2` | `T1` | Abrir curso | Curso aberto com tema ativo | — | [M11_A1_T1_02_Curso.png](evidencias/acessibilidade/A1/M11_A1_T1_02_Curso.png) |
| `M11-A1-T1-E3` | `T1` | Abrir unidade | Lista de aulas exibida | — | [M11_A1_T1_03_ListaDeAulas.png](evidencias/acessibilidade/A1/M11_A1_T1_03_ListaDeAulas.png) |
| `M11-A1-T2-E1` | `T2` | Abrir videoaula | Página da videoaula aberta com tema ativo | — | [M11_A1_T2_01_Videoaula.png](evidencias/acessibilidade/A1/M11_A1_T2_01_Videoaula.png) |
| `M11-A1-T2-E2` | `T2` | Reproduzir | Vídeo iniciado | — | [M11_A1_T2_02_Reproducao.png](evidencias/acessibilidade/A1/M11_A1_T2_02_Reproducao.png) |
| `M11-A1-T2-E3` | `T2` | Pausar | Pausa concluída conforme relato; sem captura isolada | — | [M11_A1_T2_02_Reproducao.png](evidencias/acessibilidade/A1/M11_A1_T2_02_Reproducao.png) |
| `M11-A1-T2-E4` | `T2` | Legenda/transcrição | Legendas visíveis na captura | — | [M11_A1_T2_03_Legendas.png](evidencias/acessibilidade/A1/M11_A1_T2_03_Legendas.png) |
| `M11-A1-T3-E1` | `T3` | Abrir exercício | Exercício acessado; registro visual associado às capturas da resposta | — | [M11_A1_T3_02_Resposta.png](evidencias/acessibilidade/A1/M11_A1_T3_02_Resposta.png) |
| `M11-A1-T3-E2` | `T3` | Dica, quando disponível | Ação de dica não capturada isoladamente | — | [M11_A1_T3_02_Resposta.png](evidencias/acessibilidade/A1/M11_A1_T3_02_Resposta.png) |
| `M11-A1-T3-E3` | `T3` | Selecionar resposta | Resposta selecionada com tema ativo | — | [M11_A1_T3_02_Resposta.png](evidencias/acessibilidade/A1/M11_A1_T3_02_Resposta.png) |
| `M11-A1-T3-E4` | `T3` | Enviar resposta | Retorno *Bom trabalho!* exibido | — | [M11_A1_T3_03_Retorno.png](evidencias/acessibilidade/A1/M11_A1_T3_03_Retorno.png) |
| `M11-A1-T3-E5` | `T3` | Inspecionar ícone Recomeçar | Ícone pouco perceptível sem hover, reaparecendo com o ponteiro | `B-18` | [M11_A1_T3_04_IconeRecomecar.png.png](evidencias/acessibilidade/A1/M11_A1_T3_04_IconeRecomecar.png.png) |

*Tabela 10. Registro funcional de alto contraste em A1. Fonte: execução e capturas de [Enzo Menali](https://github.com/menali17).*

**Resultado por tarefa:** `M11-A1-T1 = S`; `M11-A1-T2 = S`; `M11-A1-T3 = SB` (B-18). Conclusão de **3/3 tarefas (100%)**, sem desativação do tema durante a execução.

### 6.2 Contraste textual — Formulário F6

O F6 da Fase 3 exige página, elemento, essencialidade, cores, tamanho, razão, conformidade AA/AAA e evidência. As **11 razões numéricas abaixo** foram reunidas nas anotações de coleta; os relatórios JSON/HTML enviados **não comprovam individualmente todas as 11 medições manuais**. Onde não existem valores brutos de cor/tamanho confirmados, consta `NR` (não registrado na evidência recebida). Os julgamentos AA/AAA dessa amostra refletem os registros manuais e a **hipótese de texto comum nos elementos com tamanho não aferido**, não uma medição posteriormente inventada.

| Página atribuída | Elemento | Essencialidade no roteiro | Cor do texto / fundo | Tamanho | Razão anotada | AA (anotação) | AAA (anotação) | Origem e evidência |
|---|---|---|---|---|---:|---|---|---|
| P1 | Matemática EF: 6º Ano | Referência para T1 | NR / NR | NR | 15,5:1 | Sim | Sim | Anotação manual; [foto_p1.png](evidencias/acessibilidade/A1/foto_p1.png) é captura de página, não leitura CCA |
| P1 | Números: sistema de numeração decimal | **Sim — link necessário em T1**, a confirmar a aplicabilidade exata do limite por tamanho | NR / NR | NR | **4,0:1** | **Não, se texto comum** | Não, se texto comum | Anotação manual B-16, sem captura específica de leitura CCA |
| P1 | Retomar | Contextual/controle de navegação | NR / NR | NR | 4,9:1 | Sim | Não, se texto comum | Anotação manual |
| P2 | Título do curso | Referência para T1 | NR / NR | NR | 16,1:1 | Sim | Sim | Anotação manual |
| P2 | **A SEGUIR!** | Controle de progressão; verificar essencialidade específica | **`#686D75` / `#E7EFF8`** | **12 px negrito** | **4,48:1** | **Não** | **Não** | **Lighthouse/axe-core**, B-17: [P2_Lighthouse_R1.json](evidencias/acessibilidade/A1/P2_Lighthouse_R1.json), [P2_Axe_R1_Contraste_Aseguir.png](evidencias/acessibilidade/A1/P2_Axe_R1_Contraste_Aseguir.png) |
| P3 | Título da unidade | Referência para T1/T2 | NR / NR | NR | 15,0:1 | Sim | Sim | Anotação manual; auditoria P3 repetiu a URL de P2 |
| P3 | História dos números | Referência para T2 | NR / NR | NR | 4,7:1 | Sim | Não, se texto comum | Anotação manual |
| P4 | Título da videoaula | Referência para T2 | NR / NR | NR | 16,2:1 | Sim | Sim | Anotação manual |
| P5 | Enunciado do exercício | Informação necessária em T3 | NR / NR | NR | 15,5:1 | Sim | Sim | Anotação manual |
| P5 | Verificar | Controle essencial para envio de T3 | NR / NR | NR | 4,8:1 | Sim | Não, se texto comum | Anotação manual |
| P6 | Bom trabalho! | Retorno de T3 | NR / NR | NR | 16,1:1 | Sim | Sim | Anotação manual |

*Tabela 11. Checklist consolidado F6 de M11. Fonte: anotações manuais de [Enzo Menali](https://github.com/menali17) e relatórios de inspeção enviados no ZIP.*

**Cálculo das anotações:** `E_a = 11`; `E_c(AA) = 9` e `E_c(AAA) = 6`, equivalentes a **81,82% AA** e **54,55% AAA** no conjunto anotado. Esses percentuais são apresentados como **consolidação das anotações**, não como auditoria automatizada completa. As classificações dos elementos com tamanho não documentado dependem das premissas assinaladas.

**Achado automatizado confirmado:** o texto **A SEGUIR!** apresentou aproximadamente **4,48:1**, com fonte de **12 px em negrito**, abaixo do mínimo **4,5:1** para texto comum (WCAG 2.1, 1.4.3 AA). As auditorias identificadas como P2 e P3 no pacote utilizaram a **mesma URL**, de modo que devem ser descritas como duas detecções do mesmo problema e não como falhas independentes em páginas distintas.

**Avaliação técnica:** o tema de alto contraste não corrige retroativamente os problemas medidos no tema padrão; os dois resultados são relatados lado a lado. A nota da parte textual exige avaliar o efeito dos elementos não conformes sobre informação essencial conforme os [critérios de julgamento da Fase 2](../fase-2/criterios-julgamento.md#4-criterios-tecnicos-de-acessibilidade).

<a id="registro-resultados"></a>

## 7. Resultado por combinação

A matriz abaixo registra **24 combinações de tarefa e condição**: nove de M8, nove de M9, três de M10 e três do teste funcional de alto contraste de M11. **Medições textuais de M11 não são tarefas e permanecem na Tabela 11.** As seis linhas de A3 mantêm as classificações e URLs originais da avaliadora.

| ID | Sessão | Data | Executor / observador | Classificação | Barreiras | Evidência |
|---|---|---|---|:---:|---|---|
| `M8-A1-T1` | `AC-20261117-01` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M8_A1_Piloto_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T1_FL1.mp4) |
| `M8-A1-T2` | `AC-20261117-01` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M8_A1_Piloto_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T2_FL2.mp4) |
| `M8-A1-T3` | `AC-20261117-01` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `IMP` | `B-09` | [M8_A1_Piloto_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T3_FL3.mp4) |
| `M8-A3-T1` | `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `S` | --- | [`AC-20261121-01_M8-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T1.mov) |
| `M8-A3-T2` | `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `SB` | `B-01`, `B-02`, `B-03` | [`AC-20261121-01_M8-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2.mov) |
| `M8-A3-T3` | `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `SB` | `B-03` | [`AC-20261121-01_M8-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T3.mov) |
| `M8-A4-T1` | `AC-20261121-03` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M8_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T1_FL1.webm) |
| `M8-A4-T2` | `AC-20261121-03` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M8_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T2_FL2.webm) |
| `M8-A4-T3` | `AC-20261121-03` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `IMP` | `B-10` | [M8_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T3_FL3.webm) |
| `M9-A1-T1` | `AC-20261121-02` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M9_A1_T1_FL1.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T1_FL1.mp4) |
| `M9-A1-T2` | `AC-20261121-02` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `SB` | `B-11` | [M9_A1_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T2_FL2.mp4) |
| `M9-A1-T3` | `AC-20261121-02` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M9_A1_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T3_FL3.mp4) |
| `M9-A3-T1` | `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `IMP` | `B-04`, `B-05` | [`AC-20261122-02_M9-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T1.mov) |
| `M9-A3-T2` | `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `IMP` | `B-04`, `B-06` | [`AC-20261122-02_M9-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T2.mov) |
| `M9-A3-T3` | `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `SB` | `B-07`, `B-08` | [`AC-20261122-02_M9-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T3.mov) |
| `M9-A4-T1` | `AC-20261121-04` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M9_A4_T1_FL1.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T1_FL1.webm) |
| `M9-A4-T2` | `AC-20261121-04` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `SB` | `B-12` | [M9_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T2_FL2.webm) |
| `M9-A4-T3` | `AC-20261121-04` | 21/11/2026 | [Enzo Menali](https://github.com/menali17) | `IMP` | B-13, B-14 | [M9_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T3_FL3.webm) |
| `M10-A1-T1` | `AC-20261117-02` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M10_A1_T1_04_ListaDeAulas.png](evidencias/acessibilidade/A1/M10_A1_T1_04_ListaDeAulas.png) |
| `M10-A1-T2` | `AC-20261117-02` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `SB` | `B-15` | [M10_A1_T2_02_Legendas.png](evidencias/acessibilidade/A1/M10_A1_T2_02_Legendas.png) |
| `M10-A1-T3` | `AC-20261117-02` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M10_A1_T3_03_Retorno.png](evidencias/acessibilidade/A1/M10_A1_T3_03_Retorno.png) |
| `M11-A1-T1` | `AC-20261117-04` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M11_A1_T1_03_ListaDeAulas.png](evidencias/acessibilidade/A1/M11_A1_T1_03_ListaDeAulas.png) |
| `M11-A1-T2` | `AC-20261117-04` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `S` | — | [M11_A1_T2_03_Legendas.png](evidencias/acessibilidade/A1/M11_A1_T2_03_Legendas.png) |
| `M11-A1-T3` | `AC-20261117-04` | 17/11/2026 | [Enzo Menali](https://github.com/menali17) | `SB` | `B-18` | [M11_A1_T3_03_Retorno.png](evidencias/acessibilidade/A1/M11_A1_T3_03_Retorno.png) |

*Tabela 12. Resultado por combinação. Fonte: registros das sessões e evidências consolidadas.*

**Gravações A3 no repositório:** [pasta A3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/tree/main/assets/dados/fase4/acessibilidade/A3), [pasta M8](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/tree/main/assets/dados/fase4/acessibilidade/A3/M8) e [pasta M9](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/tree/main/assets/dados/fase4/acessibilidade/A3/M9). Evidências adicionais: [preparação de A3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/AC_Preparacao-A3.mov) e [preparação do VoiceOver](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_Preparacao-VoiceOver.mov).

**Uso dos resultados:** a classificação `SB` de `M9-A3-T3` foi preservada para manter a fidelidade ao documento original. A nota e as conclusões de Q8 são as mesmas se a combinação for reclassificada como impedimento: 6/9 (66,67%) ou 5/9 (55,56%), ambos abaixo da meta.

<a id="registro-barreiras"></a>

## 8. Registro das barreiras

**Gravidade adotada:** *bloqueia* (impede etapa essencial), *dificulta* (demanda contorno ou reduz compreensão) e *incomoda* (não altera a conclusão). A associação WCAG é **indicativa e específica do achado observado**, não uma declaração de descumprimento global da plataforma.

| ID | Combinação e etapa | Passos para reproduzir | Comportamento esperado | Comportamento observado | Critério WCAG | Gravidade | Evidência |
|---|---|---|---|---|---|:---:|---|
| `B-01` | `M8-A3-T2`, etapa 4 | Abrir "História dos números", iniciar e pausar com Espaço e pressionar Tab sem mover o ponteiro | Botões CC e configurações recebem foco pelo teclado | Os controles só aparecem com o ponteiro sobre o vídeo; sem ele, ficam ocultos e o Tab não os alcança, impedindo ativar a legenda pelo teclado. A transcrição pelas abas é alternativa acessível | 2.1.1 | Dificulta | [`AC-20261121-01_M8-A3-T2-verificacao`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2-verificacao.mov) |
| `B-02` | `M8-A3-T2`, etapa 4 | Com os controles visíveis, levar o foco ao botão de configurações e pressionar Enter | Esc fecha o menu e o foco volta ao player | Tab, Shift+Tab, setas e Esc não saem do menu; foi preciso usar o **trackpad** | 2.1.2 | Dificulta | [`AC-20261121-01_M8-A3-T2-verificacao`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2-verificacao.mov) |
| `B-03` | `M8-A3-T2`, etapas 1 e 2; `M8-A3-T3`, etapas 1 e 3 | Da barra de endereço, avançar com Tab até a videoaula, o player, o botão "Vamos lá" e a primeira resposta | Chegar ao conteúdo da tarefa com poucas teclas | 63 Tabs até a videoaula, 40 até o player, 34 até "Vamos lá" e 45 até a primeira resposta. A página tem o link "Pular para o conteúdo principal", identificado no rotor do VoiceOver | --- | Incomoda | [`AC-20261121-01_M8-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T2.mov), [`AC-20261121-01_M8-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M8/AC-20261121-01_M8-A3-T3.mov) |
| `B-04` | `M9-A3-T1`, etapa 3; `M9-A3-T2`, etapa 1 | Com o VoiceOver ativo, abrir pelo rotor a unidade "Números: sistema de numeração decimal" | Anúncio da nova página e foco no início do conteúdo | Nenhum anúncio; o cursor do VoiceOver fica em um elemento vazio, sem nome, acima de "Sobre esta unidade" | 2.4.3, 4.1.2 | Dificulta | [`AC-20261122-02_M9-A3-T1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T1.mov), [`AC-20261122-02_M9-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T2.mov) |
| `B-05` | `M9-A3-T1`, etapa 3 | Na página da unidade, avançar com VO+seta para a direita a partir do topo do conteúdo | Leitura resumida do progresso e passagem para "Sobre esta unidade" e a lista de aulas | Os quadrados da barra de progresso são lidos um a um e soletrados, e o cursor não avança até o conteúdo da unidade, impedindo ouvir a lista de aulas | 1.3.1, 4.1.2 | Bloqueia | [`AC-20261122-02_M9-A3-T1-verificacao`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T1-verificacao.mov) |
| `B-06` | `M9-A3-T2`, etapas 2 a 4 | Com o VoiceOver ativo, abrir "História dos números" pelo rotor e avançar com VO+seta para a direita ou Espaço | O cursor do VoiceOver alcança o player, anuncia os controles de reprodução e chega às abas "Sobre" e "Transcrição" | O cursor percorre a navegação lateral com as demais aulas e não alcança o player nem as abas; não é possível iniciar o vídeo nem abrir a transcrição | 2.1.1, 4.1.2 | Bloqueia | [`AC-20261122-02_M9-A3-T2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T2.mov) |
| `B-07` | `M9-A3-T3`, etapa 3 | Com o VoiceOver ativo, abrir o exercício, acionar "Vamos lá" e levar o foco ao campo de resposta | O campo é anunciado com o enunciado e a expressão a converter | O campo é anunciado apenas como caixa de texto; o enunciado e a expressão matemática não são lidos, e não é possível saber o que responder | 1.3.1, 3.3.2 | Dificulta | [`AC-20261122-02_M9-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T3.mov) |
| `B-08` | `M9-A3-T3`, etapa 2 | Com o VoiceOver ativo, levar o foco ao botão de dica com Tab e acioná-lo | O texto da dica é anunciado ou o foco vai para ele | A dica aparece na tela, mas não é anunciada | 4.1.3 | Dificulta | [`AC-20261122-02_M9-A3-T3`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A3/M9/AC-20261122-02_M9-A3-T3.mov) |
| `B-09` | `M8-A1-T3-E3/E4` | No Chrome/Windows, abrir o exercício de T3; percorrer alternativas SIM/NÃO usando Tab, Shift+Tab, setas, Enter e Espaço | Alternativas recebem foco e podem ser escolhidas pelo teclado | Opções não foram alcançadas/acionadas, impossibilitando envio da resposta | 2.1.1 | Bloqueia | [M8_A1_Piloto_T3_FL3.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M8_A1_Piloto_T3_FL3.mp4) (nome do arquivo recebido; T3) |
| `B-10` | `M8-A4-T3-E3/E4` | No Firefox/Ubuntu, abrir T3 e percorrer SIM/NÃO com Tab, Shift+Tab, setas e Espaço | Alternativas acessíveis e acionáveis | As opções não puderam ser selecionadas, impedindo envio | 2.1.1 | Bloqueia | [M8_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M8_A4_T3_FL3.webm) |
| `B-11` | `M9-A1-T2-E2/E4` | Com NVDA ativo, abrir T2 e iniciar vídeo com anúncios do leitor habilitados | Controles e mensagens essenciais permanecem compreensíveis | Áudio do conteúdo e voz do NVDA se sobrepuseram | 1.4.2 (referência de áudio; relação indicativa) | Dificulta | [M9_A1_T2_FL2.mp4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A1/M9_A1_T2_FL2.mp4) (nome do arquivo recebido; T2) |
| `B-12` | `M9-A4-T2-E2/E4` | Com Orca ativo, iniciar reprodução da videoaula | Fala do leitor identificável durante a interação | Fala do Orca sobreposta ao áudio do conteúdo | 1.4.2 (relação indicativa) | Dificulta | [M9_A4_T2_FL2.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T2_FL2.webm) |
| `B-13` | `M9-A4-T3-E3/E4` | Percorrer controles de T3 com Orca/Firefox e tentar selecionar SIM/NÃO | Controle anunciado e acionável com tecnologia assistiva | Alternativas inacessíveis pelos comandos utilizados e impossibilidade de enviar | 2.1.1, 4.1.2 (indícios a confirmar) | Bloqueia | [M9_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T3_FL3.webm) |
| `B-14` | `M9-A4-T3-E1/E3` | Navegar pelo enunciado e alternativas de T3 usando Orca | Leitura inteligível dos enunciados/alternativas | Conteúdo fragmentado, inclusive soletração de alternativas | 1.3.1, 4.1.2 (associação indicativa) | Dificulta | [M9_A4_T3_FL3.webm](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/assets/dados/fase4/acessibilidade/A4/M9_A4_T3_FL3.webm) |
| `B-15` | `M10-A1-T2-E2` | Ajustar Chrome para 200%, abrir e reproduzir a videoaula | Conteúdo e controles essenciais preservados | Área visível do reprodutor ficou limitada; tarefa ainda concluída | 1.4.4 (análise funcional; não é violação comprovada) | Incomoda | [M10_A1_T2_02_Reproducao.png](evidencias/acessibilidade/A1/M10_A1_T2_02_Reproducao.png) |
| `B-16` | `M11-A1/P1` | Inspecionar o link *Números: sistema de numeração decimal* com CCA no tema padrão | Contraste mínimo compatível com tamanho de fonte | Razão manual anotada de **4,0:1**; captura numérica específica não localizada | 1.4.3 (condicional ao tamanho) | Dificulta | Registro manual de F6; [foto_p1.png](evidencias/acessibilidade/A1/foto_p1.png) apenas para contexto |
| `B-17` | `M11-A1/P2–P3` | Inspecionar o texto *A SEGUIR!* e executar contraste do Lighthouse/axe | Texto comum com razão mínima AA de 4,5:1 | Razão **4,48:1**, com texto de 12 px negrito e cores `#686D75`/`#E7EFF8`; duas detecções da mesma URL | 1.4.3 | Dificulta | [P2_Axe_R1_Contraste_Aseguir.png](evidencias/acessibilidade/A1/P2_Axe_R1_Contraste_Aseguir.png), [P2_Lighthouse_R1.json](evidencias/acessibilidade/A1/P2_Lighthouse_R1.json), [P3_Lighthouse_R1.json](evidencias/acessibilidade/A1/P3_Lighthouse_R1.json) |
| `B-18` | `M11-A1-T3-E5` | Com tema Céu noturno, observar controle Recomeçar antes de posicionar o mouse | Ícone perceptível mesmo sem hover | Ícone quase indistinguível sem hover, tornando-se perceptível com ponteiro sobre ele | 1.4.11 (associação indicativa para contraste não textual) | Dificulta | [M11_A1_T3_04_IconeRecomecar.png.png](evidencias/acessibilidade/A1/M11_A1_T3_04_IconeRecomecar.png.png) |

*Tabela 13. Barreiras B-01 a B-18. As barreiras B-01 a B-08 foram preservadas da versão 1.0 de Luisa de Souza; B-09 a B-18 foram consolidadas com base nas observações de [Enzo Menali](https://github.com/menali17).*

**Observação:** B-11 e B-12 descrevem dificuldades de sobreposição de áudio observadas nos testes. Sem ensaio adicional específico, não se atribui automaticamente a origem à implementação da Khan Academy ou ao sistema operacional. Em B-16, a razão de 4,0:1 foi anotada manualmente e não recebe o mesmo grau de comprovação automatizada de B-17.

<a id="registro-julgamento"></a>

## 9. Cálculo e julgamento de M8–M11, Q7–Q10 e H7–H10

### 9.1 Escalas e fórmulas

Para M8, M9 e M10:

`Taxa de conclusão = 100 × A / N`, com `A = S + SB` e `N = S + SB + F + IMP` entre as combinações válidas (`X` não é contabilizada).

Na [Fase 2](../fase-2/criterios-julgamento.md#2-metricas-percentuais), os níveis são **3 = 100%**, **2 = de 90% até menos de 100%**, **1 = de 75% até menos de 90%** e **0 = menos de 75%**. Para aprovar uma questão, além da nota mínima 2, não pode haver impedimento de tarefa essencial.

| Métrica | S | SB | IMP | F | Total válido | Conclusões válidas | Resultado | Nota |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **M8** — teclado | 5 | 2 | 2 | 0 | **9** | **7** | **77,78%** | **1 — Mínimo aceitável** |
| **M9** — leitor de tela (classificações originais) | 3 | 3 | 3 | 0 | **9** | **6** | **66,67%** | **0 — Inaceitável** |
| **M10** — zoom a 200% | 2 | 1 | 0 | 0 | **3** | **3** | **100%** | **3 — Excelente** |
| **M11** — alto contraste funcional (complementar) | 2 | 1 | 0 | 0 | **3** | **3** | **100%** | **Sem nota percentual isolada para M11** |

*Tabela 14. Contagens, percentuais e notas. Fonte: resultados válidos da Tabela 12 e critérios de julgamento da Fase 2.*

**Verificação aritmética:** `M8 = 7/9 × 100 = 77,78%`; `M9 = 6/9 × 100 = 66,67%`; `M10 = 3/3 × 100 = 100%`; alto contraste `3/3 × 100 = 100%` (indicador complementar de M11).

### 9.2 Contraste textual de M11

Nas **anotações** do F6: `E_a = 11`, `E_c(AA) = 9` (**81,82%**) e `E_c(AAA) = 6` (**54,55%**). O nível Alvo (2) exige que **todos** os textos aplicáveis inspecionados atendam AA; a observação confirmada B-17 impede essa condição. O resultado do tema Céu noturno é relatado separadamente e não substitui a medição textual.

**Nota proposta de M11: 0 — Inaceitável, sob a interpretação de que B-16 compromete o texto do link necessário à tarefa T1 e de que a razão manual de 4,0:1 se aplica a texto comum.** Esse é um **julgamento condicionado e rastreado**, não comprovação independente da razão de 4,0:1 por arquivo do CCA. Caso o link não seja considerado essencial ou a medição não seja aplicável após verificar o tamanho, o critério da Fase 2 prevê **nota 1** se a falha remanescente afetar apenas elementos não essenciais. Em ambos os cenários, **Q10 não atende integralmente ao alvo AA** e **H10 não é sustentada na amostra**, em virtude da falha de contraste textual B-17 confirmada.

### 9.3 Respostas às questões e hipóteses

| Questão / hipótese | Evidência principal | Questão atendida? | Hipótese na amostra |
|---|---|---|---|
| **Q7/H7 — teclado** | M8 7/9 = 77,78%; T3 bloqueada em A1 e A4 (B-09, B-10) | **Não** | **H7 não sustentada**; meta 90% não atingida |
| **Q8/H8 — leitor de tela** | M9 6/9 = 66,67%; impedimentos em A3 e A4 | **Não** | **H8 não sustentada**; meta 90% não atingida |
| **Q9/H9 — ampliação** | M10 3/3 = 100%; sem bloqueio essencial a 200% | **Sim**, no recorte testado | **H9 sustentada na amostra** |
| **Q10/H10 — contraste** | B-17 confirmada; 3/3 tarefas em Céu noturno | **Não integralmente** | **H10 não sustentada**; requisito textual não atendido |

*Tabela 15. Julgamento das questões Q7–Q10 e hipóteses H7–H10.*

**Ressalva de M9/A3/T3:** o registro original `SB` foi preservado, embora a falta de anúncio de informação essencial (B-07) seja metodologicamente relevante. Aplicando leitura estrita da definição de M9, essa combinação poderia ser reclassificada como impedimento, resultando em **5/9 = 55,56%**. Esse cenário alternativo não altera a nota 0 de M9 nem a conclusão negativa de Q8/H8.


### 9.4 Recomendações priorizadas

| Prioridade proposta | Barreiras associadas | Recomendação de melhoria |
|---|---|---|
| **Alta** | B-09, B-10, B-13 | Tornar alternativas SIM/NÃO focáveis, identificáveis e acionáveis por teclado e leitores de tela; verificar HTML semântico, rótulos e gerenciamento de foco. |
| **Alta** | B-05, B-06, B-07, B-08, B-14 | Corrigir ordem e estrutura de leitura para progressão, enunciados, controles de vídeo e dicas; anunciar contexto e mudanças de estado. |
| **Alta** | B-16, B-17 | Adequar contraste dos textos identificados, especialmente links e rótulos de navegação; confirmar tamanhos e estados de interface. |
| **Média** | B-01, B-02, B-04 | Permitir revelar e operar controles do player exclusivamente pelo teclado; garantir saída de menus e anúncio de mudanças de página. |
| **Média** | B-18 | Tornar o ícone Recomeçar perceptível sem depender exclusivamente de hover no tema de contraste. |
| **Baixa/Média** | B-03, B-11, B-12, B-15 | Reduzir navegação excessiva, investigar clareza simultânea de áudio e melhorar o enquadramento do reprodutor com zoom. |

*Tabela 16. Recomendações derivadas das barreiras observadas; prioridades indicativas da avaliação, não classificações automatizadas.*

### 9.5 Síntese analítica

A avaliação demonstrou que a ampliação de 200% preservou as tarefas essenciais do recorte observado no Windows (`M10 = 100%`, nota 3), enquanto a navegação por teclado (`M8 = 77,78%`, nota 1) e o uso de leitores de tela (`M9 = 66,67%`, nota 0 conforme registro original) apresentaram impedimentos importantes. O contraste textual apresentou ao menos uma não conformidade AA confirmada automaticamente, embora os três fluxos tenham sido concluídos com o tema Céu noturno. Assim, **H9 foi sustentada na amostra e H7, H8 e H10 não foram sustentadas**. As conclusões dependem do escopo efetivamente ensaiado e não representam avaliação de todas as páginas, pessoas ou tecnologias assistivas.



## Referências

<a id="s1"></a>

> **[S1]** FCTE/UnB. *Procedimentos de avaliação de acessibilidade e apreensibilidade (M8 a M14)*, Fase 3. [Acessar](../fase-3/procedimentos-acessibilidade-apreensibilidade.md).

<a id="s2"></a>

> **[S2]** FCTE/UnB. *Registro de execuções de adaptabilidade (M6 e M7)*, Fase 4. [Acessar](registro-adaptabilidade.md).

<a id="s3"></a>

> **[S3]** APPLE. *VoiceOver User Guide for Mac*. [Acessar](https://support.apple.com/guide/voiceover/welcome/mac). Acesso registrado em 22 nov. 2026 pela versão original.

<a id="s4"></a>

> **[S4]** FCTE/UnB. *Especificação das métricas M1–M14*, Fase 2. [Acessar](../fase-2/metricas.md).

<a id="s5"></a>

> **[S5]** FCTE/UnB. *Questões e hipóteses Q1–Q11*, Fase 2. [Acessar](../fase-2/questoes-hipoteses.md).

<a id="s6"></a>

> **[S6]** FCTE/UnB. *Níveis de pontuação e critérios de julgamento*, versão 1.5, Fase 2. [Acessar](../fase-2/criterios-julgamento.md).

<a id="s7"></a>

> **[S7]** FCTE/UnB. *Escopo da avaliação*, Fase 1. [Acessar](../fase-1/escopo-da-avaliacao.md).

<a id="s8"></a>

> **[S8]** W3C. *Web Content Accessibility Guidelines (WCAG) 2.1*. [Acessar](https://www.w3.org/TR/WCAG21/).

<a id="s9"></a>

> **[S9]** GOOGLE. *Lighthouse — Chrome for Developers*. [Acessar](https://developer.chrome.com/docs/devtools/lighthouse/).

<a id="s10"></a>

> **[S10]** DEQUE SYSTEMS. *axe-core — Accessibility engine for automated Web UI testing*. [Acessar](https://github.com/dequelabs/axe-core).

*O protocolo da Fase 3 também reúne as referências normativas e de ferramentas para Colour Contrast Analyser, NVDA, Orca e o tema de contraste do Windows.*

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 22/11/2026 | Estrutura de registro M8/M9 e preparação do ambiente A3, com observações, barreiras e evidências da avaliadora. | [Luisa de Souza](https://github.com/luisa12ll) | [Enzo Menali](https://github.com/menali17) |
| 1.1 | 22/11/2026 | Consolidação de A1/A3/A4; M8–M11, F5/F6/F7, resultados, barreiras B-01 a B-18, julgamento Q7–Q10/H7–H10, referências e inventário de evidências para integração posterior. | [Enzo Menali](https://github.com/menali17)| [Luisa de Souza](https://github.com/luisa12ll) |



---
