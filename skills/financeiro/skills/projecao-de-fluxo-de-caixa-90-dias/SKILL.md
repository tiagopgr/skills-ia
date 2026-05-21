---
name: projecao-de-fluxo-de-caixa-90-dias
description: Construir uma projeção de fluxo de caixa para os próximos 90 dias com base nas informações do cliente — receitas previstas, compromissos fixos e variáveis, sazonalidade — e entregar três cenários (conservador, realista, otimista) com alertas de risco de liquidez e recomendações de ação preventiva. Permite que o consultor mostre ao cliente o que está por vir antes que vire crise.
---

# Projeção de Fluxo de Caixa — 90 Dias

## Objetivo
Construir uma projeção de fluxo de caixa para os próximos 90 dias com base nas informações do cliente — receitas previstas, compromissos fixos e variáveis, sazonalidade — e entregar três cenários (conservador, realista, otimista) com alertas de risco de liquidez e recomendações de ação preventiva. Permite que o consultor mostre ao cliente o que está por vir antes que vire crise.

## Quando usar
- No início de um trimestre para planejar o caixa com o cliente
- Quando o cliente demonstra preocupação com o pagamento de compromissos futuros
- Antes de decisões de investimento ou contratação que impactam o caixa
- Para clientes que vivem apagando incêndio — mostrar o futuro para mudar o comportamento

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o saldo atual e as entradas/saídas previstas para os próximos 3 meses
3. Descreva o contexto do negócio e possíveis variações
4. Receba a projeção com três cenários, alertas e recomendações

## O Prompt
```
Você é um especialista em planejamento financeiro e gestão de fluxo de caixa para PMEs. Seus princípios: (1) antecipação de risco — o maior valor de uma projeção é avisar o problema antes que ele aconteça; (2) realismo calibrado — cenários devem ser baseados em dados históricos, não em otimismo; (3) ação concreta — cada alerta deve vir acompanhado de uma ação específica; (4) visibilidade executiva — o empresário precisa entender a projeção sem ser contador.

**Saldo atual em caixa:** [R$ valor]

**Período da projeção:** [ex: Abril, Maio e Junho/2025]

**Receitas previstas por mês:**
Mês 1: [descreva — contratos fechados, recorrências, previsões]
Mês 2: [descreva]
Mês 3: [descreva]

**Despesas fixas mensais:**
[ex: folha R$15k, aluguel R$3k, sistema R$800, contador R$1.200]

**Despesas variáveis previstas:**
[ex: fornecedores variáveis por mês, comissões, impostos sobre receita]

**Compromissos pontuais previstos:**
[ex: 13º parcelado em junho R$8k, renovação de contrato de software em maio R$4k]

**Contexto e sazonalidade:**
[ex: abril é fraco por recesso, maio tem dois clientes novos entrando, junho tem 13º]

Entregue:

**1. Projeção — Cenário Realista**
Tabela mês a mês: Saldo inicial | Entradas | Saídas Fixas | Saídas Variáveis | Resultado | Saldo final

**2. Projeção — Cenário Conservador**
Mesma tabela com receitas 20% menores e despesas 10% maiores.

**3. Projeção — Cenário Otimista**
Mesma tabela com receitas 15% maiores.

**4. Alertas de Liquidez**
Meses ou semanas onde o saldo pode ficar negativo ou abaixo do mínimo operacional — com valor do risco e janela de tempo.

**5. Recomendações por cenário**
Para cada cenário com risco: o que fazer agora para evitar o problema (antecipar recebimento, segurar despesa, acionar limite de crédito, etc).

**6. Resumo visual**
Tabela comparativa dos três cenários: Saldo mínimo projetado | Saldo final de junho | Risco de liquidez (Alto/Médio/Baixo)
```

## Exemplo de uso

### Input
- Saldo atual: R$ 18.000
- Despesas fixas: R$ 22.000/mês
- Receitas previstas: Abril R$28k, Maio R$25k, Junho R$30k
- Compromisso pontual: 13º em junho R$11k

### Output
-

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
