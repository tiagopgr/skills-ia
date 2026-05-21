---
name: design-de-fluxo-de-automacao-visual
description: Mapear visualmente fluxos de automação de vendas e marketing — diagramas de sequência, peças visuais para cada touchpoint e dashboards de acompanhamento — para que o time entenda a jornada completa do lead e cada touchpoint tenha material profissional.
---

# Design de Fluxo de Automação Visual

## Objetivo
Mapear visualmente fluxos de automação de vendas e marketing — diagramas de sequência, peças visuais para cada touchpoint e dashboards de acompanhamento — para que o time entenda a jornada completa do lead e cada touchpoint tenha material profissional.

## Quando usar
- Ao planejar uma automação de vendas multicanal (email + LinkedIn + call)
- Para documentar visualmente fluxos do Apollo, HubSpot, Pipedrive ou ActiveCampaign
- Quando precisa apresentar o fluxo de automação para um cliente ou gestor
- Para criar materiais visuais para cada etapa da automação

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o fluxo de automação, canais e objetivos
3. Receba o mapa visual completo + specs de cada peça
4. Execute o diagrama no Figma/FigJam/Miro e as peças individualmente

## O Prompt
```
Você é um designer de processos de vendas que visualiza automações complexas de forma clara e profissional. Você sabe que: (1) automação sem visualização é caixa-preta — ninguém entende o que acontece quando, (2) cada touchpoint da automação precisa de material visual adequado, (3) o diagrama do fluxo é tão importante quanto o fluxo em si — é o mapa que o time segue, (4) dashboards visuais de performance tornam otimização intuitiva.

Crie o design do fluxo de automação para:

**Tipo de automação:** [prospecção outbound, nurturing inbound, onboarding, reativação]
**Ferramenta:** [Apollo.io, HubSpot, ActiveCampaign, Pipedrive, Make/Zapier]
**Canais envolvidos:** [email, LinkedIn, WhatsApp, call, SMS]
**Etapas do fluxo:** [descreva as etapas ou peça sugestão]
**Triggers e condições:** [o que inicia o fluxo, o que define os caminhos]
**Público:** [quem passa por essa automação]
**Quem vai ver o diagrama:** [time interno, cliente, investidor, gestor]
**Ferramenta de diagramação:** [FigJam, Miro, Whimsical, Figma, draw.io]

Entregue: diagrama do fluxo completo com legenda de cores por canal (email azul, LinkedIn azul escuro, call verde, WhatsApp verde claro, delay cinza, conversão verde, saída vermelho); peças visuais por touchpoint; variações por cenário (principal, reengajamento, nurturing, urgência); layout de dashboard de performance; documentação por step em tabela; e deck de 5 slides para apresentar a stakeholders.
```

## Exemplo de uso

### Input
Tipo: prospecção outbound multicanal
Ferramenta: Apollo.io + LinkedIn manual
Canais: email (4 steps) + LinkedIn (2 steps)
Público: Heads de Marketing de SaaS
Ferramenta de diagrama: FigJam

### Output
Diagrama top-down: [Lead entra] → Email1 D0 → LinkedIn Connect D2 → Email2 D4 → ◆Abriu? → Sim: LinkedIn Message + One-pager / Não: Email3 D7 → Break-up D10 → ◆Respondeu? → Sim: ✅SQL / Não: 🔄Nurturing. Nodes arredondados, conectores com setas, condições em diamante.

---
**Tags:** Avançado | Template | Design & Branding
