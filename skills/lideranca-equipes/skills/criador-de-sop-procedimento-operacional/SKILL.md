---
name: criador-de-sop-procedimento-operacional
description: Criar SOPs (Standard Operating Procedures) claros e utilizáveis — documentos que permitem a qualquer pessoa da equipe executar um processo corretamente, sem depender de quem 'sabe de cabeça'.
---

# Criador de SOP (Procedimento Operacional)

## Objetivo
Criar SOPs (Standard Operating Procedures) claros e utilizáveis — documentos que permitem a qualquer pessoa da equipe executar um processo corretamente, sem depender de quem 'sabe de cabeça'.

## Quando usar
- Para documentar processos que só uma pessoa sabe fazer
- Ao treinar novos funcionários
- Quando erros operacionais se repetem
- Para escalar operações sem perder qualidade

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo que quer documentar
3. Receba o SOP completo e estruturado
4. Revise com quem executa o processo e publique

## O Prompt
```
Você é um especialista em processos operacionais que sabe que: (1) se não está documentado, não existe — está na cabeça de alguém, (2) um SOP bom é seguido, um ruim fica na gaveta, (3) SOPs devem ser escritos para a pessoa menos experiente da equipe conseguir executar.

Crie o SOP para:

**Nome do processo:** [ex: "Onboarding de novo cliente"]
**Departamento:** [ex: Operações, Marketing, Financeiro, RH]
**Quem executa:** [cargo/função responsável]
**Frequência:** [diário, semanal, por demanda]
**Ferramentas usadas:** [sistemas, software, planilhas]
**Objetivo do processo:** [o que deve ser alcançado]
**Problemas comuns:** [o que costuma dar errado]

Estruture o SOP:
1. Cabeçalho (título, código, versão, responsável)
2. Objetivo
3. Escopo (coberto e NÃO coberto)
4. Pré-requisitos
5. Passo a passo detalhado (com checagem)
6. Exceções e troubleshooting
7. Checklist de qualidade
8. Métricas do processo
9. Histórico de alterações
```

## Exemplo de uso

### Input
Processo: Publicação de post no Instagram do cliente
Departamento: Social Media
Quem executa: Analista de conteúdo
Frequência: Diário
Ferramentas: Canva, mLabs, Google Drive, Trello
Problema comum: Postar sem aprovação do cliente, erros de texto

### Output
Passo 3: Acesse o Trello → Board do cliente → Lista 'Aprovado para publicação'. Confirme que o card do post tem a etiqueta verde (= cliente aprovou). NUNCA publique card sem etiqueta verde.

Passo 4: Abra o criativo no Canva. Verifique: (a) texto sem erros, (b) formato correto (1080x1080 feed / 1080x1920 stories), (c) logo do cliente visível.

Passo 5: No mLabs, selecione o perfil → 'Novo post'. Upload da imagem. Cole a legenda do Trello. Verifique hashtags (máx. 15). Agende para o horário do calendário editorial.

Troubleshooting: "E se o cliente pediu alteração depois da aprovação?" → Mova o card para 'Em revisão', aplique alteração, solicite nova aprovação pelo WhatsApp.

---
**Tags:** Intermediário | Template | Liderança & Equipes
