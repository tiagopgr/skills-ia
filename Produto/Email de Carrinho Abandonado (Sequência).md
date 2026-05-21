---
name: email-de-carrinho-abandonado-sequencia
description: Criar uma sequência de emails de recuperação de carrinho abandonado que traz o cliente de volta para concluir a compra — com timing, copy e incentivos estratégicos que recuperam de 10-30% dos carrinhos abandonados.
---

# Email de Carrinho Abandonado (Sequência)

## Objetivo
Criar uma sequência de emails de recuperação de carrinho abandonado que traz o cliente de volta para concluir a compra — com timing, copy e incentivos estratégicos que recuperam de 10-30% dos carrinhos abandonados.

## Quando usar
- Em qualquer e-commerce com taxa de abandono de carrinho
- Para SaaS com checkout de plano pago
- Quando implementar automação de email pela primeira vez
- Para otimizar sequência existente com baixa recuperação

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva seu e-commerce e público
3. Receba a sequência completa com copy e timing
4. Configure na ferramenta de automação de email

## O Prompt
```
Você é um especialista em recuperação de carrinhos que sabe que 70% dos carrinhos são abandonados — mas 10-30% podem ser recuperados. Seus princípios: (1) o primeiro email não oferece desconto — apenas lembra, (2) cada email trata uma objeção diferente, (3) o desconto só vem no último email.

Crie a sequência de carrinho abandonado para:

**E-commerce/Produto:** [descreva]
**Ticket médio:** [valor]
**Público:** [quem compra]
**Tom da marca:** [casual, premium, divertido, profissional]
**Ferramenta de email:** [Mailchimp, Klaviyo, RD Station]
**Incentivo disponível:** [frete grátis, desconto %, cupom, bônus, nenhum]

Entregue sequência (3-4 emails): Email 1 — Lembrete (1h), Email 2 — Objeção (24h), Email 3 — Urgência (48h), Email 4 — Última chance (72h — opcional).

Para cada: Timing, Assunto + preview text, Copy completa, CTA, Produto dinâmico.

Extras: SMS de recuperação, Popup de exit intent, A/B tests sugeridos.
```

## Exemplo de uso

### Input
E-commerce: Loja de cosméticos naturais
Ticket médio: R$120
Público: Mulheres 25-45, preocupadas com ingredientes
Tom: Acolhedor e clean
Incentivo: Frete grátis acima de R$99

### Output
Email 1 — 1h após abandono:
Assunto: "Esqueceu algo? Seus produtos estão esperando"
Preview: "Separamos seus itens. É só finalizar."

"Oi [nome],

Você deixou alguns produtos no carrinho — e entendemos, às vezes a gente precisa de um tempinho.

[IMAGEM DO PRODUTO]
[Nome do produto] — R$[valor]

Seus itens estão reservados, mas não por muito tempo.

[BOTÃO: Finalizar minha compra]"

Email 3 (48h):
Assunto: "Últimas unidades + frete grátis pra você decidir"
Copy: "Use o código VOLTEI e ganhe frete grátis. Válido por 24h."

---
**Tags:** Intermediário | Geração | Produto, E-commerce & SaaS
