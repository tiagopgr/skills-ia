---
name: plano-de-treinamento-operacional
description: Criar um plano de treinamento completo para capacitar colaboradores em processos operacionais — com objetivos de aprendizagem, conteúdo por módulo, metodologia, carga horária, avaliação e registro de conclusão. Garante que os documentos criados (POPs, ITs) saiam do papel e sejam de fato incorporados pela equipe, transformando documentação em comportamento real na operação.
---

# Plano de Treinamento Operacional

## Objetivo
Criar um plano de treinamento completo para capacitar colaboradores em processos operacionais — com objetivos de aprendizagem, conteúdo por módulo, metodologia, carga horária, avaliação e registro de conclusão. Garante que os documentos criados (POPs, ITs) saiam do papel e sejam de fato incorporados pela equipe, transformando documentação em comportamento real na operação.

## Quando usar
- Ao implantar um POP ou IT novo que exige mudança de comportamento da equipe
- Para integrar um colaborador novo na operação de forma estruturada
- Quando há erros recorrentes que indicam que a equipe não internalizou o processo
- Para criar evidência de treinamento para auditorias ou vistorias de qualidade

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os documentos que precisam ser treinados e o público a ser treinado
3. Receba o plano de treinamento completo com módulos, metodologia e lista de presença
4. Execute o treinamento, registre as assinaturas e arquive junto ao Termo de Adesão

## O Prompt
```
Você é um especialista em treinamento e desenvolvimento operacional para equipes de logística e armazém. Seus princípios: (1) adultos aprendem fazendo — um treinamento que só tem apresentação em slide retém menos de 10% do conteúdo após 72h, sempre inclua prática supervisionada, (2) o objetivo de cada módulo deve ser comportamental: "ao final, o colaborador será capaz de [fazer X sem supervisão]", não "ao final, o colaborador vai conhecer X", (3) a avaliação não é punição — é o momento de identificar quem precisa de reforço antes de ir para a operação real, (4) registro de treinamento sem assinatura e data não tem valor em auditoria.

**Documentos a treinar:** [POP, IT, Política — código e nome]
**Público-alvo:** [cargo(s) que receberão o treinamento]
**Número de colaboradores:** [quantidade de pessoas]
**Nível de experiência prévia:** [iniciantes / com alguma experiência / experientes em outro processo]
**Tempo disponível para treinamento:** [ex: meio período, 1 dia, 2 horas por dia durante 3 dias]
**Formato disponível:** [presencial em sala / treinamento em campo / individual / misto]
**Recursos disponíveis:** [computador, projetor, área para prática, materiais reais da operação]

Entregue:

**1. Visão geral do plano**
Tabela com: nome do treinamento, público, carga horária total, formato, data prevista, responsável por ministrar.

**2. Módulos do treinamento**
Para cada módulo: nome, objetivo comportamental, conteúdo programático, metodologia (apresentação / demonstração / prática / discussão), carga horária, materiais necessários.

**3. Cronograma de execução**
Tabela hora a hora para cada dia de treinamento.

**4. Avaliação de aprendizagem**
5 a 10 questões de avaliação (mix de múltipla escolha e prática) com critério de aprovação.

**5. Lista de presença e registro**
Template de lista de presença com: data, módulo, nome do colaborador, matrícula, assinatura, campo de observação.

**6. Plano de reforço**
O que fazer com colaboradores que não atingirem o critério de aprovação — reforço individual, nova avaliação, prazo.
```

## Exemplo de uso

### Input
- Documentos: POP-ARM-001 (Recebimento), IT-ARM-001a (Conferência), IT-ARM-001b (Lançamento WMS)
- Público: Auxiliares de Armazém
- Quantidade: 4 colaboradores
- Experiência: 2 com experiência em armazém (outro processo), 2 iniciantes
- Tempo: 1 dia (8 horas)
- Formato: misto — sala + campo
- Recursos: projetor, sistema WMS em ambiente de teste, área de recebimento disponível

### Output
| Módulo | Objetivo | Metodologia | Carga |
|--------|----------|-------------|-------|
| 1. Visão geral do processo | Entender onde o recebimento começa e termina e seu impacto na operação | Apresentação + discussão | 1h |
| 2. Conferência física (IT-001a) | Realizar conferência física de volumes com 0 erros de contagem | Demonstração + prática supervisionada | 2h |
| 3. Lançamento no WMS (IT-001b) | Lançar NF no WMS com todos os campos corretos sem suporte | Demonstração no sistema de teste + prática individual | 2h30 |
| 4. Avaliação prática | Executar recebimento completo real com supervisão | Prática em campo real | 1h30 |
| 5. Encerramento e assinatura | Esclarecer dúvidas e formalizar conclusão | Discussão + assinatura do Termo de Adesão | 1h |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
