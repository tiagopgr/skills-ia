---
name: definicao-de-kpis-por-tipo-de-negocio
description: Definir os KPIs (Key Performance Indicators) certos para cada tipo de negócio — separando métricas de vaidade de métricas que realmente importam — com metas, frequência de acompanhamento e dashboards sugeridos.
---

# Definição de KPIs por Tipo de Negócio

## Objetivo
Definir os KPIs (Key Performance Indicators) certos para cada tipo de negócio — separando métricas de vaidade de métricas que realmente importam — com metas, frequência de acompanhamento e dashboards sugeridos.

## Quando usar
- Ao estruturar o sistema de métricas da empresa
- Quando acompanha muitos números mas não sabe quais importam
- Para criar dashboards de acompanhamento
- Em reuniões de planejamento estratégico

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva seu tipo de negócio e fase atual
3. Receba os KPIs prioritários com metas e benchmarks
4. Configure o acompanhamento nas ferramentas que já usa

## O Prompt
```
Você é um analista de dados de negócio que sabe que medir tudo é tão ruim quanto não medir nada. A maioria das empresas: (1) mede métricas de vaidade (seguidores, visitantes) ao invés de métricas de resultado, (2) acompanha números demais e não age sobre nenhum, (3) não tem meta clara para cada KPI.

Defina os KPIs para:

**Tipo de negócio:** [e-commerce, SaaS, agência, infoproduto, consultoria]
**Fase:** [validação, crescimento, escala, estabilidade]
**Modelo de receita:** [recorrente, vendas únicas, projetos, misto]
**Faturamento atual:** [faixa]
**Equipe:** [tamanho]
**Objetivo principal do momento:** [crescer, reter, lucrar, escalar]

Entregue: North Star Metric, KPIs primários (5-7), KPIs por departamento, Métricas de vaidade para PARAR de acompanhar, Dashboard sugerido, Ritual de métricas (diário, semanal, mensal).
```

## Exemplo de uso

### Input
Tipo: SaaS B2B (gestão de projetos)
Fase: Crescimento (product-market fit validado)
Receita: Recorrente (MRR R$45K)
Equipe: 15 pessoas
Objetivo: Crescer MRR para R$100K em 6 meses

### Output
North Star Metric: Weekly Active Teams (equipes ativas semanalmente)
"Mais do que MRR, o número de equipes usando ativamente o produto toda semana prediz retenção, expansão e referral."

KPIs primários:
1. MRR — R$45K atual → Meta: R$100K — Semanal
2. Net Revenue Retention — Meta: >110% — Mensal
3. Churn Rate — Meta: <3%/mês — Mensal
4. CAC — Meta: <R$800 — Mensal
5. LTV/CAC — Meta: >3x — Mensal

Vaidade (parar de olhar): Visitantes do site (olhe leads, não visitantes)

---
**Tags:** Intermediário | Análise | Produto, E-commerce & SaaS
