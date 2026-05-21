---
name: framework-de-analise-de-precificacao-e-margem
description: Analisar a estrutura de precificação e margem de contribuição de um negócio — mapeando o custo real de cada produto ou serviço, calculando a margem por item e identificando o que está gerando lucro, o que está no zero a zero e o que está consumindo caixa — para que o consultor entregue ao cliente uma visão clara de onde o dinheiro está sendo destruído e como precificar corretamente.
---

# Framework de Análise de Precificação e Margem

## Objetivo
Analisar a estrutura de precificação e margem de contribuição de um negócio — mapeando o custo real de cada produto ou serviço, calculando a margem por item e identificando o que está gerando lucro, o que está no zero a zero e o que está consumindo caixa — para que o consultor entregue ao cliente uma visão clara de onde o dinheiro está sendo destruído e como precificar corretamente.

## Quando usar
- Quando o cliente fatura bem mas não sobra dinheiro (sinal clássico de margem ruim)
- Quando quiser fazer uma análise de rentabilidade por produto ou serviço
- Quando o cliente nunca calculou o custo real do que vende
- Quando quiser identificar quais clientes ou contratos são mais lucrativos
- Quando precisar recomendar reajuste de preços com embasamento técnico

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Preencha com os dados de produtos/serviços, custos e preços praticados
3. Receba a análise de margem por item com recomendações de precificação
4. Use como base para a conversa de reajuste com o cliente

## O Prompt
```
Você é um consultor de precificação e rentabilidade com especialização em análise de margem de contribuição para PMEs de serviços e produtos. Seus princípios: (1) preço sem custo calculado é chute — e chute no escuro destrói margem silenciosamente, (2) margem de contribuição é a métrica que importa — não receita bruta, (3) nem todo produto ou cliente que "gera receita" gera lucro — identificar isso é o primeiro passo, (4) reajuste de preço com dados é argumento — sem dados é pedido.

Faça a análise de precificação e margem com as seguintes informações:

**Tipo de negócio:** [produto / serviço / misto]
**Lista de produtos ou serviços:** [liste cada um com o preço atual praticado]
**Custos diretos por produto/serviço:** [insumos, comissão, entrega, tempo do profissional — o que é variável por unidade]
**Custos fixos mensais totais:** [aluguel, salários fixos, sistemas, etc.]
**Volume de vendas por item (mensal):** [quantas unidades ou horas de cada]
**Impostos e taxas:** [% sobre faturamento — Simples, MEI, Lucro Presumido, etc.]
**Inadimplência média:** [% aproximado]
**Custo financeiro (se houver):** [parcelamento, antecipação de recebíveis, maquininha]

Entregue:

**1. Tabela de margem de contribuição por item**
| Produto/Serviço | Preço | Custos Variáveis | Margem Bruta (R$) | Margem Bruta (%) | Classificação |

Classificação: ✅ Saudável / ⚠️ Atenção / ❌ Crítico

**2. Análise de ponto de equilíbrio**
Quanto o negócio precisa vender por mês para cobrir todos os custos fixos — por produto e no total.

**3. Mapa de produtos campeões vs vilões**
Quais itens mais contribuem para o lucro real e quais estão destruindo margem.

**4. Recomendação de precificação**
Para cada item com problema: qual deveria ser o preço mínimo saudável e qual seria o preço ideal — com justificativa.

**5. Simulação de impacto**
Se implementar os preços recomendados: qual seria o impacto no faturamento e na margem líquida estimada.
```

## Exemplo de uso

### Input
- Negócio: Agência de marketing digital
- Serviços: Gestão de redes sociais R$1.800/mês / Tráfego pago R$2.500/mês / Criação de site R$3.500 único
- Custos diretos: Social media: 20h × R$45/h profissional = R$900 / Tráfego: 15h × R$45/h = R$675 / Site: 60h × R$45/h = R$2.700
- Fixos: R$18.000/mês (equipe + estrutura)
- Volume: 12 clientes social media, 8 tráfego, 2 sites/mês
- Impostos: 6% Simples

### Output
"❌ CRÍTICO — Gestão de Redes Sociais
Preço: R$1.800 | Custo direto: R$900 | Impostos: R$108 | Margem bruta: R$792 (44%)
Parece saudável, mas com 12 clientes, contribui R$9.504 para cobrir R$18.000 de fixo.
Sozinho, esse serviço não se paga. E se considerar retrabalho e reuniões não faturadas, a margem real cai para ~30%.
Preço mínimo saudável: R$2.200 | Preço ideal de mercado: R$2.800-3.200..."

---
**Tags:** Avançado | Análise | Financeiro, Jurídico & Compliance
