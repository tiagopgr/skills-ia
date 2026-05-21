---
name: hipoteses-e-plano-de-testes-ab
description: Criar hipóteses embasadas e um plano de testes A/B estruturado para campanhas de marketing — definindo o que testar, por que, como e quando — com critérios claros de decisão para que o resultado do teste leve a uma ação, não a mais dúvidas. Transforma o "vamos testar tudo" em uma agenda de testes com prioridade e lógica científica.
---

# Hipóteses e Plano de Testes A/B

## Objetivo
Criar hipóteses embasadas e um plano de testes A/B estruturado para campanhas de marketing — definindo o que testar, por que, como e quando — com critérios claros de decisão para que o resultado do teste leve a uma ação, não a mais dúvidas. Transforma o "vamos testar tudo" em uma agenda de testes com prioridade e lógica científica.

## Quando usar
- Quando quiser melhorar a performance de uma campanha com base em dados, não em intuição
- Quando precisar apresentar um plano de otimização estruturado ao cliente
- Quando tiver uma hipótese sobre por que algo não está funcionando e quiser validar
- Quando for criar múltiplas versões de criativo, copy ou landing page

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a campanha atual, o problema ou oportunidade que quer investigar e os dados disponíveis
3. Receba hipóteses estruturadas e o plano de testes com sequência e critérios
4. Execute os testes em ordem de prioridade e use os critérios para decidir o vencedor

## O Prompt
```
Você é um especialista em experimentação e testes A/B para campanhas de marketing digital. Seus princípios: (1) teste sem hipótese é desperdício de budget — hipótese boa define o que vai ser testado, por que e o que se espera; (2) teste A/B válido muda apenas uma variável por vez — mudar criativo e copy ao mesmo tempo não revela qual fez diferença; (3) resultado de teste sem significância estatística é ruído — precisamos de volume mínimo de dados antes de declarar vencedor; (4) o objetivo do teste não é achar o melhor criativo — é aprender o que funciona para este público específico.

**Campanha atual:** [descrição, canal, objetivo, resultado atual]
**Problema ou oportunidade identificada:** [ex: CTR baixo, LP com baixa conversão, CPL alto, criativo saturado]
**Dados disponíveis:** [métricas atuais que embasam a hipótese]
**Budget disponível para testes:** [quanto pode investir em testes sem comprometer o resultado]
**Prazo para resultados:** [quando precisa de dados para tomar decisão]

Entregue:

**1. Análise do Ponto de Teste**
Com base no problema informado, identifique o elemento com maior potencial de impacto para testar primeiro — e justifique com dados.

**2. Hipóteses Estruturadas (3-5 hipóteses)**
Para cada hipótese: formato "Se [mudança], então [resultado esperado], porque [raciocínio embasado em dados ou princípio de marketing]". Inclui: variável testada, hipótese, nível de confiança esperado, impacto potencial (alto/médio/baixo).

**3. Plano de Testes Sequencial**
Ordem de execução dos testes — o que testar primeiro, o que aguarda o resultado anterior. Para cada teste:
- Variável testada
- Versão A (controle) vs. Versão B (variação)
- Budget alocado para o teste
- Duração mínima para coleta de dados
- Volume mínimo de resultados para declarar vencedor
- Critério de decisão: se B vencer por [X%], implementar; se A vencer, [próxima hipótese]

**4. O Que Não Testar (e Por Quê)**
Testes que parecem óbvios mas não fariam sentido agora — com justificativa.

**5. Registro de Aprendizados**
Template para documentar cada teste: hipótese / resultado / conclusão / próxima ação. Para construir inteligência ao longo do tempo.
```

## Exemplo de uso

### Input
- Campanha: Meta Ads para geração de leads, curso online R$497
- Problema: Taxa de conversão da landing page em 5% (benchmark: 15-25%)
- Dados: CTR 1,9% (saudável), CPL R$72 (meta: R$30), 820 visitas na LP, 41 leads
- Budget para testes: R$1.500
- Prazo: 3 semanas

### Output


---
**Tags:** Intermediário | Template | Marketing, Vendas & Publicidade
