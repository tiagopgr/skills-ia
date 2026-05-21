---
name: planejamento-de-sprint-solo
description: Planejar sprints de desenvolvimento semanais ou quinzenais para freelancer solo — com backlog priorizado, estimativa de tarefas, metas de entrega e revisão de resultado — para ter sempre clareza sobre o que vai ser desenvolvido nesse período, evitar o "comecei 10 coisas e terminei nenhuma" e entregar projetos de forma previsível mesmo tocando múltiplos clientes.
---

# Planejamento de Sprint Solo

## Objetivo
Planejar sprints de desenvolvimento semanais ou quinzenais para freelancer solo — com backlog priorizado, estimativa de tarefas, metas de entrega e revisão de resultado — para ter sempre clareza sobre o que vai ser desenvolvido nesse período, evitar o "comecei 10 coisas e terminei nenhuma" e entregar projetos de forma previsível mesmo tocando múltiplos clientes.

## Quando usar
- No início de cada semana ou quinzena para planejar o que vai ser desenvolvido
- Quando o projeto está grande demais e você não sabe por onde começar
- Para decompor um projeto complexo em tarefas que cabem em uma semana
- Para ter uma cadência de entregas parciais que mantém o cliente confiante

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto, as funcionalidades que faltam e as horas disponíveis
3. Receba o plano do sprint completo com backlog priorizado e estimativas
4. Execute, anote o que ficou para trás e use no planejamento do próximo sprint

## O Prompt
```
Você é um desenvolvedor sênior com experiência em metodologias ágeis adaptadas para trabalho solo. Seus princípios: (1) sprint solo não é Scrum — é uma disciplina pessoal de foco que elimina a procrastinação por excesso de escolhas, (2) estimativas de desenvolvedor sênior ainda estão erradas em 30% do tempo — adicione buffer, (3) a meta do sprint deve ser um entregável que o cliente consegue ver e testar, não só tarefas técnicas finalizadas, (4) o que não foi entregue no sprint anterior precisa ser a primeira conversa do próximo — não some debaixo do tapete.

**Projeto(s) envolvidos:** [nome e breve descrição de cada]
**Funcionalidades ou tarefas pendentes:** [liste tudo que falta fazer, pode ser bagunçado]
**Horas disponíveis nesse sprint:** [total de horas para esse período]
**Prazo final de entrega do projeto:** [data]
**O que o cliente está esperando ver primeiro:** [o que tem mais valor para ele ver funcionando]
**Dívidas técnicas ou bloqueios conhecidos:** [ex: "preciso migrar o banco antes", "aguardando acesso do cliente"]

Entregue:

**1. Backlog Priorizado**
Lista de todas as tarefas organizadas por prioridade (crítico / importante / desejável), com estimativa de horas para cada uma.

**2. Meta do Sprint**
O entregável principal do período — o que vai estar funcionando ao final que o cliente pode ver e testar.

**3. Plano Dia a Dia**
Distribuição das tarefas nos dias do sprint com sequência lógica e margem para imprevistos.

**4. Critério de Conclusão (Definition of Done)**
O que significa "feito" para cada tarefa principal — sem ambiguidade sobre quando você pode marcar como concluída.

**5. O que fica fora deste sprint**
Lista explícita do que não vai ser feito agora e por quê — para você não se sentir culpado por não fazer tudo de uma vez.
```

## Exemplo de uso

### Input
- Projeto: Sistema de agendamento online para clínica (React + Node + PostgreSQL)
- Pendências: Login de paciente, cadastro de horários, tela de agendamento, confirmação por e-mail, painel do médico, relatórios
- Horas disponíveis: 30h (1 semana)
- Prazo final: 3 semanas
- O que cliente quer ver: Paciente conseguindo agendar uma consulta
- Bloqueios: Nenhum

### Output


---
**Tags:** Intermediário | Template | Código, Dev & Automação
