---
name: dockerfile-otimizado-multi-stage
description: Criar Dockerfiles otimizados usando multi-stage builds — reduzindo o tamanho da imagem final, melhorando a segurança e acelerando builds — para containers leves, rápidos de deployar e seguros para produção.
---

# Dockerfile Otimizado (Multi-Stage)

## Objetivo
Criar Dockerfiles otimizados usando multi-stage builds — reduzindo o tamanho da imagem final, melhorando a segurança e acelerando builds — para containers leves, rápidos de deployar e seguros para produção.

## Quando usar
- Ao containerizar uma aplicação pela primeira vez
- Quando a imagem Docker está grande demais (>500MB)
- Para melhorar tempo de build e deploy
- Na padronização de containers da equipe

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a stack, dependências e requisitos
3. Receba o Dockerfile otimizado com explicações
4. Teste localmente e integre no pipeline

## O Prompt
```
Você é um engenheiro DevOps que cria Dockerfiles otimizados para produção. Seus princípios: (1) imagens pequenas — cada MB a mais é tempo de deploy desperdiçado, (2) multi-stage builds — separar build de runtime, (3) segurança — nunca rodar como root, (4) cache inteligente — ordenar layers para maximizar cache hits, (5) reproducibilidade — builds devem ser idênticos em qualquer máquina.

Crie o Dockerfile otimizado para:

**Aplicação:** [tipo — API, web app, worker, cron job]
**Stack:** [ex: Node.js 20, Python 3.12, Go 1.22, Java 21]
**Framework:** [ex: Express, FastAPI, Gin, Spring Boot]
**Gerenciador de pacotes:** [npm, yarn, pnpm, pip, poetry, go modules]
**Build command:** [ex: npm run build, go build, mvn package]
**Porta:** [ex: 3000, 8080, 8000]
**Dependências de sistema:** [ex: imagemagick, ffmpeg, sharp, pg_client]
**Arquivos estáticos:** [serve estáticos? precisa de nginx?]
**Variáveis de ambiente:** [em runtime — não hardcodar]
**Health check:** [endpoint ou comando para verificar saúde]

Entregue:

**1. Dockerfile otimizado (multi-stage)** com 3 stages: deps, build, runtime
**2. .dockerignore** completo
**3. Comparação de tamanho** antes vs depois
**4. Boas práticas aplicadas** (checklist)
**5. docker-compose.yml** para desenvolvimento
**6. Comandos úteis** para build, run, debug
```

## Exemplo de uso

### Input
Aplicação: API REST
Stack: Node.js 20, TypeScript
Framework: Express
Pacotes: npm
Build: npm run build (tsc → dist/)
Porta: 3000
Health check: GET /health

### Output
# Stage 1: Dependências
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --only=production && \
    cp -R node_modules /prod_modules && \
    npm ci

# Stage 2: Build
FROM node:20-alpine AS build
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Stage 3: Runtime (imagem final)
FROM node:20-alpine AS runtime
WORKDIR /app

RUN addgroup -g 1001 -S appgroup && \
    adduser -S appuser -u 1001 -G appgroup

COPY --from=deps /prod_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY package.json ./

ENV NODE_ENV=production
EXPOSE 3000

USER appuser

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

CMD ["node", "dist/index.js"]

# Tamanho: ~180MB (naïve) → ~85MB (otimizado) — redução de 53%

---
**Tags:** Intermediário | Template | Código, Dev & Automação
