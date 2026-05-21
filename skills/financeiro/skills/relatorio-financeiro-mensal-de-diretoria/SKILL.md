---
name: relatorio-financeiro-mensal-de-diretoria
description: Transformar dados financeiros brutos do mês em um relatório executivo claro e orientado a decisão — com análise de receita, margem, custos, fluxo de caixa e projeções — para que o diretor tenha a fotografia financeira do negócio em uma leitura de 10 minutos e chegue à reunião mensal com perguntas, não com dúvidas básicas.
---

# Relatório Financeiro Mensal de Diretoria

## Objetivo
Transformar dados financeiros brutos do mês em um relatório executivo claro e orientado a decisão — com análise de receita, margem, custos, fluxo de caixa e projeções — para que o diretor tenha a fotografia financeira do negócio em uma leitura de 10 minutos e chegue à reunião mensal com perguntas, não com dúvidas básicas.

## Quando usar
- Para estruturar o fechamento financeiro mensal em formato executivo
- Quando o financeiro envia dados brutos e o diretor precisa interpretar tudo sozinho
- Para criar o padrão de relatório que o time financeiro vai usar todo mês
- Ao preparar apresentação de resultados para sócios ou conselho

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados financeiros do mês (pode ser em formato de texto ou lista)
3. Receba o relatório estruturado com análise, destaques e recomendações
4. Use como base para a reunião de diretoria ou envie diretamente para os sócios

## O Prompt
```
Você é um CFO experiente com sólida formação em finanças corporativas e habilidade de transformar dados complexos em narrativas executivas claras. Seus princípios: (1) um bom relatório financeiro conta uma história — não apenas descreve números; (2) desvios precisam de explicação e plano de ação, não apenas registro; (3) o diretor precisa saber 3 coisas: onde estamos, onde deveríamos estar e o que fazer; (4) projeção sem premissas é adivinhação — sempre explicite as hipóteses.

Crie um relatório financeiro mensal executivo com base nos dados abaixo:

**Mês de referência:** [ex: março/2025]
**Receita bruta do mês:** [valor]
**Receita bruta do mês anterior:** [valor]
**Meta de receita do mês:** [valor]
**Principais custos do mês:** [liste os maiores custos com valores aproximados]
**Resultado operacional (lucro/prejuízo):** [valor]
**Saldo de caixa atual:** [valor]
**Contas a receber em aberto:** [valor e aging se disponível]
**Contas a pagar nos próximos 30 dias:** [valor]
**Contexto relevante do mês:** [ex: perdemos 2 contratos, fechamos 3 novos, tivemos custo extra com rescisão]

Entregue:

**1. Sumário executivo (máximo 5 linhas)**
A fotografia do mês: o que aconteceu, onde estamos vs. meta e a principal mensagem financeira.

**2. Análise de receita**
Comparativo mês atual vs. mês anterior vs. meta com variação em % e análise dos principais fatores.

**3. Análise de custos e margem**
Breakdown dos principais custos, margem bruta e operacional, e comparativo com período anterior.

**4. Posição de caixa e liquidez**
Saldo atual, projeção de caixa para os próximos 30 dias e alerta se houver risco de liquidez.

**5. Destaques e alertas**
3 pontos positivos do mês e 3 pontos de atenção — com recomendação de ação para cada alerta.

**6. Projeção do próximo mês**
Estimativa de receita, custo e resultado com premissas explícitas.
```

## Exemplo de uso

### Input
- Mês: Março/2025
- Receita bruta: R$380.000
- Receita mês anterior: R$410.000
- Meta: R$420.000
- Principais custos: Folha R$180.000, fornecedores R$60.000, aluguel R$15.000, outros R$35.000
- Resultado operacional: R$90.000
- Caixa atual: R$145.000
- A receber: R$230.000 (R$80.000 com mais de 45 dias)
- Contexto: Perdemos 1 contrato grande (R$35k/mês), custos de rescisão de R$12.000

### Output
> Março encerrou com receita de R$380k — 9,5% abaixo da meta de R$420k e 7,3% abaixo de fevereiro. A principal causa é a saída do contrato Grupo Delta (R$35k/mês), que gerou também R$12k em custos de rescisão. A margem operacional se manteve em 23,7%, dentro do intervalo saudável. O ponto crítico do mês é o aging de recebíveis: R$80k com mais de 45 dias representa risco real de caixa se não endereçado nas próximas 2 semanas.

---
**Tags:** Intermediário | Geração | Financeiro, Jurídico & Compliance
