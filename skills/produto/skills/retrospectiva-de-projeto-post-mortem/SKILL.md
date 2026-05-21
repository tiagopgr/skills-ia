---
name: retrospectiva-de-projeto-post-mortem
description: Conduzir uma retrospectiva estruturada de projeto — analisando o que funcionou, o que falhou e o que aprender — para transformar erros em lições e acertos em processos replicáveis, criando uma cultura de melhoria contínua na equipe.
---

# Retrospectiva de Projeto (Post-Mortem)

## Objetivo
Conduzir uma retrospectiva estruturada de projeto — analisando o que funcionou, o que falhou e o que aprender — para transformar erros em lições e acertos em processos replicáveis, criando uma cultura de melhoria contínua na equipe.

## Quando usar
- Ao finalizar qualquer projeto significativo
- Após incidentes ou crises operacionais
- No final de sprints (equipes ágeis)
- Quando um projeto deu muito certo (documentar o que funcionou)

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto e o que aconteceu
3. Receba a estrutura da retrospectiva
4. Conduza a reunião com a equipe usando o roteiro

## O Prompt
```
Você é um facilitador de retrospectivas que sabe que: (1) retrospectiva sem ação é só reclamação organizada, (2) o ambiente precisa ser seguro para que as pessoas falem a verdade, (3) o foco é aprender e melhorar, não culpar, (4) os 3 outputs obrigatórios são: o que manter, o que parar, o que começar — com donos e prazos.

Crie a retrospectiva do projeto:

**Nome do projeto:** [título]
**Duração:** [prazo planejado vs prazo real]
**Equipe:** [quem participou]
**Objetivo original:** [o que deveria ter sido entregue]
**Resultado real:** [o que foi entregue de fato]
**O que deu certo:** [liste os pontos positivos]
**O que deu errado:** [liste os problemas]
**O projeto foi considerado um sucesso?** [sim, parcial, não — e por quê]

Entregue: Roteiro da reunião (60-90 min), Análise estruturada com 5 Porquês, Framework "Manter, Parar, Começar", Plano de ação com responsáveis, Documento de lições aprendidas.
```

## Exemplo de uso

### Input
Projeto: Lançamento do novo site da empresa
Planejado: 45 dias | Real: 68 dias (+23 dias de atraso)
Deu certo: Design ficou excelente, equipe de dev performou bem
Deu errado: Cliente mudou escopo 3 vezes, aprovações demoraram
Sucesso: Parcial — site ficou bom mas atrasou e estourou orçamento

### Output
Problema: Mudança de escopo 3 vezes durante o projeto

5 Porquês:
1. Por que o escopo mudou? O cliente pediu funcionalidades novas.
2. Por que ele pediu? Não tinha clareza do que queria no início.
3. Por que não tinha clareza? O briefing não aprofundou as necessidades reais.
4. Por que o briefing foi superficial? Não temos um framework padrão de discovery.
5. Por que não temos? Nunca priorizamos criar um — cada PM faz do seu jeito.

Causa raiz: Falta de processo padronizado de discovery/briefing.

Ação: Criar template de briefing obrigatório. Responsável: PM Lead. Prazo: 15 dias.

---
**Tags:** Intermediário | Template | Produto, E-commerce & SaaS
