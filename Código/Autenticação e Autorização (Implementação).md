---
name: autenticacao-e-autorizacao-implementacao
description: Implementar um sistema completo de autenticação e autorização — com login, registro, tokens JWT, refresh tokens, roles e permissões — seguindo boas práticas de segurança, para proteger os recursos da aplicação.
---

# Autenticação e Autorização (Implementação)

## Objetivo
Implementar um sistema completo de autenticação e autorização — com login, registro, tokens JWT, refresh tokens, roles e permissões — seguindo boas práticas de segurança, para proteger os recursos da aplicação.

## Quando usar
- Ao implementar auth em uma nova aplicação
- Para substituir um sistema de auth inseguro ou improvisado
- Quando precisa adicionar roles/permissões a um sistema existente
- Em code reviews de fluxos de autenticação

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a stack, requisitos de auth e tipos de usuário
3. Receba a implementação completa com código
4. Adapte ao seu projeto e implemente

## O Prompt
```
Você é um engenheiro de segurança que implementa sistemas de autenticação robustos. Seus princípios: (1) nunca invente criptografia — use bibliotecas comprovadas (bcrypt, argon2, jose), (2) defesa em profundidade — múltiplas camadas de proteção, (3) princípio do menor privilégio — cada role tem acesso mínimo necessário, (4) tokens com vida curta — access token expira rápido, refresh token renova, (5) falhe de forma segura — em caso de dúvida, negar acesso.

Implemente o sistema de autenticação para:

**Stack:** [ex: Node.js/Express, Python/FastAPI, Go/Gin]
**Banco de dados:** [PostgreSQL, MongoDB, MySQL]
**ORM:** [Prisma, SQLAlchemy, GORM]
**Tipo de auth:** [JWT, session-based, OAuth2 — ou recomendar]
**Tipos de usuário:** [ex: admin, manager, user, viewer]
**Permissões:** [o que cada tipo pode fazer]
**Requisitos especiais:** [2FA, OAuth social, magic link, API keys]
**Frontend:** [SPA, SSR, mobile — afeta onde guardar tokens]

Entregue:

**1. Arquitetura do sistema** - Diagrama do fluxo completo
**2. Schema do banco** - Tabelas users, refresh_tokens, roles
**3. Endpoints da API** - register, login, refresh, logout, forgot/reset password
**4. Middleware de autenticação** - Validar JWT, injetar usuário
**5. Middleware de autorização** - Verificar roles e permissões
**6. Segurança implementada** - Checklist de boas práticas
**7. Código completo** - Implementação funcional de cada componente
**8. Testes** - Cenários críticos de auth
```

## Exemplo de uso

### Input
Stack: Node.js/Express + TypeScript
Banco: PostgreSQL com Prisma
Auth: JWT (access + refresh)
Roles: admin (tudo), editor (CRUD conteúdo), viewer (leitura)
Frontend: React SPA

### Output
import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';

interface JwtPayload {
  userId: string;
  role: string;
}

export function authenticate(req: Request, res: Response, next: NextFunction) {
  const header = req.headers.authorization;
  if (!header?.startsWith('Bearer ')) {
    return res.status(401).json({
      error: { code: 'MISSING_TOKEN', message: 'Token de autenticação não fornecido.' }
    });
  }

  const token = header.split(' ')[1];

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET!) as JwtPayload;
    req.user = { id: payload.userId, role: payload.role };
    next();
  } catch (err) {
    if (err instanceof jwt.TokenExpiredError) {
      return res.status(401).json({
        error: { code: 'TOKEN_EXPIRED', message: 'Token expirado. Use o refresh token.' }
      });
    }
    return res.status(401).json({
      error: { code: 'INVALID_TOKEN', message: 'Token inválido.' }
    });
  }
}

export function authorize(...allowedRoles: string[]) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({
        error: { code: 'FORBIDDEN', message: 'Sem permissão para acessar este recurso.' }
      });
    }
    next();
  };
}

// Uso: router.get('/admin/users', authenticate, authorize('admin'), listUsers);

---
**Tags:** Intermediário | Template | Código, Dev & Automação
