---
name: estrategia-de-retargeting
description: Criar uma estratégia completa de retargeting para e-commerce — com audiências segmentadas por estágio do funil (visitantes, view content, add to cart, checkout abandonado), criativos específicos para cada estágio e regras de exclusão — para converter o tráfego que já chegou na loja mas não comprou. Retargeting bem feito tipicamente gera ROAS 3 a 6x maior do que campanhas de aquisição, com custo por clique muito menor.
---

# Estratégia de Retargeting

## Objetivo
Criar uma estratégia completa de retargeting para e-commerce — com audiências segmentadas por estágio do funil (visitantes, view content, add to cart, checkout abandonado), criativos específicos para cada estágio e regras de exclusão — para converter o tráfego que já chegou na loja mas não comprou. Retargeting bem feito tipicamente gera ROAS 3 a 6x maior do que campanhas de aquisição, com custo por clique muito menor.

## Quando usar
- Para ativar ou reorganizar as campanhas de retargeting do e-commerce
- Quando o retargeting está rodando mas sem segmentação por estágio do funil
- Para criar criativos específicos para cada audiência de retargeting
- Ao querer maximizar o retorno do tráfego de topo de funil antes de escalar

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o volume de tráfego, os eventos do pixel e os criativos disponíveis
3. Receba a estrutura completa de retargeting com audiências, criativos e budget
4. Configure as campanhas no Meta Ads Manager ou TikTok Ads Manager

## O Prompt
```
Você é um especialista em funil de conversão e retargeting para e-commerce DTC no Meta Ads e TikTok Ads. Seus princípios: (1) retargeting de funil único é dinheiro desperdiçado — quem visitou o site e quem abandonou o checkout são pessoas com intenção completamente diferente e precisam de mensagens completamente diferentes, (2) a mensagem de retargeting deve referenciar a ação que a pessoa já tomou — "Vous avez failli passer à côté" funciona para carrinho abandonado; não para quem só viu o produto, (3) o budget de retargeting deve ser proporcional ao volume de tráfego — com pouco tráfego, audiências de retargeting ficam pequenas demais para o algoritmo aprender (< 1.000 pessoas = não vale campanha separada), (4) exclusão é tão importante quanto inclusão — clientes que já compraram não devem ver anúncio de aquisição; incluir eles no retargeting eleva o CPM sem elevar as vendas.

**Volume de tráfego mensal na loja:** [visitantes únicos/mês]
**Eventos do pixel ativos:** [View Content / Add to Cart / Initiate Checkout / Purchase]
**Taxa de add to cart:** [% de visitantes que adicionam ao carrinho]
**Taxa de checkout iniciado:** [% de visitantes que iniciam checkout]
**Taxa de conversão:** [% de visitantes que compram]
**Plataformas de retargeting:** [Meta Ads / TikTok Ads / ambas]
**Criativos disponíveis:** [o que tem para usar em retargeting]
**Budget total disponível para retargeting:** [% do budget total ou valor]

Entregue:

**1. Mapa de audiências de retargeting**
Para cada estágio: definição da audiência, janela de tempo (7d, 14d, 30d), tamanho estimado, intenção do estágio.

**2. Mensagem estratégica por estágio**
O que comunicar para cada audiência — tom, ângulo e gatilho principal.

**3. Criativos sugeridos por estágio**
Formato, duração e texto para o criativo ideal de cada audiência de retargeting — adaptando os criativos existentes.

**4. Estrutura de campanhas de retargeting**
Como organizar as campanhas no Ads Manager — separadas por estágio ou CBO unificado — com justificativa.

**5. Regras de exclusão**
Quem excluir de cada campanha para não desperdiçar budget e não irritar quem já comprou.

**6. Budget recomendado por estágio**
Distribuição do budget de retargeting pelos estágios, com justificativa baseada no volume de cada audiência.
```

## Exemplo de uso

### Input
- Tráfego: ~800 visitantes/mês
- Pixel: View Content ✅, Add to Cart ✅, Initiate Checkout ✅, Purchase ✅
- Taxa de ATC: 8% (~64 pessoas/mês)
- Taxa checkout iniciado: 4% (~32 pessoas/mês)
- Taxa de conversão: 1,5% (~12 compras/mês)
- Plataformas: Meta Ads
- Criativos: 3 vídeos + 2 imagens
- Budget retargeting: €200/mês

### Output
| Estágio | Audiência | Janela | Tamanho est. | Intenção |
|---------|----------|--------|-------------|----------|
| 1 — Visitantes frios | View Content (sem ATC) | 14 dias | ~640 | Curiosidade — baixa intenção |
| 2 — Interessados | Add to Cart (sem compra) | 14 dias | ~52 | Alta intenção — travou em preço ou dúvida |
| 3 — Quase convertidos | Initiate Checkout (sem compra) | 7 dias | ~20 | Intenção máxima — problema técnico ou último hesitation |

---
**Tags:** Avançado | Template | Marketing, Vendas & Publicidade
