---
name: framework-de-analise-de-dados-de-campanha
description: Conduzir uma análise estruturada dos dados de performance de uma campanha — cruzando métricas de funil, identificando padrões de público, criativo e timing — para extrair insights que informam decisões de otimização concretas, não apenas reportar números para o cliente mas interpretar o que eles revelam sobre o comportamento do público e o que fazer a seguir.
---

# Framework de Análise de Dados de Campanha

## Objetivo
Conduzir uma análise estruturada dos dados de performance de uma campanha — cruzando métricas de funil, identificando padrões de público, criativo e timing — para extrair insights que informam decisões de otimização concretas, não apenas reportar números para o cliente mas interpretar o que eles revelam sobre o comportamento do público e o que fazer a seguir.

## Quando usar
- Para a análise semanal ou mensal de qualquer conta de tráfego pago
- Quando os resultados caíram e precisa entender o motivo antes de agir
- Para preparar o relatório de resultados com análise real, não só tabela de dados
- Antes de escalar um orçamento — para garantir que a estrutura aguenta mais verba

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole os dados da campanha (métricas, segmentações, criativos)
3. Receba a análise com interpretação dos dados, hipóteses e recomendações
4. Use para tomar decisões de otimização e para embasar o relatório ao cliente

## O Prompt
```
Você é um analista de dados de performance e especialista em tráfego pago, treinado para ir além dos números e identificar padrões de comportamento de público e criativo que informam decisões estratégicas de otimização. Seus princípios: (1) dado sem contexto é ruído — sempre pergunte "comparado com quê?" antes de concluir; (2) correlação entre métricas revela mais do que cada métrica isolada; (3) a análise precisa terminar com uma decisão clara — insight sem ação é desperdício; (4) quando dois indicadores contradizem, investigar antes de concluir — geralmente há uma variável escondida.

Analise os dados da seguinte campanha:

**Plataforma:** [Meta Ads / Google Ads]
**Objetivo da campanha:** [ex: leads, vendas, agendamentos]
**Período analisado:** [ex: últimas 2 semanas, mês de abril]
**Dados disponíveis:** [cole as métricas — quanto mais detalhado, melhor]
**Segmentações ativas:** [públicos, interesses, lookalikes, retargeting]
**Criativos ativos:** [quantos, quais formatos, resultados por criativo se disponível]
**Contexto externo:** [sazonalidade, mudanças feitas, eventos relevantes]
**Principal dúvida:** [o que você mais quer entender com essa análise]

Entregue:

**1. Diagnóstico geral**
O que os dados revelam em 3 linhas — a história que os números contam.

**2. Análise por nível do funil**
Onde está o gargalo: impressão → clique → LP → conversão — qual etapa está quebrando mais.

**3. Análise de criativos**
Quais criativos performam melhor, o padrão entre os vencedores e o que isso revela sobre o que o público responde.

**4. Análise de público**
Qual segmento converte melhor, qual tem CTR alto mas conversão baixa (problema de oferta/LP) e qual está saturando.

**5. Hipóteses de causa**
3-5 hipóteses sobre por que os resultados estão como estão — com nível de confiança de cada uma.

**6. Plano de ação baseado na análise**
O que testar, o que pausar, o que escalar — com prioridade e justificativa em dados.
```

## Exemplo de uso

### Input
- Plataforma: Meta Ads
- Objetivo: Leads (formulário nativo)
- Período: Últimas 2 semanas
- Dados: CPL semana 1: R$42 | CPL semana 2: R$78 | CTR mantido 1,2% | Taxa de preenchimento do form caiu de 68% para 31%
- Segmentação: Público frio (interesses) + lookalike 2%
- Criativos: 3 ativos — vídeo A (melhor CTR), carrossel B (melhor conversão semana 1), estático C (novo, semana 2)
- Contexto: Adicionaram nova pergunta no formulário nativo na virada da semana 2
- Dúvida: Por que o CPL dobrou se o CTR não mudou?

### Output
| Hipótese | Evidência | Confiança |
|----------|-----------|-----------|
| Nova pergunta no formulário aumentou fricção e reduziu preenchimento de 68% para 31% | CPL dobrou exatamente na semana da mudança do form; CTR inalterado indica que o problema não é criativo | Alta |
| Público do lookalike 2% saturando (frequência alta) | Precisa verificar frequência — se > 3,5, confirma | Média |
| Criativo C novo está consumindo budget sem converter | Verificar distribuição de orçamento e CPL por criativo | Média |

---
**Tags:** Avançado | Análise | SEO, Analítica & Dados
