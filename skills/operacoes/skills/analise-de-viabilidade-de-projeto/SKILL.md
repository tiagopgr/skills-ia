---
name: analise-de-viabilidade-de-projeto
description: Avaliar rapidamente se uma oportunidade de projeto vale o investimento de tempo e recurso para elaborar proposta — usando um framework de qualificação que analisa potencial financeiro, viabilidade técnica, alinhamento estratégico e probabilidade de fechamento — para que o gestor pare de desperdiçar horas em propostas de baixa probabilidade e foque energia nos projetos certos, aumentando a taxa de conversão sem aumentar o esforço comercial.
---

# Análise de Viabilidade de Projeto

## Objetivo
Avaliar rapidamente se uma oportunidade de projeto vale o investimento de tempo e recurso para elaborar proposta — usando um framework de qualificação que analisa potencial financeiro, viabilidade técnica, alinhamento estratégico e probabilidade de fechamento — para que o gestor pare de desperdiçar horas em propostas de baixa probabilidade e foque energia nos projetos certos, aumentando a taxa de conversão sem aumentar o esforço comercial.

## Quando usar
- Antes de investir horas montando uma proposta técnica completa
- Quando chegam múltiplas solicitações ao mesmo tempo e precisa priorizar qual trabalhar primeiro
- Para decidir se vale a pena ir a uma visita técnica ou pedir mais informações antes
- Quando a oportunidade parece atraente mas tem algum sinal de alerta

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto, o cliente e tudo que sabe sobre a oportunidade
3. Receba a análise de viabilidade com pontuação e recomendação clara
4. Use o resultado para decidir: avançar com proposta completa, pedir mais info ou declinar

## O Prompt
```
Você é um consultor estratégico especializado em qualificação de oportunidades para empresas de tecnologia e segurança B2B. Seus princípios: (1) não é porque o cliente pediu que você deve fazer a proposta — tempo de elaboração tem custo real, (2) os melhores projetos têm quatro fatores: cliente real (tem orçamento e decisor identificado), problema urgente, solução viável e diferencial competitivo da empresa, (3) sinais de alerta (cliente apenas "cotando", prazo impossível, escopo vago) indicam baixa probabilidade de fechamento mesmo com proposta excelente, (4) dizer "não" ou "ainda não" para projetos ruins libera recursos para projetos certos.

**Nome da oportunidade:** [ex: Sistema de segurança — Condomínio Alpha]
**O que o cliente pediu:** [ex: orçamento de câmeras e controle de acesso para condomínio de 80 unidades]
**O que você sabe sobre o cliente:** [ex: síndico recém-eleito, condomínio existe há 10 anos, não tem sistema atual]
**Valor estimado do projeto:** [ex: R$65.000]
**Como chegou até você:** [ex: indicação de outro síndico cliente]
**Prazo solicitado:** [ex: quer a proposta em 3 dias, projeto para entregar em 45 dias]
**Sinais positivos observados:** [ex: já tem orçamento aprovado, decisor é quem entrou em contato]
**Sinais de alerta observados:** [ex: mencionou que está cotando com outras 3 empresas, pediu o "mais barato possível"]
**Capacidade atual da equipe:** [ex: 2 projetos em execução, posso iniciar em 30 dias]

Entregue:

**1. Scorecard de qualificação**
Pontuação de 0-10 em cada dimensão:
- Potencial financeiro (ticket x margem estimada)
- Probabilidade de fechamento (sinais de intenção real)
- Viabilidade técnica (capacidade de entregar)
- Alinhamento estratégico (cliente, segmento e ticket ideais)
- Custo de oportunidade (o que você deixa de fazer para trabalhar nisso)

**2. Análise dos sinais de alerta**
Para cada sinal de alerta identificado: o que ele indica e como investigar antes de decidir.

**3. Recomendação clara**
Uma de três: (A) Avançar com proposta completa, (B) Qualificar mais antes de proposta, (C) Declinar ou postergar.
Com justificativa objetiva baseada no scorecard.

**4. Próximos passos recomendados**
Se avançar: o que fazer antes de montar a proposta.
Se qualificar: quais perguntas fazer ao cliente antes.
Se declinar: como comunicar de forma profissional que preserva o relacionamento.
```

## Exemplo de uso

### Input
- Oportunidade: smartcity — 40 câmeras urbanas, prefeitura pequena
- Pedido: projeto completo + proposta em 5 dias
- Cliente: secretaria de obras, não de segurança — sem budget aprovado ainda
- Valor estimado: R$420.000
- Como chegou: chamada pública informal, 8 empresas cotando
- Sinais positivos: projeto real, verba prevista no orçamento 2025
- Sinais de alerta: decisor não é o secretário, prazo impossível, "menor preço ganha"
- Capacidade: equipe no limite

### Output


---
**Tags:** Avançado | Análise | Operações, RH & Gestão
