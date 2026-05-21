---
name: interpretacao-de-metricas-e-kpis
description: Interpretar métricas e KPIs de marketing digital — entendendo o que cada número significa, se está bom ou ruim, por que e o que fazer — com benchmarks de referência por nicho e canal. Elimina a insegurança de quem está começando na área e não sabe se os resultados são satisfatórios, e fornece linguagem clara para comunicar esses dados para clientes não técnicos.
---

# Interpretação de Métricas e KPIs

## Objetivo
Interpretar métricas e KPIs de marketing digital — entendendo o que cada número significa, se está bom ou ruim, por que e o que fazer — com benchmarks de referência por nicho e canal. Elimina a insegurança de quem está começando na área e não sabe se os resultados são satisfatórios, e fornece linguagem clara para comunicar esses dados para clientes não técnicos.

## Quando usar
- Quando receber dados de campanha e não souber interpretar se o resultado é bom ou ruim
- Quando um cliente perguntar "esse número está bom?" e você precisar de uma resposta embasada
- Quando quiser montar um guia de referência de métricas para usar no dia a dia
- Quando for definir as metas de uma nova campanha e precisar de benchmarks realistas

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe as métricas que quer interpretar e o contexto da campanha
3. Receba interpretação de cada métrica com benchmark, diagnóstico e recomendação
4. Use para tomar decisões e para comunicar resultados ao cliente com segurança

## O Prompt
```
Você é um analista de marketing digital sênior especializado em métricas de performance e comunicação de dados. Seus princípios: (1) métrica boa ou ruim depende do contexto — nicho, canal, estágio da campanha e objetivo mudam tudo; (2) benchmarks são referências, não verdades absolutas — servem para orientar, não para julgar; (3) métrica isolada mente — CPL baixo com qualidade de lead ruim é pior do que CPL alto com qualidade boa; (4) o cliente precisa entender o que o número significa para o negócio dele, não para o marketing.

**Métricas a interpretar:** [liste as métricas e seus valores — ex: CTR: 1,4%, CPL: R$45, Taxa de conversão: 3,2%]
**Canal:** [Meta Ads, Google Ads, email marketing, orgânico, etc.]
**Objetivo da campanha:** [geração de leads, venda direta, awareness, etc.]
**Nicho/setor:** [ex: infoproduto, e-commerce, serviços locais, B2B, saúde, educação]
**Ticket médio do produto:** [R$ — impacta o que é um CPL/CPA aceitável]
**Público:** [frio, morno, quente — impacta benchmarks esperados]
**Estágio da campanha:** [em aprendizado (< 2 semanas), estabilizada (> 4 semanas), em otimização]

Entregue:

**1. Tabela de Interpretação das Métricas**
Para cada métrica informada:

| Métrica | Valor | Benchmark (nicho/canal) | Status | Interpretação em 1 frase |

**2. Diagnóstico Integrado**
O que os números dizem juntos — a história completa da campanha. Não métricas isoladas, mas o que a combinação revela.

**3. Glossário Personalizado**
Definição de cada métrica em linguagem simples — como você explicaria para o cliente. Versão técnica + versão leiga de cada uma.

**4. O Que as Métricas Não Revelam**
Pontos cegos — o que os dados não mostram e que precisaria ser investigado com dados adicionais ou testes.

**5. Como Apresentar ao Cliente**
Sugestão de como comunicar cada métrica para um cliente não técnico — qual a analogia, qual o contexto de negócio, como dar a notícia de um número ruim sem perder credibilidade.
```

## Exemplo de uso

### Input
- Métricas: CTR: 2,1% | CPC: R$1,80 | Taxa de conversão landing page: 8% | CPL: R$22,50 | Frequência: 2,3 | Alcance: 28.000 | Leads: 64
- Canal: Meta Ads
- Objetivo: geração de leads para curso online
- Nicho: educação/infoproduto
- Ticket: R$297
- Público: morno (seguidores + lookalike 1%)
- Estágio: estabilizada (5 semanas rodando)

### Output
| Métrica | Valor | Benchmark | Status | Interpretação |
|---------|-------|-----------|--------|---------------|
| CTR | 2,1% | 1-3% (feed) | ✅ Saudável | Anúncio está chamando atenção e gerando cliques acima da média |
| CPC | R$1,80 | R$1,50-R$3,50 | ✅ Saudável | Custo por clique competitivo para este nicho |
| Conv. LP | 8% | 15-30% | ⚠️ Atenção | Landing page convertendo abaixo do esperado — principal gargalo do funil |
| CPL | R$22,50 | R$15-R$40 | ✅ Saudável | Custo por lead dentro do aceitável para produto de R$297 |
| Frequência | 2,3 | <3 | ✅ Saudável | Audiência ainda não saturada — há espaço para escalar |

---
**Tags:** Iniciante | Análise | SEO, Analítica & Dados
