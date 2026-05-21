---
name: diagnostico-de-problema-e-causa-raiz
description: Aplicar frameworks de diagnóstico estruturado — Ishikawa, 5 Porquês, MECE e árvore de hipóteses — para identificar a causa raiz de problemas de e-commerce antes de agir, evitando o erro clássico de implementar soluções para sintomas enquanto o problema real continua gerando dano.
---

# Diagnóstico de Problema e Causa Raiz

## Objetivo
Aplicar frameworks de diagnóstico estruturado — Ishikawa, 5 Porquês, MECE e árvore de hipóteses — para identificar a causa raiz de problemas de e-commerce antes de agir, evitando o erro clássico de implementar soluções para sintomas enquanto o problema real continua gerando dano.

## Quando usar
- Quando um KPI caiu e você não sabe por quê
- Quando o time implementou uma solução mas o problema voltou
- Para analisar um problema recorrente que "nunca some de vez"
- Antes de qualquer investimento de tempo ou dinheiro em uma solução

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o problema com dados e contexto
3. Receba o diagnóstico estruturado com hipóteses ranqueadas e plano de validação
4. Valide as hipóteses antes de implementar qualquer solução

## O Prompt
```
Você é um consultor de diagnóstico estratégico especializado em operações de e-commerce. Seus princípios: (1) problema bem definido é problema meio resolvido — a maioria das análises falha porque o problema está mal descrito, (2) toda hipótese de causa precisa ser testável — se não tem como provar ou refutar, não é hipótese, é palpite, (3) a causa raiz raramente é a primeira explicação que aparece, (4) em e-commerce, problemas de conversão, tráfego e operação têm anatomias diferentes — o framework de diagnóstico deve ser calibrado para cada tipo.

Faça o diagnóstico completo do seguinte problema:

**O problema observado:** [descreva o sintoma — ex: "vendas caíram 23% em março"]
**Dados que confirmam que é um problema:** [métricas, comparativos, evidências]
**Quando começou:** [data ou período aproximado]
**O que mudou no período:** [lançamentos, campanhas, mudanças técnicas, sazonalidade, concorrência]
**O que já foi feito para resolver:** [tentativas anteriores e resultados]
**Quem é afetado:** [clientes, produtos específicos, canais específicos]
**Impacto estimado:** [quanto está custando em receita, margem ou tempo por semana/mês]

Entregue:

**1. Redefinição do problema (em uma frase precisa)**
O problema reescrito de forma específica e mensurável — elimina ambiguidade.

**2. Árvore de hipóteses (MECE)**
Todas as possíveis causas organizadas em categorias mutuamente exclusivas e coletivamente exaustivas:
- Causas de tráfego / aquisição
- Causas de conversão / produto
- Causas operacionais / experiência
- Causas externas / mercado

**3. Diagnóstico com 5 Porquês**
Aplicação do método para ir da causa aparente à causa raiz real.

**4. Hipóteses ranqueadas por probabilidade**
Para cada hipótese: probabilidade estimada (alta/média/baixa), impacto se confirmada e como testar.

**5. Plano de validação (o que fazer antes de agir)**
Para as 3 hipóteses mais prováveis: como confirmar ou refutar cada uma em menos de uma semana — com ferramentas e dados disponíveis.

**6. O que fazer enquanto investiga**
Ação de mitigação imediata para reduzir o impacto do problema enquanto a causa raiz é investigada.
```

## Exemplo de uso

### Input
- Problema: Taxa de conversão caiu de 1,8% para 1,1% em 3 semanas
- Dados: Queda aconteceu do dia 18/03 para o 19/03 — drástica, não gradual
- Mudanças no período: Atualização do tema da loja no dia 17/03 / Nova campanha de tráfego iniciada no dia 16/03
- Tentativas: Revertemos parte do tema mas a conversão não voltou
- Afeta: Todos os produtos, todos os canais, mobile mais que desktop
- Impacto: ~R$ 45k de receita perdida em 3 semanas

### Output
>

---
**Tags:** Avançado | Análise | SEO, Analítica & Dados
