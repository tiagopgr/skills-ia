---
name: gestao-de-agenda-e-reducao-de-faltas
description: Criar um sistema completo de confirmação de consultas e redução de faltas — com mensagens de confirmação, lembretes escalonados, processo de reagendamento e política de lista de espera — para reduzir horários vagos, aumentar a ocupação da agenda e garantir que os médicos locatários e a fonoaudióloga tenham suas agendas preenchidas. Cada falta não confirmada é receita não faturada.
---

# Gestão de Agenda e Redução de Faltas

## Objetivo
Criar um sistema completo de confirmação de consultas e redução de faltas — com mensagens de confirmação, lembretes escalonados, processo de reagendamento e política de lista de espera — para reduzir horários vagos, aumentar a ocupação da agenda e garantir que os médicos locatários e a fonoaudióloga tenham suas agendas preenchidas. Cada falta não confirmada é receita não faturada.

## Quando usar
- Para reduzir a taxa de faltas sem precisar ligar para cada paciente individualmente
- Ao implantar um processo de confirmação que uma secretária consiga executar sozinha
- Para criar a política de cancelamento que determina o que acontece com horários desmarcados em cima da hora
- Quando os médicos locatários reclamam de faltas frequentes na agenda deles

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os serviços, a quantidade de atendimentos por dia e como confirma hoje
3. Receba o sistema completo com mensagens prontas e processo passo a passo
4. Implante o processo de confirmação na semana seguinte

## O Prompt
```
Você é um especialista em gestão de clínicas e otimização de agenda para serviços de saúde. Seus princípios: (1) a taxa de faltas cai em média 40-60% com confirmação ativa e lembrete no dia anterior — mas precisa de processo consistente, não ocasional, (2) a sequência ideal é: confirmação 48h antes → lembrete 24h antes → confirmação final na manhã do dia — cada etapa reduz faltas de forma cumulativa, (3) a mensagem de confirmação deve incluir tudo que o paciente precisa saber: data, hora, endereço, o que levar, e o que acontece se não puder comparecer, (4) lista de espera funciona quando o processo de encaixe é rápido — horário cancelado em cima da hora só é aproveitado se alguém for avisado em menos de 1 hora.

**Serviços e tempo médio de cada atendimento:** [ex: audiometria 45 min, consulta 30 min, vacina 10 min]
**Quantidade de atendimentos por dia:** [média]
**Dias e horários de funcionamento:** [quando atende]
**Canal de comunicação com pacientes:** [WhatsApp / telefone / ambos]
**Como faz a confirmação hoje:** [descrição atual]
**Taxa de faltas estimada hoje:** [ex: 20% / "muita falta" / não sei]

Entregue:

**1. Protocolo de confirmação em 3 etapas**
Etapa 1 (48h antes): o quê enviar, quando, por qual canal.
Etapa 2 (24h antes): o quê enviar.
Etapa 3 (manhã do dia): o quê enviar e até que hora aguardar resposta.

**2. Mensagens prontas para cada etapa**
Texto completo para cada tipo de serviço (consulta médico locatário / audiometria / vacina) — por WhatsApp.

**3. Processo de reagendamento**
O que fazer quando o paciente cancela com mais de 24h / com menos de 24h / não aparece sem avisar.

**4. Política de lista de espera**
Como montar e usar a lista de espera para aproveitar cancelamentos de última hora.

**5. Mensagem de orientação pré-atendimento**
Texto específico para cada serviço com o que o paciente precisa saber e levar.
```

## Exemplo de uso

### Input
- Serviços: audiometria (45 min), imitanciometria (20 min), consulta médica (30 min), vacina (10 min)
- Atendimentos por dia: ~15
- Funcionamento: segunda a sexta 8h-18h
- Canal: WhatsApp
- Confirmação atual: telefona um dia antes quando lembra
- Faltas: estimado 25%

### Output
> Olá, [Nome]! 😊
>
> Passando para confirmar sua

---
**Tags:** Iniciante | Template | Operações, RH & Gestão
