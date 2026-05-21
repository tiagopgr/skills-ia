---
name: analise-de-margem-por-produtoservico
description: Calcular e analisar a margem de contribuição e a rentabilidade real de cada produto ou serviço — identificando quais geram lucro de verdade e onde focar esforço para maximizar o resultado.
---

# Análise de Margem por Produto/Serviço

## Objetivo
Calcular e analisar a margem de contribuição e a rentabilidade real de cada produto ou serviço — identificando quais geram lucro de verdade e onde focar esforço para maximizar o resultado.

## Quando usar
- Na revisão de portfólio de produtos/serviços
- Para decidir quais produtos escalar e quais descontinuar
- Em decisões de precificação e promoções
- No planejamento financeiro trimestral/anual

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste seus produtos com preços e custos
3. Receba a análise completa de rentabilidade
4. Tome decisões baseadas em margem, não só faturamento

## O Prompt
```
Você é um analista financeiro que sabe que faturamento é vaidade e lucro é sanidade. Muitas empresas focam no produto que mais vende sem perceber que é o que menos dá lucro.

Analise a margem dos seguintes produtos/serviços:

**Empresa:** [nome e setor]
**Faturamento total mensal:** [valor]

**Produto/Serviço 1:**
- Nome: [nome]
- Preço de venda: [valor]
- Unidades vendidas/mês: [quantidade]
- Custos diretos: [custo de produção, entrega, plataforma, comissão]
- Tempo de execução: [horas — para serviços]

(liste de 3 a 8 produtos)

**Custos fixos totais:** [valor mensal]
**Custo hora da equipe:** [se for serviço]

Entregue:
1. Análise por produto (margem em R$ e %, R$/hora)
2. Tabela comparativa (ranking por margem)
3. Matriz BCG simplificada (Estrela, Vaca leiteira, Interrogação, Abacaxi)
4. Rateio de custos fixos
5. Insights e alertas
6. Recomendações (top 3 ações)
7. Simulações (aumento de preço, descontinuação)
```

## Exemplo de uso

### Input
Empresa: Agência de design
Produtos:
- Logo: R$2.500, 8/mês, 15h cada
- Social media: R$1.500/mês, 12 clientes, 20h/mês cada
- Branding completo: R$12.000, 2/mês, 60h cada
Custos fixos: R$25.000/mês
Custo hora equipe: R$45

### Output
| Produto | Receita | Margem | R$/hora | Class. |
| Branding | R$24K | 67% (R$16K) | R$267/h | Estrela |
| Logo | R$20K | 73% (R$14.6K) | R$122/h | Estrela |
| Social media | R$18K | 40% (R$7.2K) | R$30/h | Abacaxi |

Insight: Social media gera R$18K de faturamento (parece bom) mas apenas R$30/hora — menos que o custo hora. É o "produto vaidade".

Recomendação #1: Aumentar preço de social media para R$2.200 ou reduzir horas.
Recomendação #2: Investir em marketing para vender mais Branding (maior R$/hora).

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
