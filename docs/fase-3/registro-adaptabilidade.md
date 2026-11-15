# Registro de execuções (M6 e M7)

**Versão 1.0**

Esta página reúne os formulários de registro da avaliação de adaptabilidade definida em [Procedimentos de avaliação de adaptabilidade](procedimentos-adaptabilidade.md) [S1](#s1). As tabelas estão **em branco** e serão preenchidas na Fase 4, por *pull request*, conforme cada execução. Nenhum resultado foi coletado.

**Como preencher.** Mantenha os identificadores das linhas. Use os códigos de resultado `C` (concluída), `F` (falha), `I` (inviável) e `X` (inválida), definidos em [4.3](procedimentos-adaptabilidade.md#43-passos-de-execucao). Em `F`, indique `F-BLQ` ou `F-AJ`. Nas colunas de evidência, cite o nome do arquivo conforme o padrão da [seção 8](procedimentos-adaptabilidade.md#8-formularios-e-modelos-de-registro). Cada ocorrência recebe um `id_ocorrencia` (`OC-001`, `OC-002`, ...) usado nas tabelas de M6 e M7 e na [tabela de ocorrências](#registro-ocorrencias).

<a id="registro-preparacao"></a>

## 1. Preparação dos ambientes

A Tabela 1 identifica cada ambiente, com os dados já conhecidos do [ambiente de testes](ambiente-de-testes.md) [S2](#s2).

| ID | Sistema operacional | Navegador | Versão | Modalidade | Recursos | Data da preparação | Responsável | Build do sistema |
|---|---|---|---|---|---|---|---|---|
| `A1` | Windows 11 Pro | Google Chrome | 157.0 | Virtualizado (Docker, Winboat) | 4 GB, 4 vCPUs | | | |
| `A2` | Windows 11 Pro | Mozilla Firefox | 159.1 | Virtualizado (Docker, Winboat) | 4 GB, 4 vCPUs | | | |
| `A3` | macOS (a registrar) | Apple Safari | (a registrar) | Computador real | (a registrar) | | | |
| `A4` | Ubuntu 26.04 | Mozilla Firefox | 159.0 | Virtualizado (QEMU/KVM, Gnome Boxes) | 4 GB, 4 vCPUs | | | |

*Tabela 1. Identificação dos ambientes de teste. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM), com base no [ambiente de testes](ambiente-de-testes.md)*

A Tabela 2 registra as verificações de [preparação](procedimentos-adaptabilidade.md#34-preparacao-do-ambiente). Marque `S` quando atendida.

| ID | PA-1 | PA-2 | PA-3 | PA-4 | PA-5 | PA-6 | PA-7 | PA-8 | PA-9 | PA-10 | Observações |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| `A1` | | | | | | | | | | | |
| `A2` | | | | | | | | | | | |
| `A3` | | | | | | | | | | | |
| `A4` | | | | | | | | | | | |

*Tabela 2. Verificações de preparação por ambiente. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-rotulos"></a>

## 2. Dados de teste congelados e rótulos dos controles

A Tabela 3 registra os dados de teste da [preparação](procedimentos-adaptabilidade.md#34-preparacao-do-ambiente), iguais em todos os ambientes.

| ID | Dado | Valor congelado | Data do congelamento |
|---|---|---|---|
| `D1` | Disciplina | | |
| `D2` | Curso | | |
| `D3` | Unidade e aula | | |
| `D4` | Videoaula (com legenda e transcrição) | | |
| `D5` | Exercício (com dica) | | |
| `D6` | Conta de teste (identificador, sem senha) | | |

*Tabela 3. Dados de teste congelados. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

A Tabela 4 registra o rótulo real de cada item do [inventário de controles essenciais](procedimentos-adaptabilidade.md#54-inventario-de-controles-essenciais) na interface em uso.

| ID | Conteúdo ou controle essencial | Rótulo real na interface |
|---|---|---|
| `CE1.1` | Menu ou busca para localizar a disciplina | |
| `CE1.2` | Item do curso-alvo | |
| `CE1.3` | Lista de unidades e aulas do curso | |
| `CE1.4` | Conteúdo da aula selecionada | |
| `CE2.1` | Área do vídeo e barra de reprodução | |
| `CE2.2` | Controle de iniciar e pausar | |
| `CE2.3` | Controle de legenda | |
| `CE2.4` | Acesso à transcrição | |
| `CE3.1` | Enunciado e área de resposta | |
| `CE3.2` | Controle de dica | |
| `CE3.3` | Controle de envio da resposta | |
| `CE3.4` | Retorno da plataforma e controle de continuidade | |
| `CE4.1` | Acesso à área do estudante | |
| `CE4.2` | Informações de progresso | |

*Tabela 4. Rótulos reais dos controles essenciais. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-resolucao"></a>

## 3. Resolução verificada

A Tabela 5 registra o resultado do comando de [3.5](procedimentos-adaptabilidade.md#35-resolucao-e-janela) ao início das sessões de cada ambiente e dimensão. Se algum valor mudar durante a coleta, acrescente uma linha com a data.

| Ambiente | Dimensão | `screen` (largura × altura) | `inner` (largura × altura) | `dpr` | Data |
|---|---|---|---|---|---|
| `A1` | `J1` (1366 × 768) | | | | |
| `A1` | `J2` (1920 × 1080) | | | | |
| `A2` | `J1` (1366 × 768) | | | | |
| `A2` | `J2` (1920 × 1080) | | | | |
| `A3` | `J1` (1366 × 768) | | | | |
| `A3` | `J2` (1920 × 1080) | | | | |
| `A4` | `J1` (1366 × 768) | | | | |
| `A4` | `J2` (1920 × 1080) | | | | |

*Tabela 5. Resolução e viewport verificados por ambiente e dimensão. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-m6"></a>

## 4. Registro de M6

A Tabela 6 registra as execuções em `J2` (1920 × 1080). `T1` a `T3` são os resultados das tentativas ([reprodução de falhas](procedimentos-adaptabilidade.md#46-reproducao-de-falhas)); o resultado final é `C` salvo falha confirmada em 2 de 3.

| ID | Data | Executor / observador | T1 | T2 | T3 | Final | Tipo de falha | Ocorrência | Evidência |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|---|
| `M6-A1-FL1` | | | | | | | | | |
| `M6-A1-FL2` | | | | | | | | | |
| `M6-A1-FL3` | | | | | | | | | |
| `M6-A1-FL4` | | | | | | | | | |
| `M6-A2-FL1` | | | | | | | | | |
| `M6-A2-FL2` | | | | | | | | | |
| `M6-A2-FL3` | | | | | | | | | |
| `M6-A2-FL4` | | | | | | | | | |
| `M6-A3-FL1` | | | | | | | | | |
| `M6-A3-FL2` | | | | | | | | | |
| `M6-A3-FL3` | | | | | | | | | |
| `M6-A3-FL4` | | | | | | | | | |
| `M6-A4-FL1` | | | | | | | | | |
| `M6-A4-FL2` | | | | | | | | | |
| `M6-A4-FL3` | | | | | | | | | |
| `M6-A4-FL4` | | | | | | | | | |

*Tabela 6. Registro das execuções de M6. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-m7"></a>

## 5. Registro de M7

A Tabela 7 registra as execuções de M7. A gravidade máxima segue a [escala `G1` a `G3`](procedimentos-adaptabilidade.md#55-problemas-de-adaptacao-e-gravidade); use `G0` quando não houver problema. As linhas em `J2` aproveitam a sessão de M6, com critério próprio.

| ID | Data | Executor / observador | Resultado | Gravidade máxima | CE afetados | Ocorrência | Evidência |
|---|---|---|:-:|:-:|---|---|---|
| `M7-A1-J1-FL1` | | | | | | | |
| `M7-A1-J1-FL2` | | | | | | | |
| `M7-A1-J1-FL3` | | | | | | | |
| `M7-A1-J1-FL4` | | | | | | | |
| `M7-A1-J2-FL1` | | | | | | | |
| `M7-A1-J2-FL2` | | | | | | | |
| `M7-A1-J2-FL3` | | | | | | | |
| `M7-A1-J2-FL4` | | | | | | | |
| `M7-A2-J1-FL1` | | | | | | | |
| `M7-A2-J1-FL2` | | | | | | | |
| `M7-A2-J1-FL3` | | | | | | | |
| `M7-A2-J1-FL4` | | | | | | | |
| `M7-A2-J2-FL1` | | | | | | | |
| `M7-A2-J2-FL2` | | | | | | | |
| `M7-A2-J2-FL3` | | | | | | | |
| `M7-A2-J2-FL4` | | | | | | | |
| `M7-A3-J1-FL1` | | | | | | | |
| `M7-A3-J1-FL2` | | | | | | | |
| `M7-A3-J1-FL3` | | | | | | | |
| `M7-A3-J1-FL4` | | | | | | | |
| `M7-A3-J2-FL1` | | | | | | | |
| `M7-A3-J2-FL2` | | | | | | | |
| `M7-A3-J2-FL3` | | | | | | | |
| `M7-A3-J2-FL4` | | | | | | | |
| `M7-A4-J1-FL1` | | | | | | | |
| `M7-A4-J1-FL2` | | | | | | | |
| `M7-A4-J1-FL3` | | | | | | | |
| `M7-A4-J1-FL4` | | | | | | | |
| `M7-A4-J2-FL1` | | | | | | | |
| `M7-A4-J2-FL2` | | | | | | | |
| `M7-A4-J2-FL3` | | | | | | | |
| `M7-A4-J2-FL4` | | | | | | | |

*Tabela 7. Registro das execuções de M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-ocorrencias"></a>

## 6. Ocorrências

A Tabela 8 recebe uma linha por problema observado. Atribuição: plataforma, ambiente de teste, executor ou serviço externo, conforme a [atribuição de causa](procedimentos-adaptabilidade.md#72-atribuicao-de-causa).

| ID | Combinação | Ponto de verificação | CE afetado | Descrição | Passos para reproduzir | Gravidade | Atribuição | Reproduzida (2 de 3) | Evidência |
|---|---|---|---|---|---|:-:|---|:-:|---|
| `OC-001` | | | | | | | | | |
| `OC-002` | | | | | | | | | |
| `OC-003` | | | | | | | | | |
| `OC-004` | | | | | | | | | |
| `OC-005` | | | | | | | | | |

*Tabela 8. Ocorrências registradas. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

<a id="registro-resumo"></a>

## 7. Resumo, julgamento e decisão

Preencher após a coleta, conforme [Cálculo, interpretação e relato](procedimentos-adaptabilidade.md#9-calculo-interpretacao-e-relato). Registrar sempre as contagens absolutas.

**M6.** Na Tabela 9, em cada célula, o resultado final (`C`, `F`, `I` ou `X`).

| Ambiente | FL1 | FL2 | FL3 | FL4 | Concluídas |
|---|:-:|:-:|:-:|:-:|:-:|
| `A1` | | | | | / 4 |
| `A2` | | | | | / 4 |
| `A3` | | | | | / 4 |
| `A4` | | | | | / 4 |

*Tabela 9. Matriz de resultados de M6. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

**M7.** Na Tabela 10, em cada célula, o resultado (`C`, `F`, `I` ou `X`) e, se houver, a gravidade máxima.

| Ambiente | Dimensão | FL1 | FL2 | FL3 | FL4 | Preservadas |
|---|---|:-:|:-:|:-:|:-:|:-:|
| `A1` | `J1` | | | | | / 4 |
| `A1` | `J2` | | | | | / 4 |
| `A2` | `J1` | | | | | / 4 |
| `A2` | `J2` | | | | | / 4 |
| `A3` | `J1` | | | | | / 4 |
| `A3` | `J2` | | | | | / 4 |
| `A4` | `J1` | | | | | / 4 |
| `A4` | `J2` | | | | | / 4 |

*Tabela 10. Matriz de resultados de M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

A Tabela 11 consolida o cálculo, a Tabela 12 registra o julgamento de cada questão e hipótese e a Tabela 13, a decisão e as ações.

| Item | Valor |
|---|---|
| M6: concluídas / elegíveis (`C/N`) | |
| M6: percentual e nota | |
| M7: preservadas / elegíveis (`C/N`) | |
| M7: percentual e nota | |
| M7, subconjunto `FL1`–`FL3` (`C/24`) | |
| Falha confirmada em `FL1`–`FL3` em algum ambiente? | |

*Tabela 11. Cálculo de M6 e M7. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

| Questão / hipótese | Estado | Justificativa com contagens |
|---|---|---|
| `Q5` | Atendida / não atendida / inconclusiva | |
| `H5` | Sustentada / não sustentada / inconclusiva | |
| `Q6` | Atendida / não atendida / inconclusiva | |
| `H6` | Sustentada / não sustentada / inconclusiva | |
| `G2` | Atendido / não atendido | |

*Tabela 12. Julgamento de Q5, Q6, H5, H6 e G2. Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

| Desfecho de `D1` quanto à adaptabilidade | Ações para a coordenação |
|---|---|
| | |

*Tabela 13. Decisão e ações, conforme [9.4](procedimentos-adaptabilidade.md#94-da-medicao-a-decisao-e-as-acoes). Fonte: Elaborada por: [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM)*

## Referências

<a id="s1"></a>

> [S1] Procedimentos de avaliação de adaptabilidade (M6 e M7) — Fase 3. Disponível em: [Procedimentos de adaptabilidade](procedimentos-adaptabilidade.md).

<a id="s2"></a>

> [S2] Ambiente de testes — Fase 3. Disponível em: [Ambiente de testes](ambiente-de-testes.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 07/11/2026 | Estrutura dos formulários de registro de M6 e M7, sem dados coletados. | [Pedro Lucas](https://github.com/Pwdrinho) e [José Augusto](https://github.com/JAugustoM) | A definir |