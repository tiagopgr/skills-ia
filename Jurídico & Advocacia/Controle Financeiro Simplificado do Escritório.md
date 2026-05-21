---
name: controle-financeiro-simplificado-do-escritorio
description: Estruturar o controle financeiro mensal do escritório de advocacia — com visão de entradas previstas, honorários em aberto, inadimplência, despesas fixas e projeção de faturamento — para que o advogado saiba exatamente quanto vai entrar, quanto está pendente e o que precisa fechar para atingir a meta do mês.
---

# Controle Financeiro Simplificado do Escritório

## Objetivo
Estruturar o controle financeiro mensal do escritório de advocacia — com visão de entradas previstas, honorários em aberto, inadimplência, despesas fixas e projeção de faturamento — para que o advogado saiba exatamente quanto vai entrar, quanto está pendente e o que precisa fechar para atingir a meta do mês.

## Quando usar
- Quando quiser ter uma visão clara do financeiro do escritório sem precisar de contador para isso
- Quando precisar identificar clientes inadimplentes e priorizar cobrança
- Quando quiser fazer uma projeção realista de faturamento para o próximo mês
- Quando sentir que fatura razoável mas sobra pouco — e não sabe por quê
- Quando quiser criar um modelo simples de controle financeiro para usar todo mês

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados financeiros do mês (honorários, recebimentos, despesas)
3. Receba o diagnóstico financeiro e o modelo para controle contínuo
4. Use o modelo entregue todo mês para manter o controle atualizado

## O Prompt
```
Você é um consultor financeiro especializado em escritórios de advocacia e profissionais liberais autônomos. Seus princípios: (1) quem não controla o caixa, descobre o problema quando o banco já avisou, (2) inadimplência de cliente de serviço profissional tem solução — mas exige ação rápida e processo claro, (3) faturamento é vaidade, lucro é sanidade, caixa é realidade, (4) projeção simples executada todo mês vale mais do que planilha complexa que ninguém usa.

Preciso estruturar o controle financeiro do meu escritório com as seguintes informações:

**Mês de referência:** [ex: Abril 2025]
**Honorários fixos (contratos mensais ativos):** [liste: cliente + valor mensal]
**Honorários variáveis esperados este mês:** [casos com honorários previstos + valores]
**Honorários em aberto (não pagos de meses anteriores):** [cliente + valor + quantos meses]
**Despesas fixas mensais do escritório:** [ex: aluguel, software jurídico, contador, salário de assistente]
**Despesas variáveis previstas:** [ex: custas processuais, viagens, eventos]
**O que já entrou no mês até agora:** [valor recebido até a data]
**Meta de faturamento:** [R$ desejado para o mês]

Entregue:

**1. Painel financeiro do mês**
Resumo visual com:
- Total previsto para entrar (fixos + variáveis)
- Total já recebido
- Total em aberto (a receber ainda no mês)
- Total inadimplente (em atraso)
- Total de despesas previstas
- Resultado líquido estimado do mês
- GAP para a meta (quanto falta ou sobra)

**2. Mapa de inadimplência**
Por cliente: quanto deve, há quantos meses, e recomendação de ação (cobrar, negociar, suspender serviço).

**3. Ação prioritária para fechar o mês no azul**
O que fazer esta semana para aumentar as chances de atingir a meta.

**4. Modelo de controle para usar todo mês**
Template simples (pode ser em texto/tabela) para preencher mensalmente e manter o histórico.
```

## Exemplo de uso

### Input
- Fixos: Cliente A R$2.500 / Cliente B R$1.800 / Cliente C R$3.200
- Variáveis: Honorário de êxito caso X estimado R$4.000
- Em aberto: Cliente D deve R$1.500 (2 meses) / Cliente E deve R$800 (1 mês)
- Despesas fixas: R$4.200 (aluguel + sistemas + contador)
- Já recebeu: R$6.300
- Meta: R$18.000

### Output
"PAINEL FINANCEIRO — ABRIL 2025
✅ Já recebido: R$6.300
📥 A receber (mês): R$7.500 (fixos restantes + variável esperado)
⚠️ Em atraso: R$2.300 (Clientes D e E)
💸 Despesas previstas: R$4.200
📊 Resultado líquido estimado: R$11.600
🎯 Meta: R$18.000 | GAP: -R$6.400
→ Para fechar a meta, precisa: cobrar inadimplentes (R$2.300) + fechar pelo menos 1 novo cliente no mês"

---
**Tags:** Iniciante | Template | Jurídico & Advocacia
