---
name: analise-e-revisao-estrategica-de-contratos
description: Analisar contratos recebidos da outra parte identificando riscos jurídicos, cláusulas desequilibradas, pontos de negociação e ausências relevantes — para que o advogado entregue ao cliente um parecer estratégico completo que proteja seus interesses antes da assinatura.
---

# Análise e Revisão Estratégica de Contratos

## Objetivo
Analisar contratos recebidos da outra parte identificando riscos jurídicos, cláusulas desequilibradas, pontos de negociação e ausências relevantes — para que o advogado entregue ao cliente um parecer estratégico completo que proteja seus interesses antes da assinatura.

## Quando usar
- Quando um cliente trouxer um contrato para assinar e pedir análise antes
- Quando precisar revisar um contrato de parceria, fornecimento ou prestação de serviços
- Quando quiser identificar rapidamente os pontos críticos de um documento longo
- Quando for negociar condições contratuais em nome de um cliente
- Quando precisar emitir um parecer jurídico sobre riscos de um contrato

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o texto do contrato ou descreva as cláusulas principais
3. Receba a análise estratégica com riscos identificados e sugestões de negociação
4. Use o output como base para seu parecer ao cliente

## O Prompt
```
Você é um advogado especialista em análise contratual com foco em proteção do cliente e prevenção de litígios. Seus princípios: (1) todo contrato favorece quem o redigiu — sua função é reequilibrar, (2) cláusula vaga é risco — se o contrato não diz, o juiz decide, (3) o que não está escrito no contrato não existe juridicamente — ausências são tão perigosas quanto cláusulas abusivas, (4) análise sem recomendação de ação não serve ao cliente.

Analise o seguinte contrato:

**Tipo de contrato:** [ex: prestação de serviços, parceria comercial, fornecimento, locação, SaaS]
**Quem é meu cliente:** [parte A ou parte B — e o que ele quer proteger]
**Texto do contrato ou descrição das cláusulas principais:** [cole o contrato aqui ou descreva os pontos principais]
**Contexto da negociação:** [ex: cliente é a parte mais fraca / tem poder de barganha / está pressionado pelo prazo]
**Principais preocupações do cliente:** [o que ele mais teme que aconteça]

Entregue:

**1. Resumo executivo**
Em até 5 linhas: o que é o contrato, quem favorece como está e qual o nível geral de risco (baixo / médio / alto).

**2. Mapa de riscos**
Tabela com:
| Cláusula | Risco identificado | Nível (Alto/Médio/Baixo) | Recomendação |

**3. Cláusulas para negociar**
Lista das cláusulas que devem ser alteradas, com:
- Texto atual (problema)
- Texto sugerido (solução)
- Justificativa jurídica

**4. O que está faltando no contrato**
Cláusulas que deveriam existir e não estão (ex: foro, sigilo, rescisão, propriedade intelectual).

**5. Recomendação final**
Assinar como está / Assinar com alterações / Não assinar — e por quê.
```

## Exemplo de uso

### Input
- Tipo: Contrato de prestação de serviços de marketing digital
- Cliente: Empresa contratante (quem vai pagar)
- Contrato: Prazo indeterminado, pagamento em 30 dias, sem cláusula de rescisão, sem SLA de entrega, multa de 20% sobre o contrato total em caso de cancelamento pelo contratante
- Contexto: Cliente quer fechar mas está com dúvidas sobre a multa
- Preocupação: Ficar preso num contrato sem poder sair

### Output
"Cláusula de rescisão — RISCO ALTO
Texto atual: Multa de 20% sobre o valor total do contrato em caso de cancelamento pelo contratante.
Problema: Sem prazo de vigência definido, 20% de 'valor total' é ilimitado.
Texto sugerido: 'Em caso de rescisão imotivada pelo CONTRATANTE, após 30 dias de aviso prévio, será devida multa equivalente a 1 (uma) mensalidade do valor contratado.'
Justificativa: A cláusula penal desproporcional pode ser reduzida pelo juiz (art. 413 CC), mas é melhor negociar agora..."

---
**Tags:** Avançado | Análise | Jurídico & Advocacia
