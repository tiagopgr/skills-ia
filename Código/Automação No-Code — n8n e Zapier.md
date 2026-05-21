---
name: automacao-no-code-n8n-e-zapier
description: Criar o blueprint completo de um fluxo de automação no-code — descrevendo cada nó, gatilho, condição e ação em linguagem visual e passo a passo — para implementar no n8n ou Zapier sem precisar escrever código. Permite ao consultor de IA construir automações para si e para clientes usando ferramentas visuais, com um roteiro tão claro que qualquer pessoa consegue seguir.
---

# Automação No-Code — n8n e Zapier

## Objetivo
Criar o blueprint completo de um fluxo de automação no-code — descrevendo cada nó, gatilho, condição e ação em linguagem visual e passo a passo — para implementar no n8n ou Zapier sem precisar escrever código. Permite ao consultor de IA construir automações para si e para clientes usando ferramentas visuais, com um roteiro tão claro que qualquer pessoa consegue seguir.

## Quando usar
- Para automatizar processos do próprio negócio sem precisar de desenvolvedor
- Para entregar automações a clientes como parte da implementação de IA
- Quando quer documentar um fluxo de automação antes de construí-lo
- Para criar um template de automação replicável para diferentes clientes do mesmo setor

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo que quer automatizar em linguagem livre
3. Informe as ferramentas que o cliente ou você usa
4. Receba o blueprint completo com cada passo do fluxo e instruções de implementação

## O Prompt
```
Você é um especialista em automação no-code com domínio profundo de n8n, Zapier, Make (Integromat) e ferramentas de integração. Seus princípios: (1) gatilho claro — toda automação começa com "quando X acontece"; (2) um passo por vez — descreva cada ação em sequência, nunca pule etapas; (3) tratamento de exceção — o que acontece quando um dado está faltando ou uma API falha; (4) documente para o cliente — o blueprint deve ser compreensível por quem vai manter depois de você.

**Processo a automatizar (descreva livremente):**
[ex: "quando um lead preenche o formulário do site, quero que: (1) ele receba um email de boas-vindas automático, (2) seu contato seja adicionado no CRM, (3) eu receba uma notificação no WhatsApp"]

**Ferramentas que estão em uso (ou preferidas):**
[liste todas as ferramentas envolvidas — ex: site WordPress, formulário Typeform, CRM HubSpot, email via Gmail, WhatsApp via Z-API]

**Plataforma de automação preferida:**
[n8n (self-hosted, gratuito) / Zapier (pago, mais simples) / Make/Integromat / sem preferência]

**Frequência / gatilho:**
[ex: em tempo real quando o formulário é preenchido / toda manhã às 8h / quando um arquivo é adicionado ao Google Drive]

**Volume estimado:**
[ex: 10 ativações por dia / 200 por mês / imprevisível]

**Nível de complexidade do cliente:**
[básico — poucas ferramentas / intermediário / avançado com banco de dados]

Entregue:

**1. Visão geral do fluxo**
Diagrama textual do fluxo completo: GATILHO → Passo 1 → Passo 2 → [Condição] → Passo 3a / 3b → Resultado final.

**2. Blueprint detalhado — passo a passo**
Para cada nó/etapa: Nome do nó | Tipo (trigger/ação/condição) | Ferramenta | O que configura | Dados que usa | Dados que passa adiante

**3. Configuração de cada integração**
Para cada ferramenta: como conectar a conta, quais permissões dar, qual campo mapear para qual.

**4. Tratamento de erros**
O que configurar para quando: um campo vier vazio / a API retornar erro / a automação falhar silenciosamente.

**5. Como testar antes de ativar**
Passo a passo para testar o fluxo com dados fictícios sem afetar dados reais.

**6. Estimativa de custo**
Se usar Zapier/Make: quantas "operações" esse fluxo consome por mês e qual plano é necessário. Se usar n8n: custo zero.
```

## Exemplo de uso

### Input
- Processo: lead preenche formulário → email automático → adicionar no Notion → notificação no WhatsApp
- Ferramentas: Typeform, Gmail, Notion, WhatsApp (Z-API)
- Plataforma: n8n
- Volume: 5-15 leads por semana

### Output
```
[GATILHO] Typeform — novo preenchimento
    ↓
[AÇÃO 1] Formatar dados (nome, email, telefone, empresa)
    ↓
[CONDIÇÃO] Email é válido?
    ↓ SIM                    ↓ NÃO
[AÇÃO 2a] Gmail —         [AÇÃO 2b] Log de erro
enviar email boas-vindas   no Google Sheets
    ↓
[AÇÃO 3] Notion — criar página em "Leads" com todos os dados
    ↓
[AÇÃO 4] Z-API — enviar mensagem WhatsApp para Pedro
"Novo lead: [Nome] da [Empresa] — ver no Notion: [link]"
```

---
**Tags:** Iniciante | Template | Código, Dev & Automação
