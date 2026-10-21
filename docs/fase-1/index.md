# Fase 1: Planejamento da avaliação

A Fase 1 estabelece os requisitos da avaliação da Khan Academy. Nesta etapa, são definidos o propósito e o uso pretendido dos resultados, o produto e seu contexto de uso, as partes interessadas, as características de qualidade priorizadas e o recorte dos ensaios. A documentação também explicita o que pode ser observado externamente, os elementos excluídos e os limites de validade das conclusões.

A avaliação adota o modelo de qualidade de produto da **ISO/IEC 25010:2011** e prioriza **eficiência de desempenho**, **portabilidade** e **usabilidade**. Essas características são detalhadas em cinco requisitos de avaliação, `R1` a `R5`, relacionados às decisões `D1` a `D4`. A Fase 1 planeja a avaliação; não apresenta resultados de testes.

## Organização da Fase 1

A **Tabela 1** apresenta os temas da documentação, seus responsáveis e o acesso a cada página.

**Tabela 1. Organização e responsáveis pela documentação da Fase 1.**

| **Tema** | **Responsável** | **Página** |
| :--- | :--- | :--- |
| Caracterização do produto, contexto de uso, stakeholders e perfis de estudantes | [Enzo Menali](https://github.com/menali17) | [Produto e contexto](produto-e-contexto.md) |
| Propósito, uso pretendido, modelo de qualidade e priorização das características | [Luisa de Souza](https://github.com/luisa12ll) | [Requisitos de avaliação](requisitos-de-avaliacao.md) |
| Objetos, fluxos, ambientes, profundidade, exclusões, limites e relação com os ODS | [José Augusto](https://github.com/JAugustoM) | [Escopo da avaliação](escopo-da-avaliacao.md) |

*Fonte: organização da documentação da Fase 1. A indicação de responsabilidade refere-se à elaboração principal de cada artefato; as contribuições e revisões posteriores permanecem registradas nos respectivos históricos de versões.*

## Delimitação e relação com a Fase 2

O propósito da avaliação é produzir evidências que apoiem, em um cenário hipotético, a decisão de uma coordenação de escola pública sobre recomendar a Khan Academy Web em computadores e indicar as condições de acesso observadas. Estudantes são os usuários primários; professores e responsáveis são usuários de apoio; a equipe avaliadora define o desenho de medição; e a Khan Academy é fornecedora do produto e destinatária potencial dos achados.

O objeto dos ensaios é a **plataforma web acessada por navegadores em computadores**, sob uma abordagem externa de caixa-preta. Os fluxos incluem localizar conteúdo, reproduzir uma videoaula, responder a um exercício e consultar o progresso da própria conta. Aplicativos nativos, navegadores móveis, painéis de professores e responsáveis, infraestrutura interna, testes ativos de segurança e avaliação pedagógica do conteúdo permanecem fora do escopo.

Os ambientes `A1` a `A4` contemplam combinações dirigidas de Windows, macOS e Ubuntu com Chrome, Firefox e Safari. A acessibilidade inclui navegação por teclado e leitores de tela nas combinações previstas e, no ambiente `A1`, inspeções separadas com zoom de 200% e alto contraste do Windows para o perfil de baixa visão. Esses procedimentos não representam todas as pessoas com deficiência nem comprovam conformidade integral com as WCAG.

Os requisitos definidos nesta etapa orientam a estrutura GQM da [Fase 2](../fase-2/index.md): `R1` e `R2` fundamentam `G1`, `R3` fundamenta `G2`, e `R4` e `R5` fundamentam `G3`. Assim, objetivos, questões e métricas devem permanecer coerentes com o propósito, os stakeholders, os fluxos, os ambientes e os limites estabelecidos na Fase 1.

## Referências

- [Produto e contexto](produto-e-contexto.md). Caracterização da Khan Academy, stakeholders, interfaces, dependências e perfis de estudantes.
- [Requisitos de avaliação](requisitos-de-avaliacao.md). Propósito, decisões `D1` a `D4`, características priorizadas e requisitos `R1` a `R5`.
- [Escopo da avaliação](escopo-da-avaliacao.md). Objetos, fluxos, ambientes, profundidade, exclusões, limites de validade e relação com os ODS.
- [Critérios de avaliação da Fase 1](../criterios/fase1.md), disciplina Qualidade de Software 1, UnB/FGA, 2026/2.
- **ISO/IEC 25010:2011**: *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 20/10/2026 | Estruturação da visão geral da Fase 1, organização dos artefatos e síntese da delimitação e da rastreabilidade com a Fase 2. | [Enzo Menali](https://github.com/menali17) | |
