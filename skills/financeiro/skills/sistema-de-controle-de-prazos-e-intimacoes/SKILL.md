---
name: sistema-de-controle-de-prazos-e-intimacoes
description: Criar um sistema completo de controle de prazos e intimações processuais — com lógica de registro, alertas, classificação por urgência e acompanhamento de movimentações — para que o advogado freelancer nunca perca um prazo por desorganização, tenha visão clara de todos os processos em andamento e passe a operar com a segurança de um escritório estruturado.
---

# Sistema de Controle de Prazos e Intimações

## Objetivo
Criar um sistema completo de controle de prazos e intimações processuais — com lógica de registro, alertas, classificação por urgência e acompanhamento de movimentações — para que o advogado freelancer nunca perca um prazo por desorganização, tenha visão clara de todos os processos em andamento e passe a operar com a segurança de um escritório estruturado.

## Quando usar
- Para estruturar o controle de processos quando você ainda faz isso na memória ou em anotações soltas
- Quando o volume de processos cresceu e o controle informal virou risco
- Para criar um sistema de alertas e registro de intimações que funcione sem software caro
- Ao montar um protocolo de trabalho para quando delegar tarefas processuais a um assistente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe seus tipos de processo, volume atual e ferramentas disponíveis
3. Receba o sistema estruturado com templates, regras de prazo e fluxo de controle
4. Implemente em planilha, Notion, Trello ou no sistema que você já usa

## O Prompt
```
Você é um especialista em gestão de escritórios jurídicos e compliance processual para advogados autônomos e freelancers. Seus princípios: (1) prazo perdido é o maior risco da advocacia — nenhum sistema é perfeito, mas todo sistema é melhor do que a memória, (2) controle de intimações não é sobre tecnologia, é sobre disciplina de processo — o melhor sistema é o que o advogado realmente vai usar, (3) alerta de prazo deve chegar antes que seja urgente — configurar para D-5, D-3 e D-1, (4) registro de movimentação processual tem valor duplo: operacional (não perder prazo) e estratégico (histórico para tomada de decisão).

Preciso estruturar meu sistema de controle de prazos e intimações.

**Tipos de processo que você trabalha:** [ex: cível, trabalhista, tributário, contratual]
**Volume aproximado de processos:** [quantos processos ativos você acompanha]
**Como você controla hoje:** [ex: memória, anotações no celular, planilha básica, sem controle formal]
**Ferramentas disponíveis:** [planilha, Notion, Trello, Google Calendar, sistema jurídico]
**Maior risco atual:** [o que você mais teme — perder prazo, esquecer movimentação, não informar cliente]
**Você trabalha sozinho ou tem assistente:** [isso muda o fluxo de delegação]

Entregue:

**1. Estrutura do sistema de controle**
Campos obrigatórios para cada processo: o que registrar, em qual momento e por quê.

**2. Template de planilha de controle**
Colunas completas para uma planilha de controle de processos e prazos, com instruções de preenchimento.

**3. Fluxo de processamento de intimação**
Passo a passo do momento em que você recebe uma intimação até o registro, calculo do prazo e agendamento do alerta.

**4. Régua de alertas**
Sistema de alertas por prazo: o que configurar em D-10, D-5, D-3 e D-1 para cada tipo de ato processual.

**5. Rotina semanal de revisão processual**
Checklist de 10 minutos para revisar toda semana todos os processos ativos e garantir que nenhum prazo foi esquecido.

**6. Template de atualização para o cliente**
Mensagem padrão para informar o cliente sobre movimentações processuais — clara, profissional e sem jargão excessivo.
```

## Exemplo de uso

### Input
- Tipos: Contratos e cível (cobrança, revisional, indenização)
- Volume: ~25 processos ativos
- Controle atual: Anotações no celular + planilha básica
- Ferramentas: Google Sheets + Google Calendar
- Maior risco: Perder prazo para contestação ou recurso
- Trabalha: Sozinho

### Output
| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| Nº Processo | Número CNJ completo | 0001234-00.2024.8.26.0001 |
| Vara/Tribunal | Onde corre o processo | 5ª Vara Cível SP |
| Parte Contrária | Nome e advogado adverso | Beta Ltda — Dr. X |
| Tipo de Ação | Classificação | Cobrança / Indenização |
| Fase Atual | Momento processual | Aguardando contestação |
| Última Intimação | Data e conteúdo | 10/04 — Prazo para contestar |
| Prazo Fatal | Data limite absoluta | 24/04/2026 |
| Alerta D-5 | Data do primeiro alerta | 19/04/2026 |
| Alerta D-1 | Data do alerta final | 23/04/2026 |
| Status | Situação do prazo | 🔴 Urgente / 🟡 Atenção / 🟢 Ok |
| Próxima Ação | O que precisa ser feito | Redigir contestação |
| Cliente Informado | Foi atualizado? | Sim — 11/04 |

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
