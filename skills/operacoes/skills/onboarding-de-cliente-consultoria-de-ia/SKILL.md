---
name: onboarding-de-cliente-consultoria-de-ia
description: Estruturar o processo completo de entrada de um novo cliente de implementação de IA — do "contrato assinado" ao "começando a construir" — com email de boas-vindas, formulário técnico de briefing, checklist de credenciais e acessos necessários, e alinhamento de expectativas. Resolve o início caótico de projetos onde o consultor precisa ir pedindo informações aos poucos, perdendo tempo e transmitindo desorganização.
---

# Onboarding de Cliente — Consultoria de IA

## Objetivo
Estruturar o processo completo de entrada de um novo cliente de implementação de IA — do "contrato assinado" ao "começando a construir" — com email de boas-vindas, formulário técnico de briefing, checklist de credenciais e acessos necessários, e alinhamento de expectativas. Resolve o início caótico de projetos onde o consultor precisa ir pedindo informações aos poucos, perdendo tempo e transmitindo desorganização.

## Quando usar
- Sempre que fechar um novo projeto de implementação de IA
- Para padronizar a entrada de todos os clientes e economizar tempo
- Quando projetos começam com atraso porque as credenciais demoram a chegar
- Para criar uma experiência profissional desde o primeiro dia

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto e o que você precisa do cliente para começar
3. Informe o prazo e o canal de comunicação
4. Receba o kit completo de onboarding

## O Prompt
```
Você é um especialista em processos de consultoria de tecnologia para clientes não técnicos. Seus princípios: (1) cliente não sabe o que você precisa — você precisa perguntar de forma que ele entenda; (2) credenciais primeiro — projeto não começa sem acesso; quanto antes você pede, melhor; (3) expectativa técnica nivelada — o cliente precisa entender o que vai acontecer em cada semana; (4) ponto de contato único — defina quem do cliente fala com você para não ter ruído.

**Projeto:** [descreva o que vai ser implementado]

**O que você precisa do cliente para começar:**
[ex: acesso ao WhatsApp Business / credenciais do sistema de agendamento / acesso ao Google Sheets ou conta Google / chave de API se já tem]

**O que o cliente NÃO precisa saber fazer (você faz):**
[ex: configurar o n8n / criar as integrações / escrever código]

**Prazo do projeto:** [ex: 15 dias corridos após recebimento dos acessos]

**Canal de comunicação:** [WhatsApp / email / reunião semanal]

**Marcos do projeto:**
[ex: semana 1: briefing e acesso / semana 2: construção / semana 3: testes / semana 4: entrega e treinamento]

Entregue:

**1. Email de boas-vindas**
Tom profissional e tranquilizador — o cliente que não é técnico precisa sentir que está em boas mãos.

**2. Formulário de briefing técnico**
Perguntas para coletar todas as informações necessárias — escritas em linguagem que leigo entende.

**3. Checklist de credenciais e acessos**
Lista do que você precisa, com: o que é | para que serve | onde o cliente encontra | como te envia com segurança.

**4. Cronograma visual do projeto**
Semana a semana, o que acontece — escrito para o cliente, não para o técnico.

**5. Regras de trabalho (expectativas)**
O que o cliente pode esperar + o que você precisa dele para cumprir o prazo.

**6. Como enviar credenciais com segurança**
Instrução simples para o cliente não enviar senha por WhatsApp — ex: usar 1Password, Bitwarden ou o método mais simples que você usa.
```

## Exemplo de uso

### Input
- Projeto: bot de confirmação de consultas via WhatsApp para clínica
- Precisa: acesso ao sistema de agendamento da clínica + número WhatsApp Business + conta Google
- Prazo: 15 dias | Canal: WhatsApp

### Output
| O que preciso | Para que serve | Onde você encontra | Como me envia |
|---|---|---|---|
| Login e senha do sistema de agendamento | Para buscar as consultas dos próximos 2 dias automaticamente | Email que você usou para criar a conta no sistema | Via link seguro (te explico como) |
| Número do WhatsApp Business da clínica | Para enviar as confirmações automáticas | O chip que está no celular da recepção | Me informa o número aqui |
| Conta Google (Gmail) | Para guardar os registros num Google Sheets | Qualquer conta Google — pode ser a da clínica | Me manda o email, peço acesso pelo Google |

---
**Tags:** Iniciante | Template | Operações, RH & Gestão
