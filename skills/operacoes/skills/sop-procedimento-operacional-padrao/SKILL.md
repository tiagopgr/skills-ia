---
name: sop-procedimento-operacional-padrao
description: Criar SOPs (Procedimentos Operacionais Padrão) completos para qualquer processo repetitivo do negócio — onboarding de cliente, entrega de projeto, briefing de parceiro, fechamento de contrato, faturamento mensal — para que cada processo seja executado da mesma forma toda vez, com ou sem você, eliminando o retrabalho por esquecimento e criando a consistência que hoje falta na operação.
---

# SOP — Procedimento Operacional Padrão

## Objetivo
Criar SOPs (Procedimentos Operacionais Padrão) completos para qualquer processo repetitivo do negócio — onboarding de cliente, entrega de projeto, briefing de parceiro, fechamento de contrato, faturamento mensal — para que cada processo seja executado da mesma forma toda vez, com ou sem você, eliminando o retrabalho por esquecimento e criando a consistência que hoje falta na operação.

## Quando usar
- Para documentar um processo que você faz bem mas que depende da sua memória para acontecer
- Ao precisar repassar uma atividade para um parceiro ou assistente eventual
- Quando um mesmo processo tiver resultado inconsistente — ora funciona, ora não
- Para construir a base operacional do negócio antes de contratar alguém ou crescer

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo que quer documentar, seus passos e os pontos de falha conhecidos
3. Receba o SOP completo com checklist, responsável por etapa e critérios de qualidade
4. Salve no Notion ou Google Docs e consulte toda vez que for executar o processo

## O Prompt
```
Você é um especialista em operações e documentação de processos para empresas de pequeno porte e prestadores de serviços. Seus princípios: (1) um bom SOP é escrito para que alguém que nunca fez aquele processo consiga executar sem precisar te perguntar nada, (2) SOP muito longo não é seguido — o ideal é 1 página com checklist visual, fluxo e exceções documentadas, (3) cada etapa do SOP deve ter um responsável, um critério de conclusão e um prazo — sem isso, é só uma lista de desejos, (4) o SOP deve ser testado por alguém que não criou o processo — se essa pessoa tiver dúvidas, o SOP está incompleto.

Crie um SOP completo para o processo descrito com base nas informações abaixo:

**Nome do processo:** [ex: Onboarding de novo cliente / Entrega de relatório mensal / Briefing de parceiro]
**Objetivo do processo:** [o que precisa ter acontecido quando o processo estiver completo]
**Gatilho de início:** [o que dispara este processo — ex: contrato assinado / e-mail recebido / todo dia X]
**Passos que você já identifica:** [liste os passos que você conhece, mesmo que incompletos]
**Ferramentas usadas no processo:** [ex: Notion, WhatsApp, Google Drive, Canva, e-mail]
**Quem executa:** [só você / você + parceiro / pode ser delegado]
**Pontos de falha conhecidos:** [onde o processo costuma travar ou dar errado]
**Critério de conclusão:** [como saber que o processo foi concluído com sucesso]

Entregue:

**1. Visão geral do processo**
Nome, objetivo, gatilho, duração estimada e quem executa.

**2. Fluxo do processo (etapa a etapa)**
Cada etapa numerada com: ação | responsável | ferramenta usada | critério de conclusão da etapa | tempo estimado.

**3. Checklist de execução**
Versão resumida em formato de checklist para marcar durante a execução.

**4. Pontos de atenção e exceções**
O que fazer quando algo foge do padrão — as exceções mais comuns e como tratar cada uma.

**5. Critério de qualidade**
Como saber que o processo foi bem executado — métricas ou critérios objetivos.

**6. Log de versão**
Campo para registrar quando o SOP foi atualizado e o que mudou.
```

## Exemplo de uso

### Input
- Processo: Onboarding de novo cliente
- Objetivo: Cliente começa a receber atendimento de forma estruturada e com expectativas alinhadas
- Gatilho: Contrato assinado e primeiro pagamento confirmado
- Passos conhecidos: Apresentar-se por ligação, pedir informações do negócio, apresentar parceiros, definir frequência de reunião
- Ferramentas: WhatsApp, Google Drive, Notion
- Pontos de falha: Às vezes esquece de pedir o acesso às ferramentas do cliente antes de começar

### Output
| # | Ação | Responsável | Ferramenta | Conclusão | Tempo |
|---|---|---|---|---|---|
| 1 | Enviar WhatsApp de boas-vindas com próximos passos | Frederico | WhatsApp | Mensagem entregue | 5 min |
| 2 | Criar pasta do cliente no Google Drive | Frederico | Google Drive | Pasta criada e organizada | 10 min |
| 3 | Enviar formulário de onboarding (dados do negócio) | Frederico | Google Forms | Cliente preencheu | até 24h |
| 4 | Agendar call de kickoff (dentro de 3 dias úteis) | Frederico | Google Calendar | Call confirmada | 5 min |
| 5 | Solicitar acessos necessários (redes, analytics, etc.) | Frederico | E-mail | Acessos recebidos | até 48h |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
