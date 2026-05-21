---
name: matriz-de-riscos-do-negocio
description: Criar uma matriz de riscos completa do negócio — identificando, classificando e priorizando os riscos por probabilidade e impacto — com planos de mitigação para cada risco.
---

# Matriz de Riscos do Negócio

## Objetivo
Criar uma matriz de riscos completa do negócio — identificando, classificando e priorizando os riscos por probabilidade e impacto — com planos de mitigação para cada risco.

## Quando usar
- No planejamento estratégico anual
- Ao expandir operações ou lançar novos produtos
- Para apresentar a investidores ou conselho
- Em auditorias de governança corporativa

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o negócio e contexto atual
3. Receba a matriz de riscos completa com mitigações
4. Revise trimestralmente e atualize conforme o cenário

## O Prompt
```
Você é um consultor de gestão de riscos que sabe equilibrar identificar riscos importantes sem paralisar a empresa.

Crie a matriz de riscos para:

**Empresa:** [nome e setor]
**Porte:** [faturamento ou número de funcionários]
**Modelo de negócio:** [serviço, produto, SaaS, e-commerce]
**Principais fontes de receita:** [de onde vem o dinheiro]
**Número de clientes:** [e concentração]
**Fase do negócio:** [início, crescimento, estabilidade, expansão]
**Riscos que já preocupam:** [liste os que já identificou]

Mapeie riscos em 6 categorias:
1. Riscos financeiros
2. Riscos operacionais
3. Riscos de mercado
4. Riscos de pessoas
5. Riscos legais e regulatórios
6. Riscos de reputação

Para cada risco:
- Descrição
- Probabilidade (Baixa/Média/Alta)
- Impacto (Baixo/Médio/Alto/Crítico)
- Score de risco
- Plano de mitigação
- Plano de contingência
- Indicador de alerta

Entregue:
- Matriz visual (Probabilidade × Impacto)
- Top 5 riscos críticos
- Plano de ação priorizado
```

## Exemplo de uso

### Input
Empresa: Agência de marketing digital (12 funcionários)
Faturamento: R$120K/mês
Clientes: 8, sendo 2 = 55% da receita
Riscos que preocupam: dependência de 2 clientes, dificuldade de contratar

### Output
Risco #1: Perda de cliente-chave (Cliente A = 30% da receita)

Probabilidade: MÉDIA (renovação em 4 meses)
Impacto: CRÍTICO (perder R$36K/mês causa prejuízo imediato)
Score: CRÍTICO

Mitigação:
1. Assinar contrato de 12 meses com multa rescisória
2. Meta: nenhum cliente representar mais de 20% até dezembro
3. Programa de cross-sell para aumentar ticket dos menores

Contingência: Se perder, ativar prospecção emergencial + reduzir custos variáveis em 20%.

Indicador de alerta: Cliente reduziu pedidos, pediu relatório de resultados detalhado.

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
