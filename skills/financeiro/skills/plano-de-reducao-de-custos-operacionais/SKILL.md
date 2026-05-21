---
name: plano-de-reducao-de-custos-operacionais
description: Criar um plano estruturado de redução de custos operacionais — com mapeamento de despesas, identificação de oportunidades de corte ou otimização, e plano de ação por prioridade — para que gestores de pequenas equipes consigam reduzir custos de forma inteligente, sem cortar o que gera resultado e sem comprometer a produtividade ou a qualidade das entregas para o cliente.
---

# Plano de Redução de Custos Operacionais

## Objetivo
Criar um plano estruturado de redução de custos operacionais — com mapeamento de despesas, identificação de oportunidades de corte ou otimização, e plano de ação por prioridade — para que gestores de pequenas equipes consigam reduzir custos de forma inteligente, sem cortar o que gera resultado e sem comprometer a produtividade ou a qualidade das entregas para o cliente.

## Quando usar
- Quando o resultado financeiro estiver abaixo do esperado e precisar reduzir despesas
- Para revisar o custo da equipe e identificar se há tarefas que podem ser eliminadas ou automatizadas
- Ao querer aumentar a margem do negócio sem precisar aumentar a receita
- Para preparar um plano de eficiência para apresentar a sócios ou diretores

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste as principais categorias de custo, os valores e o que você já sabe sobre cada uma
3. Receba o plano de redução de custos com oportunidades identificadas, impacto estimado e ações
4. Priorize as ações por impacto e facilidade de implementação e execute em 30-60 dias

## O Prompt
```
Você é um consultor de gestão especializado em eficiência operacional e redução de custos para pequenas e médias empresas. Seus princípios: (1) cortar custo de forma inteligente significa cortar o que não gera resultado, não o que parece mais fácil de cortar — o erro mais comum é cortar treinamento, marketing e ferramentas que são multiplicadores de resultado, (2) antes de cortar, otimize — muitas vezes o mesmo custo pode ser reduzido sem eliminação: negociação com fornecedor, renegociação de contrato, substituição por alternativa mais eficiente, (3) custo de pessoal é o maior e o mais sensível — antes de demitir, analise se redistribuição de tarefas ou automação resolve, (4) toda redução de custo tem um custo de implementação — calcule o tempo de payback antes de agir.

Crie o plano de redução de custos com base nas informações abaixo:

**Despesas mensais por categoria:**
[liste cada categoria com o valor mensal: pessoal / aluguel / ferramentas e software / marketing / fornecedores / logística / outros]

**Meta de redução:** [ex: reduzir R$X ou X% dos custos totais]
**Prazo para implementar:** [ex: 30 dias / 60 dias / 90 dias]
**Restrições:** [o que NÃO pode ser cortado — ex: não pode demitir / não pode parar de atender clientes X]
**Contexto do negócio:** [por que está buscando redução agora — crise, crescimento, melhoria de margem]
**O que você já identificou como oportunidade:** [se já tem alguma ideia, liste aqui]

Entregue:

**1. Mapeamento de despesas**
Tabela de todas as despesas com: categoria | valor mensal | % do total | classificação (essencial / importante / opcional).

**2. Oportunidades de redução identificadas**
Para cada oportunidade: categoria | ação sugerida | economia estimada | facilidade (fácil/médio/difícil) | risco (baixo/médio/alto).

**3. Análise de custo de pessoal**
Mapeamento das funções e tarefas da equipe, identificando: tarefas que podem ser automatizadas, tarefas que podem ser redistribuídas, e tarefas que podem ser terceirizadas de forma mais barata.

**4. Plano de ação por prioridade**
Ordem de implementação baseada em impacto financeiro × facilidade × risco, com responsável e prazo para cada ação.

**5. Projeção de economia**
Total de economia possível se todas as ações forem implementadas, dividido em: curto prazo (30 dias), médio prazo (60 dias), longo prazo (90+ dias).

**6. Alertas de risco**
O que não cortar — lista de custos que parecem cortáveis mas que têm impacto negativo alto se eliminados.
```

## Exemplo de uso

### Input
- Despesas: Pessoal R$18.000 / Aluguel R$3.500 / Software R$1.200 / Marketing R$2.500 / Fornecedores R$4.000 / Outros R$1.800 — Total R$31.000
- Meta: Reduzir R$4.000-5.000/mês
- Prazo: 60 dias
- Restrições: Não pode demitir os 2 funcionários fixos / não pode parar a operação de atendimento
- Contexto: Margem caiu de 25% para 18% nos últimos 3 meses

### Output
| Categoria | Ação | Economia estimada | Facilidade | Risco |
|---|---|---|---|---|
| Software | Auditar ferramentas — 3 provavelmente duplicadas ou subutilizadas | R$400-600/mês | Fácil | Baixo |
| Marketing | Migrar 1 canal pago para orgânico por 60 dias e medir impacto | R$1.000/mês | Médio | Médio |
| Fornecedores | Renegociar contrato do principal fornecedor com prazo maior em troca de desconto | R$600-800/mês | Médio | Baixo |
| Outros | Revisar assinaturas e serviços recorrentes não usados | R$300-500/mês | Fácil | Baixo |

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
