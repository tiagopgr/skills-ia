---
name: bot-de-atendimento-e-vendas-para-whatsapp
description: Criar o script completo de um bot de atendimento e vendas para WhatsApp — com fluxo de qualificação, respostas automáticas para as dúvidas mais comuns, apresentação de produto e fechamento de venda — para que o empreendedor solo pare de responder as mesmas perguntas manualmente e tenha um sistema que atende e vende mesmo quando está ocupado.
---

# Bot de Atendimento e Vendas para WhatsApp

## Objetivo
Criar o script completo de um bot de atendimento e vendas para WhatsApp — com fluxo de qualificação, respostas automáticas para as dúvidas mais comuns, apresentação de produto e fechamento de venda — para que o empreendedor solo pare de responder as mesmas perguntas manualmente e tenha um sistema que atende e vende mesmo quando está ocupado.

## Quando usar
- Para criar o fluxo de um bot no WhatsApp Business ou ferramentas como ManyChat, Typebot ou Z-API
- Quando as mesmas perguntas chegam todos os dias e consomem muito tempo de atendimento
- Para atender leads de anúncios automaticamente sem precisar ficar no celular o dia todo
- Quando quiser criar um script de atendimento para uma assistente ou freelancer seguir
- Para padronizar o atendimento e garantir que nenhum lead caia no esquecimento

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os produtos que vende, as perguntas mais frequentes e o fluxo desejado
3. Receba o script completo de cada etapa do bot com as mensagens exatas
4. Configure o fluxo no WhatsApp Business (respostas rápidas) ou numa ferramenta de automação

## O Prompt
```
Você é um especialista em automação de atendimento e vendas por WhatsApp para e-commerce. Seus princípios: (1) bot não substitui relacionamento — ele filtra e qualifica para que o humano entre no momento certo, (2) a primeira mensagem do bot precisa parecer humana e contextualizada, não robótica, (3) o fluxo precisa levar o lead ao link de compra em no máximo 3-4 trocas de mensagem, (4) perguntas de qualificação aumentam conversão porque chegam ao produto certo.

Crie o script completo de bot de WhatsApp com os seguintes dados:

**Produtos que vende:** [lista com preços e link de compra de cada um]
**Principais perguntas que recebe todo dia:** [liste as 5-8 perguntas mais frequentes]
**Origem dos contatos:** [anúncio no Meta / Instagram / indicação / Mercado Livre / outros]
**Palavra-chave de ativação (se houver):** [ex: a pessoa manda "OI" ou "QUERO"]
**Quer que o bot tente vender sozinho ou apenas qualifique para você responder?** [vende sozinho / qualifica + avisa você]
**Ferramenta que vai usar:** [WhatsApp Business simples / ManyChat / Typebot / Z-API / não sabe ainda]

Entregue o script completo com:

**1. Mensagem de boas-vindas (gatilho inicial)**
A primeira mensagem automática quando alguém entra em contato — personalizada por origem se possível

**2. Fluxo de qualificação (2-3 perguntas)**
As perguntas que identificam o que o cliente precisa e qual produto apresentar

**3. Apresentação de produto (por produto)**
Para cada produto, a mensagem completa de apresentação com benefício, preço e link

**4. Respostas automáticas para as perguntas frequentes**
Para cada pergunta informada: a resposta exata que o bot deve dar

**5. Mensagem de fechamento**
A mensagem de CTA final que empurra para o link de compra

**6. Mensagem de follow-up (para quem não respondeu)**
Mensagem automática para reativar lead que parou de responder em 24h

**7. Fluxo visual (mapa do bot)**
Diagrama em texto mostrando o caminho: mensagem 1 → opção A → mensagem 2A → etc.

**8. Instruções de configuração**
Passo a passo de como configurar no WhatsApp Business simples (respostas rápidas e mensagem de ausência)
```

## Exemplo de uso

### Input
- Produtos: Suporte notebook R$89 (link A) / Mousepad R$39 (link B) / Kit home office R$109 (link C)
- Perguntas frequentes: Serve no meu notebook? / Tem frete grátis? / Quanto tempo entrega? / Pode parcelar? / Tem garantia?
- Origem: Anúncio no Instagram
- Ativação: Pessoa manda qualquer mensagem
- Objetivo: Bot vende sozinho e avisa Luis só se cliente ficar em dúvida
- Ferramenta: WhatsApp Business simples por enquanto

### Output
"Oi! 👋 Aqui é o Luis, da [Nome da Loja].
Vi que você veio pelo Instagram — fico feliz que achou a gente!
Me conta: você trabalha em home office e está montando seu setup, ou está procurando algo específico?"

Opção A — "Setup completo":
"Ótimo! Tenho um Kit Home Office com suporte ergonômico + mousepad por R$109 (frete grátis). Os dois juntos resolvem postura e conforto de uma vez. Quer ver?"
→ [Sim] → Link do Kit C
→ [Quero ver separado] → apresenta produtos individuais

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
