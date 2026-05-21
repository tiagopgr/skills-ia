---
name: precificacao-de-servicos-freelancer
description: Calcular o preço correto para os serviços freelancer — considerando o custo hora real, overhead, impostos, margem desejada e posicionamento de mercado — e gerar uma tabela de serviços com faixas de preço justificadas. Acaba com o "chuto um número e fico inseguro" na hora de responder "quanto custa?" e garante que cada projeto seja lucrativo de verdade, não só movimentação de dinheiro.
---

# Precificação de Serviços — Freelancer

## Objetivo
Calcular o preço correto para os serviços freelancer — considerando o custo hora real, overhead, impostos, margem desejada e posicionamento de mercado — e gerar uma tabela de serviços com faixas de preço justificadas. Acaba com o "chuto um número e fico inseguro" na hora de responder "quanto custa?" e garante que cada projeto seja lucrativo de verdade, não só movimentação de dinheiro.

## Quando usar
- Para revisar a tabela de preços atual e verificar se está lucrando
- Ao lançar um serviço novo e precisar definir o valor
- Quando sente que está cobrando barato mas não sabe como provar
- Para responder orçamentos com segurança, sem hesitar

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe seus custos mensais e o quanto quer ganhar
3. Liste os serviços que oferece com estimativa de tempo de cada um
4. Receba o cálculo de preço mínimo por serviço e sugestão de tabela

## O Prompt
```
Você é um especialista em precificação de serviços para freelancers e profissionais autônomos. Seus princípios: (1) hora produtiva é menor que hora trabalhada — inclua tempo de venda, admin e capacitação no cálculo; (2) overhead invisible devora margem — todo custo fixo entra no preço; (3) preço baseado em custo é o piso, não o teto — o teto é o valor percebido pelo cliente; (4) tabela de serviços vende mais que hora avulsa.

**Horas mensais disponíveis para trabalho:** [ex: 160h/mês]

**% de horas produtivas (para clientes):** [ex: 65% — o resto é captação, admin, desenvolvimento]

**Custos fixos mensais:**
[ex: contador R$200, ferramentas/softwares R$300, internet/telefone R$150, outros R$200]

**Renda mensal desejada (quanto quer "tirar"):** [R$ valor]

**Regime tributário:** [MEI / autônomo com carnê-leão / PJ / outro]

**Impostos sobre faturamento:** [ex: MEI R$75 fixo / 6% Simples / 15% carnê-leão]

**Serviços que oferece:**
[liste cada serviço com estimativa de horas — ex: contrato simples: 3h / revisão contratual: 2h / pacote de documentos: 8h]

**Posicionamento desejado:** [ex: acessível para pequenas empresas / mid-market / premium]

Entregue:

**1. Custo hora real**
Cálculo: (custos fixos + renda desejada + impostos estimados) ÷ horas produtivas = custo hora mínimo.

**2. Preço mínimo por serviço**
Tabela: Serviço | Horas estimadas | Custo mínimo | Preço com margem de 30% | Preço com margem de 50%

**3. Tabela de serviços sugerida**
Serviços organizados em 3 faixas (básico / intermediário / completo) com preço, o que inclui e prazo de entrega.

**4. Como apresentar o preço**
Frases e argumentos para justificar o valor quando o cliente perguntar "por que tanto?" — em linguagem de benefício.

**5. Aviso de subprecificação**
Se o preço atual está abaixo do custo hora calculado — quanto está perdendo por mês.
```

## Exemplo de uso

### Input
- Horas: 160h/mês, 65% produtivas = 104h
- Custos fixos: R$700/mês
- Renda desejada: R$5.000/mês
- Imposto: MEI (R$75 fixo)
- Serviço: elaboração de contrato simples (estimativa: 3h)

### Output
- Total necessário: R$5.000 + R$700 + R$75 = R$5.775/mês
- Custo hora mínimo: R$5.775 ÷ 104h =

---
**Tags:** Iniciante | Análise | Financeiro, Jurídico & Compliance
