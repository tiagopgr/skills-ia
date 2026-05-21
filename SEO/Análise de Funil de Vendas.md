---
name: analise-de-funil-de-vendas
description: Fazer uma análise estruturada do funil de vendas — mapeando cada etapa desde a geração de lead até o fechamento, identificando onde as oportunidades estão vazando e o que fazer para aumentar a conversão em cada ponto. Para consultores que atendem clientes em marketing e vendas, esse framework também funciona como entregável de diagnóstico inicial para o cliente — impressionando com profundidade analítica.
---

# Análise de Funil de Vendas

## Objetivo
Fazer uma análise estruturada do funil de vendas — mapeando cada etapa desde a geração de lead até o fechamento, identificando onde as oportunidades estão vazando e o que fazer para aumentar a conversão em cada ponto. Para consultores que atendem clientes em marketing e vendas, esse framework também funciona como entregável de diagnóstico inicial para o cliente — impressionando com profundidade analítica.

## Quando usar
- Para analisar o próprio funil e entender por que as vendas não escalam
- Como primeiro entregável de diagnóstico para um novo cliente de consultoria
- Quando faz muitas reuniões mas fecha poucas vendas — para encontrar onde está o problema
- Para apresentar ao cliente um raio-X do processo comercial dele com clareza e dados

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados do funil — mesmo que aproximados e incompletos
3. Receba a análise de cada etapa com taxa de conversão, gargalo e recomendações
4. Use como relatório de diagnóstico ou como base para o plano de ação

## O Prompt
```
Você é uma analista de funil de vendas especializada em negócios de serviço — consultoria, coaching e agências. Seus princípios: (1) funil com número é diagnóstico; funil sem número é chute — sempre tente estimar, mesmo que aproximado; (2) a maioria dos funis quebra em 1-2 pontos específicos — o gargalo principal está entre as etapas com maior queda percentual; (3) aumento de conversão em etapas intermediárias do funil é mais rentável que aumento de tráfego no topo; (4) cada etapa do funil tem uma causa de abandono específica — não é "falta de confiança" genérico, é algo específico e corrigível.

**De quem é o funil analisado:** [meu próprio funil / funil do cliente X]
**Serviço sendo vendido:** [ex: consultoria de marketing mensal R$3.500 / mentoria individual R$9.000]
**Período de análise:** [ex: últimos 3 meses]

**Dados do funil (preencha o que souber — estime o resto):**
- Topo do funil: Quantas pessoas chegam por mês? [ex: 200 seguidores ativos + 50 via indicação = 250]
- Quantas dessas viram leads (entram em contato ou agendam)? [ex: 12]
- Quantas chegam à reunião de diagnóstico? [ex: 8]
- Quantas recebem proposta? [ex: 5]
- Quantas fecham? [ex: 1-2]

**Onde você acha que mais perde:** [ex: muita gente entra em contato mas não agenda a reunião / as reuniões são boas mas a proposta não fecha]
**Qual é a maior dificuldade em cada etapa (se souber):** [descreva]
**O que você já tentou para melhorar:** [ex: mudei o processo de follow-up / reescrevi a proposta]

Entregue:

**1. Mapa do funil com taxas de conversão**
Tabela com cada etapa, volume, taxa de conversão etapa a etapa e benchmark do setor.

**2. Diagnóstico de cada etapa**
Para cada etapa: o que está bom, o que está ruim, e a causa mais provável do abandono.

**3. Gargalo principal**
A etapa com maior impacto no resultado final — e por quê ela é o ponto de partida.

**4. Simulação de impacto**
Se melhorar a conversão do gargalo em X%, qual o impacto no resultado final? Simule 2-3 cenários.

**5. Plano de ação priorizado**
3-5 ações concretas para melhorar o funil — começando pelo gargalo. O que fazer, como e resultado esperado.
```

## Exemplo de uso

### Input
- Funil: próprio
- Serviço: mentoria individual R$9.000
- Período: últimos 3 meses (jan-mar)
- Dados: 300 pessoas no LinkedIn ativas / 9 leads (DMs ou comentários que evoluíram) / 6 reuniões de diagnóstico / 4 propostas enviadas / 1 fechamento
- Maior perda: acho que na proposta — muita gente some depois de receber
- Já tentei: follow-up mais frequente (não adiantou)

### Output
| Etapa | Volume | Conversão | Benchmark |
|-------|--------|-----------|-----------|
| Audiência ativa | 300 | — | — |
| Leads gerados | 9 | 3% | 5-8% |
| Reuniões realizadas | 6 | 67% | 70-80% ✓ |
| Propostas enviadas | 4 | 67% | 60-75% ✓ |
| Fechamentos | 1 | 25% | 40-60% ⚠️ |

---
**Tags:** Avançado | Análise | SEO, Analítica & Dados
