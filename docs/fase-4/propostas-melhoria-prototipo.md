# Propostas de melhoria e ajustes

**Versão 1.1**

## 1. Introdução

Este artefato apresenta ajustes propostos para a interface da Khan Academy com base nos problemas identificados durante a [avaliação de apreensibilidade](registro-apreensibilidade.md) e na [análise de adaptabilidade](registro-adaptabilidade.md).

O objetivo é demonstrar como os resultados das avaliações orientaram melhorias na experiência dos usuários, representadas em um protótipo de alta fidelidade desenvolvido no Figma. As modificações buscam tornar determinadas interações mais claras, previsíveis e coerentes com as necessidades observadas durante a execução das tarefas avaliadas.

As propostas preservam a identidade visual e a organização geral da Khan Academy, concentrando as alterações nos elementos associados às dificuldades observadas. Dessa forma, o protótipo procura demonstrar soluções pontuais, sem propor uma reformulação completa da plataforma.

## 2. Fundamentação das melhorias

A avaliação de apreensibilidade evidenciou dificuldades na localização de cursos, na identificação de conteúdos e no acesso às dicas dos exercícios ([registros F3](registro-apreensibilidade.md#tabela-3-f3)).

Os resultados da [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) indicaram que **46,67% das primeiras tentativas elegíveis apresentaram pelo menos um erro operacional**, com maior incidência nas tarefas [T2](../fase-1/escopo-da-avaliacao.md#fluxos) e [T3](../fase-1/escopo-da-avaliacao.md#fluxos), ambas com 60%.

Esses resultados apontam oportunidades de melhoria na forma como a interface comunica as opções disponíveis e orienta o usuário durante a navegação. Em determinadas situações, os participantes precisaram explorar diferentes caminhos ou corrigir ações realizadas anteriormente para alcançar seus objetivos.

Além desses resultados, a análise de adaptabilidade identificou uma inadequação no feedback apresentado após a conclusão de exercícios com utilização prévia de todas as dicas. Essa observação também orientou uma proposta de adequação do feedback ao estado de interação, considerando as informações que o usuário já recebeu durante a resolução.

Essas evidências fundamentaram as melhorias representadas no protótipo, procurando estabelecer uma relação direta entre os problemas observados e as alterações propostas.

## 3. Ajustes propostos

### 3.1. Busca e seleção de cursos

**Problema identificado:** Durante a [T1](../fase-1/escopo-da-avaliacao.md#fluxos), participantes encontraram dificuldades para localizar o curso de Matemática do 6º ano, recorrendo a diferentes termos de pesquisa, filtros e páginas de resultados.

A dificuldade esteve relacionada à identificação do resultado mais adequado à pesquisa, exigindo atenção adicional para distinguir o curso desejado de outros conteúdos apresentados.

**Melhoria proposta:** Priorizar resultados correspondentes à série/ano pesquisada, com identificação clara do curso, da unidade e do tipo de conteúdo. Os filtros permanecem visíveis para facilitar o refinamento da busca.

No protótipo, a apresentação dos resultados procura destacar a correspondência com o termo pesquisado, permitindo que o usuário reconheça o curso relevante com maior facilidade. A interação de pesquisa também preserva o comportamento de expansão do campo de busca presente na interface original.

**Resultado esperado:** Reduzir o esforço necessário para localizar o curso solicitado e facilitar a identificação de resultados relevantes, diminuindo a necessidade de percorrer opções que não correspondem ao objetivo da pesquisa.

### 3.2. Identificação dos tipos de conteúdo

**Problema identificado:** Na [T2](../fase-1/escopo-da-avaliacao.md#fluxos), três participantes acessaram exercícios quando pretendiam abrir videoaulas, precisando corrigir o percurso de navegação ([registros F3](registro-apreensibilidade.md#tabela-3-f3)).

Essa ocorrência evidencia uma dificuldade de reconhecimento dos diferentes tipos de atividade, especialmente quando sua identificação depende predominantemente de elementos gráficos.

**Melhoria proposta:** Acrescentar rótulos textuais que identifiquem os conteúdos como **Vídeo**, **Artigo** ou **Exercício**.

Os rótulos funcionam como uma informação complementar aos ícones existentes, permitindo que o usuário identifique a natureza do conteúdo antes de selecioná-lo. A proposta não modifica a organização principal da página, apenas torna mais explícita uma informação importante para a navegação.

**Resultado esperado:** Facilitar o reconhecimento dos conteúdos e reduzir seleções equivocadas, contribuindo para que o usuário escolha a atividade correspondente ao seu objetivo.

### 3.3. Visibilidade das dicas

**Problema identificado:** Na [T3](../fase-1/escopo-da-avaliacao.md#fluxos), os participantes apresentaram dificuldades para descobrir como acessar as dicas. A funcionalidade dependia do estado da resposta, mas essa condição não era suficientemente evidente ([registros F3](registro-apreensibilidade.md#tabela-3-f3)).

A apresentação das dicas somente em determinados momentos da interação dificultava a descoberta da funcionalidade e limitava a possibilidade de solicitar auxílio antes de responder.

**Melhoria proposta:** Manter o acesso às dicas **visível e disponível desde o início da questão**, permitindo que o usuário consulte as orientações tanto antes quanto depois de enviar uma resposta, independentemente de ela estar correta ou incorreta.

No protótipo, o botão de dicas permanece acessível durante a resolução. Ao selecioná-lo, o usuário pode visualizar orientações progressivas, sem perder as alternativas que já marcou. Dessa forma, a funcionalidade passa a oferecer suporte durante todo o processo, e não apenas após uma tentativa incorreta.

**Resultado esperado:** Facilitar a descoberta e a utilização das dicas, ampliar a autonomia do usuário durante a resolução dos exercícios e diminuir a necessidade de orientação externa.

### 3.4. Adequação do feedback após respostas corretas

**Problema identificado:** Após uma resposta correta, a plataforma apresenta uma mensagem positiva acompanhada da opção de visualizar a resolução passo a passo. Entretanto, essa opção também aparece quando o usuário já consultou todas as dicas e visualizou a resolução completa, tornando a ação redundante.

Nessa situação, o feedback deixa de considerar adequadamente o histórico de interação do usuário, oferecendo uma opção que não acrescenta novas informações.

**Melhoria proposta:** Diferenciar o feedback de acordo com o estado de utilização das dicas, considerando se o usuário já teve acesso à resolução completa antes de confirmar sua resposta.

| Situação | Feedback proposto |
|---|---|
| Resposta correta sem visualizar todas as dicas | Manter a mensagem positiva e a opção de consultar a resolução passo a passo. |
| Resposta correta após visualizar todas as dicas | Confirmar o acerto, informar que a resolução já foi visualizada e oferecer a opção de avançar para a próxima pergunta. |

*Tabela 1. Estados de feedback propostos após respostas corretas. Fonte: elaborada por [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

Essa mudança busca adequar a resposta da interface às ações anteriormente realizadas pelo usuário, evitando a apresentação de opções sem efeito útil.

Para representar esse comportamento, o protótipo também contempla a seleção e o envio de respostas, incluindo situações em que o usuário responde incorretamente. Nesses casos, é apresentado um feedback de erro, com possibilidades de revisar as alternativas ou consultar as dicas antes de realizar outra tentativa. Essa interação permite demonstrar os diferentes estados da questão até sua conclusão.

**Resultado esperado:** Tornar o feedback mais coerente, compreensível e adequado ao contexto de interação, evitando informações repetitivas e oferecendo orientações compatíveis com o percurso realizado pelo usuário.

## 4. Protótipo de alta fidelidade

O protótipo reúne as propostas de busca e seleção de cursos, identificação dos tipos de conteúdo, acesso às dicas e adequação do feedback ao percurso realizado pelo usuário.

### Navegação e verificação das melhorias

A navegação pelo protótipo inicia-se na página principal da Khan Academy, seguindo para a pesquisa do curso de Matemática do 6º ano e a identificação dos diferentes tipos de conteúdo. Em seguida, o fluxo permite acessar o exercício, selecionar e enviar respostas, consultar as dicas antes ou depois do envio e observar os feedbacks apresentados para respostas corretas ou incorretas. Também é possível verificar como o feedback se adapta conforme a resolução completa tenha sido consultada ou não.

### Visualização do protótipo

<div style="width: 100%; margin: 24px 0;">
  <iframe
    src="https://embed.figma.com/proto/jwvkPL3ZlOstD6ii0L4h1X?embed-host=github-pages&node-id=55-72&starting-point-node-id=55%3A72&scaling=contain&content-scaling=fixed&page-id=0%3A1"
    title="Protótipo interativo de alta fidelidade — Khan Academy"
    width="100%"
    height="720"
    style="border: 1px solid #d9dfe7; border-radius: 8px;"
    allowfullscreen
    loading="lazy">
  </iframe>
</div>

**Acesso ao protótipo:** [Abrir protótipo interativo — Khan Academy (Figma)](https://www.figma.com/proto/jwvkPL3ZlOstD6ii0L4h1X?node-id=55-72&scaling=contain&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=55%3A72).

## 5. Considerações finais

Os ajustes propostos procuram responder às dificuldades identificadas na avaliação, principalmente na encontrabilidade dos cursos, na identificação de conteúdos, na descoberta das dicas e na adequação do feedback ao contexto do usuário.

O protótipo estabelece uma relação entre os problemas observados e possíveis soluções de interface, contribuindo para a discussão de melhorias na usabilidade da Khan Academy. A possibilidade de navegar pelas telas e experimentar diferentes respostas também permite visualizar, de maneira prática, como as modificações podem influenciar a interação.

Sua principal contribuição é apresentar alternativas fundamentadas que poderão ser avaliadas posteriormente quanto à eficácia, à clareza e à adequação às necessidades dos usuários. Dessa forma, as propostas constituem uma representação das melhorias identificadas, sem pressupor que seus benefícios já tenham sido comprovados por uma nova avaliação.

## Referências

- [Avaliação de apreensibilidade — Fase 4](registro-apreensibilidade.md).
- [Registro de execução de adaptabilidade — Fase 4](registro-adaptabilidade.md).
- [Métrica M13 — Taxa de erros operacionais](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais).
- [Procedimentos de acessibilidade e apreensibilidade — Fase 3](../fase-3/procedimentos-acessibilidade-apreensibilidade.md).
- KHAN ACADEMY. [Plataforma Khan Academy](https://pt.khanacademy.org/).

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 23/11/2026 | Criação do artefato com fundamentação, propostas de melhoria, protótipo e limitações. | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 24/11/2026 | Complementação das descrições, atualização do funcionamento das dicas e inclusão do protótipo interativo incorporado e das orientações de navegação. | [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
