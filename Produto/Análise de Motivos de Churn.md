---
name: analise-de-motivos-de-churn
description: Analisar sistematicamente os motivos de cancelamento (churn) de clientes — classificando por categoria, gravidade e acionabilidade — para criar um plano de retenção que ataque as causas reais e reduza a perda de receita recorrente.
---

# Análise de Motivos de Churn

## Objetivo
Analisar sistematicamente os motivos de cancelamento (churn) de clientes — classificando por categoria, gravidade e acionabilidade — para criar um plano de retenção que ataque as causas reais e reduza a perda de receita recorrente.

## Quando usar
- Quando o churn está acima do aceitável para o segmento
- Em revisões mensais/trimestrais de retenção
- Para criar ou otimizar o programa de Customer Success
- Antes de investir mais em aquisição (não adianta encher balde furado)

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva os dados de churn e feedback dos clientes
3. Receba a análise com padrões e plano de retenção
4. Implemente ações preventivas e monitore o impacto

## O Prompt
```
Você é um especialista em retenção que sabe que: (1) reduzir churn em 5% pode aumentar lucro em 25-95%, (2) é 5-25x mais caro adquirir novo cliente que reter, (3) a maioria do churn é previsível se monitorado.

Analise o churn para:

**Produto/Serviço:** [descreva]
**Modelo:** [SaaS, assinatura, recorrente, contrato]
**Preço:** [valor mensal/anual]
**Base de clientes ativa:** [número]
**Taxa de churn atual:** [%/mês ou %/ano]
**Motivos declarados pelos clientes que cancelaram:** [liste]
**Perfil dos clientes que mais cancelam:** [plano, segmento, tempo de conta]
**Perfil dos clientes que ficam:** [o que têm em comum]

Entregue: Classificação dos motivos (por valor, preço, produto, atendimento, involuntário, natural), Padrões identificados, Health Score framework, Plano de retenção por categoria, Quick wins (3 ações imediatas), Métricas para acompanhar.
```

## Exemplo de uso

### Input
Produto: SaaS de email marketing
Preço: R$97-R$297/mês
Base: 800 clientes ativos
Churn: 7%/mês (alto)
Motivos declarados: "Caro", "Não uso tudo", "Difícil de usar", "Migrei para Mailchimp"

### Output
Padrões identificados:
Mês crítico: Mês 3 (45% dos cancelamentos acontecem entre o mês 2 e 4)
Plano com mais churn: Plano básico (R$97) — 12% de churn vs 3% no plano avançado
Sinal preditivo: Clientes que não enviam nenhum email nos primeiros 14 dias têm 4x mais chance de cancelar.

Quick wins:
1. Onboarding ativo nos primeiros 14 dias: Email + call para ajudar a enviar a primeira campanha. Impacto: -30% churn.
2. Dunning management: 18% do churn é involuntário. Implementar retry automático. Impacto: -18%.
3. Downgrade path: Oferecer plano reduzido ao invés de cancelar. Retém 20-30%.

---
**Tags:** Avançado | Análise | Produto, E-commerce & SaaS
