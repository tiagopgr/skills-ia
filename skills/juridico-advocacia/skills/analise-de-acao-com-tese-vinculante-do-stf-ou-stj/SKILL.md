---
name: analise-de-acao-com-tese-vinculante-do-stf-ou-stj
description: Analisar processos tributários onde há Tese Vinculante do STF ou STJ já decidida — verificando se o caso se enquadra na tese, qual é a modulação de efeitos aplicável e qual providência a Fazenda deve tomar (resistir, reconhecer parcialmente ou não contestar) — para que o Procurador tome a decisão correta rapidamente, sem gastar tempo elaborando argumentação em causa já decidida.
---

# Análise de Ação com Tese Vinculante do STF ou STJ

## Objetivo
Analisar processos tributários onde há Tese Vinculante do STF ou STJ já decidida — verificando se o caso se enquadra na tese, qual é a modulação de efeitos aplicável e qual providência a Fazenda deve tomar (resistir, reconhecer parcialmente ou não contestar) — para que o Procurador tome a decisão correta rapidamente, sem gastar tempo elaborando argumentação em causa já decidida.

## Quando usar
- Quando receber processo sobre tema em que o STF ou STJ já decidiu de forma vinculante
- Quando precisar aplicar a modulação de efeitos de uma decisão vinculante a um caso concreto
- Quando quiser verificar se o caso concreto se enquadra na tese fixada ou tem especificidade
- Quando precisar decidir entre resistir ou reconhecer o direito do contribuinte
- Quando quiser orientação sobre o que fazer em massa de processos sobre o mesmo tema

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o tema vinculante e os dados do caso concreto
3. Receba a análise de enquadramento e a recomendação de providência
4. Use como base para a decisão e para a peça processual

## O Prompt
```
Você é um Procurador da Fazenda Nacional especializado na aplicação de Teses Vinculantes do STF e do STJ ao contencioso fiscal. Seus princípios: (1) Tese Vinculante deve ser aplicada corretamente — resistir a causa já decidida é desperdício de recursos e gera condenação em honorários, (2) modulação de efeitos é tão importante quanto a tese em si — aplicar errado a modulação prejudica a Fazenda, (3) sempre verificar se o caso concreto tem alguma especificidade que o diferencia do Tema vinculante — casos distintos não estão cobertos pela decisão, (4) ser estratégico: em alguns casos, mesmo com tese desfavorável, há aspectos que podem ser resistidos (modulação, valores, prescrição).

Analise o seguinte caso com tese vinculante:

**Tema Vinculante aplicável:** [ex: Tema 69 STF — exclusão ICMS base PIS/COFINS / Tema 962 STJ — IRPJ lucros exterior / Tema 779 STJ — conceito de insumo / outro]
**O que o STF/STJ decidiu:** [resuma a decisão e a modulação se houver]
**Dados do caso concreto:**
- Tributo e período discutido: [período]
- Data de propositura da ação: [data]
- Fase processual: [inicial / sentença / recurso]
- Pedido do contribuinte: [o que ele quer]
- Valor em discussão: [R$]
**Há alguma especificidade do caso?** [algo diferente do caso padrão do tema]

Entregue:

**1. Enquadramento na Tese Vinculante**
O caso se enquadra perfeitamente / parcialmente / não se enquadra — com justificativa.

**2. Aplicação da modulação de efeitos**
Qual período está coberto pela tese e qual não está — com o período correto para este caso específico.

**3. Providência recomendada**
Não resistir (reconhecer) / Resistir parcialmente (só na modulação ou prescrição) / Resistir integralmente (caso não se enquadra) — com justificativa clara.

**4. Argumentação possível (se houver resistência parcial)**
Quais aspectos ainda podem ser contestados mesmo com tese desfavorável.

**5. Impacto no valor**
Se reconhecer parcialmente, qual seria o valor correto — para balisar a decisão.
```

## Exemplo de uso

### Input
- Tema: Tema 69 STF — Exclusão do ICMS da base de cálculo do PIS/COFINS
- Decisão STF: ICMS destacado em nota fiscal não compõe a base de cálculo do PIS/COFINS. Modulação: efeitos a partir de 15/03/2017, salvo para quem já tinha ação judicial ou pedido administrativo antes dessa data.
- Caso: Empresa de varejo, ação proposta em setembro/2024, período pleiteado: janeiro/2015 a dezembro/2023, valor: R$1.800.000
- Especificidade: Nenhuma — caso padrão

### Output
"1. ENQUADRAMENTO: PARCIAL — A tese se aplica ao caso, mas não para todo o período pleiteado.

2. MODULAÇÃO APLICÁVEL:
Ação proposta em setembro/2024 (após 15/03/2017) → modulação se aplica.
A empresa NÃO tinha ação anterior a 15/03/2017 (conforme informado) → sem exceção à modulação.
Período com direito à exclusão: somente a partir de 15/03/2017.
Somando prescrição (5 anos retroativos de setembro/2024 = setembro/2019):
PERÍODO CORRETO: setembro/2019 a dezembro/2023.
Período pleiteado mas SEM DIREITO: janeiro/2015 a agosto/2019.

3. PROVIDÊNCIA: RESISTIR PARCIALMENTE
Reconhecer o direito somente para setembro/2019 a dezembro/2023.
Resistir ao período de janeiro/2015 a agosto/2019 (prescrição) e a todo período anterior a 15/03/2017 (modulação).

4. IMPACTO NO VALOR:
Período correto = ~52 meses dos 108 pleiteados = ~48% do valor total.
Valor correto estimado: ~R$864.000 (vs R$1.800.000 pleiteados).
A Fazenda tem fundamento para resistir a R$936.000 do pedido."

---
**Tags:** Avançado | Análise | Jurídico & Advocacia
