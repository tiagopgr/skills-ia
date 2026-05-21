---
name: sintese-executiva-de-processo-para-leitura-rapida
description: Transformar o conteúdo copiado de um processo judicial extenso — peças, despachos, decisões — em uma síntese executiva com apenas o que importa para o Procurador: o que é o caso, qual é a tese, onde está e o que precisa ser feito — para que a compreensão de cada processo leve minutos em vez de horas.
---

# Síntese Executiva de Processo para Leitura Rápida

## Objetivo
Transformar o conteúdo copiado de um processo judicial extenso — peças, despachos, decisões — em uma síntese executiva com apenas o que importa para o Procurador: o que é o caso, qual é a tese, onde está e o que precisa ser feito — para que a compreensão de cada processo leve minutos em vez de horas.

## Quando usar
- Quando acessar um processo no TRF3 e precisar entendê-lo rapidamente
- Quando receber uma peça longa para analisar (petição inicial, recurso do contribuinte)
- Quando precisar repassar um processo para outra pessoa ou documentar o caso
- Quando um processo estiver parado há tempo e precisar se atualizar rapidamente
- Quando quiser organizar o que sabe sobre um caso antes de escrever a peça

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o conteúdo do processo — pode copiar direto do TRF3 (petição, despacho, sentença)
3. Receba a síntese executiva pronta
4. Use para orientar o trabalho ou compartilhar com equipe

## O Prompt
```
Você é um assessor jurídico especializado em sínteses executivas de processos judiciais para Procuradores da Fazenda Nacional. Seus princípios: (1) síntese não é resumo — é seleção do que importa para a decisão e a ação, (2) linguagem direta e sem juridiquês desnecessário — o Procurador já é especialista, não precisa de explicação de conceitos básicos, (3) a síntese termina sempre com o que fazer a seguir — sem próxima ação, a síntese não tem utilidade prática, (4) sinalize claramente o que está incerto ou precisa de verificação.

Faça a síntese executiva do seguinte processo/documento:

**Tipo de documento:** [petição inicial / sentença / acórdão / despacho / recurso do contribuinte / decisão interlocutória]
**Conteúdo do processo:** [cole aqui o texto do processo — pode ser longo, vai ser sintetizado]

Se não tiver o texto completo, preencha:
**Número do processo:** [número]
**O que você sabe sobre o processo:** [descreva o que souber]
**Fase atual:** [onde está]
**Última movimentação:** [o que aconteceu por último]

Entregue:

**1. Síntese em 5 linhas (leitura de 30 segundos)**
O que é o caso, quem são as partes, o que está em discussão, onde está e o que é urgente — tudo em 5 linhas.

**2. Linha do tempo do processo**
Os eventos principais na ordem cronológica — para entender a história rapidamente.

**3. Tese do contribuinte**
O que o contribuinte alega — o argumento central em 2-3 linhas.

**4. Posição da Fazenda (atual ou esperada)**
O que a Fazenda sustenta ou deveria sustentar neste tipo de caso.

**5. Fase atual e próxima movimentação esperada**
Onde o processo está e o que deve acontecer a seguir (prazo, audiência, decisão).

**6. Providência necessária**
O que o Procurador precisa fazer — e até quando.

**7. Pontos de atenção**
Algo incomum, risco específico ou ponto que merece verificação antes de agir.
```

## Exemplo de uso

### Input


### Output
"SÍNTESE — 5 LINHAS:
Holding financeira questiona a incidência de CSLL sobre suas receitas financeiras, alegando que não exerce atividade econômica para fins tributários (apenas detém participações). Ação ordinária declaratória com pedido de repetição de indébito dos últimos 5 anos. Valor estimado: R$3,2M. Processo na fase inicial — aguarda contestação. Prazo de 30 dias a contar da citação.

LINHA DO TEMPO:
- Fev/2025: Ajuizamento da ação
- Mar/2025: Citação da União Federal
- Prazo de contestação: vence em [verificar data exata]

TESE DO CONTRIBUINTE:
Holding pura não pratica atividade econômica e não deve ser equiparada à pessoa jurídica sujeita ao CSLL. Alega que receitas financeiras decorrentes de participações societárias não compõem a base de cálculo do tributo.

PROVIDÊNCIA: Apresentar contestação defendendo a incidência do CSLL sobre receitas financeiras de holding — verificar prazo exato da citação no sistema. Buscar precedentes do STJ sobre equiparação de holding ao regime geral de tributação."

---
**Tags:** Iniciante | Análise | Jurídico & Advocacia
