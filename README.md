<div align="center">

# Skills de IA — Biblioteca Profissional de Skills

**+1.100 skills estruturados, organizados por área, prontos para usar com qualquer modelo de linguagem.**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tiagopgr/)
![Skills](https://img.shields.io/badge/skills-1.161-blueviolet?style=flat-square)
![Categorias](https://img.shields.io/badge/categorias-14-blue?style=flat-square)
![Licença](https://img.shields.io/badge/licença-MIT-green?style=flat-square)

</div>

---

## Sobre

Esta biblioteca reúne skills prontos para uso com **Claude**, **ChatGPT**, **Gemini**, **Codex** e outros modelos — organizados por área de atuação profissional.

Cada skill segue uma estrutura consistente:

```
Objetivo     → para que serve e quando usar
Quando usar  → situações práticas de aplicação  
Como usar    → passo a passo
O Prompt     → pronto para copiar e colar
```

O objetivo é eliminar a curva de aprendizado e entregar resultado desde o primeiro uso — sem precisar saber "como prompar bem".

Os skills não são genéricos. Cada um foi construído para uma situação real e específica — com o contexto, a linguagem e o resultado que aquele profissional precisa. Você vai encontrar skills para Procurador da Fazenda triando planilha de processos com SAJ, para freelancer de branding que precisa precificar um projeto sem cobrar por hora, para e-commerce Shopify rodando no mercado europeu, para fonoaudióloga que faz avaliação audiológica e vendas no mesmo atendimento.

---

## Categorias

| | Categoria | Skills | O que você encontra |
|---|---|:---:|---|
| 📦 | [Operações](./Operações/) | 245 | SOPs, POPs, delegação, onboarding, planejamento trimestral, gestão de projetos, diagnóstico de gargalos, automação com IA |
| 📣 | [Marketing](./Marketing/) | 221 | Funis de venda, campanhas Meta/TikTok Ads, propostas comerciais, scripts de reunião, sequências de e-mail, lançamentos digitais |
| ✍️ | [Conteúdo & Copy](./Conteúdo%20%26%20Copy/) | 210 | Headlines, hooks, carrosséis, roteiros de Reels, VSLs, páginas de venda, e-mails, newsletters, UX writing |
| 💰 | [Financeiro](./Financeiro/) | 133 | Fluxo de caixa, DRE gerencial, precificação, contratos, conciliação bancária, planejamento tributário, unit economics |
| 🗓️ | [Rotina](./Rotina/) | 90 | Planejamento semanal, batching de conteúdo, GTD, blocos de foco, revisão semanal, gestão de múltiplos projetos |
| ⚖️ | [Jurídico & Advocacia](./Jurídico%20%26%20Advocacia/) | 55 | Petições, contestações, pareceres, contratos, gestão de escritório, captação de clientes, honorários, conteúdo jurídico |
| 🧩 | [Produto](./Produto/) | 44 | KPIs, lançamento de produto digital, otimização de conversão, análise de churn, SEO, relatórios executivos |
| 🚀 | [Carreira](./Carreira/) | 38 | Posicionamento, bio, LinkedIn, currículo, mentoria, thought leadership, portfólio, precificação freelancer |
| 📊 | [SEO & Dados](./SEO/) | 33 | Análise de métricas, pesquisa de mercado, análise de concorrência, funil de conversão, interpretação de KPIs |
| 👥 | [Liderança & Equipes](./Liderança%20%26%20Equipes/) | 26 | OKRs, feedback estruturado, delegação, onboarding de time, reuniões produtivas, avaliação de desempenho |
| 🎨 | [Design & Branding](./Design%20%26%20Branding/) | 24 | Briefing estratégico, proposta comercial, apresentação de identidade visual, naming, moodboard, precificação de projetos |
| 💻 | [Código](./Código/) | 22 | Debugging sistemático, design de API RESTful, CI/CD, Dockerfile, code review, testes unitários, autenticação |
| 🎬 | [Direção Criativa](./Direção%20Criativa/) | 20 | Conceito de campanha, direção de arte, narrativa visual, branding estratégico, portfólio criativo |

---

## Como usar no Claude Code (plugin)

Para usar os skills como slash commands diretamente no **Claude Code**, consulte o guia completo:

**[INSTALL.md](./INSTALL.md)** — instalação passo a passo, comandos disponíveis e solução de problemas.

Resumo rápido:
1. Abra **Settings → Plugins** no Claude Code
2. Adicione `https://github.com/tiagopgr/skills-ia`
3. Instale a categoria: `/plugin install marketing@skills-ia`
4. Use: `/marketing:proposta-comercial-para-freelancer-criativo`

---

## Como usar no navegador

Não precisa instalar nada. Tudo funciona direto aqui no navegador.

**1. Escolha uma categoria** na tabela acima e clique nela — por exemplo, _Marketing_ ou _Jurídico & Advocacia_.

**2. Escolha um skill** da lista que aparecer. Os nomes são descritivos, então leia até encontrar o que resolve o seu problema.

**3. Abra o arquivo** clicando no nome dele. O conteúdo vai aparecer na tela.

**4. Copie o skill** — é o texto que começa com _"Você é um..."_. Selecione, copie e cole direto no Claude, ChatGPT, Gemini ou qualquer IA que você usar.

**5. Preencha os campos entre `[ ]`** com as informações do seu caso. Quanto mais detalhe você der, melhor será a resposta.

> Quer ver exemplos práticos em cada ferramenta? Veja o guia [USAGE.md](./USAGE.md).

---

## Exemplo de Skill

<details>
<summary><strong>Debugger Sistemático (Causa Raiz)</strong> — <code>Código/121</code></summary>

```markdown
## Objetivo
Aplicar um framework sistemático de debugging para isolar a causa raiz
de bugs — reduzindo o tempo de resolução e evitando correções superficiais.

## Quando usar
- Quando um bug persiste e as tentativas ad-hoc não resolvem
- Em bugs intermitentes ou difíceis de reproduzir
- Para treinar a equipe em debugging metódico

## O Prompt
Você é um engenheiro de software sênior especialista em debugging sistemático.
Você sabe que: (1) 90% do tempo de debugging é gasto procurando no lugar errado,
(2) reproduzir o bug de forma confiável é metade da solução...

Tecnologia/Stack: [linguagem, framework, infra]
Descrição do bug: [o que está acontecendo de errado]
```

</details>

---

## Para quem é?

<details>
<summary><strong>⚖️ Advogados e consultores</strong></summary>

**Situação:** Você tem uma consulta marcada para amanhã com um potencial cliente, mas não sabe exatamente como conduzir a conversa para fechar o caso.

**Skill:** [`Jurídico & Advocacia / Script de Consulta Inicial e Captação de Cliente`](./Jurídico%20%26%20Advocacia/173-Script%20de%20Consulta%20Inicial%20e%20Captação%20de%20Cliente.md)

**O que você faz:** Abre o arquivo, copia o skill, cola no ChatGPT ou Claude e informa a área do caso (ex: direito trabalhista, inventário, execução fiscal). A IA gera um roteiro completo com perguntas estratégicas de diagnóstico, momentos para demonstrar autoridade e a transição natural para apresentar a proposta de honorários.

**Resultado:** Você entra na reunião com um script na mão, conduz com segurança e aumenta a chance de fechar o cliente.

</details>

<details>
<summary><strong>📣 Freelancers e agências</strong></summary>

**Situação:** Um cliente pediu uma proposta comercial para um projeto de identidade visual. Você sabe fazer o trabalho, mas travar na hora de escrever a proposta é rotina.

**Skill:** [`Marketing / Proposta Comercial para Freelancer Criativo`](./Marketing/1044-Proposta%20Comercial%20para%20Freelancer%20Criativo.md)

**O que você faz:** Copia o skill, informa o nome do cliente, o tipo de projeto, o valor e o prazo. A IA escreve uma proposta profissional com apresentação, escopo, entregáveis, cronograma e condições de pagamento.

**Resultado:** Uma proposta que você mandaria com vergonha vira um documento que transmite profissionalismo — em menos de 10 minutos.

</details>

<details>
<summary><strong>🚀 Empreendedores</strong></summary>

**Situação:** Seu negócio cresceu, mas os processos continuam na sua cabeça. Toda vez que você está ausente, a equipe trava.

**Skill:** [`Operações / SOP de Processos Internos`](./Operações/)

**O que você faz:** Escolhe um processo crítico (ex: onboarding de cliente, emissão de nota fiscal, resposta a reclamações). Cola o skill no Claude, descreve como o processo funciona hoje e a IA transforma em um SOP documentado — com passo a passo, responsáveis e critérios de qualidade.

**Resultado:** O processo sai da sua cabeça e vira um documento que qualquer pessoa da equipe consegue seguir sozinha.

</details>

<details>
<summary><strong>✍️ Times de conteúdo e criadores</strong></summary>

**Situação:** Segunda-feira, calendário editorial vazio, prazo de entrega na sexta. Você precisa de 20 ideias de posts para o mês.

**Skill:** [`Marketing / Planejamento de Conteúdo Mensal`](./Marketing/853-Planejamento%20de%20Conteúdo%20Mensal.md)

**O que você faz:** Copia o skill, informa o nicho (ex: nutrição esportiva), o perfil do público, os objetivos do mês (ex: lançar um produto na última semana) e as plataformas. A IA entrega um plano semana a semana com temas, formatos, intenção estratégica de cada post e sugestões de legenda.

**Resultado:** O mês inteiro planejado em uma tarde, com conteúdos que servem ao objetivo de negócio — não publicados aleatoriamente.

</details>

<details>
<summary><strong>💻 Desenvolvedores</strong></summary>

**Situação:** Você está prestes a iniciar um novo projeto e quer garantir que a API seja bem desenhada antes de escrever qualquer linha de código.

**Skill:** [`Código / Design de API RESTful (Boas Práticas)`](./Código/122-Design%20de%20API%20RESTful%20(Boas%20Práticas).md)

**O que você faz:** Copia o skill, descreve os recursos do sistema (ex: agendamentos, usuários, notificações) e as principais operações necessárias. A IA projeta os endpoints com nomenclatura consistente, versionamento, tratamento de erros padronizado e exemplos de request/response.

**Resultado:** Você começa o desenvolvimento com uma arquitetura sólida, evita retrabalho e entrega uma API que a equipe (e os clientes) conseguem usar sem dor de cabeça.

</details>

<details>
<summary><strong>🏢 Gestores de equipes pequenas</strong></summary>

**Situação:** Você passa a semana toda apagando incêndio. Toda decisão passa por você, todo processo depende de você lembrar — e quando alguém novo entra na equipe, você precisa ensinar tudo do zero de novo.

**Skill:** [`Liderança & Equipes / Documentar processos em SOPs`](./Liderança%20%26%20Equipes/)

**O que você faz:** Descreve um processo que hoje vive só na sua cabeça (ex: como onboarda um novo cliente, como a equipe faz o fechamento semanal). A IA transforma em um SOP com passo a passo, responsáveis, ferramentas usadas e critérios de qualidade.

**Resultado:** O processo sai da sua memória e vira um documento que qualquer pessoa da equipe consegue seguir — você para de ser o gargalo de tudo.

</details>

<details>
<summary><strong>🏦 Consultores financeiros</strong></summary>

**Situação:** Você terminou a reunião com o cliente, tem as anotações na cabeça, mas transformar isso em um relatório executivo profissional vai consumir horas que você não tem.

**Skill:** [`Financeiro / Relatório Executivo de Reunião Financeira`](./Financeiro/)

**O que você faz:** Cola as notas da reunião no skill — valores discutidos, problemas identificados, decisões tomadas. A IA gera um relatório completo com análise da situação, decisões formalizadas, próximos passos com responsáveis e prazos, e pontos de atenção para o próximo encontro.

**Resultado:** O que levaria 2 horas para escrever fica pronto em minutos — e o cliente recebe um documento que reforça o valor da sua consultoria desde o primeiro dia.

</details>

<details>
<summary><strong>🏠 Corretores e gestores de imobiliária</strong></summary>

**Situação:** Você tem um imóvel excelente, mas a descrição que você publica nos portais é genérica demais para se destacar entre dezenas de outros anúncios.

**Skill:** [`Marketing / Descrições Persuasivas de Imóveis`](./Marketing/)

**O que você faz:** Informa as características do imóvel (localização, metragem, diferenciais, público-alvo, faixa de preço). A IA escreve uma descrição com técnicas de copywriting adaptadas ao mercado imobiliário — que cria desejo, gera identificação e leva o interessado a entrar em contato.

**Resultado:** A mesma propriedade gera mais contatos, mais visitas e converte mais — sem aumentar o investimento em anúncios.

</details>

<details>
<summary><strong>🛒 Empreendedores de e-commerce</strong></summary>

**Situação:** Você tem os dados do mês na tela — faturamento, ROAS, taxa de conversão — mas não sabe o que fazer com eles. Parece que está sempre trabalhando muito sem saber se está indo na direção certa.

**Skill:** [`SEO / Análise de Métricas de E-commerce`](./SEO/)

**O que você faz:** Cola os números do mês (ou semana) no skill. A IA interpreta os dados, identifica qual etapa do funil está travando, aponta as hipóteses de causa e sugere as 3 ações prioritárias para melhorar o resultado — sem precisar de analista de dados.

**Resultado:** Você sai da paralisia de "tenho os dados mas não sei o que fazer com eles" e entra em execução com um plano baseado em números reais.

</details>

---

## Destaques da Coleção

Alguns skills que mostram a profundidade e especificidade desta biblioteca:

| Skill | Categoria | Por que é único |
|---|---|---|
| Triagem de Planilha de Processos (SAJ) | Jurídico | Para Procuradores da Fazenda — analisa o lote diário e prioriza por matéria e urgência |
| E-commerce Shopify para Mercado Europeu | Marketing | Copy de produto e ads específicos para TikTok Ads no mercado francês/inglês |
| Laudos Audiológicos Padronizados | Operações | Gera laudo clínico completo a partir dos dados brutos de audiograma em 5 minutos |
| Contratos de Locação de Sala para Clínica | Financeiro | Cláusulas específicas de responsabilidade sanitária e registro em conselho profissional |
| Script de Venda de Aparelho Auditivo | Marketing | Adaptado para pacientes idosos, familiares e adultos — com objeções reais do setor |
| Operações de Mini Índice B3 | Financeiro | Plano operacional, diário de trades e análise de desempenho semanal para Day Trader |
| Recurso de Glosa de Convênio Médico | Financeiro | Carta de recurso com argumentação técnica nas normas da ANS para clínicas |
| Rotina para Procurador + Day Trader | Rotina | Estrutura a semana de quem acumula as duas atividades sem comprometer nenhuma |

---

## Contribuindo

Contribuições são bem-vindas.

1. Faça um **fork** do repositório
2. Crie uma branch: `git checkout -b meu-skill`
3. Adicione o skill seguindo a estrutura dos arquivos existentes
4. Abra um **Pull Request** com uma breve descrição

Encontrou algo para melhorar? Abra uma [Issue](../../issues).

---

## Licença

Distribuído sob licença MIT. Veja [`LICENSE`](./LICENSE) para mais detalhes.

---

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tiagopgr/)

**Se esta biblioteca foi útil, considere um café ☕**

<img src="qrcode.png" alt="Buy Me a Coffee" width="140"/>

*"A IA não vai substituir profissionais. Vai substituir profissionais que não sabem usar IA."*

</div>
