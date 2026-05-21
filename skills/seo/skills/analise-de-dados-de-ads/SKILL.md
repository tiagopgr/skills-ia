---
name: analise-de-dados-de-ads
description: Interpretar os dados brutos do Facebook Ads Manager e TikTok Ads — identificando qual métrica indica qual problema, o que está causando o ROAS abaixo do esperado e quais ações tomar em cada cenário — para transformar números em decisões concretas. Para o empreendedor solo que analisa os próprios ads, esta skill elimina a paralisia de "tenho os dados mas não sei o que fazer com eles".
---

# Análise de Dados de Ads

## Objetivo
Interpretar os dados brutos do Facebook Ads Manager e TikTok Ads — identificando qual métrica indica qual problema, o que está causando o ROAS abaixo do esperado e quais ações tomar em cada cenário — para transformar números em decisões concretas. Para o empreendedor solo que analisa os próprios ads, esta skill elimina a paralisia de "tenho os dados mas não sei o que fazer com eles".

## Quando usar
- Para fazer a revisão semanal das campanhas e definir o que otimizar
- Quando as métricas pioram e não fica claro o que está errado
- Para interpretar um período de dados antes de tomar uma decisão grande (pausar, escalar, recriar)
- Para criar uma rotina de análise que pode ser feita em 20 minutos por semana

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados das campanhas do período que quer analisar
3. Receba o diagnóstico completo com causa raiz de cada problema e ações concretas
4. Execute as ações na ordem de prioridade e documente os resultados

## O Prompt
```
Você é um especialista em análise de performance de campanhas pagas no Meta Ads e TikTok Ads para e-commerce. Seus princípios: (1) cada métrica de ads aponta para uma camada específica do problema: CPM alto → problema de público/leilão; CTR baixo → problema de criativo/hook; CVR baixa → problema de landing page ou oferta; ROAS baixo com tudo ok → problema de margem ou atribuição, (2) analisar métricas isoladas sem ver o funil completo leva a diagnósticos errados — CTR de 3% com CVR de 0,5% é pior do que CTR de 1,5% com CVR de 2%, (3) frequência alta (> 3) em audiência pequena é sinal de esgotamento de público — mais impressões no mesmo público não aumentam vendas, (4) decisões de otimização precisam de dados suficientes — pausar um criativo com 200 impressões é tão errado quanto manter um com 3.000 impressões e ROAS 0,5x.

**Dados do período a analisar:** [informe o período — ex: últimos 7 dias, últimos 30 dias]

**Métricas por campanha/conjunto/criativo:**
- Impressões: [número]
- Alcance: [número]
- Frequência: [média]
- CPM: [€]
- CTR (link): [%]
- CPC: [€]
- Cliques no link: [número]
- View Content (visualizações de produto): [número e taxa]
- Add to Cart: [número e taxa]
- Initiate Checkout: [número e taxa]
- Purchases: [número]
- Valor de compra: [€]
- ROAS: [valor]
- CPA (custo por compra): [€]

**Contexto:**
- Break-even ROAS: [seu valor]
- Qual criativo/conjunto está rodando: [descreva brevemente]
- Alguma mudança feita no período: [ex: subi o budget, mudei público, editei a página]

Entregue:

**1. Diagnóstico por funil**
Análise de cada etapa (CPM → CTR → CVR → ROAS) com status de cada métrica e o que indica.

**2. Causa raiz dos problemas identificados**
Para cada métrica fora do benchmark: o que está causando o problema (criativo? público? página? oferta?) com explicação.

**3. Ações prioritárias**
Lista de ações em ordem de impacto: o que fazer primeiro, segundo e terceiro.

**4. O que NÃO mudar**
Quais elementos estão funcionando bem e não devem ser alterados (para não destruir o que está certo).

**5. Decisões de criativo**
Para cada criativo ativo: manter, pausar, iterar ou escalar — com justificativa baseada nos dados.
```

## Exemplo de uso

### Input
- Período: últimos 14 dias
- CPM: €22 / CTR: 0,85% / CPC: €2,59 / ATC rate: 8% / CVR: 1,3% / ROAS: 1,6x / CPA: €28
- Break-even ROAS: 2,48x
- Frequência: 2,4
- Criativo: 1 vídeo de 30s rodando há 18 dias no mesmo conjunto
- Mudança: nenhuma no período

### Output
| Métrica | Valor | Benchmark | Status | O que indica |
|---------|-------|-----------|--------|-------------|
| CPM | €22 | €12-18 EU | 🔴 Alto | Público com leilão caro ou frequência elevando CPM |
| CTR | 0,85% | 1,5-3% | 🔴 Baixo | Hook fraco — criativo não está parando o scroll |
| CVR (clique→compra) | 1,3% | 2-4% | ⚠️ Abaixo | Página de produto ou oferta com fricção |
| Frequência | 2,4 após 18 dias | <3 | ⚠️ Atenção | Próximo do esgotamento — mesmo criativo há 18 dias |
| ROAS | 1,6x | ≥2,48x | 🔴 Crítico | Campanha gerando prejuízo por unidade |

---
**Tags:** Avançado | Análise | SEO, Analítica & Dados
