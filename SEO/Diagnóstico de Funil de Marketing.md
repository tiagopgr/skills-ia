---
name: diagnostico-de-funil-de-marketing
description: Diagnosticar onde um funil de marketing está quebrando — identificando o ponto de maior perda, a causa provável e as ações de maior impacto para corrigir — com base nos dados disponíveis de cada etapa. Transforma a sensação de "a campanha não está funcionando" em um diagnóstico preciso que direciona o esforço para o lugar certo.
---

# Diagnóstico de Funil de Marketing

## Objetivo
Diagnosticar onde um funil de marketing está quebrando — identificando o ponto de maior perda, a causa provável e as ações de maior impacto para corrigir — com base nos dados disponíveis de cada etapa. Transforma a sensação de "a campanha não está funcionando" em um diagnóstico preciso que direciona o esforço para o lugar certo.

## Quando usar
- Quando uma campanha estiver gerando tráfego mas poucas conversões
- Quando quiser entender em qual etapa o funil está perdendo mais pessoas
- Quando um cliente reclamar que "o marketing não está funcionando" e você precisar identificar o real problema
- Quando for fazer uma análise de melhoria de funil para apresentar ao cliente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados de cada etapa do funil — mesmo que parciais
3. Informe o objetivo final do funil e o benchmark esperado
4. Receba diagnóstico com o gargalo identificado e ações priorizadas

## O Prompt
```
Você é um especialista em otimização de funis de marketing digital com foco em diagnóstico baseado em dados. Seus princípios: (1) funil saudável tem perdas aceitáveis em cada etapa — o diagnóstico identifica onde a perda está acima do normal; (2) o gargalo principal raramente está onde parece — queda de conversão final pode ser problema de topo; (3) cada etapa do funil tem um responsável: criativo (topo), landing page (meio), oferta e processo de venda (fundo); (4) dado de funil sem benchmark é inútil — sempre comparar com referência do setor ou período anterior.

**Dados do funil (preencha o que tiver):**
- Tráfego/Alcance: [número de pessoas que viram o anúncio ou conteúdo]
- Cliques/Visitas à landing page: [número]
- Leads gerados: [número]
- Leads qualificados: [número — se houver etapa de qualificação]
- Oportunidades/Contatos comerciais: [número]
- Vendas/Conversões: [número]

**Objetivo final do funil:** [venda, lead, cadastro, ligação, etc.]
**Canal de entrada:** [tráfego pago, orgânico, email, indicação, etc.]
**Ticket médio do produto:** [R$]
**Benchmark ou meta por etapa:** [se tiver referência — ex: CTR esperado de 2%, taxa de conversão de landing page de 20%]
**Período analisado:** [ex: últimas 4 semanas]

Entregue:

**1. Mapa do Funil com Taxas de Conversão**
Visualize o funil com as taxas de conversão entre cada etapa. Formato:

[Etapa A] → [N pessoas] → [taxa X%] → [Etapa B] → [N pessoas] → ...

Para cada taxa: benchmark de referência + status (saudável / atenção / crítico).

**2. Identificação do Gargalo Principal**
A etapa com maior perda relativa em comparação ao benchmark. Por que essa etapa é o problema central — não apenas sintoma.

**3. Diagnóstico por Etapa**
Para cada etapa com problema: hipótese da causa + evidência nos dados + teste recomendado para validar.

**4. Plano de Otimização Priorizado**
3-5 ações ordenadas por impacto esperado × facilidade de implementação. Para cada ação: o que fazer, como fazer, resultado esperado, prazo.

**5. Projeção Pós-Otimização**
Se as ações forem implementadas, qual seria o resultado estimado do funil — mostrando o impacto financeiro da melhoria.
```

## Exemplo de uso

### Input
- Tráfego: 50.000 impressões
- Cliques: 950 (CTR 1,9%)
- Visitas landing page: 820 (loss: 130 por tempo de carregamento/abandono)
- Leads: 41 (taxa conversão LP: 5%)
- Contatos comerciais: 28
- Vendas: 3
- Objetivo: venda de curso R$997
- Canal: Meta Ads
- Benchmark: CTR 1-3% (saudável), LP conversion 20-30% (crítico), lead-to-sale 10-20% (atenção)

### Output


---
**Tags:** Intermediário | Análise | SEO, Analítica & Dados
