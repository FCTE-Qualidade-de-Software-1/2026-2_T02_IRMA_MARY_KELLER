# Recursos e ambientes de avaliação

A avaliação da versão web da Khan Academy exige condições de execução conhecidas para que os resultados possam ser comparados e interpretados. Esta página reúne a infraestrutura prevista, os instrumentos de medição, os dados de teste e as condições de preparação. A configuração dos ambientes parte do [escopo definido na Fase 1](../fase-1/escopo-da-avaliacao.md) e atende às [métricas e aos critérios de julgamento da Fase 2](../fase-2/criterios-julgamento.md).

Foram definidos quatro ambientes principais, identificados de [A1](../fase-1/escopo-da-avaliacao.md#ambientes) a [A4](../fase-1/escopo-da-avaliacao.md#ambientes). Eles contemplam os navegadores Chrome, Firefox e Safari, os motores Blink, Gecko e WebKit e os sistemas necessários aos testes com tecnologias assistivas. As configurações apresentadas correspondem ao **planejamento da avaliação**; as versões instaladas e as características dos equipamentos devem ser confirmadas antes da coleta oficial.

## 1. Organização dos ambientes

| Ambiente | Combinação principal | Aplicação |
|:---:|---|---|
| **[A1](../fase-1/escopo-da-avaliacao.md#ambientes)** | Windows 11 Pro e Google Chrome | Referência para desempenho (M1 a M5), adaptabilidade e verificações de usabilidade |
| **[A2](../fase-1/escopo-da-avaliacao.md#ambientes)** | Windows 11 Pro e Mozilla Firefox | Compatibilidade entre navegadores e adaptação da interface (M6 e M7) |
| **[A3](../fase-1/escopo-da-avaliacao.md#ambientes)** | macOS e Apple Safari | Compatibilidade com WebKit, adaptação da interface e testes com VoiceOver |
| **[A4](../fase-1/escopo-da-avaliacao.md#ambientes)** | Ubuntu 26.04 e Mozilla Firefox | Compatibilidade em Linux, adaptação da interface e testes com Orca |

*Tabela 1: Ambientes principais previstos para a avaliação. Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

Os testes de desempenho utilizam exclusivamente [A1](../fase-1/escopo-da-avaliacao.md#ambientes), evitando comparar resultados de consumo de recursos obtidos em configurações diferentes. [A1](../fase-1/escopo-da-avaliacao.md#ambientes) a [A4](../fase-1/escopo-da-avaliacao.md#ambientes) compõem a matriz de adaptabilidade; os ambientes [A1](../fase-1/escopo-da-avaliacao.md#ambientes), [A3](../fase-1/escopo-da-avaliacao.md#ambientes) e [A4](../fase-1/escopo-da-avaliacao.md#ambientes) também oferecem as tecnologias assistivas previstas para acessibilidade. As métricas de apreensibilidade são aplicadas em sessões com participantes, conforme os instrumentos definidos para M12 a M14.

## 2. Configuração e procedimentos por ambiente

### 2.1. A1: Windows e Chrome

[A1](../fase-1/escopo-da-avaliacao.md#ambientes) é o ambiente de referência para as medidas de desempenho e, por isso, exige controle mais rigoroso das condições de execução. Além dos fluxos de adaptabilidade, concentra os testes instrumentados de tempo, conclusão de tarefas, utilização de CPU, memória e tráfego de rede.

| Aspecto | Especificação e procedimento |
|---|---|
| **Sistema operacional** | Windows 11 Pro, com edição e build registradas antes da coleta |
| **Navegador** | Google Chrome, motor Blink; versão **157.0 prevista** na especificação técnica, sujeita à confirmação |
| **Execução e hardware** | Windows virtualizado por Winboat/Docker, com **4 vCPUs e 4 GB de RAM** previstos; registrar processador, RAM e armazenamento do hospedeiro, além de disco e rede da VM |
| **Tela e navegador** | Resolução de **1920 × 1080**, janela maximizada e zoom de 100% nas medições de referência; perfil sem extensões que interfiram nos ensaios |
| **Condições de rede** | Conexão normal e perfil limitado de **1.500 kbps de download, 750 kbps de upload e 150 ms de latência adicional**, aplicado pelo Chrome DevTools |
| **Desempenho (M1 a M5)** | Executar os fluxos definidos no [procedimento de desempenho](procedimentos-desempenho.md), com uma execução de aquecimento e cinco repetições válidas por tarefa e condição de rede; registrar tempos, conclusão, CPU, memória e dados transferidos |
| **Adaptabilidade (M6 e M7)** | Executar os fluxos e as variações de janela descritos no [procedimento de adaptabilidade](procedimentos-adaptabilidade.md), registrando a conclusão e as alterações observadas |
| **Acessibilidade** | Executar as tarefas T1–T3 por teclado e com **NVDA**; realizar em [A1](../fase-1/escopo-da-avaliacao.md#ambientes) a ampliação de 200%, as verificações de contraste e as inspeções com Lighthouse e axe-core |
| **Instrumentos** | Chrome DevTools (Network, Performance e temporização), Gerenciador de Tarefas do Chrome, monitor do sistema e, como diagnóstico complementar, Lighthouse |
| **Controle e evidências** | Registrar política de cache, estado inicial do navegador, versão dos instrumentos, escopo de CPU e memória, identificação das execuções e eventuais interferências |

*Tabela 2: Configuração e procedimentos do ambiente [A1](../fase-1/escopo-da-avaliacao.md#ambientes). Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

A utilização de uma máquina virtual está prevista na configuração do ambiente. Consequentemente, os valores de CPU e memória representam o comportamento observado **nesse ambiente virtualizado**. O procedimento de desempenho deve manter o mesmo método de leitura em todas as repetições, sem extrapolar os resultados para equipamentos físicos com outras características.

### 2.2. A2: Windows e Firefox

[A2](../fase-1/escopo-da-avaliacao.md#ambientes) permite observar se os fluxos de aprendizagem mantêm seu funcionamento quando o motor Blink é substituído pelo Gecko, sem alterar o sistema operacional utilizado em [A1](../fase-1/escopo-da-avaliacao.md#ambientes).

| Aspecto | Especificação e procedimento |
|---|---|
| **Sistema operacional** | Windows 11 Pro, com edição e build registradas |
| **Navegador** | Mozilla Firefox, motor Gecko; versão **159.1 prevista** na especificação técnica, sujeita à confirmação |
| **Execução e hardware** | Windows virtualizado por Winboat/Docker, com **4 vCPUs e 4 GB de RAM** previstos; registrar recursos do hospedeiro, disco e rede da VM |
| **Tela** | Resolução e dimensões de janela definidas no procedimento de adaptabilidade, registradas para comparação entre ambientes |
| **Adaptabilidade (M6)** | Executar os fluxos previstos e registrar conclusão, falhas e diferenças de comportamento em relação à matriz principal |
| **Adaptação da interface (M7)** | Aplicar as dimensões de janela previstas, observando legibilidade, organização e possibilidade de concluir as tarefas |
| **Instrumentos** | Firefox, ferramentas nativas de inspeção e [formulário de adaptabilidade](registro-adaptabilidade.md) |
| **Controle e evidências** | Registrar versão do navegador, configurações relevantes, resultado de cada fluxo, capturas de tela e eventuais limitações |

*Tabela 3: Configuração e procedimentos do ambiente [A2](../fase-1/escopo-da-avaliacao.md#ambientes). Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

[A2](../fase-1/escopo-da-avaliacao.md#ambientes) não integra a série de medições de desempenho M1 a M5. Sua finalidade é avaliar a continuidade de uso da plataforma em outra combinação de navegador e motor de renderização.

### 2.3. A3: macOS e Safari

[A3](../fase-1/escopo-da-avaliacao.md#ambientes) amplia a avaliação para o motor WebKit e permite observar o uso da plataforma com os recursos de acessibilidade nativos do macOS. Sua execução requer um equipamento Apple disponível durante a coleta.

| Aspecto | Especificação e procedimento |
|---|---|
| **Sistema operacional** | macOS em equipamento físico; versão e build a registrar no início da avaliação |
| **Navegador** | Apple Safari, motor WebKit; versão instalada a registrar |
| **Hardware** | Registrar modelo do equipamento, processador, memória RAM, armazenamento e resolução |
| **Adaptabilidade (M6)** | Executar os fluxos definidos e documentar funcionamento, falhas e particularidades da interface no Safari |
| **Adaptação da interface (M7)** | Reproduzir as dimensões de janela previstas no procedimento e registrar o comportamento da interface |
| **Acessibilidade** | Executar as tarefas T1–T3 por teclado e com **VoiceOver**, registrando as barreiras e evidências conforme o procedimento de acessibilidade |
| **Instrumentos** | Safari, recursos de inspeção do navegador, VoiceOver e formulário de registro dos testes |
| **Controle e evidências** | Confirmar disponibilidade do equipamento, funcionamento de áudio, configurações de acessibilidade e condições de repetição dos fluxos |

*Tabela 4: Configuração e procedimentos do ambiente [A3](../fase-1/escopo-da-avaliacao.md#ambientes). Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

O macOS é previsto em equipamento físico, sem virtualização. A ausência desse equipamento compromete a cobertura de Safari e VoiceOver e deve ser considerada na interpretação da avaliação.

### 2.4. A4: Ubuntu e Firefox

[A4](../fase-1/escopo-da-avaliacao.md#ambientes) permite verificar a adaptabilidade em Linux e a utilização do leitor de tela Orca. A virtualização torna necessário verificar previamente a resolução, a saída de áudio e o funcionamento das tecnologias assistivas.

| Aspecto | Especificação e procedimento |
|---|---|
| **Sistema operacional** | Ubuntu **26.04 previsto**, com edição e build efetivamente instaladas a registrar |
| **Navegador** | Mozilla Firefox, motor Gecko; versão **159.0 prevista** na especificação técnica, sujeita à confirmação |
| **Execução e hardware** | Máquina virtual gerenciada pelo **GNOME Boxes**, com **QEMU/KVM**, **4 vCPUs e 4 GB de RAM** previstos; registrar processador do hospedeiro, armazenamento, disco virtual e modo de rede |
| **Tela** | Registrar resolução da VM e reproduzir as dimensões de janela previstas no procedimento |
| **Adaptabilidade (M6)** | Executar os fluxos e registrar funcionamento, falhas e diferenças observadas no Linux |
| **Adaptação da interface (M7)** | Aplicar as dimensões de janela estabelecidas e registrar o comportamento da interface |
| **Acessibilidade** | Executar as tarefas T1–T3 por teclado e com **Orca**, após confirmar instalação, configuração e saída de áudio |
| **Instrumentos** | Firefox, Orca, recursos nativos de inspeção e formulário de adaptabilidade |
| **Controle e evidências** | Registrar versões, configuração da VM, funcionamento do áudio, identificação das execuções e eventuais restrições de virtualização |

*Tabela 5: Configuração e procedimentos do ambiente [A4](../fase-1/escopo-da-avaliacao.md#ambientes). Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

Os resultados obtidos em [A4](../fase-1/escopo-da-avaliacao.md#ambientes) representam a combinação de Ubuntu, Firefox e recursos virtuais alocados. O uso do Orca deve ser precedido de uma verificação-piloto, pois falhas de áudio ou de integração com a VM podem impedir a execução adequada dos testes.

## 3. Ferramentas e instrumentos de coleta

As ferramentas foram selecionadas de acordo com o tipo de informação necessário. Os instrumentos de diagnóstico complementam a análise, mas não substituem as definições de métricas da Fase 2.

| Finalidade | Instrumentos | Aplicação |
|---|---|---|
| Temporização e conclusão de tarefas | Cronometragem padronizada, APIs de temporização e Chrome DevTools | M1 e M2 |
| Utilização de recursos | Gerenciador de Tarefas do Chrome e monitores do sistema | M3 e M4 |
| Tráfego de rede | Chrome DevTools, painel Network | M5 |
| Diagnóstico de desempenho | Lighthouse e painel Performance | Apoio à interpretação de M1, M3 e M5 |
| Adaptabilidade | Chrome, Firefox, Safari e formulários de execução | M6 e M7 |
| Acessibilidade | Teclado, NVDA, VoiceOver, Orca, Lighthouse, axe DevTools e Colour Contrast Analyser | M8 a M11; inspeções automatizadas como apoio |
| Apreensibilidade | Tarefas T1–T3, cronômetro e formulários F2–F4 | M12 a M14 |

*Tabela 6: Instrumentos e respectivas finalidades. Fonte: elaboração de [Camila Silva Cavalcante](https://github.com/CamilaSilvaC) e [Geovanna Alves Umbelino](https://github.com/GeovannaUmbelino).*

## 4. Dados de teste e condições de preparação

A avaliação utiliza os fluxos de navegação por cursos (FL1), uso de videoaulas (FL2), realização de exercícios (FL3) e consulta ao progresso (FL4). Para permitir a repetição desses cenários, devem ser preparados uma conta de teste, um curso e uma unidade definidos, uma videoaula, um exercício e um estado de progresso adequado à consulta.

Os conteúdos devem ser identificados por seus títulos e endereços, acompanhados das condições iniciais necessárias a cada tarefa. Antes da coleta, os avaliadores devem confirmar que os recursos continuam disponíveis e que a conta apresenta o estado esperado. Credenciais e dados pessoais não devem ser publicados.

Os ensaios de apreensibilidade preveem **três a cinco participantes adultos sem experiência anterior com a Khan Academy**. As sessões ocorrerão em [A1](../fase-1/escopo-da-avaliacao.md#ambientes), com tarefas T1–T3 e limite de cinco minutos por tarefa. A triagem e o consentimento são registrados no formulário F2; a execução, no F3; e a percepção final, no F4. Os dados publicados devem preservar a identidade dos participantes.

## 5. Preparação dos avaliadores e controle das condições

Os avaliadores devem conhecer os fluxos selecionados e os procedimentos de registro. Para desempenho, são necessários conhecimentos de configuração de rede, interpretação dos painéis do navegador e leitura dos dados de CPU e memória. Para adaptabilidade, é necessário aplicar as mesmas tarefas e dimensões de janela em todos os ambientes. Para acessibilidade, é necessário dominar a navegação por teclado, o uso básico dos leitores de tela previstos e a classificação das barreiras observadas.

Antes da coleta oficial, deve ser realizada uma execução-piloto para confirmar o funcionamento dos instrumentos e registrar a configuração efetivamente utilizada. O inventário deve incluir:

- Identificação do ambiente, responsável e data de verificação;
- Sistema operacional, edição e build, navegador e versão;
- Processador, memória RAM, armazenamento e resolução do equipamento;
- Para máquinas virtuais, hipervisor, sistema convidado, vCPU, RAM, disco e configuração de rede;
- Leitores de tela e ferramentas instaladas, com suas versões;
- Condições de rede, dados de teste, limitações e eventuais ajustes necessários.

Os registros de [desempenho](registro-desempenho.md) e [adaptabilidade](registro-adaptabilidade.md), assim como os formulários F1 a F7 do procedimento de acessibilidade e apreensibilidade, identificam as execuções e suas evidências. As decisões que modifiquem as condições planejadas devem ser justificadas antes da coleta e refletidas no [Plano de Avaliação](plano-de-avaliacao.md) e na [matriz de rastreabilidade](matriz-rastreabilidade.md).

## Referências

- [Fase 1: Escopo da avaliação](../fase-1/escopo-da-avaliacao.md).
- [Fase 2: Critérios de julgamento](../fase-2/criterios-julgamento.md).
- [Procedimentos de desempenho](procedimentos-desempenho.md).
- [Procedimentos de adaptabilidade](procedimentos-adaptabilidade.md).
- Procedimentos de acessibilidade e apreensibilidade.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 14/11/2026 | Especificação dos ambientes de teste A1 a A4, das ferramentas de medição, dos dados de teste e das condições de preparação para a coleta. | [Camila Silva](https://github.com/CamilaSilvaC) e [Geovanna Alves](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
