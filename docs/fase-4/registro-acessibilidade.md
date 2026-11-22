# Registro de execuções de acessibilidade (M8 e M9)

**Versão 1.0**

Esta página reúne os formulários de registro dos testes manuais de acessibilidade definidos em [Procedimentos de avaliação de acessibilidade e apreensibilidade](../fase-3/procedimentos-acessibilidade-apreensibilidade.md) [S1](#s1). As tabelas são preenchidas na Fase 4, por *pull request*, conforme cada execução. Esta versão traz a preparação e as sessões de 21/11/2026 (`M8`) e 22/11/2026 (`M9`) no ambiente [`A3`](#registro-preparacao), com navegação por teclado ([`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado)) e leitor de tela VoiceOver ([`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela)).

**Como preencher.** Mantenha os identificadores das linhas. Use as classificações da [Tabela 5 do procedimento](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#42-classificacao-do-resultado): `S` (sucesso), `SB` (sucesso com barreira não essencial), `F` (falha), `IMP` (impedimento) e `X` (execução inválida). Cada barreira recebe um identificador (`B-01`, `B-02`, ...) usado nas tabelas de `M8` e `M9` e na [tabela de barreiras](#registro-barreiras). Nas colunas de evidência, cite o arquivo e o minuto da gravação.

<a id="registro-preparacao"></a>

## 1. Preparação do ambiente

A Tabela 1 identifica o ambiente, com os mesmos dados de [`A3`](registro-adaptabilidade.md#registro-preparacao) usados na avaliação de adaptabilidade [S2](#s2).

| ID | Sistema operacional | Navegador | Versão | Modalidade | Recursos | Data da preparação | Responsável | Build do sistema |
|---|---|---|---|---|---|---|---|---|
| [`A3`](#registro-preparacao) | macOS Tahoe | Apple Safari | 26.5.2 (21624.2.5.11.8) | Computador real (MacBook Pro, chip M4) | 32 GB, 10 núcleos | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | 27.2.1 |

*Tabela 1. Identificação do ambiente de teste. Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll), com base no [registro de adaptabilidade](registro-adaptabilidade.md)*

A Tabela 2 verifica os parâmetros da [preparação comum](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#2-preparacao-comum). A coluna "Situação" indica `Conforme` ou `Não conforme`.

| Parâmetro de configuração | Valor especificado | Valor verificado no ensaio | Situação |
| --- | --- | --- | :-: |
| Sistema operacional | macOS Tahoe | macOS Tahoe | |
| *Build* exata do sistema | 27.2.1 | 27.2.1 | |
| Navegador | Apple Safari 26.5.2 | Apple Safari 26.5.2 (21624.2.5.11.8) | |
| Modalidade de execução | Computador real | Computador real | |
| Memória RAM | 32 GB | 32 GB | |
| Processador | 10 núcleos (computador real) | 10 núcleos (computador real) | |
| Resolução da tela | Registrar a resolução usada | 1470 × 956 (padrão; Retina 2560 × 1664), janela maximizada | |
| Nível de zoom | 100% | | |
| Idioma da plataforma | Português do Brasil | | |
| Perfil do navegador | Sem extensões | Janela privada do Safari, sem extensões | Conforme |
| Navegação por Tab no Safari | "Pressionar Tab para destacar cada item" ativado | Ativado | Conforme |
| Navegação pelo teclado no macOS | Ativada | | |
| Notificações do sistema | Desativadas (Não Perturbe) | | |
| Conta de teste | Mesma conta das demais sessões, autenticada antes da tarefa | Conta da avaliadora, com o curso Matemática EF: 6º Ano adicionado em "Meus cursos", autenticada antes da tarefa | Não conforme |
| Leitor de tela ([`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela)) | VoiceOver, voz em português, velocidade padrão | | |
| Gravação de áudio ([`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela)) | Áudio do VoiceOver audível na gravação | | |

*Tabela 2. Verificação do ambiente [`A3`](#registro-preparacao). Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll)*

<a id="registro-sessoes"></a>

## 2. Registro das sessões (Formulário F7)

A Tabela 3 segue o [Formulário F7](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#f7-registro-do-ambiente-da-sessao). Cada sessão tem um identificador no formato `AC-AAAAMMDD-NN`, usado no nome de todas as evidências.

| Sessão | Data | Avaliador | Observador | Ambiente | Sistema operacional e versão | Navegador e versão | Tecnologia assistiva e versão | Resolução | Zoom e tema de contraste |
|---|---|---|---|---|---|---|---|---|---|
| `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | | [`A3`](#registro-preparacao) | macOS Tahoe, build 27.2.1 | Safari 26.5.2 | Nenhuma (somente teclado) | 1470 × 956 | 100%, padrão |
| `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | | [`A3`](#registro-preparacao) | macOS Tahoe, build 27.2.1 | Safari 26.5.2 | VoiceOver (macOS Tahoe, build 27.2.1), voz em português | 1470 × 956 | 100%, padrão |

*Tabela 3. Registro do ambiente das sessões. Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll)*

A Tabela 4 registra o conteúdo das [tarefas de referência](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#41-tarefas-de-referencia), o mesmo usado nos demais ambientes.

| Tarefa | Fluxo | Conteúdo | Resposta de teste e recursos opcionais |
|---|---|---|---|
| `T1` | [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) | Curso Matemática EF: 6º ano, unidade "Números: sistema de numeração decimal" | --- |
| `T2` | [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) | Videoaula "História dos números" | Legenda: disponível · Transcrição: disponível |
| `T3` | [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) | Exercício ["Semelhanças e diferenças entre sistemas de numeração"](https://pt.khanacademy.org/math/6-ano-matematica/numeros-sistema-de-numeracao-decimal-6ano/os-numeros/e/semelhancas-e-diferencas-entre-sistemas-de-numeracao) | Pergunta exibida: classificar dois sistemas de numeração, cada um em uma lista suspensa, como posicional ou não posicional. Resposta de teste: "Sistema não posicional" nas duas listas, enviada primeiro; após o retorno e a dica, envio da resposta correta. Em `M9`, a pergunta sorteada foi de digitar (escrever XXXI na forma decimal), e a resposta enviada foi 122 · Dica: disponível |

*Tabela 4. Conteúdo das tarefas de referência. Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll)*

<a id="registro-m8"></a>

## 3. Registro de M8 (Formulário F5)

A Tabela 5 registra cada etapa da [navegação por teclado](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#43-navegacao-por-teclado-m8). Na observação, indicar foco visível (WCAG 2.4.7), ordem do foco (2.4.3), acesso ao controle (2.1.1), armadilha de foco (2.1.2) e o número de teclas até o controle.

| ID | Tarefa | Etapa | Observação | Barreira | Evidência |
|---|---|---|---|---|---|
| `M8-A3-T1-E1` | `T1` | Localizar o curso | Foco visível em todos os itens e ordem coerente com a ordem visual; 19 Tabs a partir da barra de endereço até a área do curso em "Meus cursos" | --- | [`AC-20261121-01_M8-A3-T1`](https://drive.google.com/file/d/1CRAE6kb0uccfvqKGk8MG0UsqlQZ-LG7a/view) |
| `M8-A3-T1-E2` | `T1` | Abrir o curso | O título "Matemática EF: 6º Ano" é texto e não recebe foco, assim como não é clicável com o mouse; o foco passa por "Ver tudo (10)" e segue para a primeira unidade, por onde o curso é acessado | --- | [`AC-20261121-01_M8-A3-T1`](https://drive.google.com/file/d/1CRAE6kb0uccfvqKGk8MG0UsqlQZ-LG7a/view) |
| `M8-A3-T1-E3` | `T1` | Abrir a primeira unidade | Enter em "Números: sistema de numeração decimal" abriu a lista de aulas; sem armadilha de foco. A tarefa foi repetida três vezes na mesma gravação, com o mesmo comportamento, retornando à página inicial pelo logotipo com Tab | --- | [`AC-20261121-01_M8-A3-T1`](https://drive.google.com/file/d/1CRAE6kb0uccfvqKGk8MG0UsqlQZ-LG7a/view) |
| `M8-A3-T2-E1` | `T2` | Abrir a videoaula | Foco visível e ordem coerente; 63 Tabs da barra de endereço até "História dos números" | `B-03` | [`C-20261121-01_M8-A3-T2`](https://drive.google.com/file/d/1iavkItL73H68X30bTg9D-HHIfcWAO_i-/view) |
| `M8-A3-T2-E2` | `T2` | Iniciar a reprodução | 40 Tabs até o player; Espaço inicia a reprodução | `B-03` | [`C-20261121-01_M8-A3-T2`](https://drive.google.com/file/d/1iavkItL73H68X30bTg9D-HHIfcWAO_i-/view) |
| `M8-A3-T2-E3` | `T2` | Pausar | Espaço pausa a reprodução | --- | [`C-20261121-01_M8-A3-T2`](https://drive.google.com/file/d/1iavkItL73H68X30bTg9D-HHIfcWAO_i-/view) |
| `M8-A3-T2-E4` | `T2` | Ativar legenda ou transcrição | Os controles do player (volume, CC e configurações) só aparecem e recebem foco com o ponteiro sobre o vídeo; pausado pelo teclado, continuam ocultos e fora da ordem do Tab. Com os controles visíveis, Enter no CC ativa a legenda. O menu de configurações prende o foco: Tab, Shift+Tab, setas e Esc não saem dele. A transcrição é acessível pelo teclado: Tab até a aba "Sobre" e seta para a direita até "Transcrição". Na gravação principal a avaliadora usou o *trackpad* para exibir os controles; o caminho somente por teclado foi demonstrado na gravação de verificação | `B-01`, `B-02` | [`C-20261121-01_M8-A3-T2`](https://drive.google.com/file/d/1iavkItL73H68X30bTg9D-HHIfcWAO_i-/view), [`AC-20261121-01_M8-A3-T2-verificacao`](https://drive.google.com/file/d/1ntiwqavXmZZLrtXhAzdGJvcU4PXwAZ9Q/view) |
| `M8-A3-T3-E1` | `T3` | Abrir o exercício | 34 Tabs até "Vamos lá"; Enter abre a primeira pergunta. Foco visível e ordem coerente | `B-03` | [`AC-20261121-01_M8-A3-T3`](https://drive.google.com/file/d/1jpFbvOfTlqruo38EMRCP8OqSxzPx4y1X/view) |
| `M8-A3-T3-E2` | `T3` | Solicitar a dica | Botão de dica recebe foco e Enter exibe as dicas | --- | [`AC-20261121-01_M8-A3-T3`](https://drive.google.com/file/d/1jpFbvOfTlqruo38EMRCP8OqSxzPx4y1X/view) |
| `M8-A3-T3-E3` | `T3` | Selecionar a resposta de teste | 45 Tabs até a primeira lista suspensa; Enter abre a lista, o foco fica visível na opção e Enter confirma a seleção. As duas listas são acessíveis pelo teclado | `B-03` | [`AC-20261121-01_M8-A3-T3`](https://drive.google.com/file/d/1jpFbvOfTlqruo38EMRCP8OqSxzPx4y1X/view) |
| `M8-A3-T3-E4` | `T3` | Enviar e visualizar o retorno | 5 Tabs da última seleção até "Verificar"; Enter envia e o retorno da plataforma é exibido. Sem armadilha de foco e sem uso do *trackpad* | --- | [`AC-20261121-01_M8-A3-T3`](https://drive.google.com/file/d/1jpFbvOfTlqruo38EMRCP8OqSxzPx4y1X/view) |

*Tabela 5. Registro das etapas de M8 em [`A3`](#registro-preparacao). Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll)*

<a id="registro-m9"></a>

## 4. Registro de M9 (Formulário F5)

A Tabela 6 registra cada etapa do [teste com leitor de tela](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#44-leitor-de-tela-m9), com a tela coberta e um observador acompanhando. Na observação, indicar o que o VoiceOver anunciou, se o controle tem nome e função compreensíveis, se mudanças de estado foram anunciadas e se foi preciso consultar a tela.

| ID | Tarefa | Etapa | O que foi anunciado | Observação | Barreira | Evidência |
|---|---|---|---|---|---|---|
| `M9-A3-T1-E1` | `T1` | Localizar o curso | Rotor (VO+U), lista de links: "Pular para o conteúdo principal", "Cursos", "Ver tudo (10)", "Números: sistema de numeração decimal" e demais unidades | Nomes dos links claros. O título "Matemática EF: 6º Ano" não é anunciado na lista de links, e "Números: sistema de numeração decimal" aparece duas vezes sem indicar o curso; foi escolhida a primeira ocorrência | --- | [`AC-20261122-02_M9-A3-T1`](https://drive.google.com/file/d/1GP4kQjI82rDCdDtig_VgsZF1ggPrZAn9/view) |
| `M9-A3-T1-E2` | `T1` | Abrir o curso | --- | O curso é acessado pela unidade, como em `M8` | --- | [`AC-20261122-02_M9-A3-T1`](https://drive.google.com/file/d/1GP4kQjI82rDCdDtig_VgsZF1ggPrZAn9/view) |
| `M9-A3-T1-E3` | `T1` | Abrir a primeira unidade | Nenhum anúncio após o Enter; o cursor do VoiceOver para em um elemento vazio acima de "Sobre esta unidade". Com VO+seta, a leitura fica nos quadrados da barra de progresso da unidade, lidos um a um e soletrados | A mudança de página não é anunciada e o cursor do VoiceOver não avança da barra de progresso até "Sobre esta unidade" e às aulas. A avaliadora consultou a tela para entender o estado da página | `B-04`, `B-05` | [`AC-20261122-02_M9-A3-T1`](https://drive.google.com/file/d/1GP4kQjI82rDCdDtig_VgsZF1ggPrZAn9/view), [`AC-20261122-02_M9-A3-T1-verificacao`](https://drive.google.com/file/d/16Qz5Wpz-YNXDW6EPFr878y2DBW9wntQx/view) |
| `M9-A3-T2-E1` | `T2` | Abrir a videoaula | Nenhum anúncio após o Enter no link "História dos números" do rotor. Ao reabrir o rotor, o link do vídeo é indicado como página atual | A página do vídeo abre, mas a mudança não é anunciada; a avaliadora confirmou a localização pelo rotor | `B-04` | [`AC-20261122-02_M9-A3-T2`](https://drive.google.com/file/d/1TsAbnplGR4d0LtboHMx26pDtPgACHZIv/view) |
| `M9-A3-T2-E2` | `T2` | Iniciar a reprodução | Com VO+seta para a direita, a leitura percorre a navegação lateral com as demais aulas, sem chegar ao player | Espaço e VO+seta não levam ao vídeo; não foi possível iniciar a reprodução | `B-06` | [`AC-20261122-02_M9-A3-T2`](https://drive.google.com/file/d/1TsAbnplGR4d0LtboHMx26pDtPgACHZIv/view) |
| `M9-A3-T2-E3` | `T2` | Pausar | --- | Etapa não alcançada | `B-06` | [`AC-20261122-02_M9-A3-T2`](https://drive.google.com/file/d/1TsAbnplGR4d0LtboHMx26pDtPgACHZIv/view) |
| `M9-A3-T2-E4` | `T2` | Ativar legenda ou transcrição | "Sobre" e "Transcrição" não foram anunciados | Etapa não alcançada. A avaliadora consultou a tela no fim para confirmar onde estava; sem uso do *trackpad* | `B-06` | [`AC-20261122-02_M9-A3-T2`](https://drive.google.com/file/d/1TsAbnplGR4d0LtboHMx26pDtPgACHZIv/view) |
| `M9-A3-T3-E1` | `T3` | Abrir o exercício | "Vamos lá" anunciado e acionado | A pergunta sorteada foi de digitar: escrever XXXI na forma decimal | --- | [`AC-20261122-02_M9-A3-T3`](https://drive.google.com/file/d/1nxKqgd5oceoW4z6Ku9iEuTykIOLjwNGK/view) |
| `M9-A3-T3-E2` | `T3` | Solicitar a dica | Botão de dica alcançado com Tab e acionado após o retorno da resposta; o texto da dica não foi lido | A dica aparece na tela, mas o conteúdo não é anunciado | `B-08` | [`AC-20261122-02_M9-A3-T3`](https://drive.google.com/file/d/1nxKqgd5oceoW4z6Ku9iEuTykIOLjwNGK/view) |
| `M9-A3-T3-E3` | `T3` | Selecionar a resposta de teste | Campo anunciado como caixa de texto para digitar a resposta; o enunciado "Escreva o número na forma decimal" e a expressão "XXXI" não foram lidos | Sem o enunciado, a avaliadora digitou uma resposta sem saber a pergunta (122) | `B-07` | [`AC-20261122-02_M9-A3-T3`](https://drive.google.com/file/d/1nxKqgd5oceoW4z6Ku9iEuTykIOLjwNGK/view) |
| `M9-A3-T3-E4` | `T3` | Enviar e ouvir o retorno | Após "Verificar", anunciou "Não é dessa vez" | Retorno da resposta anunciado, o que conclui a tarefa somente pelo áudio. A avaliadora consultou a tela depois do retorno e da tentativa de ouvir a dica; sem uso do *trackpad* | --- | [`AC-20261122-02_M9-A3-T3`](https://drive.google.com/file/d/1nxKqgd5oceoW4z6Ku9iEuTykIOLjwNGK/view) |

*Tabela 6. Registro das etapas de M9 em [`A3`](#registro-preparacao). Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll)*

<a id="registro-resultados"></a>

## 5. Resultado por combinação

A Tabela 7 consolida a classificação de cada combinação de métrica e tarefa em [`A3`](#registro-preparacao).

| ID | Sessão | Data | Executor / observador | Classificação | Barreiras | Evidência |
|---|---|---|---|:-:|---|---|
| `M8-A3-T1` | `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `S` | --- | [`AC-20261121-01_M8-A3-T1`](https://drive.google.com/file/d/1CRAE6kb0uccfvqKGk8MG0UsqlQZ-LG7a/view) |
| `M8-A3-T2` | `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `SB` | `B-01`, `B-02`, `B-03` | [`C-20261121-01_M8-A3-T2`](https://drive.google.com/file/d/1iavkItL73H68X30bTg9D-HHIfcWAO_i-/view) |
| `M8-A3-T3` | `AC-20261121-01` | 21/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `SB` | `B-03` | [`AC-20261121-01_M8-A3-T3`](https://drive.google.com/file/d/1jpFbvOfTlqruo38EMRCP8OqSxzPx4y1X/view) |
| `M9-A3-T1` | `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `IMP` | `B-04`, `B-05` | [`AC-20261122-02_M9-A3-T1`](https://drive.google.com/file/d/1GP4kQjI82rDCdDtig_VgsZF1ggPrZAn9/view) |
| `M9-A3-T2` | `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `IMP` | `B-04`, `B-06` | [`AC-20261122-02_M9-A3-T2`](https://drive.google.com/file/d/1TsAbnplGR4d0LtboHMx26pDtPgACHZIv/view) |
| `M9-A3-T3` | `AC-20261122-02` | 22/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) | `SB` | `B-07`, `B-08` | [`AC-20261122-02_M9-A3-T3`](https://drive.google.com/file/d/1nxKqgd5oceoW4z6Ku9iEuTykIOLjwNGK/view) |

*Tabela 7. Classificação das combinações em [`A3`](#registro-preparacao). Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll)*

Os vídeos da preparação estão em [`AC_Preparacao-A3`](https://drive.google.com/file/d/1Dk90UI_L805paUHbbATmv5u1gIXM1EZu/view), com a configuração do ambiente, e em [`AC-20261122-02_Preparacao-VoiceOver`](https://drive.google.com/file/d/14YSbmuORvNl-ewQXP173eUe8RlGS37sr/view), com a configuração do VoiceOver. As gravações ficam nas pastas [`M8`](https://drive.google.com/drive/folders/1f20D-PjEjNCV0GAkCoRZku7MBPBcj1Rl) e [`M9`](https://drive.google.com/drive/folders/1kbiFeUa_rVcAJbYXkNU74rVjvH0Tgphy) de [`A3`](https://drive.google.com/drive/folders/146QSY6MaWjv2xLgB26ISgkBFP9jxFrzb).

<a id="registro-barreiras"></a>

## 6. Barreiras

A Tabela 8 recebe uma linha por barreira, com ou sem impacto na conclusão, conforme o [registro de barreiras](../fase-3/procedimentos-acessibilidade-apreensibilidade.md#47-registro-de-barreiras). Gravidade: **bloqueia** (impede etapa essencial), **dificulta** (exige contorno) ou **incomoda** (não afeta a conclusão).

| ID | Combinação e etapa | Passos para reproduzir | Comportamento esperado | Comportamento observado | Critério WCAG | Gravidade | Evidência |
|---|---|---|---|---|---|:-:|---|
| `B-01` | `M8-A3-T2`, etapa 4 | Abrir "História dos números", iniciar e pausar com Espaço e pressionar Tab sem mover o ponteiro | Botões CC e configurações recebem foco pelo teclado | Os controles só aparecem com o ponteiro sobre o vídeo; sem ele, ficam ocultos e o Tab não os alcança, impedindo ativar a legenda pelo teclado. A transcrição pelas abas é alternativa acessível | 2.1.1 | Dificulta | [`AC-20261121-01_M8-A3-T2-verificacao`](https://drive.google.com/file/d/1ntiwqavXmZZLrtXhAzdGJvcU4PXwAZ9Q/view) |
| `B-02` | `M8-A3-T2`, etapa 4 | Com os controles visíveis, levar o foco ao botão de configurações e pressionar Enter | Esc fecha o menu e o foco volta ao player | Tab, Shift+Tab, setas e Esc não saem do menu; foi preciso usar o *trackpad* | 2.1.2 | Dificulta | [`AC-20261121-01_M8-A3-T2-verificacao`](https://drive.google.com/file/d/1ntiwqavXmZZLrtXhAzdGJvcU4PXwAZ9Q/view) |
| `B-03` | `M8-A3-T2`, etapas 1 e 2; `M8-A3-T3`, etapas 1 e 3 | Da barra de endereço, avançar com Tab até a videoaula, o player, o botão "Vamos lá" e a primeira resposta | Chegar ao conteúdo da tarefa com poucas teclas | 63 Tabs até a videoaula, 40 até o player, 34 até "Vamos lá" e 45 até a primeira resposta. A página tem o link "Pular para o conteúdo principal", identificado no rotor do VoiceOver | --- | Incomoda | [`C-20261121-01_M8-A3-T2`](https://drive.google.com/file/d/1iavkItL73H68X30bTg9D-HHIfcWAO_i-/view), [`AC-20261121-01_M8-A3-T3`](https://drive.google.com/file/d/1jpFbvOfTlqruo38EMRCP8OqSxzPx4y1X/view) |
| `B-04` | `M9-A3-T1`, etapa 3; `M9-A3-T2`, etapa 1 | Com o VoiceOver ativo, abrir pelo rotor a unidade "Números: sistema de numeração decimal" | Anúncio da nova página e foco no início do conteúdo | Nenhum anúncio; o cursor do VoiceOver fica em um elemento vazio, sem nome, acima de "Sobre esta unidade" | 2.4.3, 4.1.2 | Dificulta | [`AC-20261122-02_M9-A3-T1`](https://drive.google.com/file/d/1GP4kQjI82rDCdDtig_VgsZF1ggPrZAn9/view), [`AC-20261122-02_M9-A3-T2`](https://drive.google.com/file/d/1TsAbnplGR4d0LtboHMx26pDtPgACHZIv/view) |
| `B-05` | `M9-A3-T1`, etapa 3 | Na página da unidade, avançar com VO+seta para a direita a partir do topo do conteúdo | Leitura resumida do progresso e passagem para "Sobre esta unidade" e a lista de aulas | Os quadrados da barra de progresso são lidos um a um e soletrados, e o cursor não avança até o conteúdo da unidade, impedindo ouvir a lista de aulas | 1.3.1, 4.1.2 | Bloqueia | [`AC-20261122-02_M9-A3-T1-verificacao`](https://drive.google.com/file/d/16Qz5Wpz-YNXDW6EPFr878y2DBW9wntQx/view) |
| `B-06` | `M9-A3-T2`, etapas 2 a 4 | Com o VoiceOver ativo, abrir "História dos números" pelo rotor e avançar com VO+seta para a direita ou Espaço | O cursor do VoiceOver alcança o player, anuncia os controles de reprodução e chega às abas "Sobre" e "Transcrição" | O cursor percorre a navegação lateral com as demais aulas e não alcança o player nem as abas; não é possível iniciar o vídeo nem abrir a transcrição | 2.1.1, 4.1.2 | Bloqueia | [`AC-20261122-02_M9-A3-T2`](https://drive.google.com/file/d/1TsAbnplGR4d0LtboHMx26pDtPgACHZIv/view) |
| `B-07` | `M9-A3-T3`, etapa 3 | Com o VoiceOver ativo, abrir o exercício, acionar "Vamos lá" e levar o foco ao campo de resposta | O campo é anunciado com o enunciado e a expressão a converter | O campo é anunciado apenas como caixa de texto; o enunciado e a expressão matemática não são lidos, e não é possível saber o que responder | 1.3.1, 3.3.2 | Dificulta | [`AC-20261122-02_M9-A3-T3`](https://drive.google.com/file/d/1nxKqgd5oceoW4z6Ku9iEuTykIOLjwNGK/view) |
| `B-08` | `M9-A3-T3`, etapa 2 | Com o VoiceOver ativo, levar o foco ao botão de dica com Tab e acioná-lo | O texto da dica é anunciado ou o foco vai para ele | A dica aparece na tela, mas não é anunciada | 4.1.3 | Dificulta | [`AC-20261122-02_M9-A3-T3`](https://drive.google.com/file/d/1nxKqgd5oceoW4z6Ku9iEuTykIOLjwNGK/view) |

*Tabela 8. Barreiras registradas em [`A3`](#registro-preparacao). Fonte: Elaborada por [Luisa de Souza](https://github.com/luisa12ll)*

## Referências

<a id="s1"></a>

> [S1] Procedimentos de avaliação de acessibilidade e apreensibilidade (M8 a M14), Fase 3. Disponível em: [Procedimentos de acessibilidade e apreensibilidade](../fase-3/procedimentos-acessibilidade-apreensibilidade.md).

<a id="s2"></a>

> [S2] Registro de execuções de adaptabilidade (M6 e M7), Fase 4. Disponível em: [Registro de adaptabilidade](registro-adaptabilidade.md).

<a id="s3"></a>

> [S3] APPLE. **VoiceOver User Guide for Mac**. Disponível em: <https://support.apple.com/guide/voiceover/welcome/mac>. Acesso em: 22 nov. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 22/11/2026 | Estrutura dos formulários de registro de `M8` e `M9` e preparação do ambiente [`A3`](#registro-preparacao). | [Luisa de Souza](https://github.com/luisa12ll) | A definir |
