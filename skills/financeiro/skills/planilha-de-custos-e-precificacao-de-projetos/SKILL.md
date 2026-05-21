---
name: planilha-de-custos-e-precificacao-de-projetos
description: Estruturar uma planilha de custos e precificação completa para projetos técnicos — contemplando custo dos equipamentos, mão de obra, impostos, margem de lucro e preço de venda final — para que o gestor nunca mais venda projeto sem saber exatamente quanto vai lucrar, elimine o risco de precificar abaixo do custo real e apresente ao cliente um preço fundamentado que resiste à negociação.
---

# Planilha de Custos e Precificação de Projetos

## Objetivo
Estruturar uma planilha de custos e precificação completa para projetos técnicos — contemplando custo dos equipamentos, mão de obra, impostos, margem de lucro e preço de venda final — para que o gestor nunca mais venda projeto sem saber exatamente quanto vai lucrar, elimine o risco de precificar abaixo do custo real e apresente ao cliente um preço fundamentado que resiste à negociação.

## Quando usar
- Antes de montar qualquer proposta comercial, para garantir que o preço está correto
- Quando percebe que fechou projetos mas a margem não aparece no caixa
- Para padronizar a forma de calcular preço em toda a empresa
- Quando vai negociar desconto e precisa saber até onde pode ir sem prejuízo

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os itens do projeto, custos estimados e parâmetros financeiros da empresa
3. Receba a estrutura completa da planilha com fórmulas e lógica de precificação
4. Monte no Excel ou Google Sheets e use como template padrão para todos os projetos

## O Prompt
```
Você é um especialista em finanças e precificação para empresas de tecnologia e serviços técnicos. Seus princípios: (1) custo real não é só o preço do equipamento — inclui frete, importação, estoque, perdas e custo financeiro do prazo de pagamento, (2) margem de lucro deve ser calculada sobre o preço de venda, não sobre o custo — confundir os dois é o erro mais comum em precificação, (3) mão de obra deve ter custo real calculado com encargos, não só o salário líquido, (4) imposto varia conforme regime tributário — simples nacional, lucro presumido e lucro real têm cargas muito diferentes e impactam diretamente o preço mínimo.

**Tipo de projeto:** [ex: sistema de CFTV + controle de acesso]
**Lista de equipamentos com custo de compra:** [ex: 20 câmeras a R$480 cada, 1 NVR a R$1.200, cabos e acessórios R$2.000]
**Horas estimadas de mão de obra:** [ex: 80 horas de técnico a R$45/hora]
**Regime tributário da empresa:** [ex: Simples Nacional / Lucro Presumido]
**Margem de lucro desejada:** [ex: 25% sobre o preço de venda]
**Prazo de pagamento do cliente:** [ex: 30% entrada + 70% na entrega]
**Custo de deslocamento e logística:** [ex: R$800]

Entregue:

**1. Estrutura da planilha de custos (linha por linha)**
Descrição de cada linha da planilha com fórmula:
| Linha | Descrição | Como calcular | Exemplo |
Incluir: custo direto equipamentos, custo de mão de obra real, logística, overhead (% sobre custo), impostos (% sobre preço de venda), margem desejada, preço mínimo e preço de venda sugerido.

**2. Simulação com os dados informados**
Cálculo completo com os valores fornecidos, mostrando:
- Custo total direto
- Custo total com overhead
- Impostos sobre o preço de venda
- Preço mínimo de venda (break-even)
- Preço de venda com margem desejada
- Margem de contribuição em R$ e %
- Faixa de desconto máximo possível sem prejuízo

**3. Tabela de preços por categoria para a proposta**
Versão resumida para apresentar ao cliente, agrupando itens por categoria com valor por categoria e total geral.

**4. Alerta de riscos financeiros**
Principais riscos que podem corroer a margem nesse tipo de projeto e como proteger cada um contratualmente.
```

## Exemplo de uso

### Input
- Projeto: CFTV 24 câmeras + NVR
- Equipamentos: 24 câmeras R$480 = R$11.520 / NVR R$1.800 / acessórios R$2.200
- Mão de obra: 60h a R$45/h = R$2.700
- Regime: Simples Nacional (alíquota 11%)
- Margem desejada: 28%
- Logística: R$600

### Output
| Componente | Valor |
|-----------|-------|
| Custo direto equipamentos | R$15.520 |
| Mão de obra direta | R$2.700 |
| Logística | R$600 |
|

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
