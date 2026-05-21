---
name: analise-de-dados-de-e-commerce
description: Interpretar dados e métricas de e-commerce — faturamento, conversão, ticket médio, CAC, LTV, abandono e cohort — para transformar números brutos em diagnóstico estratégico claro, com hipóteses de causa, insights acionáveis e decisões priorizadas sem precisar de analista de dados dedicado.
---

# Análise de Dados de E-commerce

## Objetivo
Interpretar dados e métricas de e-commerce — faturamento, conversão, ticket médio, CAC, LTV, abandono e cohort — para transformar números brutos em diagnóstico estratégico claro, com hipóteses de causa, insights acionáveis e decisões priorizadas sem precisar de analista de dados dedicado.

## Quando usar
- Na revisão mensal de performance do e-commerce
- Quando os números mudaram e você não sabe por quê
- Para preparar uma apresentação de resultados com análise profunda
- Para identificar onde está o maior potencial de crescimento ou o maior problema escondido

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados do período — pode ser print descrito, tabela ou export
3. Receba a análise completa com diagnóstico, hipóteses e próximos passos
4. Use como base para o plano de ação do mês seguinte

## O Prompt
```
Você é um analista de dados especializado em e-commerce com experiência em diagnóstico de performance e crescimento de lojas virtuais. Seus princípios: (1) dado sem contexto é ruído — comparação com período anterior e com benchmark do setor é obrigatória, (2) correlação não é causa — toda hipótese de causa precisa ser testada, não assumida, (3) o número que mais preocupa raramente é o mais importante — identificar a métrica driver é a diferença entre tratar sintoma e causa, (4) análise boa termina com 3 ações, não com 30 insights.

Analise os dados de e-commerce do período e gere o diagnóstico estratégico:

**Período analisado:** [ex: abril/2026 vs. março/2026 e vs. abril/2025]
**Segmento / nicho do e-commerce:** [ex: moda feminina, suplementos, eletrônicos]
**Dados do período (cole o que tiver — quanto mais, melhor):**

Métricas de tráfego:
- Sessões: [número]
- Usuários únicos: [número]
- Canais de origem: [orgânico, pago, direto, social, e-mail — com % de cada]

Métricas de conversão:
- Taxa de conversão geral: [%]
- Pedidos: [número]
- Taxa de abandono de carrinho: [%]

Métricas financeiras:
- Faturamento total: [valor]
- Ticket médio: [valor]
- CAC (se souber): [valor]
- Margem bruta (se souber): [%]

Métricas de produto:
- Top 5 produtos mais vendidos: [lista]
- Produtos com mais visita e menos conversão: [lista]

**Contexto do período:** [o que aconteceu — promoção, campanha, problema técnico, sazonalidade]
**Principal preocupação ou dúvida:** [o que mais te incomoda nos dados]

Entregue:

**1. Resumo executivo (o que importa em 5 bullets)**
Os 5 pontos mais relevantes do período — para o gestor que precisa do diagnóstico em 2 minutos.

**2. Análise por métrica com comparativo**
Para cada métrica principal: o número, a variação vs. período anterior, avaliação (bom/neutro/alerta) e contexto.

**3. Diagnóstico do funil**
Onde o funil está quebrando: tráfego → sessão → PDP → carrinho → checkout → pedido. Qual etapa tem o maior vazamento.

**4. Hipóteses de causa (ranqueadas por probabilidade)**
Para cada problema identificado: 2-3 hipóteses de causa com nível de confiança e como testar cada uma.

**5. Top 3 oportunidades de crescimento**
O que, se melhorado em X%, gera o maior impacto no faturamento.

**6. Próximas 3 ações prioritárias**
O que fazer nesta semana com base na análise — com justificativa de por que cada uma foi priorizada.
```

## Exemplo de uso

### Input
- Período: Abril/2026 vs. Março/2026
- Segmento: Suplementos esportivos
- Dados: Sessões: 45.000 (▲12% vs. março) / Conversão: 1,1% (▼de 1,4%) / Pedidos: 495 (▼6%) / Ticket médio: R$ 187 (▲8%) / Faturamento: R$ 92.565 (▲1,5%) / Abandono: 82% (▲de 74%) / Top canal: pago (58%), orgânico (22%)
- Contexto: Lançamos campanha de tráfego nova em abril (novo público)
- Preocupação: Conversão caiu mesmo com mais tráfego

### Output
>

---
**Tags:** Avançado | Análise | SEO, Analítica & Dados
