---
name: conciliacao-bancaria-assistida
description: Executar a conciliação bancária de forma estruturada — comparando o saldo do extrato bancário com o saldo contábil ou de controle interno, identificando divergências, lançamentos não reconhecidos, tarifas ocultas e pendências — e gerar um relatório de conciliação com as inconsistências priorizadas por valor. Transforma uma tarefa manual e demorada em um processo rápido com output documentado.
---

# Conciliação Bancária Assistida

## Objetivo
Executar a conciliação bancária de forma estruturada — comparando o saldo do extrato bancário com o saldo contábil ou de controle interno, identificando divergências, lançamentos não reconhecidos, tarifas ocultas e pendências — e gerar um relatório de conciliação com as inconsistências priorizadas por valor. Transforma uma tarefa manual e demorada em um processo rápido com output documentado.

## Quando usar
- No fechamento do mês para conciliar o extrato com o controle financeiro interno
- Quando identificar diferença entre o saldo bancário e o saldo no sistema de gestão
- Para auditar uma conta que nunca foi formalmente conciliada
- Ao assumir a gestão financeira de um cliente novo e precisar "limpar" o histórico

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o extrato bancário e os lançamentos do controle interno (pode ser da planilha)
3. Informe o período e o saldo esperado
4. Receba o relatório de conciliação com divergências identificadas e orientação para cada uma

## O Prompt
```
Você é um controller financeiro especialista em conciliação bancária e auditoria de lançamentos. Seus princípios: (1) zero tolerância a diferença inexplicada — toda divergência tem uma causa e precisa ser investigada; (2) classificação por risco — separe o que é erro do que é timing (lançamento em trânsito); (3) praticidade — ao identificar uma divergência, já aponte a ação de resolução; (4) rastreabilidade — cada achado deve ter referência ao lançamento de origem.

**Período da conciliação:** [ex: Março/2025]

**Saldo final do extrato bancário:** [R$ valor]

**Saldo final do controle interno (planilha/sistema):** [R$ valor]

**Diferença identificada:** [R$ valor — calcule: extrato - controle]

**Lançamentos do extrato bancário:**
[cole os lançamentos do extrato — data, descrição, valor]

**Lançamentos do controle interno:**
[cole os lançamentos da planilha ou sistema — data, descrição, valor]

**Observações do período:**
[ex: teve cheque emitido que não compensou, transferência programada para dia 2 do mês seguinte]

Entregue:

**1. Status da Conciliação**
Saldo extrato | Saldo controle | Diferença | Status (Conciliado / Pendente / Com divergência)

**2. Lançamentos presentes no extrato mas ausentes no controle**
Tabela: Data | Descrição | Valor | Classificação sugerida | Ação necessária

**3. Lançamentos no controle mas ausentes no extrato**
Tabela: Data | Descrição | Valor | Possível causa | Ação necessária

**4. Divergências de valor**
Lançamentos que existem nos dois lados mas com valores diferentes — tabela comparativa.

**5. Pendências a resolver**
Lista priorizada (do maior para o menor valor) com: Item | Valor | Responsável pela resolução | Prazo sugerido

**6. Parecer da conciliação**
Conclusão em 3 linhas: se a diferença é explicável, o risco e o que precisa ser feito para fechar.
```

## Exemplo de uso

### Input
- Período: Fevereiro/2025
- Saldo extrato: R$ 23.450
- Saldo controle: R$ 21.980
- Diferença: R$ 1.470

### Output
| Data | Descrição | Valor | Classificação sugerida | Ação |
|---|---|---|---|---|
| 14/02 | TARIFA DOC/TED | R$ 45,00 | Tarifa bancária | Lançar no controle |
| 22/02 | IOF OPERAÇÃO 88231 | R$ 125,00 | IOF empréstimo | Confirmar operação e lançar |
| 28/02 | PIX 77889 SEM DESC | R$ 1.300,00 | Não identificado | Confirmar com titular da conta urgente |

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
