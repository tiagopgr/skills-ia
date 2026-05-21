---
name: indicadores-kpi-logistico
description: Definir e estruturar os KPIs (Key Performance Indicators) para qualquer processo logístico ou operacional — com fórmula de cálculo, fonte de dados, frequência de medição, meta, responsável e plano de ação para quando o indicador sair da faixa. Transforma documentos e processos em números rastreáveis, eliminando a gestão por percepção e criando base para decisão baseada em dados.
---

# Indicadores KPI Logístico

## Objetivo
Definir e estruturar os KPIs (Key Performance Indicators) para qualquer processo logístico ou operacional — com fórmula de cálculo, fonte de dados, frequência de medição, meta, responsável e plano de ação para quando o indicador sair da faixa. Transforma documentos e processos em números rastreáveis, eliminando a gestão por percepção e criando base para decisão baseada em dados.

## Quando usar
- Para criar o painel de indicadores de um processo depois de documentá-lo (POP → KPI)
- Quando você não sabe se um processo está funcionando bem ou mal
- Para justificar melhorias com dados em vez de percepção subjetiva
- Ao precisar reportar a performance da operação para liderança ou diretoria

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o processo ou área e o que você quer medir
3. Receba o conjunto de KPIs estruturado com fórmulas e metas de referência
4. Implante a coleta de dados e monitore semanalmente ou mensalmente

## O Prompt
```
Você é um especialista em indicadores de performance para operações logísticas e gestão de armazém. Seus princípios: (1) medir tudo é não medir nada — um processo bem gerenciado tem entre 3 e 7 KPIs, não 20, (2) todo KPI precisa de uma meta (o que é bom), uma faixa de alerta (quando acender o sinal amarelo) e um gatilho de ação (quando agir obrigatoriamente), (3) a fonte de dados do KPI deve ser confiável e de fácil acesso — KPI que depende de coleta manual difícil vai deixar de ser medido em 30 dias, (4) KPIs de processo medem o que acontece durante a execução; KPIs de resultado medem o impacto no negócio — um conjunto saudável tem ambos.

**Processo ou área a monitorar:** [ex: recebimento, separação, expedição, inventário, transporte]
**Objetivo do processo:** [o que o processo deve entregar bem]
**Problemas recorrentes que quer monitorar:** [ex: atraso, divergência, retrabalho, devolução]
**Sistemas disponíveis para coleta de dados:** [WMS, ERP, planilha, controle manual]
**Frequência de gestão:** [revisão diária / semanal / mensal]
**Para quem você vai reportar:** [equipe operacional / supervisão / diretoria]

Entregue:

**1. Conjunto de KPIs sugeridos (5 a 7)**
Para cada KPI: nome, descrição, fórmula de cálculo, unidade de medida, fonte de dados, frequência de medição, meta de referência do mercado logístico.

**2. Dashboard de gestão**
Tabela de acompanhamento semanal/mensal com: KPI, meta, resultado atual, status (verde/amarelo/vermelho) e responsável.

**3. Faixas de desempenho**
Para cada KPI: faixa verde (dentro da meta), faixa amarela (atenção), faixa vermelha (ação imediata) com os valores de corte.

**4. Plano de reação por KPI**
Para cada KPI em vermelho: quem aciona, o que investiga, prazo para plano de ação.

**5. Mapa de causa e efeito**
Relação entre os KPIs — qual indicador de processo explica qual indicador de resultado.
```

## Exemplo de uso

### Input
- Processo: Recebimento de Mercadorias
- Objetivo: receber mercadoria no prazo, sem divergência e com estoque atualizado
- Problemas: divergências de quantidade, atraso no lançamento, NFs rejeitadas
- Sistemas: WMS + planilha de controle
- Frequência: revisão semanal
- Reporta para: supervisor e gerente de operações

### Output
| KPI | Fórmula | Meta | Verde | Amarelo | Vermelho |
|-----|---------|------|-------|---------|----------|
| Taxa de Divergência no Recebimento | (Recebimentos com divergência / Total de recebimentos) × 100 | ≤ 2% | 0–2% | 2,1–5% | > 5% |
| Tempo médio de lançamento de NF | Soma do tempo (chegada → lançamento WMS) / nº de NFs | ≤ 2h | 0–2h | 2–4h | > 4h |
| NFs rejeitadas por erro de digitação | Nº de NFs com erro / Total lançado × 100 | ≤ 1% | 0–1% | 1–3% | > 3% |

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
