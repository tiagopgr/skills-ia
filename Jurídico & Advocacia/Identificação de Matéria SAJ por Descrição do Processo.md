---
name: identificacao-de-materia-saj-por-descricao-do-processo
description: Identificar a matéria SAJ (Sistema de Automação da Justiça) correta de um processo judicial a partir da descrição do assunto, ementa ou dados disponíveis na planilha — para que o Procurador classifique cada processo com precisão, organize o acervo corretamente e tenha a informação de matéria pronta antes de acessar o sistema.
---

# Identificação de Matéria SAJ por Descrição do Processo

## Objetivo
Identificar a matéria SAJ (Sistema de Automação da Justiça) correta de um processo judicial a partir da descrição do assunto, ementa ou dados disponíveis na planilha — para que o Procurador classifique cada processo com precisão, organize o acervo corretamente e tenha a informação de matéria pronta antes de acessar o sistema.

## Quando usar
- Quando a matéria SAJ de um processo não está clara na planilha
- Quando precisar classificar um lote de processos novos recebidos
- Quando quiser confirmar se a classificação SAJ de um processo está correta
- Quando um processo tiver assunto ambíguo e precisar de orientação de classificação
- Quando estiver organizando o acervo e precisar padronizar as matérias

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo — assunto, partes, pedido, fase — como constar na planilha
3. Receba a matéria SAJ identificada com justificativa e nível de confiança
4. Confirme no sistema após acessar o processo completo

## O Prompt
```
Você é um especialista em classificação processual para a Procuradoria da Fazenda Nacional, com profundo conhecimento das matérias SAJ utilizadas no contencioso fiscal federal e no TRF3. Seus princípios: (1) classificação SAJ precisa ser precisa — matéria errada dificulta estatísticas, gestão do acervo e pesquisa de precedentes, (2) quando houver ambiguidade, indicar a matéria principal e a alternativa mais provável com justificativa, (3) nível de confiança deve ser explícito — "alta confiança" quando os dados são claros, "verificar" quando a descrição é insuficiente, (4) sempre indicar quais informações adicionais confirmariam ou alterariam a classificação.

Identifique a matéria SAJ do seguinte processo:

**Dados disponíveis sobre o processo:**
- Número: [número do processo]
- Partes: [quem é o autor e quem é o réu]
- Assunto/Ementa: [descrição do assunto conforme a planilha]
- Pedido (se disponível): [o que o autor pede]
- Fase processual: [inicial, instrução, sentença, recurso, execução]
- Tribunal/Vara: [onde tramita]
- Tipo de ação (se identificável): [mandado de segurança, ação ordinária, embargos, etc.]

**Arquivo de matérias SAJ para referência:** [Se você tem o arquivo de matérias SAJ, cole aqui as matérias relevantes ou o conteúdo completo do arquivo para que eu use como referência exata]

Entregue:

**1. Matéria SAJ identificada**
A classificação mais provável com o código e descrição exata conforme o arquivo de matérias.

**2. Nível de confiança**
✅ Alta confiança — dados suficientes para classificação segura
⚠️ Confiança média — classificação provável, verificar ao acessar o processo
❓ Baixa confiança — dados insuficientes, verificar obrigatoriamente

**3. Matéria alternativa (se aplicável)**
Segunda opção de classificação caso a descrição seja ambígua — com explicação de quando se aplica uma ou outra.

**4. Justificativa da classificação**
Por que esta matéria foi escolhida — quais elementos do processo levaram a essa conclusão.

**5. O que confirmar ao acessar o processo**
Informações específicas que vão confirmar ou alterar a classificação sugerida.
```

## Exemplo de uso

### Input
- Número: 5008765-99.2023.4.03.6100
- Partes: Supermercado Bom Preço Ltda x União Federal
- Assunto: "Tributário — PIS/COFINS — creditamento — insumos"
- Pedido: Reconhecimento do direito ao aproveitamento de créditos de PIS/COFINS sobre insumos utilizados na atividade econômica
- Fase: Inicial — aguardando contestação
- Tribunal: TRF3 — 5ª Vara Federal de SP
- Tipo: Ação ordinária declaratória + repetição de indébito

### Output
"1. MATÉRIA SAJ IDENTIFICADA: PIS/COFINS — Creditamento — Insumos

2. CONFIANÇA: ✅ Alta confiança — assunto, pedido e tipo de ação são coerentes e específicos

3. MATÉRIA ALTERNATIVA: PIS/COFINS — Regime Não-Cumulativo (caso o foco seja a discussão sobre o regime aplicável e não apenas o creditamento de insumos específicos)

4. JUSTIFICATIVA: O processo discute o direito ao crédito de PIS/COFINS sobre insumos — matéria definida pelo STJ no REsp 1.221.170 (Tema 779). A combinação de ação declaratória + repetição de indébito é o padrão para esse tipo de discussão. A vara (5ª Federal de SP) é compatível com esse tipo de demanda.

5. CONFIRMAR AO ACESSAR: (a) Qual o conceito de insumo que o contribuinte defende; (b) Se há pedido de tutela antecipada; (c) Período de apuração e valor em discussão; (d) Se já há sentença do STJ aplicável ao caso concreto."

---
**Tags:** Avançado | Análise | Jurídico & Advocacia
