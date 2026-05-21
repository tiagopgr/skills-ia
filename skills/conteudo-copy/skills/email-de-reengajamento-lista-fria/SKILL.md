---
name: email-de-reengajamento-lista-fria
description: Criar emails para reativar leads que pararam de abrir seus emails, trazendo-os de volta ao engajamento ativo antes de limpar a lista.
---

# Email de Reengajamento (Lista Fria)

## Objetivo
Criar emails para reativar leads que pararam de abrir seus emails, trazendo-os de volta ao engajamento ativo antes de limpar a lista.

## Quando usar
- Quando parte da lista não abre emails há 30-90+ dias
- Antes de fazer uma limpeza de lista (remover inativos)
- Quando a taxa de abertura geral está caindo
- Para reativar lista antes de um lançamento importante

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Defina o contexto e segmento inativo
3. Receba a sequência de reengajamento (3 emails)
4. Envie e, após a sequência, remova quem não abriu nenhum

## O Prompt
```
Você é um especialista em higiene e reengajamento de listas de email. Você sabe que manter leads inativos prejudica a entregabilidade, mas que antes de remover, vale fazer uma última tentativa — e que emails de reengajamento bem feitos podem recuperar 5-15% dos inativos.

Crie uma sequência de reengajamento para lista fria:

**Há quanto tempo estão inativos:** [30 dias | 60 dias | 90+ dias]
**Tamanho do segmento inativo:** [aproximado]
**Seu negócio:** [o que você faz]
**Último conteúdo relevante enviado:** [o que eles receberam antes de parar de abrir]
**Incentivo disponível:** [desconto, conteúdo exclusivo, brinde — ou nenhum]
**Tom da marca:** [casual, profissional, direto, humorístico]

Gere 3 emails de reengajamento progressivos:

**Email 1 — O toque gentil (Dia 0)**
Objetivo: Fazer a pessoa abrir SEM parecer desesperado.
Abordagem: "Faz tempo que não te vejo por aqui" — tom leve e curioso.
SEM oferta. Só reconexão.

**Email 2 — O valor irresistível (Dia 3)**
Objetivo: Dar um motivo concreto para voltar a engajar.
Abordagem: Entregar algo valioso de graça ou compartilhar algo exclusivo.

**Email 3 — O ultimato elegante (Dia 7)**
Objetivo: Última tentativa antes de remover da lista.
Abordagem: "Vou te remover da lista se você não quiser continuar — tudo bem."

Para cada email:
- **5 opções de assunto**
- **Preview text**
- **Corpo completo** (curto — máximo 150 palavras cada)
- **CTA**
- **Por que funciona psicologicamente**
- **Taxa de reabertura esperada nessa etapa**
```

## Exemplo de uso

### Input
Inativos há 60+ dias
Segmento: ~2.000 leads
Negócio: Consultoria de carreira
Último envio: Newsletter mensal
Incentivo: Ebook exclusivo "10 Erros no LinkedIn"
Tom: Casual e direto

### Output
**Email 3 — Ultimato elegante:**
- Assunto: "Vou te remover da lista (a não ser que...)"
- Preview: "Sem ressentimentos. Mas preciso saber."
- Corpo: "Oi [nome], esse é o último email que vou te enviar. Nos últimos 60 dias, mandei conteúdo sobre carreira, LinkedIn e mercado de trabalho. Parece que não está mais fazendo sentido pra você — e tudo bem. Eu prefiro uma lista menor e engajada do que uma lista grande que não lê. Se você quer CONTINUAR recebendo, clica no botão abaixo. Se não clicar, eu te removo automaticamente em 5 dias. Sem ressentimentos. [Botão: QUERO CONTINUAR RECEBENDO]"

---
**Tags:** Intermediário | Geração | Conteúdo & Copy
