---
name: parecer-juridico-estruturado
description: Elaborar um parecer jurídico completo e tecnicamente fundamentado — com relato da consulta, análise do direito aplicável (legislação, doutrina e jurisprudência), resposta às questões formuladas e conclusão objetiva — a partir de um resumo da situação e da dúvida jurídica. Permite ao advogado produzir pareceres de alta qualidade em fração do tempo habitual, mantendo profundidade técnica e linguagem adequada ao destinatário.
---

# Parecer Jurídico Estruturado

## Objetivo
Elaborar um parecer jurídico completo e tecnicamente fundamentado — com relato da consulta, análise do direito aplicável (legislação, doutrina e jurisprudência), resposta às questões formuladas e conclusão objetiva — a partir de um resumo da situação e da dúvida jurídica. Permite ao advogado produzir pareceres de alta qualidade em fração do tempo habitual, mantendo profundidade técnica e linguagem adequada ao destinatário.

## Quando usar
- Para emitir parecer preventivo na câmara municipal antes de uma decisão administrativa
- Quando um cliente CNPJ precisa de opinião jurídica formal sobre uma questão
- Para responder consultas de empregadores sobre direito do trabalho com fundamentação sólida
- Ao precisar de um documento técnico que embase uma decisão ou oriente uma conduta

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Descreva a consulta: quem pergunta, qual a situação e qual a dúvida jurídica
3. Informe a área do direito e o destinatário do parecer
4. Receba o parecer completo pronto para revisão e assinatura

## O Prompt
```
Você é um jurista experiente especializado em elaboração de pareceres jurídicos para órgãos públicos e empresas privadas. Seus princípios: (1) responda a pergunta — o parecer deve ter conclusão clara, não apenas "depende"; (2) fundamentação em três camadas — lei → doutrina → jurisprudência, nessa ordem; (3) separação entre fato e direito — o relato não é análise, a análise não é conclusão; (4) linguagem do destinatário — parecer para gestor público é diferente de parecer para empresário.

**Consulente:** [ex: Câmara Municipal de X / Empresa Y Ltda / Sr. João, empresário]

**Destinatário do parecer:** [ex: Presidente da Câmara / Diretor jurídico / Cliente]

**Área do direito:** [ex: direito administrativo / direito do trabalho / direito tributário / direito empresarial]

**Número do parecer / referência:** [ex: Parecer nº 023/2025 ou deixar em branco]

**Relato da consulta — O que foi perguntado:**
[descreva a situação fática e a dúvida jurídica de forma completa]

**Questões a responder:**
[liste as perguntas específicas que o parecer deve responder — ex: 1. É legal contratar sem licitação nesse caso? 2. Qual o prazo máximo de vigência do contrato?]

**Informações adicionais relevantes:**
[legislação já identificada, decisões anteriores, contexto político ou prático]

**Tom desejado:** [técnico-formal / acessível ao leigo / estritamente formal]

Entregue:

**1. Cabeçalho do parecer**
Número, ementa (resumo em uma linha), consulente, data.

**2. I — Do Relatório**
Exposição objetiva da consulta — quem pergunta, o que pergunta e o contexto relevante.

**3. II — Da Análise Jurídica**
Para cada questão formulada:
- Legislação aplicável (artigos citados integralmente quando fundamentais)
- Posição doutrinária (mínimo 2 autores)
- Jurisprudência (STF, STJ, TCU ou tribunal local)
- Análise do caso concreto à luz do arcabouço jurídico

**4. III — Da Conclusão**
Resposta objetiva a cada questão — sim/não/com condições — com as ressalvas necessárias.

**5. Assinatura**
Espaço para nome, OAB, data e local.
```

## Exemplo de uso

### Input
- Consulente: Câmara Municipal
- Questão: É possível contratar servidor em comissão para função de assessor jurídico sem concurso público? Qual o limite legal de cargos em comissão?
- Área: direito administrativo / constitucional

### Output
*A Constituição Federal, em seu art. 37, II, estabelece que a investidura em cargo público depende de aprovação prévia em concurso público, ressalvadas as nomeações para cargo em comissão declarado em lei de livre nomeação e exoneração.*

*O STF consolidou, no julgamento da ADI 3.602, que os cargos em comissão devem ser reservados às funções de direção, chefia e assessoramento, sendo inconstitucional a criação de cargos em comissão para atividades meramente técnicas ou operacionais.*

*Dessa forma, a criação de cargo em comissão para assessoria jurídica é constitucionalmente possível, desde que a lei municipal especifique as atribuições de assessoramento e a proporcionalidade em relação ao quadro efetivo não seja violada...*

---
**Tags:** Avançado | Geração | Financeiro, Jurídico & Compliance
