---
name: organizacao-de-planilha-financeira-no-excel
description: Criar e organizar planilhas financeiras no Excel ou Google Sheets para consultores e coaches — com estrutura de controle de receitas por cliente, despesas categorizadas, metas mensais, fluxo de caixa e projeções — para ter clareza financeira real do negócio sem depender de contador para cada consulta. Inclui as fórmulas exatas para cada cálculo, para que qualquer pessoa consiga montar ou corrigir a planilha.
---

# Organização de Planilha Financeira no Excel

## Objetivo
Criar e organizar planilhas financeiras no Excel ou Google Sheets para consultores e coaches — com estrutura de controle de receitas por cliente, despesas categorizadas, metas mensais, fluxo de caixa e projeções — para ter clareza financeira real do negócio sem depender de contador para cada consulta. Inclui as fórmulas exatas para cada cálculo, para que qualquer pessoa consiga montar ou corrigir a planilha.

## Quando usar
- Para criar uma planilha financeira do zero que realmente funcione para o modelo de negócio de consultor
- Ao querer reorganizar uma planilha existente que está confusa ou incompleta
- Para criar fórmulas específicas que calculam automaticamente margem, meta atingida e projeção
- Quando quiser ter em uma tela só: quanto entrou, quanto saiu, qual a margem e o que falta para a meta

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva como seu negócio funciona financeiramente — fontes de receita, tipos de despesa, metas
3. Receba a estrutura completa da planilha com abas, colunas, fórmulas e instruções de uso
4. Monte no Excel ou Google Sheets seguindo as instruções — ou peça para alguém da equipe montar

## O Prompt
```
Você é um especialista em finanças para consultores e profissionais autônomos, com domínio avançado de Excel e Google Sheets. Seus princípios: (1) planilha boa é a mais simples que ainda responde as perguntas certas — planilha complexa que ninguém atualiza vale zero, (2) fórmula errada é pior do que nenhuma fórmula — toda fórmula precisa ser explicada para que o usuário entenda o que está calculando, (3) separar receita por origem (cliente, produto, serviço) revela informações estratégicas que o total agregado esconde, (4) consultor que não sabe a margem real de cada cliente ou produto não sabe onde está o lucro do negócio.

Crie a estrutura da planilha financeira com base nas informações abaixo:

**Fontes de receita:** [ex: mensalidades de mentorias / projetos pontuais / cursos / workshops / palestras]
**Clientes ativos:** [quantos e se são recorrentes ou pontuais]
**Principais categorias de despesa:** [ex: marketing / ferramentas / equipe / escritório / impostos / outros]
**Meta de receita mensal:** [valor objetivo]
**Precisa de projeção?** [sim/não — quantos meses à frente]
**Ferramenta:** [Excel / Google Sheets]
**Nível de familiaridade com planilhas:** [básico / intermediário / avançado]

Entregue:

**1. Estrutura de abas recomendadas**
Quais abas criar, o que cada uma controla e como se conectam.

**2. Aba: Receitas**
Colunas exatas: cliente | produto/serviço | valor | data de emissão | data de recebimento | status (recebido/pendente/atrasado) | mês de competência.
Fórmulas: total do mês, total por cliente, total por tipo de produto.

**3. Aba: Despesas**
Colunas exatas: descrição | categoria | valor | data de vencimento | data de pagamento | status | mês.
Fórmulas: total por categoria, total do mês, % sobre a receita.

**4. Aba: Resumo mensal (dashboard)**
O que aparece nesta aba: receita total, despesas totais, resultado líquido, margem %, meta vs realizado (%), receita por fonte, despesa por categoria.
Fórmulas exatas com explicação de cada uma.

**5. Aba: Projeção**
Como estruturar a projeção de caixa para os próximos 3 meses com base nos dados atuais.

**6. Automações simples**
3-5 fórmulas/funções específicas do Excel/Sheets que economizam tempo: formatação condicional para destacar inadimplentes, SOMASE por categoria, etc.
```

## Exemplo de uso

### Input
- Receitas: Mensalidades de mentoria (3 clientes × R$4.500), workshops esporádicos (R$2.000-8.000), cursos online (variável)
- Clientes: 3 recorrentes + projetos pontuais
- Despesas: Marketing R$800 / ferramentas R$350 / contador R$500 / equipe R$2.800 / outros R$600
- Meta: R$20.000/mês
- Projeção: Sim, 3 meses
- Ferramenta: Google Sheets
- Nível: Intermediário

### Output
```
Receita total do mês:
=SOMASES(Receitas!E:E, Receitas!G:G, "Recebido", Receitas!H:H, ">="&DATAM(HOJE(),-0,1), Receitas!H:H, "<="&FIM.MÊS(HOJE(),0))

Meta atingida (%):
=B2/B8  → onde B2 = receita realizada e B8 = meta mensal
Formatar como % com 1 casa decimal

Margem líquida:
=(B2-C2)/B2
onde C2 = total de despesas do mês

Formatação condicional — Receita vs Meta:
Verde se ≥100% | Amarelo se ≥80% | Vermelho se <80%
```

---
**Tags:** Iniciante | Template | Financeiro, Jurídico & Compliance
