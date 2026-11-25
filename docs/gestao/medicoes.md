# Procedimento de medições

Este artefato descreve como a medição é executada: quais dados entram, o passo a passo de cada rodada, em que datas ela ocorre e histórico de medições.
 
<a id="responsavel"></a>

**Responsável pela execução:** Antes de cada ponto de medição, a equipe designa o integrante responsável pela coleta, validação e consolidação dos dados. Todos os integrantes devem registrar suas horas até as 12h do dia da medição. O responsável verifica as pendências, executa o script, registra os resultados e documenta as decisões decorrentes.

## 1. Dados de entrada

A Tabela 1 lista os dados necessários, onde ficam, quem os alimenta e quais medidas dependem deles.
 
| Dado | Fonte | Quem alimenta | Quando | Medidas que usam |
|---|---|---|---|---|
| ID, Janela, Estimativa, estado, datas de fechamento e reabertura, labels | Issues e pull requests do GitHub | Responsável pela issue | Ao criar, fechar ou reabrir a issue | `CP1`, `CP2`, `DP1`, `RC2` |
| Horas por integrante e por issue | Tabela de Contribuição no corpo da issue, ver [Registro de Horas](#2-registro-manual-das-horas-trabalhadas) | Cada integrante | Sempre que realizar alguma alteração | `RC1`, `RC2` |
| Nível por critério da rubrica | `assets/dados/gestao/autoavaliacao.csv` (colunas `data,fase,criterio,nivel,evidencia`) | Revisor | Em [Mg-3](#pontos) | `DP2` |
| Uso de IA | [Uso de IA](uso_de_ia.md) | Quem usou a ferramenta | No momento do uso | Evidência para os critérios de uso de IA na autoavaliação (`DP2`) |
 
*Tabela 1. Dados de entrada das medições. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*
 
No `autoavaliacao.csv`, `criterio` é o código da rubrica (por exemplo, `F1-C6`) e `nivel` é um de Insuficiente, Regular, Satisfatório ou Excelente (ou Crítico, Insuficiente, Bom, Adequado), que correspondem, nesta ordem, às quatro opções da rubrica da professora, da primeira à última.
 
## 2. Registro Manual das Horas trabalhadas

1. Abra a issue em que trabalhou. Ela deve ter sido criada com o [template de atividade planejada](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/blob/main/.github/ISSUE_TEMPLATE/atividade_planejada.md), que contém a seção **Tabela de Contribuição**.
2. Acrescente **uma linha por dia** em que trabalhou na issue:
   - `Usuário`: seu usuário do GitHub (por exemplo, `@usuario`).
   - `Data`: no formato `DD/MM/AAAA`.
   - `Horas Trabalhadas`: número decimal, em múltiplos de 0,25 (por exemplo, `1.5`, `0.75`).
3. Lance as horas **até as 12h do dia de cada ponto de medição** (Mg-1 a Mg-3; datas no plano).
4. O script de consolidação lê as tabelas das issues pela API do GitHub a cada build da página. Não há arquivo a versionar.

### Regras

- Conte tudo o que é trabalho do projeto: escrita, pesquisa, revisão do trabalho de outro membro, reuniões, preparação de slides e a conferência de textos gerados por IA.
- Em trabalho de dupla, cada integrante lança as **suas** horas, em linhas próprias. Não divida nem some as da dupla.
- Não registre horas estimadas aqui. A estimativa fica no campo **Estimativa** da issue.
- Se a atividade ainda não tem issue, crie a issue primeiro. Reuniões e tarefas de gestão também precisam de uma issue de apoio com Estimativa.
- Horas lançadas fora de uma issue não são contabilizadas e diminuem o `RC3`.
- Para corrigir um lançamento, edite a linha da tabela na issue. O histórico de edições fica registrado pelo GitHub.

### Exemplo de preenchimento

Valores fictícios, apenas para mostrar o formato. Não copiar para a sua issue.

```markdown
### Tabela de Contribuição

| Usuário  | Data       | Horas Trabalhadas |
| :------- | :--------: | :---------------: |
| @usuario | 01/01/2026 | 1.5               |
| @usuario | 02/01/2026 | 0.75              |
```

<a id="pontos"></a>

## 3. Pontos de medição previstos

A Tabela 2 apresenta as datas das medições, sua finalidade e as medidas calculadas em cada uma.
 
| Id da Medição | Data | Finalidade | Medidas |
|---|---|---|---|
| Mg-1 | 26/10/2026 (seg) | Medição da Entrega 1 (Fases 1 e 2) | `CP1`, `CP2`, `DP1`, `DP2`, `RC1`, `RC2`, `Pa` |
| Mg-2 | 16/11/2026 (seg) | Medição do Ponto de Controle 2 (PC2) | `CP1`, `CP2`, `DP1`, `RC1`, `RC2`, `Pa`; `DP2` não aferido |
| Mg-3 | 24/11/2026 (ter) | Medição da Entrega 2 Final | `CP1`, `CP2`, `DP1`, `DP2`, `RC1`, `RC2`, `Pa` |

*Tabela 2. Pontos de medição previstos. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

<a id="historico"></a>

## 4. Registro de medições realizadas

### Ponto Mg-1: Entrega 1 (26/10/2026)

Executado em 26/10/2026 sobre as issues e commits das Fases 1 e 2.

| Medida | Medida Base / Valores Brutos | Medida Derivada | Valor | Nível | Cor | Interpretação Técnica e Decisão |
|---|---|---|:---:|:---:|:---:|---|
| **CP1** Progresso | $Ac = 13$, $Ap = 13$ | $Ppp = (13 \div 13) \times 100$ | **100%** | Adequado | Verde | 100% das 13 atividades previstas para a Entrega 1 foram concluídas no escopo das Fases 1 e 2. |
| **CP2** Prazo | $Acp = 6$, $Ac = 13$ | $Pacp = (6 \div 13) \times 100$ | **46,2%** | Crítico | Vermelho | As primeiras issues (#1 a #7) sofreram replanejamento e fecharam após a data da janela original, concentrando a entrega no PC1. Ações: na Fase 3, fixar janelas mais realistas e registrar formalmente no corpo de novas issues. |
| **DP1** Retrabalho | $Ir = 0$, $Ic = 0$, $If = 13$ | $Pri = (0 \div 13) \times 100$ | **0,0%** | Adequado | Verde | Nenhuma issue com retrabalho formal registrado na Entrega 1. Adotar padronização de issue templates para a Fase 3 para manter o rastreamento rigoroso. |
| **DP2** Efetividade | $Ca = 23$, $Cb = 0$, $Ci = 0$, $Cc = 0$, $Ct = 23$ | $Qcic = 0$ <br> $PCa = 100\%$ | **Qcic: 0** <br> **PCa: 100%** | Adequado | Verde | Todos os critérios das Fases 1 e 2 avaliados como Adequados com base na rubrica docente e nos artefatos entregues. |
| **RC1** Esforço | $\sum Hr = 32,00\text{ h}$, $n = 6$ | $Hm = 32,00 \div 6$ | **32,00 h** (média 5,33 h/membro) | Informativo | Sem cor | Volume compatível com a carga prevista para a Entrega 1; esforço distribuído entre todos os integrantes. |
| **RC2** Variação | $Ee = 20,00\text{ h}$, $Er = 20,00\text{ h}$ | $Ve = (0 \div 20) \times 100$ | **0,0%** | Adequado | Verde | Estimativas em issues fechadas com estimativa explícita bateram rigorosamente com os lançamentos. |
| **Pa** Cobertura | $Ar = 11$, $Ac = 13$ | $Pa = (11 \div 13) \times 100$ | **84,6%** | Insuficiente | Amarelo | Duas issues concluídas sem apontamento na Tabela de Contribuição. Decisão: completar os lançamentos retroativos dos membros pendentes. |

### Ponto Mg-2: Ponto de Controle 2 (16/11/2026)

Executado em 16/11/2026 sobre as issues e commits das Fases 3 e 4(parcial) com alterações graduais ao longo do executado.

| Medida | Medida Base / Valores Brutos | Medida Derivada | Valor | Nível | Cor | Interpretação Técnica e Decisão |
|---|---|---|:---:|:---:|:---:|---|
| **CP1** Progresso | $Ac = 17$, $Ap = 17$ | $Ppp = (17 \div 17) \times 100$ | **100%** | Adequado | Verde | 100% das 17 atividades previstas para o ponto de controle 2 fase 3 e pouco da fase 4 |
| **CP2** Prazo | $Acp = 16$, $Ac = 17$ | $Pacp = (16 \div 17) \times 100$ | **94,1%** | Adequado | Verde | 94,1% das 17 atividades previstas para o ponto de controle 2 fase 3 e pouco da fase 4 |
| **DP1** Retrabalho | $Ir = 0$, $Ic = 0$, $If = 13$ | $Pri = (0 \div 13) \times 100$ | **0,0%** | Adequado | Verde | Com os valores registrados, nenhuma issue apresenta retrabalho formal; o total de issues fechadas ainda precisa ser conferido. |
| **DP2** Efetividade | Não aferido | Não calculada | Não aferido | Sem classificação | Sem cor | Aferição adiada para Mg-3; os dados de Mg-1 não representam esta rodada. |
| **RC1** Esforço | $\sum Hr = 82,80\text{ h}$, $n = 6$ | $Hm = 82,80 \div 6$ | **82,80 h** (média 13,80 h/membro) | Informativo | Sem cor | Total registrado a conferir com os lançamentos individuais, pois não é múltiplo de 0,25 h como exige o procedimento. |
| **RC2** Variação | $Ee = 56,00\text{ h}$, $Er = 67,00\text{ h}$ | $Ve = (11 \div 56) \times 100$ | **19,6%** | Bom | Verde | O esforço realizado superou a estimativa em 11 h; o desvio de 19,6% está na faixa Bom de `RC2`. |
| **Pa** Cobertura | $Ar = 17$, $Ac = 17$ | $Pa = (17 \div 17) \times 100$ | **100%** | Adequado | Verde | Todas as issues tiveram horas registradas |

**Pendência de validação da Mg-2:** conferir o conjunto de issues usado em `DP1` (`If = 13`, enquanto `CP1` registra `Ac = 17`) e a soma das horas de `RC1` contra as tabelas de contribuição. Os valores brutos foram mantidos até essa conferência.

<a id="padroes-issues"></a>

## 5. Padrão de texto para issues (Determinação de DP1 e Critérios)

Para assegurar a confiabilidade da medição automatizada pelo script `consolida_horas.py`, todas as issues devem conter blocos padronizados de metadados:

### Padrão 1: Nova Atividade Planejada (Alimenta CP1, CP2, RC2 e Critérios)
Adicionar no corpo da issue ao criá-la:
```markdown
## Metadados de Medição (PSM/CID)
- **Janela Prevista:** DD/MM/AAAA
- **Estimativa:** X.XX h
- **Critérios Relacionados:** [Ex: F3-C1, F3-C2]
- **Classificação:** Nova Atividade Planejada
```

### Padrão 2: Correção / Retrabalho (Alimenta DP1 e DP2)
Ao reabrir uma issue ou criar uma nova issue para sanar não conformidades identificadas por pares, autoavaliação ou apontamento docente:
- Aplicar a label **`correcao`** no GitHub;
- Incluir no corpo da issue o seguinte bloco de rastreabilidade:
```markdown
## Metadados de Medição (PSM/CID - DP1)
- **Janela Prevista:** DD/MM/AAAA
- **Estimativa:** X.XX h
- **Critérios Relacionados:** [Ex: F1-C3, F2-C5]
- **Classificação:** Correção / Retrabalho (DP1)
- **Retrabalho (DP1):** Sim
- **Issue de Origem:** #XX
- **Causa Raiz do Retrabalho:** [Descrever o motivo: apontamento em revisão por pares, critério Insuficiente na autoavaliação, etc.]
```

Templates pré-configurados estão disponíveis em `.github/ISSUE_TEMPLATE/` para facilitar a criação direta com esses campos.
