# Registro de execuções (M6 e M7)

**Versão 1.3**

Esta página reúne os formulários de registro da avaliação de adaptabilidade definida em [Procedimentos de avaliação de adaptabilidade](procedimentos-adaptabilidade.md) [S1](#s1). As tabelas são preenchidas na Fase 4, por *pull request*, conforme cada execução. Esta versão já traz a preparação e as execuções de 14/11/2026 nos ambientes [`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao); o ambiente [`A3`](#registro-preparacao) (macOS e Safari) segue pendente.

**Como preencher.** Mantenha os identificadores das linhas. Use os códigos de resultado `C` (concluída), `F` (falha), `I` (inviável) e `X` (inválida), definidos em [4.3](procedimentos-adaptabilidade.md#43-passos-de-execucao). Em `F`, indique `F-BLQ` ou `F-AJ`. Nas colunas de evidência, cite o nome do arquivo conforme o padrão da [seção 8](procedimentos-adaptabilidade.md#8-formularios-e-modelos-de-registro). Cada ocorrência recebe um `id_ocorrencia` (`OC-001`, `OC-002`, ...) usado nas tabelas de `M6` e `M7` e na [tabela de ocorrências](#registro-ocorrencias).

<a id="registro-preparacao"></a>

## 1. Preparação dos ambientes

A Tabela 1 identifica cada ambiente, com os dados já conhecidos do [ambiente de testes](ambiente-de-testes.md) [S2](#s2).

| ID | Sistema operacional | Navegador | Versão | Modalidade | Recursos | Data da preparação | Responsável | Build do sistema |
|---|---|---|---|---|---|---|---|---|
| [`A1`](#registro-preparacao) | Windows 11 Pro | Google Chrome | 157.0 | Virtualizado (Docker, Winboat) | 4 GB, 4 vCPUs | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | 26200.8037 |
| [`A2`](#registro-preparacao) | Windows 11 Pro | Mozilla Firefox | 160 | Virtualizado (Docker, Winboat) | 4 GB, 4 vCPUs | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | 26200.8037 |
| [`A3`](#registro-preparacao) | macOS Tahoe 27.2.1 | Apple Safari | 26.5.2 | Computador real | 32 GB, 10 Núcleos | xx/11/2026 | [Luisa de Souza](https://github.com/luisa12ll) e [Pedro Lucas](https://github.com/Pwdrinho) | Pendente |
| [`A4`](#registro-preparacao) | Ubuntu 26.04 | Mozilla Firefox | 159.0 | Virtualizado (QEMU/KVM, Gnome Boxes) | 4 GB, 4 vCPUs | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | 26.04.1 |

*Tabela 1. Identificação dos ambientes de teste. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [ambiente de testes](ambiente-de-testes.md)*

A Tabela 2 registra as verificações de [preparação](procedimentos-adaptabilidade.md#34-preparacao-do-ambiente). Marque `S` quando atendida.

| ID | `PA-1` | `PA-2` | `PA-3` | `PA-4` | `PA-5` | `PA-6` | `PA-7` | `PA-8` | `PA-9` | `PA-10` | Observações |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| [`A1`](#registro-preparacao) | S | S | S | S | S | S | S | S | S | S | [Preparação A1](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| [`A2`](#registro-preparacao) | S | S | S | S | S | S | S | S | S | S | [Preparação A2](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| [`A3`](#registro-preparacao) | | | | | | | | | | | [Preparação A3]() |
| [`A4`](#registro-preparacao) | S | S | S | S | S | S | S | S | S | S | [Preparação A4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |

*Tabela 2. Verificações de preparação por ambiente. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

As Tabelas 3 a 6 complementam a Tabela 2 com a verificação, por ambiente, dos parâmetros definidos no [ambiente de testes](ambiente-de-testes.md) [S2](#s2). A coluna "Situação" indica `Conforme` ou `Pendente`.

A Tabela 3 registra as características do ambiente [`A1`](#registro-preparacao), conforme definido no [ambiente de testes](ambiente-de-testes.md) [S2](#s2).

| Parâmetro de configuração | Valor especificado | Valor verificado no ensaio | Situação |
| --- | --- | --- | :-: |
| Sistema operacional convidado | Windows 11 Pro 64-bit | Windows 11 Pro 64-bit | Conforme |
| *Build* exata do sistema | 26200.8037 | 26200.8037 | Conforme |
| Navegador e motor | Google Chrome 157.0 | Google Chrome 157.0 | Conforme |
| Modalidade de execução | Virtualizado (Docker, Winboat) | Virtualizado (Docker, Winboat) | Conforme |
| Alocação de memória RAM | 4 GB | 4 GB | Conforme |
| Alocação de vCPUs | 4 vCPUs | 4 vCPUs | Conforme |
| Resolução de tela e janela | 1366 × 768 pixels (`J1`), maximizada | 1366 × 768 pixels (`J1`), maximizada | Conforme |
| Resolução de tela e janela | 1920 × 1080 pixels (`J2`), maximizada | 1920 × 1080 pixels (`J2`), maximizada | Conforme |
| Nível de zoom | 100% | 100% | Conforme |
| Data da preparação formal | 14/11/2026 | 14/11/2026 | Conforme |
| Responsável pela preparação | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | Conforme |

*Tabela 3. Verificação do ambiente de referência [`A1`](#registro-preparacao). Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho)*

A Tabela 4 registra as características do ambiente [`A2`](#registro-preparacao), conforme definido no [ambiente de testes](ambiente-de-testes.md) [S2](#s2).

| Parâmetro de configuração | Valor especificado | Valor verificado no ensaio | Situação |
| --- | --- | --- | :-: |
| Sistema operacional convidado | Windows 11 Pro 64-bit | Windows 11 Pro 64-bit | Conforme |
| *Build* exata do sistema | 26200.8037 | 26200.8037 | Conforme |
| Navegador e motor | Mozilla Firefox 160 | Mozilla Firefox 160 | Conforme |
| Modalidade de execução | Virtualizado (Docker, Winboat) | Virtualizado (Docker, Winboat) | Conforme |
| Alocação de memória RAM | 4 GB | 4 GB | Conforme |
| Alocação de vCPUs | 4 vCPUs | 4 vCPUs | Conforme |
| Resolução de tela e janela | 1366 × 768 pixels (`J1`), maximizada | 1366 × 768 pixels (`J1`), maximizada | Conforme |
| Resolução de tela e janela | 1920 × 1080 pixels (`J2`), maximizada | 1920 × 1080 pixels (`J2`), maximizada | Conforme |
| Nível de zoom | 100% | 100% | Conforme |
| Data da preparação formal | 14/11/2026 | 14/11/2026 | Conforme |
| Responsável pela preparação | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | Conforme |

*Tabela 4. Verificação do ambiente de referência [`A2`](#registro-preparacao). Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho)*

A Tabela 5 registra as características do ambiente [`A3`](#registro-preparacao), conforme definido no [ambiente de testes](ambiente-de-testes.md) [S2](#s2).

| Parâmetro de configuração | Valor especificado | Valor verificado no ensaio | Situação |
| --- | --- | --- | :-: |
| Sistema operacional | macOS Tahoe |  | Pendente |
| *Build* exata do sistema | 27.2.1 |  | Pendente |
| Navegador e motor | Apple Safari 26.5.2 |  | Pendente |
| Modalidade de execução | Computador real |  | Pendente |
| Alocação de memória RAM | 32 GB |  | Pendente |
| Alocação de vCPUs | 10 núcleos (computador real) |  | Pendente |
| Resolução de tela e janela | 1366 × 768 pixels (`J1`), maximizada |  | Pendente |
| Resolução de tela e janela | 1920 × 1080 pixels (`J2`), maximizada |  | Pendente |
| Nível de zoom | 100% |  | Pendente |
| Data da preparação formal | xx/11/2026 (prevista) |  | Pendente |
| Responsável pela preparação | [Luisa de Souza](https://github.com/luisa12ll) e [Pedro Lucas](https://github.com/Pwdrinho) |  | Pendente |

*Tabela 5. Verificação do ambiente de referência [`A3`](#registro-preparacao). Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho)*

A Tabela 6 registra as características do ambiente [`A4`](#registro-preparacao), conforme definido no [ambiente de testes](ambiente-de-testes.md) [S2](#s2).

| Parâmetro de configuração | Valor especificado | Valor verificado no ensaio | Situação |
| --- | --- | --- | :-: |
| Sistema operacional convidado | Ubuntu | Ubuntu | Conforme |
| *Build* exata do sistema | 26.04.1 | 26.04.1 | Conforme |
| Navegador e motor | Mozilla Firefox 159.0 | Mozilla Firefox 159.0 | Conforme |
| Modalidade de execução | Virtualizado (QEMU/KVM, Gnome Boxes) | Virtualizado (QEMU/KVM, Gnome Boxes) | Conforme |
| Alocação de memória RAM | 4 GB | 4 GB | Conforme |
| Alocação de vCPUs | 4 vCPUs | 4 vCPUs | Conforme |
| Resolução de tela e janela | 1366 × 768 pixels (`J1`), maximizada | 1366 × 768 pixels (`J1`), maximizada | Conforme |
| Resolução de tela e janela | 1920 × 1080 pixels (`J2`), maximizada | 1920 × 1080 pixels (`J2`), maximizada | Conforme |
| Nível de zoom | 100% | 100% | Conforme |
| Data da preparação formal | 14/11/2026 | 14/11/2026 | Conforme |
| Responsável pela preparação | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | Conforme |

*Tabela 6. Verificação do ambiente de referência [`A4`](#registro-preparacao). Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho)*

<a id="registro-rotulos"></a>

## 2. Dados de teste congelados e rótulos dos controles

A Tabela 7 registra os dados de teste da [preparação](procedimentos-adaptabilidade.md#34-preparacao-do-ambiente), iguais em todos os ambientes.

| ID | Dado | Valor congelado | Data do congelamento |
|---|---|---|---|
| `D1` | Disciplina | https://pt.khanacademy.org/math/matematica-avancada | 14/11/2026 |
| `D2` | Curso | https://pt.khanacademy.org/math/precalculus | 14/11/2026 |
| `D3` | Unidade e aula | https://pt.khanacademy.org/math/precalculus/composing/a/introduction-to-function-composition | 14/11/2026 |
| `D4` | Videoaula (com legenda e transcrição) | https://pt.khanacademy.org/math/precalculus/function-composition | 14/11/2026 |
| `D5` | Exercício (com dica) | https://pt.khanacademy.org/math/precalculus/composing/e/evaluate-composite-functions-from-formulas | 14/11/2026 |
| `D6` | Conta de teste (identificador, sem senha) | Conta 1 ([`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao)) e Conta 2 ([`A3`](#registro-preparacao)) | 14/11/2026 |

*Tabela 7. Dados de teste congelados. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

A Tabela 8 registra o rótulo real de cada item do [inventário de controles essenciais](procedimentos-adaptabilidade.md#54-inventario-de-controles-essenciais) na interface em uso.

| ID | Conteúdo ou controle essencial | Rótulo real na interface |
|---|---|---|
| `CE1.1` | Menu ou busca para localizar a disciplina | "Explorar", "Matemática Avançada" |
| `CE1.2` | Item do curso-alvo | "Pré-cálculo" |
| `CE1.3` | Lista de unidades e aulas do curso | "UNIDADE 1 Funções compostas e inversas" |
| `CE1.4` | Conteúdo da aula selecionada | "Introdução à composição de funções" |
| `CE2.1` | Área do vídeo e barra de reprodução | "Reproduzir Vídeo", "Controle deslizante de busca", "Sobre esse Vídeo", "Vídeo no YouTube" |
| `CE2.2` | Controle de iniciar e pausar | "Assistir Aula" |
| `CE2.3` | Controle de legenda | "Legenda/CC desativadas" e "Legendas/CC ativadas" |
| `CE2.4` | Acesso à transcrição | "Transcrição" |
| `CE3.1` | Enunciado e área de resposta | Não Rotulado e "Sua resposta:" |
| `CE3.2` | Controle de dica | "Preciso de ajuda. Mostre-me a solução.", "Não é bem isso", "Mostrar uma etapa" |
| `CE3.3` | Controle de envio da resposta | "Verificar" "Tentar Novamente" |
| `CE3.4` | Retorno da plataforma e controle de continuidade | "Botões de controle accordion" |
| `CE4.1` | Acesso à área do estudante | "Página inicial do aluno" |
| `CE4.2` | Informações de progresso | "Ver progresso de todos os cursos" |

*Tabela 8. Rótulos reais dos controles essenciais. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-resolucao"></a>

## 3. Resolução verificada

A Tabela 9 registra o resultado do comando de [3.5](procedimentos-adaptabilidade.md#35-resolucao-e-janela) ao início das sessões de cada ambiente e dimensão. Se algum valor mudar durante a coleta, acrescente uma linha com a data.

| Ambiente | Dimensão | `screen` (largura × altura) | `inner` (largura × altura) | `dpr` | Data |
|---|---|---|---|---|---|
| [`A1`](#registro-preparacao) | `J1` (1366 × 768) | 1366 × 768 | Não registrado | 1 | 14/11/2026 |
| [`A1`](#registro-preparacao) | `J2` (1920 × 1080) | 1920 × 1080 | Não registrado | 1 | 14/11/2026 | 
| [`A2`](#registro-preparacao) | `J1` (1366 × 768) | 1366 × 768 | Não registrado | 1 | 14/11/2026 |
| [`A2`](#registro-preparacao) | `J2` (1920 × 1080) | 1920 × 1080 | Não registrado | 1 | 14/11/2026 |
| [`A3`](#registro-preparacao) | `J1` (1366 × 768) | | | | |
| [`A3`](#registro-preparacao) | `J2` (1920 × 1080) | | | | |
| [`A4`](#registro-preparacao) | `J1` (1366 × 768) | 1366 × 768 | Não registrado | 1 | 14/11/2026 |
| [`A4`](#registro-preparacao) | `J2` (1920 × 1080) | 1920 × 1080 | Não registrado | 1 | 14/11/2026 |

*Tabela 9. Resolução e viewport verificados por ambiente e dimensão. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

O `inner` das sessões de 14/11/2026 não pôde ser recuperado do vídeo, e os valores anotados na hora foram descartados por estarem incorretos. A validade das execuções segue por `screen` e `dpr` ([3.5](procedimentos-adaptabilidade.md#35-resolucao-e-janela)). Nas próximas sessões, registrar o `inner` com o DevTools desacoplado e acrescentar uma linha com a data. Como dado era apenas para registro sem influenciar nada na avaliação foi decidido manter como não registrado, ao invés de inventar um dado.

<a id="registro-m6"></a>

## 4. Registro de M6

A Tabela 10 registra as execuções em `J2` (1920 × 1080). `T1` a `T3` são os resultados das tentativas ([reprodução de falhas](procedimentos-adaptabilidade.md#46-reproducao-de-falhas)); o resultado final é `C` salvo falha confirmada em 2 de 3. `T2` e `T3` só são preenchidos quando `T1` falha; sem falha, use `---`.

| ID | Data | Executor / observador | `T1` | `T2` | `T3` | Final | Tipo de falha | Ocorrência | Evidência |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|---|
| `M6-A1-FL1` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A1-FL1](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A1-FL2` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A1-FL2](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A1-FL3` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A1-FL3](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A1-FL4` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A2-FL1` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A2-FL2` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A2-FL3` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A2-FL4` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M6-A2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A3-FL1` | | | | | | | | | |
| `M6-A3-FL2` | | | | | | | | | |
| `M6-A3-FL3` | | | | | | | | | |
| `M6-A3-FL4` | | | | | | | | | |
| `M6-A4-FL1` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A4-FL2` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A4-FL3` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M6-A4-FL4` | 14/11/2026 | [José Augusto](https://github.com/JAugustoM) e [Pedro Lucas](https://github.com/Pwdrinho) | `C` | --- | --- | `C` | --- | --- | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |

*Tabela 10. Registro das execuções de M6. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-m7"></a>

## 5. Registro de M7

A Tabela 11 registra as execuções de `M7`. A gravidade máxima segue a [escala `Gr1` a `Gr3`](procedimentos-adaptabilidade.md#55-problemas-de-adaptacao-e-gravidade); use `Gr0` quando não houver problema. As linhas em `J2` aproveitam a sessão de `M6`, com critério próprio. Um problema `Gr2` só torna a combinação `F` quando é confirmado em 2 de 3 execuções; sem repetição, a combinação é `C` e a ocorrência fica anotada ([5.3](procedimentos-adaptabilidade.md#53-passos-de-execucao) e [4.6](procedimentos-adaptabilidade.md#46-reproducao-de-falhas)).

| ID | Data | Executor / observador | Resultado | Gravidade máxima | CE afetados | Ocorrência | Evidência |
|---|---|---|:-:|:-:|---|---|---|
| `M7-A1-J1-FL1` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A1-J1-FL1](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A1-J1-FL2` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A1-J1-FL2](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A1-J1-FL3` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A1-J1-FL3](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A1-J1-FL4` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr1` | `CE4.2` | `OC-001` | [Video M7-A1-J1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A1-J2-FL1` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M6-A1-FL1](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A1-J2-FL2` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M6-A1-FL2](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A1-J2-FL3` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M6-A1-FL3](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A1-J2-FL4` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr1` | `CE4.2` | `OC-001` | [Video M6-A1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J1-FL1` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A2-J1-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J1-FL2` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A2-J1-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J1-FL3` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A2-J1-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J1-FL4` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr1` | `CE4.2` | `OC-001` | [Video M7-A2-J1-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J2-FL1` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A2-J2-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J2-FL2` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A2-J2-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J2-FL3` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A2-J2-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A2-J2-FL4` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr2` | `CE4.2` | `OC-001`, `OC-002` | [Video M7-A2-J2-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A3-J1-FL1` | | | | | | | |
| `M7-A3-J1-FL2` | | | | | | | |
| `M7-A3-J1-FL3` | | | | | | | |
| `M7-A3-J1-FL4` | | | | | | | |
| `M7-A3-J2-FL1` | | | | | | | |
| `M7-A3-J2-FL2` | | | | | | | |
| `M7-A3-J2-FL3` | | | | | | | |
| `M7-A3-J2-FL4` | | | | | | | |
| `M7-A4-J1-FL1` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A4-J1-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A4-J1-FL2` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr2` | `CE2.4` | `OC-003` | [Video M7-A4-J1-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A4-J1-FL3` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A4-J1-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A4-J1-FL4` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr2` | `CE4.2` | `OC-001`, `OC-002` | [Video M7-A4-J1-FL1-FL4 ](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A4-J2-FL1` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A4-J2-FL2` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr2` | `CE2.4` | `OC-003` | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A4-J2-FL3` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr0` | --- | --- | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `M7-A4-J2-FL4` | 14/11/2026 | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | `C` | `Gr1` | `CE4.2` | `OC-001`, `OC-004` | [Video M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |

*Tabela 11. Registro das execuções de M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-ocorrencias"></a>

## 6. Ocorrências

A Tabela 12 recebe uma linha por problema observado. Atribuição: plataforma, ambiente de teste, executor ou serviço externo, conforme a [atribuição de causa](procedimentos-adaptabilidade.md#72-atribuicao-de-causa). Até o momento após a sessão com os ambientes [`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao)

| ID | Combinação | Ponto de verificação | CE afetado | Descrição | Passos para reproduzir | Gravidade | Atribuição | Reproduzida (2 de 3) | Evidência |
|---|---|---|---|---|---|:-:|---|:-:|---|
| `OC-001` | `M7-A1-J1-FL4` <br> `M7-A1-J2-FL4` <br> `M7-A2-J1-FL4` <br> `M7-A2-J2-FL4` <br> `M7-A4-J1-FL4` <br> `M7-A4-J2-FL4` | `FL4`, `P2` | `CE4.2` | Nome da atividade invisível no progresso (defeito visual, pouco prejudicial). Hipótese da equipe, não confirmada: abrir e fechar a atividade rápido demais, e o sistema registra mas não identifica o nome a tempo | Executar o roteiro de `FL4` até `P2` (seção 6.4 do procedimento) | `Gr1` | Plataforma | Sim (6 de 6 sessões de `FL4`) | [Videos que contenham FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `OC-002` | `M7-A2-J2-FL4` <br> `M7-A4-J1-FL4` | `FL4`, `P2` | `CE4.2` | Controles de anterior e próximo do histórico somem às vezes ao chegar à última página. Ocorreu poucas vezes. Hipótese da equipe, não confirmada: navegação muito rápida | Percorrer o histórico de progresso até a última página (`FL4`, `P2`) | `Gr2` | Plataforma | Não de forma controlada (intermitente): só reapareceu quando não era a intenção | [Videos M7-A2-J2-FL1-FL4 e M7-A4-J1-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `OC-003` | `M7-A4-J1-FL2` <br> `M7-A4-J2-FL2` | `FL2`, `P5` | `CE2.4` | Transcrição ilegível quando a primeira frase ocupa mais de uma linha. Só essa primeira frase é afetada. Atrapalha um pouco quem vai direto à transcrição | Executar o roteiro de `FL2` até `P5` com a primeira frase da transcrição maior que uma linha | `Gr2` | A definir (só aparece em [`A4`](#registro-preparacao)) | Sim (nas 2 sessões de [`A4`](#registro-preparacao), em `J1` e `J2`) | [Videos M7-A4-J1-FL1-FL4 e M7-A4-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |
| `OC-004` | `M7-A4-J2-FL4` | `FL4`, `P2` | `CE4.2` | Linha estranha no histórico (defeito visual, pouco prejudicial). Efeito inédito, não visto em outra sessão | Executar o roteiro de `FL4` até `P2` | `Gr1` | Plataforma | Não (uma ocorrência) | [Videos M7-A2-J2-FL1-FL4](https://drive.google.com/drive/folders/1ujNCfzS-N_-qRWwtbEr2eSqumHExfJiz) |

*Tabela 12. Ocorrências registradas. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*
<a id="registro-resumo"></a>

## 7. Resumo, julgamento e decisão

Os valores abaixo são **parciais**: usam as execuções de 14/11/2026 em [`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao). O ambiente [`A3`](#registro-preparacao) está pendente e não é inviável (`I`), então ainda não entra em `N`. Cálculo e interpretação conforme [Cálculo, interpretação e relato](procedimentos-adaptabilidade.md#9-calculo-interpretacao-e-relato), registrando sempre as contagens absolutas.

**`M6`.** Na Tabela 13, em cada célula, o resultado final (`C`, `F`, `I` ou `X`).

| Ambiente | `FL1` | `FL2` | `FL3` | `FL4` | Concluídas |
|---|:-:|:-:|:-:|:-:|:-:|
| [`A1`](#registro-preparacao) | `C` | `C` | `C` | `C` | 4 / 4 |
| [`A2`](#registro-preparacao) | `C` | `C` | `C` | `C` | 4 / 4 |
| [`A3`](#registro-preparacao) | | | | | Pendente |
| [`A4`](#registro-preparacao) | `C` | `C` | `C` | `C` | 4 / 4 |

*Tabela 13. Matriz de resultados de M6. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

**`M7`.** Na Tabela 14, em cada célula, o resultado (`C`, `F`, `I` ou `X`) e, se houver, a gravidade máxima.

| Ambiente | Dimensão | `FL1` | `FL2` | `FL3` | `FL4` | Preservadas |
|---|---|:-:|:-:|:-:|:-:|:-:|
| [`A1`](#registro-preparacao) | `J1` | `C` | `C` | `C` | `C` (`Gr1`) | 4 / 4 |
| [`A1`](#registro-preparacao) | `J2` | `C` | `C` | `C` | `C` (`Gr1`) | 4 / 4 |
| [`A2`](#registro-preparacao) | `J1` | `C` | `C` | `C` | `C` (`Gr1`) | 4 / 4 |
| [`A2`](#registro-preparacao) | `J2` | `C` | `C` | `C` | `C` (`Gr2`) | 4 / 4 |
| [`A3`](#registro-preparacao) | `J1` | | | | | pendente |
| [`A3`](#registro-preparacao) | `J2` | | | | | pendente |
| [`A4`](#registro-preparacao) | `J1` | `C` | `C` (`Gr2`) | `C` | `C` (`Gr2`) | 4 / 4 |
| [`A4`](#registro-preparacao) | `J2` | `C` | `C` (`Gr2`) | `C` | `C` (`Gr1`) | 4 / 4 |

*Tabela 14. Matriz de resultados de M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

Os `Gr2` de `OC-002` (`A2-J2-FL4` e `A4-J1-FL4`) e de `OC-003` (`A4-J1-FL2` e `A4-J2-FL2`) ficam `C` porque não foram confirmados em 2 de 3 execuções ([4.6](procedimentos-adaptabilidade.md#46-reproducao-de-falhas)).

A Tabela 15 consolida o cálculo de `M6` e `M7` com as contagens absolutas ([4.7](procedimentos-adaptabilidade.md#47-calculo-e-julgamento-de-q5-e-h5) e [5.6](procedimentos-adaptabilidade.md#56-calculo-e-julgamento-de-q6-e-h6)).

| Item | Valor |
|---|---|
| `M6`: concluídas / elegíveis (`C/N`) | 12 / 12 (parcial; com [`A3`](#registro-preparacao), `N` = 16) |
| `M6`: percentual e nota | 100%, nota 3 (parcial) |
| `M7`: preservadas / elegíveis (`C/N`) | 24 / 24 (parcial; com [`A3`](#registro-preparacao), `N` = 32) |
| `M7`: percentual e nota | 100%, nota 3 (parcial) |
| `M7`, subconjunto `FL1`–`FL3` (`C/24`) | 18 / 18 (parcial; com [`A3`](#registro-preparacao), `C/24`) |
| Falha confirmada em `FL1`–`FL3` em algum ambiente? | Não, nos três ambientes executados. A `OC-003` (`Gr2` em `FL2` de [`A4`](#registro-preparacao)) aguarda repetição |

*Tabela 15. Cálculo de M6 e M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

Os percentuais da Tabela 15 só valem como parciais: sem [`A3`](#registro-preparacao), `M6` seria 12 de 16 (75%, nota 1) se [`A3`](#registro-preparacao) fosse contado como não concluído, o que não é o caso, pois ele ainda não foi executado.

A Tabela 16 registra o julgamento de `Q5`, `H5`, `Q6`, `H6` e `G2`, conforme [9.2](procedimentos-adaptabilidade.md#92-interpretacao).

| Questão / hipótese | Estado | Justificativa com contagens |
|---|---|---|
| `Q5` | Atendida (parcial, sem [`A3`](#registro-preparacao)) | `M6` 12 de 12 (100%, nota 3) e nenhuma falha confirmada em `FL1`–`FL3` em [`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao). Falta [`A3`](#registro-preparacao) para fechar |
| `H5` | Sustentada (parcial) | 12 de 12 combinações concluídas (acima de 90%) e condições de `Q5` atendidas nos ambientes executados. Com [`A3`](#registro-preparacao), são necessárias 15 de 16 |
| `Q6` | Atendida (parcial, sem [`A3`](#registro-preparacao)) | `M7` 24 de 24 (100%, nota 3) e nenhum `Gr3`. `Gr1` em `OC-001` e `OC-004`; `Gr2` de `OC-002` e `OC-003` não confirmados, logo `C` |
| `H6` | Sustentada (parcial) | `FL1`–`FL3`: 18 de 18 nos ambientes executados; com [`A3`](#registro-preparacao), são necessárias 22 de 24. Se a `OC-003` for confirmada em `A4-J1-FL2` e `A4-J2-FL2`, cai para 16 de 18 (88,9%) e deixa de ser sustentada na amostra parcial |
| `G2` | Ainda não decidível | Exige `Q5` e `Q6` atendidas; ambas parciais. Faltam [`A3`](#registro-preparacao) e a repetição da `OC-003` |

*Tabela 16. Julgamento de Q5, Q6, H5, H6 e G2. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

A Tabela 17 registra o desfecho de `D1` quanto à adaptabilidade e as ações para a coordenação, conforme [9.4](procedimentos-adaptabilidade.md#94-da-medicao-a-decisao-e-as-acoes).

| Desfecho de `D1` quanto à adaptabilidade | Ações para a coordenação |
|---|---|
| Inconclusivo (provisório): combinações essenciais de [`A3`](#registro-preparacao) não executadas | Completar a execução em [`A3`](#registro-preparacao) antes de decidir. Repetir `T2` e `T3` em `A4-J1-FL2` e `A4-J2-FL2` e definir a atribuição de causa da `OC-003`. Manter `OC-001` a `OC-004` anotadas para a discussão. Com os dados atuais não há falha confirmada em [`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao). A decisão final também depende de `M1`–`M5` |

*Tabela 17. Decisão e ações, conforme [9.4](procedimentos-adaptabilidade.md#94-da-medicao-a-decisao-e-as-acoes). Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## Referências

<a id="s1"></a>

> [S1] Procedimentos de avaliação de adaptabilidade (M6 e M7) — Fase 3. Disponível em: [Procedimentos de adaptabilidade](procedimentos-adaptabilidade.md).

<a id="s2"></a>

> [S2] Ambiente de testes — Fase 3. Disponível em: [Ambiente de testes](ambiente-de-testes.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 07/11/2026 | Estrutura dos formulários de registro de `M6` e `M7`, sem dados coletados. | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.1 | 14/11/2026 | Sessão 1 de avaliação de adaptabilidade [`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao) | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | A definir |
| 1.2 | 14/11/2026 | Computação dos dados tratados para preenchimento das tabelas | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.3 | 15/11/2026 | Resumo parcial de `M6` e `M7` ([`A1`](#registro-preparacao), [`A2`](#registro-preparacao) e [`A4`](#registro-preparacao)), julgamento provisório, regra de `Gr2` sem repetição e correções de formatação. | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |