---
name: analise-de-repeticao-de-indebito-e-compensacao-tributaria
description: Analisar pedidos de repetição de indébito e compensação tributária — verificando a tese, o período de apuração, as regras de prescrição aplicáveis, os limites legais da compensação e a jurisprudência do STJ — para que o Procurador produza manifestação precisa sobre se o pedido é procedente, parcialmente procedente ou deve ser resistido.
---

# Análise de Repetição de Indébito e Compensação Tributária

## Objetivo
Analisar pedidos de repetição de indébito e compensação tributária — verificando a tese, o período de apuração, as regras de prescrição aplicáveis, os limites legais da compensação e a jurisprudência do STJ — para que o Procurador produza manifestação precisa sobre se o pedido é procedente, parcialmente procedente ou deve ser resistido.

## Quando usar
- Quando um contribuinte pleitear repetição de indébito de qualquer tributo federal
- Quando houver discussão sobre compensação tributária negada pela Receita Federal
- Quando precisar analisar se os valores pleiteados estão dentro do prazo prescricional
- Quando precisar avaliar se a compensação era permitida no período em questão
- Quando quiser construir a defesa da Fazenda em caso de repetição de indébito

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados do pedido de repetição ou compensação
3. Receba a análise com posição da Fazenda e argumentos para a peça
4. Confirme os dados específicos antes de usar na peça processual

## O Prompt
```
Você é um Procurador da Fazenda Nacional especializado em repetição de indébito e compensação tributária. Seus princípios: (1) repetição de indébito pressupõe pagamento indevido — verificar se o pagamento realmente foi indevido é o primeiro passo, (2) prazo prescricional de 5 anos para repetição (LC 118/2005 e Tema 169/STJ) é crucial — valores fora do prazo devem ser excluídos mesmo se a tese for procedente, (3) compensação tributária tem regras específicas — verificar se era permitida na época e se os créditos são homologáveis, (4) ser honesto sobre a viabilidade da tese — resistir a pedido claramente procedente gera desgaste sem resultado.

Analise o seguinte pedido de repetição de indébito / compensação:

**Tributo objeto do pedido:** [IRPJ / CSLL / PIS / COFINS / outro]
**Tese do contribuinte:** [por que ele afirma que pagou indevidamente]
**Período reivindicado:** [quais anos ou competências o contribuinte quer restituir]
**Valor pleiteado:** [R$ aproximado — se informado]
**Forma pedida:** [repetição (devolução em dinheiro) / compensação / ambas]
**Data da propositura da ação:** [quando o contribuinte ajuizou]
**Há decisão judicial vinculante sobre o tema?** [STF/STJ já decidiu? qual foi o resultado?]
**Dados adicionais:** [qualquer informação relevante]

Entregue:

**1. Viabilidade da tese**
A tese do contribuinte tem fundamento? Há decisão vinculante? Qual é a posição atual do STJ/STF?

**2. Análise do prazo prescricional**
Quais competências estão dentro do prazo de 5 anos a contar da propositura da ação? Quais estão prescritas?

**3. Verificação das regras de compensação (se aplicável)**
A compensação era permitida no período? Há limitações legais aplicáveis?

**4. Posição recomendada para a Fazenda**
Resistir integralmente / Resistir parcialmente (excluir prescritos) / Reconhecer procedência — com justificativa.

**5. Argumentação para a peça**
O que dizer na contestação ou manifestação — adaptado à posição recomendada.

**6. Valor corretamente calculado (se parcialmente procedente)**
Qual seria o valor correto levando em conta o prazo prescricional — para balizar eventual acordo ou proposta.
```

## Exemplo de uso

### Input
- Tributo: PIS/COFINS
- Tese: Exclusão do ICMS da base de cálculo (Tema 69 STF — RE 574.706)
- Período: Janeiro/2010 a dezembro/2023
- Valor: R$2.100.000
- Forma: Compensação com débitos vincendos
- Ação proposta: Março/2024
- Decisão vinculante: Sim — STF definiu modulação a partir de 15/03/2017 (exceto para quem já tinha ação ajuizada antes dessa data)

### Output
"1. VIABILIDADE DA TESE: PROCEDENTE — Tema 69 do STF é vinculante. O ICMS destacado em nota fiscal deve ser excluído da base de cálculo do PIS/COFINS.

2. ANÁLISE PRESCRICIONAL:
Ação proposta em março/2024. Prazo de 5 anos retroage a março/2019.
Competências DENTRO DO PRAZO: março/2019 a dezembro/2023 → RESTITUÍVEIS
Competências PRESCRITAS: janeiro/2010 a fevereiro/2019 → NÃO RESTITUÍVEIS

3. MODULAÇÃO DO STF:
A empresa propôs ação em março/2024 — APÓS 15/03/2017. Portanto, a modulação se aplica: o direito à exclusão vale somente a partir de 15/03/2017.
Período restituível considerando prescrição E modulação: março/2019 a dezembro/2023.

4. POSIÇÃO RECOMENDADA: RESISTIR PARCIALMENTE
Reconhecer o direito à exclusão somente das competências de março/2019 em diante, excluindo tanto as prescritas quanto as anteriores à modulação.

5. VALOR ESTIMADO CORRETO: Em vez de R$2.100.000, apenas o proporcional ao período de março/2019 a dezembro/2023 — aproximadamente 57 meses dos 168 pleiteados = ~35% do valor total = ~R$735.000 (verificar cálculo exato com os dados reais)."

---
**Tags:** Avançado | Análise | Jurídico & Advocacia
