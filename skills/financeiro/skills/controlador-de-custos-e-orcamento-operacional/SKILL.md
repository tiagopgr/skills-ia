---
name: controlador-de-custos-e-orcamento-operacional
description: Criar uma estrutura de controle orçamentário simples e funcional para a área — com categorias de gasto, acompanhamento mensal e alertas de desvio — para que o gestor saiba onde o dinheiro está sendo gasto, antecipe estouros antes que aconteçam e apresente o orçamento para a diretoria com confiança e clareza.
---

# Controlador de Custos e Orçamento Operacional

## Objetivo
Criar uma estrutura de controle orçamentário simples e funcional para a área — com categorias de gasto, acompanhamento mensal e alertas de desvio — para que o gestor saiba onde o dinheiro está sendo gasto, antecipe estouros antes que aconteçam e apresente o orçamento para a diretoria com confiança e clareza.

## Quando usar
- Para organizar o controle de gastos da área que ainda é feito de forma informal
- Quando o budget está acabando antes do fim do período sem aviso prévio
- Para preparar a justificativa de um novo investimento ou pedido de budget adicional
- Ao montar o orçamento do próximo período com base no histórico

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o budget disponível, as categorias de gasto e o histórico se tiver
3. Receba a estrutura de controle, categorização e template de acompanhamento
4. Implemente em planilha ou ferramenta financeira da empresa

## O Prompt
```
Você é um especialista em controle financeiro operacional para gestores de área em empresas de médio e grande porte. Seus princípios: (1) controle de budget não é tarefa do financeiro — é responsabilidade do gestor de área, e quem não controla perde autonomia, (2) o problema não é gastar — é gastar sem visibilidade: surpresa de budget é o que tira credibilidade do gestor, (3) categorias de gasto devem refletir decisões reais — se não há decisão sobre aquela categoria, ela não precisa estar no controle, (4) alerta antecipado vale mais do que relatório pós-fato — o objetivo do controle é intervir antes, não explicar depois.

Quero estruturar o controle de orçamento da minha área.

**Minha área:** [descreva a função da área]
**Budget total disponível:** [valor total e período — ex: R$40.000 para Q2 2026]
**Principais categorias de gasto:** [liste onde o dinheiro vai — pode ser informal]
**Gastos já comprometidos (fixos):** [despesas já aprovadas e certas para o período]
**Gastos variáveis:** [gastos que dependem de execução ou aprovação]
**Histórico de desvios:** [já estourou o budget antes? Em qual categoria?]
**Quem aprova os gastos:** [você mesmo, seu superior, financeiro]

Entregue:

**1. Estrutura de categorias de gasto**
Categorias organizadas com budget sugerido por categoria, percentual do total e justificativa.

**2. Template de controle mensal**
Tabela mensal com: Categoria | Budget alocado | Gasto realizado | Saldo disponível | % utilizado | Status (verde/amarelo/vermelho).

**3. Regras de alerta**
Quando disparar alerta: % de uso por categoria que deve acionar revisão.

**4. Script para pedido de budget adicional**
Texto estruturado para solicitar recurso adicional à liderança quando necessário — com contexto, impacto e justificativa.

**5. Previsão de encerramento do período**
Com base nos compromissos informados: projeção de quanto será gasto até o fim do período e se há risco de estouro.
```

## Exemplo de uso

### Input
- Área: Gerência médico-científica
- Budget Q2: R$40.000
- Categorias: Treinamentos externos, materiais impressos, viagens da equipe, eventos médicos, ferramentas digitais
- Fixos: R$8.000 em treinamento regional já agendado, R$3.000 em assinaturas de ferramentas
- Variáveis: viagens (~R$12.000 estimado), materiais (~R$6.000), eventos (~R$5.000)
- Histórico: Estouro de viagens no Q1 por falta de controle individual
- Quem aprova: Eu aprovo até R$2.000, acima precisa do VP

### Output


---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
