---
name: otimizacao-de-pagina-shopify-cro
description: Auditar e otimizar a taxa de conversão (CVR) da página de produto Shopify — identificando os elementos que criam fricção no processo de compra e gerando um plano de ação priorizado por impacto — para extrair mais vendas do mesmo volume de tráfego sem precisar aumentar o budget de ads. Um aumento de 1% para 2% na CVR dobra as vendas sem gastar mais um euro em anúncios.
---

# Otimização de Página Shopify (CRO)

## Objetivo
Auditar e otimizar a taxa de conversão (CVR) da página de produto Shopify — identificando os elementos que criam fricção no processo de compra e gerando um plano de ação priorizado por impacto — para extrair mais vendas do mesmo volume de tráfego sem precisar aumentar o budget de ads. Um aumento de 1% para 2% na CVR dobra as vendas sem gastar mais um euro em anúncios.

## Quando usar
- Quando o CTR dos ads é bom mas a CVR da página está baixa
- Para revisar a página de produto antes de escalar o budget de ads
- Ao lançar um produto novo — para garantir que a página está pronta para converter
- Para auditar periodicamente e identificar o que testar a seguir

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a estrutura atual da página ou cole o conteúdo/link
3. Receba o diagnóstico completo com o que mudar e em que ordem
4. Implemente as mudanças por prioridade e monitore a CVR nos 7 dias seguintes

## O Prompt
```
Você é um especialista em CRO (Conversion Rate Optimization) para e-commerce Shopify com foco em produtos de nicho no mercado europeu. Seus princípios: (1) CVR de página de produto de e-commerce europeu varia entre 1,5% e 4% para produtos de €40-80 — abaixo disso há problema identificável na página, (2) a hierarquia de elementos por impacto na CVR: imagens do produto (maior) → preço + proposta de valor → reviews → descrição → FAQ → garantias → confiança (menor, mas cumulativo), (3) fricção de compra tem causas técnicas (velocidade, mobile) e de copy (dúvida não resolvida, objeção não tratada, falta de urgência) — ambas precisam ser auditadas, (4) o primeiro A/B test de CRO deve ser sempre na headline acima do botão — é o elemento de maior visibilidade com menor custo de teste.

**URL da loja / produto:** [opcional — ou descreva a estrutura]
**Estrutura atual da página:**
- Imagens: [quantas, tipos — produto puro, detalhes, lifestyle, contexto de uso]
- Título do produto: [como está escrito]
- Preço: [valor e como é apresentado]
- Descrição curta (acima do botão): [texto atual]
- Botão de compra: [texto e cor]
- Descrição longa: [o que inclui]
- Reviews: [tem? quantos? com fotos?]
- Garantias/trust badges: [o que tem — frete grátis, devolução, pagamento seguro]
- FAQ: [tem? quais perguntas?]

**Métricas atuais da página:**
- CVR: [%]
- Bounce rate: [%]
- Add to cart rate: [%]
- Tempo médio na página: [segundos]
- % mobile vs desktop: [%]

Entregue:

**1. Diagnóstico por elemento da página**
Para cada elemento: nota de 1 a 10 e o principal problema identificado.

**2. Top 5 mudanças de maior impacto na CVR**
Em ordem de impacto: o que mudar, como mudar e resultado esperado em CVR.

**3. Checklist de confiança (trust)**
O que está faltando ou pode ser melhorado para aumentar a confiança do comprador europeu.

**4. Plano de testes A/B**
3 elementos para testar em sequência — com variante de controle e variante de teste.

**5. Checklist mobile**
A página está otimizada para mobile? 5 pontos críticos a verificar — importante porque TikTok Ads gera >80% de tráfego mobile.
```

## Exemplo de uso

### Input
- Imagens: 3 (frasco fundo branco, close detalhe tampa, imagem lifestyle mesa de madeira)
- Título: "Oud Parisien — Eau de Parfum"
- Preço: €45 (sem âncora, sem frete mencionado)
- Descrição curta: "Un parfum oriental boisé, avec des notes de oud et cuir." (1 linha)
- Botão: "Ajouter au panier" — cor preta
- Sem reviews, sem FAQ, sem trust badges
- CVR: 1,3% / ATC rate: 8% / Mobile: 78%

### Output
| # | Elemento | Problema | Mudança | Impacto estimado CVR |
|---|---------|---------|---------|---------------------|
| 1 | Descrição curta (acima do botão) | 1 linha técnica não cria desejo nem urgência | Substituir por: "Tenue 12-14h. Formulé artisanalement. €45 livraison offerte." | +0,3-0,5% |
| 2 | Trust badges | Nenhum elemento de confiança visível antes do botão | Adicionar: ✅ Livraison suivie offerte / ✅ Retour 30 jours / ✅ Paiement sécurisé | +0,2-0,4% |
| 3 | Sem reviews | Comprador europeu não compra sem prova social | Adicionar 5-10 reviews reais (ou solicitar ativamente a compradores) | +0,3-0,5% |
| 4 | Sem âncora de preço | €45 parece muito sem comparação | Adicionar: "Parfums de niche équivalents: €80-150. Notre prix: €45." | +0,1-0,3% |
| 5 | Apenas 3 imagens | Produto sem imagem em uso/contexto real reduz imaginação | Adicionar imagem de mão segurando o frasco + lifestyle masculino | +0,1-0,2% |

---
**Tags:** Intermediário | Auditoria | Produto, E-commerce & SaaS
