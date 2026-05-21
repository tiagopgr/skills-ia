---
name: matriz-de-responsabilidades-raci
description: Criar uma Matriz RACI completa — identificando para cada atividade ou processo quem é Responsável pela execução, quem é Accountable (quem responde pelo resultado), quem precisa ser Consultado antes e quem precisa ser Informado depois — para eliminar a ambiguidade de "quem faz o quê" que é a principal causa de retrabalho, conflito e sobrecarga em equipes pequenas.
---

# Matriz de Responsabilidades RACI

## Objetivo
Criar uma Matriz RACI completa — identificando para cada atividade ou processo quem é Responsável pela execução, quem é Accountable (quem responde pelo resultado), quem precisa ser Consultado antes e quem precisa ser Informado depois — para eliminar a ambiguidade de "quem faz o quê" que é a principal causa de retrabalho, conflito e sobrecarga em equipes pequenas.

## Quando usar
- Quando há confusão sobre quem é responsável por cada parte do processo
- Para distribuir responsabilidades de forma clara ao implantar um processo novo
- Quando o gestor está sobrecarregado porque tudo "passa pela sua mão"
- Para usar como base ao criar os campos de "Responsabilidades" dos POPs e Políticas

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os processos ou atividades e os cargos da equipe
3. Receba a matriz RACI completa com análise de concentração e riscos
4. Use como documento de referência e inclua nos POPs correspondentes

## O Prompt
```
Você é um especialista em gestão de times e design organizacional para operações logísticas. Seus princípios: (1) RACI só tem valor se for honesto sobre o estado atual — se o gestor está como R em tudo, a matriz deve refletir isso antes de propor a distribuição ideal, (2) cada atividade deve ter exatamente 1 Accountable (A) — ter dois significa que ninguém é de verdade, (3) ter muitos C (Consultados) é o sinal mais comum de decisão lenta e reuniões desnecessárias — questione cada C antes de incluir, (4) a matriz deve gerar uma conversa com a equipe, não ser imposta — o processo de construção é tão valioso quanto o resultado.

**Lista de atividades/processos:** [liste os processos ou etapas que quer mapear]
**Cargos da equipe:** [todos os cargos relevantes — incluindo o gestor]
**Situação atual:** [você mesmo executa a maioria / já há distribuição / equipe nova]
**Objetivo:** [descentralizar execução / clarificar aprovação / identificar sobrecarga]

Entregue:

**1. Matriz RACI completa**
Tabela com: linhas = atividades/processos, colunas = cargos. Célula preenchida com R, A, C ou I.

**2. Legenda e guia de uso**
Definição de cada letra com exemplos práticos do contexto logístico.

**3. Análise de concentração**
Por cargo: quantos R, A, C e I cada um tem. Identificar sobrecarga e subutilização.

**4. Alertas e inconsistências**
Atividades sem A definido, atividades com múltiplos A, atividades sem nenhum R.

**5. Recomendações de redistribuição**
Sugestões de transferência de responsabilidades com justificativa — especialmente para aliviar o gestor das execuções que podem ser delegadas.
```

## Exemplo de uso

### Input
- Atividades: recebimento de NF, conferência física, lançamento no WMS, posicionamento de estoque, inventário, emissão de NF de saída, gestão de escala, treinamento de novos colaboradores
- Cargos: Gestor de Operações, Supervisor de Armazém, Auxiliar de Armazém (2), Assistente Administrativo
- Situação: gestor executa ou aprova quase tudo
- Objetivo: descentralizar execução, gestor foca em supervisão e melhoria

### Output
| Atividade | Gestor Ops | Supervisor Arm | Aux Armazém | Assistente Adm |
|-----------|-----------|----------------|-------------|----------------|
| Recebimento de NF | A | R | C | I |
| Conferência física | I | A | R | — |
| Lançamento no WMS | I | A | R | — |
| Gestão de escala | A | R | I | I |
| Treinamento novos | A | R | C | I |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
