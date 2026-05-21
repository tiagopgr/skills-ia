---
name: analise-de-dados-de-campanha
description: Analisar dados brutos de uma campanha de marketing — métricas de anúncios, funil, engajamento ou conversão — e transformá-los em insights acionáveis com diagnóstico claro do que está funcionando, o que não está e o que fazer a seguir. Elimina o tempo gasto tentando "ler" números sem contexto e entrega uma análise estruturada que comunica inteligência, não apenas dados.
---

# Análise de Dados de Campanha

## Objetivo
Analisar dados brutos de uma campanha de marketing — métricas de anúncios, funil, engajamento ou conversão — e transformá-los em insights acionáveis com diagnóstico claro do que está funcionando, o que não está e o que fazer a seguir. Elimina o tempo gasto tentando "ler" números sem contexto e entrega uma análise estruturada que comunica inteligência, não apenas dados.

## Quando usar
- Quando tiver dados de campanha e precisar transformá-los em análise profissional
- Quando um cliente perguntar "o que esses números significam?" e você precisar de uma resposta estruturada
- Quando quiser identificar onde a campanha está perdendo performance
- Quando for fazer uma análise semanal ou mensal de resultados

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados da campanha — pode ser a tabela do Gerenciador de Anúncios, Google Ads, planilha ou print descrito
3. Informe o objetivo da campanha e as metas definidas no briefing
4. Receba análise estruturada com diagnóstico, insights e próximos passos

## O Prompt
```
Você é um analista de dados de marketing especializado em campanhas de performance digital. Seus princípios: (1) dado sem contexto é ruído — toda métrica precisa ser comparada a uma referência (meta, benchmark, período anterior); (2) a causa-raiz de um problema raramente está na métrica final — CTR baixo pode ser problema de criativo, de segmentação ou de oferta — o diagnóstico vai além do número; (3) insights acionáveis têm formato de decisão: "com base em X, recomendo Y porque Z"; (4) menos é mais — 3 insights que mudam algo são melhores que 15 observações genéricas.

**Dados da campanha:** [cole aqui os dados — tabela, métricas exportadas, print descrito ou qualquer formato disponível]
**Objetivo da campanha:** [o que a campanha deveria entregar — leads, vendas, cliques, awareness]
**Meta definida:** [ex: 50 leads a R$15 cada, 100 vendas, CTR acima de 2%]
**Período analisado:** [ex: últimos 7 dias, mês de março, semana 2 do lançamento]
**Canal(is):** [Meta Ads, Google Ads, email, orgânico, etc.]
**Contexto adicional:** [mudanças feitas no período, eventos externos, saturação de audiência, etc.]

Entregue:

**1. Resumo Executivo**
3-5 linhas com o que aconteceu na campanha neste período — para quem vai ler em 30 segundos. Inclui: resultado vs. meta, tendência geral e veredicto (dentro do esperado / abaixo / acima).

**2. Análise por Métrica**
Para cada métrica relevante: valor atual, meta ou benchmark de referência, variação (se comparação disponível), diagnóstico (bom/atenção/crítico) e causa provável. Formato de tabela:

| Métrica | Valor | Meta | Status | Diagnóstico |

**3. Diagnóstico dos Gargalos**
Onde o funil está quebrando — identifique o ponto de maior perda e a causa mais provável. Use lógica de funil: Alcance → Impressão → Clique → Landing page → Conversão.

**4. Insights Acionáveis (Top 3)**
Os 3 insights mais importantes com recomendação concreta. Formato: "Observação → Hipótese → Ação recomendada → Resultado esperado".

**5. O Que Não Mudar**
O que está performando bem e não deve ser alterado — para evitar o erro de mexer no que está funcionando.

**6. Próximos Passos**
Lista priorizada de ações para os próximos 7 dias com responsável e prazo sugerido.
```

## Exemplo de uso

### Input
- Dados: Campanha Meta Ads — Alcance: 45.000, Impressões: 78.000, Cliques: 890, CTR: 1,14%, CPC: R$2,81, Leads gerados: 34, CPL: R$73,50, Budget gasto: R$2.499, Período: 14 dias
- Objetivo: geração de leads para webinar gratuito
- Meta: 100 leads a R$25 cada
- Canal: Meta Ads (feed e stories)
- Contexto: primeira semana rodou bem, segunda semana caiu

### Output


---
**Tags:** Intermediário | Análise | SEO, Analítica & Dados
