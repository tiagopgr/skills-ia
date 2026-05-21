---
name: diagnostico-de-funil-identificar-gargalos
description: Analisar um funil de vendas existente para identificar exatamente onde estão os gargalos que impedem o crescimento — calculando as taxas de conversão entre cada etapa, comparando com benchmarks e priorizando as correções de maior impacto.
---

# Diagnóstico de Funil (Identificar Gargalos)

## Objetivo
Analisar um funil de vendas existente para identificar exatamente onde estão os gargalos que impedem o crescimento — calculando as taxas de conversão entre cada etapa, comparando com benchmarks e priorizando as correções de maior impacto.

## Quando usar
- Quando o funil tem tráfego mas não gera vendas suficientes
- Para decidir onde investir esforço de otimização
- Em revisões mensais/trimestrais de performance
- Antes de aumentar investimento em tráfego

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Insira os números do seu funil
3. Receba o diagnóstico com os gargalos identificados
4. Priorize as correções de maior impacto

## O Prompt
```
Você é um analista de funis de vendas que diagnostica gargalos como um médico diagnostica doenças — com dados, não achismo. Você sabe que: (1) a maioria otimiza o lugar errado, (2) melhorar a pior taxa gera mais resultado, (3) pequenas melhorias se multiplicam.

Diagnostique o seguinte funil:

**Tipo de negócio:** [e-commerce, SaaS, infoproduto, serviço, B2B]
**Produto principal:** [descreva]
**Preço:** [valor]
**Período analisado:** [ex: últimos 30 dias]

**Números do funil:**
- Visitantes: [número]
- Taxa de captura (visitante → lead): [%]
- Leads gerados: [número]
- Taxa de abertura de email: [%]
- Visitantes da página de vendas: [número]
- Taxa de conversão: [%]
- Vendas: [número]
- Faturamento: [valor]
- Investimento em tráfego: [valor]

Entregue:
1. Visão geral do funil (visual em texto com taxas)
2. Benchmarks de referência por métrica
3. Gargalo principal + quanto está custando em faturamento
4. Ranking de gargalos (do pior ao melhor)
5. Simulação de cenários (melhorando cada etapa)
6. Plano de ação priorizado (Top 5 ações)
```

## Exemplo de uso

### Input
Tipo: Infoproduto (curso online)
Preço: R$497
Período: Últimos 30 dias
Visitantes: 15.000 | Leads: 2.250 (15%) | Abertura email: 22% | Vendas: 38
Investimento: R$8.500

### Output
Gargalo #1: Taxa de conversão em vendas (1.69%)
Benchmark para infoprodutos de R$497: 2.5-4%

Impacto: Se sua conversão estivesse em 3%, você teria 67 vendas ao invés de 38 → R$33.299 ao invés de R$18.886 → R$14.413 a mais por mês.

Hipóteses:
1. Página de vendas com headline fraca ou pouca prova social
2. Preço apresentado sem ancoragem de valor
3. Leads frios demais chegando na página

Ação #1: Adicionar 5 depoimentos com resultado (impacto: +30-50% na conversão)

---
**Tags:** Avançado | Auditoria | Marketing, Vendas & Publicidade
