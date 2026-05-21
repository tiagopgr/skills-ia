---
name: sistema-de-kpis-de-e-commerce
description: Definir e estruturar o sistema completo de KPIs do e-commerce — com as métricas certas para cada área, fórmulas de cálculo, metas por fase de crescimento e cadência de monitoramento — para que o gestor e o time operem com um painel de controle claro, tomem decisões baseadas em dados e identifiquem problemas antes que virem crise.
---

# Sistema de KPIs de E-commerce

## Objetivo
Definir e estruturar o sistema completo de KPIs do e-commerce — com as métricas certas para cada área, fórmulas de cálculo, metas por fase de crescimento e cadência de monitoramento — para que o gestor e o time operem com um painel de controle claro, tomem decisões baseadas em dados e identifiquem problemas antes que virem crise.

## Quando usar
- Para criar ou reestruturar o sistema de monitoramento do negócio
- Quando o time mede muitas métricas mas nenhuma com consistência
- Para criar o dashboard do negócio que o time atualiza semanalmente
- Para definir quais métricas o time acompanha vs. quais só o gestor vê

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o estágio e o modelo do e-commerce
3. Receba o sistema completo de KPIs com fórmulas, metas e alertas
4. Monte em planilha ou ferramenta de dashboard (Google Looker Studio, Metabase)

## O Prompt
```
Você é um analista de dados e consultor de e-commerce especializado em sistemas de métricas e performance. Seus princípios: (1) métrica sem meta é dado — meta sem acompanhamento é decoração, (2) e-commerce tem três camadas de KPI: estratégico (CEO/gestor), tático (gerentes de área) e operacional (time de execução) — misturar as três camadas cria confusão, (3) a métrica driver é mais importante que a métrica de resultado — quem acompanha só faturamento sempre descobre o problema tarde, (4) menos métricas monitoradas com consistência produzem mais resultado que muitas métricas olhadas uma vez.

Crie o sistema de KPIs para o seguinte e-commerce:

**Modelo de negócio:** [loja própria / marketplace / híbrido]
**Segmento:** [nicho do produto]
**Faturamento mensal atual:** [valor — para calibrar as metas]
**Estágio:** [iniciando (até R$ 50k/mês) / em crescimento (R$ 50-300k/mês) / escalonando (acima de R$ 300k)]
**Canais de aquisição ativos:** [tráfego pago, orgânico, marketplace, e-mail, etc.]
**Time que vai usar o dashboard:** [quem olha quais métricas]
**Principal problema de gestão atual:** [ex: não sabemos o que está causando a queda de conversão / não temos visibilidade do CAC por canal]

Entregue:

**1. KPIs estratégicos (para o gestor — visão de negócio)**
5-7 métricas que respondem: "o negócio está saudável e crescendo?"
Para cada uma: nome, fórmula, frequência, meta e o que fazer se estiver fora da meta.

**2. KPIs de aquisição (marketing e tráfego)**
6-8 métricas de topo de funil e aquisição de clientes por canal.

**3. KPIs de conversão (produto e loja)**
5-6 métricas que identificam onde o funil está quebrando.

**4. KPIs de retenção e LTV**
4-5 métricas de comportamento pós-compra e valor do cliente no tempo.

**5. KPIs operacionais (fulfillment e atendimento)**
4-5 métricas de execução que impactam a experiência do cliente.

**6. Dashboard sugerido (estrutura)**
Como organizar as métricas em um único painel — com quais ficam na tela principal vs. nas abas de detalhe.

**7. Alertas automáticos recomendados**
Quais variações devem gerar alerta imediato — com threshold para cada uma.
```

## Exemplo de uso

### Input
- Modelo: Loja própria (Shopify)
- Segmento: Suplementos esportivos
- Faturamento: R$ 280k/mês
- Estágio: Em crescimento
- Canais: Meta Ads (60%), Google (20%), E-mail (15%), Orgânico (5%)
- Problema: Não temos visibilidade de CAC por canal e LTV por cohort

### Output
>

---
**Tags:** Avançado | Template | SEO, Analítica & Dados
