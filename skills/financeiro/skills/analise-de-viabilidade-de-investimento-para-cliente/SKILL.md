---
name: analise-de-viabilidade-de-investimento-para-cliente
description: Analisar a viabilidade financeira de investimentos e decisões estratégicas de clientes — calculando payback, retorno esperado, ponto de equilíbrio do investimento e cenários de risco — para que o consultor ajude o cliente a tomar decisões de alocação de capital com base em dados, e não em intuição ou pressão do mercado.
---

# Análise de Viabilidade de Investimento para Cliente

## Objetivo
Analisar a viabilidade financeira de investimentos e decisões estratégicas de clientes — calculando payback, retorno esperado, ponto de equilíbrio do investimento e cenários de risco — para que o consultor ajude o cliente a tomar decisões de alocação de capital com base em dados, e não em intuição ou pressão do mercado.

## Quando usar
- Quando o cliente quer comprar um equipamento, abrir uma filial ou contratar mais pessoas
- Quando precisar calcular se um investimento faz sentido financeiro
- Quando o cliente quer expandir e precisa de base para decidir quanto e como
- Quando quiser comparar duas alternativas de investimento
- Quando precisar apresentar a viabilidade de um projeto para sócios ou financiadores

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados do investimento que o cliente quer fazer
3. Receba a análise completa com payback, cenários e recomendação
4. Use como base para a reunião de decisão com o cliente

## O Prompt
```
Você é um analista de investimentos e viabilidade financeira com especialização em PMEs e negócios em crescimento. Seus princípios: (1) investimento sem análise de payback é aposta — e empreendedor não pode se dar ao luxo de apostar o caixa, (2) toda análise precisa de três cenários: o que você espera, o que você quer e o que acontece se der errado, (3) o custo de oportunidade é invisível mas real — o que mais poderia ser feito com esse capital?, (4) decisão financeira boa considera não só o retorno mas o risco e o momento do caixa.

Faça a análise de viabilidade do seguinte investimento:

**Empresa e setor:** [nome e tipo de negócio]
**Descrição do investimento:** [o que o cliente quer fazer — seja específico]
**Valor total do investimento:** [R$ total]
**Forma de pagamento:** [à vista / financiado / parcelado — e condições se financiado]
**Receita adicional esperada:** [quanto esse investimento vai gerar a mais por mês]
**Custo adicional gerado:** [novos custos que o investimento traz — operacionais, manutenção, pessoal]
**Prazo estimado para gerar resultado:** [quantos meses até o investimento começar a dar retorno]
**Situação atual do caixa:** [tem reserva para fazer o investimento? como fica o caixa depois?]
**Alternativas consideradas:** [outras opções que o cliente cogitou]
**Urgência ou prazo externo:** [alguma pressão de tempo — promoção, contrato, prazo de mercado]

Entregue:

**1. Resumo executivo da análise**
Em 5 linhas: o investimento faz sentido? sob quais condições? qual o maior risco?

**2. Cálculos de viabilidade**
- Payback simples (meses para recuperar o investimento)
- Payback descontado (considerando custo do capital)
- ROI do investimento (%)
- Ponto de equilíbrio do investimento (quanto precisa gerar para justificar)

**3. Análise de três cenários**
| Cenário | Receita adicional | Custo adicional | Resultado mensal | Payback |
- Base (realista)
- Otimista (+20% receita)
- Pessimista (-20% receita ou +20% custo)

**4. Análise de risco**
Os 3 maiores riscos deste investimento e como mitigá-los.

**5. Recomendação**
Fazer agora / Fazer com condições / Adiar / Não fazer — e a justificativa clara.
```

## Exemplo de uso

### Input
- Empresa: Padaria artesanal
- Investimento: Forno industrial novo para aumentar produção em 40%
- Valor: R$38.000 (à vista) ou R$42.000 financiado em 24x de R$1.750
- Receita adicional esperada: +R$12.000/mês com mais produção
- Custo adicional: +R$3.200/mês (energia, embalagem, 1 funcionário parcial)
- Caixa atual: R$22.000 de reserva
- Alternativa: Continuar terceirizando produção excedente (custo atual R$4.500/mês)

### Output
"RECOMENDAÇÃO: FAZER — com condição de financiamento, não à vista.

Razão: O payback de 4,7 meses (cenário base) é excelente. A receita adicional de R$8.800/mês líquida cobre a parcela de R$1.750 em 5x. Mas pagar R$38.000 à vista reduziria a reserva de caixa de R$22.000 para R$0 — isso é risco operacional inaceitável. Financiando, você preserva o caixa, paga R$4.000 a mais no total (custo aceitável pela segurança) e ainda elimina os R$4.500/mês de terceirização..."

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
