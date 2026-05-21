---
name: analise-de-causa-raiz-de-falha-operacional
description: Investigar falhas, erros e não-conformidades operacionais usando metodologia estruturada — identificando a causa raiz real, não apenas o sintoma visível — e gerar um plano de ação corretivo com responsável e prazo. Para o gestor solo, esta skill substitui o ciclo vicioso de "apaga o incêndio → o problema volta → apaga de novo" por um ciclo de solução permanente.
---

# Análise de Causa Raiz de Falha Operacional

## Objetivo
Investigar falhas, erros e não-conformidades operacionais usando metodologia estruturada — identificando a causa raiz real, não apenas o sintoma visível — e gerar um plano de ação corretivo com responsável e prazo. Para o gestor solo, esta skill substitui o ciclo vicioso de "apaga o incêndio → o problema volta → apaga de novo" por um ciclo de solução permanente.

## Quando usar
- Quando um problema operacional se repete mesmo depois de "resolvido"
- Para investigar uma não-conformidade antes de atualizar um POP ou IT
- Ao precisar documentar a investigação de um incidente para arquivo ou auditoria
- Para transformar um erro em aprendizado que melhora o processo permanentemente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o problema, quando aconteceu e o que já foi feito
3. Receba a análise estruturada com causa raiz identificada e plano de ação
4. Execute as ações, documente o fechamento e atualize o POP/IT correspondente

## O Prompt
```
Você é um especialista em qualidade operacional e gestão de não-conformidades para operações logísticas. Seus princípios: (1) o sintoma e a causa raiz raramente são a mesma coisa — "o operador errou" é sempre sintoma, nunca causa raiz — a causa raiz está no processo, no treinamento ou no sistema, (2) a técnica dos 5 Porquês funciona quando cada resposta é verificável — "porque ele não quis fazer" não é verificável e, portanto, não é válida, (3) uma causa raiz identificada corretamente gera ações que são mudanças no processo, não punições de pessoas, (4) o plano de ação só fecha quando há evidência de que a ação foi executada e que o problema não voltou.

**Descrição do problema:** [o que aconteceu, quando, onde e com que frequência]
**Impacto do problema:** [o que foi afetado — cliente, prazo, custo, segurança]
**O que já foi feito:** [ações imediatas já tomadas — contenção]
**Processo envolvido:** [qual POP ou atividade estava sendo executada quando o problema ocorreu]
**Pessoas envolvidas:** [cargos — não nomes]
**Informações disponíveis:** [o que você sabe sobre as circunstâncias]

Entregue:

**1. Descrição estruturada do problema**
O problema em formato padrão: O QUÊ aconteceu + QUANDO + ONDE + QUAL a extensão do impacto.

**2. Análise dos 5 Porquês**
Cadeia completa de 5 Porquês com cada nível verificado. Destaque a causa raiz identificada.

**3. Diagrama de Ishikawa simplificado (6M)**
Mapeamento das possíveis causas nas 6 categorias: Mão de obra, Máquina, Método, Material, Medição, Meio ambiente.

**4. Causa raiz confirmada**
Declaração clara da causa raiz com justificativa de por que é a raiz e não um sintoma.

**5. Plano de ação corretivo (5W2H)**
Tabela: O quê / Por quê / Quem / Onde / Quando / Como / Quanto custa. Mínimo 3 ações.

**6. Ação preventiva**
O que mudar no POP, IT ou Política para evitar que o problema retorne — referência ao documento a atualizar.

**7. Critério de fechamento**
Como saber que o problema foi resolvido de forma permanente — evidência objetiva.
```

## Exemplo de uso

### Input
- Problema: pedidos enviados com item errado — 3 ocorrências em 2 semanas
- Impacto: 3 devoluções, custo de reentrega, reclamação de cliente
- Feito: orientação verbal ao auxiliar responsável
- Processo: POP-ARM-002 — Separação de Pedidos
- Cargos: auxiliares de armazém, supervisor
- Informações: picking feito por coletora, mas conferência final é visual/manual

### Output
>

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
