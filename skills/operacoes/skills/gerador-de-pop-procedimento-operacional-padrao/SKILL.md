---
name: gerador-de-pop-procedimento-operacional-padrao
description: Criar um Procedimento Operacional Padrão completo — com objetivo, escopo, responsabilidades, fluxo de etapas, critérios de qualidade e referências cruzadas — para qualquer processo logístico ou operacional. O POP é o documento-mestre que garante que o processo seja executado da mesma forma, por qualquer pessoa, em qualquer momento, eliminando variação e retrabalho.
---

# Gerador de POP (Procedimento Operacional Padrão)

## Objetivo
Criar um Procedimento Operacional Padrão completo — com objetivo, escopo, responsabilidades, fluxo de etapas, critérios de qualidade e referências cruzadas — para qualquer processo logístico ou operacional. O POP é o documento-mestre que garante que o processo seja executado da mesma forma, por qualquer pessoa, em qualquer momento, eliminando variação e retrabalho.

## Quando usar
- Para documentar um processo que depende de uma só pessoa e precisa ser transferido
- Quando um processo é executado de formas diferentes por pessoas diferentes da equipe
- Ao implantar um processo novo que precisa ser padronizado desde o início
- Para criar a base documental que alimentará as ITs, Políticas e Termos de Adesão vinculados

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo que quer documentar com o máximo de detalhes que você já conhece
3. Receba o POP completo formatado e pronto para revisar e assinar
4. Revise as etapas, ajuste conforme a realidade da operação e arquive no sistema de gestão

## O Prompt
```
Você é um especialista em gestão de processos e documentação operacional com foco em operações logísticas. Seus princípios: (1) um POP eficaz é escrito para quem nunca fez o processo — se quem leu consegue executar sem perguntar, o documento está bom, (2) o nível de detalhe deve ser proporcional ao risco do processo — quanto maior o impacto de um erro, mais granular deve ser o passo a passo, (3) cada etapa do POP deve ter um responsável claro, uma entrada (input) e uma saída (output) identificáveis, (4) o POP deve ser um documento vivo — com número de versão, data de revisão e campo de aprovação.

**Nome do processo:** [ex: Recebimento de Mercadorias, Separação de Pedidos, Controle de Estoque]
**Área/setor:** [ex: armazém, transporte, expedição, atendimento]
**Objetivo do processo:** [o que este processo entrega quando bem-feito]
**Quem executa:** [cargo(s) responsável(is) pela execução]
**Quem aprova/supervisiona:** [gestor responsável]
**Entradas do processo:** [o que precisa estar disponível para o processo começar]
**Saídas do processo:** [o que é gerado ao final]
**Etapas que você já conhece:** [descreva livremente o que sabe — pode ser incompleto]
**Documentos relacionados:** [outros POPs, ITs, formulários ou políticas ligadas a este processo]
**Ferramentas/sistemas utilizados:** [ex: WMS, ERP, planilha, coletora]

Entregue:

**1. Cabeçalho do documento**
Tabela com: código do documento, nome do processo, versão, data de emissão, data de revisão, elaborado por, aprovado por, área.

**2. Objetivo e escopo**
Parágrafo de objetivo (o que o processo faz) e parágrafo de escopo (onde começa, onde termina, o que inclui e o que está fora do escopo).

**3. Definições e siglas**
Glossário com os termos técnicos e siglas utilizados no documento.

**4. Responsabilidades**
Tabela com cargo, responsabilidade dentro do processo e nível de autoridade (executa / supervisiona / aprova).

**5. Descrição do processo — passo a passo**
Tabela com: número da etapa, descrição da ação, responsável, ferramenta/sistema utilizado, critério de qualidade (como saber que foi feito corretamente), documento gerado.

**6. Fluxograma textual**
Representação do fluxo em formato texto (Início → Etapa 1 → Decisão → Etapa 2...) para quem não tem ferramenta de diagramas.

**7. Indicadores do processo**
2 a 3 métricas para monitorar se o processo está sendo cumprido corretamente.

**8. Histórico de revisões**
Tabela para registrar futuras atualizações do documento.

**9. Referências cruzadas**
Lista dos documentos que se conectam a este POP: ITs vinculadas, políticas aplicáveis, formulários utilizados.
```

## Exemplo de uso

### Input
- Nome: Recebimento de Mercadorias
- Área: Armazém
- Objetivo: garantir que toda mercadoria recebida seja conferida, registrada e armazenada corretamente
- Executa: auxiliar de armazém
- Aprova: supervisor de armazém
- Entradas: nota fiscal, mercadoria física, ordem de compra
- Saídas: entrada no sistema, mercadoria posicionada, nota conferida
- Etapas conhecidas: receber NF, conferir volumes, lançar no sistema, posicionar
- Ferramentas: WMS, coletora de dados

### Output
| Etapa | Ação | Responsável | Ferramenta | Critério de Qualidade |
|-------|------|-------------|------------|----------------------|
| 1 | Receber a NF do transportador e verificar se o CNPJ do emitente corresponde ao fornecedor esperado | Auxiliar de Armazém | NF física + OC impressa | NF aceita somente se CNPJ e número do pedido conferem |
| 2 | Contar os volumes fisicamente e comparar com a quantidade descrita na NF | Auxiliar de Armazém | Coletora / planilha | Divergência de qualquer volume deve ser registrada antes de assinar o canhoto |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
