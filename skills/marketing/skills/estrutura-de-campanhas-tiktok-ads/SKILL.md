---
name: estrutura-de-campanhas-tiktok-ads
description: Criar a estrutura completa de campanhas de TikTok Ads para e-commerce de produto físico — com arquitetura de campanha/grupo de anúncio/criativo, configuração de público, estratégia de lance, pixel events e organização para testes — para maximizar a eficiência do gasto e o aprendizado do algoritmo. TikTok Ads tem lógica diferente do Meta Ads, e estrutura errada custa caro.
---

# Estrutura de Campanhas TikTok Ads

## Objetivo
Criar a estrutura completa de campanhas de TikTok Ads para e-commerce de produto físico — com arquitetura de campanha/grupo de anúncio/criativo, configuração de público, estratégia de lance, pixel events e organização para testes — para maximizar a eficiência do gasto e o aprendizado do algoritmo. TikTok Ads tem lógica diferente do Meta Ads, e estrutura errada custa caro.

## Quando usar
- Para criar a estrutura inicial de campanhas de TikTok Ads do zero
- Para reorganizar campanhas existentes que estão com performance instável
- Ao querer implementar uma estrutura de testes de criativos no TikTok
- Para entender as diferenças de configuração entre TikTok Ads e Meta Ads

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o produto, o budget e os objetivos das campanhas
3. Receba a estrutura completa com configurações específicas
4. Configure no TikTok Ads Manager seguindo a estrutura recomendada

## O Prompt
```
Você é um especialista em TikTok Ads para e-commerce DTC, com foco no mercado europeu (França, Bélgica, Suíça). Seus princípios: (1) TikTok Ads funciona melhor com menos grupos de anúncio e mais criativos por grupo — ao contrário do Meta, o algoritmo do TikTok é mais forte que o targeting manual, então deixe o algoritmo trabalhar com públicos mais amplos, (2) a fase de aprendizado do TikTok precisa de ~50 eventos de otimização em 7 dias — com budget baixo, otimizar por Add to Cart (evento mais frequente) pode ser melhor do que otimizar por Purchase direto, (3) o TikTok tem "creative fatigue" mais rápido do que o Meta — um criativo que performa bem costuma durar 1-2 semanas antes de começar a degradar, então o pipeline de novos criativos deve ser constante, (4) Spark Ads (impulsionar conteúdo orgânico) frequentemente tem CPM menor e mais confiança do que Dark Posts — se você tem conta TikTok orgânica, teste Spark Ads.

**Produto e preço:** [perfume, €45]
**Budget diário total para TikTok:** [valor]
**Objetivo de conversão:** [Purchase / Add to Cart / Initiate Checkout]
**Criativos disponíveis:** [quantos e que tipos]
**Conta TikTok orgânica:** [tem / não tem]
**Pixel TikTok:** [instalado e events configurados? quais events?]
**Mercados alvo:** [France / Belgique / Suisse / outros]
**Fase atual:** [testando / otimizando / escalando]

Entregue:

**1. Estrutura de campanhas recomendada**
Quantas campanhas, quantos grupos de anúncio por campanha, quantos criativos por grupo — com justificativa.

**2. Configuração de cada campanha**
Para cada campanha: objetivo, estratégia de lance, budget (campanha ou grupo), países, idioma, dispositivos.

**3. Configuração de públicos por grupo**
Grupo de aquisição amplo: configurações sugeridas.
Grupo de interesses: quais interesses selecionar para perfume de nicho masculino na França.
Grupo de retargeting (se volume suficiente): configuração.

**4. Configuração de pixel e eventos**
Quais eventos configurar, em que ordem de prioridade, e como verificar se estão disparando corretamente.

**5. Rotina de manutenção semanal**
O que verificar toda semana no TikTok Ads Manager — em 15 minutos — para manter a performance.
```

## Exemplo de uso

### Input
- Produto: perfume masculino nicho €45
- Budget TikTok: €15/dia (~€450/mês)
- Objetivo: Purchase (se pixel tiver dados suficientes) ou ATC
- Criativos: 3 vídeos de 30s
- Conta TikTok orgânica: sim
- Pixel: instalado, PageView e ATC confirmados, Purchase em verificação
- Mercados: France, Belgique
- Fase: testando

### Output
```
CAMPANHA 1 — Conversão / Aquisição Fria
├── Budget: €10/dia (CBO no nível campanha)
├── Grupo 1A — Broad (sem interesses) — 3 criativos
│   └── França + Bélgica / Homens 22-45 / Sem interesse
└── Grupo 1B — Interesses perfume — 3 criativos
    └── Interesses: Perfume, Luxury goods, Fashion menswear

CAMPANHA 2 — Spark Ads / Aquecimento
├── Budget: €5/dia
└── Grupo 2A — Impulsionar melhor post orgânico atual
    └── Objetivo: Video Views ou Traffic → pixel aprende

Fase atual: otimizar para ATC (evento mais frequente com €15/dia)
Quando tiver 50 ATC em 7 dias: mudar otimização para Purchase
```

---
**Tags:** Avançado | Template | Marketing, Vendas & Publicidade
