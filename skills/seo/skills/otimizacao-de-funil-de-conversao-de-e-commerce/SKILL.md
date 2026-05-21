---
name: otimizacao-de-funil-de-conversao-de-e-commerce
description: Diagnosticar o funil de conversão do e-commerce — da sessão até o pedido — para identificar onde estão os maiores vazamentos, gerar hipóteses testáveis e criar um plano de CRO (Conversion Rate Optimization) priorizado que o time consegue executar sem precisar de consultoria externa.
---

# Otimização de Funil de Conversão de E-commerce

## Objetivo
Diagnosticar o funil de conversão do e-commerce — da sessão até o pedido — para identificar onde estão os maiores vazamentos, gerar hipóteses testáveis e criar um plano de CRO (Conversion Rate Optimization) priorizado que o time consegue executar sem precisar de consultoria externa.

## Quando usar
- Quando a taxa de conversão está abaixo do benchmark do segmento
- Para criar um programa estruturado de otimização de conversão
- Antes de aumentar o investimento em tráfego — tráfego num funil furado é dinheiro perdido
- Para identificar o maior problema de conversão e resolvê-lo antes de tratar o próximo

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados do funil e o contexto da loja
3. Receba o diagnóstico completo com hipóteses e plano de testes priorizados
4. Execute os testes em ordem de prioridade e meça o impacto

## O Prompt
```
Você é um especialista em CRO (Conversion Rate Optimization) para e-commerce com experiência em diagnóstico de funil e testes A/B. Seus princípios: (1) a otimização mais impactante raramente é a mais glamourosa — muitas vezes é corrigir um bug de mobile ou simplificar o checkout, (2) hipótese sem dado é palpite — CRO bom começa com análise, não com solução, (3) testar tudo ao mesmo tempo invalida os resultados — um teste por vez, variável por vez, (4) taxa de conversão não é o único KPI de CRO — também importam: taxa de abandono por etapa, tempo na página, scroll depth e cliques em elementos.

Analise o funil de conversão e crie o plano de otimização:

**Dados do funil (últimos 30 dias):**
- Sessões totais: [número]
- Sessões em páginas de produto (PDPs): [número ou %]
- Taxa de adição ao carrinho: [%]
- Taxa de checkout iniciado: [%]
- Taxa de conversão final: [%]
- Taxa de abandono de carrinho: [%]
- Taxa de conversão mobile vs. desktop: [%]
- Principais fontes de tráfego e conversão por fonte: [dados]

**Dados qualitativos (se tiver):**
- Principais reclamações de clientes sobre a compra: [o que dizem]
- Páginas com maior taxa de saída: [quais páginas perdem visitantes]
- Resultados de pesquisas de satisfação ou NPS: [se tiver]

**Contexto técnico:**
- Plataforma: [Shopify, VTEX, Nuvemshop, WooCommerce]
- Tempo de carregamento médio: [segundos — mobile e desktop]
- Formas de pagamento disponíveis: [Pix, boleto, cartão, parcelamento]

**O que já foi testado e o resultado:** [para não repetir]

Entregue:

**1. Mapa do funil com taxa de conversão por etapa**
Visualização do funil com as taxas atuais e benchmark do segmento — identificação visual do maior gargalo.

**2. Diagnóstico dos top 3 problemas de conversão**
Para cada problema: evidência nos dados, impacto estimado na conversão e hipótese de causa.

**3. Plano de testes A/B priorizados (backlog de CRO)**
Lista de testes ordenados por: facilidade de implementação × impacto potencial. Para cada teste:
- Hipótese: "Se [mudarmos X], então [conversão Y vai melhorar] porque [razão Z]"
- O que testar (variável)
- Como medir o resultado
- Duração mínima do teste para significância estatística
- Responsável e esforço estimado

**4. Quick wins (melhorias sem teste que provavelmente funcionam)**
Ajustes com alta probabilidade de melhoria que não precisam de teste A/B — implementar esta semana.

**5. Simulação de impacto**
Se resolver o maior gargalo identificado, qual seria o impacto no faturamento mensal?
```

## Exemplo de uso

### Input
- Sessões: 45.000 / PDPs: 28.000 (62%) / Adição ao carrinho: 8% / Checkout iniciado: 4,2% / Conversão: 1,1% / Abandono carrinho: 74%
- Mobile: 0,7% conversão / Desktop: 1,9%
- Maior reclamação: Frete caro e calculado só no checkout
- Página com mais saída: Checkout (passo de pagamento)
- Plataforma: Shopify / Carregamento mobile: 4,2s
- Pagamento: Cartão, Pix, boleto (parcelamento com juros acima de 2x)
- Testado antes: Adicionamos banner de frete grátis na home — não moveu conversão

### Output
>

---
**Tags:** Avançado | Análise | SEO, Analítica & Dados
