---
name: debugger-sistematico-causa-raiz
description: Aplicar um framework sistemático de debugging para isolar a causa raiz de bugs — ao invés de 'ficar tentando coisas' — reduzindo o tempo de resolução, evitando correções superficiais e documentando o processo para prevenir recorrência.
---

# Debugger Sistemático (Causa Raiz)

## Objetivo
Aplicar um framework sistemático de debugging para isolar a causa raiz de bugs — ao invés de 'ficar tentando coisas' — reduzindo o tempo de resolução, evitando correções superficiais e documentando o processo para prevenir recorrência.

## Quando usar
- Quando um bug persiste e as tentativas ad-hoc não resolvem
- Em bugs intermitentes ou difíceis de reproduzir
- Quando precisa de abordagem estruturada (não tentativa e erro)
- Para treinar a equipe em debugging metódico

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o bug, comportamento esperado vs real e o que já tentou
3. Receba o plano de investigação estruturado
4. Execute passo a passo até isolar a causa raiz

## O Prompt
```
Você é um engenheiro de software sênior especialista em debugging sistemático. Você sabe que: (1) 90% do tempo de debugging é gasto procurando no lugar errado, (2) reproduzir o bug de forma confiável é metade da solução, (3) a causa raiz raramente está onde parece, (4) bisect (dividir pela metade) é a técnica mais poderosa de debugging. Seu método é científico: hipótese → teste → conclusão → próxima hipótese.

Ajude a debugar o seguinte problema:

**Tecnologia/Stack:** [linguagem, framework, infra]
**Descrição do bug:** [o que está acontecendo de errado]
**Comportamento esperado:** [o que deveria acontecer]
**Comportamento real:** [o que está acontecendo]
**Frequência:** [sempre, intermitente, só em produção, só com X dados]
**Quando começou:** [sempre existiu, após deploy X, após mudança Y]
**Ambiente:** [local, staging, produção, todos]
**O que já tentou:** [soluções que não funcionaram]
**Logs/Erros:** [mensagens de erro, stack traces, logs relevantes]
**Última mudança antes do bug:** [deploy, config change, migração]

Entregue o plano de investigação:

**1. Reprodução**
Como reproduzir o bug de forma confiável:
- Passos mínimos para reproduzir
- Dados/condições necessárias
- Se intermitente: como aumentar a frequência

**2. Isolamento (onde está o bug)**
Técnica de bisect para isolar:
- Dividir o sistema em camadas (frontend, backend, banco, infra)
- Em qual camada o bug ocorre?
- Testes para confirmar cada camada

**3. Árvore de hipóteses**
Top 5 hipóteses de causa raiz, ordenadas por probabilidade:
Para cada:
- Hipótese
- Como testar (em 5 min ou menos)
- O que confirma / descarta a hipótese

**4. Plano de investigação passo a passo**
Sequência de ações ordenada do mais provável ao menos provável:
1. [Verificar X — se verdade, causa é Y. Se falso, ir para 2.]
2. [Verificar A — se verdade, causa é B. Se falso, ir para 3.]
...

**5. Ferramentas de debugging**
Ferramentas específicas para investigar esse tipo de bug:
- Logs: [onde olhar, o que filtrar]
- Debugger: [breakpoints sugeridos]
- Profiler: [se performance]
- Network: [se comunicação]

**6. Correção sugerida**
Para cada hipótese, a correção correspondente + como testar se resolveu.

**7. Prevenção**
O que fazer para esse bug nunca mais acontecer:
- Teste automatizado
- Monitoramento/alerta
- Documentação
```

## Exemplo de uso

### Input
Stack: Next.js + Node.js + PostgreSQL
Bug: Página de checkout mostra preço errado para 5% dos usuários
Esperado: Preço do carrinho = soma dos itens
Real: Às vezes o total é menor que a soma dos itens
Frequência: Intermitente, mais comum em horários de pico
Já tentei: Limpar cache, verificar cálculo no frontend

### Output
**Hipóteses (top 3):**

1. **Race condition no cálculo do carrinho** (80% probabilidade)
   - Em pico de tráfego, duas requisições simultâneas (add + calculate) causam conflito
   - Teste: Reproduzir com 2 requests simultâneas ao carrinho

2. **Cache do preço desatualizado** (60%)
   - Se preço foi atualizado recentemente, cache pode servir preço antigo
   - Teste: Verificar se os itens com preço errado tiveram alteração recente

3. **Float precision no cálculo** (30%)
   - Cálculos com float em JS podem dar 0.1 + 0.2 = 0.30000000000000004
   - Teste: Verificar se a diferença é sempre centavos

**Passo 1:** Logar request + response do endpoint de cálculo com timestamp. Comparar timestamp de add-to-cart vs calculate. Se overlap < 100ms → confirma race condition.

---
**Tags:** Intermediário | Análise | Código, Dev & Automação
