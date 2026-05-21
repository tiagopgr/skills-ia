---
name: framework-de-alocacao-de-budget-de-ads
description: Criar um framework de decisão para alocar o budget total de anúncios entre canais (Facebook vs TikTok), fases do funil (aquisição vs retargeting) e tipos de campanha (teste vs escala) — para maximizar o ROAS total sem depender de intuição ou distribuição arbitrária. A alocação de budget é uma das decisões mais impactantes e menos sistemáticas de quem gerencia os próprios ads.
---

# Framework de Alocação de Budget de Ads

## Objetivo
Criar um framework de decisão para alocar o budget total de anúncios entre canais (Facebook vs TikTok), fases do funil (aquisição vs retargeting) e tipos de campanha (teste vs escala) — para maximizar o ROAS total sem depender de intuição ou distribuição arbitrária. A alocação de budget é uma das decisões mais impactantes e menos sistemáticas de quem gerencia os próprios ads.

## Quando usar
- Para definir como dividir o budget entre Facebook Ads e TikTok Ads
- Quando o budget muda (para cima ou para baixo) e precisa redistribuir
- Para criar uma regra de alocação que pode ser revisada mensalmente
- Ao querer entender qual canal merece mais investimento com base em dados

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o budget disponível, os canais ativos e os dados de performance de cada um
3. Receba o framework de alocação com regras e distribuição recomendada
4. Aplique o framework e revisite mensalmente com os dados atualizados

## O Prompt
```
Você é um especialista em media planning e alocação de budget para e-commerce DTC com múltiplos canais de tráfego pago. Seus princípios: (1) a alocação de budget deve seguir a performance, não a preferência — canal com ROAS mais alto recebe mais, canal com ROAS abaixo do break-even recebe menos até melhorar, (2) a distribuição ideal entre aquisição e retargeting depende do volume de tráfego: com menos de 2.000 visitas/mês, retargeting deve ser ≤ 20% do budget; acima de 5.000 visitas, pode ir até 30%, (3) budget de teste de criativos deve ser fixo e separado do budget de performance — misturar os dois contamina os dados de ambos, (4) regra de ouro: nunca deixe 100% do budget em um único canal sem backup — concentração de risco em ads é o maior erro de e-commerces solo.

**Budget total mensal de ads:** [valor em euros]
**Canais ativos:** [Facebook Ads / TikTok Ads / Google / outros]
**Performance atual por canal:**
- Facebook: ROAS [x], CPA [€], volume de compras [n]
- TikTok: ROAS [x], CPA [€], volume de compras [n]
**Volume de tráfego atual:** [visitantes/mês na loja]
**Fase atual do negócio:** [testando / crescendo / escalando]
**Objetivo do próximo mês:** [escalar vendas / reduzir CPA / testar novos criativos / tudo]

Entregue:

**1. Diagnóstico de alocação atual**
Como está distribuído hoje e se é adequado para a fase do negócio.

**2. Framework de distribuição recomendado**
Percentuais recomendados por: canal (FB vs TikTok) / fase do funil (aquisição vs retargeting) / tipo (performance vs teste).

**3. Regras de rebalanceamento**
Quando e como rebalancear: o que fazer se um canal supera o outro / se o ROAS de um canal cai / se o budget aumenta ou diminui.

**4. Distribuição para os próximos 30 dias**
Em euros: quanto alocar em cada canal, fase e tipo — com justificativa.

**5. KPI de alocação**
Como saber se a alocação está funcionando — qual métrica revisar mensalmente para ajustar a distribuição.
```

## Exemplo de uso

### Input
- Budget total: €1.200/mês
- Canais: Facebook Ads + TikTok Ads
- Facebook: ROAS 1,8x / CPA €30 / 13 compras
- TikTok: ROAS 2,1x / CPA €25 / 11 compras
- Tráfego: ~800 visitas/mês
- Fase: testando (criativos novos em desenvolvimento)
- Objetivo: melhorar ROAS geral para acima do break-even (2,48x)

### Output
| Destinação | % | Valor/mês | Justificativa |
|-----------|---|-----------|--------------|
| TikTok Ads — Performance | 35% | €420 | Melhor ROAS atual (2,1x) — mais perto do break-even |
| Facebook Ads — Performance | 30% | €360 | ROAS 1,8x ainda abaixo, mas volume maior — manter com criativo novo |
| Teste de criativos (ambos) | 20% | €240 | Fase de testes requer orçamento fixo e separado |
| Retargeting (Meta) | 15% | €180 | Volume de 800 visitas/mês — limite de ~15% para retargeting ser eficaz |
|

---
**Tags:** Avançado | Template | Financeiro, Jurídico & Compliance
