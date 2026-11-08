# Procedimento de medição

Este artefato descreve como a medição é executada: quais dados entram, o passo a passo de cada rodada e em que datas ela ocorre.
 
<a id="responsavel"></a>

**Responsável pela execução:** Antes de cada ponto de medição, a equipe designa o integrante responsável pela coleta, validação e consolidação dos dados. Todos os integrantes devem registrar suas horas até as 12h do dia da medição. O responsável verifica as pendências, executa o script, registra os resultados e documenta as decisões decorrentes.

## 1. Dados de entrada

A Tabela 1 lista os dados necessários, onde ficam, quem os alimenta e quais medidas dependem deles.
 
| Dado | Fonte | Quem alimenta | Quando | Medidas que usam |
|---|---|---|---|---|
| ID, Janela, Estimativa, estado, datas de fechamento e reabertura, labels | Issues e pull requests do GitHub | Responsável pela issue | Ao criar, fechar ou reabrir a issue | `CP1`, `CP2`, `DP1`, `RC2` |
| Horas por integrante e por issue | Tabela de Contribuição no corpo da issue (colunas `Usuário`, `Data`, `Horas Trabalhadas`; ver [Registro de Horas](horas.md)) | Cada integrante | Até 12h do dia da medição | `RC1`, `RC2` |
| Nível por critério da rubrica | `assets/dados/gestao/autoavaliacao.csv` (colunas `data,fase,criterio,nivel,evidencia`) | Revisor | Em [Mg-3](#pontos) | `DP2` |
| Uso de IA | [Uso de IA](uso_de_ia.md) | Quem usou a ferramenta | No momento do uso | Evidência para os critérios de uso de IA na autoavaliação (`DP2`) |
 
*Tabela 1. Dados de entrada das medições. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*
 
No `autoavaliacao.csv`, `criterio` é o código da rubrica (por exemplo, `F1-C6`) e `nivel` é um de Insuficiente, Regular, Satisfatório ou Excelente (ou Crítico, Insuficiente, Bom, Adequado), que correspondem, nesta ordem, às quatro opções da rubrica da professora, da primeira à última.
 
## 2. Passos operacionais

Os passos abaixo são seguidos a cada ponto de medição:
 
1. Até as 12h do dia da medição, cada membro lança suas horas na Tabela de Contribuição das issues em que trabalhou.
2. O [Responsável](#responsavel) confere as pré-condições: issues fechadas com Janela, Estimativa e revisão registrada; horas lançadas fora de issues; labels `correcao` aplicadas onde devidas. Pendências são cobradas das duplas donas antes do cálculo.
3. O [Responsável](#responsavel) gera a página de acompanhamento. O script `assets/scripts/consolida_horas.py` roda automaticamente no build do ProperDocs (`uv run properdocs build` ou `serve`), lê as issues pela API do GitHub e publica [Medições Consolidadas](horas_consolidadas.md). Defina `GITHUB_TOKEN` no ambiente ou em um arquivo `.env` na raiz (não versionado) para evitar o limite de requisições. Os cálculos seguem as fórmulas de [3. Medidas e indicadores por categoria](plano_de_medicao.md#3-medidas-e-indicadores-por-categoria). A cada medição, confere-se à mão ao menos uma medida (por exemplo, o `CP1`) contra o resultado gerado.
4. O [Responsável](#responsavel) registra os valores consolidados na tabela de histórico ([seção 7.4](#historico)), indicando ponto de medição, data, valores das medidas base, valor derivado, nível e cor.
5. Em Mg-1, Mg-2 e Mg-3, o revisor preenche ou valida o `assets/dados/gestao/autoavaliacao.csv` para a fase correspondente, com um nível e uma evidência (link para o trecho do artigo, da GitPage ou do repositório) por critério. Antes disso, o Responsável confere o [registro de uso de IA](uso_de_ia.md).
6. O [Responsável](#responsavel) interpreta cada medida amarela ou vermelha: registra causa provável e decisão conforme as [Regras de Decisão](plano_de_medicao.md#regras), e abre issue de ação quando houver trabalho corretivo a fazer.
7. Medidas "sem dados" ou "com ressalva" são registradas como tal, com o motivo.
8. O resultado é comunicado ao grupo no mesmo dia e commitado por pull request.

<a id="pontos"></a>

## 3. Pontos de medição previstos

A Tabela 2 apresenta as datas das medições, sua finalidade e as medidas calculadas em cada uma.
 
| Id da Medição | Data | Finalidade | Medidas |
|---|---|---|---|
| Mg-1 | 26/10/2026 (seg) | Medição da Entrega 1 (Fases 1 e 2) | `CP1`, `CP2`, `DP1`, `DP2`, `RC1`, `RC2`, `Pa` |
| Mg-2 | 09/11/2026 (seg) | Medição do Ponto de Controle 2 (PC2) | `CP1`, `CP2`, `DP1`, `DP2`, `RC1`, `RC2`, `Pa` |
| Mg-3 | 18/11/2026 (qua) | Medição da Entrega 2 Final | `CP1`, `CP2`, `DP1`, `DP2`, `RC1`, `RC2`, `Pa` |

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
