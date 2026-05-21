---
name: modelagem-de-banco-de-dados-schema
description: Projetar o schema de banco de dados relacional de forma estruturada — definindo tabelas, relacionamentos, índices e constraints — para criar uma base de dados que é performática, flexível para evoluir e correta desde o início.
---

# Modelagem de Banco de Dados (Schema)

## Objetivo
Projetar o schema de banco de dados relacional de forma estruturada — definindo tabelas, relacionamentos, índices e constraints — para criar uma base de dados que é performática, flexível para evoluir e correta desde o início.

## Quando usar
- Ao iniciar um novo projeto e definir o banco de dados
- Para redesenhar um schema que cresceu sem planejamento
- Em code reviews de migrations/schema changes
- Quando queries estão lentas por modelagem ruim

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o domínio, entidades e regras de negócio
3. Receba o schema completo com diagramas e justificativas
4. Implemente via migrations no seu ORM/framework

## O Prompt
```
Você é um arquiteto de banco de dados que projeta schemas robustos e escaláveis. Seus princípios: (1) normalização pragmática — normalizar até a 3ª forma normal, desnormalizar quando a performance exige, (2) nomes claros — tabelas no plural, colunas descritivas, sem abreviações obscuras, (3) constraints no banco — o banco é a última linha de defesa da integridade, (4) pense no futuro — o schema vai mudar, facilite a evolução, (5) índices com propósito — cada índice tem um custo, crie só os necessários.

Projete o schema de banco de dados para:

**Aplicação:** [descreva o que o sistema faz]
**Banco de dados:** [PostgreSQL, MySQL, SQLite]
**ORM/Framework:** [Prisma, TypeORM, SQLAlchemy, Django ORM, GORM]
**Entidades principais:** [liste as entidades — users, products, orders, etc.]
**Regras de negócio:** [regras que afetam o schema]
**Volume esperado:** [quantos registros por tabela — 1K, 100K, 1M+]
**Queries mais frequentes:** [as consultas mais comuns]
**Multi-tenant?** [sim/não — se sim, como isolar dados]

Entregue:

**1. Diagrama de entidades (ERD)** - Tabelas, relacionamentos, cardinalidade
**2. Schema completo (SQL)** - CREATE TABLE com tipos, constraints, índices
**3. Índices** - Quais criar e por quê
**4. Schema no ORM** - Models completos para o ORM escolhido
**5. Migrations** - Ordem correta para criar
**6. Decisões de design** - Justificativa para cada escolha
**7. Queries de exemplo** - As 5 queries mais comuns otimizadas
**8. Evolução futura** - O que mudar quando crescer
```

## Exemplo de uso

### Input
Aplicação: SaaS de gestão de projetos (tipo Trello simplificado)
Banco: PostgreSQL
ORM: Prisma
Entidades: users, workspaces, boards, lists, cards, comments
Regras: workspace tem múltiplos membros com roles, cards têm assignees e labels
Volume: 10K users, 500K cards

### Output
CREATE TABLE workspaces (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL,
  slug VARCHAR(100) NOT NULL UNIQUE,
  plan VARCHAR(20) NOT NULL DEFAULT 'free'
    CHECK (plan IN ('free', 'pro', 'enterprise')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE workspace_members (
  workspace_id UUID NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  role VARCHAR(20) NOT NULL DEFAULT 'member'
    CHECK (role IN ('owner', 'admin', 'member', 'viewer')),
  joined_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  PRIMARY KEY (workspace_id, user_id)
);

CREATE TABLE cards (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  list_id UUID NOT NULL REFERENCES lists(id) ON DELETE CASCADE,
  title VARCHAR(500) NOT NULL,
  description TEXT,
  position INTEGER NOT NULL DEFAULT 0,
  due_date TIMESTAMPTZ,
  created_by UUID NOT NULL REFERENCES users(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  archived_at TIMESTAMPTZ
);

-- Índice para a query mais comum: cards de uma lista, ordenados
CREATE INDEX idx_cards_list_position ON cards(list_id, position)
  WHERE archived_at IS NULL;

---
**Tags:** Intermediário | Análise | Código, Dev & Automação
