# Escopo da avaliação

<a id="escopo-e-objetos"></a>

## 1. Escopo e objetos de avaliação

### 1.1 Foco da avaliação

A avaliação examina a qualidade externa da [Khan Academy](https://pt.khanacademy.org/) nas características **Eficiência de desempenho**, **Portabilidade** e **Usabilidade**, conforme as subcaracterísticas selecionadas nos [Requisitos de avaliação](requisitos-de-avaliacao.md): comportamento temporal, utilização de recursos, adaptabilidade, acessibilidade e apreensibilidade.

O objeto é exclusivamente a **plataforma web acessada por navegadores em computadores**. A equipe observa comportamentos disponíveis pela interface pública, sem acesso ao código-fonte, à infraestrutura de servidores ou a dados internos. Aplicativos nativos e navegadores de celulares não fazem parte da avaliação.

Os perfis de estudantes e as condições de uso que fundamentam esse recorte estão descritos em [Produto e contexto](produto-e-contexto.md). O escopo não pressupõe que a plataforma atende a esses perfis; ele define como produzir evidências sobre as barreiras e os comportamentos observáveis relevantes.

### 1.2 Fluxos avaliados

Os ensaios utilizam quatro fluxos identificados de `FL1` a `FL4`. Os três primeiros representam a jornada central de estudo e recebem maior profundidade. O quarto é secundário e serve para verificar a consulta ao próprio progresso.

| ID | Módulo | Tarefa delimitada | Saída observável |
|---|---|---|---|
| `FL1` | Navegação em cursos | Localizar uma disciplina, abrir um curso e selecionar uma unidade ou aula | Conteúdo selecionado apresentado pela interface |
| `FL2` | Videoaulas | Iniciar e pausar uma videoaula e, quando disponíveis, acionar legenda ou transcrição | Estado do reprodutor e recursos selecionados apresentados ao usuário |
| `FL3` | Exercícios | Informar uma resposta, solicitar uma dica quando disponível e enviar a resposta | Retorno da plataforma sobre a resposta e continuidade da atividade |
| `FL4` | Progresso do estudante | Abrir a área do estudante e consultar o progresso exibido pela plataforma | Informações de progresso disponíveis para a própria conta de teste |

*Tabela 1. Fluxos e saídas observáveis incluídos na avaliação. Fonte: Elaborada por: [Enzo Menali](https://github.com/menali17)*

A autenticação é uma precondição dos ensaios, não um objeto de avaliação. Será utilizada uma conta de teste controlada pela equipe, sem dados pessoais de estudantes menores de idade. O painel de pais ou responsáveis não integra os fluxos principais porque acrescentaria outro papel, vinculação entre contas e tarefas que não são necessárias para avaliar a jornada central do estudante.

<a id="ambientes-de-teste"></a>

## 2. Ambientes de teste

### 2.1 Navegadores e motores de renderização

A adaptabilidade será observada nos três motores de renderização contemplados pela matriz de ambientes:

- **Blink**, por meio do Google Chrome;
- **Gecko**, por meio do Mozilla Firefox;
- **WebKit**, por meio do Apple Safari.

As versões exatas serão registradas na coleta. A escolha de versões estáveis vigentes evita fixar antecipadamente números que podem mudar antes dos ensaios.

### 2.2 Matriz direcionada de ambientes

A Tabela 2 define combinações com finalidade específica. A avaliação não executará o produto cartesiano de todos os navegadores, sistemas, fluxos e técnicas, pois isso reduziria a profundidade e a repetibilidade dentro do calendário disponível.

| ID | Sistema operacional | Navegador | Finalidade principal | Tecnologia assistiva |
|---|---|---|---|---|
| `A1` | Windows | Google Chrome | Ambiente de referência para eficiência de desempenho, adaptabilidade e acessibilidade | NVDA e navegação por teclado |
| `A2` | Windows | Mozilla Firefox | Comparação de adaptabilidade com o motor Gecko | Navegação por teclado |
| `A3` | macOS | Apple Safari | Adaptabilidade no motor WebKit e acessibilidade no ecossistema Apple | VoiceOver e navegação por teclado |
| `A4` | Ubuntu LTS | Mozilla Firefox | Adaptabilidade em sistema livre e acessibilidade no Linux | Orca e navegação por teclado |

*Tabela 2. Matriz direcionada de ambientes e finalidade de cada combinação. Fonte: Elaborada por: [Enzo Menali](https://github.com/menali17)*

Windows e macOS serão executados em computadores reais disponíveis à equipe. O Ubuntu poderá ser executado em computador real ou máquina virtual; a modalidade e os recursos alocados serão registrados antes da coleta. Essa diferença será considerada na interpretação, sem comparar diretamente consumo de recursos entre máquinas distintas.

### 2.3 Ambiente de referência para desempenho

O cenário da escola pública motiva a observação de comportamento temporal e utilização de recursos, pois limitações de processamento, memória ou conectividade podem impedir a execução dos fluxos de estudo. Para tornar essa preocupação verificável sem presumir as condições de todas as escolas, os ensaios serão concentrados em um ambiente de referência documentado e em dois perfis de rede reproduzíveis.

Comportamento temporal e utilização de recursos serão medidos somente no ambiente `A1`. Antes da coleta serão registrados processador, memória, sistema operacional, versão do navegador, resolução e processos relevantes em segundo plano.

Cada tarefa dos fluxos `FL1` a `FL3` terá uma execução de aquecimento, não contabilizada, e cinco repetições válidas em cada condição de rede. Serão usadas duas condições: conexão sem limitação artificial e perfil controlado de conexão limitada. A largura de banda, a latência e eventual perda de pacotes do perfil limitado serão fixadas no plano de medição e registradas junto às evidências. A conta, o conteúdo, a sequência de passos e a configuração do navegador serão mantidos constantes entre repetições. As cinco repetições são um critério metodológico da equipe para reduzir o peso de ocorrências isoladas, não um mínimo prescrito pelas normas citadas.

Esse desenho permite comparação interna sob condições controladas, mas não transforma o computador utilizado em representante de todos os equipamentos de escolas públicas.

### 2.4 Acessibilidade e apreensibilidade

Os fluxos `FL1` a `FL3` serão percorridos manualmente com teclado e leitores de tela nas combinações `A1`, `A3` e `A4`. Uma inspeção automatizada baseada nas WCAG será usada como apoio nas mesmas páginas, sem substituir a verificação de que as tarefas podem ser executadas com tecnologia assistiva.

A apreensibilidade será observada nos fluxos `FL1` a `FL3`, no ambiente `A1`, com três a cinco participantes adultos que declarem não ter experiência anterior com a Khan Academy. Serão registrados conclusão da tarefa, erros observáveis, pedidos de ajuda e percepção relatada ao final. Os participantes serão identificados apenas por códigos e deverão consentir com a atividade. A quantidade é uma escolha da equipe compatível com uma investigação exploratória, não uma amostra estatística. Se a equipe não conseguir recrutar a amostra planejada, não será apresentada conclusão sobre estudantes reais; a inspeção da equipe será identificada como evidência exploratória.

<a id="profundidade"></a>

## 3. Profundidade da avaliação

A avaliação é externa e de caixa-preta. A Tabela 3 relaciona cada subcaracterística à profundidade planejada e às evidências que deverão permitir reprodução e auditoria dos resultados.

| Subcaracterística | Objetos e ambientes | Profundidade planejada | Evidências previstas |
|---|---|---|---|
| Comportamento temporal | `FL1` a `FL3` em `A1` | Uma execução de aquecimento e cinco repetições válidas por tarefa e condição de rede | Marcações de início e fim, exportações de rede, configuração do perfil e planilha de resultados brutos |
| Utilização de recursos | `FL1` a `FL3` em `A1` | Cinco repetições com a mesma conta e conteúdo, registrando os recursos definidos no plano de medição | Registros do navegador ou sistema operacional, configuração do computador e planilha de resultados brutos |
| Adaptabilidade | `FL1` a `FL4` em `A1` a `A4` | Execução funcional dirigida em resoluções de referência de 1366 × 768 e 1920 × 1080, sem alterar o produto | Lista de verificação por ambiente, capturas e descrição de divergências reproduzíveis |
| Acessibilidade | `FL1` a `FL3` em `A1`, `A3` e `A4` | Navegação por teclado e leitor de tela, complementada por inspeção automatizada nas páginas avaliadas | Roteiro executado, gravações ou capturas permitidas, achados manuais e relatório automatizado |
| Apreensibilidade | `FL1` a `FL3` em `A1` | Três a cinco participantes adultos novos na plataforma, com tarefas e instruções iguais | Formulário anonimizado de execução, erros, ajuda solicitada e percepção relatada |

*Tabela 3. Profundidade planejada e evidências por subcaracterística. Fonte: Elaborada por: [Enzo Menali](https://github.com/menali17)*

As resoluções são condições experimentais definidas pela equipe para comparar uma área de visualização menor e outra maior em computadores. Elas não são apresentadas como estimativa da distribuição de telas da população. Métricas, fórmulas e critérios de julgamento serão especificados na Fase 2; este documento delimita os objetos, ambientes e intensidade dos ensaios.

<a id="fora-do-escopo"></a>

## 4. Elementos fora do escopo e justificativas dos cortes

A Tabela 4 explicita os cortes que mantêm a avaliação compatível com o propósito, a autorização e os recursos da equipe.

| Elemento fora do escopo | Categoria | Justificativa do corte |
|---|---|---|
| Aplicativos nativos para Android, iOS ou computadores | Plataforma | O objeto definido é a plataforma web; incluir aplicativos exigiria ferramentas, interfaces e procedimentos próprios |
| Navegadores de celulares e tablets | Plataforma | A avaliação foi delimitada a navegadores em computadores para reduzir a matriz e aprofundar os ensaios selecionados |
| Painéis de pais, responsáveis, professores e administradores | Fluxo | Esses painéis envolvem outros papéis, permissões e tarefas; a avaliação prioriza a jornada central do estudante |
| Cadastro, recuperação de conta e autenticação como objeto | Fluxo | A conta de teste é apenas precondição para acessar os fluxos; segurança de identidade não integra as decisões apoiadas |
| Backend, servidores, código-fonte e arquitetura interna | Arquitetura | A equipe não possui acesso privilegiado e não deve inferir estruturas internas a partir da interface pública |
| APIs internas não documentadas | Interface | A avaliação utiliza somente interfaces públicas destinadas ao usuário final |
| Testes ativos de segurança | Característica | Não há autorização do responsável pelo serviço para executar varreduras ou testes de intrusão |
| Carga, estresse, disponibilidade e recuperação de servidores | Característica | Induzir carga ou falhas em produção não é autorizado e não é necessário para responder às decisões `D1` a `D3` |
| Correção e qualidade pedagógica do conteúdo | Conteúdo | O objeto é a qualidade do produto de software, não a validade curricular ou didática das aulas |
| Outros sistemas, navegadores e tecnologias assistivas | Ambiente | O recorte usa as combinações disponíveis e mais distintas para manter os ensaios reproduzíveis no prazo |

*Tabela 4. Elementos fora do escopo e justificativas dos cortes. Fonte: Elaborada por: [Enzo Menali](https://github.com/menali17)*

<a id="limites-de-validade"></a>

## 5. Limites de validade dos resultados

Os limites da Tabela 5 orientam a redação das conclusões e impedem generalizações que as evidências não sustentam.

| Dimensão | Condição adotada | Limite de generalização |
|---|---|---|
| Produto e período | Plataforma web pública em português do Brasil, nas datas registradas entre outubro e novembro de 2026 | Atualizações posteriores podem alterar os comportamentos observados |
| Fluxos | `FL1` a `FL3` como fluxos centrais e `FL4` como fluxo secundário | Os resultados não representam módulos, papéis e tarefas excluídos |
| Ambientes | Combinações `A1` a `A4`, nas versões registradas | Não representam outros sistemas, navegadores, versões antigas, aplicativos ou navegadores móveis |
| Desempenho | Computador de referência `A1` e dois perfis de rede controlados | Não estima o desempenho de toda a população de computadores e conexões; permite apenas comparação nas condições registradas |
| Tecnologias assistivas | NVDA, VoiceOver e Orca, com navegação por teclado | Não comprova conformidade integral com as WCAG nem representa todas as deficiências e tecnologias assistivas |
| Apreensibilidade | Três a cinco adultos voluntários sem experiência prévia declarada | A amostra é exploratória e não representa estatisticamente estudantes de escolas públicas ou menores de idade |
| Serviço externo | Infraestrutura de produção fora do controle da equipe | Variações de rota, carga do serviço e conteúdo disponível podem influenciar as medições |

*Tabela 5. Condições e limites de validade dos resultados. Fonte: Elaborada por: [Enzo Menali](https://github.com/menali17)*

<a id="ods"></a>

## 6. Alinhamento com os Objetivos de Desenvolvimento Sustentável

A relação com os Objetivos de Desenvolvimento Sustentável (ODS) é contextual e indireta. A avaliação produz evidências técnicas sobre barreiras de acesso ao software, mas não mede resultados educacionais, renda ou os indicadores populacionais oficiais. A Tabela 6 explicita essa distinção.

| ODS e meta | Indicador oficial | Pertinência para o software e evidência produzida | Limite da relação |
|---|---|---|---|
| **ODS 4, Meta 4.5:** eliminar disparidades na educação e assegurar acesso aos níveis de ensino e à formação para grupos vulneráveis, incluindo pessoas com deficiência | **4.5.1:** índices de paridade entre grupos, como sexo, localização, renda e deficiência, aplicados aos indicadores educacionais que possam ser desagregados | Os ensaios de acessibilidade e apreensibilidade podem identificar barreiras técnicas enfrentadas ao localizar conteúdo, assistir a aulas e responder a exercícios | O estudo não calcula índices de paridade nem mede matrícula, permanência, conclusão ou aprendizagem |
| **ODS 10, Meta 10.2:** promover a inclusão social, econômica e política de todas as pessoas, independentemente de características pessoais ou condição econômica | **10.2.1:** proporção de pessoas que vivem abaixo de 50% da renda mediana, por sexo, idade e pessoas com deficiência | Ensaios de eficiência e adaptabilidade em condições documentadas podem revelar barreiras técnicas associadas a computadores e conexões limitados | O estudo não mede renda ou inclusão social da população e não demonstra impacto causal da plataforma sobre o indicador |

*Tabela 6. Relação entre ODS, metas, indicadores e evidências da avaliação. Fonte: Elaborada por: [Enzo Menali](https://github.com/menali17), com base na ONU e no IPEA*

Assim, os ODS orientam a relevância social das perguntas de avaliação, enquanto as conclusões permanecem restritas à qualidade observada do software nas condições declaradas.

<a id="rastreabilidade"></a>

## 7. Rastreabilidade com requisitos e decisões

A Tabela 7 liga os requisitos `R1` a `R5` aos fluxos, ambientes e decisões definidos nos [Requisitos de avaliação](requisitos-de-avaliacao.md).

| ID | Subcaracterística | Fluxos | Ambientes | Decisão | Atendimento no escopo |
|---|---|---|---|---|---|
| `R1` | Comportamento temporal | `FL1` a `FL3` | `A1` | `D1` | Cinco repetições por tarefa e condição de rede no ambiente de referência |
| `R2` | Utilização de recursos | `FL1` a `FL3` | `A1` | `D1` | Registros instrumentais repetidos, associados à configuração do computador |
| `R3` | Adaptabilidade | `FL1` a `FL4` | `A1` a `A4` | `D1` | Verificação dirigida nos três motores, três sistemas e duas resoluções de computador |
| `R4` | Acessibilidade | `FL1` a `FL3` | `A1`, `A3` e `A4` | `D2` | Ensaios com NVDA, VoiceOver e Orca, teclado e inspeção automatizada complementar |
| `R5` | Apreensibilidade | `FL1` a `FL3` | `A1` | `D3` | Tarefas com três a cinco participantes adultos novos na plataforma, com registros anonimizados |

*Tabela 7. Rastreabilidade entre requisitos, fluxos, ambientes e decisões. Fonte: Elaborada por: [Enzo Menali](https://github.com/menali17)*

## Referências

> BRASIL. Instituto de Pesquisa Econômica Aplicada (IPEA). **Metas e Indicadores Nacionais dos Objetivos de Desenvolvimento Sustentável**. Brasília: IPEA, 2024. Disponível em: <https://www.ipea.gov.br/ods/>. Acesso em: 20 out. 2026.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - System and software quality models. Genebra: ISO, 2011. Disponível em: <https://www.iso.org/standard/35733.html>. Acesso em: 20 out. 2026.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Measurement of system and software product quality. Genebra: ISO, 2016. Disponível em: <https://www.iso.org/standard/35747.html>. Acesso em: 20 out. 2026.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25040:2011**: Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Evaluation process. Genebra: ISO, 2011. Disponível em: <https://www.iso.org/standard/35765.html>. Acesso em: 20 out. 2026.

> ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU). **Indicadores dos Objetivos de Desenvolvimento Sustentável: Meta 4.5**. Nova York: Divisão de Estatística das Nações Unidas. Disponível em: <https://unstats.un.org/sdgs/metadata/?Goal=4&Target=4.5>. Acesso em: 20 out. 2026.

> ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU). **Indicadores dos Objetivos de Desenvolvimento Sustentável: Meta 10.2**. Nova York: Divisão de Estatística das Nações Unidas. Disponível em: <https://unstats.un.org/sdgs/metadata/?Goal=10&Target=10.2>. Acesso em: 20 out. 2026.

> WORLD WIDE WEB CONSORTIUM (W3C). **Web Content Accessibility Guidelines (WCAG) 2.1**. W3C Recommendation, 2018. Disponível em: <https://www.w3.org/TR/WCAG21/>. Acesso em: 20 out. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|---|---|---|---|---|
| 1.0 | 18/10/2026 | Criação do documento com objetos, ambientes, profundidade, cortes, limites de validade e alinhamento com ODS 4 e 10 | [José Augusto](https://github.com/JAugustoM) | |
| 1.1 | 18/10/2026 | Padronização de tabelas e referências | [José Augusto](https://github.com/JAugustoM) | |
| 1.2 | 20/10/2026 | Delimitação da plataforma web em computadores, matriz direcionada de ambientes, profundidade por subcaracterística e revisão do vínculo com os ODS | [Enzo Menali](https://github.com/menali17) | |
