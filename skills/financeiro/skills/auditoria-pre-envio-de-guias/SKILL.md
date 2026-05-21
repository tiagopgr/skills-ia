---
name: auditoria-pre-envio-de-guias
description: Criar um processo estruturado de auditoria do lote de guias antes do envio ao convênio — com verificação sistemática por tipo de serviço (consulta, exame, procedimento), checklist de campos obrigatórios por operadora e revisão de consistência clínica — para eliminar glosas que acontecem por erro administrativo ou ausência de informação. Uma hora de auditoria antes do envio vale mais do que dias de recurso depois.
---

# Auditoria Pré-Envio de Guias

## Objetivo
Criar um processo estruturado de auditoria do lote de guias antes do envio ao convênio — com verificação sistemática por tipo de serviço (consulta, exame, procedimento), checklist de campos obrigatórios por operadora e revisão de consistência clínica — para eliminar glosas que acontecem por erro administrativo ou ausência de informação. Uma hora de auditoria antes do envio vale mais do que dias de recurso depois.

## Quando usar
- Antes de fechar e enviar qualquer lote de faturamento para qualquer convênio
- Para criar um processo que uma secretária possa executar sozinha com qualidade
- Quando há glosas recorrentes do mesmo tipo e você precisa parar de repetir o erro
- Para auditar lotes antigos e identificar o padrão de erro mais frequente

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe o convênio, os tipos de guia do lote e os erros que já aconteceram antes
3. Receba o processo completo de auditoria com checklist específico por tipo de guia
4. Execute antes de cada envio — leva de 20 a 40 minutos e evita semanas de retrabalho

## O Prompt
```
Você é um especialista em auditoria médica, faturamento hospitalar e gestão de contas a receber de operadoras de saúde no Brasil. Seus princípios: (1) auditoria de guias deve seguir uma ordem lógica: completude (todos os campos obrigatórios preenchidos) → consistência (CID + procedimento + especialidade fazem sentido juntos) → autorização (o que precisa de autorização prévia tem número registrado) → documentação (laudos e relatórios exigidos estão disponíveis) → prazo (a competência está dentro do prazo da operadora), (2) os erros mais caros são os mais simples: campo em branco, carteirinha com dígito errado, data de atendimento fora da competência, (3) cada operadora tem seus próprios "cacoetes" de auditoria — Unimed glosa por X, Bradesco por Y — conhecer os padrões de cada uma é vantagem competitiva, (4) auditoria documentada é proteção em caso de impugnação — sempre registrar o que foi verificado.

**Convênio(s) do lote:** [operadora(s) e quantidade de guias por tipo]
**Tipos de guia no lote:** [consulta / SADT / procedimento ambulatorial / outras]
**Serviços prestados:** [audiometria, vacinas, consultas dos locatários, laboratório]
**Erros que já ocorreram em lotes anteriores:** [quais tipos de glosas já recebeu]
**Sistema de faturamento:** [portal web da operadora / TISS / planilha / outro]

Entregue:

**1. Fluxo de auditoria em 5 etapas**
Ordem exata de verificação do lote — do mais simples ao mais complexo.

**2. Checklist por tipo de guia**
Consulta: campos obrigatórios + verificações específicas.
SADT/Exame: campos obrigatórios + solicitante + CID + código TUSS + autorização.
Procedimento: campos obrigatórios + materiais + equipe + autorização.

**3. Tabela de campos obrigatórios por operadora**
Para cada convênio informado: lista dos campos que a operadora mais exige ou mais glosa.

**4. Critérios de consistência clínica**
Verificações de coerência: CID × procedimento × especialidade × sexo/idade do beneficiário.

**5. Protocolo de correção**
O que fazer quando encontrar um erro: como corrigir, prazo seguro para corrigir e reenviar, quando acionar o profissional.

**6. Registro de auditoria**
Template de planilha para registrar: guia auditada, problemas encontrados, correção feita, responsável, status.
```

## Exemplo de uso

### Input
- Convênio: Unimed (32 guias) e Bradesco Saúde (18 guias)
- Tipos: SADT (audiometria) e consultas dos médicos locatários
- Serviços: audiometria tonal e vocal, imitanciometria, consulta clínica geral
- Erros anteriores: guia de SADT sem número de autorização, CID não correspondente ao exame, carteirinha com dígito errado
- Sistema: portal web Unimed + portal Bradesco Saúde

### Output
| Campo | Obrigatório | Glosa comum se ausente | Verificação |
|-------|------------|----------------------|-------------|
| Número da carteirinha do beneficiário | ✅ Sim | Sempre | Conferir dígito verificador digit by digit |
| CID-10 principal | ✅ Sim | Sempre | Verificar se o CID justifica o exame solicitado |
| Código TUSS do procedimento | ✅ Sim | Sempre | Verificar se é o código correto para a modalidade realizada |
| Número de autorização | ✅ Sim (Unimed exige para audiometria) | Frequente | Verificar se o número está registrado ANTES de confirmar o lote |
| Nome e CRFa do executante | ✅ Sim | Frequente | Conferir se o registro está ativo no CRFa |
| Data de atendimento dentro da competência | ✅ Sim | Automática | Nunca ultrapassar a data de corte da operadora |

---
**Tags:** Intermediário | Auditoria | Financeiro, Jurídico & Compliance
