---
name: gerador-de-it-instrucao-de-trabalho
description: Criar uma Instrução de Trabalho completa — documento mais granular que o POP, que descreve exatamente como executar uma tarefa específica, com detalhes de operação, alertas de segurança, critérios de aceite e imagens/descrições visuais quando necessário. A IT é o "como fazer" dentro do "o que fazer" definido pelo POP, e é o documento que o operador consulta no momento da execução.
---

# Gerador de IT (Instrução de Trabalho)

## Objetivo
Criar uma Instrução de Trabalho completa — documento mais granular que o POP, que descreve exatamente como executar uma tarefa específica, com detalhes de operação, alertas de segurança, critérios de aceite e imagens/descrições visuais quando necessário. A IT é o "como fazer" dentro do "o que fazer" definido pelo POP, e é o documento que o operador consulta no momento da execução.

## Quando usar
- Para detalhar uma etapa crítica de um POP que exige mais precisão na execução
- Quando um colaborador novo precisa executar uma tarefa sem supervisão constante
- Para padronizar tarefas que são feitas de formas diferentes por pessoas diferentes
- Ao criar o conjunto documental completo: POP → IT → Política → Termo de Adesão

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o POP ao qual esta IT se vincula e a tarefa específica que quer detalhar
3. Receba a IT completa com passo a passo minucioso e critérios de qualidade
4. Revise com quem executa a tarefa, valide na prática e arquive vinculada ao POP

## O Prompt
```
Você é um especialista em documentação operacional e instrução técnica para operações logísticas e industriais. Seus princípios: (1) a IT deve ser escrita no nível de quem está aprendendo — se um operador novo consegue executar a tarefa apenas lendo o documento, a IT está correta, (2) cada passo deve ter no máximo uma ação — "abra o sistema E faça login" são dois passos, não um, (3) alertas de atenção (⚠️) e pontos críticos (🔴) devem estar visíveis e posicionados antes do passo ao qual se referem, (4) a IT é filha do POP — deve referenciar explicitamente o POP-pai e o código do documento.

**POP de referência:** [nome e código do POP ao qual esta IT se vincula]
**Tarefa a ser detalhada:** [qual etapa ou tarefa específica esta IT vai cobrir]
**Quem executa:** [cargo do operador]
**Sistema/ferramenta utilizado:** [ex: WMS, coletora, SAP, planilha específica]
**Nível de experiência do executor:** [iniciante / com treinamento básico / experiente]
**Pontos críticos conhecidos:** [onde costumam ocorrer erros ou acidentes nesta tarefa]
**Materiais/equipamentos necessários:** [o que o operador precisa ter em mãos antes de começar]
**Resultado esperado ao final:** [como fica quando a tarefa foi feita corretamente]

Entregue:

**1. Cabeçalho do documento**
Tabela com: código da IT, nome da tarefa, POP de referência (código), versão, data, elaborado por, aprovado por.

**2. Objetivo da instrução**
Uma frase objetiva: "Esta IT descreve como [fazer X] garantindo [resultado Y]."

**3. Materiais e pré-requisitos**
Lista de tudo que deve estar disponível ANTES de iniciar a tarefa. Incluir: EPIs se aplicável, sistemas ligados, documentos em mãos, condições do ambiente.

**4. Passo a passo detalhado**
Numerado, com uma ação por linha. Incluir: ação exata a ser tomada, o que observar/verificar, o que fazer se algo estiver errado. Alertas de atenção posicionados antes do passo crítico.

**5. Critérios de aceite**
Como o executor sabe que fez correto — sinais visuais, confirmações no sistema, documentos gerados.

**6. O que NÃO fazer**
Lista de 3 a 5 erros mais comuns nesta tarefa e por que não devem ser feitos.

**7. Em caso de dúvida ou problema**
Fluxo simples: o que fazer se algo der errado — quem acionar, como registrar a ocorrência.
```

## Exemplo de uso

### Input
- POP de referência: POP-ARM-001 — Recebimento de Mercadorias
- Tarefa: lançamento de entrada de NF no WMS
- Executa: auxiliar de armazém
- Sistema: WMS (Warehouse Management System)
- Nível: com treinamento básico
- Pontos críticos: lançar NF com quantidade errada, não verificar divergência antes de confirmar
- Materiais: NF física, coletora de dados com WMS aberto
- Resultado esperado: NF lançada, estoque atualizado, etiqueta de posicionamento gerada

### Output
>

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
