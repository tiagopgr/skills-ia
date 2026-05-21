---
name: readme-profissional-template
description: Criar um README completo e profissional para repositórios de código — com descrição clara, instruções de instalação, exemplos de uso e guia de contribuição — para que qualquer dev entenda, instale e contribua com o projeto em minutos.
---

# README Profissional (Template)

## Objetivo
Criar um README completo e profissional para repositórios de código — com descrição clara, instruções de instalação, exemplos de uso e guia de contribuição — para que qualquer dev entenda, instale e contribua com o projeto em minutos.

## Quando usar
- Ao criar um novo repositório (open source ou privado)
- Para melhorar um README existente incompleto
- Em projetos que recebem contribuidores novos frequentemente
- Para documentar projetos internos da empresa

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto, stack e funcionalidades
3. Receba o README completo formatado em Markdown
4. Cole no arquivo README.md do repositório

## O Prompt
```
Você é um desenvolvedor que cria READMEs que fazem projetos se destacarem. Você sabe que: (1) um bom README é o marketing do seu código — decide se alguém vai usar ou ignorar, (2) devs têm 30 segundos de atenção — se não entender rápido o que faz, fecha a aba, (3) o README substitui o "me chama no Slack pra explicar" — tudo deve estar documentado, (4) exemplos valem mais que descrições. Seu estilo é claro, direto e com exemplos práticos.

Crie o README profissional para:

**Nome do projeto:** [nome]
**O que faz:** [descrição em 1-2 frases]
**Stack:** [linguagens, frameworks, dependências principais]
**Tipo:** [lib/package, API, web app, CLI tool, template, monorepo]
**Público:** [devs internos, open source, clientes]
**Status:** [produção, beta, em desenvolvimento]
**Licença:** [MIT, Apache 2.0, proprietária]
**Funcionalidades principais:** [liste 3-5 features]
**Como instalar:** [npm install, pip install, docker, clone]
**Como rodar:** [comandos para rodar local]
**Variáveis de ambiente:** [quais são necessárias]
**Testes:** [como rodar testes]

Entregue o README completo:

**1. Header** - Nome, descrição, badges, screenshot/GIF
**2. Highlights** - 3-5 features principais
**3. Quick Start** - Do zero ao funcionando em 4-5 comandos
**4. Instalação detalhada** - Pré-requisitos, passo a passo, .env
**5. Uso/Exemplos** - 2-3 exemplos práticos com código
**6. API/Comandos** - Métodos, endpoints ou comandos disponíveis
**7. Configuração** - Tabela de opções disponíveis
**8. Estrutura do projeto** - Árvore de diretórios com descrições
**9. Desenvolvimento** - Setup de dev, testes, padrões de código
**10. Contribuição** - Como contribuir, convenções, processo de PR
**11. FAQ** - 3-5 problemas comuns e soluções
**12. Licença e créditos**
```

## Exemplo de uso

### Input
Projeto: "fastqueue" — lib TypeScript para gerenciar filas em memória
Stack: TypeScript, Node.js
Tipo: npm package (open source)
Features: filas com prioridade, retry automático com backoff, dead-letter queue, métricas

### Output
# fastqueue

Lightweight in-memory queue for Node.js with retry, backoff, and dead-letter support.

[![npm version](https://img.shields.io/npm/v/fastqueue)](https://www.npmjs.com/package/fastqueue)
[![CI](https://github.com/user/fastqueue/actions/workflows/ci.yml/badge.svg)](https://github.com/user/fastqueue/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Quick Start

```bash
npm install fastqueue
```

```typescript
import { Queue } from 'fastqueue';

const queue = new Queue({
  concurrency: 5,
  retries: 3,
  backoff: 'exponential',
});

queue.add(async (job) => {
  await sendEmail(job.data.to, job.data.body);
});

queue.push({ to: 'user@email.com', body: 'Olá!' });
```

---
**Tags:** Iniciante | Template | Código, Dev & Automação
