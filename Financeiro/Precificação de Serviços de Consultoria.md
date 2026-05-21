---
name: precificacao-de-servicos-de-consultoria
description: Calcular o preço correto para os serviços de consultoria — considerando custo hora real, overhead, margem desejada e posicionamento de mercado — e gerar uma tabela de preços com diferentes pacotes e justificativas de valor. Elimina o "chuto um número e reza" na hora de precificar e garante que cada contrato seja lucrativo de verdade.
---

# Precificação de Serviços de Consultoria

## Objetivo
Calcular o preço correto para os serviços de consultoria — considerando custo hora real, overhead, margem desejada e posicionamento de mercado — e gerar uma tabela de preços com diferentes pacotes e justificativas de valor. Elimina o "chuto um número e reza" na hora de precificar e garante que cada contrato seja lucrativo de verdade.

## Quando usar
- Para revisar a tabela de preços atual e verificar se está cobrindo os custos
- Ao criar um pacote novo e precisar definir o valor
- Quando sente que está cobrando barato mas não sabe como calcular o preço certo
- Para precificar um cliente de porte diferente dos habituais

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe seus custos operacionais e quanto tempo cada serviço demanda
3. Informe sua margem desejada e o posicionamento de mercado
4. Receba o cálculo completo com sugestão de tabela de preços por pacote

## O Prompt
```
Você é um especialista em precificação de serviços profissionais e consultoria. Seus princípios: (1) preço baseado em custo é o mínimo, não o objetivo — o teto é o valor percebido pelo cliente; (2) hora produtiva é menor que hora trabalhada — nunca divida faturamento desejado pelas horas totais; (3) overhead é invisível mas devora margem — inclua tudo: sistema, contador, imposto, tempo de venda; (4) pacotes vendem mais que hora — precificação por pacote aumenta ticket e reduz atrito.

**Horas mensais disponíveis para trabalho:** [ex: 160h/mês]

**% de horas produtivas (billable):** [ex: 60% — o resto é venda, admin, capacitação]

**Custos fixos mensais (MEI/empresa):**
[ex: contador R$800, sistemas R$500, aluguel R$1.200, telefone/internet R$200]

**Pró-labore ou salário desejado:** [R$ valor/mês]

**Impostos sobre faturamento:** [ex: Simples Nacional 6% / ISS 5%]

**Margem líquida desejada sobre faturamento:** [ex: 25%]

**Serviços que oferece:**
[lista os serviços com estimativa de horas mensais por cliente — ex: gestão financeira mensal: 8h/cliente]

**Posicionamento desejado:** [ex: mid-market / premium / acessível para pequenas empresas]

**Referência de mercado (se souber):**
[o que a concorrência cobra ou o que seus clientes pagam hoje]

Entregue:

**1. Custo hora real**
Cálculo detalhado: (custos fixos + pró-labore + impostos) ÷ horas produtivas mensais = custo hora mínimo.

**2. Preço mínimo por serviço**
Tabela: Serviço | Horas/mês | Custo mínimo | Preço com margem desejada

**3. Sugestão de tabela de pacotes**
3 pacotes (básico, intermediário, completo) com: nome do pacote, o que inclui, horas estimadas, preço sugerido, margem.

**4. Análise de viabilidade da carteira atual**
Se informado o faturamento atual: verificar se os preços cobertos estão acima do custo hora real.

**5. Argumento de valor para justificar o preço**
Para cada pacote: 3 bullets do que o cliente ganha que justificam o investimento — em linguagem de benefício, não de tarefa.
```

## Exemplo de uso

### Input
- Custos fixos: R$3.500/mês
- Pró-labore desejado: R$8.000/mês
- Imposto: 6% Simples
- Horas: 160h, 65% billable (104h)
- Serviço: gestão financeira mensal (8h/cliente)

### Output
- Custos totais: R$3.500 + R$8.000 = R$11.500/mês
- + Impostos (6%): R$11.500 ÷ 0,94 = R$12.234 de receita necessária
- Horas produtivas: 104h
-

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
