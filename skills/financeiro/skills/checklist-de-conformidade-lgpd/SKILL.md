---
name: checklist-de-conformidade-lgpd
description: Criar um checklist completo e prático de conformidade com a LGPD — avaliando o estado atual, identificando gaps e priorizando as ações necessárias para estar em conformidade e evitar multas.
---

# Checklist de Conformidade LGPD

## Objetivo
Criar um checklist completo e prático de conformidade com a LGPD — avaliando o estado atual, identificando gaps e priorizando as ações necessárias para estar em conformidade e evitar multas.

## Quando usar
- Para avaliar se a empresa está em conformidade com a LGPD
- Ao iniciar um programa de adequação
- Em auditorias internas periódicas
- Antes de lançar novos produtos que coletam dados

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o tipo de empresa e dados que trata
3. Receba o checklist com avaliação e ações
4. Use como guia para o programa de adequação

## O Prompt
```
Você é um consultor de LGPD que sabe que a adequação não precisa ser complexa se for prática e priorizada. Comece pelo que gera mais risco.

IMPORTANTE: Para conformidade completa, recomende consultoria especializada.

Crie o checklist de conformidade para:

**Tipo de empresa:** [e-commerce, SaaS, agência, clínica, escola]
**Porte:** [MEI, ME, EPP, médio, grande]
**Dados que coleta:** [nome, email, CPF, dados de saúde, financeiros]
**Canais de coleta:** [site, app, formulários, WhatsApp, loja física]
**Ferramentas que usa:** [CRM, email marketing, analytics, ERP]
**Tem DPO definido?** [sim/não]

Entregue o checklist em 8 áreas:
1. Governança e responsabilidade
2. Mapeamento de dados
3. Direitos dos titulares
4. Consentimento e transparência
5. Segurança da informação
6. Compartilhamento e terceiros
7. Retenção e descarte
8. Treinamento e cultura

Para cada item: Status (Conforme/Parcial/Não conforme), Prioridade, Ação necessária

Ao final:
- Score de conformidade (0-100%)
- Top 5 ações prioritárias
- Riscos de não conformidade
```

## Exemplo de uso

### Input
Tipo: E-commerce de suplementos
Porte: ME
Dados: nome, email, CPF, endereço, cartão (via gateway)
Ferramentas: Shopify, Mailchimp, Google Analytics, Meta Pixel
DPO: Não definido

### Output
Score estimado: 25/100 — "Fase inicial. Há riscos significativos."

Top 5 ações prioritárias:
1. Nomear DPO (pode ser o próprio dono em ME) — Prioridade ALTA
2. Atualizar política de privacidade — precisa listar Meta Pixel, GA
3. Implementar banner de cookies com opção de recusa
4. Criar processo para atender solicitações de titulares
5. Revisar contrato com Mailchimp — dados transferidos para EUA

Risco: Multa de até 2% do faturamento. Para ME, maior risco é advertência pública e dano reputacional.

---
**Tags:** Intermediário | Auditoria | Financeiro, Jurídico & Compliance
