---
name: estrategia-de-escala-de-anuncios
description: Criar um framework completo para escalar campanhas de Facebook Ads e TikTok Ads lucrativas — com critérios claros de quando escalar, como escalar (vertical vs horizontal), quanto subir por vez e como monitorar para não matar a performance ao aumentar o budget. Escalar sem método é a forma mais rápida de transformar uma campanha lucrativa em prejuízo.
---

# Estratégia de Escala de Anúncios

## Objetivo
Criar um framework completo para escalar campanhas de Facebook Ads e TikTok Ads lucrativas — com critérios claros de quando escalar, como escalar (vertical vs horizontal), quanto subir por vez e como monitorar para não matar a performance ao aumentar o budget. Escalar sem método é a forma mais rápida de transformar uma campanha lucrativa em prejuízo.

## Quando usar
- Quando uma campanha está com ROAS acima do break-even e quer crescer o volume de vendas
- Para decidir entre escalar o budget (vertical) ou criar novos conjuntos/criativos (horizontal)
- Quando subiu o budget e a performance caiu — para entender o que aconteceu
- Para criar uma rotina de escala que possa ser executada semanalmente com segurança

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe as campanhas ativas, os resultados e o objetivo de escala
3. Receba o plano de escala com passos sequenciais e alertas de risco
4. Execute na ordem definida, monitorando diariamente nos primeiros 3 dias

## O Prompt
```
Você é um especialista em media buying e escala de campanhas pagas para e-commerce no Meta Ads e TikTok Ads. Seus princípios: (1) escalar budget direto em mais de 20-30% por vez força o algoritmo a sair da fase de aprendizado — o CPA sobe, o ROAS cai e parece que a campanha "quebrou", (2) escala horizontal (novos conjuntos, novos públicos, novos criativos) é mais estável do que escala vertical (subir budget na mesma campanha) — mas escala horizontal exige mais criativos vencedores prontos, (3) antes de escalar, o criativo vencedor precisa estar identificado — escalar com múltiplos criativos sem saber qual performa dilui o aprendizado, (4) a regra de ouro da escala: dobrar o budget só quando o ROAS sustentou acima do break-even por 5-7 dias consecutivos — não por 1 bom dia.

**Campanha(s) para escalar:**
- Objetivo: [conversão, etc.]
- Budget atual: [valor diário]
- ROAS médio últimos 7 dias: [valor]
- Break-even ROAS: [seu threshold]
- Criativo(s) vencedor(es): [descreva os que estão performando]
- Fase de aprendizado: [concluída / em andamento]

**Objetivo de escala:**
- Budget alvo: [onde quer chegar em euros/dia]
- Prazo desejado: [ex: dobrar em 30 dias]
- Risco tolerado: [conservador / moderado / agressivo]

**Situação das outras alavancas:**
- Criativos prontos para rodar: [quantos tem em reserve]
- Páginas de produto otimizadas: [sim/não]
- Capacidade de estoque/fulfillment: [limite de pedidos por dia]

Entregue:

**1. Diagnóstico de prontidão para escala**
A campanha está pronta para escalar? Checklist de 8 critérios antes de subir budget.

**2. Plano de escala semana a semana**
Quanto subir por semana, qual método usar (CBO adjustment / duplicar conjunto / novo público), critério de avanço para a próxima semana.

**3. Método de escala recomendado**
Vertical (subir budget) vs horizontal (novos conjuntos/criativos) — recomendação para o contexto específico.

**4. Alertas e sinais de reversão**
Quais métricas monitorar diariamente durante a escala e quando reverter (pausar ou voltar ao budget anterior).

**5. Estrutura de campanha para alta escala**
Como reorganizar a estrutura de campanhas quando o budget superar €X/dia — para suportar volume maior sem instabilidade.
```

## Exemplo de uso

### Input
- Campanha: conversão, 1 CBO com 3 conjuntos
- Budget atual: €30/dia
- ROAS médio 7 dias: 3,1x (acima do break-even de 2,48x)
- Criativo vencedor: Vídeo V1 com hook de durabilidade
- Aprendizado: concluído (>50 eventos na janela)
- Budget alvo: €100/dia em 30 dias
- Prazo: 30 dias
- Risco: moderado
- Criativos em reserve: 2 vídeos não testados
- Estoque: ilimitado (dropshipping/sob demanda)

### Output
| Semana | Budget Diário | Ação | Critério de Avanço |
|--------|-------------|------|-------------------|
| Semana 1 | €30 → €40 | Subir 33% no CBO existente | ROAS ≥ 2,48x por 5 dias |
| Semana 2 | €40 → €55 | Subir 37% no CBO | ROAS ≥ 2,48x por 5 dias |
| Semana 3 | €55 → €75 | Duplicar o CBO vencedor + testar 1 criativo novo no duplicado | ROAS ≥ 2,48x em ambos por 4 dias |
| Semana 4 | €75 → €100 | Consolidar em CBO com budget maior / pausar o underperformer | ROAS consolidado ≥ 2,48x |

---
**Tags:** Avançado | Template | Marketing, Vendas & Publicidade
