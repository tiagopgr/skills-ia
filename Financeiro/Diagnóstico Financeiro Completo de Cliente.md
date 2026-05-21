---
name: diagnostico-financeiro-completo-de-cliente
description: Conduzir um diagnóstico financeiro estruturado e aprofundado de clientes de consultoria — mapeando a situação atual, identificando gargalos, causas-raiz dos problemas e oportunidades de melhoria — para que o consultor entregue uma análise que vai além dos números e mostra ao cliente exatamente onde o dinheiro está escapando e o que fazer primeiro.
---

# Diagnóstico Financeiro Completo de Cliente

## Objetivo
Conduzir um diagnóstico financeiro estruturado e aprofundado de clientes de consultoria — mapeando a situação atual, identificando gargalos, causas-raiz dos problemas e oportunidades de melhoria — para que o consultor entregue uma análise que vai além dos números e mostra ao cliente exatamente onde o dinheiro está escapando e o que fazer primeiro.

## Quando usar
- Na entrada de um novo cliente para entender a situação financeira real
- Quando um cliente apresenta problema de caixa mas não sabe a causa
- Quando quiser estruturar um relatório diagnóstico de alto impacto
- Quando precisar transformar dados financeiros brutos em insights acionáveis
- Quando quiser diferenciar sua entrega de uma análise contábil comum

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados financeiros do cliente (DRE, fluxo de caixa, indicadores)
3. Receba o diagnóstico estruturado com análise, causas e recomendações
4. Use como base para a apresentação ao cliente

## O Prompt
```
Você é um consultor financeiro sênior com 15 anos de experiência em diagnóstico e turnaround financeiro de empresas. Seus princípios: (1) número sem contexto é dado — contexto sem número é opinião: o diagnóstico precisa dos dois, (2) todo problema financeiro tem uma causa-raiz comportamental ou estrutural — encontre ela antes de recomendar qualquer ação, (3) o cliente não quer saber o que está errado — quer saber o que fazer, em que ordem e com qual impacto esperado, (4) diagnóstico que não cabe numa conversa de 30 minutos não vai ser implementado.

Faça um diagnóstico financeiro completo com as seguintes informações do cliente:

**Perfil do negócio:** [tipo de empresa, segmento, porte, tempo de mercado]
**Faturamento mensal atual:** [R$ médio dos últimos 3-6 meses]
**Principais custos fixos:** [liste com valores]
**Principais custos variáveis:** [liste com valores ou % do faturamento]
**Margem de contribuição estimada:** [% ou valor por produto/serviço]
**Situação de caixa:** [positivo, negativo, quanto de reserva]
**Endividamento:** [tem dívidas? quais? juros? prazo?]
**Inadimplência de clientes:** [% aproximado]
**Ticket médio e volume de vendas:** [dados disponíveis]
**Principal queixa do cliente:** [o que ele diz que está acontecendo de errado]
**Dados adicionais disponíveis:** [cole DRE, fluxo de caixa ou qualquer dado que tiver]

Entregue:

**1. Retrato financeiro atual**
Resumo executivo do estado financeiro do negócio em linguagem clara — o que os números dizem antes de qualquer interpretação.

**2. Mapa de gargalos**
Tabela com:
| Gargalo identificado | Impacto estimado (R$ ou %) | Urgência (Alta/Média/Baixa) | Causa-raiz provável |

**3. Análise de causa-raiz**
Para os 3 principais gargalos: por que está acontecendo (estrutural, comportamental, mercado) — sem suposição sem base nos dados.

**4. Recomendações priorizadas**
Lista numerada do que fazer, do mais impactante para o menos — com:
- Ação específica
- Impacto financeiro esperado
- Prazo realista de implementação
- Responsável (cliente ou consultor)

**5. Indicadores para monitorar**
5-8 KPIs financeiros que o cliente deve acompanhar mensalmente, com referência de onde deveriam estar.
```

## Exemplo de uso

### Input
- Negócio: Clínica odontológica, 8 anos de mercado, 3 dentistas sócios
- Faturamento: R$95.000/mês (média últimos 6 meses)
- Custos fixos: R$62.000 (salários, aluguel, equipamentos)
- Margem: ~35%
- Caixa: Negativo, cheque especial ativo há 4 meses
- Dívida: R$180.000 em equipamentos (juros 1,8%/mês)
- Inadimplência: ~18%
- Queixa: "Atendo bem, fatura razoável, mas não sobra nada"

### Output
"Gargalo #1 — Inadimplência de 18%: A clínica está financiando os tratamentos dos pacientes involuntariamente. Com faturamento de R$95k, 18% inadimplente = R$17.100/mês que entra no DRE mas não entra no caixa. Causa-raiz: ausência de política de crédito e cobrança — parcelamentos feitos sem critério, sem contrato e sem processo de acompanhamento. Não é problema de vendas. É problema de gestão de recebíveis..."

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
