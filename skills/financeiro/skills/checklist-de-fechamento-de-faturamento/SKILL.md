---
name: checklist-de-fechamento-de-faturamento
description: Criar um checklist completo e sequencial para o fechamento mensal de faturamento de convênios — cobrindo desde a conferência das guias até o protocolo de envio e acompanhamento de pagamento — para que nenhuma etapa crítica seja pulada, os prazos sejam cumpridos e a taxa de glosas seja minimizada. Para quem faz o faturamento sozinha, este checklist é o processo que garante que o trabalho seja feito da mesma forma todo mês, mesmo sob pressão.
---

# Checklist de Fechamento de Faturamento

## Objetivo
Criar um checklist completo e sequencial para o fechamento mensal de faturamento de convênios — cobrindo desde a conferência das guias até o protocolo de envio e acompanhamento de pagamento — para que nenhuma etapa crítica seja pulada, os prazos sejam cumpridos e a taxa de glosas seja minimizada. Para quem faz o faturamento sozinha, este checklist é o processo que garante que o trabalho seja feito da mesma forma todo mês, mesmo sob pressão.

## Quando usar
- Todo mês no período de fechamento de competência de cada convênio
- Para criar um processo replicável que possa ser delegado quando tiver equipe
- Quando há glosas recorrentes por prazo vencido ou campo faltante
- Para auditar se o fechamento do mês anterior foi completo antes de abrir o próximo

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os convênios que opera, os procedimentos realizados e os prazos de cada operadora
3. Receba o checklist personalizado e completo para seu faturamento
4. Use todo mês, marque cada etapa concluída e arquive o checklist assinado

## O Prompt
```
Você é um especialista em faturamento médico e gestão de contas a receber de clínicas de saúde no Brasil. Seus princípios: (1) faturamento sem processo é faturamento com prejuízo — cada guia não enviada ou enviada errada é receita perdida, (2) o fechamento de faturamento tem três fases distintas que não podem se misturar: pré-fechamento (conferência), fechamento (envio) e pós-fechamento (acompanhamento) — cada fase tem suas próprias verificações, (3) os prazos das operadoras são fatais — guia fora do prazo de competência é glosa automática sem recurso possível, (4) o checklist deve ser um documento físico ou digital que alguém assina ao completar cada etapa — não apenas uma lista mental.

**Convênios que atende:** [liste todos os convênios e planos]
**Procedimentos/serviços faturados:** [ex: consultas, exames audiológicos, vacinas, SADT]
**Prazo de fechamento de cada convênio:** [data de corte mensal de cada operadora]
**Sistema de faturamento utilizado:** [ex: TOTVS, Tasy, planilha própria, envio manual via portal]
**Principal dificuldade atual no fechamento:** [onde perde mais tempo ou onde ocorrem mais erros]
**Tem secretária que auxilia?** [sim / não / às vezes]

Entregue:

**1. Checklist de pré-fechamento (conferência)**
Lista de verificação de todas as guias do período: campos obrigatórios, autorizações, CIDs, códigos TUSS, assinaturas, documentação de suporte.

**2. Checklist de fechamento (envio)**
Etapas de organização do lote, conferência final, protocolo de envio (físico ou eletrônico), comprovante de recebimento.

**3. Checklist de pós-fechamento (acompanhamento)**
Prazo para retorno do convênio, o que verificar na remessa de retorno, como identificar glosas, prazo e processo de recurso.

**4. Calendário mensal de faturamento**
Tabela com cada convênio, data de corte, data ideal de envio, data esperada de pagamento e observações.

**5. Ficha de controle de glosas**
Template para registrar cada glosa recebida: guia, convênio, motivo, valor, ação tomada, resultado.
```

## Exemplo de uso

### Input
- Convênios: Unimed, Bradesco Saúde, Amil, GEAP
- Procedimentos: exames audiológicos (audiometria, imitanciometria), vacinas (particular + convênio), consultas de médicos locatários
- Prazos: Unimed — até dia 5, Bradesco — até dia 10, Amil — até dia 15, GEAP — até dia 8
- Sistema: portal web de cada operadora + planilha de controle própria
- Dificuldade: esquecer guias de procedimentos complementares e perder prazo da Unimed
- Secretária: não

### Output
| Convênio | Corte (competência) | Envio ideal | Pagamento esperado | Alerta |
|----------|--------------------|-----------|--------------------|--------|
| Unimed | Dia 5 | Dia 3 | ~Dia 25 do mês seguinte | Enviar 2 dias antes para margem de correção |
| GEAP | Dia 8 | Dia 6 | ~Dia 28 do mês seguinte | Checar guias de retorno antes de fechar |
| Bradesco | Dia 10 | Dia 8 | ~Dia 30 do mês seguinte | Verificar autorizações eletrônicas pendentes |
| Amil | Dia 15 | Dia 13 | ~Dia 5 do mês +2 | Maior prazo — usar para revisar glosas dos outros |

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
