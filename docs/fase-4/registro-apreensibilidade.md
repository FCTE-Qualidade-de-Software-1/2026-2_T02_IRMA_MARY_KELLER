# Registro de execução e análise da apreensibilidade — Fase 4

**Versão 1.2**

## 1. Introdução e finalidade do artefato

Este artefato documenta a **execução, a coleta, o tratamento, a análise e o julgamento dos testes de apreensibilidade** da plataforma web Khan Academy, realizados na Fase 4 do processo de avaliação de qualidade. O foco é verificar se pessoas adultas sem experiência prévia com a plataforma conseguem compreender como iniciar e concluir tarefas essenciais após uma instrução inicial padronizada, sem assistência adicional.

O documento consolida a triagem dos voluntários (F2), a caracterização do ambiente (F7), os registros de tarefas (F3), as respostas de percepção (F4), as gravações autorizadas e o cálculo das métricas [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos), [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) e [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma). Os resultados são confrontados com a questão [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade), a hipótese [`H11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) e o objetivo [`G3`](../fase-2/objetivos.md#g3) — Usabilidade, definidos na Fase 2, considerando os procedimentos da [Fase 3](../fase-3/procedimentos-acessibilidade-apreensibilidade.md). As conclusões subsidiam melhorias concretas de navegação e orientação para novos usuários, em consonância com o propósito e o requisito [`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade) da Fase 1.


## 2. Tarefas executadas

Os três roteiros reproduzem os fluxos essenciais da Fase 1. Cada tarefa teve **limite de observação de 5 minutos**, sem avaliar o conhecimento matemático do participante.

| Tarefa | Fluxo | Instrução ao participante | Ações e critério de conclusão | Limite |
|---|---|---|---|---|
| **T1 — Localização de curso** | [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) | “Você quer estudar Matemática do 6º ano. Encontre esse curso e abra a primeira parte dele.” | Localizar o curso, acessar a primeira unidade e exibir a lista de aulas. | 5 min |
| **T2 — Videoaula** | [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) | “Agora abra a videoaula indicada no cartão. Comece o vídeo, pause e, se houver, ative a legenda ou a transcrição.” | Abrir a videoaula, reproduzir, pausar e acionar legenda/transcrição quando disponível. | 5 min |
| **T3 — Exercício** | [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) | “Abra o exercício indicado no cartão. Se houver uma dica, abra-a. Informe a resposta de teste escrita no cartão e envie.” | Abrir o exercício, consultar dica quando disponível, enviar a resposta padronizada e visualizar o retorno da plataforma. | 5 min |

*Tabela 1. Tarefas de apreensibilidade e critérios de conclusão. Fonte: procedimentos da Fase 3 [S7](#s7), adaptados para este registro. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

## 3. Perfil e consentimento dos voluntários (F2)

A triagem foi realizada por formulário eletrônico antes da execução das sessões. Foram obtidas **cinco respostas**. As figuras a seguir reproduzem, na ordem das perguntas, as distribuições dos gráficos fornecidos pela equipe. Os dados pessoais dos participantes não são publicados.

### 3.1. Verificação de maioridade

**Pergunta inicial — Você tem mais de 18 anos?**

<div class="ap-chart"><canvas id="f2-maioridade" aria-label="Maioridade: cinco respostas Sim"></canvas></div>

*Figura 1. Verificação de maioridade: cinco respostas “Sim” (100%). Fonte: F2.*

### 3.2. Faixa etária

**Pergunta 1 — Qual é a sua faixa etária?**

<div class="ap-chart"><canvas id="f2-idade" aria-label="Faixa etária: cinco participantes de 18 a 24 anos"></canvas></div>

*Figura 2. Faixa etária: cinco participantes entre 18 e 24 anos (100%). Fonte: F2.*

A amostra é integralmente composta por jovens adultos de 18 a 24 anos, o que limita a extrapolação dos resultados para outras faixas etárias.

### 3.3. Experiência prévia com a plataforma

**Pergunta 2 — Você já utilizou a Khan Academy?**

<div class="ap-chart"><canvas id="f2-khan" aria-label="Experiência prévia: cinco respostas Não após retificação"></canvas></div>

*Figura 3. Experiência prévia: cinco respostas “Não” (100%), após retificação comunicada pela equipe. Fonte: F2 e confirmação posterior da equipe.*

A equipe confirmou que nenhum voluntário havia utilizado a Khan Academy anteriormente. Uma resposta inicialmente marcada como “Sim” foi considerada incorreta; o gráfico apresenta a **informação retificada**, não a transcrição literal do formulário original. A correção deve permanecer verificável junto ao registro original e à confirmação da equipe.

### 3.4. Frequência de uso do computador

**Pergunta 3 — Com que frequência você utiliza computador com mouse e teclado no seu dia a dia?**

<div class="ap-chart"><canvas id="f2-computador" aria-label="Escala de frequência: uma resposta 3 e quatro respostas 5"></canvas></div>

*Figura 4. Frequência de uso em escala de 1 a 5: uma resposta no nível 3 (20%) e quatro no nível 5 (80%). Fonte: F2.*

A maior parte dos participantes assinalou o nível máximo da escala. Uma pessoa marcou o nível intermediário; a elegibilidade desse caso depende da definição operacional de “uso habitual” estabelecida pela equipe.

### 3.5. Atuação profissional relacionada

**Pergunta 4 — Você trabalha com testes de software, design de interfaces ou desenvolvimento web?**

<div style="max-width: 420px; height: 320px; margin: 20px auto;"><canvas id="f2-profissao" aria-label="Atuação profissional: cinco respostas Não e nenhuma Sim"></canvas></div>

*Figura 5. Atuação profissional dos participantes. Fonte: F2.*

**Interpretação:** todos os cinco participantes (100%) declararam não trabalhar com testes de software, design de interfaces ou desenvolvimento web, atendendo ao critério de elegibilidade profissional estabelecido no protocolo da avaliação de apreensibilidade.

### 3.6. Plataformas de estudo on-line

**Pergunta 5 — Quais plataformas de estudo on-line você já utilizou?**

<div class="ap-chart" style="max-width:750px;height:350px;margin:20px auto"><canvas id="f2-plataformas" aria-label="Plataformas de estudo on-line: YouTube, Duolingo, Google Classroom e Udemy ou Coursera"></canvas></div>

*Figura 6. Plataformas de estudo on-line utilizadas pelos participantes. Fonte: formulário F2.*

Como a pergunta permite indicar mais de uma plataforma, as contagens não são mutuamente exclusivas e podem somar mais do que o número de participantes.

### 3.7. Consentimento voluntário

**Pergunta 6 — Você leu as informações e concorda em participar voluntariamente da avaliação?**

<div class="ap-chart"><canvas id="f2-consentimento" aria-label="Consentimento: cinco respostas Sim, concordo"></canvas></div>

*Figura 7. Aceite voluntário: cinco respostas “Sim, concordo” (100%). Fonte: F2.*

### 3.8. Autorização para gravação

**Pergunta 7 — Você autoriza a gravação da tela e do áudio do computador durante a sessão?**

<div class="ap-chart"><canvas id="f2-gravacao" aria-label="Autorização de gravação: cinco respostas Sim, autorizo"></canvas></div>

*Figura 8. Autorização de gravação: cinco respostas “Sim, autorizo” (100%). Fonte: F2.*

Todos os respondentes assinalaram consentimento e autorização de gravação. A publicação dos vídeos em ambiente público deve respeitar o alcance efetivo dessa autorização, incluindo eventual identificação indireta.

## 4. Ambiente e padronização das sessões (F7)

As cinco sessões foram registradas em **18/11/2026**, no ambiente **A1**, com o mesmo sistema operacional, navegador e resolução. Essa uniformidade reduz diferenças de apresentação entre participantes. O **zoom de 100%** e o uso de **mouse** foram informados para todas as sessões. URLs e recursos opcionais não foram registrados.

| Sessão | Data | Avaliadores | Ambiente | Sistema operacional | Navegador e versão | Resolução | Zoom | Dispositivos de entrada | Fluxos e tarefas |
|---|---|---|---|---|---|---|---|---|---|
| S1 | 18/11/2026 | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Windows 11 Pro (25H2) | Google Chrome 157.0.8103.51 (64 bits) | 1920 × 1200 | 100% | Mouse | T1, T2 e T3 ([`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos)–[`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos)) |
| S2 | 18/11/2026 | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Windows 11 Pro (25H2) | Google Chrome 157.0.8103.51 (64 bits) | 1920 × 1200 | 100% | Mouse | T1, T2 e T3 ([`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos)–[`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos)) |
| S3 | 18/11/2026 | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Windows 11 Pro (25H2) | Google Chrome 157.0.8103.51 (64 bits) | 1920 × 1200 | 100% | Mouse | T1, T2 e T3 ([`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos)–[`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos)) |
| S4 | 18/11/2026 | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Windows 11 Pro (25H2) | Google Chrome 157.0.8103.51 (64 bits) | 1920 × 1200 | 100% | Mouse | T1, T2 e T3 ([`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos)–[`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos)) |
| S5 | 18/11/2026 | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Windows 11 Pro (25H2) | Google Chrome 157.0.8103.51 (64 bits) | 1920 × 1200 | 100% | Mouse | T1, T2 e T3 ([`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos)–[`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos)) |

*Tabela 2. Registro do ambiente de cada sessão (F7). Fonte: registros fornecidos pela equipe. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

A resolução efetivamente registrada foi **1920 × 1200**, com zoom de **100%** e uso de **mouse** em todas as sessões. A comparação com a configuração-base prevista para [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) é relevante porque diferenças de resolução podem alterar a disposição dos controles de navegação.

## 5. Evidências audiovisuais e observações por sessão

Os vídeos foram fornecidos pela equipe na ordem S1–S5. As observações a seguir descrevem o comportamento observado em cada gravação e complementam os registros de execução (F3) e os relatos pós-teste (F4). Os vídeos constituem evidências de cada sessão, condicionadas à autorização específica de divulgação dos participantes.

### 5.1. Sessão S1 — Pessoa 1

<iframe width="560" height="315" style="max-width:100%;border:0" src="https://www.youtube-nocookie.com/embed/Vm9Yx6u5Wlw" title="Registro da sessão S1 — avaliação de apreensibilidade" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Observações:** A participante apresentou dificuldades para localizar o curso de Matemática do 6º ano pela busca, recorrendo ao menu **Explorar** e demonstrando alguma hesitação ao acessar a primeira unidade. Na T2, identificou os controles da videoaula e a transcrição sem dificuldades relevantes. Na T3, inicialmente não encontrou uma opção evidente para consultar as dicas e, após enviar uma resposta incorreta, conseguiu acessar o recurso **Mostrar uma etapa**. O comportamento evidencia dificuldades na busca pelo curso e na descoberta inicial das dicas.

### 5.2. Sessão S2 — Pessoa 2

<iframe width="560" height="315" style="max-width:100%;border:0" src="https://www.youtube-nocookie.com/embed/Zrzeuq3FyDY" title="Registro da sessão S2 — avaliação de apreensibilidade" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Observações:** A participante localizou o curso de maneira relativamente direta pela opção **Adicionar outro curso**. Na T2, identificou os controles de reprodução e legendas, embora tenha ocorrido uma aparente interrupção visual do vídeo. Na T3, conseguiu abrir o exercício e enviar uma resposta, mas não encontrou como acessar as dicas. Após acertar a primeira questão, explorou a ferramenta de desenho na questão seguinte, sem conseguir visualizar o recurso solicitado. A sessão evidencia uma dificuldade de apreensibilidade relacionada à identificação das dicas, que não estavam disponíveis de maneira evidente.

### 5.3. Sessão S3 — Pessoa 3

<iframe width="560" height="315" style="max-width:100%;border:0" src="https://www.youtube-nocookie.com/embed/Pq6b5v_sKPE" title="Registro da sessão S3 — avaliação de apreensibilidade" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Observações:** O participante apresentou dificuldades para localizar o curso, realizando diversas pesquisas e utilizando filtros até acessar a primeira unidade por meio da navegação lateral. Na T2, utilizou os controles da videoaula com facilidade. Na T3, inicialmente não identificou como consultar as dicas e precisou enviar uma resposta incorreta para que o botão **Mostrar uma etapa** aparecesse. Após encontrá-lo, conseguiu percorrer as dicas disponíveis, demonstrando que a principal dificuldade estava na descoberta do recurso, e não em sua utilização.

### 5.4. Sessão S4 — Pessoa 4

<iframe width="560" height="315" style="max-width:100%;border:0" src="https://www.youtube-nocookie.com/embed/ZCx6TEb8Rks" title="Registro da sessão S4 — avaliação de apreensibilidade" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Observações:** O participante enfrentou dificuldades para localizar o curso pela busca, precisando percorrer quatro páginas de resultados. Na T2, utilizou os controles da videoaula e acessou a transcrição sem dificuldades relevantes. Na T3, apresentou momentos de hesitação durante a exploração do exercício e não identificou inicialmente o acesso às dicas. Somente após enviar uma resposta incorreta encontrou o botão **Mostrar uma etapa**, conseguindo utilizar as dicas disponíveis. O comportamento reforça a dificuldade de descoberta desse recurso na primeira interação.

### 5.5. Sessão S5 — Pessoa 5

<iframe width="560" height="315" style="max-width:100%;border:0" src="https://www.youtube-nocookie.com/embed/k-5FmNxrR-Q" title="Registro da sessão S5 — avaliação de apreensibilidade" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Observações:** O participante encontrou o curso de forma direta pela opção **Editar cursos** e utilizou os controles da videoaula sem dificuldades relevantes. Na T3, conseguiu abrir o exercício e enviar respostas, mas também não identificou inicialmente como acessar as dicas. O recurso **Mostrar uma etapa** tornou-se acessível após uma resposta incorreta, permitindo que consultasse as orientações disponíveis.

## 6. Registros de execução por tarefa (F3)

A Tabela 3 reproduz os quinze registros fornecidos pela equipe, com **tempos padronizados em segundos**, e incorpora a reanálise dos erros operacionais nas gravações. Para T3 de S1, por exemplo, `01:27.75` foi convertido para **87,75 s**. A coluna de horários apresenta resolução de minuto, enquanto a cronometragem apresenta centésimos de segundo; por isso, os tempos cronometrados são a referência de M14.

| Sessão | Participante | Tarefa | Início | Fim | Tempo (s) | Concluiu | Autônoma | Pedidos de ajuda | Erros operacionais | Falha técnica | Desistiu |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | Pessoa 1 | T1 | 10:23 | 10:24 | 51,79 | Sim | Sim | Não | Nenhum confirmado | Nenhuma registrada | Não |
| S1 | Pessoa 1 | T2 | 10:24 | 10:25 | 20,41 | Sim | Sim | Não | **1 confirmado** — abriu exercício em vez de videoaula; corrigiu pelo menu lateral (02:06–02:16) | Nenhuma registrada | Não |
| S1 | Pessoa 1 | T3 | 10:28 | 10:30 | 87,75 | Sim | Não | Sim | **1 confirmado** — acessou página diferente do exercício e precisou retornar ou consultar novamente o menu lateral | Nenhuma registrada | Não |
| S2 | Pessoa 2 | T1 | 10:37 | 10:38 | 51,18 | Sim | Sim | Não | Nenhum confirmado | Nenhuma registrada | Não |
| S2 | Pessoa 2 | T2 | 10:38 | 10:39 | 26,97 | Sim | Sim | Não | **1 confirmado** — abriu exercício em vez de videoaula; corrigiu pelo menu lateral (01:12–01:54) | Nenhuma registrada | Não |
| S2 | Pessoa 2 | T3 | 10:40 | 10:41 | 60,80 | **Não** | Não | Sim | Nenhum confirmado | Nenhuma registrada | **Sim** |
| S3 | Pessoa 3 | T1 | 11:11 | 11:13 | 154,36 | Sim | Não | Sim | **2 confirmados** — abriu Matemática EM: Álgebra 1 (00:24–00:32) e exercício da Unidade 6 (03:16–03:32); corrigiu a navegação | Nenhuma registrada | Não |
| S3 | Pessoa 3 | T2 | 11:14 | 11:14 | 12,68 | Sim | Sim | Não | Nenhum confirmado | Nenhuma registrada | Não |
| S3 | Pessoa 3 | T3 | 11:14 | 11:15 | 59,35 | Sim | Não | Sim | **2 ocorrências confirmadas na tentativa** — acessou página diferente do exercício e corrigiu pelo menu lateral; também acionou Pular em vez de Verificar e cancelou o modal (04:58–05:00) | Nenhuma registrada | Não |
| S4 | Pessoa 4 | T1 | 11:21 | 11:22 | 77,64 | Sim | Sim | Não | Nenhum confirmado | Nenhuma registrada | Não |
| S4 | Pessoa 4 | T2 | 11:23 | 11:23 | 24,91 | Sim | Sim | Não | Nenhum confirmado | Nenhuma registrada | Não |
| S4 | Pessoa 4 | T3 | 11:25 | 11:26 | 108,56 | Sim | Não | Sim | **1 confirmado** — acessou página diferente do exercício e precisou retornar ou consultar novamente o menu lateral | Nenhuma registrada | Não |
| S5 | Pessoa 5 | T1 | 11:48 | 11:48 | 26,04 | Sim | Sim | Não | Nenhum confirmado | Nenhuma registrada | Não |
| S5 | Pessoa 5 | T2 | 11:49 | 11:49 | 19,70 | Sim | Sim | Não | **1 confirmado** — abriu exercício em vez de videoaula; corrigiu pelo menu lateral (01:22–02:18) | Nenhuma registrada | Não |
| S5 | Pessoa 5 | T3 | 11:49 | 11:50 | 60,85 | Sim | Não | Sim | Nenhum confirmado | Nenhuma registrada | Não |

*Tabela 3. Registros F3 das quinze primeiras tentativas. Fonte: dados fornecidos pela equipe; padronização decimal e organização por [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

Os demais registros de erros operacionais permanecem como **nenhum confirmado**. As situações abaixo estão pendentes de validação humana e não foram incluídas no resultado principal de M13:

- **S4/T1 (03:16–03:22):** abertura do exercício pela grade — verificar se houve desvio com necessidade real de correção.
- **S5/T3 (03:58–04:04):** troca de alternativa durante notificação do sistema — verificar se houve ação equivocada e correção.

## 7. Percepção dos voluntários (F4)

As perguntas finais foram:

- Qual tarefa foi mais difícil e por quê?
- Houve algum momento de incerteza sobre o próximo passo?
- Qual foi a facilidade de uso na primeira experiência, de **1 (muito difícil)** a **5 (muito fácil)**?

As respostas são evidências qualitativas e **não substituem** os registros observacionais de M12–M14.

| Participante | Maior dificuldade relatada | Não soube o próximo passo? | Facilidade (1–5) |
|---|---|---|---:|
| Pessoa 1 | Localizar a aula específica; percurso pouco intuitivo. | Não. | 3 |
| Pessoa 2 | Identificar exercícios pelos ícones e localizar as dicas. | Sim, ao procurar as dicas. | 4 |
| Pessoa 3 | Encontrar Matemática do 6º ano pela busca; termos esperados não retornaram o curso facilmente. | Não. | 1 |
| Pessoa 4 | Encontrar o curso entre resultados e páginas; dicas pouco visíveis. | Sim, ao procurar as dicas. | 2 |
| Pessoa 5 | Acessar as dicas sem indicação clara. | Sim, ao mudar de módulo. | 3 |

*Tabela 4. Síntese das respostas individuais ao F4. Fonte: respostas transcritas pela equipe. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

### 7.1. Síntese interpretativa

Os relatos apontam **dois padrões recorrentes**:

- Dificuldade para localizar o curso de Matemática do 6º ano por busca e navegação (Pessoas 1, 3 e 4).
- Dificuldade para reconhecer exercícios ou localizar dicas (Pessoas 2, 4 e 5).

Três pessoas relataram algum momento de incerteza sobre o próximo passo. As notas de facilidade foram **3, 4, 1, 2 e 3**, com **mediana 3/5** e média **2,6/5**. A Tabela 3 registra pedidos de ajuda em seis tentativas; 14 das quinze tarefas foram concluídas, e a T3 da Pessoa 2 terminou em desistência. As tentativas com pedido de ajuda não contam como autônomas para M12 e M14. Em especial, os relatos sobre dicas devem ser confrontados com o critério de T3 e a disponibilidade real do recurso.

## 8. Cálculo das métricas e julgamento GQM

Os cálculos seguem as definições de [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos), [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) e [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma), além das [faixas de pontuação](../fase-2/criterios-julgamento.md) estabelecidas antes da coleta. A unidade de análise é a **primeira tentativa elegível de cada par participante–tarefa**. Os quinze registros disponíveis atendem ao critério de elegibilidade profissional informado no F2. Os resultados devem ser interpretados considerando a retificação de experiência prévia e a disponibilidade dos passos opcionais de T3 descritas neste artefato.

### 8.1. [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos) — Taxa de conclusão autônoma

**Fórmula:** `M12 = 100 × S/N`, em que `S` representa as primeiras tentativas concluídas sem ajuda e `N` representa as primeiras tentativas elegíveis.

Para a T3, a conclusão exige abrir o exercício, acessar as dicas quando disponíveis e enviar uma resposta, independentemente de sua correção matemática. O envio de uma resposta incorreta não caracteriza falha na tarefa.

| Recorte | Conclusões autônomas (S) | Tentativas elegíveis (N) | M12 | Nota |
|---|---:|---:|---:|---|
| T1 | 4 | 5 | **80%** | **2 — Alvo** |
| T2 | 5 | 5 | **100%** | **3 — Excelente** |
| T3 | 0 | 5 | **0%** | **0 — Inaceitável** |
| **Total** | **9** | **15** | **60%** | **0 — Inaceitável** |

*Tabela 5. Resultado provisório de M12, calculado conforme os registros de autonomia e pedidos de ajuda do F3. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

**Análise:** A T2 apresentou o melhor resultado de autonomia, enquanto a T1 registrou uma tentativa com pedido de ajuda. Na T3, quatro participantes conseguiram acessar as dicas após enviar uma resposta incorreta, mas as cinco tentativas foram registradas no F3 como não autônomas. Além disso, a participante S2 não acessou as dicas, deixando de cumprir integralmente o objetivo previsto.

Portanto, o resultado de 0% em T3 reflete a classificação de autonomia registrada no F3, e não a ausência de acesso às dicas em todas as sessões. Antes do julgamento definitivo, os pedidos de ajuda devem ser confrontados com as gravações para distinguir intervenções das avaliadoras de exploração independente da interface.

### 8.2. [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) — Taxa de tentativas com erros operacionais

**Fórmula:** `M13 = 100 × E/N`, em que `E` representa as primeiras tentativas elegíveis com pelo menos um erro operacional e `N` representa o total de primeiras tentativas elegíveis.

Conforme o protocolo da Fase 3, **erro operacional** é uma *ação concluída que se afasta do caminho da tarefa e exige voltar ou desfazer*. Hesitações, exploração legítima, respostas matemáticas incorretas e falhas técnicas não são contabilizadas automaticamente.

A análise das sessões identificou erros operacionais em sete das quinze primeiras tentativas elegíveis.

| Recorte | Tentativas com erro (E) | Tentativas elegíveis (N) | M13 |
|---|---:|---:|---:|
| T1 | 1 | 5 | **20%** |
| T2 | 3 | 5 | **60%** |
| T3 | 3 | 5 | **60%** |
| **Total** | **7** | **15** | **46,67%** |

*Tabela 6. Resultado atualizado de M13 após revisão das gravações. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

**Análise:** A T1 apresentou erros em 20% das tentativas, concentrados na sessão S3, que registrou a abertura de um curso incorreto e de um exercício de outra unidade. Na T2, 60% das tentativas apresentaram erros relacionados à abertura de exercícios em vez das videoaulas solicitadas, exigindo correção pela navegação lateral.

A T3 também apresentou taxa de 60%, com erros de navegação nas sessões S1, S3 e S4, nas quais os participantes acessaram páginas diferentes do exercício solicitado e precisaram retornar ou consultar novamente o menu lateral. Na S3, também ocorreu o acionamento equivocado da opção **Pular**, contabilizado como uma ocorrência adicional, mas não como uma nova tentativa com erro.

**Julgamento:** A taxa geral de erros operacionais foi de **46,67%**, indicando dificuldades principalmente na identificação e no acesso aos conteúdos de videoaula e exercício. As tarefas T2 e T3 concentraram os maiores percentuais de erro, enquanto a T1 apresentou dificuldades adicionais de encontrabilidade que nem sempre configuraram erros operacionais. Os resultados reforçam a necessidade de melhorar a diferenciação visual entre os conteúdos e a orientação da navegação.

### 8.3. [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma) — Tempo mediano de conclusão autônoma

**Fórmula:** `M14 = mediana(t_fim − t_início)`, em segundos, considerando somente as primeiras tentativas concluídas autonomamente.

Os limites de referência da Fase 2 são **≤60 s (nota 3)**, **>60–120 s (nota 2)**, **>120–180 s (nota 1)** e **>180 s (nota 0)**.

| Tarefa | Tempos das conclusões autônomas (s) | Mediana (s) | Nota |
|---|---|---:|---|
| T1 | 51,79; 51,18; 77,64; 26,04 | **51,49** | **3 — Excelente** |
| T2 | 20,41; 26,97; 12,68; 24,91; 19,70 | **20,41** | **3 — Excelente** |
| T3 | — (nenhuma conclusão registrada como autônoma) | **—** | **Não calculável** |

*Tabela 7. Resultado provisório de M14 por tarefa, conforme a classificação de autonomia do F3. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

**Análise:** A T2 apresentou a menor mediana de tempo, indicando facilidade na identificação e utilização dos controles da videoaula. Na T1, embora a mediana das conclusões autônomas tenha sido de 51,49 segundos, as gravações evidenciam diferenças importantes entre os caminhos utilizados para encontrar o curso.

Os participantes que recorreram à busca enfrentaram dificuldades de localização, enquanto aqueles que utilizaram as opções de adicionar ou editar cursos encontraram caminhos mais diretos.

Na T3, não foi possível calcular M14 com os registros atuais, pois todas as tentativas foram classificadas como não autônomas no F3. Apesar disso, quatro participantes conseguiram acessar as dicas após uma resposta incorreta. Esses acessos não devem ser confundidos com conclusões autônomas sem que os pedidos de ajuda sejam verificados.

**Julgamento:** Os resultados indicam maior facilidade na utilização da videoaula do que na localização de cursos e na descoberta das dicas dos exercícios. A T3 apresentou dificuldades que exigiram orientação das avaliadoras, resultando em 0% de conclusão autônoma. Por esse motivo, não foi possível calcular a mediana de M14 para essa tarefa, mantendo-se inalterados os tempos originalmente coletados.

### 8.4. Síntese e relação entre os indicadores


| Métrica | Resultado registrado | Interpretação |
|---|---|---|
| [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos) — Autonomia | T1: 80%; T2: 100%; T3: 0%; total: **60%** | Os resultados confirmam maior autonomia nas tarefas T1 e T2. Na T3, todos os participantes necessitaram de orientação das avaliadoras, especialmente para localizar e acessar as dicas dos exercícios. |
| [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) — Erros operacionais | T1: 20%; T2: 60%; T3: 60%; total: **46,67%** | Sete das quinze tentativas apresentaram pelo menos um erro operacional. T2 e T3 concentraram as maiores taxas, evidenciando dificuldades na identificação e localização dos conteúdos. |
| [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma) — Tempo | T1: 51,49 s; T2: 20,41 s; T3: não calculável | As medianas consideram apenas as tentativas concluídas autonomamente. Na T3, não foi possível calcular a mediana devido à ausência de conclusões autônomas. |
| **F4 — Facilidade percebida** | Mediana: 3/5; média: 2,6/5 | As avaliações reforçam as dificuldades observadas na localização do curso e na identificação das dicas. |


*Tabela 8. Síntese cruzada dos registros F3, das observações das gravações e das respostas F4. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

A análise conjunta das métricas evidencia dificuldades distintas de apreensibilidade. A **T1** apresentou problemas de encontrabilidade do curso, especialmente pelo mecanismo de busca, enquanto as **T2 e T3** concentraram as maiores taxas de erros operacionais (**60%** cada). Na T2, os erros se relacionaram à abertura de exercícios em vez das videoaulas; na T3, às páginas diferentes do exercício solicitado e à correção do percurso. Também houve dificuldade para descobrir as dicas, que não necessariamente configurou erro operacional. Assim, conclusão, autonomia, tempo de execução e erros representam dimensões complementares da experiência inicial dos participantes.

### 8.5. Resposta à [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) e avaliação de [`H11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade)

**[`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade):** *Estudantes novos conseguem compreender como iniciar e concluir as tarefas essenciais após a instrução inicial, sem orientação adicional?*

**Resposta:** Os resultados indicam que a compreensão das tarefas varia conforme a funcionalidade utilizada. Os participantes demonstraram facilidade na utilização dos controles das videoaulas, mas enfrentaram dificuldades na localização de cursos, na identificação dos conteúdos e na descoberta das dicas dos exercícios.

Na **T1**, três participantes enfrentaram dificuldades com a busca, recorrendo a filtros, paginação ou estratégias alternativas. Ainda assim, a tarefa apresentou **80% de autonomia**.

Na **T2**, todos concluíram autonomamente (**100%**), embora três participantes tenham aberto exercícios em vez de videoaulas, resultando em **60% de erros operacionais**.

Na **T3**, quatro participantes acessaram as dicas após enviar respostas incorretas, enquanto um não conseguiu encontrá-las. As intervenções das avaliadoras foram classificadas como ajuda, resultando em **0% de autonomia**. Além disso, a tarefa apresentou **60% de erros operacionais**, principalmente relacionados à navegação.

Esses resultados evidenciam dificuldades de apreensibilidade, especialmente na encontrabilidade dos conteúdos e na visibilidade das funcionalidades de apoio.

**[`H11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade):** *No ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), pelo menos 90% das primeiras tentativas elegíveis de cada tarefa essencial e do conjunto avaliado serão concluídas pelos participantes adultos novos na plataforma, após a instrução inicial padronizada e sem ajuda adicional.*

**Julgamento de H11:** A hipótese **não foi sustentada**, pois M12 apresentou **80% em T1, 100% em T2 e 0% em T3**, com resultado geral de **60%**, abaixo do limite de 90% estabelecido.

**Relação com [`G3`](../fase-2/objetivos.md#g3) e [`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade):** As dificuldades observadas indicam oportunidades de melhoria no requisito de apreensibilidade, principalmente na busca por cursos, na diferenciação entre videoaulas e exercícios e na identificação das dicas. Os resultados contribuem para a avaliação de [`G3`](../fase-2/objetivos.md#g3) — Usabilidade, sem representar isoladamente o julgamento completo desse objetivo.

## 9. Julgamento final, oportunidades e ação de melhoria

A análise das sessões identificou erros operacionais em sete das quinze primeiras tentativas elegíveis, resultando em [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) geral de **46,67%**. As tarefas T2 e T3 apresentaram as maiores taxas de erro (60% cada), principalmente devido à abertura de conteúdos diferentes dos solicitados e à necessidade de corrigir a navegação. Na T1, a taxa foi de 20%, embora três participantes tenham enfrentado dificuldades adicionais com o mecanismo de busca. Também foram observados problemas na descoberta das dicas dos exercícios, que não configuraram erros operacionais. Esses resultados evidenciam fragilidades de apreensibilidade relacionadas à identificação dos tipos de conteúdo, à encontrabilidade e à orientação durante a navegação.

| Prioridade | Oportunidade identificada | Evidência | Ação técnica proposta | Verificação posterior |
|---|---|---|---|---|
| Alta | Encontrabilidade do curso de Matemática do 6º ano | Pessoas 1, 3 e 4; T1 de S3 = 154,36 s | **Protótipo de alta fidelidade** de busca e seleção de curso, com correspondência por série/ano, filtros visíveis e resultados identificados por título. | Novo teste T1 com voluntários elegíveis; comparar M12, M13, M14 e percepção. |
| Alta | Dicas e exercícios pouco identificáveis | Pessoas 2, 4 e 5 | No mesmo protótipo, adicionar rótulos textuais aos exercícios e controle de dicas claramente sinalizado, com indicação de quando fica disponível. | Repetir T3 e observar se a dica é encontrada sem intervenção. |
| Média | Orientação inicial para mudança de módulo | Pessoa 5 | Adicionar sinalização de unidade/módulo atual e próximo passo no protótipo. | Observar navegação sem instruções adicionais. |

*Tabela 9. Oportunidades de melhoria e ações técnicas fundamentadas nas evidências. Fonte: F3 e F4. Elaboração de [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino).*

## Referências

<a id="s1"></a>

> [S1] Escopo da avaliação — Fase 1. Fluxos, ambientes, profundidade e limites de validade. Disponível em: [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md).

<a id="s2"></a>

> [S2] Requisitos de avaliação — Fase 1. Requisitos [`R1`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade)–[`R5`](../fase-1/requisitos-de-avaliacao.md#rastreabilidade). Disponível em: [Requisitos de avaliação](../fase-1/requisitos-de-avaliacao.md).

<a id="s3"></a>

> [S3] Objetivos GQM — Fase 2. Disponível em: [Objetivos da avaliação](../fase-2/objetivos.md).

<a id="s4"></a>

> [S4] Questões e hipóteses — Fase 2. Inclui [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) e [`H11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade). Disponível em: [Questões e hipóteses](../fase-2/questoes-hipoteses.md).

<a id="s5"></a>

> [S5] Definição de métricas M12–M14 — Fase 2. Disponível em: [Métricas da avaliação](../fase-2/metricas.md).

<a id="s6"></a>

> [S6] Níveis de pontuação e critérios de julgamento — Fase 2. Disponível em: [Critérios de julgamento](../fase-2/criterios-julgamento.md).

<a id="s7"></a>

> [S7] Procedimentos de avaliação de acessibilidade e apreensibilidade (M8–M14) — Fase 3. Disponível em: [Procedimentos de acessibilidade e apreensibilidade](../fase-3/procedimentos-acessibilidade-apreensibilidade.md).

<a id="s8"></a>

> [S8] Projeto final da disciplina: **Avaliação da Qualidade de Produto de Software**, versão 1.0, 05/10/2026, especialmente as seções 3.2, 6.1.4 e 6.1.5.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|---|---|---|---|
| 1.0 | 22/11/2026 | Consolidação do registro de apreensibilidade, padronização da autoria das tabelas e inclusão do histórico de versões. | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 22/11/2026 | Reorganização das referências no padrão numerado com identificadores e âncoras adotado nos demais artefatos do projeto. | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.2 | 22/11/2026 | Inclusão de links destacados de rastreabilidade para métricas, questão, hipótese, ambiente e fluxos nas respectivas definições. | [Camila Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |

<!-- Gráficos interativos incorporados neste único arquivo Markdown.
     Requer acesso à CDN do Chart.js e preservação de HTML/scripts pelo MkDocs. -->
<style>
.ap-chart { position:relative; width:100%; max-width:700px; height:300px; margin:1rem auto; }
.ap-chart canvas { width:100% !important; height:100% !important; }
</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>
<script>
(function () {
  function desenharGraficos() {
    if (typeof Chart === 'undefined') return;
    const graficos = [
      ['f2-maioridade', 'pie', ['Sim', 'Não'], [5,0]],
      ['f2-idade', 'pie', ['18 a 24 anos'], [5]],
      ['f2-khan', 'pie', ['Não', 'Sim'], [5,0]],
      ['f2-computador', 'bar', ['1', '2', '3', '4', '5'], [0,0,1,0,4]],
      ['f2-profissao', 'pie', ['Não', 'Sim'], [5,0]],
      ['f2-plataformas', 'bar', ['YouTube (para estudar)', 'Duolingo', 'Google Classroom', 'Udemy ou Coursera'], [5,4,4,3]],
      ['f2-consentimento', 'pie', ['Sim, concordo', 'Não concordo'], [5,0]],
      ['f2-gravacao', 'pie', ['Sim, autorizo', 'Não autorizo'], [5,0]],
      ['f3-tempos', 'bar', ['T1', 'T2', 'T3'], [51.49,20.41,null]]
    ];
    graficos.forEach(function (g) {
      const el = document.getElementById(g[0]);
      if (!el) return;
      const anterior = Chart.getChart(el);
      if (anterior) anterior.destroy();
      const tempos = g[0] === 'f3-tempos';
      const plataformas = g[0] === 'f2-plataformas';
      const profissao = g[0] === 'f2-profissao';
      const total = g[3].reduce((a,b) => a+b, 0);
      new Chart(el, {
        type: g[1],
        data: {labels:g[2], datasets:[{
          label: tempos ? 'Mediana (segundos)' : 'Respostas',
          data:g[3],
          backgroundColor: profissao
            ? ['#dc3912','#3366cc']
            : (g[0] === 'f2-maioridade'
            ? ['#3366cc','#dc3912']
            : (g[0] === 'f2-khan'
              ? ['#dc3912','#3366cc']
              : (g[1] === 'bar' ? '#3b82f6' : ['#3366cc','#dc3912','#ff9900','#109618','#990099']))),
          borderRadius: plataformas ? 5 : 0,
          borderWidth: g[1] === 'pie' ? 0 : 1
        }]},
        options: {
          responsive:true, maintainAspectRatio:false,
          plugins:{
          legend:{display:g[1] !== 'bar',position:profissao?'right':'bottom'},
            tooltip:{callbacks:{label:function(ctx){
              const n=plataformas ? ctx.parsed.x : (ctx.parsed.y ?? ctx.parsed);
              if (tempos) return ctx.label + ': ' + Number(n).toLocaleString('pt-BR',{maximumFractionDigits:2}) + ' s';
              if (plataformas) return n + ' participante(s) (' + (100*n/5).toLocaleString('pt-BR',{maximumFractionDigits:0}) + '%)';
              if (profissao) return ctx.label + ': ' + n + ' participante(s) (' + (100*n/5).toLocaleString('pt-BR',{maximumFractionDigits:0}) + '%)';
              return ctx.label + ': ' + n + ' resposta(s) (' + (100*n/total).toLocaleString('pt-BR',{maximumFractionDigits:1}) + '%)';
            }}}
          },
          indexAxis: plataformas ? 'y' : 'x',
          scales: g[1] === 'bar' ? (plataformas
            ? {x:{beginAtZero:true,max:5,ticks:{stepSize:1},title:{display:true,text:'Número de participantes'}},y:{grid:{display:false}}}
            : {y:{beginAtZero:true,ticks:{stepSize:tempos?undefined:1}}}) : {}
        }
      });
    });
  }
  if (typeof document$ !== 'undefined') document$.subscribe(desenharGraficos);
  else if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', desenharGraficos);
  else desenharGraficos();
})();
</script>
