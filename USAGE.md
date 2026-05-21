# Como Usar Esta Biblioteca de Skills

Um guia prático com exemplos reais para as principais ferramentas de IA.

---

## Índice

- [Claude Code](#claude-code)
- [Gemini](#gemini)
- [Google Antigravity](#google-antigravity)
- [OpenAI Codex](#openai-codex)
- [Dicas Universais](#dicas-universais)

---

## Claude Code

> Terminal com IA da Anthropic. Ideal para skills de **Código**, **Operações** e qualquer skill que envolva arquivos, projetos ou automações.

### Instalação

```bash
npm install -g @anthropic-ai/claude-code
claude
```

### Uso básico com um skill

1. Abra um skill — ex: [`Código/121-Debugger Sistemático (Causa Raiz).md`](Código/121-Debugger%20Sistemático%20(Causa%20Raiz).md)
2. Copie o conteúdo do bloco `## O Prompt`
3. No terminal, cole diretamente e pressione Enter

```bash
# Exemplo real: debugar um erro em Python
$ claude

> Você é um engenheiro de software sênior especialista em debugging sistemático...
> Tecnologia/Stack: Python 3.11, FastAPI
> Descrição do bug: endpoint /users retorna 500 intermitentemente sob carga
> Comportamento esperado: retornar lista paginada com status 200
> O que já tentei: adicionar logs, o erro some com restart
```

### Uso com arquivo de contexto

Passe o skill diretamente como arquivo de contexto para o Claude Code processar junto com seu projeto:

```bash
# Envia o skill + seu código atual para análise
$ claude --file "Código/123-Code Review Estruturado (Checklist).md"

> Revise o arquivo src/api/routes.py usando o framework acima
```

### Fluxo recomendado para skills de Código

```bash
# 1. Abra o Claude Code na raiz do projeto
$ claude

# 2. Cole o prompt do skill e preencha o contexto
> [prompt do skill]
> Meu projeto: [descrição breve]
> Arquivo relevante: [caminho/arquivo.py]

# 3. Peça ao Claude para aplicar diretamente no código
> Agora aplique as correções no arquivo
```

---

## Gemini

> Assistente do Google disponível em [gemini.google.com](https://gemini.google.com). Excelente para skills de **Marketing**, **Conteúdo & Copy**, **SEO** e **Carreira** — especialmente quando integrado ao Google Workspace.

### Uso básico com um skill

1. Abra o Gemini no navegador ou app
2. Copie o prompt do skill escolhido
3. Cole e preencha as variáveis entre `[ ]`

**Exemplo real — skill [`Marketing/848-Página de Venda Express.md`](Marketing/848-Página%20de%20Venda%20Express.md):**

```
[cole o prompt do skill aqui]

Produto: Mentoria em Direito Tributário para advogados iniciantes
Público: Advogados formados há menos de 3 anos
Preço: R$ 1.997 à vista ou 12x R$ 197
Diferencial: método com aproveitamento de 94% em concursos da área fiscal
```

### Gemini com Google Docs (Workspace)

Para skills de documentos longos (pareceres, propostas, relatórios):

1. Abra um Google Doc
2. Clique em **Gemini** (ícone de estrela na barra lateral)
3. Cole o prompt do skill diretamente no painel lateral
4. O Gemini gera o conteúdo direto no documento

**Exemplo real — skill [`Jurídico & Advocacia/218-Modelo de Parecer Jurídico Rápido.md`](Jurídico%20%26%20Advocacia/218-Modelo%20de%20Parecer%20Jurídico%20Rápido.md):**

```
[prompt do skill]

Tema: Responsabilidade tributária do sócio-gerente em execução fiscal
Legislação aplicável: CTN art. 135, III
Posição do cliente: devedor redirecionado após encerramento irregular
Jurisprudência relevante: REsp 1.104.900/ES (recurso repetitivo STJ)
```

### Gemini com upload de arquivo

Para skills que analisam documentos:

```
1. Clique no ícone de clipe (anexar arquivo)
2. Faça upload do contrato, relatório ou planilha
3. Cole o prompt do skill
4. Peça a análise sobre o arquivo enviado
```

**Exemplo:**

```
[prompt do skill Análise e Revisão Estratégica de Contratos]

Analise o contrato em anexo. Identifique as 3 cláusulas de maior risco
para o contratante e sugira redação alternativa para cada uma.
```

---

## Google Antigravity

> Ferramenta de IA do Google disponível em [antigravity.google](https://antigravity.google/product/antigravity-2).

### Acesso

Acesse em: **https://antigravity.google/product/antigravity-2**

### Uso básico com um skill

O fluxo segue o mesmo padrão das outras ferramentas:

1. Abra a interface do Google Antigravity
2. Copie o prompt do skill desejado
3. Preencha as variáveis entre `[ ]` com o seu contexto
4. Envie e itere sobre a resposta

**Exemplo real — skill [`SEO/589-Pesquisa de Palavras-Chave e Tendências de Mercado.md`](SEO/589-Pesquisa%20de%20Palavras-Chave%20e%20Tendências%20de%20Mercado.md):**

```
[prompt do skill]

Segmento: escritório de advocacia tributária em São Paulo
Serviço principal: defesa em execuções fiscais e exclusão do ICMS do PIS/Cofins
Concorrentes diretos: [nomes dos escritórios concorrentes]
```

> **Nota:** Assim que tiver acesso completo à ferramenta, atualize esta seção com as funcionalidades específicas do Antigravity — integrações nativas, capacidade de memória, acesso à web em tempo real, etc.

---

## OpenAI Codex

> Modelo de IA da OpenAI via API ou [platform.openai.com](https://platform.openai.com). Ideal para skills de **Código** e automações que precisam de integração programática.

### Uso via Playground

1. Acesse [platform.openai.com/playground](https://platform.openai.com/playground)
2. Selecione o modelo `gpt-4o` ou `o1`
3. Em **System**, cole a identidade do skill (primeira parte do prompt, geralmente "Você é um...")
4. Em **User**, cole o restante com seus dados preenchidos

**Exemplo real — skill [`Código/124-Pipeline CI_CD (GitHub Actions).md`](Código/124-Pipeline%20CI_CD%20(GitHub%20Actions).md):**

```
# Campo System:
Você é um engenheiro DevOps sênior especialista em CI/CD com GitHub Actions...

# Campo User:
Projeto: API Node.js com TypeScript
Repositório: monorepo com /api e /frontend
Testes: Jest (unitários) + Playwright (e2e)
Deploy: Railway (produção) e Render (staging)
Requisitos: rodar testes antes do deploy, cache de dependências, notificação no Slack em falha
```

### Uso via API (integração programática)

Para automatizar o uso dos skills em scripts ou pipelines:

```python
import openai

# Carrega o skill de um arquivo .md
with open("Código/121-Debugger Sistemático (Causa Raiz).md", "r") as f:
    skill_content = f.read()

client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": skill_content  # prompt do skill como instrução de sistema
        },
        {
            "role": "user",
            "content": """
                Tecnologia/Stack: Node.js 20, Express, PostgreSQL
                Descrição do bug: memory leak em produção, uso de RAM cresce 50MB/hora
                Comportamento esperado: uso de RAM estável em ~200MB
                O que já tentei: reiniciar o serviço a cada 6h como paliativo
            """
        }
    ]
)

print(response.choices[0].message.content)
```

### Uso via CLI com curl

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "system",
        "content": "Você é um especialista em design de API RESTful..."
      },
      {
        "role": "user",
        "content": "Projete uma API para um sistema de agendamentos médicos com múltiplas especialidades"
      }
    ]
  }'
```

---

## Dicas Universais

Estas práticas funcionam em qualquer ferramenta.

### Preencha todas as variáveis

Prompts com `[ ]` não preenchidos geram respostas genéricas. Quanto mais contexto, melhor o output.

```
# ❌ Fraco
Produto: [seu produto]

# ✅ Forte
Produto: Curso online de Excel para assistentes administrativos de clínicas médicas,
focado em controle de agenda e faturamento de convênios, entregue 100% em vídeo-aulas
```

### Use o skill como ponto de partida

Após a primeira resposta, refine com perguntas de follow-up:

```
> [resposta do skill]

Agora reescreva o segundo parágrafo em tom mais direto e reduza para 3 bullet points.
```

### Combine skills de categorias diferentes

Skills de categorias distintas se complementam:

```
1. Use "Briefing de Campanha de Marketing" para estruturar a estratégia
2. Use "Copy para Landing Page" para escrever o texto de conversão
3. Use "Definição de Métricas e Dashboard" para montar os KPIs
```

### Salve seus prompts preenchidos

Após preencher um skill com seu contexto, salve como template pessoal para reusar:

```bash
# Crie uma pasta local com seus templates preenchidos
mkdir meus-templates
cp "Marketing/848-Página de Venda Express.md" meus-templates/pagina-venda-mentoria.md
# edite o arquivo com seus dados permanentes já preenchidos
```

---

> Dúvidas ou sugestões? Abra uma [Issue](../../issues) ou conecte-se no [LinkedIn](https://www.linkedin.com/in/tiagopgr/).
