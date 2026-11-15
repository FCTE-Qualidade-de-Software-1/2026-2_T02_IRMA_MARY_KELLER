# Registro de execuções de eficiência de desempenho (M1 a M5)

**Versão 1.0**

Este documento reúne os formulários e planilhas padronizadas para registro dos dados brutos e resultados consolidados da avaliação de **eficiência de desempenho** da versão web da Khan Academy em computadores, conforme especificado em [Procedimentos de avaliação de eficiência de desempenho (M1 a M5)](procedimentos-desempenho.md) [S1](#s1).

Todas as tabelas de coleta encontram-se atualmente **em branco** e serão preenchidas na Fase 4, mediante *pull requests* submetidos pela equipe avaliadora à medida que cada bateria de testes for concluída no ambiente de referência `A1`. Nenhum resultado foi coletado previamente.

**Instruções de preenchimento:**
1. Mantenha inalterados os identificadores das linhas e colunas;
2. Para o resultado da tentativa (M2), utilize os códigos padronizados: `C` (concluída com sucesso), `F-BLQ` (falha por bloqueio da interface/script), `F-TO` (falha por timeout > 30 s), `F-SOB` (falha por travamento/sobrecarga de CPU) ou `X` (execução inválida por causa externa descartada);
3. Nas colunas de evidência, indique o nome exato do arquivo gerado conforme a convenção de nomenclatura definida na seção 8 de [Procedimentos de desempenho](procedimentos-desempenho.md#8-formularios-e-modelos-de-registro);
4. Havendo anomalia ou falha técnica, atribua um identificador sequencial de ocorrência (`OC-DES-001`, `OC-DES-002`, ...) e preencha a respectiva linha na [Tabela de ocorrências](#registro-ocorrencias);
5. As linhas de aquecimento (`W`) servem apenas para estabilização prévia e seus valores são anotados mas **não entram** no cálculo das medianas, do P90 e das médias de recursos.

<a id="registro-preparacao"></a>

## 1. Preparação do ambiente de referência (A1)

A Tabela 1 registra as características do ambiente `A1`, conforme definido no [Ambiente de testes](ambiente-de-testes.md) [S2](#s2).

| Parâmetro de configuração | Valor especificado | Valor verificado no ensaio | Situação |
|---|---|---|:---:|
| Sistema Operacional convidado | Windows 11 Pro 64-bit | | |
| *Build* exata do sistema | A registrar na preparação | | |
| Navegador e motor | Google Chrome 157.0 (Blink) | | |
| Modalidade de execução | Virtualizado (Docker / Winboat) | | |
| Alocação de memória RAM | 4 GB | | |
| Alocação de vCPUs | 4 vCPUs | | |
| Resolução de tela e janela | 1920 × 1080 pixels (`J2`), maximizada | | |
| Nível de zoom | 100% | | |
| Data da preparação formal | A registrar | | |
| Responsável pela preparação | A registrar | | |

*Tabela 1. Verificação do ambiente de referência A1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

A Tabela 2 registra o atendimento às verificações prévias de preparação (`PD-1` a `PD-10`). Marque `S` para atendida ou `N` para não atendida.

| ID da sessão | PD-1 | PD-2 | PD-3 | PD-4 | PD-5 | PD-6 | PD-7 | PD-8 | PD-9 | PD-10 | Observações operacionais |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Preparação Geral A1 | | | | | | | | | | | |

*Tabela 2. Checklist de preparação do ambiente A1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-dados"></a>

## 2. Dados de teste congelados

A Tabela 3 documenta os valores e URLs congeladas antes do início das medições para garantir repetibilidade estrita.

| ID | Elemento de teste | Valor / Identificador congelado | Data do congelamento |
|---|---|---|---|
| `D1` | Disciplina | | |
| `D2` | Curso | | |
| `D3` | Unidade e aula | | |
| `D4` | Videoaula (com legenda e transcrição) | | |
| `D5` | Exercício (com suporte a dicas) | | |
| `D6` | Conta de teste (login/usuário) | | |

*Tabela 3. Massa de dados congelada para os ensaios de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-rede"></a>

## 3. Verificação das condições de conectividade de rede

A Tabela 4 documenta a calibração da conexão do laboratório e os parâmetros aplicados no emulador de tráfego.

| Condição experimental | Download medido / configurado | Upload medido / configurado | Latência (RTT) | Data da calibração | Responsável |
|---|:---:|:---:|:---:|:---:|---|
| **Rede Normal (sem limitação)** | Mbps | Mbps | ms | | |
| **Rede Limitada (Throttling)** | 1.500 kbps (1,5 Mbps) | 750 kbps (0,75 Mbps) | 150 ms adicionais | | |

*Tabela 4. Condições de conectividade registradas. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-fl1"></a>

## 4. Registro de execuções de FL1 — Navegação em cursos

### 4.1 Bateria FL1 sob Rede Normal

A Tabela 5 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL1` em conexão normal.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E1.1 (s) | Tempo E1.2 (s) | Tempo E1.3 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| `W-FL1-NORM` | | | | | | | | | | | | |
| `R1-FL1-NORM` | | | | | | | | | | | | |
| `R2-FL1-NORM` | | | | | | | | | | | | |
| `R3-FL1-NORM` | | | | | | | | | | | | |
| `R4-FL1-NORM` | | | | | | | | | | | | |
| `R5-FL1-NORM` | | | | | | | | | | | | |

*Tabela 5. Registro bruto de FL1 sob Rede Normal. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 4.2 Bateria FL1 sob Rede Limitada

A Tabela 6 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL1` em conexão limitada.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E1.1 (s) | Tempo E1.2 (s) | Tempo E1.3 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| `W-FL1-LIM` | | | | | | | | | | | | |
| `R1-FL1-LIM` | | | | | | | | | | | | |
| `R2-FL1-LIM` | | | | | | | | | | | | |
| `R3-FL1-LIM` | | | | | | | | | | | | |
| `R4-FL1-LIM` | | | | | | | | | | | | |
| `R5-FL1-LIM` | | | | | | | | | | | | |

*Tabela 6. Registro bruto de FL1 sob Rede Limitada. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-fl2"></a>

## 5. Registro de execuções de FL2 — Videoaulas

### 5.1 Bateria FL2 sob Rede Normal

A Tabela 7 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL2` em conexão normal.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E2.1 (s) | Tempo E2.2 (s) | Tempo E2.3 (s) | Tempo E2.4 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| `W-FL2-NORM` | | | | | | | | | | | | | |
| `R1-FL2-NORM` | | | | | | | | | | | | | |
| `R2-FL2-NORM` | | | | | | | | | | | | | |
| `R3-FL2-NORM` | | | | | | | | | | | | | |
| `R4-FL2-NORM` | | | | | | | | | | | | | |
| `R5-FL2-NORM` | | | | | | | | | | | | | |

*Tabela 7. Registro bruto de FL2 sob Rede Normal. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 5.2 Bateria FL2 sob Rede Limitada

A Tabela 8 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL2` em conexão limitada.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E2.1 (s) | Tempo E2.2 (s) | Tempo E2.3 (s) | Tempo E2.4 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| `W-FL2-LIM` | | | | | | | | | | | | | |
| `R1-FL2-LIM` | | | | | | | | | | | | | |
| `R2-FL2-LIM` | | | | | | | | | | | | | |
| `R3-FL2-LIM` | | | | | | | | | | | | | |
| `R4-FL2-LIM` | | | | | | | | | | | | | |
| `R5-FL2-LIM` | | | | | | | | | | | | | |

*Tabela 8. Registro bruto de FL2 sob Rede Limitada. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-fl3"></a>

## 6. Registro de execuções de FL3 — Exercícios

### 6.1 Bateria FL3 sob Rede Normal

A Tabela 9 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL3` em conexão normal.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E3.1 (s) | Tempo E3.2 (s) | Tempo E3.3 (s) | Tempo E3.4 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| `W-FL3-NORM` | | | | | | | | | | | | | |
| `R1-FL3-NORM` | | | | | | | | | | | | | |
| `R2-FL3-NORM` | | | | | | | | | | | | | |
| `R3-FL3-NORM` | | | | | | | | | | | | | |
| `R4-FL3-NORM` | | | | | | | | | | | | | |
| `R5-FL3-NORM` | | | | | | | | | | | | | |

*Tabela 9. Registro bruto de FL3 sob Rede Normal. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 6.2 Bateria FL3 sob Rede Limitada

A Tabela 10 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL3` em conexão limitada.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E3.1 (s) | Tempo E3.2 (s) | Tempo E3.3 (s) | Tempo E3.4 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| `W-FL3-LIM` | | | | | | | | | | | | | |
| `R1-FL3-LIM` | | | | | | | | | | | | | |
| `R2-FL3-LIM` | | | | | | | | | | | | | |
| `R3-FL3-LIM` | | | | | | | | | | | | | |
| `R4-FL3-LIM` | | | | | | | | | | | | | |
| `R5-FL3-LIM` | | | | | | | | | | | | | |

*Tabela 10. Registro bruto de FL3 sob Rede Limitada. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-lighthouse"></a>

## 7. Registro de auditoria complementar com Lighthouse

A Tabela 11 documenta os indicadores de laboratório gerados pela auditoria do Lighthouse nas páginas de entrada dos fluxos sob condições de rede normal e limitada.

| Página avaliada | Condição de rede | Performance Score (0–100) | First Contentful Paint - FCP (s) | Largest Contentful Paint - LCP (s) | Total Blocking Time - TBT (ms) | Speed Index (s) | Arquivo de relatório (.json / .html) |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| Curso `D2` (FL1) | Rede Normal | | | | | | |
| Curso `D2` (FL1) | Rede Limitada | | | | | | |
| Videoaula `D4` (FL2) | Rede Normal | | | | | | |
| Videoaula `D4` (FL2) | Rede Limitada | | | | | | |
| Exercício `D5` (FL3) | Rede Normal | | | | | | |
| Exercício `D5` (FL3) | Rede Limitada | | | | | | |

*Tabela 11. Resultados da auditoria complementar Lighthouse. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-ocorrencias"></a>

## 8. Tabela de ocorrências de desempenho

A Tabela 12 reúne todas as falhas, anomalias, picos anormais de carga ou ocorrências impeditivas identificadas durante os ensaios de desempenho.

| ID Ocorrência | Bateria / Repetição | Etapa | Descrição detalhada do comportamento | Gravidade | Atribuição da causa | Impacto na repetição | Evidência (.png / .log) |
|---|---|---|---|:---:|---|---|---|
| `OC-DES-001` | | | | | | | |
| `OC-DES-002` | | | | | | | |
| `OC-DES-003` | | | | | | | |
| `OC-DES-004` | | | | | | | |
| `OC-DES-005` | | | | | | | |

*Tabela 12. Ocorrências registradas na avaliação de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-resumo"></a>

## 9. Resumo estatístico, julgamento e decisões

Esta seção consolida os indicadores derivados das cinco repetições válidas de cada fluxo e condição de rede, confrontando-os com as faixas de pontuação e critérios de julgamento estabelecidos.

### 9.1 Consolidação de M1 — Tempo observável por etapa

A Tabela 13 consolida a mediana e o P90 de cada etapa avaliada, convertendo o resultado na nota correspondente (0 a 3).

| Fluxo | Etapa do roteiro | Condição de rede | Mediana observada (s) | P90 observado (s) | Faixa de julgamento atingida | Nota M1 (0–3) |
|:---:|---|---|:---:|:---:|---|:---:|
| `FL1` | E1.1 (Catálogo inicial) | Rede Normal | | | | |
| `FL1` | E1.1 (Catálogo inicial) | Rede Limitada | | | | |
| `FL1` | E1.2 (Grade do curso) | Rede Normal | | | | |
| `FL1` | E1.2 (Grade do curso) | Rede Limitada | | | | |
| `FL1` | E1.3 (Ambiente da aula) | Rede Normal | | | | |
| `FL1` | E1.3 (Ambiente da aula) | Rede Limitada | | | | |
| `FL2` | E2.1 (Interface do player) | Rede Normal | | | | |
| `FL2` | E2.1 (Interface do player) | Rede Limitada | | | | |
| `FL2` | E2.2 (Disparo do vídeo) | Rede Normal | | | | |
| `FL2` | E2.2 (Disparo do vídeo) | Rede Limitada | | | | |
| `FL2` | E2.3 (Legenda) | Rede Normal | | | | |
| `FL2` | E2.3 (Legenda) | Rede Limitada | | | | |
| `FL2` | E2.4 (Transcrição) | Rede Normal | | | | |
| `FL2` | E2.4 (Transcrição) | Rede Limitada | | | | |
| `FL3` | E3.1 (Abertura do exercício) | Rede Normal | | | | |
| `FL3` | E3.1 (Abertura do exercício) | Rede Limitada | | | | |
| `FL3` | E3.2 (Exibição da dica) | Rede Normal | | | | |
| `FL3` | E3.2 (Exibição da dica) | Rede Limitada | | | | |
| `FL3` | E3.3 (Envio e feedback) | Rede Normal | | | | |
| `FL3` | E3.3 (Envio e feedback) | Rede Limitada | | | | |
| `FL3` | E3.4 (Próxima atividade) | Rede Normal | | | | |
| `FL3` | E3.4 (Próxima atividade) | Rede Limitada | | | | |

*Tabela 13. Consolidação estatística e notas de M1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.2 Consolidação de M2 — Taxa de conclusão das tentativas

A Tabela 14 resume o índice de sucesso operacional obtido para cada fluxo e condição de rede.

| Fluxo | Condição de rede | Tentativas elegíveis ($N$) | Tentativas concluídas ($C$) | Taxa $M2 = 100 \times C/N$ (%) | Ocorrência de bloqueio essencial? | Nota M2 (0–3) |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| `FL1` | Rede Normal | | | | | |
| `FL1` | Rede Limitada | | | | | |
| `FL2` | Rede Normal | | | | | |
| `FL2` | Rede Limitada | | | | | |
| `FL3` | Rede Normal | | | | | |
| `FL3` | Rede Limitada | | | | | |
| **Total** | **Geral consolidado** | | | | | |

*Tabela 14. Consolidação da taxa de conclusão M2. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.3 Consolidação de M3 — Utilização de CPU

A Tabela 15 consolida a demanda média e os picos de processamento registrados.

| Fluxo | Condição de rede | Média de CPU apurada (%) | Maior pico instantâneo (%) | Houve sobrecarga > 75%? | Nota M3 (0–3) |
|:---:|---|:---:|:---:|:---:|:---:|
| `FL1` | Rede Normal | | | | |
| `FL1` | Rede Limitada | | | | |
| `FL2` | Rede Normal | | | | |
| `FL2` | Rede Limitada | | | | |
| `FL3` | Rede Normal | | | | |
| `FL3` | Rede Limitada | | | | |

*Tabela 15. Consolidação da utilização de CPU M3. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.4 Consolidação de M4 — Pico de memória

A Tabela 16 consolida o maior pico individual de memória privada alocada nos processos da aba.

| Fluxo | Condição de rede | Maior pico de memória $\max(\text{RAM}(t))$ (MiB) | Média dos picos (MiB) | Risco de esgotamento observado? | Nota M4 (0–3) |
|:---:|---|:---:|:---:|:---:|:---:|
| `FL1` | Rede Normal | | | | |
| `FL1` | Rede Limitada | | | | |
| `FL2` | Rede Normal | | | | |
| `FL2` | Rede Limitada | | | | |
| `FL3` | Rede Normal | | | | |
| `FL3` | Rede Limitada | | | | |

*Tabela 16. Consolidação do consumo de memória M4. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.5 Consolidação de M5 — Dados transferidos

A Tabela 17 consolida o tráfego médio e mediano de rede transmitido para a conclusão de cada fluxo padronizado.

| Fluxo | Condição de rede | Volume mediano transferido (MiB) | Maior volume observado (MiB) | Orçamento ≤ 10 MiB respeitado? | Nota M5 (0–3) |
|:---:|---|:---:|:---:|:---:|:---:|
| `FL1` | Rede Normal | | | | |
| `FL1` | Rede Limitada | | | | |
| `FL2` | Rede Normal | | | | |
| `FL2` | Rede Limitada | | | | |
| `FL3` | Rede Normal | | | | |
| `FL3` | Rede Limitada | | | | |

*Tabela 17. Consolidação de dados transferidos M5. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.6 Julgamento das questões Q1 a Q4, hipóteses H1 a H4 e objetivo G1

A Tabela 18 registra a classificação final de cada questão, hipótese e o atendimento global do objetivo `G1`.

| Questão / Hipótese | Métricas de suporte | Estado formal | Justificativa com base nos dados consolidados |
|---|---|---|---|
| **Questão Q1** (Espera nas etapas) | M1, M2 | Atendida / Não atendida / Inconclusiva | |
| **Hipótese H1** (Mediana ≤ 3 s e Conclusão ≥ 90%) | M1, M2 | Sustentada / Não sustentada / Inconclusiva | |
| **Questão Q2** (Processamento disponível) | M3 | Atendida / Não atendida / Inconclusiva | |
| **Hipótese H2** (CPU média ≤ 50%) | M3 | Sustentada / Não sustentada / Inconclusiva | |
| **Questão Q3** (Memória disponível) | M4 | Atendida / Não atendida / Inconclusiva | |
| **Hipótese H3** (Pico de RAM ≤ 1024 MiB) | M4 | Sustentada / Não sustentada / Inconclusiva | |
| **Questão Q4** (Orçamento de acesso) | M5 | Atendida / Não atendida / Inconclusiva | |
| **Hipótese H4** (Volume transferido ≤ 10 MiB) | M5 | Sustentada / Não sustentada / Inconclusiva | |
| **Objetivo G1** (Eficiência de desempenho) | M1 a M5 | Atendido / Não atendido | |

*Tabela 18. Julgamento formal de Q1–Q4, H1–H4 e objetivo G1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.7 Desfecho para a Decisão D1 e recomendações práticas

A Tabela 19 documenta a conversão dos achados no desfecho da decisão `D1` e orientações concretas para a coordenação da escola pública.

| Desfecho para a Decisão `D1` | Recomendações e orientações práticas para a coordenação escolar |
|---|---|
| *A preencher na Fase 4* | *A preencher na Fase 4* |

*Tabela 19. Desfecho da decisão D1 e ações para o requisitante escolar. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## Referências

<a id="s1"></a>

> [S1] Procedimentos de avaliação de eficiência de desempenho (M1 a M5) — Fase 3. Disponível em: [Procedimentos de desempenho](procedimentos-desempenho.md).

<a id="s2"></a>

> [S2] Ambiente de testes e ferramentas de avaliação — Fase 3. Disponível em: [Ambiente de testes](ambiente-de-testes.md).

<a id="s3"></a>

> [S3] Critérios de julgamento — Fase 2. Disponível em: [Critérios de julgamento](../fase-2/criterios-julgamento.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 08/11/2026 | Estruturação inicial das planilhas e formulários de registro para eficiência de desempenho (M1 a M5), sem resultados coletados. | [José Augusto](https://github.com/JAugustoM) | [Pedro Lucas](https://github.com/Pwdrinho) |
