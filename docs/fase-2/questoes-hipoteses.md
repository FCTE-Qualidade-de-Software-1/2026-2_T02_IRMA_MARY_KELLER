[← Visão geral da Fase 2](index.md)

# Questões e hipóteses — nível operacional

## Convenção e situação da proposta

Os identificadores Q1–Q5 e H1–H5 são mantidos como famílias. Seus desdobramentos identificam os atributos avaliados. A adoção dos sufixos permanece sujeita ao alinhamento com a issue #6. M2 já contém medidas distintas, explicitadas pelos sufixos.

As hipóteses abaixo são **propostas de expectativas da equipe**, derivadas das necessidades R1–R5. Não há resultados preliminares que comprovem o comportamento da Khan Academy. As normas definem características e requisitos de referência; não demonstram que a plataforma atenderá a eles. A equipe deverá ratificar as expectativas antes de atribuí-las a si mesma.

“Adequado” nas hipóteses significa obter pontuação de questão **pelo menos 2**, pelas regras dos [critérios de julgamento](criterios-julgamento.md), em todos os grupos obrigatórios da questão, com cobertura completa do plano, inclusive combinações complementares. “Inconclusivo” não confirma nem contraria uma hipótese. Trata-se de verificação descritiva no escopo ensaiado, sem alegar teste estatístico ou generalização populacional.

A Tabela 1 cobre os atributos documentados. Os tamanhos de janela pertencem à adaptabilidade; ampliação e contraste, à acessibilidade.

**Tabela 1 — Cobertura de atributos, questões, hipóteses e medidas.**

| Origem e objetivo | Atributo | Questão qualitativa e operacional | Hipótese proposta | Medida |
|---|---|---|---|---|
| R1 / G1 | Espera para carregar páginas, iniciar vídeo e obter resposta de exercício | **Q1:** A espera nas etapas dos fluxos permite utilizar o conteúdo sem prejudicar a continuidade da atividade, em cada ambiente obrigatório? | **H1:** Em cada ambiente obrigatório, a espera atende aos limites aceitáveis previamente definidos para as etapas avaliadas. | M1, por etapa e ambiente |
| R2 / G1 | CPU | **Q2.1:** A plataforma permite concluir os fluxos sem sobrecarregar a capacidade de processamento disponível em cada ambiente? | **H2.1:** A mediana das médias temporais de CPU das execuções comparáveis permanece dentro do orçamento aceitável em cada grupo obrigatório, sem bloqueio impeditivo atribuível à sobrecarga conforme o protocolo. | M2.CPU |
| R2 / G1 | Memória | **Q2.2:** Os fluxos podem ser utilizados dentro da memória disponível, sem interrupção por esgotamento desse recurso? | **H2.2:** A mediana dos picos de memória entre sessões permanece no orçamento aceitável nos grupos obrigatórios, respeitada a regra prévia para eventual limite rígido de capacidade, sem interrupção atribuível ao esgotamento observado. | M2.RAM |
| R2 / G1 | Dados de rede | **Q2.3:** O volume de dados exigido pelos fluxos é compatível com o orçamento de acesso definido para o cenário? | **H2.3:** A mediana do tráfego total das execuções comparáveis de cada fluxo padronizado permanece dentro do orçamento aceitável em cada grupo obrigatório. | M2.REDE |
| R3 / G2 | Adaptação entre SOs e navegadores | **Q3.1:** O estudante consegue concluir os fluxos essenciais nos ambientes selecionados sem ajustes extraordinários? | **H3.1:** Todas as combinações essenciais de fluxo, SO e navegador são concluídas, sem ajustes extraordinários. | M3.AMB |
| R3 / G2 | Adaptação a tamanhos de janela | **Q3.2:** O conteúdo e os controles essenciais continuam utilizáveis nos tamanhos de janela selecionados para computadores? | **H3.2:** Todas as combinações essenciais de ambiente, janela e fluxo permanecem executáveis, sem perda de controles ou conteúdo necessário. | M3.JAN |
| R4 / G3 | Operação por teclado | **Q4.1:** Uma pessoa que utiliza apenas teclado consegue concluir os fluxos essenciais sem bloqueios de navegação? | **H4.1:** Todos os fluxos essenciais são concluídos por teclado, sem armadilha de foco ou controle essencial inacessível. | M4.TEC |
| R4 / G3 | Uso de leitor de tela | **Q4.2:** Uma pessoa que utiliza leitor de tela recebe as informações necessárias e consegue concluir os fluxos essenciais? | **H4.2:** Todas as combinações essenciais de tarefa, leitor de tela e ambiente podem ser concluídas, com informações necessárias perceptíveis. | M4.LEI |
| R4 / G3 | Ampliação | **Q4.3:** A pessoa que amplia o texto consegue ler e operar os fluxos sem perder conteúdo ou funcionalidade? | **H4.3:** Os fluxos essenciais permanecem utilizáveis com texto ampliado até 200%, observadas as exceções do critério WCAG 1.4.4. | M4.AMP |
| R4 / G3 | Contraste e uso em configuração de alto contraste | **Q4.4:** A apresentação visual permite distinguir informações e controles necessários nos fluxos essenciais? | **H4.4:** Os elementos essenciais satisfazem os critérios de contraste selecionados e permanecem utilizáveis na configuração de alto contraste definida no protocolo. | M4.CON |
| R5 / G3 | Aprendizagem inicial com autonomia | **Q5:** Estudantes novos conseguem compreender como iniciar e concluir as tarefas essenciais sem orientação adicional? | **H5:** A conclusão autônoma alcança os patamares aceitáveis previamente definidos para cada tarefa essencial e para o conjunto avaliado. | M5, por tarefa e agregado |

*Fonte: proposta elaborada com apoio de ChatGPT a partir dos requisitos R1–R5, do escopo e dos objetivos existentes. Para acessibilidade: WCAG 2.1, critérios selecionados; as expectativas de atendimento são suposições a ratificar pela equipe.*

As definições de essencial, complementar e cobertura completa seguem os [critérios de julgamento](criterios-julgamento.md#plano-e-cobertura). H4.1–H4.4 são verificadas nas combinações essenciais de ambiente, recurso e tarefa; a ausência de ensaios complementares mantém o julgamento completo inconclusivo.

## Fundamentação das hipóteses

- **H1:** R1 prioriza a continuidade do estudo diante da espera. A expectativa é uma suposição orientada à necessidade do usuário; não há baseline coletada nem prazo universal fornecido pela ISO.
- **H2.1:** R2 e o limite de hardware do escopo justificam verificar folga de processamento. O orçamento depende da capacidade e instrumentação reais da VM; não assumir que “100%” tem o mesmo significado entre ferramentas.
- **H2.2:** R2 prevê pouca memória e o escopo prevê VMs com até 4 GB. Isso fundamenta testar limites, mas não autoriza escolher um orçamento de sessão sem reservar memória para SO, navegador e outros processos.
- **H2.3:** R2 identifica o custo de dados de rede. O orçamento depende do fluxo e da decisão do cenário; vídeo exige duração, qualidade e cache padronizados. Não comparar tráfego de vídeos diferentes.
- **H3.1:** R3 e G2 exigem continuidade de uso entre ambientes. A expectativa de sucesso nos essenciais decorre dessa necessidade, sem comprovar compatibilidade real da plataforma.
- **H3.2:** A Fase 1 inclui tamanhos de tela entre os atributos de adaptabilidade. Testar janelas em computadores mantém o recorte web existente; não representa ensaio em smartphones.
- **H4.1:** WCAG 2.1, 2.1.1 e 2.1.2, fornecem referência para operação por teclado e ausência de armadilha de teclado. Aplicar as exceções pertinentes do critério 2.1.1.
- **H4.2:** WCAG 2.1, 1.3.1 e 4.1.2, fundamentam informações relacionais e identificação de controles para tecnologias assistivas. A execução real com leitor complementa as verificações; não confundir sucesso da tarefa com conformidade integral.
- **H4.3:** WCAG 2.1, 1.4.4, explicita ampliação de texto até 200% sem perda de conteúdo ou funcionalidade, com suas exceções. Não tratar simples captura de tela ampliada como teste suficiente.
- **H4.4:** WCAG 2.1, 1.4.3, adota contraste mínimo de 4,5:1 para texto normal e 3:1 para texto grande, com exceções; 1.4.11 prevê 3:1 para componentes e informação gráfica abrangidos pelo critério. Registrar a definição normativa de texto grande e as exceções no checklist. Alto contraste do SO é um ensaio adicional e não substitui medir essas relações.
- **H5:** R5 e D3 justificam observar se é necessário planejar orientação inicial. A expectativa de autonomia é suposição a ratificar. M5 mede sucesso na primeira utilização como indicador limitado de apreensibilidade; não mede retenção nem curva de aprendizagem.

## Verificação das hipóteses

Cada H1, H2.1–H2.3, H3.1–H3.2, H4.1–H4.4 e H5 é sustentada descritivamente quando sua questão tem nota pelo menos 2 e cobertura obrigatória completa. É contrariada na amostra quando a nota é 0 ou 1, e inconclusiva quando faltam dados obrigatórios ou parâmetros aprovados. H2, H3 e H4 identificam somente as famílias correspondentes. H1, H2.1–H2.3 e H5 ainda dependem de parâmetros fundamentados e aprovados para verificação operacional.

O julgamento de produto e o status da hipótese devem aparecer em colunas distintas. As hipóteses adotadas preveem atendimento no patamar 2. H3.1–H3.2 e H4.1–H4.4 se referem às combinações essenciais: uma falha complementar pode reduzir a pontuação para 2 sem contrariá-las, desde que a cobertura do plano esteja completa. Uma hipótese de sucesso de todas as combinações exigiria nota 3 e não é adotada aqui.

Exemplo exclusivamente lógico: se CPU recebe 3, RAM recebe 1 e rede recebe 2, Q2 recebe 1. H2.2 é contrariada, H2.1 e H2.3 são sustentadas, e G1 não poderá superar 1. Se faltar coleta de rede, Q2/G1 ficam inconclusivos, embora a insuficiência de RAM já esteja documentada. **As notas do exemplo não são resultados do projeto.**

## Referência de acessibilidade

[W3C — WCAG 2.1, recomendação de 5 de junho de 2018](https://www.w3.org/TR/2018/REC-WCAG21-20180605/). A seleção de critérios não permite declarar conformidade WCAG integral.


## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- | 
| 1.0 | 18/10/2026 | Elaboração das questões e hipóteses GQM e organização da tabela de correspondência com os objetivos e métricas. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho)| 
| 1.1 | 19/10/2026 | Detalhamento das 11 questões e hipóteses por atributo e de suas regras de verificação; proposta pendente de ratificação. | Camila Silva (apoio de Codex) | Revisão humana pendente |
| 1.2 | 19/10/2026 | Ajustes complementares da issue #7: observações e grupos, repetições, cobertura, hipóteses e figuras sincronizadas, com apoio de Codex. | Camila Silva | Revisão humana pendente |
| 1.3 | 19/10/2026 | Alinhamento das hipóteses de CPU e rede aos resumos por mediana dos grupos. | Camila Silva | Revisão humana pendente |

---

[Navegar pela Fase 2](index.md)
