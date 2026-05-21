---
name: sistema-de-gestao-de-projetos-consultoria-de-ia
description: Criar um sistema operacional completo de gestão de projetos para o consultor de IA solo — com estrutura para controlar clientes ativos, status técnico de cada implementação, credenciais e acessos, prazos de entrega e contratos de manutenção — de forma que o consultor saiba em 30 segundos o que está acontecendo em cada projeto e nunca perca um prazo ou deixe um cliente sem resposta. O consultor de IA que tem caos interno não inspira confiança para resolver o caos dos outros.
---

# Sistema de Gestão de Projetos — Consultoria de IA

## Objetivo
Criar um sistema operacional completo de gestão de projetos para o consultor de IA solo — com estrutura para controlar clientes ativos, status técnico de cada implementação, credenciais e acessos, prazos de entrega e contratos de manutenção — de forma que o consultor saiba em 30 segundos o que está acontecendo em cada projeto e nunca perca um prazo ou deixe um cliente sem resposta. O consultor de IA que tem caos interno não inspira confiança para resolver o caos dos outros.

## Quando usar
- Para montar o sistema de controle de projetos do zero
- Quando está com múltiplos clientes e perdendo o fio dos projetos
- Para criar uma operação organizada que suporte o crescimento
- Ao querer documentar os projetos de forma que possa delegar no futuro

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva sua situação atual — clientes, tipos de projeto, ferramentas disponíveis
3. Informe o que mais te causa problema na organização atual
4. Receba o sistema completo com templates e instrução de implementação

## O Prompt
```
Você é um especialista em sistemas de gestão para consultores de tecnologia solos. Seus princípios: (1) consultor de IA tem projetos técnicos + relacionamento com cliente — o sistema precisa cobrir os dois; (2) credenciais e acessos organizados = menos stress — você nunca deve procurar uma senha na hora errada; (3) status técnico visível — você precisa saber se um fluxo está rodando ou quebrado sem ter que entrar em cada ferramenta; (4) manutenção recorrente é um produto — clientes mensais precisam de gestão separada de projetos avulsos.

**Ferramentas disponíveis ou preferidas:**
[ex: Notion / Google Sheets / Trello / Airtable / qualquer — me recomende a mais simples]

**Tipos de projeto que gerencia:**
[ex: implementações únicas 2-4 semanas / manutenções mensais / consultorias de diagnóstico]

**Número de clientes ativos em média:** [ex: 3-6]

**Principais problemas de organização hoje:**
[ex: não sei onde estão as credenciais dos clientes / perco o status de cada projeto / esqueço de cobrar manutenção mensal / não documento o que foi feito]

**O que quer controlar:**
[status do projeto / credenciais e acessos / prazos / pagamentos / documentação técnica / histórico de comunicação]

Entregue:

**1. Arquitetura do sistema**
Quais "módulos" ou seções criar e o que cada um controla.

**2. Painel de projetos ativos**
Design do dashboard principal — o que aparece e em qual formato para visão rápida.

**3. Ficha de cliente**
Template com todas as informações de cada cliente: contato, ferramentas usadas, credenciais (referência, não a senha em si), contratos, histórico.

**4. Ficha de projeto**
Template para cada implementação: escopo, ferramentas, status técnico, marcos, entregáveis, documentação.

**5. Controle de manutenções recorrentes**
Como gerenciar clientes com contrato mensal — o que verificar, quando cobrar, como documentar.

**6. Gestão segura de credenciais**
Como organizar acessos de clientes sem armazenar senhas em planilha aberta — ferramentas gratuitas recomendadas.

**7. Checklist mensal do consultor**
O que revisar todo mês: projetos / cobranças / clientes em manutenção / pipeline de novos clientes.
```

## Exemplo de uso

### Input
- Ferramenta: Notion (já usa mas de forma bagunçada)
- Projetos: 2 implementações + 3 manutenções mensais
- Problema: não sabe onde estão as credenciais e esquece de cobrar manutenção

### Output
| Cliente | Tipo | Status | Prazo/Próximo check | Pagamento | Ação urgente |
|---|---|---|---|---|---|
| Clínica Sorriso | Implementação | 🔵 Em construção | 20/04 | ✅ 50% pago | Entregar rascunho do fluxo |
| Academia FitLife | Manutenção mensal | 🟢 Rodando | Check 30/04 | 🔴 Maio não cobrado |

---
**Tags:** Iniciante | Template | Operações, RH & Gestão
