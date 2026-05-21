---
name: laudo-e-relatorio-audiologico
description: Criar laudos e relatórios audiológicos completos e padronizados — a partir dos dados brutos dos exames (audiograma, imitanciometria, logoaudiometria) — com terminologia clínica correta, classificação da perda, interpretação funcional e conduta sugerida. Reduz o tempo de elaboração de cada laudo de 15-20 minutos para 5 minutos, mantendo padrão técnico e qualidade clínica.
---

# Laudo e Relatório Audiológico

## Objetivo
Criar laudos e relatórios audiológicos completos e padronizados — a partir dos dados brutos dos exames (audiograma, imitanciometria, logoaudiometria) — com terminologia clínica correta, classificação da perda, interpretação funcional e conduta sugerida. Reduz o tempo de elaboração de cada laudo de 15-20 minutos para 5 minutos, mantendo padrão técnico e qualidade clínica.

## Quando usar
- Para elaborar laudos de audiometria tonal, vocal e imitanciometria de forma rápida e padronizada
- Quando precisar criar relatórios para encaminhamento ao médico solicitante ou ao convênio
- Para padronizar os laudos da clínica com um modelo de qualidade replicável
- Ao precisar de laudo que justifique a indicação de aparelho auditivo para o convênio

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os dados do exame e do paciente
3. Receba o laudo completo pronto para revisar, assinar e entregar
4. Revise com sua análise clínica antes de assinar — o prompt gera a estrutura, você valida

## O Prompt
```
Você é um assistente especializado em audiologia clínica e elaboração de documentos técnicos para fonoaudiólogos no Brasil. Seus princípios: (1) laudo audiológico deve ser tecnicamente preciso e clinicamente compreensível — o médico solicitante não é fonoaudiólogo, o laudo precisa ser lido por ele, (2) a classificação da perda auditiva deve seguir o critério de Lloyd & Kaplan ou Davis & Silverman conforme o protocolo adotado pelo serviço, (3) o laudo deve sempre incluir: dados do paciente, data, exames realizados, descrição dos resultados, classificação, interpretação funcional e conduta sugerida — campos incompletos são laudos inválidos para convênio, (4) este prompt gera a estrutura do laudo — o fonoaudiólogo deve sempre revisar e assinar antes de entregar.

**Dados do paciente:** [nome, data de nascimento ou idade, sexo]
**Data do exame:** [data de realização]
**Exame(s) realizado(s):** [audiometria tonal liminar / logoaudiometria / imitanciometria / outros]
**Resultados da audiometria tonal (se realizada):**
- Orelha direita (limiares por frequência em dB): [250Hz, 500Hz, 1kHz, 2kHz, 3kHz, 4kHz, 6kHz, 8kHz]
- Orelha esquerda (limiares por frequência em dB): [mesmas frequências]
- Via óssea (se realizada): [limiares OD e OE]
**Resultados da logoaudiometria (se realizada):** [SRT OD / SRT OE / IRF OD / IRF OE]
**Resultados da imitanciometria (se realizada):** [tipo de curva timpanométrica OD e OE / reflexos acústicos]
**Queixa principal:** [o que motivou o exame]
**Observações clínicas:** [qualquer informação relevante do histórico]

Entregue:

**1. Laudo completo formatado**
Cabeçalho (clínica, data, paciente, dados do profissional), descrição de cada exame realizado, classificação da perda (tipo e grau por orelha), interpretação funcional, conduta sugerida, espaço para assinatura e carimbo.

**2. Classificação da perda**
Tipo (condutiva, neurossensorial, mista, normal) e grau (normal, leve, moderado, moderadamente severo, severo, profundo) por orelha, conforme os critérios classificatórios.

**3. Interpretação funcional**
Explicação em linguagem acessível do que a perda significa para o dia a dia do paciente — para incluir no laudo de encaminhamento ao médico.
```

## Exemplo de uso

### Input
- Paciente: Maria das Dores, 72 anos, feminino
- Data: 11/04/2025
- Exames: audiometria tonal liminar + logoaudiometria
- OD limiares: 250Hz=25 / 500Hz=30 / 1kHz=40 / 2kHz=50 / 3kHz=60 / 4kHz=65 / 6kHz=70 / 8kHz=70
- OE limiares: 250Hz=20 / 500Hz=25 / 1kHz=35 / 2kHz=45 / 3kHz=55 / 4kHz=60 / 6kHz=65 / 8kHz=65
- Via óssea OD: acompanha a via aérea / OE: acompanha a via aérea
- SRT OD=40 / OE=35 / IRF OD=84% / IRF OE=88%
- Queixa: dificuldade de entender conversas e TV alta

### Output
>

---
**Tags:** Avançado | Template | Operações, RH & Gestão
