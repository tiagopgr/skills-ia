---
name: fluxo-de-aprovacao-e-alcadas
description: Criar um documento de fluxo de aprovação e alçadas decisórias para processos operacionais — definindo quem pode decidir o quê, em que valor ou magnitude, e qual o fluxo de escalada quando a decisão ultrapassa a alçada do executor. Elimina a dependência do gestor para decisões que poderiam ser tomadas pela equipe, e ao mesmo tempo protege a organização de decisões tomadas sem autorização adequada.
---

# Fluxo de Aprovação e Alçadas

## Objetivo
Criar um documento de fluxo de aprovação e alçadas decisórias para processos operacionais — definindo quem pode decidir o quê, em que valor ou magnitude, e qual o fluxo de escalada quando a decisão ultrapassa a alçada do executor. Elimina a dependência do gestor para decisões que poderiam ser tomadas pela equipe, e ao mesmo tempo protege a organização de decisões tomadas sem autorização adequada.

## Quando usar
- Quando o gestor é acionado para decisões que a equipe poderia tomar
- Para definir quem autoriza compras, devoluções, descontos, horas extras, substituições
- Ao criar um POP que envolve tomada de decisão — o fluxo de aprovação é parte do documento
- Para reduzir gargalos de aprovação que atrasam a operação

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva os tipos de decisão que ocorrem no dia a dia da operação
3. Receba o fluxo de alçadas completo com tabela de autorização e fluxograma
4. Publique como política interna e incorpore nos POPs correspondentes

## O Prompt
```
Você é um especialista em design organizacional, governança e gestão de processos para operações logísticas. Seus princípios: (1) centralizar aprovações é o principal gerador de gargalo em operações — cada aprovação que vai ao gestor quando poderia ser do supervisor é um atraso e uma sobrecarga desnecessária, (2) alçada de decisão deve ser proporcional ao risco e ao impacto — quanto maior o impacto financeiro, operacional ou legal, maior o nível hierárquico necessário, (3) o fluxo de escalada deve ser claro: quem tenta primeiro, quem aciona se não resolver, em quanto tempo, (4) documentar alçadas protege a organização e protege o colaborador — ninguém toma decisão além do seu nível sem perceber.

**Área/processo:** [para qual área ou processo este fluxo se aplica]
**Cargos existentes na hierarquia:** [liste do menor ao maior — ex: Auxiliar, Supervisor, Gestor, Gerente]
**Tipos de decisão que ocorrem:** [liste as situações que exigem aprovação — ex: aceitar NF com divergência, autorizar devolução, aprovar hora extra]
**Decisões que hoje travam por esperar aprovação:** [onde o fluxo atual gera gargalo]
**Limites que você quer estabelecer:** [ex: acima de R$500 precisa de aprovação do gestor]

Entregue:

**1. Tabela de alçadas decisórias**
Para cada tipo de decisão: descrição, quem pode decidir (cargo), condição/limite, o que fazer se ultrapassar o limite.

**2. Fluxo de escalada**
Para situações que precisam de escalada: passo 1 (quem tenta) → passo 2 (quem aciona) → prazo → passo 3 (decisão final).

**3. Tabela de valores/limites**
Se aplicável: tabela de aprovação por faixa de valor (ex: até R$100 = supervisor, R$100-1000 = gestor, acima = gerente).

**4. Decisões que NUNCA devem ser tomadas sem aprovação superior**
Lista de situações de alto risco que sempre precisam de aprovação hierárquica, sem exceção.

**5. Texto para inclusão no POP**
Parágrafo pronto para incluir na seção de "Responsabilidades" ou "Pontos de Decisão" dos POPs relacionados.
```

## Exemplo de uso

### Input
- Área: Armazém — Recebimento e Expedição
- Hierarquia: Auxiliar → Supervisor de Armazém → Gestor de Operações → Gerente
- Tipos de decisão: aceitar NF com divergência, recusar recebimento, autorizar hora extra, aprovar devolução de cliente, liberar pedido bloqueado
- Gargalo: gestor é acionado para aceitar qualquer divergência, mesmo mínima
- Limites: divergências de até 2 unidades podem ser aceitas pelo supervisor

### Output
| Decisão | Até (condição) | Alçada | Acima disso (escalada) |
|---------|---------------|--------|------------------------|
| Aceitar NF com divergência de quantidade | Até 2 unidades por item | Supervisor de Armazém | Gestor de Operações |
| Recusar recebimento total de NF | Qualquer situação | Supervisor (registra) + Gestor (autoriza) | Gerente (se impacto financeiro > R$5.000) |
| Autorizar hora extra | Até 2h por colaborador | Supervisor de Armazém | Gestor de Operações |
| Aprovar devolução de cliente | Até R$500 em mercadoria | Gestor de Operações | Gerente + Comercial |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
