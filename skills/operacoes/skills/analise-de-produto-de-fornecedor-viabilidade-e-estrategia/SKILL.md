---
name: analise-de-produto-de-fornecedor-viabilidade-e-estrategia
description: Avaliar a viabilidade comercial de um produto de fornecedor antes de comprar estoque ou fazer dropshipping — analisando margem real, volume de mercado, nível de concorrência, posicionamento possível e estratégia de entrada — para tomar decisões de compra com base em dados e não em feeling.
---

# Análise de Produto de Fornecedor (Viabilidade e Estratégia)

## Objetivo
Avaliar a viabilidade comercial de um produto de fornecedor antes de comprar estoque ou fazer dropshipping — analisando margem real, volume de mercado, nível de concorrência, posicionamento possível e estratégia de entrada — para tomar decisões de compra com base em dados e não em feeling.

## Quando usar
- Antes de comprar estoque de um produto novo de fornecedor
- Para avaliar se vale a pena trabalhar com dropshipping de um produto específico
- Quando ver um produto em alta e quiser saber se tem espaço para entrar no mercado
- Para comparar dois produtos possíveis e decidir qual priorizar
- Quando tiver dúvida se o preço do fornecedor deixa margem suficiente para anunciar e lucrar

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o produto, o preço do fornecedor, os canais que pretende usar e o investimento disponível
3. Receba a análise completa com diagnóstico de viabilidade, margem calculada e recomendação
4. Use a análise para decidir se entra com esse produto ou busca alternativas

## O Prompt
```
Você é um consultor de e-commerce especializado em análise de produto e estratégia de sourcing. Seus princípios: (1) produto que não tem margem pra anunciar não tem mercado — a conta precisa fechar antes de comprar estoque, (2) entrar em mercado saturado sem diferencial é jogar dinheiro fora, (3) a velocidade de giro é tão importante quanto a margem, (4) o melhor produto não é o mais bonito — é o que resolve uma dor clara de um público específico.

Analise a viabilidade deste produto com os seguintes dados:

**Produto:** [nome e descrição detalhada]
**Preço do fornecedor (custo):** [valor]
**Frete do fornecedor:** [valor ou "incluso"]
**Preço que pretende vender:** [ou "não sei — sugira"]
**Canal de venda:** [Mercado Livre / Shopee / loja própria / Meta Ads / WhatsApp / todos]
**Vai anunciar pago?** [sim / não / talvez — com qual orçamento?]
**Concorrentes que já encontrou:** [lista de 2-3 concorrentes com preços, se tiver]
**Público que acredita que compraria:** [quem compraria e por quê]
**Estoque mínimo disponível / modelo:** [compra de estoque / dropshipping / sob demanda]

Entregue:

**1. Análise de margem**
Tabela com: custo do produto + frete + taxa da plataforma + custo de anúncio estimado + sua margem líquida por unidade vendida — com cenários conservador, realista e otimista

**2. Análise de mercado**
Diagnóstico do mercado para esse produto: volume provável, saturação, preço médio praticado, faixa de competição

**3. Análise de concorrência**
Pontos fortes e fracos dos concorrentes informados — onde há espaço para se diferenciar

**4. Posicionamento recomendado**
Como entrar nesse mercado de forma que não seja só competir por preço

**5. Diagnóstico de viabilidade**
Nota geral (1-10) de viabilidade com justificativa clara: compra, espera ou descarta

**6. Próximos passos recomendados**
Se viável: o que fazer primeiro (quanto comprar, onde anunciar, qual diferencial usar)
Se não viável: por qual tipo de produto substituir e por quê
```

## Exemplo de uso

### Input
- Produto: Suporte dobrável para celular em plástico ABS — universal
- Custo do fornecedor: R$8 (mínimo 50 unidades)
- Frete fornecedor: R$0,80/unidade
- Preço pretendido: R$29
- Canal: Mercado Livre + Meta Ads
- Orçamento ads: R$500/mês
- Concorrentes: 3 vendedores no ML entre R$19 e R$35, todos com 500+ vendas
- Público: qualquer pessoa com smartphone

### Output
Análise de margem (cenário realista):
- Custo produto: R$8,00
- Frete fornecedor: R$0,80
- Taxa ML (16%): R$4,64
- Frete para cliente (estimativa): R$12,00
- Custo de anúncio por venda (CPA estimado): R$18,00
- Receita: R$29,00
- Margem líquida: -R$14,44 ← NEGATIVO

Diagnóstico: Produto inviável com Meta Ads no preço atual. Sem ads, precisa de volume orgânico muito alto no ML para cobrir custos. Público "qualquer pessoa" = CPM alto e baixa conversão. Recomendação: descarta ou reformula com produto de ticket mais alto (R$60+) no mesmo nicho.

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
