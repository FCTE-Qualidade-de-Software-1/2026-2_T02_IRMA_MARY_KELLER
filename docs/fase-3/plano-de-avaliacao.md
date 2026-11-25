# Plano de Avaliação

**Versão 1.1**

## 1. Finalidade e contexto

Este plano estabelece como será conduzida a avaliação da qualidade da versão web da `Khan Academy`, considerando tarefas de aprendizagem realizadas em computadores. A proposta parte do [`escopo e dos requisitos definidos na Fase 1`](../fase-1/escopo-da-avaliacao.md) e utiliza os [`objetivos, as questões e as métricas especificados na Fase 2`](../fase-2/index.md).

Trata-se de uma avaliação `externa e de caixa-preta`: serão observados o comportamento da plataforma e as interações realizadas no navegador, sem acesso ao código-fonte ou à infraestrutura do serviço. O estudo adota as características de eficiência de desempenho, portabilidade e usabilidade, no enquadramento da ISO/IEC 25010:2011 utilizado pela equipe.

O plano descreve as condições necessárias para que diferentes avaliadores possam seguir o mesmo procedimento, produzir registros comparáveis e justificar suas conclusões. Os resultados propriamente ditos serão apresentados na Fase 4.

## 2. Escopo e estratégia de avaliação

Os procedimentos adotam os quatro fluxos definidos no escopo da Fase 1:

| Fluxo | Atividade observada | Aplicação na avaliação |
|:---:|---|---|
| [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos) | Navegar até um curso e seu conteúdo | Desempenho, adaptabilidade e usabilidade |
| [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos) | Acessar e utilizar uma videoaula | Desempenho, adaptabilidade e usabilidade |
| [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) | Acessar e realizar um exercício | Desempenho, adaptabilidade e usabilidade |
| [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos) | Consultar informações de progresso | Adaptabilidade |

*Tabela 1: Fluxos considerados no plano. Fonte: elaboração de [`Camila Silva Cavalcante`](https://github.com/CamilaSilvaC) e [`Geovanna Alves Umbelino`](https://github.com/GeovannaUmbelino).*

A estratégia combina `medições instrumentadas`, `inspeções guiadas por tarefas` e `observação de participantes iniciantes`. A seleção desses métodos decorre da natureza de cada atributo: tempos e consumo de recursos exigem instrumentos; adaptabilidade e acessibilidade exigem execução controlada em diferentes condições; apreensibilidade requer observar a realização das tarefas por pessoas sem experiência prévia na plataforma.

## 3. Métodos de avaliação

### 3.1 Eficiência de desempenho: G1

As métricas [`M1`](../fase-2/metricas.md#11-m1-tempo-observavel-por-etapa), [`M2`](../fase-2/metricas.md#12-m2-taxa-de-conclusao-dos-fluxos), [`M3`](../fase-2/metricas.md#13-m3-utilizacao-de-cpu), [`M4`](../fase-2/metricas.md#14-m4-pico-de-memoria) e [`M5`](../fase-2/metricas.md#15-m5-dados-transferidos) investigam o tempo necessário à execução dos fluxos, o sucesso das tarefas, a utilização de CPU e memória e o volume de dados transferidos. As medições são concentradas no ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), sob condições de rede normal e limitada. Para cada tarefa e condição, está prevista uma execução de aquecimento, não utilizada nos cálculos, seguida de `cinco repetições válidas`.

O [`procedimento de desempenho`](procedimentos-desempenho.md) descreve a preparação do navegador, a instrumentação, os eventos de início e término, o tratamento de falhas e as regras de registro. Os dados serão documentados no formulário de desempenho. As definições e faixas de julgamento permanecem vinculadas às [`fichas de métricas`](../fase-2/metricas.md) e aos [`critérios da Fase 2`](../fase-2/criterios-julgamento.md).

### 3.2 Adaptabilidade: G2

As métricas [`M6`](../fase-2/metricas.md#16-m6-execucao-por-ambiente) e [`M7`](../fase-2/metricas.md#17-m7-adaptacao-ao-tamanho-da-janela) verificam se os fluxos permanecem executáveis nos ambientes [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A2`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes) e se os elementos essenciais continuam utilizáveis nos tamanhos de janela definidos no projeto. O procedimento considera os quatro fluxos [`FL1`](../fase-1/escopo-da-avaliacao.md#fluxos), [`FL2`](../fase-1/escopo-da-avaliacao.md#fluxos), [`FL3`](../fase-1/escopo-da-avaliacao.md#fluxos) e [`FL4`](../fase-1/escopo-da-avaliacao.md#fluxos), preservando a mesma sequência de tarefas e o mesmo conteúdo em cada combinação de ambiente e janela.

O [`procedimento de adaptabilidade`](procedimentos-adaptabilidade.md) estabelece as verificações, as regras para classificar ocorrências e os critérios de registro. O [`formulário correspondente`](../fase-4/registro-adaptabilidade.md) documenta as execuções.

### 3.3 Acessibilidade e apreensibilidade: G3

As métricas [`M8`](../fase-2/metricas.md#18-m8-execucao-por-teclado), [`M9`](../fase-2/metricas.md#19-m9-execucao-com-leitor-de-tela), [`M10`](../fase-2/metricas.md#110-m10-preservacao-com-ampliacao) e [`M11`](../fase-2/metricas.md#111-m11-conformidade-de-contraste) abrangem a interação por teclado, o uso de leitores de tela, a ampliação da interface e a verificação de contraste. As tarefas de navegação por teclado e com leitores de tela serão verificadas em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), [`A3`](../fase-1/escopo-da-avaliacao.md#ambientes) e [`A4`](../fase-1/escopo-da-avaliacao.md#ambientes). Os ensaios de ampliação a 200% e de contraste serão conduzidos em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes). Inspeções com Lighthouse e axe-core serão usadas como apoio à identificação de barreiras, sem substituir os testes manuais nem compor diretamente as métricas.

As métricas [`M12`](../fase-2/metricas.md#112-m12-conclusao-autonoma-por-estudantes-novos), [`M13`](../fase-2/metricas.md#113-m13-taxa-de-erros-operacionais) e [`M14`](../fase-2/metricas.md#114-m14-tempo-de-conclusao-autonoma) examinam a realização das tarefas por `três a cinco participantes adultos iniciantes`, contemplando sucesso, erros operacionais e tempo. As sessões ocorrerão em [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes), com três tarefas padronizadas, duração máxima de cinco minutos por tarefa, consentimento e identificação anonimizada dos participantes.

O [`procedimento de acessibilidade e apreensibilidade`](procedimentos-acessibilidade-apreensibilidade.md) especifica os roteiros, as regras de classificação e os formulários F1 a F7. As medidas seguem as definições e os [`critérios de julgamento da Fase 2`](../fase-2/criterios-julgamento.md).

## 4. Condições para execução comparável

Antes da coleta oficial, devem ser registradas as configurações efetivas dos ambientes, as versões dos instrumentos, a conta de teste e os conteúdos utilizados. O mesmo curso, videoaula e exercício devem ser empregados nas execuções comparáveis, com indicação das condições iniciais e dos endereços correspondentes. Credenciais não serão publicadas.

O ambiente [`A1`](../fase-1/escopo-da-avaliacao.md#ambientes) será mantido estável durante as medições de desempenho, inclusive quanto ao navegador, aos recursos disponíveis, à resolução e às condições de rede. A configuração de rede limitada deverá ser reproduzida com os mesmos parâmetros. Alterações de zoom, contraste e tecnologia assistiva serão aplicadas em sessões próprias, com restauração das condições iniciais entre as famílias de testes.

O artefato [`Ambientes e recursos`](ambiente-de-testes.md) reúne os requisitos de infraestrutura, as ferramentas e as condições de preparação. Os roteiros técnicos detalham os passos específicos de cada família.

## 5. Verificação dos instrumentos e dos dados de teste

A avaliação será precedida por um ensaio-piloto, destinado a verificar se os fluxos continuam disponíveis, se os instrumentos registram as informações esperadas e se os procedimentos podem ser executados sem interpretações divergentes. Os resultados do piloto não integram a amostra oficial; o participante do piloto também não participa das sessões oficiais. Eventuais alterações de conteúdo, configuração ou instrumento serão documentadas antes de iniciar a coleta.

Para cada ambiente, será mantido um inventário com as versões dos sistemas e instrumentos utilizados, as especificações de hardware e, quando aplicável, os parâmetros da máquina virtual. Para os fluxos, serão identificados o curso, a videoaula, o exercício e a conta de teste, preservando-se credenciais e dados pessoais.

Os instrumentos de coleta devem permitir relacionar cada observação ao fluxo executado, à métrica correspondente e à evidência obtida. Essa identificação possibilita a conferência dos registros e a reprodução das medições.

## 6. Registro, tratamento e julgamento dos resultados

Cada execução deverá permitir identificar `o fluxo, a métrica, o ambiente, a condição de teste, a versão do procedimento, o avaliador e o arquivo de evidência`. Registros inválidos, falhas de tarefa e limitações de ambiente precisam ser distinguidos conforme as regras de cada procedimento, evitando a exclusão indevida de resultados desfavoráveis.

O tratamento dos dados seguirá as fórmulas estabelecidas na Fase 2. Em seguida, os valores obtidos serão comparados aos [`níveis de pontuação e critérios de julgamento`](../fase-2/criterios-julgamento.md). A interpretação deverá responder às questões [`Q1`](../fase-2/questoes-hipoteses.md#31-q1-comportamento-temporal), [`Q2`](../fase-2/questoes-hipoteses.md#32-q2-utilizacao-de-cpu), [`Q3`](../fase-2/questoes-hipoteses.md#33-q3-utilizacao-de-memoria), [`Q4`](../fase-2/questoes-hipoteses.md#34-q4-consumo-de-dados-de-rede), [`Q5`](../fase-2/questoes-hipoteses.md#41-q5-adaptacao-entre-sistemas-operacionais-e-navegadores), [`Q6`](../fase-2/questoes-hipoteses.md#42-q6-adaptacao-a-tamanhos-de-janela), [`Q7`](../fase-2/questoes-hipoteses.md#51-q7-navegacao-por-teclado), [`Q8`](../fase-2/questoes-hipoteses.md#52-q8-utilizacao-com-leitor-de-tela), [`Q9`](../fase-2/questoes-hipoteses.md#53-q9-utilizacao-com-ampliacao), [`Q10`](../fase-2/questoes-hipoteses.md#54-q10-contraste-e-alto-contraste) e [`Q11`](../fase-2/questoes-hipoteses.md#55-q11-apreensibilidade) e, por consequência, aos objetivos [`G1`](../fase-2/objetivos.md#g1), [`G2`](../fase-2/objetivos.md#g2) e [`G3`](../fase-2/objetivos.md#g3). A [`matriz de rastreabilidade`](matriz-rastreabilidade.md) explicita essas relações.

Os critérios de julgamento definidos na Fase 2 serão utilizados para interpretar os resultados da avaliação. Antes do início das medições, será verificada a adequação dos valores e parâmetros estabelecidos às condições dos testes. Caso seja necessário realizar algum ajuste, a alteração será justificada e documentada.

A análise dos resultados considerará as condições em que os testes foram realizados, permitindo identificar os aspectos que atendem aos critérios de qualidade e aqueles que apresentam oportunidades de melhoria.

Os resultados serão apresentados juntamente com seus registros de origem, preservando a rastreabilidade das medições. Antes da publicação, informações pessoais e dados sensíveis eventualmente presentes nas evidências serão protegidos.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 14/11/2026 | Definição do escopo e dos métodos de avaliação de desempenho, adaptabilidade e usabilidade, incluindo as condições de execução e as regras de registro, tratamento e julgamento dos resultados. | [Camila Silva](https://github.com/CamilaSilvaC) e [Geovanna Alves](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 15/11/2026 | Inclusão de links para fluxos, ambientes, métricas, questões e objetivos, padronização dos destaques e atualização das referências ao ambiente consolidado e ao registro da Fase 4. | [Camila Silva](https://github.com/CamilaSilvaC) e [Geovanna Alves](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
