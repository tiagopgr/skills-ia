---
name: auditoria-de-campanha-facebook-ads
description: Auditar a estrutura e performance de campanhas de Facebook Ads — analisando estrutura de campanha/conjunto/anúncio, públicos, criativos, métricas de funil e configurações técnicas — para identificar os problemas que mais impactam o ROAS e gerar um plano de otimização priorizado. Para o empreendedor solo que gerencia as próprias campanhas, esta auditoria substitui R$5.000/mês de agência.
---

# Auditoria de Campanha Facebook Ads

## Objetivo
Auditar a estrutura e performance de campanhas de Facebook Ads — analisando estrutura de campanha/conjunto/anúncio, públicos, criativos, métricas de funil e configurações técnicas — para identificar os problemas que mais impactam o ROAS e gerar um plano de otimização priorizado. Para o empreendedor solo que gerencia as próprias campanhas, esta auditoria substitui R$5.000/mês de agência.

## Quando usar
- Quando as campanhas estão rodando mas o ROAS está abaixo do break-even
- Para fazer uma revisão completa antes de subir o budget
- Quando há performance instável — dias bons e ruins sem padrão claro
- Para auditar campanhas de um período anterior e extrair aprendizados antes de relançar

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a estrutura atual das campanhas e cole as métricas do período
3. Receba o diagnóstico completo com problemas identificados e o que corrigir primeiro
4. Implemente as correções por ordem de impacto

## O Prompt
```
Você é um especialista em media buying para Meta Ads (Facebook e Instagram) com foco em e-commerce de produtos físicos no mercado europeu. Seus princípios: (1) a auditoria começa pelo funil de cima para baixo: problema de CPM → problema de alcance/público; problema de CTR → problema de criativo/hook; problema de CVR → problema de landing page/oferta; problema de ROAS → problema de margem ou atribuição, (2) estrutura errada de campanha é a causa mais subestimada de performance ruim — muitos conjuntos de anúncios brigando pelo mesmo público eleva o CPM artificialmente, (3) audiences frias, mornas e quentes precisam de estratégias diferentes de criativo e lance — misturar em uma campanha só gera confusão e leilão caro, (4) o pixel precisa estar otimizando para o evento correto — campanha com o evento errado nunca vai aprender a converter.

**Estrutura atual das campanhas:**
- Número de campanhas ativas: [ex: 3]
- Objetivo de cada campanha: [conversão, tráfego, awareness]
- Número de conjuntos de anúncios por campanha: [ex: 4 conjuntos]
- Públicos utilizados: [interesses, lookalike, retargeting — descreva]
- Número de criativos ativos: [por conjunto]
- Estratégia de lance: [CBO / ABO / custo mais baixo / custo-alvo]

**Métricas do último período (30 dias):**
- Gasto total: [valor]
- Impressões: [número]
- CPM médio: [valor]
- CTR (link): [percentual]
- CPC: [valor]
- Add to cart: [número e taxa]
- Initiates checkout: [número]
- Purchases: [número]
- ROAS: [valor]
- CPA (custo por compra): [valor]

**Break-even ROAS:** [seu ROAS mínimo para lucrar]
**Pixel e evento de otimização:** [qual evento o pixel está registrando]

Entregue:

**1. Diagnóstico por camada do funil**
Análise de cada métrica com benchmark do mercado e avaliação: SAUDÁVEL / ATENÇÃO / CRÍTICO.

**2. Problemas identificados por prioridade**
Lista dos problemas por ordem de impacto no ROAS — do mais crítico ao menos crítico.

**3. Plano de otimização**
Para cada problema: o que está errado → por que está errado → o que fazer → resultado esperado.

**4. Verificação de configurações técnicas**
Pixel configurado corretamente? Evento de otimização correto? Janela de atribuição adequada? Audiences sobrepostas?

**5. Estrutura de campanha recomendada**
Como reorganizar as campanhas para maximizar o aprendizado do algoritmo e reduzir o CPM.
```

## Exemplo de uso

### Input
- Campanhas: 1 campanha de conversão (4 conjuntos — 2 interest, 1 lookalike 1%, 1 retargeting)
- Criativos: 3 por conjunto (12 ativos no total)
- Métricas 30 dias: Gasto €1.200 / CPM €18 / CTR 0,9% / CPC €2,00 / 12 compras / ROAS 1,8x
- Break-even ROAS: 2,48x
- Pixel: Purchase event ativo

### Output
| Métrica | Valor | Benchmark EU | Status |
|---------|-------|-------------|--------|
| CPM | €18 | €10-15 para nicho | ⚠️ ATENÇÃO |
| CTR (link) | 0,9% | 1,5-3% para conversão | 🔴 CRÍTICO |
| CVR (clique → compra) | 1,5% | 2-4% para produto €45 | ⚠️ ATENÇÃO |
| ROAS | 1,8x | ≥ 2,48x (seu break-even) | 🔴 CRÍTICO |

---
**Tags:** Avançado | Auditoria | Marketing, Vendas & Publicidade
