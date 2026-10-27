# Fichas das métricas GQM

**Versão 1.3**

As fichas abaixo especificam as métricas externas propostas para a avaliação **exclusivamente da versão web da Khan Academy em computadores**. Cada ficha segue a organização do exemplo fornecido: questão respondida, definição, fórmula, unidade, fonte, procedimento de coleta, interpretação, justificativa e níveis. Os 14 indicadores M1–M14 correspondem às [questões](questoes-hipoteses.md) Q1–Q11.

**Situação:** proposta de especificação, sem resultados coletados. Os níveis quantitativos estão definidos como **proposta operacional do estudo** em [critérios de julgamento](criterios-julgamento.md), incluindo fundamentação e condições de aplicação. Não constituem limites oficiais da ISO/IEC 25023:2016 [S1](#s1).

## 1. Métricas detalhadas

### 1.1 M1: Tempo observável por etapa

**Questão respondida:** [Q1 / H1](questoes-hipoteses.md#31-q1-comportamento-temporal).

**Definição:** Tempo observável de carregamento ou resposta de cada etapa, sem contabilizar duração pedagógica.

**Fórmula ou indicador:** Mediana de `t_fim − t_início` em execuções concluídas da mesma etapa e condição; registrar também P90 e bloqueios.

**Unidade:** s, mediana e P90.

**Fonte dos dados:** DevTools, marcas temporais e roteiro de execução; excluir tempo de assistir vídeo ou resolver exercício.

**Procedimento de coleta:** Marcar início e fim da etapa; repetir em condições equivalentes; registrar falhas e computar mediana e P90 por etapa.

**Interpretação:** Tempos menores favorecem interação, mas medição só é comparável para a mesma tarefa e condição.

**Justificativa dos níveis:** Para tempos de resposta da interface, utilizam-se marcos de 1 s e 10 s da literatura de interação, com faixa intermediária de 3 s proposta pelo estudo. A mediana resume o desempenho e o P90 evidencia esperas longas; excluir tempo pedagógico.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.2 M2: Taxa de conclusão dos fluxos

**Questão respondida:** [Q1 / H1](questoes-hipoteses.md#31-q1-comportamento-temporal).

**Definição:** Proporção de tentativas iniciadas que efetivamente concluem o fluxo.

**Fórmula ou indicador:** `100 × C/N`, tentativas do fluxo concluídas / tentativas elegíveis; inclui tentativas não concluídas no denominador.

**Unidade:** %.

**Fonte dos dados:** Registro de execução com início, sucesso, falha, timeout e condição de ensaio.

**Procedimento de coleta:** Registrar conclusão, falha ou timeout em toda tentativa elegível, inclusive as não concluídas.

**Interpretação:** Evita que resultados rápidos de apenas algumas execuções escondam bloqueios.

**Justificativa dos níveis:** Uma duração curta não comprova sucesso quando parte das tentativas falha. A avaliação usa todas as tentativas elegíveis no denominador.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.3 M3: Utilização de CPU

**Questão respondida:** [Q2 / H2](questoes-hipoteses.md#32-q2-utilizacao-de-cpu).

**Definição:** Percentual médio de utilização da CPU durante o fluxo e episódios de sobrecarga.

**Fórmula ou indicador:** `CPU_média = Σ CPU_i / n`; registrar pico, duração e ocorrências de sobrecarga.

**Unidade:** % de CPU conforme instrumento.

**Fonte dos dados:** Monitoramento do navegador/sistema, por fluxo; identificar escopo do processo e intervalo amostral.

**Procedimento de coleta:** Identificar processo e significado do percentual do instrumento; registrar amostras, picos e duração dos excessos.

**Interpretação:** A média precisa ser acompanhada de picos, pois sobrecarga pode interromper tarefas.

**Justificativa dos níveis:** Monitorar picos e duração da sobrecarga; a CPU média não é suficiente para aprovar uma execução que foi interrompida.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.4 M4: Pico de memória

**Questão respondida:** [Q3 / H3](questoes-hipoteses.md#33-q3-utilizacao-de-memoria).

**Definição:** Maior consumo de memória da sessão ou processo durante cada execução.

**Fórmula ou indicador:** `RAM_pico = max(RAM(t))` em cada execução válida.

**Unidade:** MB.

**Fonte dos dados:** Monitor de memória por processo/sessão, com registros de interrupções.

**Procedimento de coleta:** Amostrar memória no intervalo do fluxo e registrar o máximo individual, travamentos e ambiente.

**Interpretação:** O pico representa risco de esgotamento em computadores de recursos limitados.

**Justificativa dos níveis:** A memória máxima é relevante para dispositivos com recursos limitados; a capacidade de memória efetivamente disponível para a sessão deve ser registrada.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.5 M5: Dados transferidos

**Questão respondida:** [Q4 / H4](questoes-hipoteses.md#34-q4-consumo-de-dados-de-rede).

**Definição:** Volume enviado e recebido para concluir um fluxo padronizado.

**Fórmula ou indicador:** `D = bytes_recebidos + bytes_enviados` por fluxo concluído e padronizado.

**Unidade:** MB.

**Fonte dos dados:** DevTools/Network; controlar cache, qualidade e duração dos vídeos.

**Procedimento de coleta:** Usar aba Network no DevTools; controlar cache, duração e qualidade de vídeo; computar apenas execuções concluídas.

**Interpretação:** Tráfego maior pode dificultar uso sob rede limitada; consumo baixo em execução interrompida não indica qualidade.

**Justificativa dos níveis:** A transferência deve ser comparada em fluxos concluídos e equivalentes, com cache, duração e qualidade dos vídeos controlados.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.6 M6: Execução por ambiente

**Questão respondida:** [Q5 / H5](questoes-hipoteses.md#41-q5-adaptacao-entre-sistemas-operacionais-e-navegadores).

**Definição:** Proporção de combinações elegíveis de sistema operacional, navegador e fluxo concluídas.

**Fórmula ou indicador:** `100 × C/N`, combinações SO–navegador–fluxo concluídas / combinações elegíveis testadas.

**Unidade:** %.

**Fonte dos dados:** Matriz de execução, navegador, SO, fluxo e evidência de conclusão.

**Procedimento de coleta:** Executar roteiros iguais nas combinações viáveis pré-definidas e registrar sucesso ou falha e evidência.

**Interpretação:** A taxa indica adaptação entre ambientes e não deve ocultar falha em combinação essencial.

**Justificativa dos níveis:** A adaptabilidade exige que os fluxos essenciais funcionem nos ambientes elegíveis; resultados globais não anulam uma falha essencial.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.7 M7: Adaptação ao tamanho da janela

**Questão respondida:** [Q6 / H6](questoes-hipoteses.md#42-q6-adaptacao-a-tamanhos-de-janela).

**Definição:** Proporção de combinações de dimensão de janela e fluxo sem perda de controles essenciais.

**Fórmula ou indicador:** `100 × C/N`, combinações ambiente–dimensão–fluxo com conteúdo e controles preservados / testadas.

**Unidade:** %.

**Fonte dos dados:** Roteiro com dimensões da janela, capturas e resultado por fluxo.

**Procedimento de coleta:** Fixar dimensões, testar os mesmos fluxos e documentar conteúdo, controles e impedimentos.

**Interpretação:** Desconsiderar dimensões pode ocultar barreiras mesmo quando a página abre.

**Justificativa dos níveis:** A abertura da página não é suficiente: conteúdo e controles relevantes precisam permanecer operáveis nas dimensões avaliadas.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.8 M8: Execução por teclado

**Questão respondida:** [Q7 / H7](questoes-hipoteses.md#51-q7-navegacao-por-teclado).

**Definição:** Proporção de tarefas essenciais concluídas apenas pelo teclado, sem barreiras.

**Fórmula ou indicador:** `100 × A/N`, tarefas concluídas só por teclado, sem barreira essencial / testadas.

**Unidade:** %.

**Fonte dos dados:** Observação do foco, navegação, acionamento e conclusão.

**Procedimento de coleta:** Executar roteiro sem mouse, anotando foco, ordem, atalhos, armadilhas e resultado.

**Interpretação:** Navegação completa por teclado é condição prática de acesso para usuários que não utilizam mouse.

**Justificativa dos níveis:** Barreiras em controles essenciais impedem acesso mesmo que outras tarefas funcionem por teclado.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.9 M9: Execução com leitor de tela

**Questão respondida:** [Q8 / H8](questoes-hipoteses.md#52-q8-utilizacao-com-leitor-de-tela).

**Definição:** Proporção de tarefas concluídas com leitor de tela e informações essenciais compreensíveis.

**Fórmula ou indicador:** `100 × A/N`, combinações tarefa–leitor com informação necessária percebida e conclusão / testadas.

**Unidade:** %.

**Fonte dos dados:** Registro de NVDA/VoiceOver/Orca apenas em configurações viáveis.

**Procedimento de coleta:** Usar combinações viáveis de SO, navegador e leitor; registrar anúncios, acesso aos controles e conclusão.

**Interpretação:** A simples presença de rótulos não demonstra utilização efetiva com tecnologia assistiva.

**Justificativa dos níveis:** É necessário compreender a informação essencial e concluir a tarefa com tecnologia assistiva, não apenas detectar rótulos.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.10 M10: Preservação com ampliação

**Questão respondida:** [Q9 / H9](questoes-hipoteses.md#53-q9-utilizacao-com-ampliacao).

**Definição:** Proporção de combinações de zoom e tarefa que preservam conteúdo e funcionalidade.

**Fórmula ou indicador:** `100 × A/N`, combinações com conteúdo e funções necessários preservados / testadas.

**Unidade:** %.

**Fonte dos dados:** Registro de nível de zoom, ambiente, fluxo e barreiras.

**Procedimento de coleta:** Testar níveis de ampliação predefinidos, anotando perda de elementos, rolagem impeditiva e conclusão.

**Interpretação:** A ampliação deve preservar tarefas relevantes para estudantes com baixa visão.

**Justificativa dos níveis:** A ampliação precisa preservar informação e funcionalidade; Q9 não deve ser confundida com redimensionamento de janela em Q6.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.11 M11: Conformidade de contraste

**Questão respondida:** [Q10 / H10](questoes-hipoteses.md#54-q10-contraste-e-alto-contraste).

**Definição:** Proporção de elementos aplicáveis conformes ao critério de contraste selecionado, com verificação separada de uso em alto contraste.

**Fórmula ou indicador:** `100 × E_c/E_a`, elementos aplicáveis conformes / avaliados; registrar **separadamente** conclusão em alto contraste.

**Unidade:** % + registro de uso em alto contraste.

**Fonte dos dados:** Checklist de contraste aplicável e evidências em alto contraste.

**Procedimento de coleta:** Estabelecer previamente critérios aplicáveis, medir elementos e testar fluxos em configuração de alto contraste documentada.

**Interpretação:** Um percentual agregado não garante que informações essenciais continuem distinguíveis.

**Justificativa dos níveis:** Verificar critérios aplicáveis de contraste e, separadamente, a execução em alto contraste. Elementos essenciais não conformes impedem aprovação isolada por percentual.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.12 M12: Conclusão autônoma por estudantes novos

**Questão respondida:** [Q11 / H11](questoes-hipoteses.md#55-q11-apreensibilidade).

**Definição:** Proporção de primeiras tentativas concluídas sem assistência por participantes novos.

**Fórmula ou indicador:** `100 × S/N`, primeiras tentativas concluídas sem ajuda / primeiras tentativas elegíveis; apurar por tarefa e total.

**Unidade:** %.

**Fonte dos dados:** Observação com protocolo e instrução inicial padronizada.

**Procedimento de coleta:** Aplicar instrução inicial padronizada e registrar ajuda, conclusão e abandonos por tarefa.

**Interpretação:** Conclusão independente evidencia capacidade de aprender a utilizar a interface.

**Justificativa dos níveis:** A primeira tentativa independente fornece evidência de apreensibilidade; a equipe deverá definir perfis, instrução padronizada e tarefas essenciais.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.13 M13: Taxa de erros operacionais

**Questão respondida:** [Q11 / H11](questoes-hipoteses.md#55-q11-apreensibilidade).

**Definição:** Proporção de primeiras tentativas com pelo menos um erro operacional previamente definido.

**Fórmula ou indicador:** `100 × E/N`, primeiras tentativas com ao menos um erro operacional / primeiras tentativas elegíveis.

**Unidade:** %.

**Fonte dos dados:** Observação com definição prévia de erro e registro de ocorrência por tarefa.

**Procedimento de coleta:** Definir erro antes do ensaio; observar escolhas ou ações incorretas e distingui-las de falha técnica ou exploração.

**Interpretação:** Evidencia dificuldades mesmo quando uma tarefa é concluída autonomamente.

**Justificativa dos níveis:** Erros recorrentes podem indicar dificuldade de aprendizagem mesmo quando tarefas são concluídas. O protocolo deverá distinguir erros de exploração legítima e falha técnica.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

---

### 1.14 M14: Tempo de conclusão autônoma

**Questão respondida:** [Q11 / H11](questoes-hipoteses.md#55-q11-apreensibilidade).

**Definição:** Tempo mediano das primeiras tentativas concluídas sem ajuda por estudantes novos.

**Fórmula ou indicador:** Mediana de `t_fim − t_início` das primeiras tentativas concluídas autonomamente; registrar separadamente falhas, abandonos e pedidos de ajuda.

**Unidade:** s, mediana por tarefa.

**Fonte dos dados:** Cronometragem de tarefa padronizada com estudantes sem experiência prévia.

**Procedimento de coleta:** Cronometrar cada tarefa, considerar somente conclusões autônomas e relatar desistências separadamente.

**Interpretação:** Tempo complementa autonomia, mas não compensa insucesso; referência deve ser própria da tarefa.

**Justificativa dos níveis:** As faixas propostas de 60, 120 e 180 segundos aplicam-se somente a tarefas curtas e padronizadas, não ao tempo pedagógico. Registrar abandonos e pedidos de ajuda à parte.

**Níveis de pontuação:** Aplicar as faixas quantitativas e as regras de bloqueio da seção [Níveis de pontuação e critérios de julgamento](criterios-julgamento.md), propostas para aprovação antes da coleta.

## Referências

<a id="s1"></a>

> [S1] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 25023:2016**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality. Genebra: ISO, 2016.

<a id="s2"></a>

> [S2] INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO 9241-11:2018**: Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts. Genebra: ISO, 2018.

<a id="s3"></a>

> [S3] NIELSEN, Jakob. **Response times: the 3 important limits**. Nielsen Norman Group, 1 jan. 1993.

<a id="s4"></a>

> [S4] WORLD WIDE WEB CONSORTIUM (W3C). **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C Recommendation, 12 dez. 2024.

<a id="s5"></a>

> [S5] GOOGLE. **Performance monitor panel**. Chrome for Developers, 16 maio 2024. Disponível em: <https://developer.chrome.com/docs/devtools/performance-monitor>. Acesso em: 17 out. 2026.

<a id="s6"></a>

> [S6] GOOGLE. **Network features reference**. Chrome for Developers, 16 jul. 2024. Disponível em: <https://developer.chrome.com/docs/devtools/network/reference>. Acesso em: 17 out. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 17/10/2026 | Especificação das métricas de qualidade, incluindo definições, fórmulas, fontes de dados, procedimentos de coleta e critérios de interpretação. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1 | 20/10/2026 | Inclusão dos indicadores complementares de conclusão, erros e tempo sem alterar Q1–Q11. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |[Pedro Lucas](https://github.com/Pwdrinho) |
| 1.2 | 21/10/2026 | Inclusão das referências utilizadas para elaborar o artefato |  [Camila Cavalcante](https://github.com/CamilaSilvaC) | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) |
| 1.3 | 26/10/2026 | Padronização | [Pedro Lucas](https://github.com/Pwdrinho) | [Camila Cavalcante](https://github.com/CamilaSilvaC) |