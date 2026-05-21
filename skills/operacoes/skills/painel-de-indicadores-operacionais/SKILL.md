---
name: painel-de-indicadores-operacionais
description: Definir os indicadores certos para cada departamento da empresa e estruturar um painel de acompanhamento gerencial — com métricas, metas, frequência de atualização e semáforos de alerta — para que o diretor monitore a saúde do negócio em uma única visão sem precisar ficar perguntando o que está acontecendo no operacional.
---

# Painel de Indicadores Operacionais

## Objetivo
Definir os indicadores certos para cada departamento da empresa e estruturar um painel de acompanhamento gerencial — com métricas, metas, frequência de atualização e semáforos de alerta — para que o diretor monitore a saúde do negócio em uma única visão sem precisar ficar perguntando o que está acontecendo no operacional.

## Quando usar
- Para criar pela primeira vez um sistema de indicadores para a empresa
- Quando o diretor não sabe o que está acontecendo a não ser que pergunte
- Para estruturar o que cada gerente precisa reportar toda semana
- Ao implantar uma cultura de gestão por resultados no time

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva os departamentos da empresa e o que importa medir em cada um
3. Receba o painel completo com KPIs, metas sugeridas e lógica de semáforo
4. Monte em uma planilha ou ferramenta de gestão e treine o time para atualizar

## O Prompt
```
Você é um especialista em gestão por indicadores (KPIs) para empresas de serviços. Seus princípios: (1) menos indicadores, mais foco — 3 KPIs bem acompanhados valem mais que 30 ignorados; (2) todo KPI precisa de meta, responsável e frequência de atualização; (3) indicadores de lagging (resultado) precisam ser complementados por indicadores de leading (processo); (4) o painel precisa ser simples o suficiente para qualquer gerente atualizar sem depender de TI.

Crie um painel de indicadores operacionais para a seguinte empresa:

**Tipo de empresa:** [ex: prestadora de serviços B2B, empresa de terceirização, consultoria]
**Número de funcionários:** [quantidade]
**Departamentos que existem:** [ex: operações, financeiro, RH, comercial, atendimento]
**Principal objetivo do negócio agora:** [ex: crescer receita, reduzir custo, melhorar retenção de clientes]
**Como as informações são registradas hoje:** [ex: planilha, ERP, nenhum sistema]
**O que o diretor mais precisa saber toda semana:** [quais perguntas o diretor fica fazendo]

Entregue:

**1. KPIs por departamento**
Para cada departamento: nome do indicador, o que mede, fórmula de cálculo, meta sugerida, frequência de atualização e responsável pelo preenchimento.

**2. KPIs estratégicos do diretor (visão consolidada)**
5-7 indicadores que o diretor precisa ver toda semana para ter a saúde do negócio em uma tela.

**3. Lógica de semáforo**
Para cada KPI estratégico: critério de verde (no caminho), amarelo (atenção) e vermelho (ação imediata necessária).

**4. Template de painel em tabela**
Estrutura pronta de planilha com colunas: KPI | Meta | Semana anterior | Semana atual | Tendência | Semáforo | Observações.

**5. Ritual de atualização**
Como e quando o time deve atualizar o painel e como o diretor deve usá-lo na reunião semanal.
```

## Exemplo de uso

### Input
- Empresa: Empresa de serviços de facilities (limpeza + manutenção) B2B
- Funcionários: 80
- Departamentos: Operações, Financeiro, RH, Comercial
- Objetivo: Reduzir custo operacional e melhorar retenção de contratos
- Sistemas: Planilha Google + WhatsApp
- Perguntas frequentes do diretor: "Quantos contratos renovaram?", "Como está o absenteísmo?", "Quanto faturamos esse mês?"

### Output
| KPI | Meta | Frequência | Semáforo Verde | Semáforo Amarelo | Semáforo Vermelho |
|-----|------|------------|----------------|------------------|-------------------|
| Taxa de renovação de contratos | ≥ 90% | Mensal | ≥ 90% | 80-89% | < 80% |
| Absenteísmo operacional | ≤ 4% | Semanal | ≤ 4% | 4-6% | > 6% |
| Margem bruta por contrato | ≥ 28% | Mensal | ≥ 28% | 22-27% | < 22% |
| NPS dos clientes ativos | ≥ 70 | Trimestral | ≥ 70 | 50-69 | < 50 |
| Custo de substituição de funcionário | ≤ R$800 | Mensal | ≤ R$800 | R$800-1.200 | > R$1.200 |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
