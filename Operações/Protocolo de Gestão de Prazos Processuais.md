---
name: protocolo-de-gestao-de-prazos-processuais
description: Estruturar o sistema de controle e gestão de prazos processuais — com protocolo de registro, alerta antecipado e priorização — para que o Procurador nunca perca um prazo por falta de controle, saiba sempre o que está vencendo nos próximos dias e tenha uma rotina simples de acompanhamento que funcione mesmo nas semanas mais pesadas.
---

# Protocolo de Gestão de Prazos Processuais

## Objetivo
Estruturar o sistema de controle e gestão de prazos processuais — com protocolo de registro, alerta antecipado e priorização — para que o Procurador nunca perca um prazo por falta de controle, saiba sempre o que está vencendo nos próximos dias e tenha uma rotina simples de acompanhamento que funcione mesmo nas semanas mais pesadas.

## Quando usar
- Quando quiser criar ou reorganizar o sistema de controle de prazos
- Quando sentir que os prazos estão se acumulando sem controle visível
- Quando receber um lote novo de processos e quiser organizar o que vence quando
- Quando quiser criar um protocolo simples para usar toda semana
- Quando quiser prevenir que a urgência de prazo "exploda" sem aviso

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os processos que tem em andamento e os prazos conhecidos
3. Receba o sistema de controle organizado e o protocolo de acompanhamento
4. Implemente e atualize semanalmente

## O Prompt
```
Você é um consultor de gestão processual para Procuradores da Fazenda Nacional. Seus princípios: (1) prazo perdido em execução fiscal ou mandado de segurança pode ter consequências graves e irreversíveis — controle de prazo é prioridade absoluta, (2) sistema de controle de prazo que depende só da memória vai falhar — precisa ser externalizado e revisado rotineiramente, (3) alerta com 5 dias de antecedência é o mínimo — o ideal é 10 dias para peças complexas, (4) prazo não confirmado no sistema é prazo em risco — sempre verificar a data exata antes de trabalhar com uma estimativa.

Monte o sistema de gestão de prazos com as seguintes informações:

**Lista de processos com prazos conhecidos ou estimados:**
[Liste: número do processo / tipo de prazo / data de início do prazo / prazo em dias / data de vencimento estimada]

**Processos com prazo incerto (precisa verificar no sistema):**
[Liste os processos onde não sabe a data exata do prazo]

**Data de hoje:** [data]
**Quantos dias úteis você trabalha por semana:** [5 / 4 / outro]
**Onde registra prazos atualmente:** [caderno / planilha / sistema / nenhum lugar]

Entregue:

**1. Mapa de prazos organizado**
Tabela com todos os prazos ordenados por data de vencimento:
| Processo | Tipo de prazo | Vence em | Dias restantes | Urgência | Status |

**2. Alertas imediatos**
Prazos que vencem nos próximos 5 dias úteis — com o que precisa ser feito.

**3. Prazos para verificar no sistema**
Lista de processos onde a data precisa ser confirmada — com instrução de como verificar.

**4. Protocolo semanal de revisão de prazos (10 minutos)**
Passo a passo do que fazer toda segunda-feira para manter o controle atualizado.

**5. Template de registro de prazo**
Modelo simples para registrar cada novo prazo que surgir — pode ser usado em planilha, caderno ou qualquer sistema.
```

## Exemplo de uso

### Input
- Processo 5001234 — Contrarrazões — intimado em 01/04/2025 — 15 dias úteis → vence ~22/04
- Processo 5002345 — Apelação — intimado em 07/04/2025 — 15 dias úteis → vence ~28/04
- Processo 5003456 — Contestação embargos — prazo incerto (precisa verificar)
- Processo 5004567 — MS — informações — intimado em 10/04/2025 — 10 dias → vence ~24/04
- Data: 14/04/2025
- Dias úteis: 5/semana
- Registra prazos: Nenhum lugar fixo

### Output
"MAPA DE PRAZOS — 14/04/2025

| Processo | Tipo | Vence | Dias restantes | Urgência |
|---|---|---|---|---|
| 5001234 | Contrarrazões | 22/04 | 6 dias úteis | 🔴 URGENTE |
| 5004567 | MS — Informações | 24/04 | 8 dias úteis | 🔴 URGENTE |
| 5002345 | Apelação | 28/04 | 10 dias úteis | 🟡 ATENÇÃO |
| 5003456 | Contestação | VERIFICAR | — | ❓ VERIFICAR HOJE |

AÇÃO IMEDIATA:
1. Verificar prazo do processo 5003456 no sistema HOJE — prazo desconhecido é risco
2. Começar as contrarrazões do processo 5001234 HOJE — 6 dias úteis para peça complexa é pouco
3. Preparar MS — Informações do processo 5004567 até quarta"

---
**Tags:** Iniciante | Template | Operações, RH & Gestão
