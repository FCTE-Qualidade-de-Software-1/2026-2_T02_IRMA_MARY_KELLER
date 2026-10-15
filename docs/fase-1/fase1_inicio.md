# Fase 1 — Estabelecer Requisitos de Avaliação

Divisão das duplas
1.
2.
3.

Elaboração dos tópicos referente a Fase 1 entrega para dia 12/10/2026


## 1. Propósito da avaliação 

O propósito da avaliação é **analisar a qualidade do site da Khan Academy sob a perspectiva de usuários que utilizam a plataforma para fins educacionais**, considerando aspectos relacionados à facilidade de uso, à adaptação a diferentes ambientes de acesso e ao funcionamento conjunto com diferentes softwares e componentes.

A avaliação será orientada pelo modelo de qualidade da **ISO/IEC 25010**, sendo selecionadas as características **Usabilidade, Portabilidade e Compatibilidade**. A escolha considera tanto a relevância dessas características para uma plataforma educacional disponibilizada pela Web quanto a viabilidade de sua avaliação com os recursos e informações acessíveis à equipe.

O objetivo não será avaliar a qualidade geral da [Khan Academy](https://pt.khanacademy.org/), mas **delimitar e analisar aspectos observáveis dessas três características no produto disponível aos usuários**.

---

## 2. Tipo de produto

### 2.1 Produto avaliado

**Khan Academy — plataforma educacional online**

A Khan Academy é uma plataforma educacional acessível pela Web que disponibiliza conteúdos de aprendizagem, exercícios e outros recursos educacionais aos seus usuários.

### 2.2 Caracterização do produto

O produto pode ser caracterizado como uma **aplicação Web educacional**, acessada principalmente por meio de navegadores em computadores e dispositivos móveis.

Entre os recursos que podem fazer parte do escopo da avaliação estão:

- acesso à plataforma;
    
- navegação entre conteúdos;
    
- busca por conteúdos educacionais;
    
- acesso a cursos e aulas;
    
- reprodução de conteúdos multimídia;
    
- realização de exercícios;
    
- acompanhamento do progresso;
    
- utilização da plataforma em diferentes dispositivos e navegadores.
    

### 2.3 Escopo

O escopo será limitado à **interface e ao comportamento observável da plataforma disponibilizada aos usuários**, não abrangendo aspectos internos da infraestrutura da Khan Academy que não possam ser diretamente observados ou avaliados pela equipe.

Por exemplo, não será objetivo avaliar diretamente:

- arquitetura interna dos servidores;
    
- código-fonte proprietário;
    
- desempenho interno dos bancos de dados;
    
- segurança da infraestrutura;
    
- escalabilidade dos servidores;
    
- algoritmos internos.
    

Essa delimitação é importante porque a escolha das características deve considerar a **disponibilidade das informações necessárias para realizar a avaliação**.

---

## 3. Interessados (Stakeholders)

Para uma plataforma educacional como a Khan Academy, existem diferentes grupos interessados na qualidade do produto.

|Interessado|Interesse na qualidade|
|---|---|
|**Estudantes**|Conseguir acessar conteúdos, realizar atividades e acompanhar sua aprendizagem de maneira adequada|
|**Professores/educadores**|Utilizar a plataforma como apoio ao processo de ensino e aprendizagem|
|**Responsáveis**|Ter uma plataforma acessível e adequada para o uso educacional|
|**Khan Academy**|Garantir que a plataforma ofereça uma experiência adequada aos seus usuários|
|**Equipe de desenvolvimento**|Identificar problemas e oportunidades de melhoria no produto|
|**Equipe avaliadora**|Obter evidências para analisar as características de qualidade selecionadas|

Para esta avaliação, **estudantes/usuários da plataforma serão considerados os principais interessados**, pois as três características escolhidas possuem impacto direto na experiência de utilização do produto.

---

# 4. Modelo de qualidade

A avaliação será baseada no modelo de qualidade da **ISO/IEC 25010**, com foco nas características **Usabilidade, Portabilidade e Compatibilidade**.

A seleção das subcaracterísticas considera dois critérios principais:

1. **Relevância** para o contexto de uma plataforma educacional Web;
    
2. **Viabilidade**, considerando se a equipe possui acesso às informações e aos ambientes necessários para produzir evidências.
    

---

## 4.1 Usabilidade

A Usabilidade foi selecionada porque a Khan Academy é uma plataforma diretamente utilizada pelos usuários para realizar atividades educacionais. Portanto, aspectos relacionados à interação entre usuário e sistema podem ser observados diretamente pela equipe.

### Subcaracterísticas selecionadas

|Subcaracterística|Aplicação no contexto da Khan Academy|Viabilidade|
|---|---|---|
|**Reconhecimento de adequação**|Verificar se o usuário consegue compreender que a plataforma oferece os recursos necessários para suas atividades|Alta|
|**Aprendizibilidade**|Verificar a facilidade para um usuário aprender a utilizar as funcionalidades da plataforma|Alta|
|**Operabilidade**|Verificar se o usuário consegue operar e controlar as funcionalidades da plataforma adequadamente|Alta|

Essas subcaracterísticas são viáveis porque podem ser avaliadas por meio da **interação direta dos usuários com a plataforma**, sem necessidade de acesso ao código-fonte ou à infraestrutura interna.

Exemplos de aspectos observáveis:

- localizar um curso;
    
- iniciar uma aula;
    
- localizar um exercício;
    
- compreender como avançar no conteúdo;
    
- acompanhar o progresso;
    
- utilizar funcionalidades da plataforma.
    

---

## 4.2 Portabilidade

A Portabilidade foi selecionada porque a Khan Academy é uma aplicação Web utilizada em diferentes dispositivos e ambientes de acesso.

### Subcaracterística selecionada

#### Adaptabilidade

A avaliação poderá verificar a capacidade da plataforma de se adaptar a diferentes ambientes de acesso sem que sejam necessárias alterações no produto.

Podem ser considerados, por exemplo:

- computadores;
    
- smartphones;
    
- diferentes sistemas operacionais;
    
- diferentes tamanhos de tela;
    
- diferentes resoluções;
    
- diferentes navegadores.
    

A avaliação poderá observar:

- adaptação do layout;
    
- navegação;
    
- acesso às funcionalidades;
    
- visualização dos conteúdos;
    
- reprodução de mídia;
    
- realização de exercícios;
    
- interação com elementos da interface.
    

### Justificativa da seleção

A **Adaptabilidade** é a subcaracterística de Portabilidade mais viável para o contexto da avaliação, pois pode ser observada diretamente utilizando diferentes ambientes disponíveis para a equipe.

Outras subcaracterísticas relacionadas à instalação ou substituição são menos adequadas ao contexto, pois a Khan Academy é uma aplicação Web e não um software tradicional que precise ser instalado em diferentes sistemas operacionais.

---

## 4.3 Compatibilidade

A Compatibilidade deve ser diferenciada da Portabilidade.

Enquanto a Portabilidade estará concentrada na **adaptação da plataforma a diferentes ambientes**, a Compatibilidade será analisada considerando o funcionamento da Khan Academy **em conjunto com outros componentes, softwares ou sistemas**.

Na ISO/IEC 25010, a Compatibilidade envolve principalmente:

- **Coexistência**;
    
- **Interoperabilidade**.
    

### Subcaracterística 1 — Coexistência

Será avaliado se a Khan Academy consegue funcionar adequadamente compartilhando o ambiente com outros produtos ou componentes.

Podem ser considerados:

- outras abas abertas no navegador;
    
- diferentes aplicações executando simultaneamente;
    
- extensões do navegador;
    
- recursos de áudio e vídeo;
    
- diferentes configurações do navegador.
    

A questão central será:

> **A utilização simultânea de outros componentes do ambiente interfere no funcionamento da Khan Academy?**

Essa subcaracterística apresenta **alta viabilidade**, pois os testes podem ser realizados diretamente no ambiente de acesso da equipe.

### Subcaracterística 2 — Interoperabilidade

Será avaliado, dentro dos limites observáveis, se a Khan Academy consegue utilizar adequadamente recursos ou trocar informações com outros sistemas e componentes.

Podem ser observados, por exemplo:

- autenticação;
    
- recursos multimídia;
    
- links externos;
    
- mecanismos do navegador;
    
- armazenamento de informações no ambiente do usuário;
    
- comunicação com serviços necessários ao funcionamento da plataforma.
    

Entretanto, essa subcaracterística apresenta uma limitação: a equipe não possui necessariamente acesso às APIs e aos componentes internos da Khan Academy.

Por isso, a avaliação de Interoperabilidade deverá ficar restrita aos **aspectos observáveis externamente**.

---

# 5. Modelo de qualidade selecionado

A configuração proposta para a avaliação é:

|Característica|Subcaracterísticas|Justificativa|
|---|---|---|
|**Usabilidade**|Reconhecimento de adequação, Aprendizibilidade e Operabilidade|Podem ser avaliadas diretamente pela interação dos usuários com a plataforma|
|**Portabilidade**|Adaptabilidade|Pode ser observada comparando diferentes dispositivos, sistemas e ambientes de acesso|
|**Compatibilidade**|Coexistência e Interoperabilidade|Permitem avaliar o funcionamento da plataforma em conjunto com outros componentes e sistemas observáveis|

No total, serão avaliadas **3 características e 6 subcaracterísticas**.

---

# 6. Matriz de viabilidade

A viabilidade da avaliação deve ser considerada antes da execução dos testes, garantindo que a equipe consiga obter evidências suficientes para cada subcaracterística.

|Característica|Subcaracterística|Evidência necessária|Acesso da equipe|Viabilidade|
|---|---|---|---|---|
|Usabilidade|Reconhecimento de adequação|Interação do usuário|Sim|**Alta**|
|Usabilidade|Aprendizibilidade|Execução de tarefas|Sim|**Alta**|
|Usabilidade|Operabilidade|Execução de tarefas|Sim|**Alta**|
|Portabilidade|Adaptabilidade|Diferentes dispositivos/ambientes|Sim|**Alta**|
|Compatibilidade|Coexistência|Testes com outros componentes|Sim|**Alta**|
|Compatibilidade|Interoperabilidade|Interação com outros sistemas/componentes|Parcialmente|**Média**|

Essa matriz demonstra que a escolha das características não foi baseada apenas em sua relevância teórica, mas também na **possibilidade concreta de obtenção de evidências pela equipe**.

---

# 7. Limitações da avaliação

Algumas limitações devem ser consideradas na definição dos requisitos:

- a equipe não possui acesso ao código-fonte proprietário da Khan Academy;
    
- não será possível avaliar diretamente componentes internos da infraestrutura;
    
- a avaliação de Interoperabilidade ficará restrita aos comportamentos observáveis;
    
- a disponibilidade de dispositivos, sistemas operacionais e navegadores poderá limitar a quantidade de ambientes testados;
    
- os resultados representarão os ambientes e cenários efetivamente avaliados, não podendo ser generalizados automaticamente para todos os ambientes existentes.
    

Essas limitações devem ser registradas para evitar conclusões que ultrapassem as evidências obtidas.

---

# 8. Estrutura final da Fase 1

A Fase 1 poderá ser organizada no documento da seguinte maneira:

```
FASE 1 — ESTABELECER REQUISITOS DE AVALIAÇÃO

1. Propósito da avaliação
   - Objetivo
   - Contexto
   - Motivação

2. Tipo de produto
   2.1 Caracterização da Khan Academy
   2.2 Escopo da avaliação
   2.3 Limitações e informações acessíveis

3. Interessados
   3.1 Estudantes
   3.2 Professores
   3.3 Responsáveis
   3.4 Khan Academy/equipe de desenvolvimento
   3.5 Equipe avaliadora

4. Modelo de qualidade
   4.1 Usabilidade
       - Reconhecimento de adequação
       - Aprendizibilidade
       - Operabilidade

   4.2 Portabilidade
       - Adaptabilidade

   4.3 Compatibilidade
       - Coexistência
       - Interoperabilidade

5. Justificativa da seleção
   - Relevância
   - Viabilidade
   - Disponibilidade de evidências
   - Limitações

6. Matriz de requisitos de avaliação
```

## Síntese da decisão

A avaliação da Khan Academy será delimitada às características **Usabilidade, Portabilidade e Compatibilidade**, selecionadas por sua relevância para uma plataforma educacional Web e pela possibilidade de obtenção de evidências diretamente acessíveis à equipe.

A **Usabilidade** será avaliada por meio de aspectos diretamente relacionados à interação do usuário. A **Portabilidade** será concentrada na **Adaptabilidade** da plataforma a diferentes ambientes de acesso. A **Compatibilidade** será analisada por meio da **Coexistência** e, de forma limitada aos aspectos observáveis, da **Interoperabilidade**.

Essa delimitação busca garantir que as características escolhidas sejam **relevantes, observáveis e viáveis de avaliar** dentro do tempo e dos recursos disponíveis para a equipe.
