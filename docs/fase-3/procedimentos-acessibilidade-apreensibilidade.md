# Procedimentos de avaliação de acessibilidade e apreensibilidade

**Versão 1.0**

Este documento especifica como serão coletadas as métricas [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) a [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma), que respondem às questões [`Q7`](../fase-2/questoes-hipoteses.md#51-q7-navegacao-por-teclado) a [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) do objetivo [`G3`](../fase-2/objetivos.md#g3), adaptadas da ISO/IEC 25023:2016 [S2](#s2). Os procedimentos cobrem três frentes: inspeções automatizadas, testes manuais com tecnologias assistivas e testes com voluntários. A aplicação oficial ocorre na Fase 4; aqui ficam definidos os roteiros, os critérios de classificação e os instrumentos de coleta, de forma que qualquer integrante consiga repetir a avaliação nas mesmas condições.

O objeto continua sendo a **versão web da Khan Academy em computadores**, nos fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) a [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) e nos ambientes [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) definidos no [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md#ambientes).

## 1. Visão geral

A Tabela 1 resume cada procedimento, as métricas que alimenta e as condições em que é executado.

| Procedimento | Métricas | Questões e hipóteses | Ambientes | Evidência principal |
|---|---|---|---|---|
| Inspeção automatizada | Apoio a [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) a [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) | Q7 a Q10 / H7 a H10 | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Relatórios do Lighthouse e do axe-core |
| Navegação por teclado | [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) | Q7 / H7 | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) | Formulário F5 e gravação de tela |
| Leitor de tela | [`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela) | Q8 / H8 | NVDA em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), VoiceOver em [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes), Orca em [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) | Formulário F5 e gravação com áudio |
| Ampliação de 200% | [`M10`](../fase-2/metricas.md#110-m10-preservacao-com-ampliacao) | Q9 / H9 | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), 1366 × 768 | Formulário F5 e capturas de tela |
| Contraste e alto contraste | [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) | Q10 / H10 | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), 1366 × 768 | Formulários F5 e F6 |
| Testes com voluntários | [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos), [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais), [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma) | Q11 / H11 | [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | Formulários F3 e F4 |

*Tabela 1. Procedimentos de acessibilidade e apreensibilidade. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

## 2. Preparação comum

Antes de qualquer sessão, o avaliador prepara o ambiente da mesma forma, para que diferenças nos resultados venham da plataforma e não da configuração do computador.

1. Usar a conta de teste controlada pela equipe, a mesma em todas as sessões, conforme o [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md#fluxos). A autenticação é feita antes do início da tarefa e não entra na medição.
2. Abrir o navegador em um perfil sem extensões, com exceção das ferramentas de inspeção da seção 3, e limpar cache e cookies de sessões anteriores, mantendo apenas o login da conta de teste.
3. Ajustar a resolução do sistema para 1366 × 768 em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) e registrar a resolução usada em [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes).
4. Manter o idioma da plataforma em português do Brasil e o zoom do navegador em 100%, exceto no teste de ampliação.
5. Desativar notificações do sistema e fechar programas que não fazem parte do ensaio.
6. Preencher o Formulário F7 com sistema operacional, navegador, tecnologia assistiva e respectivas versões, data e avaliador.

Cada sessão recebe um identificador no formato `AC-AAAAMMDD-NN` (acessibilidade) ou `AP-AAAAMMDD-NN` (apreensibilidade), usado no nome de todas as evidências daquela sessão.

## 3. Inspeções automatizadas

### 3.1 Ferramentas e justificativa

As inspeções automatizadas localizam rapidamente problemas técnicos verificáveis por código, como imagens sem texto alternativo, controles sem nome acessível e contraste insuficiente. Elas orientam os testes manuais, indicando onde procurar barreiras, mas não decidem se uma tarefa pode ser concluída com tecnologia assistiva. A Tabela 2 justifica cada ferramenta.

| Ferramenta | Forma de uso | Por que foi escolhida | Tipo de auditoria |
|---|---|---|---|
| Lighthouse [S3](#s3) | Painel do Chrome DevTools, categoria Acessibilidade, nos modos navegação e *snapshot* | Já vem no Chrome do ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), não exige instalação e gera relatório exportável com pontuação de 0 a 100 | Visão geral da página: nomes acessíveis, atributos ARIA, estrutura de títulos, idioma, contraste e ordem de navegação sinalizada para revisão manual |
| axe-core [S4](#s4) | Extensão axe DevTools no Chrome, com as regras marcadas como WCAG 2.0 e 2.1 níveis A e AA | Motor de regras aberto, usado como referência no mercado, que separa violações de itens que precisam de revisão humana | Lista detalhada por elemento, com seletor, regra violada, critério WCAG relacionado e impacto |

*Tabela 2. Ferramentas de inspeção automatizada e finalidade. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

As duas ferramentas são complementares. O Lighthouse usa um subconjunto das regras do axe-core e resume o resultado em uma nota, útil para comparar páginas. O axe-core lista cada ocorrência com o elemento afetado, o que permite reproduzir e registrar a barreira.

### 3.2 Páginas e estados inspecionados

As páginas da Tabela 3 cobrem as etapas dos fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) a [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos). Estados que só existem depois de uma interação, como o retorno de uma resposta, são inspecionados no modo *snapshot*, com a página já no estado desejado.

| Código | Página ou estado | Fluxo | Modo do Lighthouse |
|---|---|---|---|
| P1 | Página inicial da conta de teste após o login | [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) | Navegação |
| P2 | Página do curso selecionado | [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) | Navegação |
| P3 | Página da unidade com a lista de aulas | [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) | Navegação |
| P4 | Página da videoaula com o reprodutor carregado | [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) | Navegação |
| P5 | Página do exercício antes da resposta | [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) | Navegação |
| P6 | Exercício com dica aberta e retorno da resposta exibido | [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) | *Snapshot* |

*Tabela 3. Páginas e estados submetidos à inspeção automatizada. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

O curso, a unidade, a videoaula e o exercício são os mesmos das tarefas da seção 4.1, para que os achados automatizados possam ser confrontados com os testes manuais.

### 3.3 Configuração e execução

1. Preparar o ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) conforme a seção 2.
2. Abrir a página P1 e aguardar o carregamento completo.
3. No Lighthouse, selecionar apenas a categoria Acessibilidade, dispositivo **Computador** e o modo indicado na Tabela 3; executar a auditoria e exportar o relatório em HTML e JSON.
4. Na mesma página, executar a varredura completa do axe DevTools e exportar o resultado em JSON ou CSV.
5. Fazer uma captura de tela inteira da página no estado auditado.
6. Repetir os passos 2 a 5 para P2 a P6. Para P6, abrir a dica e enviar uma resposta antes de executar o Lighthouse em modo *snapshot* e a varredura do axe.
7. Executar a sequência duas vezes no mesmo dia. Se a pontuação do Lighthouse variar mais de 5 pontos entre as execuções de uma página, executar uma terceira vez e registrar as três.

### 3.4 Evidências

Os arquivos seguem o padrão `AC-AAAAMMDD-NN_P1_lighthouse.html`, `AC-AAAAMMDD-NN_P1_axe.json` e `AC-AAAAMMDD-NN_P1_captura.png`. Cada violação encontrada é transcrita no Formulário F1, com página, regra, critério WCAG, impacto, seletor do elemento e se o elemento participa de alguma etapa das tarefas. Itens que as ferramentas marcam como "precisa de revisão" entram na lista de pontos a confirmar nos testes manuais.

### 3.5 Limitações

- Apenas parte dos critérios da WCAG 2.1 [S1](#s1) pode ser verificada por código. Ordem lógica de leitura, clareza dos anúncios do leitor de tela, armadilhas de foco em componentes dinâmicos e utilidade do texto alternativo exigem avaliação humana.
- A pontuação do Lighthouse é ponderada pelas regras aplicáveis à página e não representa grau de acessibilidade. Ela não entra no cálculo de nenhuma métrica.
- Conteúdo carregado em `iframe` de terceiros, como reprodutores de vídeo incorporados, pode não ser inspecionado por completo. Quando isso ocorrer, o fato é registrado no Formulário F1.
- Ausência de violações automáticas não permite concluir que a página é acessível. O julgamento de [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) a [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) depende dos testes manuais da seção 4.

## 4. Testes manuais de acessibilidade

### 4.1 Tarefas de referência

Os testes manuais usam três tarefas fixas, uma por fluxo, descritas na Tabela 4. O mesmo conteúdo é usado em todos os ambientes e configurações.

| Tarefa | Fluxo | Etapas | Estado de conclusão |
|---|---|---|---|
| T1 | [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) | A partir da página inicial, localizar o curso de Matemática do 6º ano, abrir o curso e abrir a primeira unidade | Lista de aulas da primeira unidade exibida |
| T2 | [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) | Na primeira unidade, abrir a primeira videoaula, iniciar a reprodução, pausar e ativar a legenda ou a transcrição, quando disponível | Vídeo pausado e legenda ou transcrição ativa |
| T3 | [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) | Abrir o primeiro exercício da unidade, solicitar uma dica, informar uma resposta e enviá-la | Retorno da plataforma sobre a resposta exibido |

*Tabela 4. Tarefas de referência dos testes manuais. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

A verificação piloto da seção 7 confirma que o caminho de cada tarefa está disponível na conta de teste. Se a plataforma alterar o conteúdo entre o piloto e a coleta, a tarefa é substituída por uma equivalente no mesmo fluxo e a troca é registrada no Formulário F7.

### 4.2 Classificação do resultado

Cada combinação de tarefa e condição recebe uma das classificações da Tabela 5.

| Classificação | Quando aplicar | Efeito no cálculo |
|---|---|---|
| Sucesso | A tarefa chega ao estado de conclusão usando somente o recurso avaliado, sem barreira em etapa essencial | Conta em `A` e em `N` |
| Sucesso com barreira não essencial | A tarefa é concluída, mas há problema em elemento que não impede nenhuma etapa, como foco pouco visível em um link secundário | Conta em `A` e em `N`; a barreira é registrada no Formulário F5 |
| Falha | A tarefa não é concluída, ou só é concluída com recurso fora do avaliado (mouse no teste de teclado, consulta visual no teste de leitor de tela, retorno ao zoom de 100%, desativação do alto contraste) | Conta apenas em `N` |
| Impedimento | Uma barreira da plataforma bloqueia uma etapa essencial, como armadilha de foco ou controle sem acesso pelo recurso avaliado | Conta apenas em `N` e aciona a regra de bloqueio dos [critérios de julgamento](../fase-2/criterios-julgamento.md#5-regra-de-julgamento) |
| Execução inválida | Falha que não tem relação com a acessibilidade, como queda da internet, erro do servidor ou erro de configuração do avaliador | Não entra no cálculo; a combinação é repetida uma vez e, se falhar de novo, é registrada como inconclusiva |

*Tabela 5. Classificação do resultado de cada combinação. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

Uma etapa é essencial quando, sem ela, a tarefa não atinge o estado de conclusão da Tabela 4.

### 4.3 Navegação por teclado (M8)

**Condição:** T1 a T3 nos ambientes [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes), totalizando 9 combinações. No Safari de [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes), ativar antes a opção que permite navegar por todos os itens da página com a tecla Tab.

1. Posicionar o cursor fora da área da página e não tocar no mouse ou no *trackpad* até o fim da tarefa.
2. Usar apenas Tab e Shift+Tab para mover o foco, Enter e Espaço para acionar, setas dentro de menus e controles compostos e Esc para fechar janelas e menus.
3. Em cada etapa, observar e registrar no Formulário F5:
    - se o foco está sempre visível (WCAG 2.4.7);
    - se a ordem do foco acompanha a ordem visual e lógica (WCAG 2.4.3);
    - se todos os controles necessários recebem foco e podem ser acionados (WCAG 2.1.1);
    - se o foco fica preso em algum componente sem saída pelo teclado (WCAG 2.1.2);
    - quantas teclas foram necessárias até alcançar o controle da etapa, como apoio à descrição de barreiras.
4. Gravar a tela durante toda a tarefa.
5. Classificar a combinação conforme a Tabela 5.

**Cálculo:** `M8 = 100 × A/N`, em que `A` é o número de combinações com Sucesso ou Sucesso com barreira não essencial e `N` é o número de combinações válidas.

### 4.4 Leitor de tela (M9)

**Condição:** T1 a T3 em três combinações de leitor, navegador e sistema, totalizando 9 combinações, conforme a Tabela 6.

| Ambiente | Leitor de tela | Navegador | Comandos de referência |
|---|---|---|---|
| [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) | NVDA [S6](#s6) | Google Chrome | Modo de navegação, H para títulos, K para links, B para botões, F para campos, Insert+F7 para lista de elementos |
| [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) | VoiceOver [S7](#s7) | Apple Safari | VO (Control+Option) com setas para percorrer, VO+U para o rotor, VO+Espaço para acionar |
| [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) | Orca [S8](#s8) | Mozilla Firefox | Navegação estrutural com H, K, B e F, Insert+Espaço para alternar modo de foco e de navegação |

*Tabela 6. Combinações de leitor de tela e comandos de referência. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

1. Ativar o leitor de tela com voz em português e velocidade padrão, e registrar a versão no Formulário F7.
2. Antes de iniciar, desligar o monitor ou cobrir a tela, para que a tarefa seja conduzida apenas pelo que é anunciado. Um segundo integrante acompanha a tela para registrar o que acontece, sem orientar o avaliador.
3. Executar a tarefa usando apenas teclado e os comandos do leitor.
4. Em cada etapa, registrar no Formulário F5:
    - o que o leitor anunciou ao chegar no controle necessário;
    - se o controle tem nome e função compreensíveis, como "botão Enviar" em vez de "botão" sem nome;
    - se mudanças de estado são anunciadas, como reprodução iniciada, dica aberta e resposta correta ou incorreta;
    - se foi preciso consultar a tela para continuar.
5. Gravar a tela com o áudio do sistema.
6. Classificar a combinação conforme a Tabela 5. Consultar a tela para continuar é Falha.

**Cálculo:** `M9 = 100 × A/N`, com `A` e `N` definidos como em M8.

### 4.5 Ampliação de 200% (M10)

**Condição:** T1 a T3 em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), na resolução de 1366 × 768, com zoom do navegador em 200%, totalizando 3 combinações. O critério de referência é o 1.4.4 da WCAG 2.1 [S1](#s1).

1. Com a página inicial aberta, ajustar o zoom do Chrome para 200% pelo atalho Ctrl e + até o indicador mostrar 200%.
2. Executar a tarefa com mouse e teclado, sem reduzir o zoom em nenhum momento.
3. Em cada etapa, registrar no Formulário F5:
    - texto cortado, sobreposto ou escondido sem forma de acesso;
    - controles necessários que deixam de aparecer ou ficam inacessíveis;
    - necessidade de rolagem horizontal para ler uma linha de texto;
    - menus que só abrem com o zoom reduzido.
4. Fazer uma captura de tela de cada etapa.
5. Classificar a combinação conforme a Tabela 5. Reduzir o zoom para concluir é Falha.

**Cálculo:** `M10 = 100 × A/N`. Com apenas 3 combinações, uma única falha leva o resultado a 66,7%, por isso cada barreira é descrita individualmente, como pedem os [critérios técnicos](../fase-2/criterios-julgamento.md#4-criterios-tecnicos-de-acessibilidade).

### 4.6 Contraste e alto contraste (M11)

A [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) tem duas partes, registradas separadamente, como define a [hipótese H10](../fase-2/questoes-hipoteses.md#54-q10-contraste-e-alto-contraste).

**Parte 1: medição de contraste.** Em P1 a P6, o avaliador lista no Formulário F6 os textos e controles necessários às tarefas T1 a T3, como títulos, links do caminho, botões do reprodutor, enunciado, campo de resposta, botão de dica, botão de envio e mensagem de retorno.

1. Medir a razão de contraste de cada elemento com o Colour Contrast Analyser [S9](#s9), usando o conta-gotas sobre a cor do texto e a cor de fundo.
2. Confirmar com o resultado da regra de contraste do axe-core, quando houver.
3. Classificar o tamanho do texto: grande é a partir de 18 pt (24 px) ou 14 pt (cerca de 18,7 px) em negrito.
4. Registrar se o elemento atende a 4,5:1 para texto comum e 3:1 para texto grande (WCAG 1.4.3, AA) e a 7:1 e 4,5:1 (WCAG 1.4.6, AAA).
5. Marcar se o elemento é essencial para a tarefa.

**Cálculo da parte 1:** `M11 = 100 × E_c/E_a`, em que `E_c` são os elementos conformes ao critério 1.4.3 e `E_a` são os elementos avaliados. A nota segue os [critérios técnicos](../fase-2/criterios-julgamento.md#4-criterios-tecnicos-de-acessibilidade): falha em elemento essencial leva a nota 0, mesmo com percentual alto.

**Parte 2: alto contraste do Windows.** T1 a T3 em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), totalizando 3 combinações.

1. Ativar o tema de contraste **Céu noturno** em Configurações, Acessibilidade, Temas de contraste [S10](#s10), e registrar o tema no Formulário F7.
2. Executar a tarefa com mouse e teclado, sem desativar o tema.
3. Registrar no Formulário F5 textos, ícones, bordas de campos e indicadores de foco que desaparecem ou ficam indistinguíveis.
4. Fazer uma captura de tela de cada etapa e classificar a combinação conforme a Tabela 5.

**Registro da parte 2:** percentual de tarefas concluídas com alto contraste, relatado ao lado de M11, sem ser somado a ele.

### 4.7 Registro de barreiras

Toda barreira encontrada, com ou sem impacto na conclusão, é registrada no Formulário F5 com os campos abaixo, de modo que outra pessoa consiga reproduzi-la.

- Identificador da barreira (`B-NN`) e da sessão.
- Ambiente, navegador, tecnologia assistiva e versões.
- Tarefa e etapa.
- Passos exatos para reproduzir, a partir da página inicial.
- Comportamento esperado e comportamento observado.
- Critério WCAG relacionado, quando houver.
- Gravidade: **bloqueia** (impede etapa essencial), **dificulta** (exige contorno) ou **incomoda** (não afeta a conclusão).
- Evidência: nome do arquivo de captura ou trecho da gravação com minuto e segundo.

## 5. Testes com voluntários

### 5.1 Seleção dos participantes

A amostra prevista no [Escopo da avaliação](../fase-1/escopo-da-avaliacao.md#ambientes) é de três a cinco adultos sem experiência anterior com a Khan Academy. A Tabela 7 detalha os critérios.

| Tipo | Critério |
|---|---|
| Inclusão | Ter 18 anos ou mais |
| Inclusão | Declarar nunca ter usado a Khan Academy em nenhuma plataforma |
| Inclusão | Usar computador com mouse e teclado no dia a dia |
| Inclusão | Ler em português sem dificuldade |
| Exclusão | Fazer parte da equipe ou ter acompanhado a preparação da avaliação |
| Exclusão | Trabalhar com teste, design ou desenvolvimento de interfaces web |
| Exclusão | Ter participado da verificação piloto |

*Tabela 7. Critérios de seleção dos voluntários. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

O Formulário F2 aplica esses critérios antes do agendamento. Também registra faixa etária, frequência de uso de computador e plataformas de estudo on-line já usadas, apenas para descrever a amostra.

### 5.2 Recrutamento e agenda

1. Convidar colegas de outros cursos da universidade e pessoas próximas da equipe que atendam à Tabela 7, por mensagem com descrição curta da atividade, duração de cerca de 30 minutos e o caráter voluntário.
2. Enviar o Formulário F2 a quem aceitar e confirmar a elegibilidade.
3. Agendar as sessões em horários diferentes, com pelo menos dois participantes reserva, para manter a amostra mínima de três em caso de desistência.
4. Realizar todas as sessões no mesmo computador do ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), em local silencioso, com um avaliador condutor e um observador.

### 5.3 Consentimento e anonimização

O tratamento dos dados segue a Lei Geral de Proteção de Dados Pessoais [S5](#s5).

- No início da sessão, o condutor lê o Termo de Consentimento (Formulário F2, parte 2), que informa o objetivo, o que será registrado, que a avaliação é da plataforma e não da pessoa, que é possível parar a qualquer momento sem justificativa e como os dados serão usados. A sessão só começa após o aceite.
- Cada participante recebe um código, de P1 a P5. Nome e contato ficam apenas no termo de consentimento, guardado fora do repositório público.
- A gravação, quando autorizada, captura somente a tela e o áudio do computador, sem câmera. Se o participante não autorizar a gravação, a coleta é feita apenas pelo Formulário F3.
- Publicam-se somente dados agregados e trechos anonimizados de comentários. Arquivos brutos são apagados ao fim da disciplina.

### 5.4 Tarefas padronizadas

As tarefas dos voluntários reproduzem T1 a T3 da seção 4.1, mas são lidas em linguagem do dia a dia, sem citar nomes de botões ou menus. A Tabela 8 traz o enunciado lido ao participante.

| Tarefa | Enunciado lido ao participante | Estado de conclusão | Limite de tempo |
|---|---|---|---|
| T1 | "Você quer estudar Matemática do 6º ano. Encontre esse curso e abra a primeira parte dele." | Lista de aulas da primeira unidade exibida | 5 minutos |
| T2 | "Agora assista ao primeiro vídeo dessa parte. Comece o vídeo, pause e ligue as legendas." | Vídeo pausado e legenda ou transcrição ativa | 5 minutos |
| T3 | "Faça o primeiro exercício dessa parte. Peça uma ajuda antes de responder e envie uma resposta." | Retorno da plataforma sobre a resposta exibido | 5 minutos |

*Tabela 8. Tarefas padronizadas dos testes com voluntários. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

A resposta do exercício não é avaliada: acertar ou errar a questão não altera a conclusão da tarefa. O limite de 5 minutos é a janela de observação; ele é maior que a faixa de 180 segundos da [`M14`](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) para que o tempo das tentativas lentas também seja registrado.

### 5.5 Instrução inicial padronizada

O condutor lê o texto abaixo, sem acrescentar explicações, antes da primeira tarefa.

> "Obrigado por participar. Hoje vamos observar como as pessoas usam um site de estudos pela primeira vez. Quem está sendo avaliado é o site, não você, então não existe resposta certa ou errada. Vou ler três tarefas, uma de cada vez. Quando terminar uma tarefa, ou se achar que não consegue continuar, é só avisar. Durante as tarefas, não vou poder ajudar; se você pedir ajuda, vou anotar e, se precisar, explico como seguir. Pode falar em voz alta o que está pensando, se quiser. Você já está com a conta aberta no site. Podemos começar?"

### 5.6 Roteiro do avaliador

1. Preparar o computador conforme a seção 2, com a conta de teste já autenticada e a página inicial aberta.
2. Iniciar a gravação de tela, se autorizada, e anotar o horário no Formulário F3.
3. Ler o termo de consentimento e registrar o aceite.
4. Ler a instrução inicial da seção 5.5.
5. Para cada tarefa, na ordem T1, T2 e T3:
    1. ler o enunciado da Tabela 8 e entregar o mesmo texto impresso;
    2. iniciar o cronômetro quando o participante disser que vai começar ou tocar no mouse, o que acontecer primeiro;
    3. observar sem comentar e registrar erros e pedidos de ajuda no Formulário F3;
    4. parar o cronômetro quando a tela atingir o estado de conclusão, quando o participante desistir ou ao fim dos 5 minutos;
    5. se a tarefa não for concluída, levar a página ao ponto de início da próxima tarefa antes de seguir.
6. Ao final, aplicar as perguntas de percepção do Formulário F4.
7. Agradecer, encerrar a gravação e conferir se todos os campos do Formulário F3 foram preenchidos.

O observador registra os horários e as ações em paralelo, para que o condutor possa se concentrar no participante. Divergências entre os dois registros são resolvidas pela gravação; sem gravação, vale o registro do observador.

### 5.7 Conclusão autônoma, erro operacional e pedido de ajuda

A Tabela 9 define os termos usados nos registros e nos cálculos.

| Termo | Definição | Exemplos |
|---|---|---|
| Conclusão autônoma | O participante atinge o estado de conclusão dentro de 5 minutos, na primeira tentativa, sem ter recebido ajuda | Abre a lista de aulas da unidade sozinho em 2 minutos |
| Pedido de ajuda | O participante pergunta como fazer ou o condutor precisa intervir para a tarefa continuar | "Onde fica o curso?"; condutor aponta o menu |
| Resposta neutra | Resposta do condutor que não indica caminho; não conta como ajuda | "Faça como achar melhor"; "Pode continuar" |
| Erro operacional | Ação concluída que se afasta do caminho da tarefa e exige voltar ou desfazer | Abrir um curso de outra série; acionar o botão errado no reprodutor; enviar o exercício sem resposta por engano |
| Exploração | Movimentos sem compromisso para conhecer a página; não conta como erro | Rolar a página; passar o mouse sobre menus; abrir e fechar um menu sem escolher item |
| Falha técnica | Problema da plataforma ou do ambiente, alheio ao participante | Página que não carrega; vídeo que não inicia por erro do servidor |
| Desistência | O participante declara que não consegue continuar | "Não sei mais o que fazer" |

*Tabela 9. Definições usadas nos testes com voluntários. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

Uma tentativa é **elegível** quando não houve falha técnica que impedisse a tarefa. Tentativas com falha técnica impeditiva são registradas, mas saem de `N`. Errar a resposta do exercício não é erro operacional, porque mede conhecimento do conteúdo e não uso da interface.

### 5.8 Cronometragem e registro

- O tempo é medido em segundos, com cronômetro digital, e conferido pela gravação quando houver.
- O início e o fim seguem o passo 5 do roteiro da seção 5.6.
- Cada erro operacional é anotado com o horário aproximado e a ação realizada.
- Cada pedido de ajuda é anotado com o horário, a pergunta e a resposta dada.
- Falhas técnicas são anotadas com a mensagem exibida, quando houver.

### 5.9 Cálculo das métricas

Os dados do Formulário F3 alimentam as fórmulas da Fase 2.

- **M12:** `100 × S/N`, em que `S` são as primeiras tentativas com conclusão autônoma e `N` as primeiras tentativas elegíveis. Calcular por tarefa e no total.
- **M13:** `100 × E/N`, em que `E` são as primeiras tentativas elegíveis com pelo menos um erro operacional.
- **M14:** mediana, em segundos, de `t_fim − t_início` apenas das tentativas com conclusão autônoma, por tarefa. Desistências, pedidos de ajuda e tempos esgotados são relatados à parte.

Com três a cinco participantes e três tarefas, `N` fica entre 9 e 15 tentativas no total e entre 3 e 5 por tarefa.

### 5.10 Limitações e resultados inconclusivos

- A amostra é exploratória e não representa estudantes de escolas públicas nem menores de idade, como já registrado nos [limites de validade](../fase-1/escopo-da-avaliacao.md#limites-de-validade).
- Com poucos participantes, uma única tentativa muda o percentual em 20 a 33 pontos por tarefa. Os resultados são apresentados com as contagens absolutas.
- O resultado de [`H11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) é **inconclusivo** quando houver menos de três participantes válidos ou quando mais da metade das tentativas de uma tarefa for inelegível por falha técnica. Nesse caso, os registros são apresentados como evidência exploratória.
- A presença do condutor e do observador pode alterar o comportamento do participante. A instrução padronizada e as respostas neutras reduzem esse efeito, mas não o eliminam.

## 6. Rastreabilidade com a Fase 2

A Tabela 10 liga cada procedimento às questões, hipóteses, métricas e critérios de julgamento da Fase 2.

| Questão | Hipótese | Métrica | Procedimento | Dado coletado | Fórmula | Critério de julgamento |
|---|---|---|---|---|---|---|
| [`Q7`](../fase-2/questoes-hipoteses.md#51-q7-navegacao-por-teclado) | H7 | [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado) | Seção 4.3 | Classificação das 9 combinações no F5 | `100 × A/N` | [Faixas percentuais](../fase-2/criterios-julgamento.md#2-metricas-percentuais) e regra de bloqueio |
| [`Q8`](../fase-2/questoes-hipoteses.md#52-q8-utilizacao-com-leitor-de-tela) | H8 | [`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela) | Seção 4.4 | Anúncios e classificação das 9 combinações no F5 | `100 × A/N` | [Faixas percentuais](../fase-2/criterios-julgamento.md#2-metricas-percentuais) e regra de bloqueio |
| [`Q9`](../fase-2/questoes-hipoteses.md#53-q9-utilizacao-com-ampliacao) | H9 | [`M10`](../fase-2/metricas.md#110-m10-preservacao-com-ampliacao) | Seção 4.5 | Classificação das 3 combinações e capturas no F5 | `100 × A/N` | [Faixas percentuais](../fase-2/criterios-julgamento.md#2-metricas-percentuais) e [WCAG 1.4.4](../fase-2/criterios-julgamento.md#4-criterios-tecnicos-de-acessibilidade) |
| [`Q10`](../fase-2/questoes-hipoteses.md#54-q10-contraste-e-alto-contraste) | H10 | [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) | Seção 4.6 | Razões de contraste no F6 e tarefas em alto contraste no F5 | `100 × E_c/E_a` e conclusão em alto contraste à parte | [WCAG 1.4.3 e 1.4.6](../fase-2/criterios-julgamento.md#4-criterios-tecnicos-de-acessibilidade) |
| [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) | H11 | [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos) | Seção 5 | Conclusão e ajuda por tentativa no F3 | `100 × S/N` | [Faixas percentuais](../fase-2/criterios-julgamento.md#2-metricas-percentuais) |
| [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) | H11 | [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) | Seção 5 | Erros operacionais por tentativa no F3 | `100 × E/N` | [Faixas percentuais, menor é melhor](../fase-2/criterios-julgamento.md#2-metricas-percentuais) |
| [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) | H11 | [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma) | Seção 5 | Tempos das conclusões autônomas no F3 | Mediana de `t_fim − t_início` | [Faixas de tempo](../fase-2/criterios-julgamento.md#3-tempo-e-consumo-de-recursos) |

*Tabela 10. Rastreabilidade entre procedimentos e especificação da Fase 2. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

## 7. Verificação piloto

Antes da coleta oficial, uma sessão piloto testa a clareza dos roteiros.

1. Um integrante executa as seções 3 e 4 em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) seguindo apenas este documento, sem ajuda de quem o escreveu.
2. Uma pessoa de fora da equipe, que atenda aos critérios da Tabela 7, faz as tarefas T1 a T3 da seção 5 com o roteiro completo.
3. A equipe confere se o caminho das tarefas existe na conta de teste, se os enunciados foram entendidos sem explicação extra, se o limite de 5 minutos é suficiente e se os formulários cobrem tudo o que aconteceu.
4. Ajustes de texto ou de formulário são feitos antes da coleta e registrados no histórico de versões deste documento.

Os dados do piloto não entram no cálculo das métricas, e a pessoa do piloto não participa da coleta oficial.

## 8. Instrumentos de coleta

Os formulários abaixo são preenchidos na Fase 4. Cada um vira uma planilha compartilhada da equipe, com uma linha por registro.

### F1. Registro da inspeção automatizada

| Sessão | Página | Ferramenta | Regra | Critério WCAG | Impacto | Seletor do elemento | Etapa de tarefa afetada | Evidência |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

*Tabela 11. Formulário F1, registro da inspeção automatizada. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

### F2. Triagem e consentimento dos voluntários

**Parte 1, triagem:** idade igual ou superior a 18 anos (sim ou não); já usou a Khan Academy (sim ou não); usa computador com mouse e teclado no dia a dia (sim ou não); trabalha com teste, design ou desenvolvimento web (sim ou não); faixa etária; frequência de uso de computador; plataformas de estudo on-line já usadas.

**Parte 2, consentimento:** objetivo da atividade; o que será registrado (tela, áudio do computador, tempos e anotações); caráter voluntário e direito de parar a qualquer momento; uso dos dados apenas de forma agregada e anonimizada nesta disciplina; prazo de exclusão dos arquivos brutos; autorização de gravação (sim ou não); data e aceite.

### F3. Registro por tarefa dos voluntários

| Sessão | Participante | Tarefa | Início | Fim | Tempo (s) | Concluiu (sim ou não) | Autônoma (sim ou não) | Pedidos de ajuda | Erros operacionais | Falha técnica | Desistiu | Observações |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

*Tabela 12. Formulário F3, registro por tarefa dos voluntários. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

### F4. Percepção ao final da sessão

1. Qual das três tarefas foi a mais difícil? Por quê?
2. Em algum momento você não soube o que fazer em seguida? Onde?
3. De 1 (muito difícil) a 5 (muito fácil), como você avalia a facilidade de usar o site pela primeira vez?

As respostas descrevem a experiência relatada e não entram no cálculo de M12 a M14.

### F5. Registro dos testes manuais de acessibilidade

| Sessão | Métrica | Ambiente | Tecnologia ou configuração | Tarefa | Etapa | Observação | Barreira (`B-NN`) | Classificação | Evidência |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

*Tabela 13. Formulário F5, registro dos testes manuais de acessibilidade. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

### F6. Checklist de contraste

| Página | Elemento | Essencial (sim ou não) | Cor do texto | Cor do fundo | Tamanho | Razão medida | 1.4.3 AA | 1.4.6 AAA | Evidência |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

*Tabela 14. Formulário F6, checklist de contraste. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

### F7. Registro do ambiente da sessão

| Sessão | Data | Avaliador | Ambiente | Sistema operacional e versão | Navegador e versão | Tecnologia assistiva e versão | Resolução | Zoom ou tema de contraste | Alterações de conteúdo das tarefas |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

*Tabela 15. Formulário F7, registro do ambiente da sessão. Fonte: Elaborada por: [Luisa de Souza](https://github.com/luisa12ll)*

## Referências

<a id="s1"></a>

> [S1] WORLD WIDE WEB CONSORTIUM (W3C). **Web Content Accessibility Guidelines (WCAG) 2.1**. W3C Recommendation, 5 jun. 2018. Disponível em: <https://www.w3.org/TR/2018/REC-WCAG21-20180605/>. Acesso em: 13 nov. 2026.

<a id="s2"></a>

> [S2] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Measurement of system and software product quality. Genebra: ISO, 2016.

<a id="s3"></a>

> [S3] GOOGLE. **Lighthouse accessibility score**. Chrome for Developers. Disponível em: <https://developer.chrome.com/docs/lighthouse/accessibility/scoring>. Acesso em: 13 nov. 2026.

<a id="s4"></a>

> [S4] DEQUE SYSTEMS. **axe-core**: accessibility engine for automated Web UI testing. Disponível em: <https://github.com/dequelabs/axe-core>. Acesso em: 13 nov. 2026.

<a id="s5"></a>

> [S5] BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Lei Geral de Proteção de Dados Pessoais (LGPD). Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 13 nov. 2026.

<a id="s6"></a>

> [S6] NV ACCESS. **NVDA User Guide**. Disponível em: <https://www.nvaccess.org/files/nvda/documentation/userGuide.html>. Acesso em: 13 nov. 2026.

<a id="s7"></a>

> [S7] APPLE. **VoiceOver User Guide for Mac**. Disponível em: <https://support.apple.com/guide/voiceover/welcome/mac>. Acesso em: 13 nov. 2026.

<a id="s8"></a>

> [S8] GNOME PROJECT. **Orca Screen Reader**. Disponível em: <https://help.gnome.org/users/orca/stable/>. Acesso em: 13 nov. 2026.

<a id="s9"></a>

> [S9] TPGI. **Colour Contrast Analyser (CCA)**. Disponível em: <https://www.tpgi.com/color-contrast-checker/>. Acesso em: 13 nov. 2026.

<a id="s10"></a>

> [S10] MICROSOFT. **Change color contrast in Windows**. Disponível em: <https://support.microsoft.com/windows/change-color-contrast-in-windows-fedc744c-90ac-69df-aed5-c8a90125e696>. Acesso em: 13 nov. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|---|---|---|---|---|
| 1.0 | 13/11/2026 | Elaboração dos procedimentos de inspeção automatizada, testes manuais de acessibilidade e testes com voluntários, com rastreabilidade para M8 a M14 | [Luisa de Souza](https://github.com/luisa12ll) | [Enzo Menali](https://github.com/menali17) |
