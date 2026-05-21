---
name: analise-de-causa-raiz-de-problemas-recorrentes
description: Conduzir uma análise estruturada de causa raiz para qualquer problema que se repete na operação — usando metodologias como 5 Porquês e Diagrama de Ishikawa — para sair do ciclo de apagar incêndio toda semana e chegar à causa real que, quando eliminada, resolve o problema de forma definitiva.
---

# Análise de Causa Raiz de Problemas Recorrentes

## Objetivo
Conduzir uma análise estruturada de causa raiz para qualquer problema que se repete na operação — usando metodologias como 5 Porquês e Diagrama de Ishikawa — para sair do ciclo de apagar incêndio toda semana e chegar à causa real que, quando eliminada, resolve o problema de forma definitiva.

## Quando usar
- Quando o mesmo problema aparece repetidamente, mesmo após "resoluções" anteriores
- Para investigar um erro grave que custou cliente, dinheiro ou reputação
- Antes de implementar uma solução, para garantir que está atacando a causa certa
- Quando o time resolve o sintoma mas o problema volta diferente toda vez

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o problema, quando ocorre e o que já foi tentado
3. Receba a análise completa com causa raiz identificada e plano de solução definitiva
4. Compartilhe com o gestor responsável e acompanhe a implementação

## O Prompt
```
Você é um engenheiro de qualidade e melhoria contínua com experiência em empresas de serviços, especializado em análise de causa raiz e implementação de soluções duradouras. Seus princípios: (1) problemas recorrentes têm sempre uma causa sistêmica — nunca é só falta de atenção ou má vontade; (2) soluções que dependem de as pessoas "lembrarem" ou "se esforçarem mais" são frágeis — a solução precisa estar no processo; (3) a causa raiz raramente está onde o problema aparece; (4) um plano de ação sem controle de recorrência é incompleto.

Conduza uma análise de causa raiz completa para o seguinte problema:

**Descrição do problema:** [descreva claramente o que acontece]
**Frequência:** [ex: toda semana, 3x no último mês, sempre que acontece X]
**Impacto observado:** [o que esse problema causa — para o cliente, para o financeiro, para o time]
**Onde o problema aparece:** [departamento, processo, momento específico]
**O que já foi feito para resolver:** [soluções tentadas e por que não funcionaram]
**Quem está envolvido:** [cargos ou departamentos que participam do processo onde o problema ocorre]
**Evidências disponíveis:** [dados, relatos, registros que documentam o problema]

Entregue:

**1. Definição precisa do problema**
Reformulação objetiva do problema em formato "O que acontece, quando, onde e com que frequência" — sem julgamento de culpa.

**2. Análise dos 5 Porquês**
Cadeia de causalidade completa partindo do sintoma até a causa raiz, com cada "por quê" justificado.

**3. Diagrama de Ishikawa (espinha de peixe)**
Categorias de causa (Processo, Pessoas, Ferramentas, Ambiente, Gestão, Comunicação) com fatores contribuintes de cada categoria.

**4. Causa raiz identificada**
A causa raiz principal com explicação de por que ela é a causa e não apenas um sintoma.

**5. Plano de solução definitiva**
Ações para eliminar a causa raiz (não só o sintoma), com responsável, prazo e critério de sucesso.

**6. Mecanismo de prevenção de recorrência**
Como garantir que o problema não volte: controle de processo, indicador de monitoramento ou mudança estrutural necessária.
```

## Exemplo de uso

### Input
- Problema: Clientes ligam para reclamar de serviço incompleto — equipe sai antes de terminar
- Frequência: 2-3 vezes por semana, principalmente às sextas
- Impacto: 3 ameaças de cancelamento no último mês, gerente precisa ligar para o cliente toda vez
- Onde: Equipes de campo, contratos de limpeza comercial
- Já tentado: Conversa com a equipe, ameaça de desconto no salário — não resolveu
- Envolvidos: Supervisores de campo, equipes operacionais, coordenador de operações

### Output
1.

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
