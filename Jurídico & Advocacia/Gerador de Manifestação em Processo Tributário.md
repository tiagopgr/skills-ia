---
name: gerador-de-manifestacao-em-processo-tributario
description: Gerar manifestações processuais rápidas para as situações mais recorrentes em processos tributários — impugnação de tutela de urgência, nota de expediente, informações em mandado de segurança, petições simples, requerimento de prazo — para que o Procurador produza peças curtas com agilidade sem precisar escrever do zero cada vez.
---

# Gerador de Manifestação em Processo Tributário

## Objetivo
Gerar manifestações processuais rápidas para as situações mais recorrentes em processos tributários — impugnação de tutela de urgência, nota de expediente, informações em mandado de segurança, petições simples, requerimento de prazo — para que o Procurador produza peças curtas com agilidade sem precisar escrever do zero cada vez.

## Quando usar
- Quando precisar impugnar urgentemente uma tutela de urgência deferida
- Quando precisar de uma nota de expediente ou informação simples
- Quando precisar pedir prazo, juntada de documento ou outra providência básica
- Quando receber intimação para se manifestar sobre algo específico e limitado
- Quando quiser um ponto de partida rápido para qualquer manifestação curta

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Escolha o tipo de manifestação e preencha com os dados do caso
3. Receba a peça pronta em minutos
4. Revise e protocole

## O Prompt
```
Você é um Procurador da Fazenda Nacional. Gere a seguinte manifestação processual de forma objetiva, técnica e sem prolixidade. Peça processual de qualidade não é peça longa — é peça precisa. Sempre incluir fundamento legal relevante. Sempre fechar com o pedido específico ao juízo.

**Tipo de manifestação:** [escolha: Impugnação à tutela de urgência / Nota de expediente / Informações em MS / Petição de juntada / Requerimento de prazo / Impugnação à gratuidade / Outra — descreva]

**Processo:** [número e tribunal]
**O que o juiz determinou ou o que o contribuinte requereu:** [o que motivou a manifestação]
**Minha posição:** [o que a Fazenda quer — negar o pedido, deferir, informar, etc.]
**Fundamento principal:** [o argumento central]
**Documentos a juntar (se houver):** [o que vai junto com a peça]
**Urgência:** [há prazo determinado? qual?]
**Dados adicionais:** [qualquer informação relevante para a peça]

Entregue:

**1. Peça processual completa**
Formatada com:
- Endereçamento
- Qualificação básica
- Exposição dos fatos
- Fundamento jurídico
- Pedido específico
- Fechamento

**2. Versão resumida (se aplicável)**
Quando a manifestação puder ser ainda mais concisa — versão de uma lauda ou menos.

**3. Alertas antes de protocolar**
O que verificar antes de assinar e protocolar — dados, datas, documentos.
```

## Exemplo de uso

### Input
- Tipo: Impugnação à tutela de urgência
- Processo: 5011234-56.2024.4.03.6100 — TRF3
- O que aconteceu: Juiz deferiu liminar suspendendo a exigibilidade de débito de CSLL de R$800.000 pendente em execução fiscal, com base em alegação de prescrição
- Minha posição: Impugnar — a prescrição não ocorreu, prazos foram interrompidos por parcelamento em 2019
- Fundamento: Parcelamento interrompe prescrição (art. 174, IV, CTN) — houve parcelamento REFIS em 2019 com exclusão em 2022
- Urgência: 3 dias para se manifestar

### Output
"EXCELENTÍSSIMO SENHOR DOUTOR JUIZ FEDERAL DA __ VARA DE EXECUÇÕES FISCAIS DA SEÇÃO JUDICIÁRIA DE SÃO PAULO

Processo nº 5011234-56.2024.4.03.6100

A FAZENDA NACIONAL, por seu Procurador infra-assinado, vem, respeitosamente, à presença de Vossa Excelência, tempestivamente, apresentar IMPUGNAÇÃO À DECISÃO QUE DEFERIU TUTELA DE URGÊNCIA, com fundamento no art. 300 e seguintes do CPC, pelas razões a seguir expostas.

I — DOS FATOS
Em [data], Vossa Excelência deferiu tutela de urgência suspendendo a exigibilidade do crédito tributário executado (CSLL, no valor de R$800.000,00), acolhendo a alegação de prescrição do executado.

II — DO ERRO NO RECONHECIMENTO DA PRESCRIÇÃO
A decisão merece reforma. O executado aderiu ao programa de parcelamento REFIS em [data de 2019], fato este que interrompeu o prazo prescricional nos termos do art. 174, parágrafo único, inciso IV, do CTN.

A exclusão do parcelamento ocorreu em [data de 2022], reiniciando o prazo prescricional a partir desta data. Portanto, quando do ajuizamento da execução fiscal, o prazo prescricional de 5 anos ainda não havia transcorrido integralmente.

III — DO PEDIDO
Requer a Fazenda Nacional a reconsideração da decisão que deferiu a tutela de urgência, determinando-se o prosseguimento normal da execução fiscal.

[Local], [data].
[Nome do Procurador] — PFN"

---
**Tags:** Avançado | Template | Jurídico & Advocacia
