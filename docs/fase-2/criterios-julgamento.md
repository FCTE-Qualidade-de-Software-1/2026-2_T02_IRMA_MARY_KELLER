[← Visão geral da Fase 2](index.md)

# Níveis de pontuação e critérios de julgamento

Os critérios avaliam a **versão web da Khan Academy em computadores**, conforme os requisitos R1–R5 da Fase 1 e as métricas M1–M14 da Fase 2. Os resultados se aplicam somente aos fluxos e ambientes testados. A escala é uma **proposta metodológica do estudo**: os limites operacionais não são prescritos pela ISO/IEC 25023:2016.

## 1. Escala de pontuação

| Nota | Nível | Interpretação |
|:---:|---|---|
| 3 | Excelente | Supera a meta do estudo ou atende ao nível técnico mais exigente especificado |
| 2 | Alvo | Atende à meta definida para a avaliação |
| 1 | Mínimo aceitável | Apresenta limitações e exige melhoria; não corresponde a aprovação plena |
| 0 | Inaceitável | Não atende ao limite mínimo ou impede tarefa essencial |
| — | Inconclusivo | Não há evidências válidas suficientes para julgamento |

## 2. Métricas percentuais

Para M2, M6–M10 e M12, **maior é melhor**. As faixas de 100%, 90% e 75% são **metas operacionais escolhidas para distinguir atendimento integral, falhas pontuais e falhas recorrentes**; não são percentuais normativos. Registrar também as contagens absolutas e não considerar aprovado um fluxo essencial bloqueado.

| Métricas | Excelente (3) | Alvo (2) | Mínimo aceitável (1) | Inaceitável (0) |
|---|---:|---:|---:|---:|
| M2, M6, M7, M8, M9, M10, M12 | 100% | 90% ≤ x < 100% | 75% ≤ x < 90% | x < 75% |
| M13 — tentativas com erro (menor é melhor) | 0% | 0% < x ≤ 10% | 10% < x ≤ 25% | x > 25% |

Em M13, erro operacional do participante e falha técnica da plataforma devem ser registrados separadamente. As faixas de 10% e 25% também são decisões metodológicas, sujeitas ao protocolo de tarefas e participantes.

## 3. Tempo e consumo de recursos

Para M1, M3–M5 e M14, **menor é melhor**. Os valores são faixas propostas para condições específicas e não limites universais de qualidade. Sem condições de coleta comparáveis e aprovação dos parâmetros, o julgamento será inconclusivo.

| Métrica | Excelente (3) | Alvo (2) | Mínimo aceitável (1) | Inaceitável (0) |
|---|---:|---:|---:|---:|
| M1 — resposta da interface | ≤ 1 s | > 1 a 3 s | > 3 a 10 s | > 10 s |
| M3 — CPU média | ≤ 25% | > 25% a 50% | > 50% a 75% | > 75% |
| M4 — pico de memória | ≤ 512 MiB | > 512 a 1024 MiB | > 1024 a 2048 MiB | > 2048 MiB |
| M5 — dados transferidos por fluxo | ≤ 5 MiB | > 5 a 10 MiB | > 10 a 20 MiB | > 20 MiB |
| M14 — tempo de tarefa curta | ≤ 60 s | > 60 a 120 s | > 120 a 180 s | > 180 s |

**Justificativa e condições:**

- **M1:** os marcos de **1 s e 10 s** são referências de Nielsen para resposta interativa; **3 s é uma faixa intermediária proposta pelo estudo**. Medir resposta da interface, não o tempo de assistir a vídeos ou resolver exercícios; relatar mediana e P90.
- **M3–M4:** os limites de CPU são faixas operacionais propostas. Para M4, 512/1024/2048 MiB equivalem a cerca de 12,5%/25%/50% de um perfil de **4 GiB de RAM proposto pela equipe**. Antes da coleta, a capacidade efetivamente disponível no ambiente `A1` deverá ser registrada, e as faixas deverão ser ratificadas ou ajustadas pela equipe. Registrar também o consumo de outros processos.
- **M5:** os orçamentos de 5/10/20 MiB são propostas para **navegação e carregamento sem transferência integral de videoaulas**; usar fluxos equivalentes e mesma política de cache.
- **M14:** os limites de 60/120/180 s são propostos apenas para **tarefas curtas e padronizadas**, como localizar um curso. Não incluem tempo de aprendizagem do conteúdo ou resolução pedagógica.

## 4. Critérios técnicos de acessibilidade

- **M10 — ampliação:** verificar preservação de conteúdo e funcionalidade com **texto ampliado até 200%**, conforme **WCAG 2.1, critério 1.4.4 (AA)**, com suas exceções. A meta de **300%**, se testada, é um critério extra **do estudo**, não exigência desse item WCAG. O percentual agregado de M10 não substitui a verificação de cada barreira.
- **M11 — contraste:** classificar como **Alvo (2)** se todos os textos aplicáveis inspecionados cumprirem o **critério 1.4.3 da WCAG 2.1 (AA)**: 4,5:1 para texto comum e 3:1 para texto grande; como **Excelente (3)** se todos cumprirem o **critério 1.4.6 (AAA)**: 7:1 e 4,5:1, respectivamente; **1** se houver falha apenas em elemento não essencial e **0** se houver falha que comprometa informação essencial. Notas 0 ou 1 **não representam conformidade AA**. Registrar separadamente os testes de alto contraste.
- **M8–M9:** conclusão de tarefas com teclado ou leitor de tela deve ser confrontada com barreiras encontradas; sucesso agregado não comprova conformidade WCAG da plataforma inteira.

## 5. Regra de julgamento

Uma **questão** é considerada atendida quando seus indicadores principais atingem **nota 2 ou 3** e nenhuma tarefa essencial é impedida. A nota 1 indica atendimento apenas ao nível mínimo e **não** aprovação plena; resultados de indicadores complementares devem ser discutidos. Um **objetivo** é atendido quando todas as suas questões forem atendidas. As **hipóteses H1–H11** devem ser avaliadas conforme seus enunciados e evidências, e não apenas pela nota da métrica; podem ser sustentadas, não sustentadas ou inconclusivas.

| Objetivo | Questões | Métricas | Requisitos |
|---|---|---|---|
| G1 — eficiência de desempenho | Q1–Q4 | M1–M5 | R1–R2 |
| G2 — portabilidade | Q5–Q6 | M6–M7 | R3 |
| G3 — usabilidade | Q7–Q11 | M8–M14 | R4–R5 |

As faixas percentuais e os limites de CPU, memória, tráfego e tempo de tarefa são **propostas metodológicas**, não limites oficiais da ISO/IEC 25023 ou da WCAG. A equipe deve aprovar e registrar sua justificativa e as condições de aplicação **antes da coleta**; sem essa validação, o resultado permanece inconclusivo.

## Referências

> NIELSEN, Jakob. **Response times: the 3 important limits**. Nielsen Norman Group, 1 jan. 1993. Disponível em: <https://www.nngroup.com/articles/response-times-3-important-limits/>. Acesso em: 18 out. 2026.
> WORLD WIDE WEB CONSORTIUM (W3C). **Web Content Accessibility Guidelines (WCAG) 2.1**. W3C Recommendation, 6 maio 2025. Disponível em: <https://www.w3.org/TR/WCAG21/>. Acesso em: 18 out. 2026.

## Histórico de versões

| Versão | Data | Descrição | Responsável | Revisor |
|:---:|:---:|---|---|---|
| 1.0 | 18/10/2026 | Estruturação inicial dos critérios GQM. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho) |
| 1.1| 20/10/2026 | Consolidação das faixas e justificativas dos critérios de julgamento. | [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | [Pedro Lucas](https://github.com/Pwdrinho)  |
| 1.2 | 21/10/2026 | Correção da procedência das faixas de memória, mantidas como proposta metodológica sujeita à ratificação da equipe. | [Enzo Menali](https://github.com/menali17) | |
| 1.3 | 21/10/2026 | Padronização dos critérios de ampliação e contraste conforme a WCAG 2.1 adotada na Fase 1. | [Enzo Menali](https://github.com/menali17) | |
| 1.4 | 21/10/2026 | Ajustes na estrutura do artefato e referências | [Camila Cavalcante](https://github.com/CamilaSilvaC) |  |

---

[Navegar pela Fase 2](index.md)
