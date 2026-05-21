---
name: analise-de-ponto-de-equilibrio-break-even
description: Calcular o ponto de equilíbrio do negócio — o momento exato em que a receita cobre todos os custos — para definir metas mínimas de vendas, precificar corretamente e tomar decisões de investimento com segurança.
---

# Análise de Ponto de Equilíbrio (Break-even)

## Objetivo
Calcular o ponto de equilíbrio do negócio — o momento exato em que a receita cobre todos os custos — para definir metas mínimas de vendas, precificar corretamente e tomar decisões de investimento com segurança.

## Quando usar
- Ao lançar um produto ou serviço novo
- Para definir meta mínima de vendas mensal
- Antes de aumentar custos fixos (contratar, mudar de escritório)
- Em negociações de preço (saber até onde pode dar desconto)

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Insira seus custos e preços
3. Receba a análise completa com cenários
4. Use como referência para metas e decisões

## O Prompt
```
Você é um analista financeiro prático que sabe calcular e interpretar o ponto de equilíbrio. Quando o empresário sabe exatamente quantas vendas precisa para cobrir os custos, ele para de operar no escuro.

Faça a análise de ponto de equilíbrio para:

**Tipo de negócio:** [produto físico, digital, serviço, SaaS]
**Produto(s):** [liste com preço de venda de cada]
**Custo por unidade (variável):** [custo de produção, entrega, comissão]
**Custos fixos mensais:** [aluguel, salários, ferramentas, impostos fixos]
**Meta de lucro mensal:** [quanto quer lucrar além do break-even]

Entregue:
1. Cálculos fundamentais (margem de contribuição, break-even em unidades e R$)
2. Interpretação prática ("Você precisa vender X unidades por mês/dia")
3. Cenários (aumento de preço, redução de custos, desconto)
4. Break-even com meta de lucro
5. Margem de segurança (quanto acima do break-even está)
6. Recomendações
```

## Exemplo de uso

### Input
Tipo: Infoproduto (curso online)
Preço de venda: R$297
Custo variável por venda: R$45 (plataforma + imposto + afiliado)
Custos fixos mensais: R$8.500
Meta de lucro: R$10.000/mês

### Output
Margem de contribuição: R$297 - R$45 = R$252 por venda (84.8%)

Break-even: R$8.500 ÷ R$252 = 34 vendas/mês (R$10.098 de faturamento)
Isso é ~1.1 venda por dia ou ~8-9 por semana.

Com meta de lucro: (R$8.500 + R$10.000) ÷ R$252 = 74 vendas/mês

Cenário desconto 20%: Nova margem = R$192. Novo break-even = 45 vendas (+32%).
Desconto só vale se aumentar conversão em mais de 32%.

Margem de segurança (se vende 50/mês): 16 vendas acima do break-even (32%).

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
