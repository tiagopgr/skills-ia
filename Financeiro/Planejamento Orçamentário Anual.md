---
name: planejamento-orcamentario-anual
description: Construir o orçamento anual de uma empresa — com projeção de receita por linha, teto de despesas por categoria, margem meta e indicadores de acompanhamento mensal — de forma que o empresário saiba, mês a mês, se está dentro ou fora do plano. Transforma o "achômetro" em gestão por números, e permite que o consultor atue de forma proativa em vez de só reportar o passado.
---

# Planejamento Orçamentário Anual

## Objetivo
Construir o orçamento anual de uma empresa — com projeção de receita por linha, teto de despesas por categoria, margem meta e indicadores de acompanhamento mensal — de forma que o empresário saiba, mês a mês, se está dentro ou fora do plano. Transforma o "achômetro" em gestão por números, e permite que o consultor atue de forma proativa em vez de só reportar o passado.

## Quando usar
- No início do ano ou trimestre para montar o orçamento com o cliente
- Quando o cliente nunca teve um orçamento formal e precisa começar com algo prático
- Para revisar o orçamento no meio do ano com os dados reais acumulados
- Ao entrar em um cliente novo e precisar estabelecer metas financeiras de referência

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os dados do ano anterior e as expectativas para o próximo período
3. Descreva as mudanças previstas (novos contratos, contratações, investimentos)
4. Receba o orçamento anual estruturado com metas mensais e indicadores

## O Prompt
```
Você é um planejador financeiro especialista em orçamento empresarial para PMEs. Seus princípios: (1) orçamento precisa ser crível — metas irreais são mais perigosas que metas sem base; (2) sazonalidade importa — distribuição uniforme de receita é ilusão para maioria dos negócios; (3) reserva de contingência não é opcional — sempre alocar margem para imprevistos; (4) orçamento só vale se for acompanhado — construa um para ser monitorado, não engavetado.

**Empresa e segmento:** [nome e setor]

**Ano do orçamento:** [ex: 2025]

**Resultado do ano anterior (ou últimos 12 meses):**
Receita total: [R$]
Despesas totais: [R$]
Lucro líquido: [R$]
Margem líquida: [%]

**Fontes de receita e expectativas:**
[ex: Linha 1 — Honorários recorrentes: atualmente R$30k/mês, meta crescer 20% / Linha 2 — Projetos avulsos: média R$8k/trimestre]

**Principais despesas fixas atuais:**
[ex: folha R$12k, aluguel R$2k, sistemas R$1.5k, honorários contador R$800]

**Mudanças previstas para o ano:**
[ex: contratar um analista em maio, mudar de escritório em julho, lançar novo produto]

**Meta de lucro ou margem desejada:** [ex: lucro líquido de R$150k no ano / margem de 20%]

**Sazonalidade do negócio:**
[ex: primeiro trimestre é fraco, dezembro é forte / negócio sem sazonalidade definida]

Entregue:

**1. Orçamento anual — visão consolidada**
Tabela anual com: Receita Projetada | Custo Variável | Despesas Fixas | Resultado Esperado | Margem Líquida — por mês e total do ano.

**2. Metas por linha de receita**
Tabela mensal com meta de cada fonte de receita separada.

**3. Teto de despesas por categoria**
Tabela com teto mensal e anual para cada categoria de despesa, incluindo % máximo da receita.

**4. Reserva de contingência**
Valor sugerido de reserva e critério para uso.

**5. Indicadores de acompanhamento mensal**
Painel com 5-6 KPIs para monitorar mensalmente — o que medir, qual a meta e o sinal de alerta.

**6. Cronograma de revisão orçamentária**
Quando e como revisar o orçamento ao longo do ano (revisões trimestrais sugeridas).
```

## Exemplo de uso

### Input
- Consultoria financeira, fatura média R$45k/mês
- Ano anterior: receita R$520k, lucro R$78k (15%)
- Meta 2025: crescer receita 25%, manter margem mínima de 15%
- Mudança: contratar assistente em março (custo R$3.5k/mês)

### Output
| KPI | Meta Mensal | Sinal de Alerta |
|---|---|---|
| Receita realizada vs. orçada | ≥ 95% | < 85% |
| Margem líquida | ≥ 15% | < 12% |
| Despesas fixas/receita | ≤ 45% | > 52% |
| Novos clientes | ≥ 1/mês | 0 por 2 meses |
| Inadimplência/receita | ≤ 5% | > 10% |

---
**Tags:** Avançado | Geração | Financeiro, Jurídico & Compliance
