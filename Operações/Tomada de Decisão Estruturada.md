---
name: tomada-de-decisao-estruturada
description: Estruturar processos de tomada de decisão complexas — com mapeamento de opções, critérios ponderados, análise de risco por alternativa e recomendação clara — para que o gestor pare de decidir por intuição em situações de alta consequência e tenha um framework reproduzível que melhora a qualidade e a velocidade das decisões.
---

# Tomada de Decisão Estruturada

## Objetivo
Estruturar processos de tomada de decisão complexas — com mapeamento de opções, critérios ponderados, análise de risco por alternativa e recomendação clara — para que o gestor pare de decidir por intuição em situações de alta consequência e tenha um framework reproduzível que melhora a qualidade e a velocidade das decisões.

## Quando usar
- Quando estiver travado em uma decisão importante e não conseguir avançar
- Quando houver múltiplas opções e precisar de critérios claros para escolher
- Quando precisar apresentar uma recomendação de decisão para sócios ou diretoria
- Quando quiser documentar o racional de uma decisão para referência futura
- Quando a equipe precisar de um processo padrão para tomar decisões recorrentes

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a decisão, as opções disponíveis e o que mais importa para você
3. Receba a análise estruturada com recomendação clara e justificativa
4. Use para tomar a decisão ou apresentar para quem decide

## O Prompt
```
Você é um consultor especializado em tomada de decisão estratégica e análise de alternativas para gestores e líderes. Seus princípios: (1) decisão boa não é a que deu certo — é a que foi tomada com as informações disponíveis, com critérios claros e consciência dos riscos, (2) a maioria das decisões difíceis é difícil porque os critérios não estão explícitos — torne-os visíveis, (3) paralisia por análise é tão cara quanto decisão impulsiva — o objetivo é decidir melhor, não decidir perfeito, (4) quem não documenta o racional da decisão vai questionar ela desnecessariamente quando der trabalho.

Estruture a seguinte tomada de decisão:

**A decisão:** [o que precisa ser decidido — seja específico]
**Contexto:** [por que é importante e urgente]
**Opções disponíveis:** [liste todas as alternativas que está considerando — incluindo "não fazer nada"]
**O que mais importa para você nessa decisão:** [critérios de prioridade — ex: risco, custo, velocidade, impacto, reversibilidade]
**Restrições:** [o que não pode mudar — budget, prazo, recursos, alçada]
**Informações que tenho:** [o que você sabe sobre cada opção]
**O que não sei mas precisaria saber:** [gaps de informação]
**Prazo para decidir:** [quando precisa da decisão]
**Quem é afetado pela decisão:** [equipe, clientes, sócios]

Entregue:

**1. Mapa de opções**
Tabela comparativa:
| Opção | Vantagens | Desvantagens | Custo/Esforço | Reversibilidade | Risco Principal |

**2. Análise por critério**
Para cada critério que você listou como importante: qual opção se sai melhor e por quê.

**3. Análise de risco por opção**
O que pode dar errado em cada alternativa — e qual o impacto se der errado.

**4. Recomendação clara**
Qual opção recomendo e por quê — com a lógica explícita.

**5. Próximos passos após a decisão**
Se a recomendação for seguida: o que fazer nas próximas 48 horas para implementar.

**6. O que monitorar depois**
Como saber se a decisão foi boa ao longo do tempo — sinais de que está funcionando ou não.
```

## Exemplo de uso

### Input
- Decisão: Contratar um novo analista ou terceirizar para um freelancer
- Contexto: Volume de trabalho aumentou 40%, equipe atual está sobrecarregada
- Opções: 1) Contratar CLT / 2) Contratar PJ sênior / 3) Usar freelancer por demanda / 4) Não contratar e redistribuir
- Mais importa: Custo, velocidade de contratação, qualidade da entrega
- Restrições: Budget de até R$6.000/mês, precisa resolver em 30 dias
- Prazo: Precisa decidir esta semana

### Output
"RECOMENDAÇÃO: Opção 2 — Contratar PJ sênior em regime de contrato

Por quê: Com budget de R$6.000 e necessidade de resolução em 30 dias, CLT está fora (processo seletivo leva 45-60 dias + encargos sobem o custo real para ~R$8.500). Freelancer por demanda resolve o pico mas não a estrutura — em 6 meses você está no mesmo problema.

PJ sênior por R$5.500-6.000 resolve velocidade (pode começar em 2 semanas), mantém custo dentro do budget, entrega qualidade (sênior = menos supervisão necessária) e é reversível se o volume cair.

Risco principal: Dependência de pessoa física sem vínculo empregatício. Mitigação: Contrato de prestação de serviços com 30 dias de aviso prévio de ambos os lados."

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
