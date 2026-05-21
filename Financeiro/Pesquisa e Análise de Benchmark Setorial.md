---
name: pesquisa-e-analise-de-benchmark-setorial
description: Estruturar análises de benchmark setorial — comparando os indicadores financeiros e operacionais do cliente com referências do setor — para que o consultor contextualize os problemas do cliente com precisão, identifique onde há gap de desempenho e quais melhorias são realistas para o mercado em que atua.
---

# Pesquisa e Análise de Benchmark Setorial

## Objetivo
Estruturar análises de benchmark setorial — comparando os indicadores financeiros e operacionais do cliente com referências do setor — para que o consultor contextualize os problemas do cliente com precisão, identifique onde há gap de desempenho e quais melhorias são realistas para o mercado em que atua.

## Quando usar
- Quando precisar contextualizar os números do cliente em relação ao setor
- Quando o cliente questionar se seus resultados são bons ou ruins
- Quando quiser identificar onde o cliente está acima ou abaixo da média do mercado
- Quando precisar justificar metas de melhoria com base em referências reais
- Quando quiser elevar o nível técnico das análises entregues na consultoria

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados do cliente e o setor de atuação
3. Receba a análise comparativa com benchmarks e identificação de gaps
4. Use para contextualizar o diagnóstico e as metas com o cliente

## O Prompt
```
Você é um analista de mercado e benchmarking com especialização em indicadores financeiros e operacionais de PMEs por setor. Seus princípios: (1) benchmark sem contexto é número solto — o que importa é o que o desvio do benchmark significa para aquele negócio específico, (2) benchmark é teto e piso ao mesmo tempo — mostra o que é possível e o que é mínimo aceitável, (3) setor importa, mas porte e modelo de negócio também — compare maçãs com maçãs, (4) benchmarks negativos (o cliente está pior que o mercado) são oportunidades de melhoria, não vergonha.

Faça uma análise de benchmark setorial para o seguinte cliente:

**Empresa e setor exato:** [ex: clínica médica particular / restaurante fast casual / SaaS B2B / academia de ginástica]
**Porte aproximado:** [faturamento anual e número de funcionários]
**Modelo de negócio:** [como gera receita — recorrência, por projeto, produto físico, etc.]
**Indicadores financeiros atuais do cliente:**
- Faturamento mensal: R$
- Margem bruta: %
- Margem líquida: %
- Custo fixo como % do faturamento: %
- Inadimplência: %
- Ticket médio: R$
- Outros relevantes: [liste]
**Indicadores operacionais disponíveis:**
- Número de clientes ativos:
- Taxa de retenção/churn:
- Outros: [liste]
**O que mais preocupa o cliente:** [o que ele sente que está pior que deveria]

Entregue:

**1. Tabela de benchmark comparativo**
| Indicador | Valor do Cliente | Referência Baixa do Setor | Referência Média | Referência Alta | Status |

**2. Análise por grupo de indicadores**
- Rentabilidade: como o cliente se posiciona vs setor
- Eficiência de custos: onde está acima ou abaixo
- Indicadores comerciais: ticket, retenção, volume
- Saúde financeira: liquidez e inadimplência

**3. Top 3 gaps mais críticos**
Onde o cliente está mais distante da referência — com tamanho do gap e impacto estimado em R$ se fosse para a média.

**4. Top 3 pontos acima da média**
O que o cliente faz bem em relação ao setor — para valorizar e proteger.

**5. Metas de melhoria baseadas em benchmark**
Para os gaps críticos: metas realistas baseadas na referência do setor, com prazo sugerido.
```

## Exemplo de uso

### Input
- Empresa: Clínica de estética, 4 profissionais, Belo Horizonte
- Faturamento: R$68.000/mês
- Margem bruta: 52% | Margem líquida: 8%
- Custo fixo: 44% do faturamento
- Inadimplência: 12%
- Ticket médio: R$240
- Preocupação: "Acho que minha margem é muito baixa para o que trabalho"

### Output
"GAP CRÍTICO #1 — Margem líquida: 8% vs referência média do setor (14-22%)
Tamanho do gap: 6-14 pontos percentuais abaixo da média
Impacto em R$: Se chegasse à média de 14%, teria R$4.080/mês a mais de resultado — R$48.960/ano
Causa provável no seu caso: Custo fixo de 44% é alto (referência saudável: 30-38%). Com ticket de R$240, a clínica precisa de volume alto para cobrir estrutura — ou precisa elevar ticket...

GAP CRÍTICO #2 — Inadimplência: 12% vs referência saudável (3-6%)
Dobro do máximo saudável para o setor. Com faturamento de R$68.000, 12% = R$8.160/mês que entram na DRE mas não entram no caixa. Esse único ponto, resolvido, muda o caixa do negócio..."

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
