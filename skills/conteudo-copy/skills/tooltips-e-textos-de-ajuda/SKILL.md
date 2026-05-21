---
name: tooltips-e-textos-de-ajuda
description: Criar tooltips, hints e textos de ajuda contextual para interfaces digitais que orientam o usuário sem interromper o fluxo — explicando funcionalidades, prevenindo erros e reduzindo a necessidade de suporte.
---

# Tooltips e Textos de Ajuda

## Objetivo
Criar tooltips, hints e textos de ajuda contextual para interfaces digitais que orientam o usuário sem interromper o fluxo — explicando funcionalidades, prevenindo erros e reduzindo a necessidade de suporte.

## Quando usar
- Ao projetar interfaces com funcionalidades não-óbvias
- Em configurações, dashboards e painéis administrativos
- Para funcionalidades novas que precisam de explicação
- Quando o suporte recebe perguntas repetitivas sobre a mesma feature

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste as funcionalidades que precisam de textos de ajuda
3. Receba tooltips e textos de apoio prontos
4. Implemente nos componentes de interface

## O Prompt
```
Você é um UX Writer especialista em ajuda contextual. O melhor texto de ajuda é aquele que o usuário nem percebe que está lendo — ele simplesmente entende e age. Seus princípios: (1) responda antes que perguntem, (2) seja breve — tooltip não é documentação, (3) use linguagem do usuário, (4) dê exemplos concretos.

Crie tooltips e textos de ajuda para:

**Produto:** [descreva o app/plataforma]
**Público:** [nível técnico — leigo, intermediário, avançado]
**Tom:** [casual, técnico, institucional]

**Funcionalidades/Elementos que precisam de tooltip:**
1. [ex: "Botão de exportar relatório — tem 3 formatos"]
2. [ex: "Campo de tags — aceita múltiplas, separadas por vírgula"]
3. [ex: "Toggle de 'modo público' — controla visibilidade"]
(liste de 5 a 15 elementos)

Para CADA elemento, entregue:

**Tooltip curto (max 15 palavras)**
**Tooltip expandido (max 40 palavras)**
**Exemplo prático**
**Placeholder (se for campo)**
**Nota de consequência (se ação tiver impacto)**
**Formato recomendado** (hover, info-icon, inline, banner, tour)

Ao final: Guia de escrita + Glossário de termos + Mapa de onde colocar ajuda
```

## Exemplo de uso

### Input
Produto: Dashboard de analytics de e-commerce
Público: Lojistas (nível intermediário)
Elementos: 1) Métrica "Taxa de conversão" 2) Filtro de período 3) Botão "Comparar períodos"

### Output
**Elemento 1 — Taxa de conversão:**

Tooltip curto: "Percentual de visitantes que finalizaram uma compra."

Tooltip expandido: "A taxa de conversão mostra quantos visitantes do seu site completaram uma compra. Calculada como: (pedidos ÷ sessões) × 100. A média do e-commerce brasileiro é 1.5-2%."

Exemplo: "Se 1.000 pessoas visitaram e 20 compraram, sua taxa é 2%."

Formato recomendado: Info-icon com popover ao lado da métrica.

---
**Tags:** Iniciante | Template | Conteúdo & Copy
