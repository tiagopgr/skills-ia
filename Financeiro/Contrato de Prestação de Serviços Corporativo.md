---
name: contrato-de-prestacao-de-servicos-corporativo
description: Gerar contratos de prestação de serviços completos e juridicamente robustos para clientes corporativos — com escopo detalhado, SLA, cláusulas de confidencialidade, responsabilidade e rescisão adequadas ao ambiente B2B — para que gestores e consultores consigam formalizar acordos com empresas de qualquer porte de forma profissional, sem precisar de advogado para cada novo contrato padrão.
---

# Contrato de Prestação de Serviços Corporativo

## Objetivo
Gerar contratos de prestação de serviços completos e juridicamente robustos para clientes corporativos — com escopo detalhado, SLA, cláusulas de confidencialidade, responsabilidade e rescisão adequadas ao ambiente B2B — para que gestores e consultores consigam formalizar acordos com empresas de qualquer porte de forma profissional, sem precisar de advogado para cada novo contrato padrão.

## Quando usar
- Para formalizar a prestação de serviços para uma empresa cliente
- Ao precisar de um contrato mais robusto do que os modelos genéricos da internet, calibrado para B2B
- Para incluir cláusulas específicas de sigilo, SLA e proteção de dados (LGPD)
- Quando o cliente exigir um contrato formal antes de iniciar o projeto

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha os dados das partes, o escopo do serviço e as condições comerciais
3. Receba o contrato completo com todas as cláusulas e alertas sobre os pontos mais críticos
4. Envie para revisão do seu advogado em casos de alto valor, ou use diretamente para valores menores

## O Prompt
```
Você é um advogado especializado em contratos comerciais B2B para prestação de serviços no Brasil. Seus princípios: (1) contrato B2B precisa ser mais robusto do que contrato com pessoa física — empresas têm mais recursos para contestar e os valores envolvidos geralmente justificam cláusulas mais detalhadas, (2) SLA (Service Level Agreement) é o coração do contrato de serviço — sem critérios claros de qualidade e prazo, qualquer entrega pode ser contestada, (3) cláusulas de confidencialidade e LGPD não são opcionais para contratos que envolvam dados de clientes ou informações estratégicas — são obrigatórias e podem ser exigidas pelo contratante, (4) cláusula de rescisão mal redigida é fonte de litígio — sempre definir prazo de aviso, multa e processo de transição.

Gere o contrato corporativo de prestação de serviços com base nas informações abaixo:

**Prestador (você):**
- Razão Social e CNPJ: [dados]
- Endereço: [cidade e estado]
- Representante legal: [nome e CPF]

**Contratante (cliente):**
- Razão Social e CNPJ: [dados]
- Endereço: [cidade e estado]
- Representante legal: [nome e CPF]

**Objeto do contrato:** [o serviço contratado]
**Escopo detalhado:** [o que está incluso — e o que não está]
**SLA e entregáveis:** [prazos, qualidade mínima, métricas de entrega]
**Valor e forma de pagamento:** [valor, data de vencimento, multas por atraso]
**Vigência:** [duração e condições de renovação]
**Confidencialidade:** [quais informações são confidenciais]
**Dados pessoais envolvidos:** [se o serviço envolve dados de terceiros — para cláusula LGPD]
**Rescisão:** [aviso prévio, multa rescisória, procedimento de transição]
**Foro:** [cidade para resolução de conflitos]

Gere o contrato completo com:
1. Qualificação das partes
2. Objeto
3. Escopo, exclusões e SLA
4. Remuneração e condições de pagamento
5. Vigência e renovação
6. Obrigações do prestador
7. Obrigações do contratante
8. Confidencialidade e sigilo
9. Proteção de dados (LGPD)
10. Propriedade intelectual
11. Responsabilidade civil
12. Rescisão e penalidades
13. Disposições gerais e foro

Após o contrato: alerta dos 3 pontos mais críticos e sugestão de cláusula adicional para o tipo de serviço informado.
```

## Exemplo de uso

### Input
- Prestador: FS Consultoria Ltda, CNPJ 00.000.000/0001-00, São Paulo/SP
- Contratante: Distribuidora ABC Ltda, CNPJ 11.111.111/0001-11, São Paulo/SP
- Serviço: Consultoria de gestão financeira e implantação de processos
- Escopo: Diagnóstico financeiro, implantação de dashboard, 4 reuniões mensais, relatório mensal
- SLA: Relatório entregue até dia 5 de cada mês, reuniões agendadas com 5 dias de antecedência
- Valor: R$5.500/mês todo dia 1
- Vigência: 12 meses com renovação automática
- Rescisão: 30 dias de aviso + multa de 2 mensalidades se rescisão imotivada pelo contratante

### Output
"3.1 O PRESTADOR compromete-se a entregar o Relatório Gerencial Mensal até o 5º (quinto) dia útil do mês subsequente ao período de referência.
3.2 As reuniões mensais serão agendadas com antecedência mínima de 5 (cinco) dias úteis, respeitando a disponibilidade de ambas as partes.
3.3 O atraso na entrega do Relatório superior a 3 (três) dias úteis, salvo em casos de força maior ou ausência de dados por parte do CONTRATANTE, implicará desconto proporcional de 10% no valor da mensalidade correspondente."

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
