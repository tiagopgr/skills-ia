---
name: analise-de-inadimplencia-da-carteira
description: Analisar a carteira de contas a receber de um cliente de consultoria — identificando inadimplentes por faixa de atraso, valor e perfil — e gerar um plano de cobrança priorizado com abordagens diferentes por perfil (bom pagador com atraso pontual vs. inadimplente recorrente) e modelos de mensagem prontos para usar. Transforma uma lista de devedores em uma estratégia de recuperação.
---

# Análise de Inadimplência da Carteira

## Objetivo
Analisar a carteira de contas a receber de um cliente de consultoria — identificando inadimplentes por faixa de atraso, valor e perfil — e gerar um plano de cobrança priorizado com abordagens diferentes por perfil (bom pagador com atraso pontual vs. inadimplente recorrente) e modelos de mensagem prontos para usar. Transforma uma lista de devedores em uma estratégia de recuperação.

## Quando usar
- No fechamento mensal para apresentar a situação de inadimplência ao cliente
- Quando o cliente relata dificuldade de receber e não tem processo de cobrança estruturado
- Para montar o plano de cobrança dos próximos 15 dias
- Ao assumir a gestão financeira de uma empresa com inadimplência histórica elevada

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole a lista de inadimplentes com valor, dias de atraso e contexto de cada um
3. Informe o perfil do negócio e a política de cobrança atual
4. Receba o ranking priorizado com plano de ação e mensagens prontas

## O Prompt
```
Você é um especialista em gestão de crédito e cobrança para PMEs. Seus princípios: (1) priorize por impacto no caixa — comece pelos maiores valores, não pelos mais antigos; (2) cobrança é relacionamento — tom agressivo destrói clientes bons que tiveram um deslize; (3) diferente perfil, diferente abordagem — bom pagador com atraso pontual ≠ inadimplente recorrente; (4) documente tudo — cada tentativa de cobrança deve ser registrada.

**Empresa e segmento:** [nome e setor]

**Lista de inadimplentes:**
[para cada devedor: Nome/empresa | Valor em aberto | Dias de atraso | Histórico (bom pagador / recorrente / novo cliente)]

**Valor total em aberto:** [R$ total]

**% de inadimplência sobre receita mensal:** [ex: 12%]

**Política de cobrança atual:**
[ex: nenhuma estruturada / manda WhatsApp quando lembra / bloqueia serviço após 30 dias]

**Canal principal de relacionamento com clientes:** [WhatsApp / email / telefone / presencial]

**Restrições (se houver):**
[ex: não pode bloquear serviço de clientes com contrato vigente / tem um cliente VIP inadimplente]

Entregue:

**1. Dashboard de inadimplência**
Tabela com faixas de atraso: 1-15 dias | 16-30 dias | 31-60 dias | +60 dias — com total de clientes e valor em cada faixa.

**2. Ranking de cobrança priorizado**
Lista dos inadimplentes ordenados por prioridade de ação (valor + risco) com: Nome | Valor | Dias | Perfil | Ação recomendada | Prazo

**3. Plano de cobrança — próximos 15 dias**
Cronograma dia a dia das ações de cobrança, segmentado por faixa de atraso.

**4. Modelos de mensagem prontos**
- Lembrete amigável (1-15 dias)
- Cobrança direta (16-30 dias)
- Cobrança firme com prazo (31-60 dias)
- Carta de intenção de protesto (+60 dias)

**5. Indicadores de monitoramento**
O que acompanhar semanalmente para medir a evolução da inadimplência.
```

## Exemplo de uso

### Input
- 5 inadimplentes, total R$23.400 (15% da receita mensal)
- Mix: 2 bons pagadores com atraso < 20 dias, 2 entre 30-45 dias, 1 com 75 dias e R$8.500

### Output
*Olá [Nome], tudo bem?*

*Passando para avisar que identificamos um valor em aberto de R$[X] referente a [descrição], com vencimento em [data].*

*Sabemos que às vezes uma data pode passar despercebida. Caso já tenha realizado o pagamento, por favor desconsidere esta mensagem.*

*Para regularizar, segue o PIX: [chave] ou o link do boleto: [link]*

*Se precisar conversar sobre o pagamento, estou à disposição.*

---
**Tags:** Intermediário | Análise | Financeiro, Jurídico & Compliance
