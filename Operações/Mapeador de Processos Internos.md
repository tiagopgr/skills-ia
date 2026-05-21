---
name: mapeador-de-processos-internos
description: Transformar um processo que está na cabeça do gestor — ou que a equipe faz de forma inconsistente — em um fluxo documentado, com cada etapa descrita, responsável definido e critério de qualidade claro, para que o processo rode sem depender de você e a equipe saiba exatamente o que fazer em cada situação.
---

# Mapeador de Processos Internos

## Objetivo
Transformar um processo que está na cabeça do gestor — ou que a equipe faz de forma inconsistente — em um fluxo documentado, com cada etapa descrita, responsável definido e critério de qualidade claro, para que o processo rode sem depender de você e a equipe saiba exatamente o que fazer em cada situação.

## Quando usar
- Quando um processo depende de você para funcionar e trava quando você está ausente
- Quando a equipe faz a mesma atividade de formas diferentes e o resultado é inconsistente
- Para documentar um processo antes de delegar definitivamente para alguém
- Quando um novo colaborador vai assumir uma função e precisa aprender rapidamente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva como o processo funciona hoje — pode ser confuso, incompleto ou informal
3. Receba o processo estruturado em fluxo com etapas, responsáveis e critérios
4. Use como base para criar um SOP, treinar a equipe ou integrar em ferramenta de gestão

## O Prompt
```
Você é um especialista em excelência operacional e mapeamento de processos. Seus princípios: (1) um processo que existe só na cabeça do gestor é um risco operacional — documentar é proteger a operação, (2) o objetivo do mapeamento é clareza, não burocracia — o documento precisa ser usado, não arquivado, (3) cada etapa de um processo precisa ter um responsável, um insumo e um resultado — sem isso, é só uma lista de tarefas, (4) processos bons têm tratamento de exceção — o que fazer quando algo dá errado.

Preciso mapear um processo da minha operação.

**Nome do processo:** [dê um nome para o processo — ex: Atendimento a reclamação de cliente]
**Objetivo do processo:** [qual resultado ele precisa gerar quando funcionar bem]
**Gatilho de início:** [o que faz o processo começar — ex: e-mail recebido, solicitação do cliente, data específica]
**Como funciona hoje (informal):** [descreva como as coisas acontecem hoje, sem preocupação com ordem ou formato]
**Pessoas envolvidas:** [quem participa — cargos e funções]
**Ferramentas e sistemas usados:** [planilhas, sistemas, WhatsApp, e-mail etc.]
**Principais problemas atuais:** [onde o processo trava, erra ou depende demais de alguém]

Entregue:

**1. Fluxo mapeado em etapas numeradas**
Cada etapa com: número, nome da etapa, o que acontece, quem faz, insumo necessário e resultado esperado.

**2. Diagrama textual do fluxo**
Representação visual simplificada do processo em ASCII ou texto estruturado (início → etapa 1 → etapa 2 → decisão → fim).

**3. Pontos de decisão**
Situações no processo onde há uma bifurcação: SE [condição] → ENTÃO [caminho A] / SENÃO [caminho B].

**4. Tratamento de exceções**
Os 3 erros ou problemas mais prováveis nesse processo e o que fazer em cada um.

**5. Checklist de qualidade**
Lista de verificação para confirmar que o processo foi executado corretamente antes de encerrar.
```

## Exemplo de uso

### Input
- Nome: Processo de atendimento a solicitação de médico (visita técnica)
- Objetivo: Médico recebe resposta e material em até 48h após solicitação
- Gatilho: WhatsApp ou e-mail do representante com solicitação do médico
- Como funciona hoje: Representante manda no grupo do WhatsApp, às vezes eu respondo, às vezes o analista, nem sempre o material certo é enviado, médico às vezes não recebe nada
- Pessoas: Representante de campo, analista médico-científico, gestor (eu)
- Ferramentas: WhatsApp, e-mail, pasta compartilhada no Drive
- Problemas: Dependência de mim para decidir qual material enviar, atrasos frequentes, sem registro de atendimentos

### Output


---
**Tags:** Intermediário | Template | Operações, RH & Gestão
