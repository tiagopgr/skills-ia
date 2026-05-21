---
name: comparativo-regimes-tributarios
description: Analisar e comparar Simples Nacional, Lucro Presumido e Lucro Real para o caso específico da empresa, calculando a carga tributária em cada cenário e recomendando o mais vantajoso.
---

# Comparativo Regimes Tributários

## Objetivo
Analisar e comparar Simples Nacional, Lucro Presumido e Lucro Real para o caso específico da empresa, calculando a carga tributária em cada cenário e recomendando o mais vantajoso.

## Quando usar
- Na abertura de empresa (escolher o regime certo)
- Na virada do ano fiscal (reavaliar enquadramento)
- Quando o faturamento muda significativamente
- Ao crescer além do limite do Simples (R$4.8M/ano)

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Insira os dados financeiros da empresa
3. Receba a comparação detalhada entre regimes
4. Valide com seu contador antes de tomar a decisão

## O Prompt
```
Você é um consultor tributário que sabe que a escolha do regime pode representar 5-15% de diferença no faturamento líquido — e a maioria das empresas está no regime errado.

IMPORTANTE: A decisão final deve ser tomada com o contador da empresa.

Compare os regimes tributários para:

**Atividade da empresa:** [descreva — CNAE se souber]
**Tipo:** [prestação de serviço, comércio, indústria, misto]
**Faturamento anual:** [valor]
**Folha de pagamento mensal:** [valor]
**Fator R (folha ÷ faturamento):** [se souber]
**Margem de lucro real estimada:** [%]
**Despesas dedutíveis significativas:** [aluguel, insumos]
**Estado/Município:** [para ICMS/ISS]

Entregue:
1. Simples Nacional (enquadramento, alíquota efetiva, valor mensal)
2. Lucro Presumido (base de presunção, impostos calculados)
3. Lucro Real (quando faz sentido, cálculo)
4. Tabela comparativa
5. Recomendação com justificativa
6. Cenários futuros (se faturamento dobrar, etc.)
7. Checklist para validar com o contador
```

## Exemplo de uso

### Input
Atividade: Agência de marketing digital (serviço)
Faturamento: R$60K/mês (R$720K/ano)
Folha: R$22K/mês (Fator R = 36.7%)
Margem real: ~35%
5 funcionários CLT
São Paulo/SP

### Output
| Regime | Imposto mensal | % faturamento |
| Simples (Anexo III*) | ~R$7.200 | 12.0% |
| Lucro Presumido | ~R$10.800 | 18.0% |
| Lucro Real | ~R$9.500 | 15.8% |

*Fator R de 36.7% > 28% → cai no Anexo III ao invés do V. Isso muda tudo.

Recomendação: Simples Nacional (Anexo III). Economia de R$43.200/ano vs Lucro Presumido.

Atenção: se a folha cair abaixo de 28% do faturamento, volta para Anexo V e a conta muda.

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
