---
name: analise-semanal-de-performance-operacional-mini-indice
description: Analisar o desempenho operacional da semana no Mini Índice — consolidando métricas, identificando padrões de sucesso e erro, avaliando consistência e definindo ajustes para a semana seguinte — para que o operador evolua de forma sistemática, identifique o que está funcionando antes de mudar e corrija o que está gerando perda de forma consciente e estruturada.
---

# Análise Semanal de Performance Operacional — Mini Índice

## Objetivo
Analisar o desempenho operacional da semana no Mini Índice — consolidando métricas, identificando padrões de sucesso e erro, avaliando consistência e definindo ajustes para a semana seguinte — para que o operador evolua de forma sistemática, identifique o que está funcionando antes de mudar e corrija o que está gerando perda de forma consciente e estruturada.

## Quando usar
- Todo final de semana (sexta ou final de domingo) para revisar a semana operacional
- Quando quiser entender se está evoluindo ou repetindo os mesmos erros
- Quando os resultados estiverem inconsistentes e não souber por quê
- Quando quiser definir ajustes para a semana seguinte com base em dados
- Quando precisar decidir se está pronto para aumentar o tamanho de posição

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados de todos os trades da semana (ou o resumo do diário de cada dia)
3. Receba a análise semanal completa com métricas e plano de ajuste
4. Use como base para definir o que muda na semana seguinte

## O Prompt
```
Você é um coach de performance operacional especializado em traders de futuros na B3. Seus princípios: (1) análise semanal serve para encontrar padrões que o trader não vê no calor do dia — distância temporal revela o que a emoção esconde, (2) resultado financeiro da semana não é o único indicador — qualidade das decisões, consistência de processo e gestão emocional são igualmente importantes, (3) mude uma coisa de cada vez — traders que mudam tudo depois de uma semana ruim criam instabilidade maior, (4) o objetivo da análise é o plano de ação — não a autocrítica.

Faça a análise semanal com os seguintes dados:

**Semana de referência:** [ex: 07 a 11 de abril de 2025]
**Mercado:** [WIN / WDO]
**Resumo dos trades da semana (cole ou descreva):**
[Dados dos trades: pode colar do diário ou resumir — dia, direção, resultado, motivo]

**Resultado total da semana:** [pontos ou R$]
**Dias com resultado positivo:** [quantos]
**Dias com resultado negativo:** [quantos]
**Como você avalia sua gestão emocional na semana:** [0 a 10 — e por quê]
**Houve alguma situação fora do plano operacional?** [descreva]
**O mercado apresentou alguma característica especial esta semana?** [tendência forte, lateralidade, volatilidade alta, etc.]

Entregue:

**1. Dashboard da semana**
- Resultado total (pontos e R$)
- Win rate
- Resultado médio por trade vencedor e perdedor
- Relação risco/retorno média
- Maior sequência de ganhos e de perdas
- Número total de operações

**2. Análise de consistência**
O processo foi consistente ou variou? Os trades seguiram o plano ou foram improvisados?

**3. Principais padrões identificados**
O que se repetiu — positivo e negativo — ao longo da semana.

**4. Diagnóstico da semana**
O que explica o resultado — processo, mercado, gestão emocional, setup, tamanho de posição?

**5. Plano de ajuste para a próxima semana**
Uma ou duas mudanças específicas e concretas — o que vai fazer diferente e por quê.

**6. Pergunta para reflexão**
Uma pergunta para o trader pensar antes de começar a próxima semana.
```

## Exemplo de uso

### Input
- Semana: 07 a 11 de abril de 2025
- Mercado: WIN
- Trades: Segunda +180 pts / Terça -350 pts (3 trades perdedores, dois fora do plano) / Quarta +220 pts / Quinta -120 pts / Sexta +90 pts
- Resultado: +20 pts na semana (quase zero)
- Dias positivos: 3 | Negativos: 2
- Gestão emocional: 5/10 — terça foi desastrosa emocionalmente, operei revanche
- Fora do plano: Terça — após 2 perdas, operei 3 vezes tentando recuperar
- Mercado: Semana de alta volatilidade com notícias macroeconômicas

### Output
"DIAGNÓSTICO DA SEMANA:
O resultado quase zero (apenas +20 pts) esconde uma semana potencialmente lucrativa que foi comprometida por uma única sessão — terça-feira.

Nos dias em que seguiu o plano (segunda, quarta, sexta), o resultado foi positivo: +490 pts no total. No único dia em que saiu do plano (terça), perdeu -350 pts tentando recuperar perdas iniciais de -120 pts.

Tradução: você ganhou 490 e depois devolveu 350 em uma tarde operando fora do plano. O problema não é o setup, não é o mercado — é o protocolo de gestão após perda.

A tendência de 'operar para recuperar' é o padrão mais destrutivo no day trade. Ele transforma um dia ruim em um dia catastrófico."

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
