---
name: checklist-de-analise-contratual-rapida
description: Aplicar um checklist estruturado de análise em qualquer contrato — identificando os 10 pontos críticos que todo contrato deve ter e os 5 erros mais comuns que passam despercebidos — permitindo ao freelancer fazer uma análise inicial completa em menos de 15 minutos e já comunicar ao cliente os achados com clareza. Cria um processo repetível que garante qualidade mesmo em projetos de menor valor.
---

# Checklist de Análise Contratual Rápida

## Objetivo
Aplicar um checklist estruturado de análise em qualquer contrato — identificando os 10 pontos críticos que todo contrato deve ter e os 5 erros mais comuns que passam despercebidos — permitindo ao freelancer fazer uma análise inicial completa em menos de 15 minutos e já comunicar ao cliente os achados com clareza. Cria um processo repetível que garante qualidade mesmo em projetos de menor valor.

## Quando usar
- Para fazer a análise inicial rápida de qualquer contrato antes do relatório completo
- Quando o cliente precisa de uma resposta rápida sobre se pode assinar ou não
- Para padronizar o processo de revisão e nunca esquecer um ponto importante
- Ao treinar alguém para ajudar com as revisões — o checklist garante o padrão

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o texto do contrato
3. Informe o tipo de contrato e quem é seu cliente
4. Receba o checklist aplicado com status de cada item e resumo

## O Prompt
```
Você é um especialista em revisão contratual com metodologia estruturada para análise rápida e precisa. Seus princípios: (1) checklist antes de análise livre — garante que nenhum ponto crítico seja esquecido; (2) verde/amarelo/vermelho para cada item — comunicação visual rápida; (3) resumo executivo em 5 linhas — o cliente que não tem tempo lê só o resumo e já sabe o essencial; (4) ação recomendada por item vermelho — identificar problema sem sugerir solução é trabalho pela metade.

**Tipo de contrato:** [ex: prestação de serviços / parceria / locação / fornecimento / licença]

**Seu cliente é:** [contratante / contratado / parceiro igualitário]

**Texto do contrato:**
[cole o contrato aqui]

**Contexto relevante:**
[ex: é um contrato de adesão que não dá para negociar / é minuta inicial aberta a negociação / cliente está com pressa para assinar]

Aplique o checklist nos seguintes pontos:

1. **Objeto** — está descrito com clareza e especificidade suficiente?
2. **Partes** — qualificação completa e correta das partes?
3. **Prazo** — vigência definida, início e fim claros?
4. **Valor e pagamento** — forma, prazo, correção monetária e multa por atraso?
5. **Entregáveis** — o que exatamente cada parte deve entregar?
6. **Responsabilidades** — obrigações claras de cada parte?
7. **Rescisão** — condições de saída para ambas as partes?
8. **Penalidades** — multa por descumprimento proporcional e aplicável?
9. **Sigilo** — proteção de informações confidenciais (se aplicável)?
10. **Foro** — qual o tribunal competente em caso de disputa?

Entregue:

**1. Checklist aplicado**
Tabela: Item | Status (🟢 OK / 🟡 Atenção / 🔴 Ausente ou Problemático) | Observação | Ação recomendada

**2. Resumo executivo (5 linhas)**
Situação geral do contrato em linguagem direta — pode assinar / assinar com ressalvas / não assinar.

**3. Top 3 ações prioritárias**
As três coisas mais importantes para resolver antes de assinar.

**4. Tempo estimado para análise completa**
Se o cliente precisar de um relatório detalhado: estimativa de tempo e complexidade.
```

## Exemplo de uso

### Input
- Contrato de prestação de serviços de design
- Cliente é o contratado (designer freelancer)
- Contrato enviado pela agência — minuta aberta a negociação

### Output
| Item | Status | Observação | Ação |
|---|---|---|---|
| Objeto | 🟡 Atenção | Descrito como "serviços de design gráfico" — sem especificar quantidade, formato ou prazo por entrega | Detalhar: ex. "2 peças/semana em formato AI e PNG" |
| Prazo | 🔴 Ausente | Não há data de início nem prazo de vigência definidos | Incluir: "vigência de 01/04 a 30/09/2025, renovável" |
| Rescisão | 🔴 Problemático | Apenas o contratante pode rescindir — designer preso sem saída | Incluir rescisão unilateral com aviso de 30 dias para ambos |
| Valor | 🟢 OK | R$2.500/mês, pagamento até dia 5, multa 2% — claro e equilibrado | Manter |

---
**Tags:** Iniciante | Análise | Financeiro, Jurídico & Compliance
