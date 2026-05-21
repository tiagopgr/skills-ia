---
name: diagnostico-de-sobrecarga-do-gestor
description: Fazer um diagnóstico honesto de tudo que ocupa o tempo do gestor — cruzando o que ele faz com o que só ele deveria fazer — para identificar quais atividades podem ser delegadas, automatizadas ou simplesmente eliminadas, gerando uma lista de ações concretas para recuperar horas da semana sem precisar contratar mais ninguém.
---

# Diagnóstico de Sobrecarga do Gestor

## Objetivo
Fazer um diagnóstico honesto de tudo que ocupa o tempo do gestor — cruzando o que ele faz com o que só ele deveria fazer — para identificar quais atividades podem ser delegadas, automatizadas ou simplesmente eliminadas, gerando uma lista de ações concretas para recuperar horas da semana sem precisar contratar mais ninguém.

## Quando usar
- Quando você sente que está sempre ocupado mas sem avanço real nas prioridades
- Para identificar quais tarefas estão consumindo tempo que deveriam estar na equipe
- Antes de pensar em contratar — para ver se o problema é volume ou distribuição errada
- Para ter uma conversa embasada com a liderança sobre carga de trabalho e recursos

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste tudo que você fez nos últimos 5 dias de trabalho — pode ser desorganizado
3. Receba o diagnóstico com classificação de cada atividade e plano de liberação de tempo
4. Use o plano para começar a delegar ou eliminar atividades nas próximas 2 semanas

## O Prompt
```
Você é um especialista em produtividade executiva e design organizacional. Seus princípios: (1) gestor sobrecarregado é um sintoma de distribuição errada de responsabilidades, não de falta de esforço, (2) a maioria das tarefas que um gestor faz poderia ser feita por outra pessoa — a pergunta certa é: por que ainda está com ele, (3) tempo liberado do gestor se converte em capacidade estratégica — cada hora de operação devolvida vale mais do que uma hora extra trabalhada, (4) o diagnóstico precisa ser honesto — incluir até as tarefas que o gestor gosta de fazer mas não deveria.

Faça um diagnóstico completo da minha sobrecarga de trabalho.

**Meu cargo e contexto:** [descreva sua função, tamanho da equipe e contexto da empresa]
**Tudo que fiz nos últimos 5 dias (lista informal):** [jogue tudo — reuniões, e-mails, tarefas, decisões, conversas, burocracias]
**Minha equipe atual:** [quem tenho disponível — cargos e capacidades gerais]
**O que considero meu trabalho de maior valor:** [as 2-3 coisas que só você pode/deve fazer no seu nível]
**O que mais me irrita na minha rotina:** [atividades que te drenam mas você continua fazendo]

Entregue:

**1. Inventário classificado de atividades**
Tabela com cada atividade listada: Atividade | Tempo estimado/semana | Classificação (Só eu / Pode delegar / Pode automatizar / Pode eliminar) | Justificativa.

**2. Horas recuperáveis por semana**
Cálculo do tempo total que pode ser liberado se as delegações e eliminações forem aplicadas.

**3. Top 5 ações de liberação de tempo**
As 5 mudanças mais impactantes para implementar nas próximas 2 semanas, com instrução prática para cada uma.

**4. O que é trabalho de gestor vs. trabalho de executor**
Uma reflexão honesta sobre quais atividades são incompatíveis com o seu nível hierárquico e por que você ainda está fazendo.

**5. Script de conversa com a equipe**
Como apresentar para a equipe as mudanças de delegação sem parecer que está jogando trabalho neles.
```

## Exemplo de uso

### Input
- Cargo: Gerente médico-científico, equipe de 3 pessoas
- Últimos 5 dias: Respondeu 47 e-mails, foi a 6 reuniões (4 internas, 2 com cliente), fez relatório de KPIs, revisou material do analista 2x por erros, comprou material de escritório, organizou arquivo de um projeto antigo, respondeu dúvidas técnicas no WhatsApp da equipe, fez proposta para 1 cliente, atualizou planilha de visitas, deu feedback para 1 colaborador
- Equipe: Analista, coordenador de campo, assistente administrativo
- Trabalho de maior valor: Estratégia de contas, relacionamento com KOLs, planejamento de longo prazo
- O que irrita: Revisar o mesmo material várias vezes por erros evitáveis, responder e-mails operacionais

### Output
| Atividade | Tempo/semana | Classificação | Justificativa |
|-----------|-------------|---------------|---------------|
| Responder 47 e-mails | ~4h | Pode delegar (triagem) | Assistente pode filtrar e responder 70% |
| Relatório de KPIs | ~2h | Pode delegar | Analista pode montar, gestor só revisa |
| Comprar material de escritório | ~30min | Pode delegar | Tarefa administrativa — assistente |
| Proposta para cliente | ~3h | Só eu (por enquanto) | Requer visão estratégica da conta |
| Revisar material 2x por erros | ~2h | Pode eliminar (processo) | Criar checklist de qualidade evita retrabalho |

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
