---
name: analise-de-indicadores-financeiros-e-kpis
description: Analisar os principais KPIs financeiros de um negócio — rentabilidade, liquidez, endividamento, eficiência operacional e crescimento — comparando com benchmarks do setor e identificando os indicadores fora da zona saudável — para que o consultor chegue na reunião com insights precisos e o cliente enxergue o diagnóstico com clareza numérica.
---

# Análise de Indicadores Financeiros e KPIs

## Objetivo
Analisar os principais KPIs financeiros de um negócio — rentabilidade, liquidez, endividamento, eficiência operacional e crescimento — comparando com benchmarks do setor e identificando os indicadores fora da zona saudável — para que o consultor chegue na reunião com insights precisos e o cliente enxergue o diagnóstico com clareza numérica.

## Quando usar
- Quando quiser fazer uma análise de saúde financeira completa de um cliente
- Quando precisar de benchmarks setoriais para contextualizar os números do cliente
- Quando quiser criar um painel de KPIs para monitorar mensalmente
- Quando precisar apresentar análise financeira para sócios ou diretoria do cliente
- Quando quiser elevar o nível técnico das suas entregas de consultoria

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados financeiros do cliente
3. Receba a análise completa dos indicadores com contexto setorial e recomendações
4. Use como base para a reunião de apresentação de resultados

## O Prompt
```
Você é um analista financeiro com expertise em avaliação de desempenho empresarial e benchmarking setorial para PMEs. Seus princípios: (1) indicador isolado é dado — indicador comparado ao benchmark e à tendência é insight, (2) a ordem certa é: medir → comparar → interpretar → recomendar — não pule etapas, (3) o cliente não precisa entender finanças para entender "você está no vermelho nisso aqui — veja o que empresas do seu porte fazem", (4) tendência é mais importante que pontualidade — um número ruim pode ser coincidência, uma tendência ruim é um problema.

Faça a análise de indicadores financeiros com os seguintes dados do cliente:

**Negócio e setor:** [tipo de empresa e segmento]
**Período de análise:** [mês/trimestre atual — e anteriores se disponíveis]
**Dados disponíveis:** [informe o que tiver: DRE, balanço, fluxo de caixa, faturamento, custos]
**Faturamento:** [bruto e líquido]
**Custos variáveis totais:** [valor ou %]
**Custos fixos totais:** [valor]
**Resultado líquido:** [lucro ou prejuízo]
**Ativo total (se disponível):** [bens e direitos]
**Passivo total (se disponível):** [dívidas e obrigações]
**Contas a receber:** [saldo total]
**Estoque (se aplicável):** [valor]
**Dívida financeira total:** [empréstimos, financiamentos]

Entregue:

**1. Painel de KPIs calculados**
Tabela com os principais indicadores:
| Indicador | Valor Atual | Referência Saudável (setor) | Status | Tendência |

Indicadores a calcular (com os dados disponíveis):
- Margem de contribuição (%)
- Margem EBITDA (%)
- Margem líquida (%)
- Ponto de equilíbrio (R$)
- Índice de liquidez corrente
- Prazo médio de recebimento
- Retorno sobre investimento (ROI)
- Nível de endividamento (%)

**2. Top 3 indicadores críticos**
Os 3 KPIs mais preocupantes com análise aprofundada de cada um.

**3. Top 3 indicadores positivos**
O que está funcionando bem — para o consultor não só trazer problema.

**4. Análise de tendência**
Se tiver dados de mais de 1 período: o que está melhorando, o que está piorando.

**5. Recomendações priorizadas**
3-5 ações concretas para melhorar os indicadores críticos — em ordem de impacto.
```

## Exemplo de uso

### Input
- Negócio: Academia de ginástica, 650 alunos
- Faturamento bruto: R$142.000/mês
- Custos variáveis: R$18.000 (comissões, material)
- Custos fixos: R$98.000 (equipe, aluguel, equipamentos)
- Resultado líquido: R$8.500
- Contas a receber: R$38.000 (muitos atrasados)
- Dívida: R$220.000 (reforma + equipamentos)
- Período: Abril 2025

### Output
"🔴 KPI CRÍTICO #1 — Margem líquida: 5,9%
Valor atual: R$8.500 / R$142.000 = 5,9%
Referência saudável para academias: 12-18%
Status: CRÍTICO — abaixo da metade do mínimo saudável
Causa provável: Custo fixo muito alto em relação ao faturamento (69%). Com 650 alunos e R$142k de receita, ticket médio de R$218 está abaixo do potencial — ou a estrutura de custo é pesada demais para o modelo atual..."

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
