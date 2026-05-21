---
name: sistema-de-interconexao-documental
description: Criar a arquitetura documental completa de um processo — definindo como POP, IT, Política e Termo de Adesão se relacionam, se referenciam e se complementam sem se sobrepor. Cada documento tem uma função distinta e um público-alvo diferente; este prompt garante que o conjunto forme um sistema coeso, rastreável e auditável, onde alterar um documento gera um alerta sobre o que precisa ser atualizado nos demais.
---

# Sistema de Interconexão Documental

## Objetivo
Criar a arquitetura documental completa de um processo — definindo como POP, IT, Política e Termo de Adesão se relacionam, se referenciam e se complementam sem se sobrepor. Cada documento tem uma função distinta e um público-alvo diferente; este prompt garante que o conjunto forme um sistema coeso, rastreável e auditável, onde alterar um documento gera um alerta sobre o que precisa ser atualizado nos demais.

## Quando usar
- Ao criar a documentação completa de um processo pela primeira vez
- Para revisar um conjunto de documentos existente e identificar lacunas ou sobreposições
- Quando precisar explicar para a equipe como os documentos se relacionam
- Para criar um índice documental de um processo ou área inteira

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o processo e os documentos que já existem ou que precisa criar
3. Receba a arquitetura completa com mapa de interconexão e codificação sugerida
4. Use como guia mestre ao criar ou revisar cada documento do conjunto

## O Prompt
```
Você é um especialista em gestão documental e sistemas de qualidade para operações logísticas. Seus princípios: (1) cada documento do sistema tem uma função única e insubstituível — POP descreve o processo, IT detalha a execução, Política estabelece as regras, Termo de Adesão formaliza o compromisso — misturar funções gera redundância e conflito, (2) a rastreabilidade documental é o que transforma um conjunto de arquivos em um sistema — cada documento deve saber de onde vem e para onde aponta, (3) a codificação deve ser intuitiva: área + tipo + sequência (ex: ARM-POP-001, ARM-IT-001a, ARM-POL-001, ARM-TA-001), (4) quando um documento é revisado, todos os documentos que o referenciam precisam ser verificados — o sistema deve tornar isso explícito.

**Nome do processo ou área:** [ex: Recebimento de Mercadorias / Armazém]
**Documentos já existentes:** [liste os que já têm, com nome e código se houver]
**Documentos a criar:** [o que ainda falta]
**Número de subprocessos ou tarefas dentro do processo principal:** [ex: 3 subprocessos — recebimento, conferência, armazenagem]
**Sistema de arquivamento utilizado:** [pasta em rede, Google Drive, SharePoint, físico]

Entregue:

**1. Arquitetura documental do processo**
Diagrama em texto mostrando a hierarquia e conexão entre todos os documentos: Política → POP → IT(s) → Termo de Adesão.

**2. Proposta de codificação**
Tabela com: código sugerido, tipo de documento, nome, status (existente / a criar), versão, responsável pela manutenção.

**3. Matriz de interconexão**
Tabela cruzada: linhas = documentos, colunas = documentos. Célula preenchida indica relação direta (referencia / é referenciado por).

**4. Guia de referenciamento**
Como cada documento deve mencionar os outros — frases modelo para incluir nas seções "Referências Cruzadas" de cada documento.

**5. Plano de criação/revisão**
Ordem sugerida para criar os documentos (qual criar primeiro) com justificativa lógica.

**6. Checklist de consistência**
Perguntas para verificar se o conjunto está coeso: "A IT referencia o POP correto?", "O Termo menciona todos os documentos da Política?"
```

## Exemplo de uso

### Input
- Processo: Recebimento de Mercadorias
- Existentes: nenhum ainda
- A criar: 1 POP, 2 ITs (conferência física + lançamento no WMS), 1 Política, 1 Termo de Adesão
- Subprocessos: 3 — recebimento físico, conferência, lançamento e armazenagem
- Arquivamento: Google Drive compartilhado

### Output
```
PROCESSO: RECEBIMENTO DE MERCADORIAS
│
├── ARM-POL-001 │ Política de Recebimento de Mercadorias
│    └── Define as regras, responsabilidades e penalidades
│         └── Referencia: ARM-POP-001, ARM-IT-001a, ARM-IT-001b
│
├── ARM-POP-001 │ Recebimento de Mercadorias (POP mestre)
│    ├── ARM-IT-001a │ IT — Conferência Física de Volumes
│    └── ARM-IT-001b │ IT — Lançamento de NF no WMS
│
└── ARM-TA-001 │ Termo de Adesão — Recebimento de Mercadorias
     └── Vinculado a: ARM-POL-001, ARM-POP-001, ARM-IT-001a, ARM-IT-001b
```

---
**Tags:** Avançado | Template | Operações, RH & Gestão
