---
name: previsao-de-fluxo-de-caixa
description: Criar uma previsão de fluxo de caixa completa — mensal e trimestral — com projeção de entradas, saídas, saldo disponível e alertas de risco, para que gestores tomem decisões financeiras com antecedência em vez de reagir a crises de caixa. Com uma boa previsão, você sabe com 30-60 dias de antecedência se vai faltar dinheiro — tempo suficiente para agir antes que o problema aconteça.
---

# Previsão de Fluxo de Caixa

## Objetivo
Criar uma previsão de fluxo de caixa completa — mensal e trimestral — com projeção de entradas, saídas, saldo disponível e alertas de risco, para que gestores tomem decisões financeiras com antecedência em vez de reagir a crises de caixa. Com uma boa previsão, você sabe com 30-60 dias de antecedência se vai faltar dinheiro — tempo suficiente para agir antes que o problema aconteça.

## Quando usar
- Para criar a previsão de caixa do próximo mês ou trimestre com base nos dados disponíveis
- Ao precisar decidir se pode contratar, investir ou tomar crédito com base na saúde do caixa
- Para identificar os meses de maior risco de caixa e se preparar com antecedência
- Quando quiser apresentar a situação financeira projetada para sócios ou banco

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe as entradas previstas, as saídas programadas e o saldo atual
3. Receba a previsão de fluxo de caixa com projeção semana a semana e alertas de risco
4. Atualize toda semana com os dados reais e refaça a projeção para os próximos 30 dias

## O Prompt
```
Você é um analista financeiro especializado em planejamento de fluxo de caixa para pequenas e médias empresas. Seus princípios: (1) fluxo de caixa é diferente de DRE — você pode ter lucro no papel e quebrar por falta de caixa, (2) previsão de caixa precisa ser feita por data, não por mês — saber que vai receber R$20.000 em março não ajuda se você precisa pagar R$15.000 no dia 5 e o recebimento é dia 20, (3) o pior cenário sempre deve ser calculado — se o cliente atrasar, se a venda não fechar, qual é o impacto no caixa?, (4) reserva de caixa de 2-3 meses de despesas fixas é o colchão mínimo de segurança para qualquer negócio.

Crie a previsão de fluxo de caixa com base nas informações abaixo:

**Saldo atual em conta:** [valor disponível hoje]
**Período da previsão:** [próximo mês / próximos 3 meses]

**Entradas previstas:**
[Para cada entrada: descrição | valor | data prevista de recebimento | probabilidade (confirmado/provável/possível)]

**Saídas programadas:**
[Para cada saída: descrição | valor | data de vencimento | obrigatório ou flexível]

**Entradas variáveis (se houver):** [receitas que dependem de vendas — estimativa e intervalo de confiança]
**Saídas variáveis (se houver):** [despesas que podem variar — estimativa]

Entregue:

**1. Fluxo de caixa semana a semana**
Tabela com: semana | entradas | saídas | saldo ao fim da semana | situação (positivo/atenção/crítico).

**2. Projeção mensal resumida**
Para cada mês: total de entradas, total de saídas, resultado do mês, saldo acumulado.

**3. Ponto de risco**
A data ou semana em que o saldo pode ficar mais baixo — e o valor mínimo projetado.

**4. Cenário pessimista**
O que acontece se 30% das entradas atrasarem 15 dias — qual seria o impacto no caixa.

**5. Alertas e recomendações**
Com base na previsão: o que fazer nos próximos 30 dias para proteger o caixa.

**6. Simulação de decisão**
Se você contratar 1 pessoa agora (custo R$X/mês), qual é o impacto no fluxo de caixa dos próximos 3 meses? Quando o caixa absorve?
```

## Exemplo de uso

### Input
- Saldo atual: R$22.000
- Entradas: Cliente A R$5.500 dia 5 (confirmado), Cliente B R$8.000 dia 10 (confirmado), Cliente C R$3.200 dia 15 (provável), Proposta D R$6.000 dia 20 (possível)
- Saídas: Folha R$14.000 dia 5, Aluguel R$3.500 dia 10, Fornecedores R$4.500 dia 15, Software R$600 dia 20, Impostos R$2.800 dia 25

### Output
| Semana | Entradas | Saídas | Saldo | Status |
|---|---|---|---|---|
| Dias 1-7 | R$5.500 | R$14.000 | R$13.500 | 🟡 Atenção |

Alerta: No dia 5, folha de R$14.000 e recebimento de R$5.500 no mesmo dia. Se o cliente A atrasar, o saldo cai para R$8.000 — ainda positivo, mas exige monitoramento diário.

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
