# Plano de Avaliação

## 1. Finalidade e contexto

Este plano estabelece como será conduzida a avaliação da qualidade da versão web da **Khan Academy**, considerando tarefas de aprendizagem realizadas em computadores. A proposta parte do [escopo e dos requisitos definidos na Fase 1](../fase-1/escopo-da-avaliacao.md) e utiliza os [objetivos, as questões e as métricas especificados na Fase 2](../fase-2/index.md).

Trata-se de uma avaliação **externa e de caixa-preta**: serão observados o comportamento da plataforma e as interações realizadas no navegador, sem acesso ao código-fonte ou à infraestrutura do serviço. O estudo adota as características de eficiência de desempenho, portabilidade e usabilidade, no enquadramento da ISO/IEC 25010:2011 utilizado pela equipe.

O plano descreve as condições necessárias para que diferentes avaliadores possam seguir o mesmo procedimento, produzir registros comparáveis e justificar suas conclusões. Os resultados propriamente ditos serão apresentados na Fase 4.

## 2. Escopo e estratégia de avaliação

Os procedimentos adotam os quatro fluxos definidos no escopo da Fase 1:

| Fluxo | Atividade observada | Aplicação na avaliação |
|:---:|---|---|
| **FL1** | Navegar até um curso e seu conteúdo | Desempenho, adaptabilidade e usabilidade |
| **FL2** | Acessar e utilizar uma videoaula | Desempenho, adaptabilidade e usabilidade |
| **FL3** | Acessar e realizar um exercício | Desempenho, adaptabilidade e usabilidade |
| **FL4** | Consultar informações de progresso | Adaptabilidade |

*Tabela 1: Fluxos considerados no plano. Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

A estratégia combina **medições instrumentadas**, **inspeções guiadas por tarefas** e **observação de participantes iniciantes**. A seleção desses métodos decorre da natureza de cada atributo: tempos e consumo de recursos exigem instrumentos; adaptabilidade e acessibilidade exigem execução controlada em diferentes condições; apreensibilidade requer observar a realização das tarefas por pessoas sem experiência prévia na plataforma.

## 3. Métodos de avaliação

### 3.1 Eficiência de desempenho: G1

As métricas **M1–M5** investigam o tempo necessário à execução dos fluxos, o sucesso das tarefas, a utilização de CPU e memória e o volume de dados transferidos. As medições são concentradas no **ambiente A1**, sob condições de rede normal e limitada. Para cada tarefa e condição, está prevista uma execução de aquecimento, não utilizada nos cálculos, seguida de **cinco repetições válidas**.

O [procedimento de desempenho](procedimentos-desempenho.md) descreve a preparação do navegador, a instrumentação, os eventos de início e término, o tratamento de falhas e as regras de registro. Os dados serão documentados no [formulário de desempenho](registro-desempenho.md). As definições e faixas de julgamento permanecem vinculadas às [fichas de métricas](../fase-2/metricas.md) e aos [critérios da Fase 2](../fase-2/criterios-julgamento.md).

### 3.2 Adaptabilidade: G2

As métricas **M6 e M7** verificam se os fluxos permanecem executáveis nos ambientes **A1–A4** e se os elementos essenciais continuam utilizáveis nos tamanhos de janela definidos no projeto. O procedimento considera os quatro fluxos FL1–FL4, preservando a mesma sequência de tarefas e o mesmo conteúdo em cada combinação de ambiente e janela.

O [procedimento de adaptabilidade](procedimentos-adaptabilidade.md) estabelece as verificações, as regras para classificar ocorrências e os critérios de registro. O [formulário correspondente](registro-adaptabilidade.md) documenta as execuções.

### 3.3 Acessibilidade e apreensibilidade: G3

As métricas **M8–M11** abrangem a interação por teclado, o uso de leitores de tela, a ampliação da interface e a verificação de contraste. As tarefas de navegação por teclado e com leitores de tela serão verificadas em A1, A3 e A4. Os ensaios de ampliação a 200% e de contraste serão conduzidos em A1. Inspeções com Lighthouse e axe-core serão usadas como apoio à identificação de barreiras, sem substituir os testes manuais nem compor diretamente as métricas.

As métricas **M12–M14** examinam a realização das tarefas por **três a cinco participantes adultos iniciantes**, contemplando sucesso, erros operacionais e tempo. As sessões ocorrerão em A1, com três tarefas padronizadas, duração máxima de cinco minutos por tarefa, consentimento e identificação anonimizada dos participantes.

O procedimento de acessibilidade e apreensibilidade especifica os roteiros, as regras de classificação e os formulários F1 a F7. As medidas seguem as definições e os [critérios de julgamento da Fase 2](../fase-2/criterios-julgamento.md).

## 4. Condições para execução comparável

Antes da coleta oficial, devem ser registradas as configurações efetivas dos ambientes, as versões dos instrumentos, a conta de teste e os conteúdos utilizados. O mesmo curso, videoaula e exercício devem ser empregados nas execuções comparáveis, com indicação das condições iniciais e dos endereços correspondentes. Credenciais não serão publicadas.

O ambiente A1 será mantido estável durante as medições de desempenho, inclusive quanto ao navegador, aos recursos disponíveis, à resolução e às condições de rede. A configuração de rede limitada deverá ser reproduzida com os mesmos parâmetros. Alterações de zoom, contraste e tecnologia assistiva serão aplicadas em sessões próprias, com restauração das condições iniciais entre as famílias de testes.

A [especificação de recursos e ambientes](recursos-e-ambientes.md) reúne os requisitos de infraestrutura, as ferramentas e as condições de preparação. Os roteiros técnicos detalham os passos específicos de cada família.

## 5. Verificação dos instrumentos e dos dados de teste

A avaliação será precedida por um ensaio-piloto, destinado a verificar se os fluxos continuam disponíveis, se os instrumentos registram as informações esperadas e se os procedimentos podem ser executados sem interpretações divergentes. Os resultados do piloto não integram a amostra oficial; o participante do piloto também não participa das sessões oficiais. Eventuais alterações de conteúdo, configuração ou instrumento serão documentadas antes de iniciar a coleta.

Para cada ambiente, será mantido um inventário com as versões dos sistemas e instrumentos utilizados, as especificações de hardware e, quando aplicável, os parâmetros da máquina virtual. Para os fluxos, serão identificados o curso, a videoaula, o exercício e a conta de teste, preservando-se credenciais e dados pessoais.

Os instrumentos de coleta devem permitir relacionar cada observação ao fluxo executado, à métrica correspondente e à evidência obtida. Essa identificação possibilita a conferência dos registros e a reprodução das medições.

## 6. Registro, tratamento e julgamento dos resultados

Cada execução deverá permitir identificar **o fluxo, a métrica, o ambiente, a condição de teste, a versão do procedimento, o avaliador e o arquivo de evidência**. Registros inválidos, falhas de tarefa e limitações de ambiente precisam ser distinguidos conforme as regras de cada procedimento, evitando a exclusão indevida de resultados desfavoráveis.

O tratamento dos dados seguirá as fórmulas estabelecidas na Fase 2. Em seguida, os valores obtidos serão comparados aos [níveis de pontuação e critérios de julgamento](../fase-2/criterios-julgamento.md). A interpretação deverá responder às questões Q1–Q11 e, por consequência, aos objetivos G1–G3. A [matriz de rastreabilidade](matriz-rastreabilidade.md) explicita essas relações.

Os critérios de julgamento definidos na Fase 2 serão utilizados para interpretar os resultados da avaliação. Antes do início das medições, será verificada a adequação dos valores e parâmetros estabelecidos às condições dos testes. Caso seja necessário realizar algum ajuste, a alteração será justificada e documentada.

A análise dos resultados considerará as condições em que os testes foram realizados, permitindo identificar os aspectos que atendem aos critérios de qualidade e aqueles que apresentam oportunidades de melhoria.

Os resultados serão apresentados juntamente com seus registros de origem, preservando a rastreabilidade das medições. Antes da publicação, informações pessoais e dados sensíveis eventualmente presentes nas evidências serão protegidos.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 14/11/2026 | Definição do escopo e dos métodos de avaliação de desempenho, adaptabilidade e usabilidade, incluindo as condições de execução e as regras de registro, tratamento e julgamento dos resultados. | [Camila Silva](https://github.com/CamilaSilvaC) e [Geovanna Alves](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
