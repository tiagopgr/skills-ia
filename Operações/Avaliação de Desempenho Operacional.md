---
name: avaliacao-de-desempenho-operacional
description: Criar um formulário completo de avaliação de desempenho para colaboradores operacionais — com critérios técnicos e comportamentais, escala de avaliação, espaço para autoavaliação, resultado consolidado e plano de ação vinculado — para que a avaliação seja um processo estruturado, justo e útil para o desenvolvimento da equipe, não apenas uma burocracia semestral sem efeito prático.
---

# Avaliação de Desempenho Operacional

## Objetivo
Criar um formulário completo de avaliação de desempenho para colaboradores operacionais — com critérios técnicos e comportamentais, escala de avaliação, espaço para autoavaliação, resultado consolidado e plano de ação vinculado — para que a avaliação seja um processo estruturado, justo e útil para o desenvolvimento da equipe, não apenas uma burocracia semestral sem efeito prático.

## Quando usar
- Para conduzir avaliações periódicas (mensal, trimestral ou semestral) da equipe
- Quando precisar de critérios objetivos para decisões de promoção, reajuste ou desligamento
- Para substituir a avaliação informal ("achei que ele foi bem") por um registro confiável
- Como base para construir o PDI do colaborador após a avaliação

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o cargo avaliado, os critérios que importam para a função e a escala desejada
3. Receba o formulário completo pronto para usar
4. Aplique com cada colaborador, consolide o resultado e construa o PDI em seguida

## O Prompt
```
Você é um especialista em gestão de desempenho e desenvolvimento de equipes operacionais. Seus princípios: (1) uma avaliação justa mede o que o colaborador pode controlar — não avalie pela sorte, pelo contexto ou por fatores fora do alcance dele, (2) critérios vagos geram avaliações tendenciosas — "comprometimento" sem descrição do que constitui comprometimento na prática não serve como critério avaliativo, (3) a autoavaliação é parte do processo — o colaborador que discorda significativamente do gestor está sinalizando um problema de comunicação que precisa ser tratado, (4) a avaliação só tem valor se gerar uma conversa e um plano de ação — formulário sem feedback é dados sem uso.

**Cargo a ser avaliado:** [ex: Auxiliar de Armazém, Supervisor Operacional]
**Frequência da avaliação:** [mensal / trimestral / semestral]
**Principais responsabilidades do cargo:** [o que é esperado desta função]
**Critérios técnicos prioritários:** [habilidades operacionais que devem ser avaliadas]
**Critérios comportamentais prioritários:** [soft skills relevantes para a função]
**Escala de avaliação:** [ex: 1-5 / Abaixo/Atende/Supera / Percentual de cumprimento]
**Haverá autoavaliação?** [sim / não]
**O que acontece com o resultado:** [apenas feedback / influencia remuneração / base para PDI]

Entregue:

**1. Formulário de avaliação completo**
Cabeçalho com dados do colaborador. Seção técnica: critérios com descrição do que é esperado e escala. Seção comportamental: idem. Espaço para exemplos concretos por critério.

**2. Tabela de autoavaliação**
Mesmos critérios para o colaborador se avaliar antes da conversa com o gestor.

**3. Consolidação do resultado**
Fórmula de cálculo do resultado geral + tabela de classificação final (ex: abaixo da expectativa / na expectativa / acima da expectativa).

**4. Espaço de devolutiva**
Campo para o gestor registrar os principais pontos da conversa de feedback e os combinados.

**5. Plano de ação pós-avaliação**
Template de 5 linhas para registrar 2 a 3 ações de desenvolvimento baseadas no resultado.

**6. Assinaturas e arquivamento**
Campos de assinatura com orientação sobre onde arquivar (prontuário, PDI, sistema de RH).
```

## Exemplo de uso

### Input
- Cargo: Auxiliar de Armazém
- Frequência: trimestral
- Responsabilidades: recebimento, conferência, separação, lançamento no WMS
- Critérios técnicos: precisão no lançamento de NF, acuracidade no picking, cumprimento dos POPs
- Critérios comportamentais: comunicação de problemas, pontualidade, trabalho em equipe
- Escala: 1 a 5 (1=muito abaixo, 3=na expectativa, 5=referência)
- Autoavaliação: sim
- Resultado: base para PDI e conversas de remuneração

### Output
| Critério | Descrição do que é esperado | Autoavaliação (1-5) | Avaliação Gestor (1-5) | Exemplo concreto |
|----------|---------------------------|--------------------|-----------------------|-----------------|
| Precisão no lançamento de NF | Zero divergências entre quantidade conferida fisicamente e quantidade lançada no WMS. Critério verificável: relatório de divergências do WMS. | | | |
| Cumprimento da IT de conferência | Executa todos os passos da IT-ARM-001a sem pular etapas. Verificável via observação direta e ausência de ocorrências. | | | |

---
**Tags:** Intermediário | Template | Operações, RH & Gestão
