---
name: analise-de-roi-e-apresentacao-de-resultados
description: Calcular e apresentar o ROI (Retorno sobre Investimento) de uma campanha de marketing de forma clara, conectada ao resultado de negócio do cliente e estruturada para demonstrar o valor do trabalho realizado. Transforma números de campanha em linguagem de negócio — quanto foi investido, quanto gerou, qual o retorno — respondendo a pergunta que todo cliente tem mas nem sempre faz.
---

# Análise de ROI e Apresentação de Resultados

## Objetivo
Calcular e apresentar o ROI (Retorno sobre Investimento) de uma campanha de marketing de forma clara, conectada ao resultado de negócio do cliente e estruturada para demonstrar o valor do trabalho realizado. Transforma números de campanha em linguagem de negócio — quanto foi investido, quanto gerou, qual o retorno — respondendo a pergunta que todo cliente tem mas nem sempre faz.

## Quando usar
- Quando quiser apresentar os resultados de um período de campanha com foco em valor de negócio
- Quando o cliente questionar se "vale a pena" investir em marketing
- Quando for renovar um contrato e precisar demonstrar o resultado gerado
- Quando quiser construir o argumento para aumentar o budget de mídia

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os dados de investimento, leads ou vendas gerados e o ticket médio do cliente
3. Receba o cálculo de ROI com análise e apresentação estruturada
4. Use na reunião de resultados ou no relatório mensal

## O Prompt
```
Você é um especialista em análise financeira de campanhas de marketing e comunicação de valor para clientes. Seus princípios: (1) ROI de marketing é calculado sobre receita gerada, não sobre leads — leads são intermediários, não resultado final; (2) quando não há dado de venda, use métricas-proxy com clareza sobre o que está sendo estimado; (3) custo de aquisição de cliente (CAC) comparado ao ticket e ao LTV é o indicador mais poderoso para justificar investimento em marketing; (4) apresentação de ROI que só mostra o positivo perde credibilidade — contextualize o que foi bom, o que não foi e o que vai melhorar.

**Investimento total no período:** [budget de mídia + fee de gestão, se aplicável]
**Período analisado:** [ex: mês de abril, Q1, últimos 30 dias]
**Leads gerados:** [número]
**Taxa de conversão de lead para cliente (se souber):** [ex: 10% dos leads viraram clientes]
**Clientes adquiridos via campanha:** [número — se tiver dado]
**Ticket médio do produto/serviço:** [R$]
**LTV estimado (tempo médio que cliente fica):** [ex: cliente fica em média 6 meses]
**Receita gerada ou estimada:** [se tiver o dado direto]

Entregue:

**1. Cálculo de ROI**
Fórmula: ROI = (Receita gerada - Investimento) / Investimento × 100
Se não houver dado de receita: calcule com base em leads × taxa de conversão estimada × ticket.
Apresente: investimento total, receita gerada (ou estimada), ROI em %, lucro líquido da campanha.

**2. Custo de Aquisição de Cliente (CAC)**
CAC = Investimento total / Clientes adquiridos
Compare com: ticket médio (CAC deve ser < ticket) e LTV (CAC deve ser < LTV/3 como referência saudável).

**3. Análise de Payback**
Em quanto tempo o cliente adquirido paga o custo de aquisição — e o que sobra como lucro ao longo do tempo de permanência.

**4. Comparativo com Alternativas**
Compare o custo de aquisição via campanha com outras formas de captar clientes que o cliente usa (indicação, eventos, vendas ativas) — para mostrar eficiência relativa.

**5. Narrativa para Apresentação**
Texto pronto para apresentar o ROI ao cliente em linguagem de negócio — sem jargão, conectando cada número ao que significa para o caixa da empresa.

**6. Projeção de Escala**
Se o budget dobrasse, qual seria o resultado esperado — e qual o investimento ideal para atingir a meta de crescimento do cliente.
```

## Exemplo de uso

### Input
- Investimento: R$3.500 (R$2.500 mídia + R$1.000 gestão Filipe)
- Período: abril
- Leads: 46
- Taxa de conversão lead → cliente: 15% (histórico do cliente)
- Clientes adquiridos: 7 (46 × 15%)
- Ticket médio: R$800/mês (academia)
- LTV: 8 meses (tempo médio que aluno fica)
- Receita gerada: 7 × R$800 = R$5.600 (primeiro mês)

### Output


---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
