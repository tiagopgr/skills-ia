---
name: acessibilidade-web-wcag-checklist
description: Auditar e corrigir problemas de acessibilidade em interfaces web seguindo as diretrizes WCAG 2.1 — garantindo que pessoas com deficiências consigam usar o produto — para ampliar o público, cumprir requisitos legais e criar uma experiência inclusiva.
---

# Acessibilidade Web (WCAG Checklist)

## Objetivo
Auditar e corrigir problemas de acessibilidade em interfaces web seguindo as diretrizes WCAG 2.1 — garantindo que pessoas com deficiências consigam usar o produto — para ampliar o público, cumprir requisitos legais e criar uma experiência inclusiva.

## Quando usar
- Antes de lançar um site ou app
- Em auditorias periódicas de acessibilidade
- Quando receber feedback de usuários com deficiência
- Para cumprir requisitos legais (Lei Brasileira de Inclusão, ADA)

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o site/app ou cole trechos do HTML
3. Receba a auditoria completa com correções
4. Implemente as correções por prioridade

## O Prompt
```
Você é um especialista em acessibilidade web que audita interfaces seguindo WCAG 2.1 nível AA. Você sabe que: (1) acessibilidade não é feature — é requisito, (2) 15% da população mundial tem alguma deficiência, (3) boas práticas de acessibilidade melhoram a UX para TODOS, (4) a maioria dos problemas é simples de corrigir. Você prioriza impacto real sobre conformidade burocrática.

Faça a auditoria de acessibilidade para:

**Tipo de interface:** [site, web app, e-commerce, dashboard, landing page]
**Stack frontend:** [HTML/CSS, React, Vue, Angular]
**URL ou código:** [cole URL ou trechos do HTML para análise]
**Público:** [quem usa — incluir se há usuários com deficiências conhecidas]
**Componentes interativos:** [formulários, modais, dropdowns, carrosséis, tabelas]
**Status atual:** [nunca auditado, parcialmente acessível, em conformidade]

Avalie usando o checklist WCAG 2.1 AA:

**1. Perceptível** - Alt text, legendas, contraste, redimensionamento
**2. Operável** - Teclado, foco visível, skip links, animações
**3. Compreensível** - Idioma, labels, erros claros, navegação consistente
**4. Robusto** - HTML semântico, ARIA roles, aria-live

**Resumo:** Nível atual, problemas críticos/sérios/melhorias, prioridades.
**Código corrigido:** Antes e depois para cada problema.
**Ferramentas:** Lista de ferramentas para validar correções.
```

## Exemplo de uso

### Input
Tipo: E-commerce (listagem de produtos + checkout)
Stack: React + Tailwind CSS
Problemas conhecidos: botões sem label, imagens sem alt, formulário difícil com leitor de tela

### Output
**Problema crítico 1 — Botão sem label:**
<!-- ANTES (inacessível) -->
<button class="bg-blue-500 p-2" onclick="addToCart(id)">
  <svg>...</svg>
</button>

<!-- DEPOIS (acessível) -->
<button
  class="bg-blue-500 p-2"
  onclick="addToCart(id)"
  aria-label="Adicionar Camiseta Básica ao carrinho"
>
  <svg aria-hidden="true">...</svg>
</button>

**Problema crítico 2 — Imagem sem alt:**
<!-- ANTES -->
<img src="produto.jpg" />

<!-- DEPOIS -->
<img src="produto.jpg" alt="Camiseta branca básica de algodão, modelo unissex, vista frontal" />

**Ferramentas:** axe DevTools, WAVE, Lighthouse (Accessibility), NVDA (leitor de tela gratuito).

---
**Tags:** Intermediário | Auditoria | Código, Dev & Automação
