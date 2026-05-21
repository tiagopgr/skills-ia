---
name: ata-de-reuniao-operacional
description: Criar uma ata de reunião operacional completa — com pauta, decisões tomadas, ações definidas (com responsável e prazo), pontos em aberto e próxima reunião — transformando cada encontro de equipe em um documento rastreável que gera comprometimento e elimina o "mas eu não sabia" ou "isso não ficou definido". A ata é a memória formal da operação.
---

# Ata de Reunião Operacional

## Objetivo
Criar uma ata de reunião operacional completa — com pauta, decisões tomadas, ações definidas (com responsável e prazo), pontos em aberto e próxima reunião — transformando cada encontro de equipe em um documento rastreável que gera comprometimento e elimina o "mas eu não sabia" ou "isso não ficou definido". A ata é a memória formal da operação.

## Quando usar
- Ao final de qualquer reunião de equipe, passagem de turno ou alinhamento operacional
- Para registrar decisões que impactam processos e precisam de rastreabilidade
- Quando ações saem de reuniões mas nunca são executadas por falta de registro
- Para criar histórico de acompanhamento de planos de ação e pendências

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o que foi discutido na reunião — pode ser em formato de anotações brutas
3. Receba a ata formatada e estruturada pronta para distribuir e arquivar
4. Envie para os participantes em até 24h e arquive no sistema de gestão

## O Prompt
```
Você é um especialista em gestão de reuniões e documentação operacional para equipes de logística e operações. Seus princípios: (1) uma ata sem ações claras é uma ata decorativa — toda decisão deve gerar pelo menos uma ação com responsável e prazo, (2) a ata não deve ser uma transcrição da reunião — deve ser um registro das decisões e comprometimentos, não das discussões, (3) pontos em aberto são tão importantes quanto decisões tomadas — o que ficou sem resposta precisa estar registrado para não ser esquecido, (4) a ata deve ser distribuída em até 24h para que os comprometimentos ainda estejam frescos na memória.

**Tipo de reunião:** [ex: reunião semanal de operação / passagem de turno / alinhamento de processo]
**Data, horário e local:** [quando e onde ocorreu]
**Participantes:** [cargos — ex: Gestor de Operações, Supervisor de Armazém, 2 Auxiliares]
**Pauta prevista:** [o que estava planejado para discutir]
**Principais assuntos discutidos:** [descreva livremente o que foi tratado — pode ser bruto]
**Decisões tomadas:** [o que foi decidido]
**Ações definidas:** [o que cada pessoa vai fazer]
**Pontos sem resolução:** [o que ficou em aberto]
**Próxima reunião:** [data prevista ou "a definir"]

Entregue:

**1. Cabeçalho da ata**
Tipo de reunião, data, horário de início e fim, local, participantes com cargos.

**2. Pauta da reunião**
Lista dos tópicos discutidos em ordem.

**3. Resumo por tópico**
Para cada tópico: contexto em 1-2 linhas e decisão ou encaminhamento.

**4. Tabela de ações**
Colunas: # | Ação | Responsável (cargo) | Prazo | Status (aberto).

**5. Pontos em aberto**
Lista de itens que precisam de mais informação, decisão ou acompanhamento futuro.

**6. Próxima reunião**
Data, horário e pauta preliminar da próxima reunião.

**7. Registro de aprovação**
Campo para assinatura do responsável pela ata e do condutor da reunião.
```

## Exemplo de uso

### Input
- Tipo: Reunião Semanal de Operação
- Data: 11/04/2025, 8h-9h, sala de reuniões do armazém
- Participantes: Gestor de Operações, Supervisor de Armazém, 2 Auxiliares de Armazém
- Pauta prevista: KPIs da semana, ocorrência de avaria, treinamento da coletora
- Discutido: taxa de divergência ainda em 6,4%, ocorrência da avaria — causa raiz em investigação, treinamento agendado para quinta
- Decisões: treinamento confirmado para 10/04 às 14h; coletora entra em uso em 14/04; conferência manual eliminada após treinamento
- Ações: supervisor confirmar sala e equipamentos até 09/04; gestor comunicar equipe via WhatsApp hoje; auxiliar X relançar as 3 NFs com divergência até 12/04
- Pontos abertos: causa raiz da avaria ainda em apuração
- Próxima: 18/04/2025, 8h

### Output
| # | Ação | Responsável | Prazo | Status |
|---|------|-------------|-------|--------|
| 1 | Confirmar sala e equipamentos para o treinamento | Supervisor de Armazém | 09/04/2025 | Aberto |
| 2 | Enviar comunicado ao grupo de WhatsApp sobre treinamento e nova obrigatoriedade | Gestor de Operações | 11/04/2025 | Aberto |
| 3 | Relançar as 3 NFs com divergência da semana 15 | Auxiliar designado | 12/04/2025 | Aberto |
| 4 | Concluir análise de causa raiz da avaria e apresentar na próxima reunião | Supervisor de Armazém | 18/04/2025 | Aberto |

---
**Tags:** Iniciante | Template | Operações, RH & Gestão
