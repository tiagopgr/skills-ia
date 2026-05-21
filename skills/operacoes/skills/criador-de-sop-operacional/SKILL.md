---
name: criador-de-sop-operacional
description: Transformar qualquer processo que vive na cabeça de alguém em um documento de procedimento operacional padrão (SOP) claro, seguível e auditável — com passo a passo, responsáveis, critérios de qualidade e pontos de controle — para que qualquer colaborador execute o processo com o mesmo padrão, sem precisar perguntar ao gestor.
---

# Criador de SOP Operacional

## Objetivo
Transformar qualquer processo que vive na cabeça de alguém em um documento de procedimento operacional padrão (SOP) claro, seguível e auditável — com passo a passo, responsáveis, critérios de qualidade e pontos de controle — para que qualquer colaborador execute o processo com o mesmo padrão, sem precisar perguntar ao gestor.

## Quando usar
- Quando um processo depende de uma única pessoa para funcionar direito
- Ao padronizar rotinas de um departamento antes de delegar para um líder
- Para documentar como as coisas funcionam antes de contratar ou promover alguém
- Quando erros se repetem porque "cada um faz do seu jeito"

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo que quer documentar (pode ser bruto, em tópicos)
3. Receba o SOP formatado com etapas, responsáveis e critérios de qualidade
4. Adapte nomes de cargos e ferramentas para a sua realidade e distribua ao time

## O Prompt
```
Você é um consultor de excelência operacional especializado em documentar e padronizar processos em empresas de serviços. Seus princípios: (1) clareza acima de completude — um SOP que ninguém entende não serve; (2) cada etapa deve ter dono e prazo claro; (3) pontos de controle previnem retrabalho; (4) o SOP deve ser seguível por alguém sem experiência anterior no processo.

Crie um SOP completo para o seguinte processo:

**Processo:** [descreva o processo que quer documentar — pode ser em tópicos ou texto livre]
**Departamento responsável:** [ex: financeiro, operações, RH, atendimento]
**Cargo que executa:** [ex: assistente administrativo, coordenador, gerente]
**Ferramentas usadas:** [ex: Excel, ERP, WhatsApp, Google Drive]
**Frequência:** [diário / semanal / mensal / sob demanda]
**Principal erro que acontece hoje:** [o que costuma dar errado nesse processo]

Entregue:

**1. Cabeçalho do SOP**
Nome do processo, código de referência, versão, data, responsável pelo processo e objetivo em uma linha.

**2. Escopo e aplicação**
Para quem se aplica, quando começa e quando termina o processo.

**3. Passo a passo detalhado**
Tabela com: Nº da etapa | Ação | Responsável | Ferramenta | Critério de qualidade | O que fazer se der errado

**4. Pontos de controle (checkpoints)**
Liste os 3-5 momentos críticos onde é obrigatório verificar se está tudo certo antes de continuar.

**5. Indicadores do processo**
2-3 métricas simples para saber se o processo está sendo seguido corretamente.

**6. Histórico de revisões**
Tabela em branco com colunas: Versão | Data | Alteração | Aprovado por
```

## Exemplo de uso

### Input
- Processo: Fechamento de caixa diário da loja
- Departamento: Financeiro
- Cargo: Assistente financeiro
- Ferramentas: Excel, sistema de PDV, WhatsApp
- Frequência: Diário
- Principal erro: Esquece de reconciliar sangrias e o caixa fecha errado

### Output
| Nº | Ação | Responsável | Ferramenta | Critério de qualidade | Se der errado |
|----|------|-------------|------------|-----------------------|---------------|
| 1 | Imprimir relatório de vendas do dia | Assistente financeiro | PDV | Relatório com data correta e assinado | Acionar TI e registrar ocorrência |
| 2 | Conferir total de sangrias registradas | Assistente financeiro | Excel – aba "sangrias" | Cada sangria tem hora, valor e assinatura do responsável | Não fechar caixa — escalar para gerente |
| 3 | Reconciliar dinheiro físico + débito + crédito | Assistente financeiro | Excel – aba "fechamento" | Diferença máxima tolerada: R$5,00 | Registrar divergência e aguardar validação do gerente |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
