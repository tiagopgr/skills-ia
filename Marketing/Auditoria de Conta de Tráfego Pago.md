---
name: auditoria-de-conta-de-trafego-pago
description: Conduzir uma auditoria estruturada de uma conta de Meta Ads ou Google Ads — analisando estrutura, segmentação, criativos, orçamento, métricas e configurações técnicas — para entregar ao cliente (ou usar internamente) um diagnóstico claro do que está errado, o que está custando dinheiro desnecessariamente e quais são as alavancas de melhoria com maior potencial de impacto no resultado.
---

# Auditoria de Conta de Tráfego Pago

## Objetivo
Conduzir uma auditoria estruturada de uma conta de Meta Ads ou Google Ads — analisando estrutura, segmentação, criativos, orçamento, métricas e configurações técnicas — para entregar ao cliente (ou usar internamente) um diagnóstico claro do que está errado, o que está custando dinheiro desnecessariamente e quais são as alavancas de melhoria com maior potencial de impacto no resultado.

## Quando usar
- Ao assumir uma conta nova que já tem histórico e precisa ser diagnosticada
- Quando os resultados de um cliente caíram sem motivo aparente
- Para apresentar valor em uma primeira reunião com um prospect
- Antes de reformular a estratégia de um cliente existente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados da conta (métricas, estrutura, prints ou descrições)
3. Receba o diagnóstico com os problemas identificados, causas prováveis e recomendações
4. Use como base para a apresentação de auditoria ou para o plano de ação interno

## O Prompt
```
Você é um especialista sênior em tráfego pago com profundo conhecimento em Meta Ads e Google Ads, especializado em diagnosticar contas com baixa performance e identificar oportunidades de escala. Seus princípios: (1) problema de resultado tem causa em estrutura, segmentação, criativo ou oferta — nessa ordem de diagnóstico; (2) conta bagunçada custa mais caro mesmo com bom orçamento; (3) métricas de vaidade (impressões, cliques) escondem o real problema — sempre ir direto ao CPL, CPA e ROAS; (4) uma boa auditoria entrega não só o problema, mas o caminho prioritário de solução.

Conduza uma auditoria completa da seguinte conta de tráfego:

**Plataforma:** [Meta Ads / Google Ads / ambas]
**Objetivo da conta:** [ex: geração de leads, vendas, tráfego para site]
**Período analisado:** [ex: últimos 30 dias, últimos 90 dias]
**Orçamento mensal:** [valor]
**Métricas atuais:** [cole ou descreva: CPL, CPA, CTR, CPC, ROAS, taxa de conversão, alcance]
**Estrutura atual:** [descreva campanhas existentes, segmentações usadas, tipos de criativos]
**Resultado esperado vs. resultado atual:** [meta que deveria bater vs. o que está atingindo]
**Histórico de mudanças recentes:** [o que foi alterado na conta recentemente]

Entregue:

**1. Diagnóstico geral**
Nota de saúde da conta (1-10) com justificativa em 3 linhas.

**2. Problemas identificados por categoria**
Para cada categoria (estrutura, segmentação, criativos, configuração técnica, oferta): lista de problemas com nível de impacto (alto/médio/baixo) e evidência nos dados.

**3. Principais oportunidades**
Top 5 alavancas que, se corrigidas, teriam maior impacto no resultado — ordenadas por impacto estimado.

**4. Plano de ação priorizado**
Tabela com: ação | categoria | impacto estimado | esforço | prazo recomendado.

**5. O que está funcionando (não mexer)**
Campanhas, públicos ou criativos com bom desempenho que devem ser preservados ou escalados.

**6. Projeção de melhoria**
Se as top 3 ações forem implementadas, qual resultado pode ser esperado em 30 dias (com premissas explícitas).
```

## Exemplo de uso

### Input
- Plataforma: Meta Ads
- Objetivo: Geração de leads (agendamento de consulta)
- Período: Últimos 30 dias
- Orçamento: R$5.000/mês
- Métricas: CPL R$87, CTR 0,8%, CPC R$4,20, taxa de conversão da LP 3,2%
- Estrutura: 1 campanha, 4 conjuntos com públicos sobrepostos, 12 anúncios ativos simultâneos
- Meta: CPL abaixo de R$50
- Mudanças recentes: Duplicaram o orçamento há 3 semanas

### Output
| Categoria | Problema | Impacto |
|-----------|----------|---------|
| Estrutura | 4 conjuntos com sobreposição de público acima de 60% — públicos competindo entre si | Alto |
| Criativos | 12 anúncios ativos sem budget para aprendizado individual — todos em subotimização | Alto |
| Configuração | Duplicação de orçamento sem fase de estabilização — algoritmo reiniciou aprendizado | Alto |
| Oferta | LP com taxa de conversão 3,2% — benchmark do setor é 6-8% para consultas | Médio |
| Segmentação | Públicos amplos sem exclusão de leads já convertidos — custo com reimpressão | Médio |

---
**Tags:** Avançado | Análise | Marketing, Vendas & Publicidade
