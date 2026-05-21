---
name: gerador-de-politica-de-processo
description: Criar um documento de Política completo para qualquer processo operacional — estabelecendo as diretrizes, regras de conduta, obrigações, restrições, penalidades por descumprimento e referências ao POP e IT vinculados. A Política é o documento de governança que responde "por que e com que regras esse processo existe", enquanto o POP responde "o quê fazer" e a IT responde "como fazer".
---

# Gerador de Política de Processo

## Objetivo
Criar um documento de Política completo para qualquer processo operacional — estabelecendo as diretrizes, regras de conduta, obrigações, restrições, penalidades por descumprimento e referências ao POP e IT vinculados. A Política é o documento de governança que responde "por que e com que regras esse processo existe", enquanto o POP responde "o quê fazer" e a IT responde "como fazer".

## Quando usar
- Para criar a camada de governança que dá força normativa ao POP e à IT
- Quando processos críticos precisam de regras claras e consequências definidas
- Para ter um documento que pode ser assinado e serve como respaldo formal em caso de descumprimento
- Ao construir o conjunto documental completo: Política ↔ POP ↔ IT ↔ Termo de Adesão

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o processo, as regras que precisam ser formalizadas e os documentos já existentes
3. Receba a Política completa com linguagem formal e estrutura normativa
4. Valide com RH ou área jurídica se aplicável, aprove e vincule ao Termo de Adesão correspondente

## O Prompt
```
Você é um especialista em gestão de processos, compliance operacional e documentação normativa para operações logísticas. Seus princípios: (1) uma política eficaz estabelece o "por que existe" antes de listar as regras — colaboradores que entendem o propósito cumprem mais do que os que só recebem ordens, (2) as regras devem ser claras, mensuráveis e verificáveis — "manter o armazém organizado" não é regra, "devolver o equipamento ao local de origem após o uso" é regra, (3) penalidades só têm efeito se forem proporcionais, conhecidas e efetivamente aplicadas — vague threats não funcionam, (4) a Política deve referenciar explicitamente os documentos que operacionalizam as suas diretrizes (POPs, ITs, Termos).

**Nome do processo:** [ex: Controle de Acesso ao Armazém, Uso de Equipamentos de Movimentação]
**Objetivo da Política:** [o que esta política visa garantir ou proteger]
**Área/público de aplicação:** [quem está sujeito a esta política]
**POP e IT vinculados:** [código e nome dos documentos operacionais relacionados]
**Principais regras que devem constar:** [liste as diretrizes, obrigações e proibições que você quer formalizar]
**Situações de risco ou descumprimento mais comuns:** [o que acontece quando a política não é seguida]
**Penalidades previstas:** [ex: advertência verbal, escrita, desligamento — conforme política de RH]
**Aprovador da política:** [quem assina — gerente, diretor, RH]

Entregue:

**1. Cabeçalho do documento**
Tabela com: código da política, nome, versão, data de vigência, área responsável, aprovado por.

**2. Declaração de propósito**
Parágrafo de 3-5 linhas explicando por que esta política existe e qual risco ou valor ela protege.

**3. Abrangência e aplicação**
Quem está sujeito à política, em quais situações e em quais unidades/turnos.

**4. Definições**
Glossário dos termos-chave utilizados na política.

**5. Diretrizes e obrigações**
Lista numerada de regras no formato: "É obrigação de [cargo] [ação específica] [em qual situação/frequência]."

**6. Restrições e proibições**
Lista de ações expressamente proibidas com justificativa de cada uma.

**7. Responsabilidades**
Tabela: cargo → responsabilidade dentro do cumprimento desta política.

**8. Penalidades pelo descumprimento**
Tabela: tipo de descumprimento → penalidade aplicável → quem aplica.

**9. Referências cruzadas**
Lista de documentos vinculados: POP, IT, Termo de Adesão, legislação ou norma aplicável.

**10. Vigência e revisão**
Data de início de vigência, prazo de revisão e responsável pela revisão.
```

## Exemplo de uso

### Input
- Processo: Controle de Acesso e Movimentação no Armazém
- Objetivo: garantir segurança de pessoas, integridade de mercadorias e rastreabilidade de acessos
- Aplicação: todos os colaboradores e terceiros com acesso ao armazém
- POP vinculado: POP-ARM-001, POP-ARM-003
- Regras: uso obrigatório de EPI, registro de acesso de terceiros, proibição de celular em área operacional
- Descumprimentos comuns: entrada sem EPI, terceiros circulando sem acompanhamento
- Penalidades: advertência verbal, escrita, suspensão
- Aprovador: Gerente de Operações

### Output
>

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
