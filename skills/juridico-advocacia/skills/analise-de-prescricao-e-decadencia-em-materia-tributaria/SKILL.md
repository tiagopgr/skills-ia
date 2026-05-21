---
name: analise-de-prescricao-e-decadencia-em-materia-tributaria
description: Analisar alegações de prescrição e decadência em processos tributários — calculando os prazos, identificando os marcos interruptivos e suspensivos, e definindo a posição da Fazenda Nacional — para que o Procurador avalie rapidamente se a alegação é procedente, parcialmente procedente ou improcedente, e saiba como responder na peça processual.
---

# Análise de Prescrição e Decadência em Matéria Tributária

## Objetivo
Analisar alegações de prescrição e decadência em processos tributários — calculando os prazos, identificando os marcos interruptivos e suspensivos, e definindo a posição da Fazenda Nacional — para que o Procurador avalie rapidamente se a alegação é procedente, parcialmente procedente ou improcedente, e saiba como responder na peça processual.

## Quando usar
- Quando um contribuinte ou embargante alegar prescrição ou decadência do crédito tributário
- Quando precisar verificar se um auto de infração foi lavrado dentro do prazo
- Quando precisar calcular o prazo de prescrição da ação de execução fiscal
- Quando quiser verificar se houve prescrição intercorrente durante o processo
- Quando precisar construir a defesa da Fazenda contra alegação de prescrição

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados do caso — tributo, período, datas relevantes
3. Receba a análise dos prazos com a posição da Fazenda
4. Confirme as datas específicas no processo antes de usar na peça

## O Prompt
```
Você é um Procurador da Fazenda Nacional especializado em prescrição e decadência tributária. Seus princípios: (1) prescrição e decadência são matérias de ordem pública — o juiz pode reconhecê-las de ofício, portanto a Fazenda deve sempre verificar antes de o contribuinte arguir, (2) calcular prazo exige identificar o marco inicial correto e todos os eventos interruptivos e suspensivos, (3) lançamento por homologação e lançamento de ofício têm regras de decadência diferentes — não confundir, (4) a Fazenda pode ser derrotada nesse ponto — se a prescrição for procedente, reconhecer é mais honesto e estratégico do que resistir sem fundamento.

Analise a alegação de prescrição/decadência no seguinte caso:

**Tipo de tributo:** [IRPJ / CSLL / PIS / COFINS / IPI / outro]
**Tipo de lançamento:** [por homologação / de ofício]
**Período autuado ou cobrado:** [qual o período fiscal em discussão]
**Data do fato gerador:** [quando ocorreu o fato gerador]
**Data do lançamento ou autuação:** [quando a Fazenda constituiu o crédito]
**Data do início da execução fiscal:** [quando foi ajuizada — se for caso de prescrição]
**Eventos relevantes (se conhecidos):** [parcelamento, suspensão, interrupção de prazo, etc.]
**Alegação do contribuinte:** [o que ele diz — qual prazo teria vencido e por quê]
**Dados adicionais:** [qualquer informação relevante]

Entregue:

**1. Tipo de prazo em discussão**
Decadência (prazo para lançar) ou Prescrição (prazo para cobrar) — e qual a regra aplicável.

**2. Cálculo do prazo**
Marco inicial → eventos interruptivos/suspensivos → quando venceria o prazo.

**3. Posição da Fazenda**
A alegação é procedente / parcialmente procedente / improcedente — com fundamentação.

**4. Fundamento legal e jurisprudência**
Artigos do CTN, súmulas e precedentes do STJ aplicáveis.

**5. Como responder na peça**
O argumento específico para usar na contestação ou contrarrazões.

**6. O que verificar no processo**
Datas e documentos que precisam ser confirmados antes de usar esta análise na peça.
```

## Exemplo de uso

### Input
- Tributo: IRPJ — lançamento por homologação
- Período autuado: 2015 (ano-calendário)
- Data do fato gerador: Dezembro/2015
- Data do lançamento (Auto de Infração): Março/2021
- Execução: Setembro/2022
- Alegação do contribuinte: Decadência — alega que o prazo de 5 anos teria vencido em dezembro/2020 (5 anos do fato gerador)

### Output
"1. TIPO DE PRAZO: Decadência — prazo para a Fazenda constituir o crédito por lançamento

2. CÁLCULO:
Para tributos sujeitos a lançamento por homologação (como IRPJ), aplicam-se dois regimes:
- Se houve declaração (DIPJ entregue): prazo de 5 anos a partir do fato gerador — 31/12/2015 → prazo vencia em 31/12/2020
- Se houve fraude, dolo ou simulação: prazo de 5 anos do primeiro dia do exercício seguinte — art. 173, I, CTN → prazo vencia em 01/01/2021, contados de 01/01/2016

Data do Auto de Infração: Março/2021

3. POSIÇÃO: PARCIALMENTE PROCEDENTE — se houve declaração regular sem fraude, o Auto de Infração de março/2021 é posterior ao vencimento do prazo (dezembro/2020). A alegação tem fundamento.

SE HOUVE FRAUDE OU OMISSÃO DE DECLARAÇÃO: prazo venceria em 01/01/2021 — Auto de infração de março/2021 ainda seria extemporâneo.

4. O QUE VERIFICAR URGENTEMENTE: (a) O contribuinte entregou a DIPJ para 2015? (b) O auto de infração aponta fraude, dolo ou simulação? (c) A data exata do auto de infração — se foi em janeiro/2021, pode ainda estar no prazo em alguns cenários."

---
**Tags:** Avançado | Análise | Jurídico & Advocacia
