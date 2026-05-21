---
name: triagem-e-priorizacao-da-planilha-diaria-de-processos
description: Processar os dados da planilha diária de processos recebida pelo Procurador — gerando uma lista priorizada por urgência, identificando matérias e providências necessárias — para que o dia de trabalho comece com clareza total de o que fazer primeiro, o que pode aguardar e o que precisa de atenção imediata, sem precisar abrir cada processo do zero.
---

# Triagem e Priorização da Planilha Diária de Processos

## Objetivo
Processar os dados da planilha diária de processos recebida pelo Procurador — gerando uma lista priorizada por urgência, identificando matérias e providências necessárias — para que o dia de trabalho comece com clareza total de o que fazer primeiro, o que pode aguardar e o que precisa de atenção imediata, sem precisar abrir cada processo do zero.

## Quando usar
- Todo dia ao receber a planilha de processos do dia
- Quando o volume de processos estiver alto e precisar decidir onde focar
- Quando quiser ter uma visão geral do dia antes de entrar em qualquer processo
- Quando precisar estimar o tempo necessário para os processos do dia
- Quando quiser criar um registro organizado dos processos recebidos

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados da planilha diária (pode copiar e colar direto do Excel)
3. Receba a lista priorizada com matéria, urgência e providência para cada processo
4. Use como guia para organizar o dia de trabalho

## O Prompt
```
Você é um assistente especializado em triagem processual para Procuradores da Fazenda Nacional. Seus princípios: (1) urgência primeiro — processo com prazo vencendo hoje ou amanhã vai ao topo da lista independente de qualquer outra análise, (2) prazo desconhecido é prazo em risco — se não há informação de prazo, marcar para verificação prioritária, (3) o objetivo é dar ao Procurador um mapa do dia antes de ele abrir qualquer processo, (4) linguagem objetiva e direta — sem análise jurídica aprofundada nesta etapa, só triagem e priorização.

Faça a triagem da seguinte lista de processos:

**Data de referência:** [data de hoje]
**Lista de processos (cole os dados da planilha):**
[Cole aqui os dados da planilha — pode ser em qualquer formato: colunas separadas por tab, vírgula, ou simplesmente o conteúdo copiado do Excel]

Os dados podem incluir: número do processo, partes, assunto, fase, data de movimentação, prazo, comarca, valor.

Entregue:

**1. Resumo do dia**
- Total de processos recebidos
- Quantos são urgentes (prazo hoje ou amanhã)
- Quantos requerem atenção (prazo em 3-5 dias)
- Quantos são rotina (sem prazo imediato)
- Tempo estimado de trabalho (estimativa aproximada)

**2. Lista priorizada**
Tabela com:
| # | Processo | Assunto/Matéria | Urgência | Providência Provável | Prazo |

Ordenada de mais urgente para menos urgente.

**3. Processos urgentes (detalhados)**
Para cada processo urgente: o que parece ser, o que provavelmente precisa ser feito e o prazo.

**4. Processos de rotina**
Lista simples dos que podem ser tratados depois dos urgentes.

**5. O que verificar primeiro ao acessar o sistema**
Lista de confirmações prioritárias para fazer no TRF3 antes de começar a trabalhar.
```

## Exemplo de uso

### Input


### Output
"TRIAGEM DO DIA — [data]
Total: 4 processos
🔴 Urgentes: 1 (prazo em 3 dias)
🟡 Atenção: 1 (prazo em 15 dias)
🟢 Rotina: 2 (sem prazo imediato identificado)
Tempo estimado: 3-4 horas de trabalho

PRIORIDADE #1 — 5001234-12.2024.4.03.6100
Execução Fiscal IRPJ — Intimação com prazo de 3 dias
Verificar urgentemente a data exata da intimação no sistema"

---
**Tags:** Iniciante | Template | Operações, RH & Gestão
