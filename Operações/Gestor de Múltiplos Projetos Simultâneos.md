---
name: gestor-de-multiplos-projetos-simultaneos
description: Criar um sistema de acompanhamento para múltiplos projetos rodando ao mesmo tempo — com visão consolidada de status, próximos passos e riscos — para que o gestor pare de depender da memória ou de planilhas confusas e tenha em 5 minutos uma visão clara do que está atrasado, do que precisa de atenção e do que está no caminho certo.
---

# Gestor de Múltiplos Projetos Simultâneos

## Objetivo
Criar um sistema de acompanhamento para múltiplos projetos rodando ao mesmo tempo — com visão consolidada de status, próximos passos e riscos — para que o gestor pare de depender da memória ou de planilhas confusas e tenha em 5 minutos uma visão clara do que está atrasado, do que precisa de atenção e do que está no caminho certo.

## Quando usar
- Quando você gerencia 3 ou mais projetos ao mesmo tempo e perde o fio de algum
- Para preparar o briefing semanal da equipe sobre o andamento dos projetos
- Quando um projeto atrasou e você precisa reorganizar as prioridades dos outros
- Para apresentar o portfólio de projetos em andamento para a liderança

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste todos os projetos em andamento com status atual e contexto
3. Receba o painel consolidado com análise de status, riscos e próximos passos
4. Use toda semana para fazer o check-in de projetos — leva menos de 10 minutos

## O Prompt
```
Você é um especialista em gestão de projetos e portfólios para líderes com múltiplas frentes simultâneas. Seus princípios: (1) projeto sem next action definida é projeto parado — o próximo passo concreto é o que move, não o plano geral, (2) visão de portfólio precisa mostrar o que está em risco, não o que está bem — o que está bem não precisa de atenção gerencial, (3) a maioria dos atrasos de projeto acontece quando ninguém está olhando — check-in semanal de 10 minutos salva projetos inteiros, (4) gestor de portfólio não executa tudo — ele garante que cada projeto tem um responsável claro e o próximo passo definido.

Preciso criar um painel de acompanhamento dos meus projetos.

**Lista de projetos ativos:** [para cada projeto: nome, objetivo, prazo final, responsável principal]
**Status atual de cada projeto (informal):** [o que está acontecendo — pode ser desestruturado]
**Dependências entre projetos:** [algum projeto depende de outro para avançar?]
**Recursos da equipe:** [quem está alocado em quê — se souber]
**O que está me preocupando:** [projetos ou situações que estão gerando ansiedade]

Entregue:

**1. Painel de portfólio (tabela)**
Para cada projeto: Nome | Status (Verde/Amarelo/Vermelho) | % Conclusão estimada | Próximo passo concreto | Responsável | Prazo do próximo passo | Risco principal.

**2. Top 3 projetos que precisam de atenção agora**
Os projetos em maior risco, com análise de por que estão em risco e ação sugerida para desbloquear.

**3. Mapa de carga da equipe**
Distribuição visual de quem está sobrecarregado e quem tem capacidade disponível.

**4. Decisões que só o gestor pode tomar**
Lista de pontos em projetos que estão travados esperando uma decisão sua — para você zerar a fila.

**5. Template de check-in semanal de projetos**
Formato para revisar o portfólio em 10 minutos toda semana com a equipe.
```

## Exemplo de uso

### Input
- Projetos: (1) Treinamento regional maio — ministrando em 3 cidades, prazo mai/15; (2) Atualização do material do produto X — aguardando aprovação regulatória; (3) Expansão de cobertura Sul — parado por ausência do representante; (4) Implementação do CRM de solicitações — em andamento com analista; (5) Relatório Q2 para diretoria — prazo jun/30
- Status informal: Treinamento no prazo mas logística confusa; material travado há 3 semanas no regulatório; Sul parado; CRM 60% feito; relatório ainda não começou
- Dependências: Material do produto X impacta o treinamento de maio
- Preocupação: Material não sair antes do treinamento; relatório Q2 ser feito em cima da hora

### Output
| Projeto | Status | Próximo passo | Responsável | Prazo | Risco |
|---------|--------|---------------|-------------|-------|-------|
| Treinamento regional | 🟡 Amarelo | Confirmar logística das 3 cidades | Assistente | Sex | Material dependente de regulatório |
| Material produto X | 🔴 Vermelho | Escalar aprovação regulatória | Gestor (hoje) | Urgente | Bloqueia treinamento se atrasar |
| Expansão Sul | 🔴 Vermelho | Definir cobertura temporária | Gestor | Seg | Sem solução = meta Q2 em risco |
| CRM de solicitações | 🟢 Verde | Revisar fase 2 do analista | Analista | Qui | Nenhum |
| Relatório Q2 | 🟡 Amarelo | Iniciar coleta de dados agora | Analista | Mai/30 | Começa tarde se esperar junho |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
