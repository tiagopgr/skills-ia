---
name: mapa-de-riscos-operacionais
description: Identificar e mapear os riscos de qualquer processo logístico ou operacional — classificando cada risco por probabilidade e impacto, definindo controles existentes e necessários, e gerando um plano de mitigação priorizado. Para o gestor de operações, o mapa de riscos é o documento que transforma a gestão reativa ("apagar incêndio") em gestão preventiva ("evitar o incêndio").
---

# Mapa de Riscos Operacionais

## Objetivo
Identificar e mapear os riscos de qualquer processo logístico ou operacional — classificando cada risco por probabilidade e impacto, definindo controles existentes e necessários, e gerando um plano de mitigação priorizado. Para o gestor de operações, o mapa de riscos é o documento que transforma a gestão reativa ("apagar incêndio") em gestão preventiva ("evitar o incêndio").

## Quando usar
- Antes de implantar um processo novo para antecipar o que pode dar errado
- Após uma falha recorrente para mapear todos os riscos do processo de uma vez
- Para complementar um POP com a seção de riscos e controles
- Para apresentar à liderança o panorama de vulnerabilidades da operação

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o processo e os problemas que já aconteceram ou que você teme
3. Receba o mapa de riscos completo com matriz de priorização e plano de controle
4. Use os controles como insumo para criar ou atualizar os POPs e ITs correspondentes

## O Prompt
```
Você é um especialista em gestão de riscos operacionais e qualidade para operações logísticas. Seus princípios: (1) risco é probabilidade × impacto — um risco improvável de alto impacto (acidente grave) e um risco provável de baixo impacto (esquecimento de carimbo) precisam de estratégias completamente diferentes, (2) controles são de dois tipos: preventivos (evitam o risco) e detectivos (identificam o risco quando ocorre) — um bom sistema tem ambos, (3) todo risco sem controle ou com controle insuficiente é uma falha aguardando acontecer, (4) o mapa de riscos deve ser revisado sempre que um processo for atualizado ou quando um risco se materializar.

**Processo a analisar:** [nome do processo]
**Etapas do processo:** [liste as principais etapas ou cole o POP correspondente]
**Problemas que já ocorreram:** [histórico de falhas, erros ou acidentes]
**Principais medos ou preocupações:** [o que você teme que aconteça]
**Controles já existentes:** [o que já é feito para prevenir ou detectar erros]
**Contexto de risco:** [ex: equipe nova, processo manual, alta rotatividade, pressão de prazo]

Entregue:

**1. Inventário de riscos**
Lista completa de riscos identificados com: código, descrição do risco, etapa do processo onde ocorre, causa provável, consequência.

**2. Matriz de priorização (Probabilidade × Impacto)**
Tabela com: risco, probabilidade (1-5), impacto (1-5), grau de risco (P×I), classificação (baixo/médio/alto/crítico).

**3. Mapa visual de calor**
Grid 5×5 com os riscos posicionados por probabilidade e impacto.

**4. Plano de controle por risco**
Para cada risco alto ou crítico: controle preventivo sugerido, controle detectivo sugerido, responsável, prazo de implantação.

**5. Riscos residuais**
Riscos que permanecerão mesmo após os controles — e o que fazer se se materializarem (plano de contingência).
```

## Exemplo de uso

### Input
- Processo: Separação de Pedidos
- Etapas: geração do romaneio, picking por coletora, conferência, embalagem, expedição
- Problemas já ocorridos: itens errados enviados (3x), quantidade divergente, pedido extraviado internamente
- Medos: enviar pedido de cliente estratégico incompleto
- Controles existentes: conferência visual antes de embalar
- Contexto: 2 auxiliares novos, pico de volume sexta-feira

### Output
| Risco | Probabilidade | Impacto | Grau | Classificação |
|-------|--------------|---------|------|---------------|
| Item errado enviado por erro de picking | 4 | 5 | 20 | Crítico |
| Quantidade divergente por leitura incorreta | 3 | 4 | 12 | Alto |
| Pedido extraviado na área antes da expedição | 2 | 5 | 10 | Alto |
| Romaneio gerado com endereço errado | 2 | 3 | 6 | Médio |

---
**Tags:** Intermediário | Análise | Operações, RH & Gestão
