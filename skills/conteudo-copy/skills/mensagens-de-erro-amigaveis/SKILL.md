---
name: mensagens-de-erro-amigaveis
description: Criar mensagens de erro que informam o problema com clareza, não assustam o usuário, e guiam para a solução — transformando momentos de frustração em experiências que reforçam a confiança na marca.
---

# Mensagens de Erro Amigáveis

## Objetivo
Criar mensagens de erro que informam o problema com clareza, não assustam o usuário, e guiam para a solução — transformando momentos de frustração em experiências que reforçam a confiança na marca.

## Quando usar
- Ao desenvolver interfaces de apps, sites e plataformas
- Em formulários (validação de campos)
- Em telas de erro do sistema (404, 500, timeout)
- Em fluxos de pagamento e checkout

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Liste os cenários de erro do seu produto
3. Receba mensagens de erro humanizadas e úteis
4. Substitua as mensagens genéricas ou técnicas

## O Prompt
```
Você é um UX Writer especialista em mensagens de erro. Uma mensagem ruim ("Erro 422") gera frustração e abandono. Uma boa mensagem: (1) diz o que aconteceu em linguagem humana, (2) explica por que, (3) diz exatamente o que fazer, (4) mantém o tom da marca.

Crie mensagens de erro amigáveis para:

**Produto/App:** [descreva]
**Tom da marca:** [formal, casual, divertido, técnico, gentil]
**Público:** [quem vai ver as mensagens]

**Cenários de erro:**
1. [ex: "Email inválido no formulário"]
2. [ex: "Senha não atende os requisitos"]
3. [ex: "Pagamento recusado"]
4. [ex: "Página não encontrada (404)"]
5. [ex: "Servidor fora do ar (500)"]
(liste de 5 a 15 cenários)

Para CADA cenário, entregue:

**Mensagem principal** (3 opções):
- Tom informativo
- Tom empático
- Tom leve (humor sutil, se contexto permitir)

**Ação sugerida:** O que o usuário deve fazer

**Texto técnico para log/suporte**

**Anti-patterns:** O que NÃO escrever e por quê

Ao final: Guia de tom para erros + Template padrão + Palavras proibidas
```

## Exemplo de uso

### Input
Produto: Plataforma de cursos online
Tom: Casual e encorajador
Cenários: 1) Email já cadastrado 2) Pagamento recusado 3) Vídeo não carrega 4) Página 404

### Output
**Cenário 2 — Pagamento recusado:**
- Informativo: "Não conseguimos processar seu pagamento. Verifique os dados do cartão ou tente outro método."
- Empático: "Ops, o pagamento não foi aprovado — não se preocupe, seus dados estão seguros. Vamos tentar de novo?"
- Leve: "Seu cartão disse 'agora não'. Pode revisar os dados ou testar outro cartão?"

Ação: Botão "Tentar novamente" + link "Usar outro cartão" + link "Preciso de ajuda"

Anti-pattern: Nunca diga "Transação recusada pelo operador" — parece culpa do usuário e usa jargão técnico.

---
**Tags:** Iniciante | Template | Conteúdo & Copy
