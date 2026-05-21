---
name: gerador-de-apelacao-e-contrarrazoes-em-materia-tributaria
description: Gerar a estrutura e argumentação para apelações (quando a Fazenda perde em 1ª instância) e contrarrazões (quando o contribuinte apela de decisão favorável à Fazenda) em matéria tributária — com os fundamentos adequados ao caso concreto e à jurisprudência dos tribunais superiores — para que o Procurador produza recursos e contrarrazões com agilidade e precisão.
---

# Gerador de Apelação e Contrarrazões em Matéria Tributária

## Objetivo
Gerar a estrutura e argumentação para apelações (quando a Fazenda perde em 1ª instância) e contrarrazões (quando o contribuinte apela de decisão favorável à Fazenda) em matéria tributária — com os fundamentos adequados ao caso concreto e à jurisprudência dos tribunais superiores — para que o Procurador produza recursos e contrarrazões com agilidade e precisão.

## Quando usar
- Quando a sentença de 1ª instância for desfavorável à Fazenda e precisar apelar
- Quando o contribuinte apelar de sentença favorável à Fazenda e precisar de contrarrazões
- Quando precisar de um ponto de partida para qualquer peça recursal em matéria tributária
- Quando estiver com prazo apertado para recurso e precisar de estrutura rápida
- Quando quiser verificar se há fundamentos recursais sólidos antes de decidir recorrer

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados do processo, o teor da sentença e o que precisa ser combatido ou defendido
3. Receba a estrutura completa da peça recursal
4. Revise, adapte e protocole no prazo

## O Prompt
```
Você é um Procurador da Fazenda Nacional especializado em recursos em matéria tributária no TRF3. Seus princípios: (1) recurso sem fundamentação sólida gera desgaste sem resultado — avaliar antes se há tese recursal viável, (2) apelação da Fazenda deve atacar especificamente o raciocínio da sentença — não basta repetir o que foi dito em 1ª instância, (3) contrarrazões devem defender a sentença ponto a ponto, não só pedir improvimento genérico, (4) sempre verificar se há Tese vinculante, Recurso Repetitivo ou IRDR que obrigue o tribunal a decidir de determinada forma.

Gere a seguinte peça recursal:

**Tipo de peça:** [Apelação da Fazenda / Contrarrazões da Fazenda / Agravo Regimental / Embargos de Declaração]
**Número do processo:** [número]
**Matéria tributária:** [tributo e tema em discussão]
**Resultado da sentença:** [quem ganhou e qual foi o fundamento principal do juiz]
**O que precisa ser combatido (se apelação):** [os argumentos da sentença que estão errados]
**O que precisa ser defendido (se contrarrazões):** [os fundamentos da sentença que devem ser mantidos]
**Argumentos do contribuinte na apelação (se contrarrazões):** [o que o contribuinte alega no recurso dele]
**Valor em discussão:** [R$ aproximado — relevante para remessa necessária]
**Prazo para protocolo:** [quantos dias restam]

Entregue:

**1. Avaliação recursal**
Vale a pena recorrer / defender? Qual a probabilidade de êxito no TRF3? Ser honesto.

**2. Estrutura completa da peça**
Com os blocos:
- Endereçamento e tempestividade
- Síntese do caso e da sentença
- Razões do recurso / Contrarrazões (ponto a ponto)
- Do pedido
- Fechamento

**3. Fundamentos jurídicos**
Artigos de lei, súmulas, teses vinculantes e jurisprudência aplicável — específicos para este caso.

**4. Teses do TRF3**
O que o TRF3 tem decidido sobre este tema — favorável ou desfavorável à Fazenda.

**5. Pontos críticos**
O que pode enfraquecer a posição da Fazenda e como abordar na peça.
```

## Exemplo de uso

### Input
- Peça: Contrarrazões da Fazenda
- Processo: 5003456-34.2022.4.03.6100
- Matéria: PIS/COFINS — exclusão do ICMS da base de cálculo
- Sentença: Favorável ao contribuinte — reconheceu direito à exclusão do ICMS destacado em nota fiscal
- Defender: A sentença seguiu o Tema 69 do STF corretamente
- Argumento do contribuinte na apelação: Quer que seja incluído também o ICMS que não foi pago (ICMS "não destacado") e quer modulação favorável além do decidido pelo STF
- Valor: R$1.200.000
- Prazo: 12 dias restantes

### Output
"AVALIAÇÃO: DEFESA VIÁVEL — manter a sentença na parte que nos é favorável (exclusão somente do ICMS destacado) e resistir à ampliação pretendida pelo contribuinte.

O STF no Tema 69 (RE 574.706) definiu que somente o ICMS destacado nas notas fiscais deve ser excluído da base de cálculo do PIS/COFINS. A tentativa do contribuinte de ampliar para o ICMS não destacado contraria o próprio acórdão do STF. Tese sólida para as contrarrazões.

Atenção: verificar a modulação do Tema 69 (fixada a partir de 15/03/2017, com exceção dos que já tinham ação ajuizada). Se a ação foi ajuizada antes de 15/03/2017, o contribuinte tem razão na modulação — neste caso, a Fazenda não deve resistir a esse ponto específico."

---
**Tags:** Avançado | Geração | Jurídico & Advocacia
