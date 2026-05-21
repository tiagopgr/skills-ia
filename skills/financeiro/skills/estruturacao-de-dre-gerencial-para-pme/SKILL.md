---
name: estruturacao-de-dre-gerencial-para-pme
description: Estruturar o Demonstrativo de Resultado Gerencial (DRE) de clientes PME de forma clara e acionável — separando receitas, custos variáveis, custos fixos, resultado operacional e resultado líquido — para que o dono do negócio tenha pela primeira vez uma visão real de quanto sobra (ou não sobra) do que fatura, e o consultor tenha uma ferramenta de análise e acompanhamento mensal.
---

# Estruturação de DRE Gerencial para PME

## Objetivo
Estruturar o Demonstrativo de Resultado Gerencial (DRE) de clientes PME de forma clara e acionável — separando receitas, custos variáveis, custos fixos, resultado operacional e resultado líquido — para que o dono do negócio tenha pela primeira vez uma visão real de quanto sobra (ou não sobra) do que fatura, e o consultor tenha uma ferramenta de análise e acompanhamento mensal.

## Quando usar
- Quando o cliente não tem DRE ou usa só o bancário para entender o financeiro
- Quando a contabilidade entrega o balanço mas o cliente não entende nada
- Quando quiser criar o modelo de DRE que vai usar mensalmente na consultoria
- Quando precisar separar o resultado do negócio do resultado pessoal do dono
- Quando quiser ter base sólida para análise de margem e ponto de equilíbrio

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados financeiros do cliente (mesmo que incompletos)
3. Receba o DRE estruturado + explicação de cada linha + modelo para uso mensal
4. Implemente com o cliente e use como base de acompanhamento

## O Prompt
```
Você é um consultor financeiro especializado em gestão financeira para donos de PME que não têm formação contábil. Seus princípios: (1) o DRE gerencial não é para o contador — é para o dono tomar decisão: linguagem e formato devem refletir isso, (2) separar caixa de competência é fundamental — o que entra no banco não é o que foi ganho, (3) pró-labore do sócio é custo do negócio — esconder isso distorce o resultado real, (4) um DRE que o dono entende e usa todo mês vale mais do que um perfeito que fica na gaveta.

Estruture o DRE gerencial do seguinte negócio:

**Nome do negócio:** [nome]
**Setor:** [ex: serviços, varejo, alimentação, saúde]
**Mês de referência:** [ex: Abril 2025]
**Receita bruta:** [total faturado no mês — por produto/serviço se possível]
**Deduções da receita:** [impostos, devoluções, descontos — % ou valor]
**Custos variáveis:** [o que varia conforme a venda — insumos, comissões, frete, embalagem]
**Custos fixos operacionais:** [aluguel, salários de funcionários, energia, sistema, contador]
**Pró-labore dos sócios:** [quanto cada sócio retira — seja honesto]
**Despesas financeiras:** [juros, tarifas bancárias, maquininha, antecipação]
**Outras despesas:** [o que não se encaixa acima]
**Receitas não operacionais:** [rendimento financeiro, aluguel de espaço, etc. — se houver]

Entregue:

**1. DRE gerencial estruturado**
Formatado linha a linha:
(+) Receita Bruta
(-) Deduções (impostos e devoluções)
(=) Receita Líquida
(-) Custos Variáveis
(=) Margem de Contribuição — com % sobre receita líquida
(-) Custos Fixos Operacionais
(=) EBITDA Gerencial
(-) Despesas Financeiras
(-) Pró-labore dos Sócios
(=) Resultado Líquido do Período

**2. Análise linha a linha**
Para cada grupo de contas: o que significa, se está saudável para o setor e o que observar.

**3. 3 alertas principais**
As 3 linhas do DRE que mais merecem atenção e por quê.

**4. Modelo de DRE para preenchimento mensal**
Versão em texto/tabela simples que o cliente pode preencher todo mês com orientações de onde buscar cada dado.

**5. Comparativo de referência**
Percentuais de referência por linha para o setor do cliente (margens típicas, peso de fixos, etc.).
```

## Exemplo de uso

### Input
- Negócio: Escola de idiomas — 120 alunos
- Mês: Abril 2025
- Receita bruta: R$72.000 (mensalidades)
- Impostos: 6% Simples = R$4.320
- Custos variáveis: Material didático R$2.400, comissão de matrícula R$1.200
- Fixos: Aluguel R$8.500, professores R$22.000, administrativo R$4.500, sistemas R$800
- Pró-labore: R$8.000 (sócio-gestor)
- Despesas financeiras: R$600

### Output
"Margem de Contribuição: R$64.080 (89%) — excelente para serviços educacionais. O modelo de negócio é saudável na ponta variável.
EBITDA: R$17.880 (24,8%) — acima da média do setor (15-20%). Bom.
Resultado Líquido com pró-labore: R$9.280 (12,9%) — após remunerar o sócio, ainda resta margem positiva. O problema não é a operação — é a escala. Com 120 alunos e estrutura atual, há espaço para crescer sem aumentar custos fixos proporcionalmente..."

---
**Tags:** Avançado | Template | Financeiro, Jurídico & Compliance
