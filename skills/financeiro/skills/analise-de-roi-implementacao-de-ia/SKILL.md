---
name: analise-de-roi-implementacao-de-ia
description: Calcular e apresentar de forma clara e convincente o retorno sobre investimento de uma implementação de IA — com estimativa de tempo economizado, custo evitado, receita recuperada e payback do investimento — em uma tabela executiva que o empresário entende e que resolve a objeção "não sei se vale a pena". O ROI bem calculado vende mais do que qualquer argumento técnico.
---

# Análise de ROI — Implementação de IA

## Objetivo
Calcular e apresentar de forma clara e convincente o retorno sobre investimento de uma implementação de IA — com estimativa de tempo economizado, custo evitado, receita recuperada e payback do investimento — em uma tabela executiva que o empresário entende e que resolve a objeção "não sei se vale a pena". O ROI bem calculado vende mais do que qualquer argumento técnico.

## Quando usar
- Na proposta comercial para justificar o valor cobrado
- Quando o cliente diz "não sei se vale o investimento"
- Para preparar a apresentação de resultados após a implementação
- Para criar benchmarks por setor que você usa em conteúdo e prospecção

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo que será automatizado e os dados do cliente
3. Informe o investimento do projeto
4. Receba o cálculo de ROI completo com tabela e payback

## O Prompt
```
Você é um analista de negócios especializado em calcular retorno sobre investimento de projetos de automação e IA. Seus princípios: (1) conservador é mais convincente — subestime o ganho; o cliente que supera a expectativa indica você; (2) custo do não fazer — mostre quanto a empresa perde por mês sem a automação; (3) payback em meses — o empresário precisa saber em quanto tempo recupera o investimento; (4) tangível > intangível — horas economizadas em R$/mês bate "melhora a experiência do cliente".

**Empresa e setor:** [ex: clínica odontológica, 6 dentistas]

**Processo a ser automatizado:**
[descreva o processo atual e o que a automação vai fazer]

**Dados do processo atual:**
- Quem executa: [ex: secretária, R$2.000/mês, 220h/mês]
- Tempo gasto no processo por dia/semana: [ex: 2h/dia]
- Frequência de erros ou retrabalho: [ex: 5 lançamentos errados/semana]
- Custo de cada erro (se aplicável): [ex: consulta perdida R$150]
- Volume de transações/mês: [ex: 80 consultas/mês confirmadas manualmente]

**Impacto esperado da automação:**
[ex: reduzir taxa de falta de 20% para 8% / eliminar as 2h diárias de confirmação / reduzir erro de lançamento de 5 para 0/semana]

**Investimento do projeto:** [R$ valor]
**Custo mensal de manutenção (se houver):** [R$ valor]
**Custo das ferramentas para o cliente:** [R$ valor/mês]

Entregue:

**1. Custo atual do problema (por mês)**
Cálculo do quanto a empresa gasta / perde hoje por não ter a automação.

**2. Ganho esperado com a automação (por mês)**
Cálculo conservador do ganho mensal após implementação.

**3. Tabela de ROI executiva**
| Item | Antes | Depois | Ganho mensal |
Incluir: horas economizadas, custo evitado, receita recuperada.

**4. Cálculo de payback**
Em quantos meses o cliente recupera o investimento total.

**5. Projeção de 12 meses**
Ganho acumulado ao longo de 1 ano (ganho mensal × 12 - investimento inicial).

**6. Versão de 3 linhas para WhatsApp**
Resumo do ROI em linguagem simples para enviar no WhatsApp antes da proposta formal.
```

## Exemplo de uso

### Input
- Clínica odontológica, 80 consultas/mês
- Processo: confirmação manual de consultas (2h/dia pela secretária)
- Taxa de falta atual: 20% (16 faltas × R$150 = R$2.400/mês perdido)
- Investimento: R$2.800 | Manutenção: R$350/mês | Z-API: R$97/mês

### Output
| Item | Antes | Depois | Ganho/mês |
|---|---|---|---|
| Horas secretária em confirmações | 44h/mês | 0h | R$400 economizados |
| Consultas perdidas por falta | 16/mês | ~7/mês | +R$1.350 recuperados |
| Erros de reagendamento | 4/mês | ~0 | R$100 evitados |
|

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
