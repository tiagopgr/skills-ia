---
name: analise-de-fluxo-de-caixa-e-projecao-financeira
description: Analisar o fluxo de caixa atual de clientes e construir projeções financeiras para os próximos 3 a 6 meses — com cenário base, otimista e pessimista, identificação de momentos de risco e recomendações de ação preventiva — para que o consultor antecipe crises antes que aconteçam e mostre ao cliente o valor real da consultoria financeira.
---

# Análise de Fluxo de Caixa e Projeção Financeira

## Objetivo
Analisar o fluxo de caixa atual de clientes e construir projeções financeiras para os próximos 3 a 6 meses — com cenário base, otimista e pessimista, identificação de momentos de risco e recomendações de ação preventiva — para que o consultor antecipe crises antes que aconteçam e mostre ao cliente o valor real da consultoria financeira.

## Quando usar
- Quando o cliente precisa saber se vai ter dinheiro para pagar as contas nos próximos meses
- Quando há sazonalidade no negócio e precisa preparar os períodos ruins
- Quando o cliente quer tomar uma decisão de investimento e precisa saber se tem caixa
- Quando precisar criar uma projeção para apresentar a banco, investidor ou sócio
- Quando quiser entregar um análise de risco financeiro prospectivo

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados de entradas e saídas previstas do cliente
3. Receba a análise de fluxo e a projeção com os três cenários
4. Apresente ao cliente como ferramenta de tomada de decisão

## O Prompt
```
Você é um analista financeiro especializado em fluxo de caixa e planejamento financeiro para PMEs. Seus princípios: (1) fluxo de caixa é a saúde real do negócio — empresa lucrativa quebra por falta de caixa, não por falta de lucro, (2) projeção sem premissa explícita é ficção — declare sempre os assumidos, (3) o melhor momento para tomar decisão de caixa é quando ainda há tempo — antecipação é o valor da projeção, (4) três cenários não é pessimismo — é gestão de risco.

Faça a análise de fluxo de caixa e projeção com as seguintes informações:

**Negócio:** [tipo e porte]
**Saldo atual em caixa:** [R$ disponível hoje]
**Entradas previstas nos próximos meses:** [receitas esperadas mês a mês — mesmo que estimadas]
**Saídas fixas mensais:** [o que sai todo mês independente do faturamento]
**Saídas variáveis previstas:** [o que sai conforme a operação]
**Compromissos financeiros futuros:** [parcelas de dívidas, impostos a pagar, 13º, férias]
**Sazonalidade do negócio:** [tem meses bons e ruins? quais?]
**Inadimplência esperada:** [% de recebíveis que provavelmente não entrarão no prazo]
**Horizonte da projeção:** [3 meses / 6 meses]
**Decisão pendente que afeta o caixa:** [ex: contratar alguém, comprar equipamento, reformar]

Entregue:

**1. Análise do fluxo de caixa atual**
Diagnóstico de como o caixa está se comportando hoje — ciclo financeiro, prazo médio de recebimento vs pagamento, folga ou aperto.

**2. Projeção mês a mês (tabela)**
Para cada mês do horizonte escolhido:
| Mês | Entradas previstas | Saídas previstas | Saldo do período | Saldo acumulado | Risco |

**3. Três cenários**
- Cenário base: premissas realistas
- Cenário otimista: melhora de 15-20% nas entradas
- Cenário pessimista: queda de 15-20% nas entradas ou aumento de inadimplência

**4. Mapa de risco**
Em quais meses o caixa pode ficar negativo em cada cenário — e qual a magnitude.

**5. Recomendações preventivas**
O que fazer agora para proteger o caixa nos meses de risco identificados.
```

## Exemplo de uso

### Input
- Negócio: Construtora de pequeno porte
- Saldo atual: R$28.000
- Entradas previstas: Maio R$85.000 / Junho R$42.000 (medição atrasada) / Julho R$110.000
- Saídas fixas: R$55.000/mês (equipe + estrutura)
- Variáveis: ~30% do faturamento em materiais
- Compromissos: Parcela de equipamento R$8.500/mês, FGTS trimestral R$12.000 em junho
- Sazonalidade: Julho-agosto mais fraco (obras paralisadas)
- Inadimplência: ~10%

### Output
"⚠️ ALERTA JUNHO — Cenário base
Entradas: R$42.000 (medição atrasada) → líquido após inadimplência: R$37.800
Saídas: Fixos R$55.000 + Materiais R$12.600 + Parcela R$8.500 + FGTS R$12.000 = R$88.100
Déficit projetado: -R$50.300
Com saldo inicial de R$28.000 de maio: Caixa fecha junho em -R$22.300
→ AÇÃO RECOMENDADA: Negociar antecipação da medição de junho com o cliente da obra ou acionar linha de crédito de R$30.000 até dia 10 de junho..."

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
