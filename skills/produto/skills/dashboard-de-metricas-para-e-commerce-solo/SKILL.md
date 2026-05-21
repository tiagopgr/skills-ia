---
name: dashboard-de-metricas-para-e-commerce-solo
description: Criar um sistema simples e prático de acompanhamento de métricas para um e-commerce tocado por uma pessoa só — identificando os 10-15 números que realmente importam para crescer, com modelo de planilha, frequência de acompanhamento e critérios de decisão — para parar de trabalhar no escuro e começar a tomar decisões baseadas em dados reais.
---

# Dashboard de Métricas para E-commerce Solo

## Objetivo
Criar um sistema simples e prático de acompanhamento de métricas para um e-commerce tocado por uma pessoa só — identificando os 10-15 números que realmente importam para crescer, com modelo de planilha, frequência de acompanhamento e critérios de decisão — para parar de trabalhar no escuro e começar a tomar decisões baseadas em dados reais.

## Quando usar
- Quando quiser entender por que o faturamento sobe ou cai sem saber o motivo
- Para saber exatamente quais produtos, canais e campanhas estão gerando resultado
- Quando começar a investir em tráfego pago e precisar saber se está tendo retorno
- Para ter uma visão semanal e mensal do negócio sem precisar de planilha complexa
- Sempre que quiser tomar decisões de produto, preço ou marketing com base em dados

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os canais de venda que usa, o volume atual e as métricas que já acompanha (se alguma)
3. Receba o modelo completo de dashboard com as métricas, fórmulas e critérios de decisão
4. Monte a planilha no Google Sheets e preencha toda semana — máx 15 minutos por semana

## O Prompt
```
Você é um analista de e-commerce especializado em negócios tocados por empreendedores solo. Seus princípios: (1) menos métricas, melhor — 10 números certos valem mais que 50 métricas que ninguém acompanha, (2) a métrica mais importante varia por estágio do negócio — identifique o gargalo antes de definir o que medir, (3) frequência de acompanhamento deve ser diária para operação e semanal/mensal para estratégia, (4) toda métrica precisa de um critério de decisão — "se esse número cair abaixo de X, faço Y".

Crie um sistema de métricas e dashboard com os seguintes dados:

**Canais de venda:** [Mercado Livre / Shopee / loja própria / WhatsApp / outros]
**Investe em tráfego pago?** [sim — quanto por mês / não]
**Volume atual:** [pedidos por dia / faturamento mensal aproximado]
**Métricas que já acompanha:** [o que você olha hoje, mesmo que informalmente]
**Principal objetivo do negócio agora:** [aumentar faturamento / melhorar margem / escalar anúncios / organizar operação]
**Ferramentas disponíveis:** [Google Sheets / Excel / Notion / nenhuma ainda]

Entregue:

**1. As 10 métricas essenciais para o seu negócio**
Para cada métrica:
- Nome e definição simples
- Como calcular (fórmula)
- Onde buscar o dado
- Frequência de acompanhamento (diário / semanal / mensal)
- Benchmark ou meta sugerida
- Critério de decisão: "se esse número estiver assim, faço isso"

**2. Modelo de planilha (estrutura)**
Estrutura completa das abas e colunas da planilha — pronta para montar no Google Sheets

**3. Rotina de análise semanal (15 minutos)**
Checklist do que verificar toda semana, em que ordem e o que fazer com cada informação

**4. Diagnóstico rápido mensal (30 minutos)**
Perguntas que você deve responder todo mês olhando para os dados — com o raciocínio de decisão para cada uma

**5. Sinais de alerta**
5 combinações de métricas que indicam problema iminente e o que fazer quando aparecerem

**6. Primeiro passo (para quem não acompanha nada hoje)**
O único número mais importante para começar a olhar agora, antes de montar o dashboard completo
```

## Exemplo de uso

### Input
- Canais: Mercado Livre + Instagram (vendas via DM) + Meta Ads
- Tráfego pago: Sim — R$1.500/mês em Meta Ads
- Volume: 8-12 pedidos/dia, ~R$15.000/mês faturamento
- Métricas acompanhadas: nenhuma formalmente, olha o faturamento do dia no app
- Objetivo: Aumentar faturamento e entender se os anúncios estão dando retorno
- Ferramentas: Google Sheets

### Output
Nome: ROAS (Retorno sobre Investimento em Anúncios)
Definição: Quanto você fatura para cada R$1 investido em anúncio
Fórmula: Faturamento atribuído ao anúncio ÷ Investimento em anúncio
Onde buscar: Gerenciador de Anúncios do Meta (coluna "Valor de conversão de compras")
Frequência: Semanal
Meta recomendada: ROAS ≥ 3 (fatura R$3 para cada R$1 investido)
Critério de decisão: Se ROAS < 2 por 2 semanas seguidas → pausar o conjunto de anúncios e testar novo criativo. Se ROAS > 5 → aumentar orçamento em 20%.

---
**Tags:** Intermediário | Análise | Produto, E-commerce & SaaS
