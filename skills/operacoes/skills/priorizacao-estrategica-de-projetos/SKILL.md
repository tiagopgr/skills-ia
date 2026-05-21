---
name: priorizacao-estrategica-de-projetos
description: Aplicar um framework de priorização em uma lista de projetos, iniciativas ou melhorias em disputa — avaliando impacto no resultado, esforço de execução, alinhamento estratégico e urgência — para que o diretor pare de tentar fazer tudo ao mesmo tempo, decida com critérios objetivos e concentre os recursos da empresa nos projetos que realmente movem o negócio.
---

# Priorização Estratégica de Projetos

## Objetivo
Aplicar um framework de priorização em uma lista de projetos, iniciativas ou melhorias em disputa — avaliando impacto no resultado, esforço de execução, alinhamento estratégico e urgência — para que o diretor pare de tentar fazer tudo ao mesmo tempo, decida com critérios objetivos e concentre os recursos da empresa nos projetos que realmente movem o negócio.

## Quando usar
- Quando há mais projetos na fila do que capacidade para executar
- Para decidir o que entra no trimestre vs. o que fica para depois
- Ao montar o planejamento anual e precisar cortar iniciativas
- Quando o time está sobrecarregado e tudo parece urgente ao mesmo tempo

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste os projetos em disputa e descreva o contexto da empresa
3. Receba a análise com pontuação, ranking e recomendação de portfólio
4. Use para apresentar a decisão ao time e alinhar expectativas

## O Prompt
```
Você é um consultor de estratégia e gestão de portfólio de projetos, especializado em ajudar empresas de médio porte a decidir onde concentrar recursos limitados. Seus princípios: (1) dizer não a bons projetos é necessário para dizer sim aos ótimos; (2) urgência percebida raramente coincide com impacto real; (3) projetos sem dono e prazo não são projetos, são intenções; (4) o portfólio ideal equilibra projetos de resultado rápido (90 dias) com projetos de impacto estrutural (6-18 meses).

Aplique o framework de priorização estratégica para o seguinte contexto:

**Objetivo estratégico principal da empresa agora:** [ex: crescer 25%, reduzir custo, melhorar retenção]
**Projetos em disputa:** [liste cada projeto com uma frase descrevendo o objetivo]
**Capacidade de execução atual:** [ex: 2 gerentes disponíveis, orçamento de R$50k, 3 meses de ciclo]
**O que não pode ser adiado (restrições regulatórias, contratuais ou de risco):** [se houver]
**Critérios que importam mais para a empresa agora:** [ex: receita, custo, qualidade, risco]

Entregue:

**1. Avaliação de cada projeto**
Tabela com: Projeto | Impacto no resultado (1-5) | Esforço de execução (1-5) | Alinhamento estratégico (1-5) | Urgência real (1-5) | Pontuação total.

**2. Ranking priorizado**
Lista ordenada dos projetos com pontuação final e classificação: Fazer agora / Planejar para próximo ciclo / Delegar / Descartar.

**3. Portfólio recomendado**
Combinação ideal de projetos para o ciclo atual, respeitando a capacidade disponível, com equilíbrio entre resultado rápido e impacto estrutural.

**4. Justificativa das exclusões**
Para cada projeto que ficou de fora: por que não agora e quando faria sentido retomar.

**5. Plano de comunicação para o time**
Como apresentar a decisão de priorização ao time sem gerar desmotivação nos donos dos projetos que não entraram.
```

## Exemplo de uso

### Input
- Objetivo: Reduzir custo operacional em 15% e melhorar NPS
- Projetos: (1) Implantar sistema de gestão de OS digital, (2) Criar programa de retenção de funcionários, (3) Abrir nova unidade em outra cidade, (4) Padronizar processos de limpeza com SOPs, (5) Criar portal do cliente, (6) Renegociar contratos de fornecedores
- Capacidade: 1 gerente de projetos + R$30k de orçamento
- Restrições: Nenhuma
- Critérios: Custo e qualidade do serviço

### Output
| # | Projeto | Pontuação | Classificação |
|---|---------|-----------|---------------|
| 1 | Padronizar processos com SOPs | 18/20 | Fazer agora |
| 2 | Renegociar contratos de fornecedores | 17/20 | Fazer agora |
| 3 | Programa de retenção de funcionários | 15/20 | Planejar Q3 |
| 4 | Sistema de gestão de OS digital | 13/20 | Planejar Q3 |
| 5 | Portal do cliente | 9/20 | Descartar por ora |
| 6 | Nova unidade | 7/20 | Descartar por ora |

---
**Tags:** Avançado | Análise | Operações, RH & Gestão
