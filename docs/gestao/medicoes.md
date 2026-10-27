# Procedimento de medição

Este artefato descreve como a medição é executada: quais dados entram, o passo a passo de cada rodada e em que datas ela ocorre.
 
<a id="responsavel"></a>

**Responsável pela execução:**A equipe definirá, antes de cada ponto de medição, o integrante responsável pela coleta, validação e consolidação dos dados. Todos os integrantes devem registrar suas horas até as 12h do dia da medição. O responsável verifica as pendências, executa o script, registra os resultados e documenta as decisões decorrentes.

### 7.1 Dados de entrada

A Tabela 9 lista os dados necessários, onde ficam, quem os alimenta e quais medidas dependem deles.
 
| Dado | Fonte | Quem alimenta | Quando | Medidas que usam |
|---|---|---|---|---|
| ID, Janela, Estimativa, estado, datas de fechamento e reabertura, labels | Issues e pull requests do GitHub | Responsável pela issue | Ao criar, fechar ou reabrir a issue | `CP1`, `CP2`, `DP1`, `RC2` |
| Horas por integrante e por issue | `assets/dados/gestao/horas/<usuario>.csv` (colunas `data,atividade,horas`; ver [Registro de Horas](horas.md)) | Cada integrante | Até 12h do dia da medição | `RC1`, `RC2` |
| Nível por critério da rubrica | `assets/dados/gestao/autoavaliacao.csv` (colunas `data,criterio,nivel,evidencia`) | Revisor | Em [Mg-3](#pontos) | `DP2` |
| Uso de IA | [Uso de IA](uso_de_ia.md) | Quem usou a ferramenta | No momento do uso | Evidência para os critérios de uso de IA na autoavaliação (`DP2`) |
 
*Tabela 9. Dados de entrada das medições. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*
 
No `autoavaliacao.csv`, `criterio` é o código da rubrica (por exemplo, `F1-C6`) e `nivel` é um de Insuficiente, Regular, Satisfatório ou Excelente, que correspondem, nesta ordem, às quatro opções da rubrica da professora, da primeira à última.
 
### 7.2 Passos

Os passos abaixo são seguidos a cada ponto de medição.
 
1. Até as 12h do dia da medição, cada membro lança suas horas no seu CSV.
2. O [Responsável](#responsavel) confere as pré-condições: issues fechadas com Janela, Estimativa e revisão registrada; horas sem ID válido; labels `correcao` aplicadas onde devidas. Pendências são cobradas das duplas donas antes do cálculo.
3. A [Responsável](#responsavel) roda `python3 scripts/coletar_psm.py --data AAAA-MM-DD` na raiz do repositório. O script deve implementar as fórmulas da [seção 3](#3-medidas-e-indicadores-por-categoria). A cada medição, conferir à mão ao menos uma medida (por exemplo, o `CP1`) contra o resultado do script.
4. O [Responsável](#responsavel) cola a tabela no registro de `docs/gestao/medicoes.md`, com, para cada medida: ponto de medição, data, valores das medidas base, valor derivado, nível e cor.
5. Em [Mg-2 e Mg-3](#pontos), o revisor, preenche o `autoavaliacao.csv` para a fase correspondente, com um nível e uma evidência (link para o trecho do artigo, da GitPage ou do repositório) por critério. Antes disso, o [Responsável](#responsavel) confere o [registro de uso de IA](uso_de_ia.md).
6. O [Responsável](#responsavel) interpreta cada medida amarela ou vermelha: registra causa provável e decisão conforme a [seção 6](#regras), e abre issue de ação quando houver trabalho a fazer.
7. Medidas "sem dados" ou "com ressalva" são registradas como tal, com o motivo.
8. O resultado é comunicado ao grupo no mesmo dia e commitado por pull request.

<a id="pontos"></a>

### 7.3 Pontos de medição

A Tabela 10 apresenta as datas das medições, sua finalidade e as medidas calculadas em cada uma. Até o momento as datas estão referentes apenas a entrega 1.    

| Id da Medição | Data | Finalidade | Medidas |
|---|---|---|---|
| Mg-1 | 26/10 (seg) | Medição Entrega 1 | `CP1`, `CP2`, `DP1`, `DP2`, `RC1`, `RC2` |
| Mg-2 | XX/11 () | A definir para Entrega 2 | --- |
| Mg-3 | XX/11 () | A definir para Entrega 2 | --- |

*Tabela 10. Pontos de medição previstos. Fonte: Elaborado por: [Pedro Lucas](https://github.com/Pwdrinho)*

Os pontos de medição apresentados nesta tabela correspondem à Entrega 1. O acompanhamento da Entrega 2, prevista para 18/11/2026, deverá ser detalhado em um cronograma complementar, caso esteja incluído no escopo de execução deste plano.

As medições de Mg-1 usam poucas issues concluídas e podem cair em "sem dados" ou oscilar muito; isso é esperado e deve constar na interpretação.
 