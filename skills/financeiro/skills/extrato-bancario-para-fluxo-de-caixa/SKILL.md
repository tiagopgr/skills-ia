---
name: extrato-bancario-para-fluxo-de-caixa
description: Transformar o extrato bancário bruto — cheio de descrições crípticas, lançamentos misturados e sem categorização — em um demonstrativo de fluxo de caixa organizado por categorias, com entradas, saídas, saldo operacional e variação do período. A skill lê o extrato colado em texto e entrega um relatório financeiro estruturado, pronto para apresentar ao cliente ou usar internamente.
---

# Extrato Bancário para Fluxo de Caixa

## Objetivo
Transformar o extrato bancário bruto — cheio de descrições crípticas, lançamentos misturados e sem categorização — em um demonstrativo de fluxo de caixa organizado por categorias, com entradas, saídas, saldo operacional e variação do período. A skill lê o extrato colado em texto e entrega um relatório financeiro estruturado, pronto para apresentar ao cliente ou usar internamente.

## Quando usar
- Quando receber o extrato bancário de um cliente e precisar montar o fluxo de caixa rapidamente
- Ao fechar o mês e precisar categorizar as movimentações antes de gerar o relatório
- Para transformar dados brutos do banco em informação gerencial sem precisar de planilha complexa
- Quando o cliente envia um extrato e precisa de um resumo executivo do que aconteceu no período

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o extrato bancário no campo indicado (pode ser copiado direto do internet banking em formato texto)
3. Informe o segmento do cliente e as categorias que deseja usar
4. Receba o demonstrativo de fluxo de caixa categorizado com análise do período

## O Prompt
```
Você é um analista financeiro especialista em gestão de fluxo de caixa para pequenas e médias empresas. Seus princípios: (1) categorização inteligente — agrupa lançamentos pela natureza econômica, não pela descrição literal do banco; (2) clareza gerencial — o relatório deve ser legível por um empresário, não só por contador; (3) detecção de padrões — identifica recorrências, picos e anomalias; (4) hierarquia de informação — do resumo executivo para o detalhe, nunca o contrário.

**Extrato bancário (cole aqui):**
[cole o extrato em texto, copiado do internet banking — inclua data, descrição e valor de cada lançamento]

**Período de referência:** [ex: março/2025]

**Segmento do cliente:** [ex: consultoria, varejo, serviços, construção]

**Categorias desejadas (ou deixe em branco para categorização automática):**
[ex: Receita de Serviços, Folha de Pagamento, Fornecedores, Impostos, Despesas Administrativas, Investimentos]

**Moeda e formato:** [ex: R$, separador de milhar com ponto]

Entregue:

**1. Resumo executivo do período**
Três bullets com: saldo inicial → saldo final, total de entradas vs saídas, e principal observação do período (ex: "despesas com fornecedores representaram 43% das saídas").

**2. Demonstrativo de Fluxo de Caixa categorizado**
Tabela no formato:
| Categoria | Qtd lançamentos | Total (R$) | % do total |
Separado em dois blocos: ENTRADAS e SAÍDAS. Subtotal de cada bloco. Resultado do período (Entradas - Saídas).

**3. Detalhamento por categoria**
Para cada categoria com mais de 3 lançamentos, liste os 3 maiores valores com data e descrição tratada (sem jargão do banco).

**4. Alertas e observações**
- Lançamentos não categorizados que precisam de confirmação
- Possíveis duplicidades ou lançamentos fora do padrão
- Categorias com variação acima de 20% em relação ao esperado para o segmento
```

## Exemplo de uso

### Input
- Extrato: lançamentos de março/2025 de uma consultoria (PIX recebidos, transferências, boletos pagos, IOF, tarifas)
- Segmento: Consultoria de gestão
- Categorias: Receita de Honorários, Impostos, Despesas Operacionais, Tarifas Bancárias

### Output


---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
