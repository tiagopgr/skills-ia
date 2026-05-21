---
name: organizacao-de-processos-e-rotinas-da-equipe
description: Mapear, documentar e organizar os processos e rotinas de uma equipe pequena — com fluxogramas em texto, checklists de execução e responsabilidades claras por função — para que as atividades aconteçam da mesma forma toda vez, independentemente de quem está executando. Substitui a dependência da memória e da pessoa certa pelo processo documentado, reduzindo erros, retrabalho e custo com treinamentos constantes.
---

# Organização de Processos e Rotinas da Equipe

## Objetivo
Mapear, documentar e organizar os processos e rotinas de uma equipe pequena — com fluxogramas em texto, checklists de execução e responsabilidades claras por função — para que as atividades aconteçam da mesma forma toda vez, independentemente de quem está executando. Substitui a dependência da memória e da pessoa certa pelo processo documentado, reduzindo erros, retrabalho e custo com treinamentos constantes.

## Quando usar
- Para documentar como a equipe executa as principais atividades e criar um manual operacional
- Ao integrar um novo colaborador e querer que aprenda rápido sem depender de você o tempo todo
- Quando uma atividade recorrente estiver dando resultado inconsistente porque depende de quem faz
- Para reduzir a necessidade de contratar alguém novo ao distribuir melhor o que já existe

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo ou rotina que quer organizar, seus passos e quem está envolvido
3. Receba o processo documentado com fluxo, checklist, responsáveis e pontos de controle
4. Salve no Notion, Google Drive ou impresso e treine a equipe usando o documento

## O Prompt
```
Você é um especialista em gestão de operações e documentação de processos para pequenas equipes e empresas em crescimento. Seus princípios: (1) processo documentado é processo que existe independente da pessoa — se só está na cabeça de alguém, não é processo, é dependência, (2) o nível de detalhe do processo deve ser proporcional ao risco de erro — processo complexo com alto risco precisa de mais detalhe, processo simples pode ser só um checklist, (3) responsabilidade sem critério de conclusão é responsabilidade sem fim — cada etapa precisa de um sinal claro de "feito", (4) processo que ninguém segue não vale o papel em que foi escrito — simplicidade e usabilidade são mais importantes do que completude.

Documente o processo ou rotina com base nas informações abaixo:

**Nome do processo:** [ex: abertura do dia / onboarding de cliente / fechamento mensal / atendimento ao cliente]
**Objetivo do processo:** [o que precisa ter acontecido quando estiver completo]
**Frequência:** [diário / semanal / mensal / por demanda]
**Quem executa:** [cargos ou nomes envolvidos]
**Ferramentas usadas:** [sistemas, planilhas, apps, físico]
**Passos que você já conhece:** [liste mesmo que incompletos]
**Pontos onde costuma dar errado:** [onde há inconsistência ou erro hoje]
**Critério de conclusão:** [como saber que o processo foi bem feito]

Entregue:

**1. Ficha do processo**
Nome, objetivo, frequência, responsável principal, tempo estimado, ferramentas.

**2. Fluxo passo a passo**
Cada etapa com: número | descrição da ação | responsável | ferramenta | critério de conclusão | tempo estimado.

**3. Checklist de execução**
Versão resumida em formato de lista para marcar durante a execução — máx 15 itens.

**4. Pontos de controle**
Momentos no processo em que o gestor deve verificar se tudo está correndo bem antes de continuar.

**5. O que fazer quando algo dá errado**
Protocolo para as 3 falhas mais comuns neste processo.

**6. Indicador de qualidade**
Como medir se o processo está sendo bem executado — 1 ou 2 métricas simples.
```

## Exemplo de uso

### Input
- Processo: Fechamento financeiro mensal
- Objetivo: Ter todos os lançamentos do mês conferidos, relatório gerado e enviado para gestão
- Frequência: Mensal — todo dia 1 do mês seguinte
- Quem executa: Analista financeiro + gestor (revisão)
- Ferramentas: Planilha Excel + sistema ERP + e-mail
- Pontos de falha: Analista esquece de incluir lançamentos de cartão / gestor não revisa antes de enviar

### Output
☐ Exportar extrato bancário do mês completo
☐ Conferir todos os lançamentos de cartão (crédito e débito)
☐ Lançar despesas não registradas no ERP
☐ Conciliar ERP com extrato bancário — diferença deve ser zero
☐ Calcular receita total, despesas por categoria e resultado líquido
☐ Preencher aba "Histórico" na planilha mestre com os dados do mês
☐ Gerar relatório no template padrão
☐ Enviar para revisão do gestor até dia 2 às 12h
☐ Gestor revisa e aprova ou devolve com comentários até dia 3
☐ Enviar versão final para sócios/diretores até dia 3 às 18h

---
**Tags:** Iniciante | Template | Operações, RH & Gestão
