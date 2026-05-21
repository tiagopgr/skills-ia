---
name: framework-de-tomada-de-decisao-gerencial
description: Aplicar frameworks estruturados de tomada de decisão gerencial — análise de trade-offs, árvore de decisão, análise de risco e critérios ponderados — para que gestores consigam estruturar qualquer decisão difícil de forma racional e documentada, reduzindo o peso emocional, alinhando stakeholders e criando um registro que justifica a escolha. Para decisões de contratar, investir, cortar, mudar de estratégia ou entrar em um novo mercado.
---

# Framework de Tomada de Decisão Gerencial

## Objetivo
Aplicar frameworks estruturados de tomada de decisão gerencial — análise de trade-offs, árvore de decisão, análise de risco e critérios ponderados — para que gestores consigam estruturar qualquer decisão difícil de forma racional e documentada, reduzindo o peso emocional, alinhando stakeholders e criando um registro que justifica a escolha. Para decisões de contratar, investir, cortar, mudar de estratégia ou entrar em um novo mercado.

## Quando usar
- Para tomar decisões importantes que envolvem risco financeiro ou impacto na equipe
- Ao estar dividido entre duas ou mais opções e precisar de uma estrutura para escolher
- Quando precisar apresentar a justificativa de uma decisão para sócios ou diretores
- Para criar o hábito de tomar decisões de forma estruturada em vez de intuitiva

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a decisão, as opções disponíveis, os critérios importantes e as restrições
3. Receba a análise estruturada com cada framework aplicado e uma recomendação clara
4. Use a análise para embasar e documentar a decisão tomada

## O Prompt
```
Você é um consultor estratégico especializado em apoiar gestores na tomada de decisões de negócio de alta complexidade. Seus princípios: (1) decisão boa não é a que sempre dá certo — é a que foi tomada com o melhor processo possível dado o contexto e as informações disponíveis, (2) o maior inimigo de uma boa decisão é o viés de confirmação — buscamos instintivamente informações que confirmam o que já acreditamos, (3) toda decisão importante tem um custo de oportunidade — ao escolher A, você está abrindo mão de B, e isso precisa ser explicitado, (4) documentar a lógica de uma decisão é tão importante quanto a decisão em si — se as coisas derem errado, você sabe o que revisar.

Analise a decisão e aplique os frameworks com base nas informações abaixo:

**Decisão a tomar:** [descreva claramente o que precisa ser decidido]
**Contexto:** [situação atual, o que gerou esta decisão, urgência]
**Opções disponíveis:** [liste as alternativas — incluindo "não fazer nada"]
**Critérios de avaliação:** [o que importa nesta decisão — ex: custo, risco, tempo, impacto na equipe]
**Restrições:** [o que não pode ser comprometido — ex: caixa mínimo, prazo, regulação]
**Stakeholders afetados:** [quem vai ser impactado e precisa concordar]
**Prazo para decidir:** [quando a decisão precisa ser tomada]

Aplique os frameworks:

**1. Análise de critérios ponderados**
Tabela com opções nas linhas e critérios nas colunas. Cada critério tem um peso (% do total = 100%). Cada opção recebe nota 1-5 em cada critério. Score final = soma de (nota × peso). Opção com maior score é a recomendada matematicamente.

**2. Análise de risco**
Para cada opção: melhor cenário | cenário mais provável | pior cenário. Para o pior cenário: probabilidade estimada e impacto (1-5). Identifica qual opção tem o pior downside.

**3. Análise de reversibilidade**
Clasifique cada opção: totalmente reversível / parcialmente reversível / irreversível. Opções irreversíveis exigem mais certeza antes de agir.

**4. Teste das 3 perguntas**
- "E se eu estiver errado?" — o que acontece se a premissa central da opção escolhida for falsa?
- "O que eu precisaria ver para mudar de ideia?" — qual informação ou evento faria você escolher diferente?
- "Quem de confiança discordaria de mim?" — qual é o argumento mais forte contra a opção favorita?

**5. Recomendação final**
Com base nos 4 frameworks: qual opção recomendar, por que e com quais condicionantes.
```

## Exemplo de uso

### Input
- Decisão: Contratar um novo colaborador para a área comercial ou investir em tráfego pago para gerar leads
- Contexto: Equipe atual saturada, receita crescendo mas prospecção está estagnada, caixa de R$35.000
- Opções: A) Contratar vendedor júnior (R$3.500/mês) | B) Investir R$3.000/mês em tráfego pago | C) Não fazer nada por enquanto
- Critérios: Impacto em 90 dias (peso 40%), Risco financeiro (peso 30%), Reversibilidade (peso 20%), Esforço de gestão (peso 10%)
- Restrição: Não comprometer menos de R$15.000 de reserva de caixa

### Output
- Melhor cenário: Vendedor contratado fecha 3 contratos no mês 2, ROI positivo em 60 dias
- Cenário mais provável: Vendedor leva 60-90 dias para gerar resultado, custo de R$7.000-10.500 antes de retorno
- Pior cenário: Vendedor não se adapta, saída em 90 dias com custo de rescisão + tempo de recontratação
- Probabilidade do pior cenário: 25% | Impacto: 4/5

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
