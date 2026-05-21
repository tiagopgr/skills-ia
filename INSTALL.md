# Instalação e Uso — Skills IA no Claude Code

Este guia explica como instalar os plugins desta biblioteca no **Claude Code** e como usar os skills no dia a dia.

---

## Instalação via Gerenciador de Plugins

Abra o Claude Code e adicione o repositório diretamente pelo gerenciador de plugins:

1. Acesse **Settings → Plugins** (ou `/plugin` no chat)
2. Clique em **Add Plugin** (ou "Adicionar plugin")
3. Cole a URL do repositório:

```
https://github.com/tiagopgr/skills-ia
```

4. Confirme a instalação

O Claude Code vai ler o `marketplace.json` automaticamente e listar os 13 plugins disponíveis.

---

## Instalar os plugins por categoria

Após adicionar o marketplace, instale as categorias que quiser usar:

```
/plugin install carreira@skills-ia
/plugin install conteudo-copy@skills-ia
/plugin install codigo@skills-ia
/plugin install design-branding@skills-ia
/plugin install direcao-criativa@skills-ia
/plugin install financeiro@skills-ia
/plugin install juridico-advocacia@skills-ia
/plugin install lideranca-equipes@skills-ia
/plugin install marketing@skills-ia
/plugin install operacoes@skills-ia
/plugin install produto@skills-ia
/plugin install rotina@skills-ia
/plugin install seo@skills-ia
```

Instale apenas os que fazem sentido para o seu trabalho.

---

## Usar os skills

Após instalar, os skills ficam disponíveis como slash commands no formato:

```
/<plugin>:<skill>
```

### Exemplos práticos

| O que você quer fazer | Comando |
|---|---|
| Criar um artigo de autoridade no LinkedIn | `/carreira:artigo-de-autoridade-para-linkedin` |
| Escrever copy para Meta Ads | `/conteudo-copy:copy-de-anuncios-meta-ads` |
| Debug sistemático de um bug | `/codigo:debugger-sistematico-causa-raiz` |
| Proposta comercial de branding | `/design-branding:proposta-comercial-de-projeto-de-branding-e-identidade-visual` |
| Analisar um contrato | `/financeiro:revisao-e-analise-de-contrato` |
| Criar uma petição inicial | `/juridico-advocacia:gerador-de-peticoes-estruturadas-com-teses-estrategicas` |
| Estruturar OKRs para a equipe | `/lideranca-equipes:okrs-objetivos-e-resultados-chave` |
| Sequência de e-mails de venda | `/marketing:sequencia-de-e-mails-de-venda` |
| Criar um SOP de processo interno | `/operacoes:criador-de-sop-operacional` |
| Definir KPIs do negócio | `/produto:definicao-de-kpis-por-tipo-de-negocio` |
| Planejamento semanal | `/rotina:planejamento-semanal-de-empreendedor-solo` |
| Analisar métricas de e-commerce | `/seo:analise-de-metricas-do-e-commerce` |

### Como funciona na prática

1. Digite o comando no Claude Code
2. O skill carrega o prompt especializado automaticamente
3. Preencha os campos entre `[ ]` com os dados do seu caso
4. Envie e receba o resultado

---

## Categorias disponíveis

| Plugin | Slug | Skills | Especialidade |
|---|---|:---:|---|
| Carreira | `carreira` | 38 | Posicionamento, LinkedIn, currículo, mentoria |
| Conteúdo & Copy | `conteudo-copy` | 210 | Headlines, hooks, carrosséis, VSLs, e-mails |
| Código | `codigo` | 22 | Debug, API, CI/CD, testes, autenticação |
| Design & Branding | `design-branding` | 24 | Briefing, naming, identidade visual, proposta |
| Direção Criativa | `direcao-criativa` | 20 | Conceito de campanha, direção de arte |
| Financeiro | `financeiro` | 133 | Fluxo de caixa, DRE, contratos, precificação |
| Jurídico & Advocacia | `juridico-advocacia` | 55 | Petições, contratos, honorários, gestão |
| Liderança & Equipes | `lideranca-equipes` | 26 | OKRs, feedback, delegação, onboarding |
| Marketing | `marketing` | 220 | Funis, Meta/TikTok Ads, proposta, lançamento |
| Operações | `operacoes` | 245 | SOPs, POPs, delegação, planejamento, gestão |
| Produto | `produto` | 44 | KPIs, lançamento digital, CRO, churn |
| Rotina | `rotina` | 89 | Planejamento semanal, GTD, foco, batching |
| SEO & Dados | `seo` | 33 | Métricas, concorrência, funil, KPIs |

**Total: 1.159 skills**

---

## Para uso local (clonar o repositório)

Se quiser usar a partir de uma cópia local ou contribuir com novos skills:

```bash
git clone https://github.com/tiagopgr/skills-ia.git
cd skills-ia
python setup_marketplace.py
```

Em seguida adicione o caminho local no gerenciador de plugins em vez da URL do GitHub.

> **Windows:** se `python` não for reconhecido, use o caminho completo:
> `C:\Users\<seu-usuario>\AppData\Local\Microsoft\WindowsApps\python3.exe setup_marketplace.py`
