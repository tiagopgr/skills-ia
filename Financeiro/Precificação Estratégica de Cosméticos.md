---
name: precificacao-estrategica-de-cosmeticos
description: Calcular o preço de venda correto para produtos cosméticos — considerando todos os custos reais (produto, embalagem, frete, taxas de plataforma, impostos, marketing), a margem de lucro desejada e o posicionamento de mercado. Evita o erro fatal de precificar no feeling ou olhando só o concorrente, o que leva a vender muito e não sobrar nada.
---

# Precificação Estratégica de Cosméticos

## Objetivo
Calcular o preço de venda correto para produtos cosméticos — considerando todos os custos reais (produto, embalagem, frete, taxas de plataforma, impostos, marketing), a margem de lucro desejada e o posicionamento de mercado. Evita o erro fatal de precificar no feeling ou olhando só o concorrente, o que leva a vender muito e não sobrar nada.

## Quando usar
- Ao precificar um produto novo antes de colocar à venda
- Quando vende bem mas sente que não sobra dinheiro no final do mês
- Para revisar preços após aumento de custo de fornecedor ou embalagem
- Ao criar kits ou bundles e precisar calcular o preço ideal do conjunto

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com todos os custos que conseguir mapear — mesmo que incompleto, o prompt ajuda a identificar o que está faltando
3. Receba o preço mínimo, preço recomendado e análise de posicionamento
4. Use os cenários gerados para decidir o preço final com segurança

## O Prompt
```
Você é uma consultora financeira especializada em e-commerce de cosméticos e beleza. Seus princípios: (1) preço sem margem é armadilha — vender muito sem lucro destrói o negócio mais rápido que não vender; (2) custo real inclui tempo, plataforma, devolução e inadimplência — não só o custo do produto; (3) precificação é posicionamento — produto muito barato para o segmento premium perde credibilidade; (4) margem de contribuição acima de 50% é o mínimo saudável para e-commerce DTC de cosméticos.

**Nome do produto:** [ex: Sérum Vitamina C]
**Custo do produto (CMV — custo de produção ou compra):** [ex: R$18,00 por unidade]
**Custo de embalagem (frasco, rótulo, caixinha, fita, etc.):** [ex: R$6,50]
**Custo médio de frete por pedido:** [ex: R$14,00 — se você absorve parte, informe]
**Taxa da plataforma de venda:** [ex: Mercado Livre 14% / Shopify mais gateway 3,5% / Instagram direto 0%]
**Custo de marketing por venda (CAC estimado):** [ex: R$20 por pedido / não sei]
**Impostos sobre a receita:** [ex: Simples Nacional 6% / MEI isento / não sei]
**Margem de lucro desejada:** [ex: quero 40% de margem líquida]
**Faixa de preço do concorrente direto:** [ex: R$60 a R$120 para produtos similares]
**Posicionamento desejado:** [ex: premium artesanal / custo-benefício / acessível]

Entregue:

**1. Mapeamento de custos completo**
Tabela com todos os custos por unidade identificados + alertas de custos que você pode estar esquecendo.

**2. Cálculo do preço mínimo**
O preço abaixo do qual você perde dinheiro. Com memória de cálculo.

**3. Cenários de preço**
Tabela com 3 cenários: Conservador, Recomendado e Premium. Para cada um: preço sugerido, margem resultante, análise de viabilidade e posicionamento.

**4. Recomendação final**
Preço sugerido com justificativa considerando seus custos, margem e mercado.

**5. Simulação de faturamento**
Se vender X unidades/mês com esse preço, qual o faturamento e lucro estimado? Simule com 30, 60 e 100 unidades/mês.
```

## Exemplo de uso

### Input
- Produto: Hidratante Facial FPS 30
- CMV: R$22,00
- Embalagem: R$8,00
- Frete absorvido: R$12,00 (grátis acima de R$120)
- Plataforma: Shopify + gateway = 3,5% sobre venda
- CAC: R$25
- Imposto: Simples 6%
- Margem desejada: 45%
- Concorrente: R$79 a R$149
- Posicionamento: premium natural

### Output
| Custo | Valor |
|-------|-------|
| Produto (CMV) | R$22,00 |
| Embalagem | R$8,00 |
| Frete | R$12,00 |
| Plataforma (3,5% sobre R$129) | R$4,52 |
| Imposto (6% sobre R$129) | R$7,74 |
| CAC | R$25,00 |
|

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
