---
name: projecao-de-fluxo-de-caixa-12-meses
description: Criar uma projeção de fluxo de caixa detalhada para os próximos 12 meses — incluindo receitas, custos fixos e variáveis, investimentos e sazonalidade — para antecipar meses de aperto e tomar decisões financeiras com segurança.
---

# Projeção de Fluxo de Caixa (12 Meses)

## Objetivo
Criar uma projeção de fluxo de caixa detalhada para os próximos 12 meses — incluindo receitas, custos fixos e variáveis, investimentos e sazonalidade — para antecipar meses de aperto e tomar decisões financeiras com segurança.

## Quando usar
- No planejamento financeiro anual da empresa
- Ao buscar investimento ou crédito (bancos pedem)
- Para decidir se pode contratar, investir ou expandir
- Quando a empresa tem meses bons e meses ruins (sazonalidade)

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Insira os dados financeiros da empresa
3. Receba a projeção completa com cenários
4. Revise mensalmente e ajuste as premissas

## O Prompt
```
Você é um analista financeiro que sabe que a maioria das empresas não fecha por falta de lucro — fecha por falta de caixa. Uma projeção bem feita mostra meses antes se vai faltar dinheiro.

Crie a projeção de fluxo de caixa para 12 meses:

**Empresa:** [nome e setor]
**Modelo de receita:** [recorrente, por projeto, vendas únicas, misto]
**Faturamento médio mensal atual:** [valor]
**Expectativa de crescimento:** [% ao mês ou estável]
**Sazonalidade:** [meses fortes e fracos, se houver]

**Receitas:** [fontes e valores]
**Custos fixos mensais:** [aluguel, salários, ferramentas, contador]
**Custos variáveis:** [tráfego pago, comissões, impostos]
**Investimentos previstos:** [contratações, equipamentos]
**Saldo atual em caixa:** [valor]

Entregue:
1. Tabela de fluxo de caixa mensal (12 meses)
2. Três cenários (otimista, realista, pessimista)
3. Alertas (meses com risco de caixa negativo)
4. Indicadores-chave (margem, runway, ponto de equilíbrio)
5. Recomendações financeiras
```

## Exemplo de uso

### Input
Empresa: Agência de marketing digital
Faturamento: R$45K/mês (3 contratos de R$15K)
Crescimento: 1 novo cliente a cada 2 meses
Custos fixos: R$22K
Saldo atual: R$30K
Investimento previsto: Novo designer no mês 4 (R$5K/mês)

### Output
Meses 1-3: Confortável. Fluxo líquido ~R$15K/mês. Saldo acumula para R$75K.
Mês 4: Entra designer (+R$5K fixo). Fluxo cai para R$10K/mês.
Mês 5: Se novo cliente entrar como previsto, fluxo volta para R$17K.

Cenário pessimista: Se perder 1 cliente no mês 3, caixa fica apertado no mês 6 (R$18K — apenas 1 mês de reserva).

Recomendação: só contratar designer após confirmar o 4º cliente.
Runway atual: 1.4 meses. Meta mínima: 3 meses de custo fixo = R$66K.

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
