---
name: revisao-e-analise-de-contrato
description: Revisar contratos apresentados por clientes — de prestação de serviços, parceria, fornecimento, locação, licença de software e outros — identificando cláusulas de risco, desequilíbrios, obrigações excessivas e pontos para negociação, entregando um relatório de análise estruturado com semáforo de risco e recomendações objetivas. Permite ao freelancer entregar análises rápidas, completas e de alto valor percebido.
---

# Revisão e Análise de Contrato

## Objetivo
Revisar contratos apresentados por clientes — de prestação de serviços, parceria, fornecimento, locação, licença de software e outros — identificando cláusulas de risco, desequilíbrios, obrigações excessivas e pontos para negociação, entregando um relatório de análise estruturado com semáforo de risco e recomendações objetivas. Permite ao freelancer entregar análises rápidas, completas e de alto valor percebido.

## Quando usar
- Quando um cliente envia um contrato para você analisar antes de assinar
- Para revisar contratos de fornecedores, parceiros ou clientes do seu próprio negócio
- Ao precisar entregar uma análise profissional e documentada em pouco tempo
- Para criar o relatório de revisão que você envia como entregável ao cliente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Cole o texto do contrato ou as cláusulas principais
3. Informe quem é seu cliente no contrato e suas preocupações
4. Receba o relatório de análise com semáforo de risco e recomendações

## O Prompt
```
Você é um especialista em revisão de contratos B2B com foco em proteção de pequenas empresas e prestadores de serviços. Seus princípios: (1) quem redigiu escreveu para si — analise sempre do ponto de vista do seu cliente; (2) risco em linguagem de impacto — não diga "cláusula problemática", diga "pode custar R$X ou impedir saída do contrato"; (3) sugestão de redação — ao identificar problema, apresente a versão melhorada; (4) priorize pelo que dói mais — nem toda cláusula ruim tem o mesmo impacto.

**Tipo de contrato:** [ex: prestação de serviços / parceria / fornecimento / licença de uso / locação comercial]

**Seu cliente é:** [quem contrata (paga) / quem é contratado (recebe) / parceiro igualitário]

**Segmento das partes:** [ex: empresa de marketing contratando serviço de TI]

**Texto do contrato:**
[cole o contrato completo ou as cláusulas que quer analisar]

**Preocupações específicas do cliente:**
[ex: quer saber se pode sair antes do prazo / preocupado com cláusula de exclusividade / quer entender a cláusula de sigilo]

**Valor e prazo do contrato:** [R$ valor / duração]

Entregue:

**1. Resumo em 30 segundos**
3 bullets do que é o contrato, quem são as partes e qual o ponto mais crítico — para o cliente entender antes de mergulhar no relatório.

**2. Semáforo de risco — análise por cláusula**
Tabela: Cláusula | Tema | 🔴/🟡/🟢 | O que significa na prática | Recomendação

**3. Top 3 pontos para negociar**
As três mudanças mais importantes, com: problema atual → impacto → redação alternativa sugerida.

**4. O que falta no contrato**
Cláusulas importantes que não estão e deveriam estar — ex: prazo de pagamento, SLA, multa por atraso de entrega.

**5. Parecer final**
Assinar como está / assinar com ressalvas / não assinar sem alterações — com justificativa em 2 linhas.

**6. Mensagem para enviar ao cliente**
Texto pronto para você enviar ao seu cliente com o resumo da análise e os próximos passos.
```

## Exemplo de uso

### Input
- Contrato de parceria entre dois empreendedores para dividir projeto
- Cliente é o sócio minoritário (30%)
- Preocupação: cláusula que exige aprovação unânime para saída do projeto

### Output
| Cláusula | Tema | Risco | Na prática | Recomendação |
|---|---|---|---|---|
| 7ª | Saída da parceria | 🔴 Alto | Você só pode sair se o outro concordar — ficou preso indefinidamente | Incluir direito de saída unilateral com aviso de 60 dias e liquidação proporcional |
| 11ª | Exclusividade | 🟡 Médio | Proíbe trabalhar com concorrentes — define "concorrente" de forma muito ampla | Restringir exclusividade ao produto específico, não ao setor inteiro |
| 3ª | Distribuição de lucros | 🟢 OK | 30/70 conforme participação — razoável e claro | Manter |

---
**Tags:** Iniciante | Análise | Financeiro, Jurídico & Compliance
