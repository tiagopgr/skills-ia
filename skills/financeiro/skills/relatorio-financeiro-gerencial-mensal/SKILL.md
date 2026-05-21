---
name: relatorio-financeiro-gerencial-mensal
description: Gerar um relatório financeiro gerencial completo — com análise de receitas, despesas, margem, fluxo de caixa e variações em relação ao mês anterior e à meta — para que gestores de pequenas equipes possam apresentar a situação financeira do negócio de forma clara, tomar decisões com base em dados e comunicar resultados para sócios ou diretores sem depender de um contador ou analista financeiro para cada relatório.
---

# Relatório Financeiro Gerencial Mensal

## Objetivo
Gerar um relatório financeiro gerencial completo — com análise de receitas, despesas, margem, fluxo de caixa e variações em relação ao mês anterior e à meta — para que gestores de pequenas equipes possam apresentar a situação financeira do negócio de forma clara, tomar decisões com base em dados e comunicar resultados para sócios ou diretores sem depender de um contador ou analista financeiro para cada relatório.

## Quando usar
- Ao final de cada mês para consolidar e apresentar os resultados financeiros
- Para preparar a apresentação de resultados para sócios, diretores ou investidores
- Quando precisar identificar onde estão os maiores desvios de custo ou receita
- Para criar o hábito de gestão financeira mensal com base em dados, não em intuição

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Insira os dados financeiros do mês: receitas, despesas, comparativo com mês anterior e meta
3. Receba o relatório gerencial completo com análise, gráfico descritivo e recomendações
4. Apresente em reunião ou envie por e-mail para as partes interessadas

## O Prompt
```
Você é um analista financeiro especializado em relatórios gerenciais para pequenas e médias empresas. Seus princípios: (1) relatório gerencial bom é o que permite uma decisão ser tomada em menos de 10 minutos de leitura — clareza e objetividade acima de tudo, (2) variação sem contexto é só número — cada dado relevante precisa de uma explicação de causa e impacto, (3) relatório que só mostra o passado tem valor limitado — o ideal sempre inclui tendência e projeção para o próximo período, (4) linguagem financeira deve ser acessível para quem decide — evite jargão técnico sem explicação.

Gere o relatório financeiro gerencial com base nos dados abaixo:

**Empresa/área:** [nome ou setor]
**Mês de referência:** [mês e ano]
**Receita realizada no mês:** [valor]
**Meta de receita do mês:** [valor]
**Receita do mês anterior:** [valor — para comparação]
**Despesas totais do mês:** [valor total]
**Principais categorias de despesa:** [ex: pessoal R$X / aluguel R$X / marketing R$X / fornecedores R$X]
**Resultado líquido (lucro/prejuízo):** [receita − despesas]
**Fluxo de caixa:** [posição atual de caixa e projeção para o próximo mês se souber]
**Desvios relevantes:** [o que foi muito acima ou abaixo do esperado]
**Meta do próximo mês:** [se souber]

Entregue o relatório completo com:

**1. Resumo executivo** (5 linhas — para quem tem 2 minutos)
Resultado do mês, desvio da meta, comparação com mês anterior, destaque positivo, ponto de atenção.

**2. Análise de receitas**
Realizado vs meta: variação em R$ e %. Comparação com mês anterior. Causa dos desvios.

**3. Análise de despesas**
Tabela por categoria: previsto (se houver) / realizado / variação. Destaque para as maiores variações.

**4. Resultado e margem**
Lucro/prejuízo do mês. Margem líquida (%). Comparação com mês anterior. Tendência.

**5. Fluxo de caixa**
Posição atual e projeção para os próximos 30 dias com base nos dados disponíveis.

**6. Destaques e alertas**
✅ 2-3 pontos positivos do período
⚠️ 2-3 pontos de atenção que precisam de ação

**7. Recomendações**
3 ações concretas para o próximo mês com base nos dados apresentados.

**8. Projeção**
Estimativa de resultado para o próximo mês com base na tendência atual.
```

## Exemplo de uso

### Input
- Mês: Março 2026
- Receita realizada: R$48.000 | Meta: R$55.000 | Mês anterior: R$44.000
- Despesas: R$38.500 (pessoal R$22.000 / aluguel R$4.500 / marketing R$3.000 / outros R$9.000)
- Resultado: R$9.500 lucro
- Fluxo de caixa: R$15.000 em conta, 2 recebíveis de R$12.000 previstos para abril
- Desvio: Marketing veio 50% acima do orçado por campanha extra

### Output
"Março encerrou com receita de R$48.000 — 13% abaixo da meta de R$55.000, mas 9% acima de fevereiro, indicando crescimento consistente. O resultado líquido foi positivo em R$9.500 (margem 19,8%). Principal desvio: despesas de marketing 50% acima do previsto pela campanha extra. Ponto de atenção: distância da meta de receita requer revisão do pipeline de vendas para abril."

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
