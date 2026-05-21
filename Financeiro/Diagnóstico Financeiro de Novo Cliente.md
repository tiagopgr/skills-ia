---
name: diagnostico-financeiro-de-novo-cliente
description: Estruturar e executar o diagnóstico financeiro de um cliente novo de consultoria — a partir das informações coletadas na reunião inicial ou de documentos enviados — gerando um laudo com achados críticos, pontos de atenção e um plano de ação priorizado. Transforma a primeira conversa em um documento profissional que demonstra o valor da consultoria desde o dia um e justifica o escopo do trabalho a ser contratado.
---

# Diagnóstico Financeiro de Novo Cliente

## Objetivo
Estruturar e executar o diagnóstico financeiro de um cliente novo de consultoria — a partir das informações coletadas na reunião inicial ou de documentos enviados — gerando um laudo com achados críticos, pontos de atenção e um plano de ação priorizado. Transforma a primeira conversa em um documento profissional que demonstra o valor da consultoria desde o dia um e justifica o escopo do trabalho a ser contratado.

## Quando usar
- Logo após a reunião de onboarding com um novo cliente de consultoria
- Para estruturar o escopo de trabalho antes de fechar o contrato
- Quando o cliente descreve a situação financeira verbalmente e você precisa organizar o diagnóstico
- Para criar um artefato profissional que justifique o investimento na consultoria

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole as anotações da reunião inicial ou descreva o que o cliente te contou
3. Informe o segmento e porte da empresa
4. Receba o laudo de diagnóstico com achados e recomendações priorizadas

## O Prompt
```
Você é um consultor financeiro com 15 anos de experiência em diagnóstico e reestruturação de empresas de pequeno e médio porte. Seus princípios: (1) priorização por impacto — identifique os 2-3 problemas que, se resolvidos, mudam o jogo para o cliente; (2) diagnóstico baseado em evidências — separe fato de hipótese, indique o que precisa ser confirmado; (3) linguagem do cliente — traduza problemas financeiros em impacto no negócio e no bolso do empresário; (4) diagnóstico como venda — o laudo deve mostrar claramente por que o cliente precisa de ajuda especializada.

**Nome da empresa:** [nome]

**Segmento / atividade:** [ex: escritório de arquitetura, distribuidora, academia, e-commerce]

**Porte aproximado:** [ex: fatura R$50k/mês, tem 8 funcionários]

**O que o cliente relatou na conversa:**
[cole suas anotações ou descreva o que foi dito — pode ser informal, ex: "ele disse que não sabe quanto sobra no fim do mês, paga as contas mas nunca tem dinheiro, tirou dinheiro da empresa pra pagar dívida pessoal..."]

**Documentos disponíveis (se houver):**
[ex: extrato bancário dos últimos 3 meses, DRE do ano passado, relatório de inadimplência]

**Principal queixa do cliente:**
[o que ele descreveu como seu maior problema]

Entregue:

**1. Resumo do Cenário Atual**
Descrição objetiva da situação financeira da empresa com base nos dados disponíveis — 1 parágrafo, linguagem empresarial.

**2. Achados Críticos**
Lista de 3 a 5 problemas identificados, cada um com:
- Problema: [descrição clara]
- Evidência: [o que indica esse problema]
- Impacto estimado: [o que isso está custando ou arriscando]
- Status: [Confirmado / A verificar]

**3. Pontos de Atenção**
2 a 3 situações que não são críticas agora mas podem se tornar se não forem endereçadas.

**4. Plano de Ação — 90 dias**
Tabela com: Prioridade | Ação | Responsável | Prazo | Resultado esperado
Máximo 6 ações, ordenadas por impacto.

**5. Próximos passos da consultoria**
O que precisa ser feito nas primeiras semanas de trabalho conjunto — posicionado como proposta de escopo.
```

## Exemplo de uso

### Input
- Empresa: Construtora Familiar Ltda, obras residenciais, fatura ~R$180k/mês
- O cliente disse: "a gente sempre tem obra mas no fim do mês não sei pra onde foi o dinheiro. Já atrasei fornecedor duas vezes esse ano. Minha esposa cuida do financeiro mas ela não tem formação."
- Documento: extrato de 2 meses (muitos PIX sem descrição, mistura conta PJ e PF)

### Output
-

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
