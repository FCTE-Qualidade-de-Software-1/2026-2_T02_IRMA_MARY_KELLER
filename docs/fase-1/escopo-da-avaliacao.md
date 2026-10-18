# Escopo da avaliação

<a id="escopo-e-objetos"></a>

## 1. Escopo e objetos de avaliação

### 1.1 Foco da avaliação

O escopo desta avaliação é centrado na **experiência do usuário (UX)**, analisando a qualidade do produto de software da [Khan Academy](https://pt.khanacademy.org/) a partir de aspectos observáveis de **usabilidade**, **portabilidade** e **eficiência de desempenho (performance)**. 

A avaliação adota o modelo da **ISO/IEC 25010:2011**, concentrando-se nas subcaracterísticas selecionadas e priorizadas no documento de [Requisitos de avaliação](requisitos-de-avaliacao.md): **apreensibilidade**, **acessibilidade**, **adaptabilidade**, **comportamento temporal** e **utilização de recursos**.

A análise restringe-se exclusivamente à **plataforma web** da Khan Academy acessada por navegadores, examinando como a aplicação se comporta quando executada sob restrições severas de hardware e quando utilizada por pessoas que dependem de tecnologias assistivas.

### 1.2 Módulos e fluxos principais avaliados

A avaliação delimita os ensaios a três fluxos principais de interação do usuário na plataforma web:

1. **Realização de cursos**:
   - Autenticação e acesso à página do curso;
   - Navegação na árvore curricular e seleção de unidades de ensino;
   - Assistir a videoaulas no player multimídia (reprodução, pausa, ajuste de velocidade, legendas e transcrição);
   - Resolução de exercícios e atividades práticas (inserção de respostas textuais/numéricas, consulta a dicas pedagógicas e envio para verificação imediata com cálculo de domínio).
2. **Acompanhamento de métricas pelo aluno**:
   - Acesso ao painel do estudante (*Dashboard* do aluno);
   - Consulta a pontos de energia acumulados, medalhas e domínio de habilidades por disciplina;
   - Histórico de tempo de estudo e lições completadas;
   - Consulta a recomendações personalizadas de estudo sugeridas pela plataforma.
3. **Acompanhamento feito pelos pais e responsáveis**:
   - Acesso ao painel dos pais (*Parent Dashboard*);
   - Vinculação e alternância entre perfis de filhos dependentes;
   - Consulta a relatórios consolidados de tempo semanal de estudo, evolução curricular e diagnóstico de tópicos com dificuldades ou facilidades.

A Tabela 1 detalha os módulos, os fluxos correspondentes, as entradas do usuário e os comportamentos observáveis esperados.

| Módulo | Fluxo principal | Entradas do usuário | Comportamentos e saídas esperadas |
|---|---|---|---|
| **Cursos (Vídeos)** | Assistir a aulas e vídeos expositivos | Seleção da aula, comandos de reprodução de vídeo, ativação de legendas/transcrição | Carregamento fluido do vídeo, sincronia de áudio/legendas e registro de progresso da aula |
| **Cursos (Exercícios)** | Resolução de questões e lições interativas | Preenchimento de resposta, solicitação de dicas, envio para conferência | Validação da resposta, exibição de feedback imediato e atualização dos pontos de domínio |
| **Painel do Aluno** | Acompanhamento de progresso pelo estudante | Navegação entre abas de perfil, seleção de filtros de disciplinas e histórico | Exibição de gráficos de domínio, medalhas conquistadas e tempo de dedicação |
| **Painel dos Pais** | Acompanhamento do desempenho dos filhos | Seleção da conta dependente, consulta a relatórios temporais e por disciplina | Relatório consolidado de horas estudadas, nível de domínio e recomendações de apoio |

*Tabela 1. Módulos e fluxos principais avaliados na Khan Academy. Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="ambientes-de-teste"></a>

## 2. Ambientes de teste e infraestrutura experimental

### 2.1 Plataforma e motores de renderização web

A avaliação é executada **estritamente em navegadores web**, descartando aplicativos nativos para dispositivos móveis ou desktop. Para cobrir os principais os navegadores de maior uso, os testes serão realizados nos navegadores de referência das três principais *engines* (motores de renderização) do mercado:

- **Blink**: testado via **Google Chrome** (*engine* compartilhado com Microsoft Edge, Brave, Opera e Chromium);
- **Gecko**: testado via **Mozilla Firefox**;
- **WebKit**: testado via **Apple Safari**.

### 2.2 Sistemas operacionais avaliados

Para averiguar a adaptabilidade da aplicação web em múltiplos ecossistemas, foram selecionados **seis sistemas operacionais**:

1. **Windows**: principal sistema operacional comercial em computadores pessoais;
2. **MacOS**: sistema operacional proprietário representativo do ecossistema Apple e do motor WebKit;
3. **Ubuntu**: distribuição Linux baseada em Debian, amplamente empregada no meio acadêmico e institucional;
4. **Fedora**: distribuição Linux de base Red Hat, representativa de ambientes corporativos;
5. **Arch Linux**: distribuição Linux independente com modelo de lançamento contínuo (*rolling release*);
6. **OpenSUSE**: distribuição Linux de base SUSE, tradicional no mercado europeu e em servidores/estações de trabalho.
7. **Android**: sistema operacional *mobile* baseado no kernel Linux, representando os usuários de dispositivos móveis.

A inclusão de quatro distribuições Linux livres (Ubuntu, Fedora, Arch e OpenSUSE), ao lado dos dois sistemas proprietários (Windows e MacOS), visa averiguar a portabilidade da Khan Academy em sistemas de código aberto frequentemente adotados em escolas públicas, universidades e por usuários que buscam alternativas livres de licenciamento.

### 2.3 Máquinas virtuais com restrição de hardware

Para isolar variáveis externas e simular as condições de alunos de escolas públicas que utilizam computadores de entrada ou máquinas antigas, **todos os testes serão realizados exclusivamente em Máquinas Virtuais (VMs) com restrição intencional de memória RAM e núcleos de CPU**:

- **Hipervisor padronizado**: KVM/QEMU (Gnome Boxes);
- **Memória RAM alocada**: limite de 4 GB por máquina virtual;
- **Processamento alocado**: limite de 6 vCPUs por máquina virtual;
- **Condições de aceleração gráfica**: emulação de vídeo padrão do hipervisor sem GPU física dedicada.

### 2.4 Testes com leitores de tela

Como parte da avaliação de acessibilidade da experiência do usuário, a plataforma web será submetida a testes operacionais práticos com tecnologias assistivas de leitura de tela, associados à navegação estrita por teclado:

- **Windows**: testes com o leitor de tela **NVDA**;
- **MacOS**: testes com o leitor de tela nativo **VoiceOver**;
- **Linux (Ubuntu, Fedora, Arch, OpenSUSE)**: testes com o leitor de tela nativo **Orca**.

<a id="profundidade"></a>

## 3. Profundidade da avaliação

A profundidade estabelece o nível de detalhe técnico e o tipo de observação empregado em cada subcaracterística. A avaliação é conduzida sob a modalidade **caixa-preta (*black-box*)**, fundamentada na observação de comportamentos externos e na medição instrumental em ambiente virtualizado controlado.

A lista de características que serão abrangidas nos testes, assim como as subcaracteristicas escolhidas e a justificativa por trás da seleção de cada uma podem ser vistas no [documento de requisitos de avaliação](requisitos-de-avaliacao.md).

<a id="fora-do-escopo"></a>

## 4. Elementos fora do escopo e justificativas dos cortes

A delimitação das fronteiras da avaliação é essencial para assegurar que a equipe atue dentro dos recursos humanos e do calendário disponível, sem perder o rigor científico. A Tabela 3 explicita os elementos que ficam fora do escopo e o racional detalhado de cada corte.

| Elemento fora do escopo | Categoria | Racional e justificativa do corte |
|---|---|---|
| **Backend, servidores e código-fonte proprietário** | Arquitetura | O código de servidor e os bancos de dados da Khan Academy são fechados e proprietários. A avaliação externa não tem acesso privilegiado à infraestrutura de nuvem, limitando-se ao comportamento observável no navegador. |
| **Segurança e testes de intrusão** | Característica | Varreduras de vulnerabilidade ativas ou testes de penetração violariam os termos de uso do serviço e a legislação aplicável. O foco do projeto é estritamente a experiência do usuário final. |
| **Confiabilidade e tolerância a falhas do servidor** | Característica | Analisar a disponibilidade de infraestrutura ou recuperação de quedas demandaria testes de estresse não autorizados contra os servidores de produção da Khan Academy. |
| **Qualidade e exatidão do conteúdo pedagógico** | Conteúdo | O objeto de estudo é a qualidade do software segundo as normas ISO/IEC 25000 (SQuaRE), e não a pertinência curricular ou didática do material instrucional. |
| **APIs internas não documentadas** | Interface | A equipe atua exclusivamente pela interface gráfica acessível ao público geral, sem invadir rotas privadas de comunicação interna da aplicação. |

<!-- | **Aplicativos móveis nativos (Android e iOS)** | Plataforma | A equipe optou por focar integralmente na plataforma web para viabilizar um ambiente homogêneo de máquinas virtuais com controle rígido de RAM e núcleos de CPU. Incluir emuladores ou dispositivos móveis físicos multiplicaria as variáveis experimentais além do tempo disponível na disciplina. | -->

*Tabela 2. Elementos fora do escopo da avaliação e justificativa dos cortes. Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="limites-de-validade"></a>

## 5. Limites de validade dos resultados

Para assegurar a validade científica das conclusões, é necessário explicitar os limites da amostra e das condições sob as quais as evidências serão colhidas. A Tabela 4 declara os parâmetros fixados e as restrições de generalização dos resultados.

| Parâmetro | Condição adotada na avaliação | Limite de generalização dos resultados |
|---|---|---|
| **Versão da aplicação** | Plataforma web pública em português do Brasil acessível no domínio `pt.khanacademy.org` entre outubro e novembro de 2026 | As conclusões não são válidas para versões anteriores ou atualizações que alterem a arquitetura de front-end após as datas de coleta. |
| **Período de coleta** | Entre outubro e novembro de 2026 | Métricas de tempo de resposta dependem das rotas de rede e do tráfego nos servidores da Khan Academy nas datas dos testes. |
| **Amostra de hardware** | Máquinas virtuais com memória RAM restrita a 4 GB e processamento limitado a 6 vCPUs | Não reflete o desempenho em dispositivos com aceleradores gráficos físicos dedicados ou máquinas com hardware moderno abundante. |
| **Perfis e tecnologias assistivas** | Roteiros operados com leitores de tela NVDA, VoiceOver e Orca, com navegação estrita por teclado | Não generaliza para outras tecnologias assistivas não testadas (ex.: leitores comerciais como JAWS, softwares proprietários de linha braille ou controle por movimento ocular). |
| **Navegadores e versões** | Versões estáveis vigentes do Chrome, Firefox e Safari | Não permite generalizar para navegadores alternativos ou versões antigas não suportadas. |

*Tabela 3. Limites de validade e restrições de generalização dos resultados. Elaborada por: [José Augusto](https://github.com/JAugustoM)*

<a id="ods"></a>

## 6. Alinhamento com os Objetivos de Desenvolvimento Sustentável (ODS)

Os Objetivos de Desenvolvimento Sustentável (ODS) da [Agenda 2030 da ONU](https://brasil.un.org/pt-br/sdgs) orientam políticas para a erradicação da pobreza e redução das desigualdades. Sendo a Khan Academy uma ferramenta de educação pública e gratuita, a presente avaliação relaciona-se diretamente a dois ODS centrais: **ODS 4 (Educação de Qualidade)** e **ODS 10 (Redução das Desigualdades)**.

A Tabela 5 estabelece a correspondência entre os ODS selecionados, suas metas e indicadores oficiais (segundo a ONU e o IPEA), e o vínculo direto com o software e as características de qualidade avaliadas.

| ODS | Meta oficial (ONU / IPEA) | Indicador oficial | Vínculo com a avaliação da Khan Academy |
|---|---|---|---|
| **ODS 4: Educação de Qualidade** | **Meta 4.5**: Até 2030, eliminar as disparidades de gênero na educação e garantir a igualdade de acesso a todos os níveis de educação e formação profissional para os mais vulneráveis, incluindo as pessoas com deficiência, povos indígenas e as crianças em situação de vulnerabilidade. | **Indicador 4.5.1**: Índices de paridade (gênero, deficiência, renda) na participação e aproveitamento educacional. | Avaliar a **Usabilidade (Acessibilidade)** por meio de testes práticos com leitores de tela (NVDA, VoiceOver e Orca) e navegação por teclado nos fluxos de cursos e exercícios assegura que estudantes com deficiência visual possam utilizar a plataforma com autonomia, removendo barreiras tecnológicas de acesso à educação de qualidade. |
| **ODS 10: Redução das Desigualdades** | **Meta 10.2**: Até 2030, empoderar e promover a inclusão social, econômica e política de todos, independentemente da idade, gênero, deficiência, raça, etnia, origem, religião, condição econômica ou outra. | **Indicador 10.2.1**: Proporção de pessoas em situação de vulnerabilidade com acesso efetivo a serviços essenciais e oportunidades de inclusão digital. | Avaliar a **Eficiência de Desempenho (Utilização de Recursos e Comportamento Temporal)** sob restrições severas de hardware em máquinas virtuais e a **Portabilidade (Adaptabilidade)** em quatro distribuições Linux livres (Ubuntu, Fedora, Arch e OpenSUSE) garante que a plataforma seja acessível a escolas públicas e famílias de baixa renda que operam computadores antigos ou de baixo custo, mitigando a exclusão digital decorrente de limitações econômicas. |

*Tabela 4. Alinhamento entre os Objetivos de Desenvolvimento Sustentável (ODS), metas oficiais e características avaliadas. Elaborada por: [José Augusto](https://github.com/JAugustoM)*

A avaliação demonstra que subcaracterísticas técnicas de qualidade de software, como consumo comedido de memória e aderência a padrões de acessibilidade, constituem requisitos primordiais para a concretização de direitos sociais e educacionais universais.

<a id="rastreabilidade"></a>

## 7. Rastreabilidade com critérios e requisitos da avaliação

A Tabela 6 apresenta a rastreabilidade entre os requisitos de avaliação definidos em [Requisitos de avaliação](requisitos-de-avaliacao.md) (`R1` a `R5`), os fluxos principais e as decisões apoiadas (`D1` a `D3`), assegurando a coerência interna do planejamento.

| ID | Requisito de avaliação | Subcaracterística | Fluxos contemplados | Decisão apoiada | Atendimento no escopo |
|---|---|---|---|---|---|
| `R1` | Comportamento temporal aceitável | Eficiência de desempenho: comportamento temporal | Realização de cursos, painel do aluno e painel dos pais | `D1` | Medições de tempo de carregamento de páginas e envio de exercícios via DevTools |
| `R2` | Consumo comedido de recursos | Eficiência de desempenho: utilização de recursos | Realização de cursos e dashboards | `D1` | Monitoramento contínuo de CPU e memória RAM nas VMs com restrição de hardware |
| `R3` | Adaptabilidade multiplataforma | Portabilidade: adaptabilidade | Todos os fluxos principais | `D1` | Matriz de ensaios cruzada nos 6 sistemas operacionais e nos 3 motores de renderização web |
| `R4` | Acessibilidade digital assistiva | Usabilidade: acessibilidade | Realização de cursos e acompanhamento | `D2` | Testes práticos com NVDA, VoiceOver e Orca, e auditoria automatizada WCAG |
| `R5` | Apreensibilidade dos fluxos | Usabilidade: apreensibilidade | Realização de cursos e painéis | `D3` | Ensaios de tarefas com novos alunos e pais com foco em facilidade de aprendizado |

*Tabela 5. Rastreabilidade entre requisitos de avaliação, subcaracterísticas, fluxos e decisões apoiadas. Elaborada por: [José Augusto](https://github.com/JAugustoM)*

## Referências

> BRASIL. Instituto de Pesquisa Econômica Aplicada (IPEA). **Metas e Indicadores Nacionais dos Objetivos de Desenvolvimento Sustentável**. Brasília: IPEA, 2024. Disponível em: <https://www.ipea.gov.br/ods/>. Acesso em: 18 out. 2026.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality. Genebra: ISO, 2016.

> INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25040:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process. Genebra: ISO, 2011.

> ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU). **Transformando Nosso Mundo: A Agenda 2030 para o Desenvolvimento Sustentável**. Nova York: ONU, 2015. Disponível em: <https://brasil.un.org/pt-br/sdgs>. Acesso em: 18 out. 2026.

> WORLD WIDE WEB CONSORTIUM (W3C). **Web Content Accessibility Guidelines (WCAG) 2.1**. W3C Recommendation, 2018. Disponível em: <https://www.w3.org/TR/WCAG21/>. Acesso em: 18 out. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor | Commit |
|---|---|---|---|---|---|
| 1.0 | 18/10/2026 | Criação do documento de escopo da avaliação: definição de objetos, fluxos (cursos, aluno e pais), ambientes em VMs restritas (6 SOs, 3 engines e leitores de tela), profundidade, cortes, limites de validade e alinhamento com ODS 4 e 10 | [José Augusto](https://github.com/JAugustoM) | | [3f89756](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/commit/3f897567cf857b0b82120baead52195847e65af2) |
| 1.1 | 18/10/2026 | Padronização de tabelas e referências | [José Augusto](https://github.com/JAugustoM) | | [35604cf](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_IRMA_MARY_KELLER/pull/10/changes/35604cfb381bc90752a3d5679e6a073349d99179) |
