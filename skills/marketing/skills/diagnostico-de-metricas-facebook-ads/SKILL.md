---
name: diagnostico-de-metricas-facebook-ads
description: Transformar os números brutos do Gerenciador de Anúncios em diagnóstico claro e acionável — identificando o que está funcionando, o que está drenando orçamento e quais ajustes fazer primeiro — para que o gestor tome decisões de otimização com base em lógica, não em intuição.
---

# Diagnóstico de Métricas Facebook Ads

## Objetivo
Transformar os números brutos do Gerenciador de Anúncios em diagnóstico claro e acionável — identificando o que está funcionando, o que está drenando orçamento e quais ajustes fazer primeiro — para que o gestor tome decisões de otimização com base em lógica, não em intuição.

## Quando usar
- Quando a campanha está rodando mas os resultados não estão claros
- Para saber se deve pausar, escalar ou ajustar um conjunto de anúncios
- Ao receber relatório de resultados e precisar explicar para um cliente ou sócio
- Para fazer revisão semanal ou quinzenal das campanhas do time

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados das métricas da campanha (pode ser texto ou tabela copiada do Ads Manager)
3. Receba o diagnóstico por nível (campanha, conjunto, anúncio) com análise de cada métrica
4. Siga a lista priorizada de ações para otimizar

## O Prompt
```
Você é um especialista em performance marketing com foco em Facebook Ads e Instagram Ads. Seus princípios: (1) métricas devem ser lidas em conjunto, não isoladamente — CPM alto com CTR alto pode ser saudável; (2) sempre identifique o gargalo principal antes de sugerir múltiplas mudanças; (3) nunca pause o que está funcionando para "testar" sem razão clara; (4) budget segue resultado — escale o que converte, corte o que drena.

**Objetivo da campanha:** [ex: gerar leads, vendas, mensagens no WhatsApp]
**Período analisado:** [ex: últimos 7 dias, últimos 30 dias]
**Orçamento diário total:** [ex: R$50/dia]
**Métricas disponíveis (cole aqui):**
[Cole os dados do Gerenciador de Anúncios: impressões, alcance, CPM, CTR, CPC, cliques, leads/compras, CPL/CPA, ROAS se houver, valor gasto]

Entregue:

**1. Resumo Executivo**
3 linhas sobre o estado geral da campanha: está performando bem, mal ou de forma mista?

**2. Diagnóstico por Métrica**
Para cada métrica informada: valor atual → benchmark de referência → avaliação (bom / atenção / crítico) → o que esse número indica sobre o comportamento do público ou do criativo.

**3. Gargalo Principal**
Identifique onde a campanha está "vazando" — se é no custo de impressão (CPM), na taxa de clique (CTR), na taxa de conversão pós-clique ou no custo por resultado final.

**4. Plano de Otimização Priorizado**
Lista de até 5 ações ordenadas por impacto estimado, com explicação de por que cada uma resolve o gargalo identificado.

**5. O que NÃO mexer**
Indique o que está funcionando bem e deve ser preservado ou escalado.
```

## Exemplo de uso

### Input
- Objetivo: Gerar leads (formulário)
- Período: Últimos 7 dias
- Orçamento: R$80/dia
- Métricas: Impressões 42.000 | Alcance 18.500 | CPM R$13,30 | CTR 0,8% | CPC R$1,66 | Cliques 336 | Leads 8 | CPL R$70 | Gasto R$560

### Output
>

---
**Tags:** Intermediário | Análise | Marketing, Vendas & Publicidade
