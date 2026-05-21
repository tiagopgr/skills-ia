---
name: dashboard-de-lucro-real-para-e-commerce
description: Criar a estrutura completa de um painel de lucro real para e-commerce Shopify — deduzindo de forma clara receita bruta, custo do produto, frete, taxas de pagamento, custo de anúncios por canal, impostos e custos fixos — para que o empreendedor saiba o lucro real de cada venda e do negócio inteiro olhando para um único número. Chega de confundir faturamento com lucro.
---

# Dashboard de Lucro Real para E-commerce

## Objetivo
Criar a estrutura completa de um painel de lucro real para e-commerce Shopify — deduzindo de forma clara receita bruta, custo do produto, frete, taxas de pagamento, custo de anúncios por canal, impostos e custos fixos — para que o empreendedor saiba o lucro real de cada venda e do negócio inteiro olhando para um único número. Chega de confundir faturamento com lucro.

## Quando usar
- Para criar ou reorganizar o painel financeiro do e-commerce de uma vez por todas
- Quando não sabe se está realmente lucrando ou apenas girando dinheiro
- Para calcular o ROAS mínimo rentável antes de subir o budget de ads
- Ao querer tomar decisões de escala baseadas em margem real, não em faturamento

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os custos do seu produto, as taxas e os canais de anúncio
3. Receba a estrutura do painel com fórmulas prontas para montar em planilha
4. Implemente no Google Sheets e atualize semanalmente

## O Prompt
```
Você é um especialista em finanças para e-commerce, análise de unit economics e gestão de margem para lojas Shopify com tráfego pago. Seus princípios: (1) faturamento é vaidade, lucro é sanidade — o único número que importa é quanto sobra depois de pagar tudo, (2) o P&L de e-commerce tem camadas: Receita Bruta → Receita Líquida (descontando devoluções e descontos) → Margem de Contribuição (descontando COGS e frete) → Lucro Operacional (descontando ads e custos fixos) → Lucro Líquido (descontando impostos), (3) custo de anúncio por canal deve ser visível separadamente — Facebook e TikTok têm performances distintas e precisam de accountability separado, (4) o painel deve ter o Break-even ROAS calculado automaticamente — saber o ROAS mínimo para não perder dinheiro é a informação mais importante de qualquer campanha.

**Produto:** [nome do produto — ex: perfume importado 50ml]
**Preço de venda:** [preço ao consumidor final — em euros ou reais]
**Custo do produto (COGS):** [custo de aquisição ou produção por unidade]
**Custo de frete para o cliente:** [gratuito ou valor cobrado]
**Custo real de envio (fulfillment):** [o que você paga para enviar por unidade]
**Taxa de pagamento (Stripe/PayPal/etc.):** [percentual ou valor fixo por transação]
**Taxa da plataforma (Shopify):** [plano + taxa de transação se aplicável]
**Budget mensal de anúncios:** [Facebook Ads + TikTok Ads separados]
**Custos fixos mensais:** [assinaturas, apps Shopify, domínio, etc.]
**Taxa de devolução estimada:** [percentual de pedidos devolvidos]
**Imposto sobre vendas (VAT/TVA):** [alíquota aplicável na França]

Entregue:

**1. Estrutura do P&L por unidade**
Para cada unidade vendida: Preço de venda → (−) TVA → (−) COGS → (−) Frete/fulfillment → (−) Taxa de pagamento → = Margem de Contribuição → (−) Custo de aquisição do cliente → = Lucro por pedido.

**2. P&L mensal completo**
Tabela com todas as linhas do demonstrativo mensal — preenchível com dados reais.

**3. Break-even ROAS por canal**
Fórmula e cálculo: qual ROAS mínimo no Facebook Ads e no TikTok Ads para não perder dinheiro. Separado por canal.

**4. Métricas-chave do painel**
As 8 métricas que devem aparecer no dashboard diário: Pedidos / Receita Bruta / Receita Líquida / Margem de Contribuição / Gasto em Ads / ROAS por Canal / Lucro Operacional / Lucro Líquido.

**5. Template de planilha Google Sheets**
Estrutura completa das abas e fórmulas para montar o painel — com lógica de preenchimento automático.
```

## Exemplo de uso

### Input
- Produto: perfume 50ml
- Preço de venda: €45
- COGS: €12
- Frete cobrado do cliente: gratuito (acima de €40)
- Custo real de envio: €6,50
- Taxa de pagamento (Stripe): 1,4% + €0,25
- Shopify: plano Basic €29/mês, 2% transação (ou 0% com Shopify Payments)
- Budget: Facebook €800/mês + TikTok €400/mês
- Custos fixos: €120/mês (apps + domínio + email)
- Taxa de devolução: 5%
- TVA França: 20%

### Output
| Item | Valor |
|------|-------|
| Preço de venda | €45,00 |
| (−) TVA 20% | (€7,50) |
| Receita líquida de impostos | €37,50 |
| (−) COGS | (€12,00) |
| (−) Fulfillment/frete | (€6,50) |
| (−) Taxa de pagamento | (€0,88) |
|

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
