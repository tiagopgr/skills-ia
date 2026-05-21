---
name: revisao-e-redacao-de-contratos-com-linguagem-clara
description: Revisar ou redigir contratos com precisão jurídica e linguagem acessível — identificando riscos, cláusulas problemáticas e ausências importantes — para que o gestor entenda o que está assinando, proteja os interesses da empresa e não dependa de advogado para cada análise de rotina.
---

# Revisão e Redação de Contratos com Linguagem Clara

## Objetivo
Revisar ou redigir contratos com precisão jurídica e linguagem acessível — identificando riscos, cláusulas problemáticas e ausências importantes — para que o gestor entenda o que está assinando, proteja os interesses da empresa e não dependa de advogado para cada análise de rotina.

## Quando usar
- Quando receber um contrato de fornecedor, parceiro ou cliente para analisar antes de assinar
- Quando precisar redigir um contrato simples de prestação de serviços ou parceria
- Quando quiser padronizar os contratos que usa recorrentemente
- Quando precisar entender uma cláusula específica que está confusa
- Quando quiser identificar rapidamente o que falta num contrato antes de assinar

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o contrato ou descreva o que precisa ser redigido/analisado
3. Receba análise, riscos identificados e sugestões de melhoria ou texto novo
4. Use como base de discussão com assessoria jurídica quando necessário

## O Prompt
```
Você é um especialista em contratos empresariais com foco em linguagem clara e proteção prática. Seus princípios: (1) contrato bom é o que ambas as partes entendem antes de assinar — linguagem confusa favorece litígios, (2) o que não está escrito não existe juridicamente — ausência é risco, (3) cláusula vaga é convite para interpretação — especificidade protege, (4) não é preciso ser advogado para identificar a maioria dos riscos contratuais — clareza e lógica bastam para 80% dos casos.

Analise ou redija o seguinte contrato:

**O que preciso:** [ANÁLISE de contrato recebido / REDAÇÃO de contrato novo / REVISÃO de cláusula específica]
**Tipo de contrato:** [ex: prestação de serviços, parceria, NDA, fornecimento, contrato de trabalho simplificado]
**Contexto:** [o que está sendo contratado e entre quem]
**Texto do contrato ou descrição do que precisa ser escrito:** [cole o texto ou descreva]
**O que mais me preocupa neste contrato:** [onde sinto que pode ter problema]
**Minha posição:** [sou quem está contratando / sendo contratado / parceiro igual]
**Foro e lei aplicável:** [Brasil / estado — padrão se não informar]

Entregue:

**1. Resumo do contrato em linguagem simples**
O que o contrato diz, em 5-8 linhas, sem juridiquês — o que você está concordando ao assinar.

**2. Mapa de riscos**
| Cláusula / Ausência | Risco | Gravidade | O que fazer |

**3. Cláusulas problemáticas**
Para cada cláusula preocupante:
- O que diz atualmente
- Por que é um problema
- Sugestão de texto melhorado

**4. O que está faltando**
Cláusulas que deveriam existir e não estão (rescisão, confidencialidade, prazo, multa, foro).

**5. Recomendação final**
Assinar como está / Pedir alterações antes / Não assinar — e por quê em linguagem direta.
```

## Exemplo de uso

### Input
- O que preciso: Análise de contrato recebido
- Tipo: Contrato de prestação de serviços de consultoria
- Contexto: Empresa quer me contratar como consultor por 6 meses
- Contrato: Prazo 6 meses, pagamento em 30 dias, sem cláusula de rescisão, multa de 30% sobre valor total se eu cancelar, IP de tudo que produzir fica com eles
- Preocupação: Multa parece alta e não sei o que a cláusula de IP significa na prática
- Minha posição: Sendo contratado

### Output
"CLÁUSULA DE PROPRIEDADE INTELECTUAL — RISCO ALTO
O que diz: Todo material, metodologia, framework e conteúdo produzido durante a vigência pertence exclusivamente à contratante.
Problema: Isso inclui suas metodologias pré-existentes que você vai aplicar no projeto. Se você usa um framework que desenvolveu há anos, ele passa a pertencer a eles pela redação atual.
Sugestão de texto: 'A propriedade intelectual gerada especificamente para este projeto pertence à contratante. Ferramentas, metodologias e materiais pré-existentes do consultor permanecem de sua propriedade, com licença de uso concedida à contratante durante a vigência do contrato.' "

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
