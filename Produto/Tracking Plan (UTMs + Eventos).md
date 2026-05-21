---
name: tracking-plan-utms-eventos
description: Criar um plano de tracking completo — definindo UTMs padronizadas para todas as campanhas e eventos para rastreamento no site/app — para que a empresa saiba exatamente de onde vem cada lead e cada venda.
---

# Tracking Plan (UTMs + Eventos)

## Objetivo
Criar um plano de tracking completo — definindo UTMs padronizadas para todas as campanhas e eventos para rastreamento no site/app — para que a empresa saiba exatamente de onde vem cada lead e cada venda.

## Quando usar
- Ao estruturar analytics do zero (Google Analytics 4, Mixpanel)
- Quando os dados de origem dos leads estão confusos
- Antes de lançar campanhas pagas (padronizar UTMs)
- Para resolver o problema de 'não sei de onde veio essa venda'

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva seus canais, campanhas e ferramentas
3. Receba o tracking plan completo com padrões
4. Implemente e garanta que toda a equipe siga o padrão

## O Prompt
```
Você é um analista de dados que sabe que dados ruins levam a decisões ruins. A maioria das empresas tem analytics configurado mas: (1) UTMs inconsistentes, (2) eventos importantes não rastreados, (3) não consegue atribuir venda ao canal correto.

Crie o tracking plan para:

**Empresa:** [tipo de negócio]
**Site/App:** [URL]
**Ferramenta de analytics:** [GA4, Mixpanel, Amplitude]
**Canais de marketing ativos:** [Google Ads, Facebook, Email, etc.]
**Ações importantes no site:** [compra, cadastro, download, agendamento]
**CRM/Plataforma de vendas:** [HubSpot, Pipedrive, Hotmart]

Entregue: Padrão de UTMs (convenção de nomenclatura), Tabela de UTMs por canal, Eventos para rastrear (conversão, engajamento, funil), Dashboard de acompanhamento, Checklist de implementação, Governança de dados.
```

## Exemplo de uso

### Input
Empresa: E-commerce de cosméticos
Analytics: GA4
Canais: Facebook Ads, Google Ads, Instagram orgânico, Email (Mailchimp), Blog
Ações: Compra, adicionar ao carrinho, cadastro newsletter

### Output
Padrão: utm_source=plataforma&utm_medium=tipo&utm_campaign=AAAA-MM-nome

| Canal | Source | Medium | Campaign | Exemplo |
| Facebook Ads | facebook | cpc | 2025-03-lancamento-verao | ?utm_source=facebook&utm_medium=cpc&utm_campaign=2025-03-lancamento-verao |
| Email | mailchimp | email | 2025-03-newsletter | ?utm_source=mailchimp&utm_medium=email&utm_campaign=2025-03-newsletter |

Eventos GA4:
- view_item → parâmetros: item_name, item_category, price
- add_to_cart → parâmetros: item_name, quantity, value
- purchase → parâmetros: transaction_id, value, items

---
**Tags:** Intermediário | Template | Produto, E-commerce & SaaS
