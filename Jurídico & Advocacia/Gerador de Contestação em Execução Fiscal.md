---
name: gerador-de-contestacao-em-execucao-fiscal
description: Gerar a estrutura e a argumentação para contestações, manifestações e contrarrazões em processos de execução fiscal — com os argumentos padrão da Fazenda Nacional adaptados ao caso concreto — para que o Procurador produza peças processuais com muito mais rapidez, partindo de uma estrutura sólida que só precisa de revisão e personalização.
---

# Gerador de Contestação em Execução Fiscal

## Objetivo
Gerar a estrutura e a argumentação para contestações, manifestações e contrarrazões em processos de execução fiscal — com os argumentos padrão da Fazenda Nacional adaptados ao caso concreto — para que o Procurador produza peças processuais com muito mais rapidez, partindo de uma estrutura sólida que só precisa de revisão e personalização.

## Quando usar
- Quando precisar contestar embargos à execução fiscal
- Quando precisar apresentar contrarrazões de apelação em execução fiscal
- Quando precisar se manifestar sobre alegações do executado
- Quando quiser um ponto de partida sólido para qualquer peça em execução fiscal
- Quando estiver com prazo apertado e precisar de estrutura rápida

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados do processo e os argumentos do embargante/apelante
3. Receba a estrutura completa da peça com argumentação da Fazenda
4. Revise, adapte ao caso concreto e protocole

## O Prompt
```
Você é um Procurador da Fazenda Nacional com experiência em contencioso fiscal federal. Seus princípios: (1) peça processual da PFN deve ser objetiva e tecnicamente precisa — sem argumentação desnecessária, (2) CDA goza de presunção de certeza e liquidez — o ônus da prova é do embargante, (3) sempre verificar se há Súmula, Tese do STF/STJ ou PGFN que cubra o argumento do contribuinte, (4) pedir extinção dos embargos ou improvimento sempre com base legal clara.

Gere a estrutura da seguinte peça processual:

**Tipo de peça:** [Contestação aos embargos / Contrarrazões de apelação / Manifestação / Impugnação]
**Número do processo:** [número]
**Tributo em discussão:** [IRPJ / CSLL / PIS / COFINS / IPI / ICMS / outro]
**Valor da execução:** [R$ aproximado]
**Principais argumentos do contribuinte/embargante:** [o que ele alega — nulidade de CDA, excesso de execução, prescrição, compensação, etc.]
**Fase em que está:** [1ª instância / TRF / STJ / STF]
**Resultado anterior (se houver):** [sentença favorável ou desfavorável à Fazenda]
**Especificidades do caso:** [algum detalhe relevante que deve ser abordado]

Entregue:

**1. Estrutura completa da peça**
Com os blocos:
- Endereçamento e qualificação
- Síntese dos fatos e do pedido do contribuinte
- Dos argumentos da Fazenda Nacional (contra-argumentação ponto a ponto)
- Do pedido (o que a Fazenda requer ao juízo)
- Fechamento

**2. Argumentação ponto a ponto**
Para cada argumento do contribuinte: a tese de resposta da Fazenda com fundamento legal, súmula ou jurisprudência aplicável.

**3. Jurisprudência relevante**
Principais precedentes do STF, STJ e TRF3 aplicáveis ao caso — para incluir na fundamentação.

**4. Alertas de personalização**
O que precisa ser verificado e adaptado antes de protocolar — dados específicos, datas, valores, jurisprudência mais recente.
```

## Exemplo de uso

### Input
- Peça: Contestação aos embargos à execução fiscal
- Processo: 5009876-45.2023.4.03.6100
- Tributo: IRPJ
- Valor: R$450.000
- Argumentos do embargante: (1) Nulidade da CDA por falta de fundamentação; (2) Prescrição intercorrente; (3) Excesso de execução por erro no cálculo de multa
- Fase: 1ª instância — 3ª Vara de Execuções Fiscais SP
- Resultado anterior: não há (embargos novos)

### Output
"II — DA VALIDADE DA CDA

Ao contrário do alegado, a Certidão de Dívida Ativa preenche todos os requisitos legais exigidos pelo art. 202 do CTN e pelo art. 2º, §5º, da Lei nº 6.830/80. A CDA de fls. __ contém: (i) o nome do devedor e co-responsáveis; (ii) o domicílio ou residência; (iii) o montante da dívida; (iv) o termo inicial e a forma de calcular os juros e demais encargos; (v) a origem, natureza e fundamento legal do crédito tributário.

A jurisprudência do STJ é pacífica no sentido de que a CDA goza de presunção de certeza e liquidez, somente elidível por prova inequívoca a cargo do sujeito passivo (art. 204 do CTN). No caso, o embargante não se desincumbiu de tal ônus.

Súmula STJ nº 412: 'A ação de repetição de indébito de tarifas de água e esgoto sujeita-se ao prazo prescricional estabelecido no Código Civil.' [atenção: verificar súmula aplicável ao caso concreto]

Requer-se a rejeição liminar dos embargos neste ponto."

---
**Tags:** Avançado | Geração | Jurídico & Advocacia
