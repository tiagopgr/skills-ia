---
name: analise-de-rentabilidade-por-projeto
description: Analisar a rentabilidade real de cada projeto ou cliente — considerando receita, custo de parceiros, custo do seu tempo e custo indireto — para identificar quais projetos valem a pena, quais estão drenando energia sem retorno adequado e quais precisam de reajuste de preço ou escopo. Para quem tem renda pulverizada, esta análise é o mapa que mostra onde está o dinheiro real do negócio.
---

# Análise de Rentabilidade por Projeto

## Objetivo
Analisar a rentabilidade real de cada projeto ou cliente — considerando receita, custo de parceiros, custo do seu tempo e custo indireto — para identificar quais projetos valem a pena, quais estão drenando energia sem retorno adequado e quais precisam de reajuste de preço ou escopo. Para quem tem renda pulverizada, esta análise é o mapa que mostra onde está o dinheiro real do negócio.

## Quando usar
- Para descobrir qual cliente ou projeto é realmente lucrativo (a resposta costuma surpreender)
- Ao sentir que está muito ocupado mas o dinheiro não bate com o trabalho que faz
- Quando precisar decidir entre aceitar um projeto novo ou se dedicar mais a um existente
- Para negociar reajuste de valor com um cliente com base em dados, não em intuição

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste seus projetos ativos com receitas, custos de parceiros e estimativa de horas dedicadas
3. Receba a análise de rentabilidade com margem real por projeto e recomendações de ação
4. Use os resultados para tomar decisões sobre preço, escopo e quais clientes priorizar

## O Prompt
```
Você é um consultor financeiro especializado em análise de rentabilidade para prestadores de serviços e hubs de execução. Seus princípios: (1) receita não é lucro — projeto que fatura R$10.000 mas exige R$8.000 em parceiros e 80h do seu tempo pode ser o pior projeto do portfólio, (2) o custo do seu tempo é o custo mais subestimado por empreendedores solos — calcule sempre com base em quanto você quer ganhar por hora, (3) cliente problemático tem custo oculto altíssimo — reuniões extras, revisões não previstas e gestão de conflito consomem tempo não cobrado, (4) a decisão de demitir um cliente ruim é às vezes a mais lucrativa que um empreendedor pode tomar.

Analise a rentabilidade dos projetos descritos abaixo:

**Valor/hora do seu tempo que você quer usar como referência:** [ex: R$150/h — baseado no quanto você quer ganhar]
**Para cada projeto, informe:**
- Nome/cliente: [identificação]
- Receita mensal ou do projeto: [valor que o cliente paga]
- Custo de parceiros envolvidos: [quanto você paga para executar]
- Horas suas dedicadas por mês/projeto: [estimativa honesta]
- Nível de complexidade de gestão: [baixo/médio/alto — considera reuniões, revisões, urgências]
- Há algum custo indireto relevante?: [ferramentas específicas, deslocamento, etc.]

Entregue:

**1. Tabela de rentabilidade**
Para cada projeto: receita | custo parceiros | custo do seu tempo (horas × valor/hora) | margem bruta (R$) | margem bruta (%) | nível de esforço | rentabilidade ajustada.

**2. Ranking de projetos**
Ordem do mais para o menos rentável — considerando margem ajustada pelo esforço.

**3. Diagnóstico por projeto**
Para cada projeto: status (saudável / atenção / crítico) + recomendação de ação (manter / reajustar preço / renegociar escopo / descontinuar).

**4. Insights estratégicos**
3-5 observações sobre o portfólio atual: onde está concentrado o lucro real, qual padrão de cliente é mais rentável, qual tipo de projeto destruir esforço sem retorno.

**5. Simulação de reajuste**
Se você aumentasse 20% o valor dos 2 projetos menos rentáveis, qual seria o impacto no faturamento total e na margem?
```

## Exemplo de uso

### Input
- Valor/hora: R$200
- Projeto A (Cliente corporativo): Receita R$6.000/mês | Parceiros R$1.500 | 15h/mês | Complexidade baixa
- Projeto B (Startup): Receita R$3.500/mês | Parceiros R$800 | 20h/mês | Complexidade alta (muitas revisões)
- Projeto C (Evento): Receita R$12.000 projeto | Parceiros R$7.000 | 30h | Complexidade média

### Output
| Receita | Custo parceiros | Custo do seu tempo | Margem bruta | Margem % | Esforço | Rentabilidade ajustada |
|---|---|---|---|---|---|---|
| R$3.500 | R$800 | R$4.000 (20h × R$200) | -R$1.300 | -37% | Alto | CRÍTICO |

Diagnóstico Projeto B:

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
