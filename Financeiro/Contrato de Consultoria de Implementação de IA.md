---
name: contrato-de-consultoria-de-implementacao-de-ia
description: Gerar um contrato de consultoria de implementação de IA completo — com escopo técnico detalhado, entregáveis, SLA de suporte, limitações de responsabilidade, propriedade intelectual e condições de rescisão — que protege o consultor dos problemas clássicos do setor: cliente que pede mais do que foi combinado, cobranças por falhas de terceiros (APIs, ferramentas externas) e expectativas irreais de resultado. Um contrato bem feito é a diferença entre uma consultoria sustentável e uma armadilha.
---

# Contrato de Consultoria de Implementação de IA

## Objetivo
Gerar um contrato de consultoria de implementação de IA completo — com escopo técnico detalhado, entregáveis, SLA de suporte, limitações de responsabilidade, propriedade intelectual e condições de rescisão — que protege o consultor dos problemas clássicos do setor: cliente que pede mais do que foi combinado, cobranças por falhas de terceiros (APIs, ferramentas externas) e expectativas irreais de resultado. Um contrato bem feito é a diferença entre uma consultoria sustentável e uma armadilha.

## Quando usar
- Antes de iniciar qualquer projeto de implementação de IA
- Para formalizar o escopo e evitar o "scope creep" (cliente pedindo cada vez mais)
- Quando o cliente é empresa e exige contrato antes de pagar
- Para projetos com manutenção mensal — o contrato recorrente é diferente do contrato de projeto

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva o projeto e as condições acordadas
3. Informe as limitações importantes e o que não está incluído
4. Receba o contrato completo para revisar e usar

## O Prompt
```
Você é um advogado especializado em contratos de tecnologia e consultoria digital. Seus princípios: (1) escopo técnico como objeto contratual — "implementar automação de atendimento via WhatsApp com n8n e Z-API" é melhor que "implementar IA"; (2) dependência de terceiros declarada — APIs da OpenAI, WhatsApp e outras podem cair ou mudar — isso não é sua responsabilidade; (3) expectativa de resultado vs. garantia — consultor entrega o sistema, não o resultado de negócio; (4) suporte com limite — defina o que é manutenção e o que é novo desenvolvimento.

**CONTRATANTE:**
Nome/Razão Social: [nome]
CNPJ/CPF: [número]
Endereço: [endereço]

**CONTRATADO (consultor):**
Nome: [seu nome]
CPF/CNPJ: [número]

**Objeto do contrato:**
[descreva o projeto com precisão técnica — ex: "implementação de fluxo de automação de confirmação de consultas via WhatsApp Business API, utilizando as ferramentas n8n, Z-API e Google Sheets, conforme especificação técnica em Anexo I"]

**Entregáveis:**
[liste o que vai ser entregue — ex: fluxo funcional no n8n / documentação de uso / treinamento de 1h / 30 dias de suporte]

**Prazo de implementação:** [ex: 15 dias corridos após recebimento das credenciais]

**Valor:** [R$ valor]
**Pagamento:** [ex: 50% início + 50% entrega]

**Modelo:** [projeto único / projeto + manutenção mensal de R$X]

**O que NÃO está incluído:**
[ex: licença das ferramentas / custo de APIs (OpenAI, Z-API) / alterações no escopo após aprovação / bugs causados por mudanças nas APIs de terceiros]

**SLA de suporte (se houver manutenção):**
[ex: resposta em até 24h úteis / correção de bugs em até 5 dias úteis]

Entregue:

**1. Contrato completo**
Documento com cláusulas cobrindo: objeto, entregáveis, prazo, valor e pagamento, obrigações das partes, dependências de terceiros, limitação de responsabilidade, propriedade intelectual, suporte e manutenção, rescisão, foro.

**2. Cláusulas de proteção críticas para consultor de IA**
As 3-4 cláusulas mais importantes para proteger o consultor — e por que cada uma é especialmente relevante em projetos de IA.

**3. Anexo I — Especificação Técnica**
Template de especificação técnica para detalhar as ferramentas, integrações e configurações do projeto.
```

## Exemplo de uso

### Input
- Projeto: bot de confirmação de consultas com n8n + Z-API
- Valor: R$2.800 | 50%+50% + manutenção R$350/mês
- Não inclui: custo da Z-API (R$97/mês pago pelo cliente), alterações de escopo

### Output
*Cláusula 8ª — Dependências de Terceiros e Limitação de Responsabilidade*
*O sistema objeto deste contrato utiliza serviços de terceiros, incluindo mas não se limitando a: Z-API (integração WhatsApp), n8n (automação), Google Sheets (armazenamento de dados) e APIs da OpenAI (quando aplicável). O CONTRATADO não se responsabiliza por: (i) interrupções nos serviços de terceiros; (ii) mudanças de API que tornem necessária readaptação do sistema; (iii) bloqueios de conta no WhatsApp Business por uso em desacordo com os termos da Meta. Adaptações necessárias por mudanças de terceiros serão cotadas separadamente como novo desenvolvimento.*

---
**Tags:** Intermediário | Template | Financeiro, Jurídico & Compliance
