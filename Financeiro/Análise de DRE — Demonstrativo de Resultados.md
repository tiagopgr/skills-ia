---
name: analise-de-dre-demonstrativo-de-resultados
description: Receber os dados do Demonstrativo de Resultado do Exercício (DRE) de uma empresa e transformá-los em análise gerencial completa — com interpretação de margens, comparativo de períodos, identificação de gargalos de rentabilidade e recomendações práticas. Transforma números contábeis em inteligência de negócio que o empresário consegue usar para tomar decisões.
---

# Análise de DRE — Demonstrativo de Resultados

## Objetivo
Receber os dados do Demonstrativo de Resultado do Exercício (DRE) de uma empresa e transformá-los em análise gerencial completa — com interpretação de margens, comparativo de períodos, identificação de gargalos de rentabilidade e recomendações práticas. Transforma números contábeis em inteligência de negócio que o empresário consegue usar para tomar decisões.

## Quando usar
- Ao receber o DRE de um cliente e precisar preparar a análise para a reunião mensal
- Para comparar o desempenho de dois períodos e identificar o que mudou
- Quando o cliente pergunta "estou lucrando ou não?" e precisa de uma resposta clara
- Para auditar o DRE de um cliente novo e identificar distorções ou problemas de classificação

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados do DRE (pode ser em tabela simples ou copiado do sistema)
3. Informe o segmento e contexto do período
4. Receba a análise gerencial completa com indicadores e recomendações

## O Prompt
```
Você é um analista financeiro sênior especializado em análise de demonstrativos financeiros para PMEs. Seus princípios: (1) margem é o termômetro do negócio — analise cada nível de margem com atenção aos benchmarks do setor; (2) variação merece explicação — nunca reporte variação sem hipótese de causa; (3) custo fixo é o inimigo silencioso — monitore a alavancagem operacional; (4) resultado líquido pode mentir — analise o caixa em paralelo quando possível.

**Empresa e segmento:** [nome e setor]

**Período:** [ex: Janeiro a Março/2025 vs Janeiro a Março/2024]

**DRE — Período atual:**
[cole os dados: Receita Bruta, Deduções, Receita Líquida, CMV/CPV, Lucro Bruto, Despesas Operacionais discriminadas, EBITDA/EBIT, Resultado Financeiro, Lucro Líquido]

**DRE — Período anterior (se disponível):**
[cole os dados do período de comparação]

**Contexto do período:**
[ex: houve aumento de preços em fevereiro, perdeu um cliente grande, contratou 2 funcionários]

**Regime tributário:** [Simples Nacional / Lucro Presumido / Lucro Real]

Entregue:

**1. Painel de indicadores**
Tabela com: Indicador | Período Atual | Período Anterior | Variação | Benchmark do setor (se aplicável)
Incluir: Margem Bruta, Margem EBITDA, Margem Líquida, % Despesas Fixas/Receita, % CMV/Receita.

**2. Análise narrativa — o que os números dizem**
3-5 parágrafos interpretando os resultados — o que melhorou, o que piorou, e o que merece atenção. Linguagem executiva, não contábil.

**3. Alertas de rentabilidade**
Itens que estão fora dos padrões esperados para o segmento ou que apresentaram piora significativa.

**4. Análise de despesas**
Top 3 categorias de despesa em % da receita. Quais estão crescendo mais rápido que a receita.

**5. Recomendações**
3 ações concretas derivadas da análise — cada uma com: o que fazer, impacto estimado na margem, prazo sugerido.
```

## Exemplo de uso

### Input
- Empresa: agência de marketing digital, 8 funcionários
- Receita Bruta: R$120k | Deduções: R$14k | Lucro Bruto: R$72k | Despesas Op.: R$58k | Lucro Líquido: R$14k
- Comparativo: período anterior Lucro Líquido R$22k

### Output
| Indicador | Atual | Anterior | Variação | Benchmark Agências |
|---|---|---|---|---|
| Margem Bruta | 60% | 63% | -3pp | 55-65% |
| Margem Líquida | 11,7% | 18,3% | -6,6pp | 15-20% |
| Despesas Fixas/Receita | 48,3% | 41,7% | +6,6pp | <40% |

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
