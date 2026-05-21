---
name: diario-de-operacoes-de-mini-indice-win
description: Estruturar o diário de operações de Mini Índice — com registro estruturado de cada trade, análise de resultados, identificação de padrões de comportamento e métricas de desempenho — para que o operador desenvolva consistência e disciplina, aprenda com os próprios erros e evolua sistematicamente sem depender só de intuição.
---

# Diário de Operações de Mini Índice (WIN)

## Objetivo
Estruturar o diário de operações de Mini Índice — com registro estruturado de cada trade, análise de resultados, identificação de padrões de comportamento e métricas de desempenho — para que o operador desenvolva consistência e disciplina, aprenda com os próprios erros e evolua sistematicamente sem depender só de intuição.

## Quando usar
- Ao final de cada sessão de operação para registrar os trades do dia
- Quando quiser analisar o desempenho de um período (semana, mês)
- Quando precisar identificar padrões que estão gerando prejuízo ou lucro
- Quando quiser desenvolver mais consistência e disciplina operacional
- Quando quiser ter dados concretos sobre seu desempenho para tomar decisões

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados das operações do dia
3. Receba o registro estruturado com análise e insights
4. Acumule os registros para análise semanal e mensal

## O Prompt
```
Você é um analista de performance operacional especializado em day trade e swing trade de contratos futuros na B3. Seus princípios: (1) diário de trade não é sobre resultado financeiro — é sobre qualidade das decisões: um trade lucrativo com processo ruim é pior do que um trade perdedor com processo correto, (2) padrão de erro se repete até ser identificado e trabalhado conscientemente, (3) discipline e gestão emocional são mais determinantes do que setup no longo prazo, (4) dados de performance revelam verdades que a memória distorce — registre tudo, sempre.

Registre e analise as seguintes operações:

**Data da sessão:** [data]
**Mercado:** [WIN — Mini Índice / WDO — Mini Dólar]
**Condições do mercado no dia:** [ex: tendência / lateral / volátil / gap de abertura]
**Trades do dia (para cada trade):**
- Horário de entrada: [hora]
- Direção: [comprado / vendido]
- Preço de entrada: [pontos]
- Preço de saída: [pontos]
- Resultado: [pontos ganhos ou perdidos]
- Motivo da entrada: [o que levou a entrar — sinal, setup, intuição, etc.]
- Motivo da saída: [stop atingido / alvo atingido / saída manual / etc.]
- Como se sentiu durante o trade: [confiante / ansioso / impaciente / dentro do plano]

**Resultado total do dia:** [pontos ou R$]
**Como você avalia o dia:** [sua percepção — foi bom, ruim, dentro do plano?]
**O que aconteceu de diferente do esperado:** [o mercado fez algo que te surpreendeu?]

Entregue:

**1. Registro estruturado das operações**
Tabela limpa com todos os trades do dia organizados.

**2. Análise de cada trade**
Para cada operação: o processo foi correto? A entrada fazia sentido? A saída foi bem conduzida? O que poderia ter sido diferente?

**3. Padrões identificados**
O que se repete — comportamentos, erros ou acertos que aparecem com frequência.

**4. Métricas do dia**
- Win rate do dia
- Resultado médio por trade
- Maior ganho e maior perda
- Relação risco/retorno

**5. Insight principal do dia**
A coisa mais importante que este dia de operação ensinou — em uma frase.

**6. Ajuste para amanhã**
Uma coisa concreta para fazer diferente ou manter na próxima sessão.
```

## Exemplo de uso

### Input
- Data: 14/04/2025
- Mercado: WIN — Mini Índice
- Condições: Mercado lateral de manhã, tendência de alta à tarde
- Trade 1: 10h15 / Comprado / Entrada 136.200 / Saída 136.050 / -150 pts / Entrei achando que ia romper a resistência / Stop atingido / Ansioso durante
- Trade 2: 11h30 / Vendido / Entrada 136.100 / Saída 135.900 / +200 pts / Setup de topo duplo / Alvo atingido / Confiante
- Trade 3: 14h20 / Comprado / Entrada 136.400 / Saída 136.250 / -150 pts / Entrei no impulso sem aguardar correção / Saída manual com medo / Arrependido
- Resultado total: -100 pts (aproximadamente -R$100 por contrato)
- Avaliação: Dia ruim emocionalmente — dois trades fora do plano
- Surpresa: A alta da tarde foi mais forte do que esperado

### Output
"PADRÃO IDENTIFICADO: Entradas antecipando rompimento sem confirmação
Trades 1 e 3 têm o mesmo padrão: você entrou antes do rompimento efetivo, esperando que aconteceria. No Trade 1, a resistência não foi rompida. No Trade 3, você entrou no impulso sem aguardar a correção que confirmaria a continuidade.

Este padrão provavelmente aparece quando o mercado está se movendo e você sente que vai 'perder o movimento'. A ansiedade de ficar de fora leva à entrada prematura.

Ajuste específico: Antes de qualquer entrada, perguntar: 'O sinal já se confirmou ou estou antecipando?' Se a resposta for 'estou antecipando' — aguardar."

---
**Tags:** Iniciante | Template | Financeiro, Jurídico & Compliance
