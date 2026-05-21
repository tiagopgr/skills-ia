---
name: framework-de-unit-economics
description: Calcular e interpretar os unit economics completos do e-commerce — CAC (Custo de Aquisição de Cliente) por canal, LTV (Lifetime Value), payback period, margem de contribuição e ponto de equilíbrio — para tomar decisões de quanto investir em ads, quando escalar e qual canal priorizar com base em matemática, não em intuição. Para e-commerce solo, conhecer seus unit economics é a diferença entre crescer de forma sustentável e queimar caixa sem perceber.
---

# Framework de Unit Economics

## Objetivo
Calcular e interpretar os unit economics completos do e-commerce — CAC (Custo de Aquisição de Cliente) por canal, LTV (Lifetime Value), payback period, margem de contribuição e ponto de equilíbrio — para tomar decisões de quanto investir em ads, quando escalar e qual canal priorizar com base em matemática, não em intuição. Para e-commerce solo, conhecer seus unit economics é a diferença entre crescer de forma sustentável e queimar caixa sem perceber.

## Quando usar
- Para calcular se o negócio tem unit economics saudáveis antes de escalar
- Quando quer saber qual canal (Facebook vs TikTok) tem melhor CAC e LTV
- Para definir o orçamento máximo de aquisição por cliente que ainda é lucrativo
- Ao querer apresentar os números do negócio de forma clara para si mesmo ou para um sócio/investidor

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os dados de receita, custos e comportamento de recompra dos clientes
3. Receba o cálculo completo com interpretação e recomendações
4. Use os números resultantes para calibrar seus bids e budget de ads

## O Prompt
```
Você é um especialista em finanças para e-commerce DTC (direct-to-consumer) com foco em unit economics e métricas de crescimento sustentável. Seus princípios: (1) o CAC só faz sentido em relação ao LTV — um CAC de €20 é ótimo se o LTV for €120 e insustentável se o LTV for €40, (2) LTV de e-commerce de produto único depende da taxa de recompra — mesmo sem produto de recorrência, clientes que compram 2x valem 2x mais do que clientes que compram 1x, (3) o payback period ideal para e-commerce DTC é menor que 3 meses — payback de 6 meses ou mais exige muito caixa para crescer, (4) LTV:CAC ratio saudável para e-commerce: > 3:1 (sustentável), > 5:1 (excelente), < 2:1 (problemático — ou margem baixa ou CAC alto demais).

**Produto e preço de venda:** [nome + preço]
**Margem de contribuição por unidade:** [receita líquida − COGS − frete − taxas de pagamento]
**Gasto em ads (último mês):** [Facebook + TikTok separados]
**Número de compras geradas (último mês):** [por canal, se souber]
**Novos clientes vs. clientes recorrentes:** [percentual de recompras se souber]
**Ticket médio:** [valor médio por pedido]
**Taxa de recompra estimada:** [% de clientes que compram uma segunda vez e em que prazo]
**Custo fixo mensal:** [todos os custos que não variam com o volume de vendas]

Entregue:

**1. Cálculo do CAC por canal**
CAC = Gasto em ads / Número de novos clientes. Separado por Facebook e TikTok.

**2. Cálculo do LTV**
LTV básico (1ª compra) e LTV projetado (com taxa de recompra estimada). Fórmula e resultado.

**3. Ratio LTV:CAC**
Resultado e interpretação: saudável / atenção / crítico — com o que isso significa para o negócio.

**4. Payback Period**
Em quantos meses o CAC de um cliente é recuperado com a margem gerada por ele.

**5. CAC Máximo Permitido**
O CAC máximo que você pode pagar por cliente e ainda ser lucrável — por canal e por scenario (LTV 1x compra vs LTV com recompra).

**6. Alavancas para melhorar os unit economics**
As 3 ações com maior impacto: aumentar LTV (programas de recompra, email) / reduzir CAC (melhorar criativos, CRO) / aumentar margem (negociar COGS, retirar frete gratuito).
```

## Exemplo de uso

### Input
- Produto: perfume 50ml — €45
- Margem de contribuição: €18,12/unidade (calculada anteriormente)
- Gasto ads último mês: Facebook €800 + TikTok €400 = €1.200 total
- Compras: 26 total (15 Facebook, 11 TikTok) — assumindo todos novos clientes
- Recompras: estimado 15% compram 2ª vez em 6 meses
- Ticket médio: €45
- Custo fixo mensal: €120

### Output
| Métrica | Facebook | TikTok | Total |
|---------|---------|--------|-------|
| Gasto | €800 | €400 | €1.200 |
| Compras | 15 | 11 | 26 |
| CAC | €53,3 | €36,4 | €46,2 |
| ROAS | 1,69x | 1,74x | 1,72x |

>

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
