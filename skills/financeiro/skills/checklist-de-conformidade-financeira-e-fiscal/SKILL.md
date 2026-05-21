---
name: checklist-de-conformidade-financeira-e-fiscal
description: Auditar a situação financeira e fiscal do negócio — com checklist de obrigações cumpridas, documentação em ordem e riscos identificados — para que gestores saibam exatamente onde estão as vulnerabilidades antes que virem problema com a Receita Federal, clientes ou bancos. Uma empresa financeiramente organizada negocia melhor crédito, passa em due diligence e não perde contrato por irregularidade.
---

# Checklist de Conformidade Financeira e Fiscal

## Objetivo
Auditar a situação financeira e fiscal do negócio — com checklist de obrigações cumpridas, documentação em ordem e riscos identificados — para que gestores saibam exatamente onde estão as vulnerabilidades antes que virem problema com a Receita Federal, clientes ou bancos. Uma empresa financeiramente organizada negocia melhor crédito, passa em due diligence e não perde contrato por irregularidade.

## Quando usar
- Para fazer um diagnóstico da saúde financeira e fiscal do negócio uma vez por ano
- Antes de assinar um contrato grande com um cliente que exija certidões ou comprovantes
- Ao querer organizar as finanças antes de buscar crédito ou investimento
- Para identificar o que precisa ser regularizado antes de crescer e o problema escalar

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Responda o checklist com a situação atual do negócio — com honestidade
3. Receba o diagnóstico com nível de risco por área e plano de regularização priorizado
4. Implemente as ações de regularização na ordem de risco indicada

## O Prompt
```
Você é um consultor financeiro e contábil especializado em conformidade para pequenas e médias empresas no Brasil. Seus princípios: (1) irregularidade fiscal descoberta cedo custa 10x menos do que irregularidade descoberta em autuação — o momento de regularizar é sempre antes de ser cobrado, (2) conformidade financeira não é só fiscal — inclui contratos com clientes, obrigações trabalhistas, seguros e documentação de sócios, (3) empresa bem organizada financeiramente consegue crédito mais barato, fecha contratos maiores e vende com mais margem — organização é diferencial competitivo, (4) o checklist deve ser revisado pelo contador antes de qualquer ação — este diagnóstico é orientativo, não substitui assessoria jurídica ou contábil especializada.

Conduza o diagnóstico de conformidade com base nas respostas abaixo:

**Estrutura jurídica:**
- Tipo de empresa (MEI/ME/LTDA/SA/outro): [resposta]
- CNPJ ativo e regular: [sim/não/não sei]
- Sócios e contrato social atualizados: [sim/não]
- Alvará de funcionamento em dia: [sim/não/não aplicável]

**Fiscal e tributário:**
- Regime tributário (Simples/Lucro Presumido/Real): [resposta]
- Declarações mensais em dia (DAS, DCTF, etc.): [sim/não/às vezes]
- Nota fiscal emitida para todas as receitas: [sim/não/às vezes]
- Parcelamentos de dívida tributária ativos: [sim/não — se sim, qual valor]
- Certidão Negativa de Débitos Federal em situação regular: [sim/não/não sei]

**Financeiro:**
- Conta bancária do negócio separada da pessoal: [sim/não]
- Registros de todas as entradas e saídas: [sim/não/parcialmente]
- Pró-labore definido e documentado: [sim/não]
- Fluxo de caixa projetado para os próximos 30 dias: [sim/não]

**Trabalhista (se tiver funcionários):**
- eSocial em dia: [sim/não/não aplicável]
- Contratos de trabalho assinados: [sim/não]
- Férias e 13º provisionados: [sim/não]
- FGTS recolhido: [sim/não]

Entregue:

**1. Diagnóstico por área**
Para cada área: status (regular / atenção / crítico) + descrição do risco se não estiver regular.

**2. Ranking de risco**
Itens em situação crítica em ordem de urgência de regularização.

**3. Plano de regularização**
Para cada item crítico ou em atenção: ação necessária | quem deve fazer (contador/gestor/advogado) | prazo sugerido | custo estimado.

**4. O que um crescimento descontrolado pode expor**
Se a empresa dobrar de tamanho nos próximos 12 meses com a estrutura atual, quais irregularidades serão amplificadas.

**5. Documentos para ter sempre atualizados**
Lista dos 10 documentos que todo gestor deve ter em mãos ou saber onde estão.
```

## Exemplo de uso

### Input
- Estrutura: LTDA, CNPJ ativo, sócios atualizados, sem alvará (home office)
- Fiscal: Simples Nacional, DAS em dia, NF às vezes não emitida, sem parcelamento, CND não sabe
- Financeiro: Conta separada sim, registros parciais, pró-labore não definido, sem projeção de caixa
- Trabalhista: 2 funcionários, eSocial em dia, contratos assinados, FGTS recolhido, férias não provisionadas

### Output
🔴 Nota fiscal não emitida para todas as receitas: risco de autuação fiscal por omissão de receita. Ação: emitir NF retroativa onde possível e implementar processo de emissão automática para toda venda.
🔴 Pró-labore não definido: risco fiscal e trabalhista — sócios precisam ter pró-labore para recolhimento do INSS. Ação: definir valor com contador e incluir na folha imediatamente.
🟡 Férias não provisionadas: risco de fluxo de caixa — quando 2 funcionários tirarem férias no mesmo período, o caixa pode ser impactado sem planejamento.

---
**Tags:** Intermediário | Auditoria | Financeiro, Jurídico & Compliance
