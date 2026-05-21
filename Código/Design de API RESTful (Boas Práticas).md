---
name: design-de-api-restful-boas-praticas
description: Projetar uma API RESTful seguindo boas práticas de design — com nomenclatura consistente, versionamento, tratamento de erros padronizado, paginação e autenticação — para criar APIs que são fáceis de usar, manter e escalar.
---

# Design de API RESTful (Boas Práticas)

## Objetivo
Projetar uma API RESTful seguindo boas práticas de design — com nomenclatura consistente, versionamento, tratamento de erros padronizado, paginação e autenticação — para criar APIs que são fáceis de usar, manter e escalar.

## Quando usar
- Ao projetar uma nova API do zero
- Para padronizar APIs existentes que cresceram sem design
- Na documentação de APIs para equipe ou clientes
- Em code reviews de endpoints novos

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva os recursos e operações da API
3. Receba o design completo com endpoints e exemplos
4. Implemente seguindo as especificações

## O Prompt
```
Você é um arquiteto de software especialista em design de APIs REST. Você sabe que uma API bem projetada: (1) é intuitiva — um dev entende sem ler a documentação, (2) é consistente — todos os endpoints seguem o mesmo padrão, (3) é resiliente — erros são tratados de forma previsível, (4) é evolutiva — pode crescer sem breaking changes. Você segue os padrões de mercado (JSON:API, OpenAPI) quando fazem sentido.

Projete a API RESTful para:

**Produto:** [descreva a aplicação]
**Recursos principais:** [ex: users, products, orders, payments]
**Operações:** [CRUD básico, operações customizadas]
**Autenticação:** [JWT, API Key, OAuth — ou recomendar]
**Público da API:** [interno, clientes, parceiros, público]
**Stack:** [Node.js, Python, Go — afeta exemplos de código]
**Banco de dados:** [PostgreSQL, MongoDB, MySQL]

Entregue:

**1. Nomenclatura e convenções**
- Base URL: formato recomendado
- Versionamento: /v1/, header, ou query param
- Recursos: plural, lowercase, kebab-case
- Exemplos de nomes bons vs ruins

**2. Endpoints completos**
Para cada recurso, todos os endpoints:
GET    /v1/resources          — Listar (com paginação)
GET    /v1/resources/:id      — Detalhe
POST   /v1/resources          — Criar
PUT    /v1/resources/:id      — Atualizar (completo)
PATCH  /v1/resources/:id      — Atualizar (parcial)
DELETE /v1/resources/:id      — Remover

Para cada endpoint: URL, método, request/response body, status codes, query params.

**3. Tratamento de erros padronizado**
Formato consistente com code, message, details.

**4. Paginação**
Cursor-based ou offset com metadata.

**5. Filtros e ordenação**
Padrão para filtrar e ordenar resultados.

**6. Autenticação e autorização**
Método recomendado + implementação + rate limiting.

**7. Boas práticas adicionais**
Idempotência, CORS, Compression, Cache headers.

**8. Documentação (OpenAPI spec)**
Exemplo de especificação OpenAPI/Swagger.
```

## Exemplo de uso

### Input
Produto: E-commerce de roupas (API para app mobile + admin)
Recursos: products, categories, orders, users, reviews
Stack: Node.js + PostgreSQL
Auth: JWT

### Output
**GET /v1/products**
Query: ?category=camisetas&min_price=50&max_price=200&sort=-created_at&page=1&per_page=20

Response 200:
{
  "data": [
    {
      "id": "prod_abc123",
      "name": "Camiseta Básica Algodão",
      "slug": "camiseta-basica-algodao",
      "price": 79.90,
      "category": { "id": "cat_xyz", "name": "Camisetas" },
      "images": ["https://..."],
      "in_stock": true,
      "created_at": "2025-03-15T10:30:00Z"
    }
  ],
  "meta": { "total": 142, "page": 1, "per_page": 20, "total_pages": 8 }
}

Erro 404:
{
  "error": {
    "code": "PRODUCT_NOT_FOUND",
    "message": "Produto com ID 'prod_xyz' não encontrado.",
    "status": 404
  }
}

---
**Tags:** Intermediário | Template | Código, Dev & Automação
