---
name: copy-para-empty-states-telas-vazias
description: Criar textos para telas vazias (empty states) de apps e plataformas que transformam momentos de 'vazio' em oportunidades de engajamento — orientando o usuário para a primeira ação.
---

# Copy para Empty States (Telas Vazias)

## Objetivo
Criar textos para telas vazias (empty states) de apps e plataformas que transformam momentos de 'vazio' em oportunidades de engajamento — orientando o usuário para a primeira ação.

## Quando usar
- Quando o usuário acessa uma seção pela primeira vez (sem dados)
- Em listas, dashboards e feeds sem conteúdo
- Após deletar todos os itens de uma seção
- Em resultados de busca sem matches

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste as telas do seu app que podem estar vazias
3. Receba copy + sugestão visual para cada empty state
4. Implemente como parte do design system

## O Prompt
```
Você é um UX Writer que sabe que telas vazias são momentos críticos — e negligenciados. Uma tela vazia mal feita ("Nenhum resultado encontrado.") gera confusão e abandono. Uma bem feita: (1) explica o que deveria aparecer ali, (2) mostra como começar, (3) motiva a primeira ação, (4) reforça o valor que o usuário terá.

Crie copy para empty states de:

**Produto/App:** [descreva]
**Tom da marca:** [casual, profissional, divertido, minimalista]
**Público:** [quem usa — nível de experiência]

**Telas com empty state:**
1. [ex: "Lista de projetos — nenhum projeto criado"]
2. [ex: "Inbox de mensagens — nenhuma mensagem"]
3. [ex: "Dashboard de analytics — sem dados ainda"]
4. [ex: "Busca sem resultados"]
(liste de 5 a 10 telas)

Para CADA tela, identifique o tipo: First-use | User-cleared | No results | Error

E entregue:

**Headline** (3 opções):
- Foco no que o usuário pode fazer
- Foco no valor que terá quando usar
- Foco em empatia/leveza

**Texto de apoio (1-2 frases)**
**CTA (botão)**
**Sugestão de ilustração**
**Versão alternativa para "user-cleared"** (se aplicável)

Ao final: Template padrão + Guia de consistência + Anti-patterns
```

## Exemplo de uso

### Input
Produto: Ferramenta de CRM para vendedores
Tom: Profissional e direto
Público: Vendedores e gerentes comerciais
Telas: 1) Pipeline de vendas vazio 2) Contatos — nenhum contato 3) Busca sem resultado

### Output
**Tela 1 — Pipeline vazio (first-use):**

Headlines:
- A (ação): "Monte seu pipeline em minutos"
- B (valor): "Aqui você acompanha cada negociação até o fechamento"
- C (empatia): "Todo grande vendedor começa com o primeiro deal"

Texto de apoio: "Adicione sua primeira oportunidade e acompanhe cada etapa. Você pode importar de uma planilha ou criar manualmente."

CTA: "Adicionar primeira oportunidade" | Link: "Importar planilha"

Sugestão de ilustração: Funil estilizado com uma seta entrando, estilo line-art.

---
**Tags:** Intermediário | Geração | Conteúdo & Copy
