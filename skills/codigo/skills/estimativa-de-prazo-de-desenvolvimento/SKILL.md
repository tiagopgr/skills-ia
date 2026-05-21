---
name: estimativa-de-prazo-de-desenvolvimento
description: Calcular estimativas de prazo realistas e defensáveis para projetos de desenvolvimento — com decomposição das funcionalidades em tarefas, estimativa de horas por tarefa, margem de risco e comunicação honesta com o cliente — para parar de prometer prazos impossíveis, parar de atrasar e nunca mais passar pela situação constrangedora de ter que pedir extensão de prazo porque não planejou direito.
---

# Estimativa de Prazo de Desenvolvimento

## Objetivo
Calcular estimativas de prazo realistas e defensáveis para projetos de desenvolvimento — com decomposição das funcionalidades em tarefas, estimativa de horas por tarefa, margem de risco e comunicação honesta com o cliente — para parar de prometer prazos impossíveis, parar de atrasar e nunca mais passar pela situação constrangedora de ter que pedir extensão de prazo porque não planejou direito.

## Quando usar
- Antes de qualquer comprometimento de prazo com cliente
- Quando cliente pede "quanto tempo leva?" e você precisa de uma resposta real
- Para decompor um projeto grande e entender o que realmente está envolvido
- Ao revisar se um prazo acordado ainda é viável dado o que descobriu durante o desenvolvimento

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto e todas as funcionalidades que você entende que precisam ser feitas
3. Receba a decomposição com estimativas por tarefa, margem de risco e prazo final defensável
4. Use a estimativa detalhada na proposta — cliente que vê o detalhamento entende por que leva o tempo que leva

## O Prompt
```
Você é um engenheiro de software sênior com experiência em estimativas de projeto. Seus princípios: (1) estimativa sem decomposição é chute — todo projeto grande deve ser quebrado em tarefas de no máximo 8h antes de estimar, (2) adicione 25-40% de buffer para freelancer solo — você não tem colega para desbloquear quando travar, (3) tarefas de integração e configuração são sempre subestimadas — elas levam 2x mais que o previsto, (4) prazo honesto que o cliente aceita é melhor que prazo otimista que você vai descumprir.

**Descrição do projeto:** [descreva o que precisa ser desenvolvido com o máximo de detalhes que você tem]
**Tecnologias que vai usar:** [stack tecnológico]
**Funcionalidades listadas:** [liste cada funcionalidade que você entende que é necessária]
**Suas horas disponíveis por semana para esse projeto:** [ex: 20h/semana exclusivo / 10h/semana dividindo com outros]
**Seu nível de familiaridade com a stack:** [iniciante / já usei / especialista]
**Integrações com terceiros:** [ex: gateway de pagamento, API de CEP, WhatsApp, autenticação Google]

Entregue:

**1. Decomposição Completa de Tarefas**
Lista de todas as tarefas com estimativa mínima e máxima de horas para cada uma. Agrupadas por módulo ou funcionalidade.

**2. Resumo de Horas**
Total mínimo, total máximo e total com buffer de risco (25-40% a mais).

**3. Prazo Calculado**
Dado as horas com buffer e as horas disponíveis por semana: prazo em dias úteis e data de entrega estimada.

**4. Riscos e Incertezas**
Itens que podem fazer a estimativa explodir e como mitigar cada um.

**5. Como Apresentar a Estimativa ao Cliente**
Como comunicar prazo e detalhamento sem assustar o cliente e sem parecer que você está exagerando.
```

## Exemplo de uso

### Input
- Projeto: Sistema de gestão para pet shop (cadastro de animais, agendamento de banho/tosa, histórico, financeiro básico)
- Stack: React + Node.js + PostgreSQL
- Funcionalidades: Cadastro de clientes e pets, calendário de agendamentos, histórico de serviços, controle de caixa diário, relatório mensal
- Horas disponíveis: 15h/semana (tocando outro projeto)
- Familiaridade: Já usei React e Node várias vezes
- Integrações: Nenhuma terceira — só WhatsApp de notificação manual

### Output


---
**Tags:** Intermediário | Análise | Código, Dev & Automação
