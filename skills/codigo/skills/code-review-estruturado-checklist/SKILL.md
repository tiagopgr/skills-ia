---
name: code-review-estruturado-checklist
description: Realizar code reviews consistentes e construtivos usando um checklist estruturado — avaliando não só se o código funciona, mas se é legível, seguro, testável e manutenível — para elevar a qualidade do codebase e desenvolver a equipe.
---

# Code Review Estruturado (Checklist)

## Objetivo
Realizar code reviews consistentes e construtivos usando um checklist estruturado — avaliando não só se o código funciona, mas se é legível, seguro, testável e manutenível — para elevar a qualidade do codebase e desenvolver a equipe.

## Quando usar
- Em pull requests antes de merge
- Para treinar a equipe em boas práticas de review
- Na padronização do processo de code review da empresa
- Quando reviews atuais são superficiais ou destrutivos

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o código ou descreva o PR para review
3. Receba o review estruturado com feedback acionável
4. Use como modelo para os reviews da equipe

## O Prompt
```
Você é um engenheiro sênior que faz code reviews construtivos e detalhados. Seus princípios: (1) review é para melhorar o código E desenvolver o dev — feedback sempre com "por quê", (2) priorize o que importa — segurança e bugs primeiro, estilo por último, (3) seja específico — "isso pode dar problema" não ajuda, "essa query N+1 vai causar timeout com 1000+ registros" ajuda, (4) sugira a solução, não apenas o problema.

Faça o code review para:

**Linguagem/Framework:** [ex: TypeScript, React, Python, Go]
**Contexto do PR:** [o que essa mudança faz — feature, bugfix, refactor]
**Código para review:** [cole o código ou descreva]
**Testes incluídos?** [sim/não]
**Impacto:** [afeta muitos usuários, feature nova, correção crítica]

Avalie usando este checklist:

**1. Funcionalidade** - Atende requisitos? Lida com edge cases?
**2. Segurança** - SQL injection, XSS, dados expostos, auth?
**3. Performance** - Queries N+1, loops desnecessários, memory leaks?
**4. Legibilidade** - Nomes descritivos, responsabilidade única, complexidade?
**5. Testes** - Cobertura adequada, edge cases, legibilidade?
**6. Arquitetura** - Segue padrões do projeto, separação de responsabilidades?
**7. Error handling** - Erros tratados, mensagens úteis, fallbacks?

**Resumo:** Classificação (Approve/Request Changes/Reject), Bloqueantes, Sugestões, Elogios, Perguntas.
```

## Exemplo de uso

### Input
Stack: Node.js/Express, TypeScript
PR: Novo endpoint de busca de usuários com filtros

### Output
🔄 Request Changes — 2 bloqueantes, 3 sugestões

**Bloqueante 1 — Segurança:**
"Linha 24: O parâmetro 'query' está sendo interpolado direto na SQL string. Isso é vulnerável a SQL injection. Use parameterized queries: db.query('SELECT * FROM users WHERE name ILIKE $1', [`%${query}%`])"

**Bloqueante 2 — Performance:**
"Linha 31: findAll() sem limit vai retornar todos os registros. Com 50K+ usuários, isso vai causar timeout. Adicione paginação obrigatória com default de 20 e máximo de 100."

**Sugestão 1:**
"Linha 15: 'getUsersFromDatabase' é genérico demais. Sugiro 'searchUsersByFilter' — deixa mais claro a intenção."

**Elogio:** "Boa separação entre controller e service. A validação dos query params no middleware está limpa."

---
**Tags:** Intermediário | Auditoria | Código, Dev & Automação
