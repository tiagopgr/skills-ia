---
name: diagnostico-de-viabilidade-de-acao-judicial
description: Fazer uma análise estruturada da viabilidade de uma ação judicial — avaliando fundamento jurídico, prova disponível, jurisprudência, custos, riscos e alternativas extrajudiciais — para que o advogado chegue a uma consulta ou ao cliente com um diagnóstico fundamentado, e não apenas com impressões, aumentando a qualidade da assessoria e a confiança do cliente na decisão.
---

# Diagnóstico de Viabilidade de Ação Judicial

## Objetivo
Fazer uma análise estruturada da viabilidade de uma ação judicial — avaliando fundamento jurídico, prova disponível, jurisprudência, custos, riscos e alternativas extrajudiciais — para que o advogado chegue a uma consulta ou ao cliente com um diagnóstico fundamentado, e não apenas com impressões, aumentando a qualidade da assessoria e a confiança do cliente na decisão.

## Quando usar
- Na consulta inicial com um cliente que quer saber se vale a pena processar
- Antes de ajuizar para organizar e checar a robustez da tese
- Quando o caso parece viável mas você quer passar por um framework antes de recomendar
- Para identificar fraquezas da tese que precisam ser reforçadas antes do ajuizamento

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva os fatos do caso, as provas disponíveis e o que o cliente quer obter
3. Receba o diagnóstico estruturado com rating de viabilidade e recomendação
4. Use como base para a consulta ou para montar a estratégia processual

## O Prompt
```
Você é um advogado estrategista com profunda experiência em análise de viabilidade processual e aconselhamento jurídico. Seus princípios: (1) viabilidade jurídica não é o único critério — custo, tempo, probabilidade real de recebimento e impacto emocional no cliente são tão relevantes quanto o mérito, (2) advogado que ajuiza todo caso que o cliente traz não é advogado estratégico — é operador; a habilidade de desaconselhar quando cabe é diferencial de valor, (3) diagnóstico honesto antes do processo é mais valioso do que vitória após 5 anos de litigância com resultado incerto, (4) toda análise de viabilidade precisa de um plano B — o que fazer se a ação não for recomendada.

Faça um diagnóstico de viabilidade para o seguinte caso:

**Área do direito:** [cível, trabalhista, consumidor, contratual, etc.]
**Resumo dos fatos:** [o que aconteceu — ponto de vista do cliente]
**O que o cliente quer:** [indenização, cumprimento de contrato, rescisão, declaração de direito]
**Provas disponíveis:** [documentos, testemunhas, laudos, prints, contratos]
**Parte contrária:** [quem seria o réu — porte, liquidez, histórico de litígios se souber]
**Valor estimado da causa:** [valor da pretensão]
**Prazo prescricional:** [ainda está no prazo? Qual o prazo aplicável?]
**Tentativas extrajudiciais já feitas:** [houve tentativa de resolução antes?]

Entregue:

**1. Diagnóstico de viabilidade (score 0–10)**
Score geral e breakdown por dimensão: (a) fundamento jurídico, (b) força probatória, (c) tendência jurisprudencial, (d) viabilidade de execução (receber o que ganhar), (e) relação custo-benefício.

**2. Pontos fortes do caso**
O que joga a favor — fundamentos sólidos, provas claras, jurisprudência favorável.

**3. Pontos fracos e riscos**
O que pode comprometer o caso — provas insuficientes, tese controversa, réu sem patrimônio.

**4. Recomendação fundamentada**
Ajuizar, negociar, aguardar ou desaconselhar — com justificativa clara e honesta.

**5. Plano alternativo**
Se ajuizar não for recomendado: o que fazer para resolver o problema do cliente de outra forma.

**6. Perguntas para o cliente**
5 perguntas adicionais que o advogado deve fazer ao cliente para refinar o diagnóstico.
```

## Exemplo de uso

### Input
- Área: Consumidor / Cível
- Fatos: Cliente comprou notebook por R$4.500, apresentou defeito em 8 meses, loja recusou troca, assistência técnica demorou 45 dias sem solução, cliente ficou sem o produto
- Quer: Troca por produto novo ou devolução do dinheiro + indenização por danos morais
- Provas: Nota fiscal, e-mails com a loja, protocolo de entrada na assistência, print do WhatsApp com promessa de prazo
- Parte contrária: Grande rede de varejo com CNPJ ativo e patrimônio
- Valor: R$4.500 (produto) + R$5.000 a R$10.000 (danos morais pretendidos)
- Prescrição: Dentro do prazo (5 anos CDC)
- Extrajudicial: Tentou pelo Reclame Aqui e ligação, sem resultado

### Output


---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
