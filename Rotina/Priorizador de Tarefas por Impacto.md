---
name: priorizador-de-tarefas-por-impacto
description: Pegar uma lista de tarefas acumuladas e caóticas — aquelas que ficam na cabeça ou no bloco de notas sem sair do lugar — e transformar em uma fila de execução clara, com cada item classificado por urgência, impacto e ação recomendada (fazer, delegar ou eliminar), para que o gestor saiba exatamente com o que começar o dia.
---

# Priorizador de Tarefas por Impacto

## Objetivo
Pegar uma lista de tarefas acumuladas e caóticas — aquelas que ficam na cabeça ou no bloco de notas sem sair do lugar — e transformar em uma fila de execução clara, com cada item classificado por urgência, impacto e ação recomendada (fazer, delegar ou eliminar), para que o gestor saiba exatamente com o que começar o dia.

## Quando usar
- Quando a lista de pendências está grande e você não sabe por onde começar
- No início da semana para decidir o foco dos próximos 5 dias
- Quando novas demandas chegam e você precisa encaixá-las sem perder o que já estava planejado
- Após um período de ausência (viagem, férias) para retomar o controle rápido

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole sua lista de tarefas pendentes — pode ser bagunçada, só jogue tudo que está na cabeça
3. Receba cada tarefa classificada em uma matriz com ação recomendada e justificativa
4. Execute na ordem sugerida ou ajuste conforme seu contexto

## O Prompt
```
Você é um especialista em gestão de tempo e produtividade executiva. Seus princípios: (1) urgente não é sinônimo de importante — a maioria das urgências pode ser delegada ou adiada, (2) o impacto real de uma tarefa se mede pelo que acontece se ela NÃO for feita, (3) um gestor que faz tudo é um gestor que delega mal — classificar é o primeiro passo para delegar, (4) o objetivo não é fazer mais, é fazer menos com mais resultado.

Preciso priorizar minhas tarefas pendentes.

**Minha função:** [descreva seu cargo e contexto — ex: gestor de operações em empresa farmacêutica]
**Minha equipe:** [quantas pessoas, quais funções disponíveis para receber delegações]
**Prazo mais crítico da semana:** [qual entrega ou compromisso não pode falhar]
**Lista de tarefas pendentes:** [cole todas as tarefas — sem ordenar, pode ser bagunçada]

Entregue:

**1. Matriz de prioridade (tabela)**
Para cada tarefa: Tarefa | Urgência (Alta/Média/Baixa) | Impacto (Alto/Médio/Baixo) | Ação (Fazer agora / Agendar / Delegar / Eliminar) | Para quem delegar (se aplicável)

**2. Top 3 do dia**
As 3 tarefas que eu devo resolver hoje, com justificativa de por que cada uma é prioritária agora.

**3. Lista de delegação**
Tarefas que podem ser passadas para a equipe, com sugestão de como comunicar a delegação em 1 frase.

**4. O que eliminar ou ignorar**
Tarefas que podem ser descartadas ou adiadas indefinidamente sem consequência real, com justificativa.
```

## Exemplo de uso

### Input
- Função: Gestor de área médico-científica, indústria farmacêutica
- Equipe: 3 pessoas (analista, coordenador, assistente)
- Prazo crítico: Apresentação para diretoria na sexta
- Tarefas: Responder 14 e-mails, revisar relatório de KPIs, comprar material de escritório, alinhar treinamento da equipe, preparar slides para diretoria, assinar documento RH, responder fornecedor sobre proposta, organizar arquivos de um projeto antigo, ligar para cliente X sobre reclamação

### Output
| Tarefa | Urgência | Impacto | Ação |
|--------|----------|---------|------|
| Preparar slides para diretoria | Alta | Alto | Fazer agora |
| Ligar para cliente X (reclamação) | Alta | Alto | Fazer agora |
| Revisar relatório de KPIs | Alta | Alto | Fazer hoje |
| Responder fornecedor sobre proposta | Média | Médio | Agendar amanhã |
| Alinhar treinamento da equipe | Média | Médio | Delegar ao coordenador |
| Responder 14 e-mails | Média | Baixo | Delegar ao assistente (triagem) |
| Assinar documento RH | Baixa | Médio | Agendar — 10 min amanhã |
| Comprar material de escritório | Baixa | Baixo | Delegar ao assistente |
| Organizar arquivos projeto antigo | Baixa | Baixo | Eliminar — não há urgência |

---
**Tags:** Iniciante | Análise | Rotina, Tarefas & Organização
