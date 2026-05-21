---
name: pipeline-cicd-github-actions
description: Criar um pipeline de CI/CD completo com GitHub Actions — automatizando testes, build, linting e deploy — para que cada push/PR seja validado automaticamente e deploys aconteçam de forma segura e consistente.
---

# Pipeline CI/CD (GitHub Actions)

## Objetivo
Criar um pipeline de CI/CD completo com GitHub Actions — automatizando testes, build, linting e deploy — para que cada push/PR seja validado automaticamente e deploys aconteçam de forma segura e consistente.

## Quando usar
- Ao configurar CI/CD pela primeira vez no projeto
- Para automatizar testes que a equipe esquece de rodar
- Na padronização do processo de deploy
- Quando deploys manuais causam problemas

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto, stack e processo de deploy
3. Receba o workflow completo do GitHub Actions
4. Configure no repositório (.github/workflows/)

## O Prompt
```
Você é um engenheiro DevOps que configura pipelines de CI/CD robustos e simples. Seus princípios: (1) pipeline rápido — se demora mais de 10 min, o dev vai ignorar, (2) feedback claro — quando falha, a mensagem deve dizer exatamente o que deu errado, (3) ambientes separados — staging antes de produção, sempre, (4) rollback fácil — deve ser possível voltar em 1 minuto.

Crie o pipeline de CI/CD para:

**Projeto:** [tipo — web app, API, mobile, monorepo]
**Stack:** [ex: Next.js, Node.js, Python/Django, Go]
**Repositório:** [GitHub — monorepo ou single]
**Testes:** [Jest, pytest, Go test — quais existem]
**Linting:** [ESLint, Prettier, Black — quais usa]
**Build:** [como faz build — npm run build, docker build, etc.]
**Deploy:** [onde deploya — Vercel, AWS, Railway, Docker, Kubernetes]
**Ambientes:** [staging, production, preview]
**Branches:** [main = prod? develop = staging? feature branches?]
**Banco de dados:** [precisa de migration no deploy?]
**Secrets:** [variáveis de ambiente necessárias]

Entregue:

**1. Estratégia de CI/CD** - Diagrama do fluxo completo
**2. Workflow de CI (Pull Request)** - YAML completo para .github/workflows/ci.yml
**3. Workflow de CD (Deploy)** - YAML para deploy staging/prod
**4. Workflow de Preview** - Deploy automático para cada PR
**5. Configuração de secrets** - Lista de secrets necessárias
**6. Branch protection rules** - Configurações recomendadas
**7. Monitoramento pós-deploy** - Health check e alertas
**8. Otimizações** - Cache, paralelização, skip CI
```

## Exemplo de uso

### Input
Projeto: API Node.js (Express + TypeScript)
Testes: Jest (unit + integration)
Linting: ESLint + Prettier
Deploy: Docker → AWS ECS
Branches: main = prod, develop = staging
DB: PostgreSQL (precisa migration com Prisma)

### Output
name: CI
on:
  pull_request:
    branches: [main, develop]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run format:check

  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: test
          POSTGRES_PASSWORD: test
        ports: ['5432:5432']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npx prisma migrate deploy
        env:
          DATABASE_URL: postgresql://postgres:test@localhost:5432/test
      - run: npm test -- --coverage

---
**Tags:** Intermediário | Template | Código, Dev & Automação
