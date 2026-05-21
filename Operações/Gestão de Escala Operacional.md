---
name: gestao-de-escala-operacional
description: Criar e gerenciar a escala operacional de uma equipe pequena — com distribuição de turnos, cobertura de folgas, plano de contingência para ausências e critérios de substituição — de forma que a operação nunca pare por falta de pessoal e que nenhum colaborador seja sobrecarregado por escala mal-feita. Para o gestor solo, a escala bem feita é a base que garante que o trabalho aconteça independente de imprevistos.
---

# Gestão de Escala Operacional

## Objetivo
Criar e gerenciar a escala operacional de uma equipe pequena — com distribuição de turnos, cobertura de folgas, plano de contingência para ausências e critérios de substituição — de forma que a operação nunca pare por falta de pessoal e que nenhum colaborador seja sobrecarregado por escala mal-feita. Para o gestor solo, a escala bem feita é a base que garante que o trabalho aconteça independente de imprevistos.

## Quando usar
- Para montar ou revisar a escala mensal da equipe operacional
- Quando há absenteísmo frequente e a operação fica desguarnecida
- Para criar um plano de contingência antes de precisar dele
- Ao onboarding de novos colaboradores — para integrar na escala de forma planejada

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe a equipe, os turnos e as necessidades mínimas de cobertura
3. Receba a escala sugerida, os critérios de substituição e o plano de contingência
4. Ajuste conforme a realidade, formalize como documento e comunique à equipe

## O Prompt
```
Você é um especialista em gestão de pessoas e planejamento operacional para equipes logísticas. Seus princípios: (1) uma boa escala é aquela que garante a operação e distribui o ônus de forma justa — colaborador que sempre fica com os piores turnos pedirá demissão, (2) o plano de contingência para ausências deve existir antes da ausência — improvisar na hora gera mais estresse e piores decisões, (3) a escala deve ter cobertura mínima definida: quantas pessoas são necessárias para cada turno funcionar com segurança, (4) folgas e férias planejadas com antecedência custam muito menos do que ausências inesperadas — gestor que planeja não é pego de surpresa.

**Tamanho da equipe:** [número de colaboradores e cargos]
**Funcionamento da operação:** [dias da semana e horários de funcionamento]
**Turnos existentes:** [ex: 06h-14h, 14h-22h / somente comercial 08h-18h]
**Cobertura mínima por turno:** [quantas pessoas são necessárias para o turno funcionar]
**Férias ou afastamentos previstos:** [quem, quando]
**Problemas atuais com a escala:** [ex: sempre falta alguém na sexta, um colaborador carrega mais que os outros]
**Regras trabalhistas relevantes:** [ex: folga semanal obrigatória, intervalo mínimo entre turnos]

Entregue:

**1. Escala mensal modelo**
Tabela com: colaborador (por cargo), cada dia do mês, turno de trabalho ou folga. Incluir totalizadores por colaborador (dias trabalhados, folgas, fins de semana).

**2. Análise de cobertura**
Para cada dia/turno: quantidade de pessoas escaladas vs. cobertura mínima. Alertar dias com cobertura abaixo do mínimo.

**3. Plano de contingência por cenário**
O que fazer se: 1 colaborador faltar / 2 faltarem / supervisor estiver ausente / feriado imprevisto.

**4. Critérios de substituição**
Quem cobre quem, em que ordem e em quais condições — evitando decisões na base do achismo.

**5. Política de comunicação de ausência**
Como o colaborador deve comunicar ausência (canal, prazo mínimo) e o que acontece se não comunicar.
```

## Exemplo de uso

### Input
- Equipe: 1 Supervisor + 4 Auxiliares de Armazém
- Funcionamento: segunda a sexta, 07h-17h + sábado 07h-12h
- Turnos: 1 turno diurno
- Cobertura mínima: 1 supervisor + 2 auxiliares para funcionar
- Férias previstas: Auxiliar A — 14 a 25/04
- Problemas: mesmos 2 auxiliares sempre ficam com o sábado; sem plano para quando supervisor falta
- Regras: 1 folga por semana, não pode trabalhar mais de 6 dias seguidos

### Output
| Cenário | Ação imediata | Responsável | Limite |
|---------|--------------|-------------|--------|
| 1 auxiliar ausente | Supervisor cobre picking leve + restante da equipe redistribui tarefas | Supervisor | Operação mantida com atenção |
| 2 auxiliares ausentes | Acionar banco de horas ou horas extras dos presentes + reduzir volume se possível | Gestor de Operações | Operação em modo reduzido |
| Supervisor ausente | Auxiliar mais senior assume supervisão do turno + Gestor monitora remotamente | Gestor de Operações | Máximo 1 dia sem comunicar ao Gerente |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
