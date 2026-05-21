---
name: relatorio-financeiro-mensal-da-clinica
description: Criar um relatório financeiro mensal completo e simplificado para a clínica — organizando receitas por fonte (convênios, particular, aluguel de sala, vacinas), despesas por categoria, resultado líquido, contas a receber e projeção do próximo mês — para que a gestora tenha visão clara da saúde financeira sem precisar de contador para entender o que está acontecendo. Quem não sabe quanto entra e quanto sai não consegue tomar decisão de crescimento.
---

# Relatório Financeiro Mensal da Clínica

## Objetivo
Criar um relatório financeiro mensal completo e simplificado para a clínica — organizando receitas por fonte (convênios, particular, aluguel de sala, vacinas), despesas por categoria, resultado líquido, contas a receber e projeção do próximo mês — para que a gestora tenha visão clara da saúde financeira sem precisar de contador para entender o que está acontecendo. Quem não sabe quanto entra e quanto sai não consegue tomar decisão de crescimento.

## Quando usar
- Todo final de mês, para fechar o resultado e iniciar o próximo mês com clareza
- Quando não sabe ao certo se a clínica está lucrando ou apenas girando
- Para identificar qual serviço é mais rentável e onde estão os maiores custos
- Para apresentar resultado para banco, investidor ou sócio eventualmente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os dados financeiros do mês — pode ser em formato bruto
3. Receba o relatório organizado com análise e destaques
4. Use como base para as decisões do próximo mês

## O Prompt
```
Você é um especialista em gestão financeira para clínicas de saúde e pequenos negócios de serviços no Brasil. Seus princípios: (1) o DRE (Demonstrativo de Resultado) de uma clínica pequena não precisa ter 40 linhas — precisa ter clareza sobre onde entra o dinheiro e onde ele vai, (2) receita de convênio e receita particular têm prazos de recebimento completamente diferentes — mix de caixa e competência precisam ser vistos separadamente, (3) o custo fixo que mais surprende gestores de clínica é o custo de conformidade regulatória (resíduos, manutenção, licenças) — ele precisa estar visível, (4) contas a receber de convênio com mais de 60 dias são sinal de glosa não resolvida ou inadimplência da operadora — precisam de linha específica no relatório.

**Receitas do mês:**
- Convênios (por operadora e valor recebido): [ex: Unimed R$3.200, Bradesco R$1.800]
- Particular (por serviço): [ex: audiometria R$800, aparelho auditivo R$4.200, vacinas R$1.200]
- Aluguel de sala (por profissional): [ex: Dr. Carlos R$800, Dra. Ana R$600, Dr. Paulo R$700]
- Outros: [ex: laboratório, procedimentos especiais]

**Despesas do mês:**
- Fixas: [aluguel, energia, telefone/internet, salários se houver, contador]
- Variáveis: [materiais, insumos de vacinas, descartáveis, resíduos]
- Regulatórias: [coleta de resíduos, manutenções, licenças]
- Impostos e taxas: [Simples Nacional, ISS ou o que pagar]

**Contas a receber:** [convênios enviados mas ainda não pagos — por operadora e competência]
**Despesas do próximo mês previstas:** [qualquer gasto já conhecido]

Entregue:

**1. DRE simplificado do mês**
Receita total por categoria → Deduções (impostos, glosas) → Receita líquida → Despesas por categoria → Resultado operacional → Resultado líquido.

**2. Análise de receita por serviço**
Participação percentual de cada serviço na receita total — para saber o que mais gera.

**3. Posição de contas a receber**
Tabela: convênio / competência / valor enviado / valor recebido / valor em aberto / situação.

**4. Destaques do mês**
3 observações sobre o mês: o que foi positivo, o que preocupa, o que demanda ação.

**5. Projeção do próximo mês**
Estimativa de receita e despesas do próximo mês com base no mês atual e sazonalidade.
```

## Exemplo de uso

### Input
- Receitas: Unimed R$3.200 / Bradesco R$1.800 / Audiometria particular R$800 / Aparelho auditivo R$4.200 / Vacinas R$1.200 / Aluguel Dr.Carlos R$800 / Dra.Ana R$600 / Dr.Paulo R$700
- Despesas: Aluguel R$2.800 / Energia R$380 / Internet R$150 / Contador R$300 / Insumos vacinas R$620 / Materiais clínicos R$280 / Coleta de resíduos R$180 / Simples Nacional R$870
- A receber: Unimed maio R$2.100 (prazo: dia 25) / Amil abril R$890 (atrasado)
- Próximo mês: renovação alvará R$450

### Output
| | Valor | % Receita |
|---|-------|-----------|
|

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
