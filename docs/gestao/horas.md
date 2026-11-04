# Registro de Horas

Versão 1.2

---

## 1. Para que serve

Este registro é a fonte de dados das medições de **Recursos e Custos** do [Plano de medição](plano_de_medicao.md): `RC1` (esforço total e equilíbrio entre integrantes), `RC2` (variação entre esforço estimado e realizado) e `RC3` (cobertura do registro de esforço). Também serve de base para o custo equivalente do trabalho. Se as horas não forem lançadas, ou forem lançadas sem o ID da issue, essas medições perdem a confiabilidade.

## 2. Como registrar (cada integrante)

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

## 3. Como as horas viram medidas

| Medida | Como usa o registro |
|---|---|
| `RC1` | `Et` é a soma de todas as horas lançadas nas issues; `Hi` é a soma por integrante; `Hm = Et ÷ n`. Alerta de desequilíbrio se algum `Hi` ficar fora de ±50% de `Hm` |
| `RC2` | Para cada issue concluída, compara as horas lançadas (`Hr`) com a Estimativa original da issue (`He`). `Ve = (ABS(Er − Ee) ÷ Ee) × 100` |
| `RC3` | `Pa` é o percentual de issues concluídas que têm ao menos uma linha na Tabela de Contribuição |

## 4. Consolidado (preenchido pela Dupla C a cada medição)

A Dupla C preenche os quadros abaixo a partir da página [Medições Consolidadas](horas_consolidadas.md), gerada automaticamente das issues. Os integrantes não precisam preencher esta parte. Copie o bloco 4.1 para cada nova semana.

A tabela semanal anterior deste arquivo tinha as colunas Início, Fim e Total. Elas foram substituídas por uma única coluna de horas, que é o dado que as medições usam, e foram acrescentadas as colunas de integrante e de ID da issue.

### 4.1 Atividades realizadas: semana 15/10 a 18/10

| Data | Integrante | ID da issue | Atividade | Horas |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

**Total de horas da semana:**

### 4.2 Esforço por integrante (`RC1`)

| Integrante | Horas (`Hi`) | Relação com a média (`Hi ÷ Hm`) | Dentro de ±50% |
|---|---|---|---|
|  |  |  |  |

**Esforço total (`Et`):** &nbsp; **Média por integrante (`Hm`):**

### 4.3 Estimado e realizado por issue concluída (`RC2` e `RC3`)

| ID da issue | Estimativa original (`He`) | Horas realizadas (`Hr`) | Desvio (`Hr − He`) | Sentido |
|---|---|---|---|---|
|  |  |  |  |  |

**`Ee`:** &nbsp; **`Er`:** &nbsp; **`Ve`:** &nbsp; **`Pa`:**

### 4.4 Custo equivalente

Valor de referência da hora (`Vh`): **a definir pela equipe, com fonte.** Custo equivalente = `Et × Vh`: a calcular após a definição de `Vh`.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | Commit |
|---|---|---|---|---|---|
| 1.0 | 14/10/2026 | Modelo de registro semanal | [Pedro Lucas](https://github.com/Pwdrinho) | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |
| 1.1 | 15/10/2026 | Adequação às medições `RC1`, `RC2` e `RC3`: instruções de uso, CSV por integrante e quadros consolidados | [Pedro Lucas](https://github.com/Pwdrinho) | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |
| 1.2 | 04/11/2026 | Registro de horas migrado dos CSVs para a Tabela de Contribuição das issues | | | [](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/) |
