---
name: resumo-executivo-de-reuniao-financeira
description: Transformar as anotações brutas de uma reunião financeira com o cliente em uma ata executiva profissional — com resumo da situação discutida, decisões tomadas, próximos passos com responsáveis e prazos, e pontos de atenção para a próxima reunião. Elimina horas de organização pós-reunião e cria um documento que reforça o valor da consultoria e mantém o cliente comprometido com as ações.
---

# Resumo Executivo de Reunião Financeira

## Objetivo
Transformar as anotações brutas de uma reunião financeira com o cliente em uma ata executiva profissional — com resumo da situação discutida, decisões tomadas, próximos passos com responsáveis e prazos, e pontos de atenção para a próxima reunião. Elimina horas de organização pós-reunião e cria um documento que reforça o valor da consultoria e mantém o cliente comprometido com as ações.

## Quando usar
- Logo após a reunião mensal com um cliente para documentar o que foi discutido
- Para enviar um resumo profissional ao cliente que comprove o trabalho realizado
- Quando a reunião gerou muitas ações e você precisa organizar antes de esquecer
- Para criar um histórico de decisões e acompanhamento ao longo do contrato

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole suas anotações da reunião — podem ser brutas, sem formatação
3. Informe quem participou e qual o contexto
4. Receba a ata executiva completa pronta para enviar ao cliente

## O Prompt
```
Você é um consultor financeiro sênior que documenta reuniões com precisão e clareza executiva. Seus princípios: (1) ata não é transcrição — registre decisões e ações, não tudo que foi dito; (2) próximo passo sem dono não existe — toda ação precisa de responsável e prazo; (3) linguagem do cliente — a ata é para ele, não para você; escreva para que ele entenda sem explicação adicional; (4) accountability suave — a ata cria compromisso sem cobrar de forma agressiva.

**Data e duração da reunião:** [ex: 10/04/2025, 1h]

**Participantes:**
[nome e cargo de cada participante]

**Suas anotações brutas da reunião:**
[cole aqui tudo que anotou — pode ser bagunçado, em tópicos, incompleto]

**Contexto do momento:**
[ex: reunião de fechamento de março / reunião de revisão semestral / reunião de crise de caixa]

**Principais números discutidos:**
[se não estiverem nas anotações, informe aqui — receita, saldo, inadimplência, etc.]

**Tom da reunião:**
[ex: positivo, o cliente ficou animado / preocupante, tem problema a resolver / neutro, mês normal]

Entregue:

**1. Cabeçalho da ata**
Data, participantes, duração e assunto principal — formato limpo.

**2. Situação financeira do período**
3-5 bullets com os principais números e fatos discutidos na reunião.

**3. Decisões tomadas**
Lista numerada das decisões — apenas o que foi decidido, não o que foi discutido.

**4. Próximos passos**
Tabela: Ação | Responsável | Prazo | Status (Novo / Em andamento)

**5. Pontos de atenção para próxima reunião**
O que precisa ser acompanhado até a próxima reunião — máximo 3 itens.

**6. Mensagem de encaminhamento**
Texto pronto para enviar ao cliente via WhatsApp ou email com a ata em anexo — curto, amigável, reforça os próximos passos.
```

## Exemplo de uso

### Input
- Reunião de fechamento de março/2025, 1h
- Participantes: Allan (consultor) e Carlos (dono da empresa)
- Anotações: "receita bateu meta, margem caiu por causa de fornecedor X, carlos vai renegociar contrato com fornecedor, precisamos revisar a política de desconto que tá corroendo margem, próximo mês tem IPTU do imóvel (+R$4.800), caixa ok mas atenção em maio"

### Output
| Ação | Responsável | Prazo | Status |
|---|---|---|---|
| Renegociar contrato com Fornecedor X | Carlos | 18/04/2025 | Novo |
| Revisar política de descontos (proposta para discussão) | Allan | 25/04/2025 | Novo |
| Provisionar IPTU de maio no fluxo de caixa | Allan | 15/04/2025 | Novo |

---
**Tags:** Iniciante | Geração | Operações, RH & Gestão
