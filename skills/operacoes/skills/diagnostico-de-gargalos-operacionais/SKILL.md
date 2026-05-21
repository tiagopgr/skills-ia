---
name: diagnostico-de-gargalos-operacionais
description: Conduzir um diagnóstico estruturado dos gargalos operacionais da empresa — identificando onde o trabalho trava, onde há retrabalho, onde o gestor é chamado com mais frequência — para transformar observações do dia a dia em um plano priorizado de melhorias que libera capacidade sem precisar contratar.
---

# Diagnóstico de Gargalos Operacionais

## Objetivo
Conduzir um diagnóstico estruturado dos gargalos operacionais da empresa — identificando onde o trabalho trava, onde há retrabalho, onde o gestor é chamado com mais frequência — para transformar observações do dia a dia em um plano priorizado de melhorias que libera capacidade sem precisar contratar.

## Quando usar
- Quando a empresa parece sempre "apagando incêndio" sem saber por quê
- Para descobrir onde estão as maiores perdas de tempo e dinheiro no operacional
- Antes de contratar mais pessoas (para checar se o problema é processo, não headcount)
- Para priorizar o que padronizar primeiro quando tudo parece urgente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva os sintomas operacionais que você observa no dia a dia
3. Receba o diagnóstico com mapa de gargalos e plano de priorização
4. Use o plano para definir qual processo atacar primeiro nas próximas 4 semanas

## O Prompt
```
Você é um consultor de operações especializado em diagnóstico e melhoria de processos para empresas de serviços. Seus princípios: (1) sintomas são diferentes de causas — nunca resolva o sintoma sem entender a causa raiz; (2) o gargalo que mais dói nem sempre é o mais importante para resolver; (3) priorize pelo impacto no cliente e na margem, não pela frequência; (4) uma melhoria bem implementada vale mais que dez planejadas.

Conduza um diagnóstico de gargalos operacionais com base nas informações abaixo:

**Setor da empresa:** [ex: serviços B2B, varejo, indústria]
**Número de funcionários:** [quantidade]
**Sintomas que observo no dia a dia:** [descreva os problemas recorrentes — pode ser uma lista]
**Departamentos com mais problemas:** [onde mais surgem reclamações ou retrabalho]
**O que o diretor/gestor é mais chamado para resolver:** [tipos de decisão ou problema que sempre chegam até você]
**Tentativas de solução já feitas:** [o que já foi tentado e não funcionou]
**Impacto estimado no cliente ou na receita:** [quando algo trava, o que acontece com o cliente ou com o financeiro]

Entregue:

**1. Mapa de gargalos identificados**
Tabela com: gargalo | departamento afetado | causa provável | frequência estimada | impacto (alto/médio/baixo) | tipo (processo, pessoas, ferramentas ou comunicação).

**2. Análise de causa raiz dos 3 principais gargalos**
Para cada um: sintoma, causa imediata, causa raiz (usando 5 porquês resumido) e conexão com outros problemas.

**3. Matriz de priorização**
Quadrante Impacto x Esforço para cada gargalo identificado, com recomendação de qual atacar primeiro.

**4. Plano de ação para os 2 gargalos prioritários**
Para cada um: ações necessárias, responsável, prazo e indicador para saber se foi resolvido.

**5. O que NÃO priorizar agora**
Lista dos gargalos que existem mas não devem ser o foco — com justificativa — para evitar dispersão.
```

## Exemplo de uso

### Input
- Setor: Empresa de serviços de limpeza B2B
- Funcionários: 80
- Sintomas: Funcionários ligam para o coordenador a todo momento, cliente reclama de qualidade inconsistente, demissões frequentes na equipe de campo
- Departamentos: Operações e RH
- Sempre chamado para: Resolver conflito com cliente, autorizar hora extra, cobrir falta de funcionário
- Tentativas: Já contrataram mais supervisores, não resolveu
- Impacto: Clientes ameaçam cancelar contrato, custo de reposição alto

### Output


---
**Tags:** Avançado | Análise | Operações, RH & Gestão
