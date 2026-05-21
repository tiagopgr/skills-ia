---
name: relatorio-de-implementacao-de-ia-para-cliente
description: Gerar um relatório completo de entrega de um projeto de implementação de IA — com o que foi implementado, como funciona, resultados iniciais, documentação para o cliente manter o sistema e recomendações de evolução — que profissionaliza a entrega e justifica o valor cobrado. O relatório de implementação transforma um "projeto técnico" em um documento executivo que o cliente apresenta aos sócios e que gera indicações.
---

# Relatório de Implementação de IA para Cliente

## Objetivo
Gerar um relatório completo de entrega de um projeto de implementação de IA — com o que foi implementado, como funciona, resultados iniciais, documentação para o cliente manter o sistema e recomendações de evolução — que profissionaliza a entrega e justifica o valor cobrado. O relatório de implementação transforma um "projeto técnico" em um documento executivo que o cliente apresenta aos sócios e que gera indicações.

## Quando usar
- Ao finalizar um projeto de implementação de IA para um cliente
- Para documentar o que foi construído de forma que o cliente consiga entender e manter
- Quando quer elevar a percepção de valor da entrega
- Para criar um histórico de cada projeto que você pode usar como case

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o que foi implementado e os resultados iniciais
3. Informe as ferramentas utilizadas e as instruções de manutenção
4. Receba o relatório completo pronto para enviar ao cliente

## O Prompt
```
Você é um consultor de tecnologia que escreve relatórios de entrega claros, profissionais e compreensíveis para clientes não técnicos. Seus princípios: (1) resultado antes de técnica — o executivo lê o resultado, depois o detalhe técnico; (2) documentação funcional — o cliente precisa saber o que fazer se algo parar de funcionar; (3) próximo passo = nova oportunidade — as recomendações de evolução são a semente do próximo projeto; (4) linguagem de negócio — "o sistema envia mensagens automaticamente" bate "o webhook dispara o fluxo n8n".

**Cliente e empresa:** [nome]

**Projeto implementado:** [descreva o que foi construído]

**Ferramentas e tecnologias utilizadas:** [lista das ferramentas]

**O que o sistema faz (em linguagem humana):**
[descreva o funcionamento do ponto de vista do usuário]

**Resultados iniciais (se já disponíveis):**
[métricas, feedback, primeiros números]

**Como o cliente faz manutenção básica:**
[o que ele pode ajustar sozinho sem precisar de você]

**O que NÃO pode ser alterado sem chamar você:**
[partes críticas que não devem ser mexidas]

**Recomendações de evolução:**
[próximos projetos ou melhorias que fazem sentido]

**Seu contato para suporte:** [como o cliente te aciona]

Entregue:

**1. Capa executiva**
Título, cliente, data, consultor responsável e resumo em 3 bullets do que foi entregue.

**2. O que foi implementado**
Descrição do sistema em linguagem de negócio — o que faz, como faz, quem usa.

**3. Como funciona — passo a passo visual**
Fluxo do sistema descrito de forma visual (textual): Gatilho → Ação 1 → Ação 2 → Resultado.

**4. Resultados e métricas**
O que foi medido, o que melhorou, comparativo antes/depois se disponível.

**5. Guia de manutenção**
O que o cliente pode fazer sozinho: como alterar textos de mensagens, como pausar o sistema, onde ver os logs.

**6. O que NÃO mexer**
Lista das configurações críticas com aviso claro de chamar suporte antes de alterar.

**7. Próximos passos recomendados**
2-3 evoluções que fariam sentido — posicionadas como cuidado com o cliente.

**8. Suporte**
Como e quando acionar você.
```

## Exemplo de uso

### Input
- Cliente: Clínica Sorriso
- Projeto: bot de confirmação de consultas via WhatsApp
- Ferramentas: n8n + Z-API + Google Sheets
- Resultado: taxa de falta caiu de 18% para 7% em 30 dias

### Output


---
**Tags:** Intermediário | Geração | Operações, RH & Gestão
