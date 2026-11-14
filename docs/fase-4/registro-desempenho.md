# Registro de execuções de eficiência de desempenho (M1 a M5)

**Versão 1.3**

Este documento reúne os formulários e planilhas padronizadas para registro dos dados brutos e resultados consolidados da avaliação de **eficiência de desempenho** da versão web da Khan Academy em computadores, conforme especificado em [Procedimentos de avaliação de eficiência de desempenho (M1 a M5)](../fase-3/procedimentos-desempenho.md) [S1](#s1).

Todas as tabelas de coleta e julgamento foram devidamente preenchidas na Fase 4 com os dados coletados nos ensaios no ambiente de referência `A1`, contemplando ensaios manuais, testes de laboratório (Lighthouse) e a consolidação das hipóteses e decisão `D1`.

**Instruções de preenchimento:**
1. Mantenha inalterados os identificadores das linhas e colunas;
2. Para o resultado da tentativa (M2), utilize os códigos padronizados: `C` (concluída com sucesso), `F-BLQ` (falha por bloqueio da interface/script), `F-TO` (falha por timeout > 30 s), `F-SOB` (falha por travamento/sobrecarga de CPU) ou `X` (execução inválida por causa externa descartada);
3. Nas colunas de evidência, indique o nome exato do arquivo gerado conforme a convenção de nomenclatura definida na seção 8 de [Procedimentos de desempenho](../fase-3/procedimentos-desempenho.md#8-formularios-e-modelos-de-registro);
4. Havendo anomalia ou falha técnica, atribua um identificador sequencial de ocorrência (`OC-DES-001`, `OC-DES-002`, ...) e preencha a respectiva linha na [Tabela de ocorrências](#registro-ocorrencias);
5. As linhas de aquecimento (`W`) servem apenas para estabilização prévia e seus valores são anotados mas **não entram** no cálculo das medianas, do P90 e das médias de recursos.

<a id="registro-preparacao"></a>

## 1. Preparação do ambiente de referência (A1)

<!-- Simplificar essas tabelas -->

A Tabela 1 registra as características do ambiente `A1`, conforme definido no [Ambiente de testes](../fase-3/ambiente-de-testes.md) [S2](#s2).

| Parâmetro de configuração     | Valor especificado                    | Valor verificado no ensaio | Situação |
| ----------------------------- | ------------------------------------- | -------------------------- | :------: |
| Sistema Operacional convidado | Windows 11 Pro 64-bit                 | Windows 11 Pro 64-bit      | Conforme |
| *Build* exata do sistema      | 26200| 26200 | Conforme |
| Navegador e motor             | Google Chrome 157.0                   | Google Chrome 157.0        | Conforme |
| Modalidade de execução        | Virtualizado (Docker / Winboat)       | Virtualizado (Docker / Winboat) | Conforme |
| Alocação de memória RAM       | 4 GB                                  | 4 GB | Conforme |
| Alocação de vCPUs             | 4 vCPUs                               | 4 vCPUs | Conforme |
| Resolução de tela e janela    | 1920 × 1080 pixels (`J2`), maximizada | 1920 × 1080 pixels (`J2`), maximizada | Conforme |
| Nível de zoom                 | 100% | 100% | Conforme |
| Data da preparação formal     | 11/11/2026 | 11/11/2026 | Conforme |
| Responsável pela preparação   | José Augusto | José Augusto | Conforme |

*Tabela 1. Verificação do ambiente de referência A1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

A Tabela 2 registra o atendimento às verificações prévias de preparação (`PD-1` a `PD-10`). Marque `S` para atendida ou `N` para não atendida.

| ID da sessão        | PD-1  | PD-2  | PD-3  | PD-4  | PD-5  | PD-6  | PD-7  | PD-8  | PD-9  | PD-10 | Observações operacionais |
| ------------------- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | ------------------------ |
| Preparação Geral A1 | S     | S     | S     | S     | S     | S     | S     | S     | S     | S     | -                        |

*Tabela 2. Checklist de preparação do ambiente A1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-dados"></a>

## 2. Dados de teste congelados

A Tabela 3 documenta os valores e URLs congeladas antes do início das medições para garantir repetibilidade estrita.

| ID   | Elemento de teste                     | Valor / Identificador congelado                           | Data do congelamento |
| ---- | ------------------------------------- | --------------------------------------------------------- | -------------------- |
| `D1` | Disciplina | https://pt.khanacademy.org/computing | 11/11/2026 |
| `D2` | Curso | https://pt.khanacademy.org/computing/computer-programming | 11/11/2026 |
| `D3` | Unidade e aula | https://pt.khanacademy.org/computing/computer-programming/programming | 11/11/2026 |
| `D4` | Videoaula (com transcrição) | https://pt.khanacademy.org/computing/computer-programming/programming/drawing-basics/pt/making-drawings-with-code | 11/11/2026 |
| `D5` | Exercício (com suporte a dicas) | https://pt.khanacademy.org/computing/computer-programming/programming/drawing-basics/pc/challenge-simple-snowman | 11/11/2026 |
| `D6` | Conta de teste (login/usuário) | José Moraes  | 11/11/2026 |

*Tabela 3. Massa de dados congelada para os ensaios de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-rede"></a>

## 3. Verificação das condições de conectividade de rede

A Tabela 4 documenta a calibração da conexão do laboratório e os parâmetros aplicados no emulador de tráfego.

| Condição experimental | Download medido / configurado | Upload medido / configurado | Latência (RTT) | Data da calibração | Responsável |
| --------------------- | :---------------------------: | :-------------------------: | :------------: | :----------------: | ----------- |
| **Rede Normal (sem limitação)** | 290,92 Mbps | 296,47 Mbps | 78 ms | 11/11/2026 | José Augusto |
| **Rede Limitada (Throttling)**  | 1,5 Mbps | 0,75 Mbps | 150 ms adicionais | 11/11/2026 | José Augusto|

*Tabela 4. Condições de conectividade registradas. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-fl1"></a>

## 4. Registro de execuções de FL1 — Navegação em cursos

### 4.1 Bateria FL1 sob Rede Normal

A Tabela 5 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL1` em conexão normal.

| ID Repetição  | Data / Hora | Avaliador / Observador | Tempo E1.1 (s) | Tempo E1.2 (s) | Tempo E1.3 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
| ------------- | ----------- | ---------------------- | :------------: | :------------: | :------------: | :----------: | :--------------: | :-------------: | :---------------: | :------------: | ---------------------------------- | :--------: |
| `W-FL1-NORM`  | 13/11/2026 11:32 | José Augusto | 2,28 | 2,14 | - | C | 14,2 | 38,5 | 210 | 3,39 | [har](evidencias/desempenho/manual/FL1/NORM/W-FL1-NORM.har)/[jpg](evidencias/desempenho/manual/FL1/NORM/W-FL1-NORM.jpg) | - |
| `R1-FL1-NORM` | 13/11/2026 11:34 | José Augusto | 1,00 | 1,85 | - | C | 13,2 | 39,4 | 261 | 3,32 | [har](evidencias/desempenho/manual/FL1/NORM/R1-FL1-NORM.har)/[jpg](evidencias/desempenho/manual/FL1/NORM/R1-FL1-NORM.jpg) | - |
| `R2-FL1-NORM` | 13/11/2026 11:37 | José Augusto | 0,96 | 1,92 | - | C | 14,5 | 42,0 | 265 | 3,39 | [har](evidencias/desempenho/manual/FL1/NORM/R2-FL1-NORM.har)/[jpg](evidencias/desempenho/manual/FL1/NORM/R2-FL1-NORM.jpg) | - |
| `R3-FL1-NORM` | 13/11/2026 11:39 | José Augusto | 1,10 | 1,88 | - | C | 12,8 | 36,5 | 269 | 3,39 | [har](evidencias/desempenho/manual/FL1/NORM/R3-FL1-NORM.har)/[jpg](evidencias/desempenho/manual/FL1/NORM/R3-FL1-NORM.jpg) | - |
| `R4-FL1-NORM` | 13/11/2026 11:49 | José Augusto | 2,10 | 2,05 | - | C | 13,0 | 38,0 | 218 | 3,39 | [har](evidencias/desempenho/manual/FL1/NORM/R4-FL1-NORM.har)/[jpg](evidencias/desempenho/manual/FL1/NORM/R4-FL1-NORM.jpg) | - |
| `R5-FL1-NORM` | 13/11/2026 11:54 | José Augusto | 0,98 | 1,84 | - | C | 12,5 | 37,0 | 210 | 3,39 | [har](evidencias/desempenho/manual/FL1/NORM/R5-FL1-NORM.har)/[jpg](evidencias/desempenho/manual/FL1/NORM/R5-FL1-NORM.jpg) | - |

*Tabela 5. Registro bruto de FL1 sob Rede Normal. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 4.2 Bateria FL1 sob Rede Limitada

A Tabela 6 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL1` em conexão limitada.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E1.1 (s) | Tempo E1.2 (s) | Tempo E1.3 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
| ------------ | ----------- | ---------------------- | :------------: | :------------: | :------------: | :----------: | :--------------: | :-------------: | :---------------: | :------------: | ---------------------------------- | :--------: |
| `W-FL1-LIM`  | 13/11/2026 12:20 | José Augusto | 5,80 | 5,20 | - | C | 15,8 | 46,0 | 211 | 3,39 | [har](evidencias/desempenho/manual/FL1/LIM/W-FL1-LIM.har)/[jpg](evidencias/desempenho/manual/FL1/LIM/W-FL1-LIM.jpg) | - |
| `R1-FL1-LIM` | 13/11/2026 12:24 | José Augusto | 5,69 | 4,85 | - | C | 15,4 | 45,2 | 230 | 3,39 | [har](evidencias/desempenho/manual/FL1/LIM/R1-FL1-LIM.har)/[jpg](evidencias/desempenho/manual/FL1/LIM/R1-FL1-LIM.jpg) | - |
| `R2-FL1-LIM` | 13/11/2026 12:25 | José Augusto | 5,74 | 4,90 | - | C | 16,1 | 48,0 | 236 | 3,39 | [har](evidencias/desempenho/manual/FL1/LIM/R2-FL1-LIM.har)/[jpg](evidencias/desempenho/manual/FL1/LIM/R2-FL1-LIM.jpg) | - |
| `R3-FL1-LIM` | 13/11/2026 12:27 | José Augusto | 5,63 | 4,75 | - | C | 14,8 | 42,6 | 227 | 3,39 | [har](evidencias/desempenho/manual/FL1/LIM/R3-FL1-LIM.har)/[jpg](evidencias/desempenho/manual/FL1/LIM/R3-FL1-LIM.jpg) | - |
| `R4-FL1-LIM` | 13/11/2026 12:28 | José Augusto | 5,65 | 4,80 | - | C | 15,5 | 46,1 | 236 | 3,39 | [har](evidencias/desempenho/manual/FL1/LIM/R4-FL1-LIM.har)/[jpg](evidencias/desempenho/manual/FL1/LIM/R4-FL1-LIM.jpg) | - |
| `R5-FL1-LIM` | 13/11/2026 12:30 | José Augusto | 5,63 | 4,72 | - | C | 15,0 | 44,5 | 268 | 3,39 | [har](evidencias/desempenho/manual/FL1/LIM/R5-FL1-LIM.har)/[jpg](evidencias/desempenho/manual/FL1/LIM/R5-FL1-LIM.jpg) | - |

*Tabela 6. Registro bruto de FL1 sob Rede Limitada. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-fl2"></a>

## 5. Registro de execuções de FL2 — Videoaulas

### 5.1 Bateria FL2 sob Rede Normal

A Tabela 7 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL2` em conexão normal.

| ID Repetição  | Data / Hora | Avaliador / Observador | Tempo E2.1 (s) | Tempo E2.2 (s) | Tempo E2.3 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
| ------------- | ----------- | ---------------------- | :------------: | :------------: | :------------: | :----------: | :--------------: | :-------------: | :---------------: | :------------: | ---------------------------------- | :--------: |
| `W-FL2-NORM`  | 13/11/2026 14:00 | José Augusto | 1,06 | 0,92 | 0,35 | C | 12,5 | 34,0 | 207 | 6,98 | [har](evidencias/desempenho/manual/FL2/NORM/W-FL2-NOR.har)/[jpg](evidencias/desempenho/manual/FL2/NORM/W-FL2-NORM.jpg) | - |
| `R1-FL2-NORM` | 13/11/2026 14:02 | José Augusto | 0,88 | 0,75 | 0,28 | C | 11,8 | 32,5 | 175 | 6,76 | [har](evidencias/desempenho/manual/FL2/NORM/R1-FL2-NOT.har)/[jpg](evidencias/desempenho/manual/FL2/NORM/R1-FL2-NORM.jpg) | - |
| `R2-FL2-NORM` | 13/11/2026 14:03 | José Augusto | 0,83 | 0,70 | 0,25 | C | 10,5 | 28,0 | 186 | 3,85 | [har](evidencias/desempenho/manual/FL2/NORM/R2-FL2-NOT.har)/[jpg](evidencias/desempenho/manual/FL2/NORM/R2-FL2-NORM.jpg) | - |
| `R3-FL2-NORM` | 13/11/2026 14:05 | José Augusto | 0,95 | 0,78 | 0,30 | C | 12,2 | 35,0 | 172 | 6,90 | [har](evidencias/desempenho/manual/FL2/NORM/R3-FL2-NOT.har)/[jpg](evidencias/desempenho/manual/FL2/NORM/R3-FL2-NORM.jpg) | - |
| `R4-FL2-NORM` | 13/11/2026 14:07 | José Augusto | 0,82 | 0,68 | 0,26 | C | 11,0 | 30,5 | 219 | 3,86 | [har](evidencias/desempenho/manual/FL2/NORM/R4-FL2-NOT.har)/[jpg](evidencias/desempenho/manual/FL2/NORM/R4-FL2-NORM.jpg) | - |
| `R5-FL2-NORM` | 13/11/2026 14:08 | José Augusto | 0,83 | 0,72 | 0,27 | C | 10,8 | 29,0 | 189 | 3,79 | [har](evidencias/desempenho/manual/FL2/NORM/R5-FL2-NOT.har)/[jpg](evidencias/desempenho/manual/FL2/NORM/R5-FL2-NORM.jpg) | - |

*Tabela 7. Registro bruto de FL2 sob Rede Normal. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 5.2 Bateria FL2 sob Rede Limitada

A Tabela 8 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL2` em conexão limitada.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E2.1 (s) | Tempo E2.2 (s) | Tempo E2.3 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
| ------------ | ----------- | ---------------------- | :------------: | :------------: | :------------: | :----------: | :--------------: | :-------------: | :---------------: | :------------: | ---------------------------------- | :--------: |
| `W-FL2-LIM`  | 13/11/2026 14:16 | José Augusto | 5,70 | 2,85 | 0,85 | C | 14,0 | 38,0 | 197 | 12,65 | [har](evidencias/desempenho/manual/FL2/LIM/W-FL2-LIM.har)/[jpg](evidencias/desempenho/manual/FL2/LIM/W-FL2-LIM.jpg) | - |
| `R1-FL2-LIM` | 13/11/2026 14:17 | José Augusto | 5,69 | 2,45 | 0,72 | C | 13,5 | 36,0 | 202 | 4,61 | [har](evidencias/desempenho/manual/FL2/LIM/R1-FL2-LIM.har)/[jpg](evidencias/desempenho/manual/FL2/LIM/R1-FL2-LIM.jpg) | - |
| `R2-FL2-LIM` | 13/11/2026 14:22 | José Augusto | 5,80 | 2,50 | 0,68 | C | 12,8 | 34,5 | 194 | 3,86 | [har](evidencias/desempenho/manual/FL2/LIM/R2-FL2-LIM.har)/[jpg](evidencias/desempenho/manual/FL2/LIM/R2-FL2-LIM.jpg) | - |
| `R3-FL2-LIM` | 13/11/2026 14:24 | José Augusto | 5,50 | 2,38 | 0,70 | C | 13,0 | 35,0 | 199 | 3,86 | [har](evidencias/desempenho/manual/FL2/LIM/R3-FL2-LIM.har)/[jpg](evidencias/desempenho/manual/FL2/LIM/R3-FL2-LIM.jpg) | - |
| `R4-FL2-LIM` | 13/11/2026 14:25 | José Augusto | 5,51 | 2,40 | 0,65 | C | 12,5 | 33,5 | 206 | 4,04 | [har](evidencias/desempenho/manual/FL2/LIM/R4-FL2-LIM.har)/[jpg](evidencias/desempenho/manual/FL2/LIM/R4-FL2-LIM.jpg) | - |
| `R5-FL2-LIM` | 13/11/2026 14:27 | José Augusto | 5,51 | 2,42 | 0,69 | C | 13,2 | 35,5 | 207 | 4,42 | [har](evidencias/desempenho/manual/FL2/LIM/R5-FL2-LIM.har)/[jpg](evidencias/desempenho/manual/FL2/LIM/R5-FL2-LIM.jpg) | - |

*Tabela 8. Registro bruto de FL2 sob Rede Limitada. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-fl3"></a>

## 6. Registro de execuções de FL3 — Exercícios

### 6.1 Bateria FL3 sob Rede Normal

A Tabela 9 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL3` em conexão normal.

| ID Repetição  | Data / Hora | Avaliador / Observador | Tempo E3.1 (s) | Tempo E3.2 (s) | Tempo E3.3 (s) | Tempo E3.4 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
| ------------- | ----------- | ---------------------- | :------------: | :------------: | :------------: | :------------: | :----------: | :--------------: | :-------------: | :---------------: | :------------: | ---------------------------------- | :--------: |
| `W-FL3-NORM`  | 13/11/2026 14:57 | José Augusto | 0,84 | 0,58 | 0,75 | 0,42 | C | 13,5 | 36,0 | 233 | 3,88 | [har](evidencias/desempenho/manual/FL3/NORM/W-FL3-NOR.har)/[jpg](evidencias/desempenho/manual/FL3/NORM/W-FL3-NORM.jpg) | - |
| `R1-FL3-NORM` | 13/11/2026 14:58 | José Augusto | 0,81 | 0,48 | 0,62 | 0,35 | C | 12,0 | 32,5 | 241 | 3,88 | [har](evidencias/desempenho/manual/FL3/NORM/R1-FL3-NOR.har)/[jpg](evidencias/desempenho/manual/FL3/NORM/R1-FL3-NORM.jpg) | - |
| `R2-FL3-NORM` | 13/11/2026 15:02 | José Augusto | 0,87 | 0,52 | 0,65 | 0,38 | C | 12,8 | 35,0 | 241 | 3,88 | [har](evidencias/desempenho/manual/FL3/NORM/R2-FL3-NOR.har)/[jpg](evidencias/desempenho/manual/FL3/NORM/R2-FL3-NORM.jpg) | - |
| `R3-FL3-NORM` | 13/11/2026 15:03 | José Augusto | 0,95 | 0,45 | 0,58 | 0,32 | C | 11,5 | 31,0 | 248 | 3,88 | [har](evidencias/desempenho/manual/FL3/NORM/R3-FL3-NOR.har)/[jpg](evidencias/desempenho/manual/FL3/NORM/R3-FL3-NORM.jpg) | - |
| `R4-FL3-NORM` | 13/11/2026 15:04 | José Augusto | 1,32 | 0,50 | 0,60 | 0,36 | C | 12,2 | 33,0 | 232 | 3,82 | [har](evidencias/desempenho/manual/FL3/NORM/R4-FL3-NOR.har)/[jpg](evidencias/desempenho/manual/FL3/NORM/R4-FL3-NORM.jpg) | - |
| `R5-FL3-NORM` | 13/11/2026 15:05 | José Augusto | 1,01 | 0,47 | 0,63 | 0,34 | C | 11,8 | 31,5 | 181 | 3,88 | [har](evidencias/desempenho/manual/FL3/NORM/R5-FL3-NOR.har)/[jpg](evidencias/desempenho/manual/FL3/NORM/R5-FL3-NORM.jpg) | - |

*Tabela 9. Registro bruto de FL3 sob Rede Normal. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 6.2 Bateria FL3 sob Rede Limitada

A Tabela 10 registra o aquecimento (`W`) e as 5 repetições válidas (`R1` a `R5`) de `FL3` em conexão limitada.

| ID Repetição | Data / Hora | Avaliador / Observador | Tempo E3.1 (s) | Tempo E3.2 (s) | Tempo E3.3 (s) | Tempo E3.4 (s) | Resultado M2 | CPU média M3 (%) | CPU pico M3 (%) | RAM pico M4 (MiB) | Dados M5 (MiB) | Arquivo de evidência (.har / .png) | Ocorrência |
| ------------ | ----------- | ---------------------- | :------------: | :------------: | :------------: | :------------: | :----------: | :--------------: | :-------------: | :---------------: | :------------: | ---------------------------------- | :--------: |
| `W-FL3-LIM`  | 13/11/2026 15:10 | José Augusto | 5,80 | 1,45 | 1,60 | 0,95 | C | 14,8 | 40,0 | 189 | 4,45 | [har](evidencias/desempenho/manual/FL3/LIM/W-FL3-LIM.har)/[jpg](evidencias/desempenho/manual/FL3/LIM/W-FL3-LIM.jpg) | - |
| `R1-FL3-LIM` | 13/11/2026 15:21 | José Augusto | 5,75 | 1,25 | 1,35 | 0,82 | C | 14,0 | 38,5 | 176 | 5,01 | [har](evidencias/desempenho/manual/FL3/LIM/R1-FL3-LIM.har)/[jpg](evidencias/desempenho/manual/FL3/LIM/R1-FL3-LIM.jpg) | - |
| `R2-FL3-LIM` | 13/11/2026 15:23 | José Augusto | 5,67 | 1,30 | 1,40 | 0,85 | C | 14,5 | 39,0 | 184 | 4,63 | [har](evidencias/desempenho/manual/FL3/LIM/R2-FL3-LIM.har)/[jpg](evidencias/desempenho/manual/FL3/LIM/R2-FL3-LIM.jpg) | - |
| `R3-FL3-LIM` | 13/11/2026 15:24 | José Augusto | 5,81 | 1,22 | 1,32 | 0,78 | C | 13,8 | 37,0 | 188 | 4,82 | [har](evidencias/desempenho/manual/FL3/LIM/R3-FL3-LIM.har)/[jpg](evidencias/desempenho/manual/FL3/LIM/R3-FL3-LIM.jpg) | - |
| `R4-FL3-LIM` | 13/11/2026 15:26 | José Augusto | 5,59 | 1,28 | 1,38 | 0,80 | C | 14,2 | 38,0 | 194 | 4,82 | [har](evidencias/desempenho/manual/FL3/LIM/R4-FL3-LIM.har)/[jpg](evidencias/desempenho/manual/FL3/LIM/R4-FL3-LIM.jpg) | - |
| `R5-FL3-LIM` | 13/11/2026 15:28 | José Augusto | 5,76 | 1,20 | 1,30 | 0,79 | C | 13,5 | 36,5 | 185 | 4,82 | [har](evidencias/desempenho/manual/FL3/LIM/R5-FL3-LIM.har)/[jpg](evidencias/desempenho/manual/FL3/LIM/R5-FL3-LIM.jpg) | - |

*Tabela 10. Registro bruto de FL3 sob Rede Limitada. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-lighthouse"></a>

## 7. Registro de auditoria complementar com Lighthouse

A Tabela 11 documenta os indicadores de laboratório gerados pela auditoria do Lighthouse nas páginas de entrada dos fluxos sob condições de rede normal e limitada.

| Página avaliada | Condição de rede | Performance Score (0–100) | First Contentful Paint - FCP (s) | Largest Contentful Paint - LCP (s) | Total Blocking Time - TBT (ms) | Speed Index (s) | Arquivo de relatório (.json / .html) |
| ---- | ---- | :--: | :--: | :--: | :--: | :--: | ---- |
| Curso `D2` (FL1) | Rede Normal | 57 | 1,7 | 2,3 | 0 | 1,9 | [json](evidencias/desempenho/lighthouse/FL1/LH_FL1_NOR_20261111.json)/[html](evidencias/desempenho/lighthouse/FL1/LH_FL1_NOR_20261111.html) |
| Curso `D2` (FL1) | Rede Limitada | 69 | 1,9 | 2,6 | 0 | 7,0 | [json](evidencias/desempenho/lighthouse/FL1/LH_FL1_LIM_20261111.json)/[html](evidencias/desempenho/lighthouse/FL1/LH_FL1_LIM_20261111.html) |
| Videoaula `D4` (FL2) | Rede Normal | 67 | 1,7 | 3,7 | 20 | 3,1 | [json](evidencias/desempenho/lighthouse/FL2/LH_FL2_NOR_20261111.json)/[html](evidencias/desempenho/lighthouse/FL2/LH_FL2_NOR_20261111.html) |
| Videoaula `D4` (FL2) | Rede Limitada | 62 | 2,0 | 4,0 | 20 | 11,4 | [json](evidencias/desempenho/lighthouse/FL2/LH_FL2_LIM_20261111.json)/[html](evidencias/desempenho/lighthouse/FL2/LH_FL2_LIM_20261111.html) |
| Exercício `D5` (FL3) | Rede Normal | 64 | 2,0 | 4,4 | 40 | 2,7 | [json](evidencias/desempenho/lighthouse/FL3/LH_FL3_NOR_20261111.json)/[html](evidencias/desempenho/lighthouse/FL3/LH_FL3_NOR_20261111.html) |
| Exercício `D5` (FL3) | Rede Limitada | 61 | 2,0 | 4,4 | 50 | 9,5 | [json](evidencias/desempenho/lighthouse/FL3/LH_FL3_LIM_20261111.json)/[html](evidencias/desempenho/lighthouse/FL3/LH_FL3_LIM_20261111.html) |

*Tabela 11. Resultados da auditoria complementar Lighthouse. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-ocorrencias"></a>

## 8. Tabela de ocorrências de desempenho

A Tabela 12 reúne todas as falhas, anomalias, picos anormais de carga ou ocorrências impeditivas identificadas durante os ensaios de desempenho.

| ID Ocorrência | Bateria / Repetição | Etapa | Descrição detalhada do comportamento | Gravidade | Atribuição da causa | Impacto na repetição | Evidência (.png / .log) |
| ------------- | ------------------- | ----- | ------------------------------------ | :-------: | ------------------- | -------------------- | ----------------------- |
| `OC-DES-001`  | Auditoria Complementar (FL1) | Entrada `D2` | Deslocamento cumulativo de layout severo (*CLS = 0,531*) sob Rede Normal decorrente da injeção assíncrona do bloco de grade curricular sem reserva prévia de espaço visual, penalizando o score sintético. | Baixa | Plataforma Khan Academy | Sem bloqueio operacional; instabilidade visual momentânea na conexão rápida | [json](evidencias/desempenho/lighthouse/FL1/LH_FL1_NOR_20261111.json) |
| `OC-DES-002`  | Baterias FL2 (Normal e Limitada) | E2.3 original | Inexistência de faixa de legendas sobrepostas (*CC*) no reprodutor da videoaula de computação `D4`, disponibilizando apenas o painel de transcrição textual sincronizada. | Baixa | Plataforma Khan Academy | Adequação do roteiro: etapa de legendas suprimida e transcrição mantida como E2.3 | [jpg](evidencias/desempenho/manual/FL2/NORM/W-FL2-NORM.jpg) |
| `OC-DES-003`  | Baterias FL3 (Normal e Limitada) | E3.2 | No editor interativo de código (*live editor* do desafio `D5`), o auxílio pedagógico (dica) não requer acionamento de botão, sendo disparado automaticamente após a digitação inicial de caracteres. | Baixa | Plataforma Khan Academy | Adequação do marco inicial de temporização de E3.2 para a entrada de texto | [jpg](evidencias/desempenho/manual/FL3/NORM/W-FL3-NORM.jpg) |

*Tabela 12. Ocorrências registradas na avaliação de desempenho. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="registro-resumo"></a>

## 9. Resumo estatístico, julgamento e decisões

Esta seção consolida os indicadores derivados das cinco repetições válidas de cada fluxo e condição de rede, confrontando-os com as faixas de pontuação e critérios de julgamento estabelecidos.

### 9.1 Consolidação de M1 — Tempo observável por etapa

A Tabela 13 consolida a mediana e o P90 de cada etapa avaliada, convertendo o resultado na nota correspondente (0 a 3).

| Fluxo | Etapa do roteiro | Condição de rede | Mediana observada (s) | P90 observado (s) | Faixa de julgamento atingida | Nota M1 (0–3) |
| :---: | ---------------- | ---------------- | :-------------------: | :---------------: | ---------------------------- | :-----------: |
| `FL1` | E1.1 (Catálogo inicial) | Rede Normal | 1,00 | 1,70 | Excelente (≤ 1 s) | 3 |
| `FL1` | E1.1 (Catálogo inicial) | Rede Limitada | 5,65 | 5,72 | Mínimo aceitável (> 3 a 10 s) | 1 |
| `FL1` | E1.2 (Grade do curso) | Rede Normal | 1,88 | 2,00 | Alvo (> 1 a 3 s) | 2 |
| `FL1` | E1.2 (Grade do curso) | Rede Limitada | 4,80 | 4,88 | Mínimo aceitável (> 3 a 10 s) | 1 |
| `FL1` | E1.3 (Ambiente da aula) | Rede Normal | - | - | Delimitado na grade D2 | - |
| `FL1` | E1.3 (Ambiente da aula) | Rede Limitada | - | - | Delimitado na grade D2 | - |
| `FL2` | E2.1 (Interface do player) | Rede Normal | 0,83 | 0,92 | Excelente (≤ 1 s) | 3 |
| `FL2` | E2.1 (Interface do player) | Rede Limitada | 5,51 | 5,76 | Mínimo aceitável (> 3 a 10 s) | 1 |
| `FL2` | E2.2 (Disparo do vídeo) | Rede Normal | 0,72 | 0,77 | Excelente (≤ 1 s) | 3 |
| `FL2` | E2.2 (Disparo do vídeo) | Rede Limitada | 2,42 | 2,48 | Alvo (> 1 a 3 s) | 2 |
| `FL2` | E2.3 (Abertura da transcrição) | Rede Normal | 0,27 | 0,29 | Excelente (≤ 1 s) | 3 |
| `FL2` | E2.3 (Abertura da transcrição) | Rede Limitada | 0,69 | 0,71 | Excelente (≤ 1 s) | 3 |
| `FL3` | E3.1 (Abertura do exercício) | Rede Normal | 0,95 | 1,20 | Excelente (≤ 1 s) | 3 |
| `FL3` | E3.1 (Abertura do exercício) | Rede Limitada | 5,75 | 5,79 | Mínimo aceitável (> 3 a 10 s) | 1 |
| `FL3` | E3.2 (Exibição da dica) | Rede Normal | 0,48 | 0,51 | Excelente (≤ 1 s) | 3 |
| `FL3` | E3.2 (Exibição da dica) | Rede Limitada | 1,25 | 1,29 | Alvo (> 1 a 3 s) | 2 |
| `FL3` | E3.3 (Envio e feedback) | Rede Normal | 0,62 | 0,64 | Excelente (≤ 1 s) | 3 |
| `FL3` | E3.3 (Envio e feedback) | Rede Limitada | 1,35 | 1,39 | Alvo (> 1 a 3 s) | 2 |
| `FL3` | E3.4 (Próxima atividade) | Rede Normal | 0,35 | 0,37 | Excelente (≤ 1 s) | 3 |
| `FL3` | E3.4 (Próxima atividade) | Rede Limitada | 0,80 | 0,84 | Excelente (≤ 1 s) | 3 |

*Tabela 13. Consolidação estatística e notas de M1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.2 Consolidação de M2 — Taxa de conclusão das tentativas

A Tabela 14 resume o índice de sucesso operacional obtido para cada fluxo e condição de rede.

| Fluxo | Condição de rede | Tentativas elegíveis ($N$) | Tentativas concluídas ($C$) | Taxa $M2 = 100 \times C/N$ (%) | Ocorrência de bloqueio essencial? | Nota M2 (0–3) |
| :--: | ---- | :--: | :---: | :--: | :--: | :--: |
| `FL1` | Rede Normal | 5 | 5 | 100% | Não | 3 |
| `FL1` | Rede Limitada | 5 | 5 | 100% | Não | 3 |
| `FL2` | Rede Normal | 5 | 5 | 100% | Não | 3 |
| `FL2` | Rede Limitada | 5 | 5 | 100% | Não | 3 |
| `FL3` | Rede Normal | 5 | 5 | 100% | Não | 3 |
| `FL3` | Rede Limitada | 5 | 5 | 100% | Não | 3 |
| **Total** | **Geral consolidado** | **30** | **30** | **100%** | **Não** | **3** |

*Tabela 14. Consolidação da taxa de conclusão M2. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.3 Consolidação de M3 — Utilização de CPU

A Tabela 15 consolida a demanda média e os picos de processamento registrados.

| Fluxo | Condição de rede | Média de CPU apurada (%) | Maior pico instantâneo (%) | Houve sobrecarga > 75%? | Nota M3 (0–3) |
| :---: | ---------------- | :----------------------: | :------------------------: | :---------------------: | :-----------: |
| `FL1` | Rede Normal | 13,2% | 42,0% | Não | 3 |
| `FL1` | Rede Limitada | 15,4% | 48,0% | Não | 3 |
| `FL2` | Rede Normal | 11,3% | 35,0% | Não | 3 |
| `FL2` | Rede Limitada | 13,0% | 36,0% | Não | 3 |
| `FL3` | Rede Normal | 12,1% | 35,0% | Não | 3 |
| `FL3` | Rede Limitada | 14,0% | 39,0% | Não | 3 |

*Tabela 15. Consolidação da utilização de CPU M3. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.4 Consolidação de M4 — Pico de memória

A Tabela 16 consolida o maior pico individual de memória privada alocada nos processos da aba.

| Fluxo | Condição de rede | Maior pico de memória $\max(\text{RAM}(t))$ (MiB) | Média dos picos (MiB) | Risco de esgotamento observado? | Nota M4 (0–3) |
| :---: | ---------------- | :-----------------------------------------------: | :-------------------: | :-----------------------------: | :-----------: |
| `FL1` | Rede Normal | 269 MiB | 244,6 MiB | Não | 3 |
| `FL1` | Rede Limitada | 268 MiB | 239,4 MiB | Não | 3 |
| `FL2` | Rede Normal | 219 MiB | 188,2 MiB | Não | 3 |
| `FL2` | Rede Limitada | 207 MiB | 201,6 MiB | Não | 3 |
| `FL3` | Rede Normal | 248 MiB | 228,6 MiB | Não | 3 |
| `FL3` | Rede Limitada | 194 MiB | 185,4 MiB | Não | 3 |

*Tabela 16. Consolidação do consumo de memória M4. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.5 Consolidação de M5 — Dados transferidos

A Tabela 17 consolida o tráfego médio e mediano de rede transmitido para a conclusão de cada fluxo padronizado.

| Fluxo | Condição de rede | Volume mediano transferido (MiB) | Maior volume observado (MiB) | Orçamento ≤ 10 MiB respeitado? | Nota M5 (0–3) |
| :---: | ---------------- | :------------------------------: | :--------------------------: | :----------------------------: | :-----------: |
| `FL1` | Rede Normal | 3,39 MiB | 3,39 MiB | Sim | 3 |
| `FL1` | Rede Limitada | 3,39 MiB | 3,39 MiB | Sim | 3 |
| `FL2` | Rede Normal | 3,86 MiB | 6,90 MiB | Sim | 3 |
| `FL2` | Rede Limitada | 4,04 MiB | 4,61 MiB | Sim | 3 |
| `FL3` | Rede Normal | 3,88 MiB | 3,88 MiB | Sim | 3 |
| `FL3` | Rede Limitada | 4,82 MiB | 5,01 MiB | Sim | 3 |

*Tabela 17. Consolidação de dados transferidos M5. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.6 Julgamento das questões Q1 a Q4, hipóteses H1 a H4 e objetivo G1

A Tabela 18 registra a classificação final de cada questão, hipótese e o atendimento global do objetivo `G1`.

| Questão / Hipótese | Métricas de suporte | Estado formal | Justificativa com base nos dados consolidados |
| ------------------ | ------------------- | ------------- | --------------------------------------------- |
| **Questão Q1** (Espera nas etapas) | M1, M2 | Atendida | Todas as etapas alcançaram nota 2 ou 3 em Rede Normal e notas 1 a 3 em Rede Limitada, com taxa de conclusão de 100% e ausência de bloqueios operacionais ou timeouts. |
| **Hipótese H1** (Mediana ≤ 3 s e Conclusão ≥ 90%) | M1, M2 | Sustentada em Rede Normal / Não sustentada na totalidade em Rede Limitada | Em Rede Normal todas as etapas obtiveram mediana ≤ 1,88 s (Nota 2 e 3) e M2 = 100%. Em Rede Limitada, os carregamentos de página inicial (E1.1, E2.1 e E3.1) e abertura de curso (E1.2) situaram-se entre 4,80 s e 5,75 s (Nota 1), embora as interações em SPA tenham permanecido ≤ 2,42 s. |
| **Questão Q2** (Processamento disponível) | M3 | Atendida | Nota 3 (Excelente) obtida em todos os fluxos e condições, sem registros de sobrecarga contínua de CPU acima de 75%. |
| **Hipótese H2** (CPU média ≤ 50%) | M3 | Sustentada | A média de utilização de CPU oscilou entre 11,3% e 15,4% e os picos máximos pontuais não excederam 48,0%, cumprindo com folga a meta de H2. |
| **Questão Q3** (Memória disponível) | M4 | Atendida | Nota 3 (Excelente) atingida em todas as baterias, com consumo privado de memória muito abaixo do teto de segurança. |
| **Hipótese H3** (Pico de RAM ≤ 1024 MiB) | M4 | Sustentada | O maior pico instantâneo observado em toda a avaliação foi de 269 MiB (no fluxo FL1), quatro vezes inferior ao limite de 1.024 MiB de H3. |
| **Questão Q4** (Orçamento de acesso) | M5 | Atendida | Nota 3 (Excelente) alcançada em todos os fluxos sob ambas as condições de conectividade. |
| **Hipótese H4** (Volume transferido ≤ 10 MiB) | M5 | Sustentada | O volume mediano de dados transmitido variou entre 3,39 MiB e 4,82 MiB, respeitando com ampla margem o orçamento máximo de 10 MiB por fluxo. |
| **Objetivo G1** (Eficiência de desempenho) | M1 a M5 | Atendido | Todas as questões de pesquisa (Q1 a Q4) foram atendidas, com notas máximas em M2, M3, M4 e M5, comprovando a eficiência operacional da plataforma no ambiente A1. |

*Tabela 18. Julgamento formal de Q1–Q4, H1–H4 e objetivo G1. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

### 9.7 Desfecho para a Decisão D1 e recomendações práticas

A Tabela 19 documenta a conversão dos achados no desfecho da decisão `D1` e orientações concretas para a coordenação da escola pública.

| Desfecho para a Decisão `D1` | Recomendações e orientações práticas para a coordenação escolar |
| ---------------------------- | --------------------------------------------------------------- |
| **Recomendar com ressalvas de conectividade de rede** | 1. **Viabilidade de hardware confirmada:** A plataforma demonstrou excelente eficiência no uso de recursos computacionais, demandando menos de 270 MiB de memória RAM e média de CPU inferior a 16%, mostrando-se perfeitamente adequada para computadores com 4 GB de RAM e 4 vCPUs típicos de escolas públicas.<br>2. **Desempenho interativo ágil:** Uma vez carregadas as interfaces, as ações pedagógicas (obtenção de dicas, validação de respostas, transição entre questões e execução de vídeo) respondem rapidamente (< 2,5 s), mesmo em conexões modestas de 1,5 Mbps.<br>3. **Ressalva de carregamento inicial em rede compartilhada:** O carregamento completo de páginas novas sob limitação de banda consome entre 4,8 s e 5,8 s. Recomenda-se aos docentes orientar os alunos a abrir as lições com antecedência no início da aula, escalonar o acesso a videoaulas pesadas e priorizar o uso de atividades interativas e exercícios (`FL3`), que apresentam baixo consumo de dados e alta responsividade. |

*Tabela 19. Desfecho da decisão D1 e ações para o requisitante escolar. Fonte: Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## Referências

<a id="s1"></a>

> [S1] Procedimentos de avaliação de eficiência de desempenho (M1 a M5) — Fase 3. Disponível em: [Procedimentos de desempenho](../fase-3/procedimentos-desempenho.md).

<a id="s2"></a>

> [S2] Ambiente de testes e ferramentas de avaliação — Fase 3. Disponível em: [Ambiente de testes](../fase-3/ambiente-de-testes.md).

<a id="s3"></a>

> [S3] Critérios de julgamento — Fase 2. Disponível em: [Critérios de julgamento](../fase-2/criterios-julgamento.md).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :----: | :--: | --------- | ----------- | ------- |
| 1.0 | 08/11/2026 | Estruturação inicial das planilhas e formulários de registro para eficiência de desempenho (M1 a M5), sem resultados coletados. | [José Augusto](https://github.com/JAugustoM) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 11/11/2026 | Congelamento do ambiente de testes e realização dos testes sintéticos com Lighthouse | [José Augusto](https://github.com/JAugustoM) | |
| 1.2 | 13/11/2026 | Preenchimento dos dados brutos das baterias manuais (Tabelas 5 a 10), registro de ocorrências (Tabela 12) e consolidação estatística com julgamento de hipóteses e decisão D1 (Capítulo 9). | [José Augusto](https://github.com/JAugustoM) | |
| 1.3 | 13/11/2026 | Migração do documento para a Fase 4 (`docs/fase-4/`) com atualização integral dos links relativos e vínculos de evidências. | [José Augusto](https://github.com/JAugustoM) | |
