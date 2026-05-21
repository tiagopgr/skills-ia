---
name: gerador-de-termo-de-adesao
description: Criar um Termo de Adesão completo — documento assinado pelo colaborador que formaliza o conhecimento, o entendimento e o comprometimento com as diretrizes de uma Política, POP ou conjunto de normas operacionais. O Termo de Adesão é o elo que transforma documentos normativos em compromissos individuais rastreáveis, criando respaldo formal em caso de descumprimento e evidência de comunicação em auditorias.
---

# Gerador de Termo de Adesão

## Objetivo
Criar um Termo de Adesão completo — documento assinado pelo colaborador que formaliza o conhecimento, o entendimento e o comprometimento com as diretrizes de uma Política, POP ou conjunto de normas operacionais. O Termo de Adesão é o elo que transforma documentos normativos em compromissos individuais rastreáveis, criando respaldo formal em caso de descumprimento e evidência de comunicação em auditorias.

## Quando usar
- Sempre que uma Política ou POP crítico for implantado ou atualizado
- Para criar o registro formal de que o colaborador foi informado e concordou com as regras
- Quando precisar de evidência documental para RH, auditoria ou processo disciplinar
- Para completar o conjunto documental: POP ↔ IT ↔ Política ↔ **Termo de Adesão**

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os documentos aos quais o Termo se vincula e as obrigações principais
3. Receba o Termo completo em linguagem formal e acessível
4. Imprima ou digitalize para assinatura, arquive no prontuário do colaborador

## O Prompt
```
Você é um especialista em documentação de RH, compliance e gestão de pessoas para operações logísticas. Seus princípios: (1) o Termo de Adesão deve usar linguagem formal mas compreensível — o colaborador deve entender o que está assinando, não apenas assinar, (2) o Termo deve referenciar explicitamente os documentos aos quais se vincula, com código e nome, para que não haja dúvida sobre o escopo do compromisso, (3) o Termo deve incluir uma declaração de ciência — o assinante declara que leu, entendeu e teve oportunidade de esclarecer dúvidas, (4) o Termo deve ter campo para data, assinatura do colaborador, assinatura da testemunha e assinatura do responsável pela aplicação.

**Documentos vinculados ao Termo:** [liste os POPs, ITs e Políticas que este Termo cobre]
**Cargo(s) que devem assinar:** [quem é o público deste Termo]
**Obrigações principais que o colaborador está assumindo:** [as responsabilidades-chave que precisam estar explícitas]
**Consequências do descumprimento:** [mencionar que estão detalhadas na Política vinculada]
**Empresa/organização:** [nome da empresa ou deixar em branco para preencher depois]
**Haverá treinamento antes da assinatura?** [sim / não — influencia o texto de declaração de ciência]

Entregue:

**1. Cabeçalho do documento**
Identificação do Termo com: código, nome, versão, data, documentos vinculados.

**2. Qualificação das partes**
Bloco para preenchimento dos dados do colaborador (nome, CPF, cargo, matrícula, unidade) e da empresa.

**3. Objeto do Termo**
Parágrafo descrevendo o que o colaborador está aderindo — referenciando os documentos pelo código e nome.

**4. Das obrigações do colaborador**
Lista numerada das obrigações principais assumidas pelo assinante.

**5. Das obrigações da empresa**
Lista das contrapartidas da empresa (fornecer treinamento, disponibilizar documentos, comunicar atualizações).

**6. Declaração de ciência e entendimento**
Parágrafo formal onde o colaborador declara ter lido, entendido, participado de treinamento (se aplicável) e tido oportunidade de esclarecer dúvidas.

**7. Das penalidades**
Parágrafo referenciando a Política vinculada para as consequências do descumprimento, sem repetir o conteúdo.

**8. Da vigência**
Prazo de validade do Termo e condições de renovação.

**9. Campos de assinatura**
Blocos para: data e local, assinatura e nome legível do colaborador, assinatura e nome do responsável pela aplicação, assinatura de 1 testemunha.
```

## Exemplo de uso

### Input
- Documentos vinculados: POL-ARM-001 (Política de Acesso ao Armazém), POP-ARM-001 (Recebimento), IT-ARM-001 (Lançamento de NF)
- Cargo: Auxiliar de Armazém
- Obrigações: uso de EPI, cumprimento dos POPs, registro correto no WMS, comunicar divergências
- Consequências: conforme POL-ARM-001
- Empresa: [nome da empresa]
- Treinamento: sim, realizado antes da assinatura

### Output
>

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
