#!/usr/bin/env python3
"""
Setup script: gera a estrutura de marketplace do Claude Code
a partir dos arquivos .md existentes no repositorio.

Estrutura gerada (13 plugins, um por categoria):

  skills/<categoria>/                  <- plugin por categoria
    .claude-plugin/
      plugin.json
    skills/
      <skill-slug>/
        SKILL.md

  .claude-plugin/marketplace.json      <- 13 entradas (uma por plugin)
  .claude/commands/<categoria>/*.md    <- slash commands

Uso:
  python setup_marketplace.py
"""
import os, json, re, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

CAT_MAP = {
    "Carreira": {
        "slug": "carreira",
        "description": "Skills de carreira - posicionamento, bio, LinkedIn, curriculo, mentoria, thought leadership, portfolio e precificacao para freelancers.",
        "keywords": ["carreira", "linkedin", "posicionamento", "curriculo", "mentoria"],
    },
    "Conteudo & Copy": {
        "slug": "conteudo-copy",
        "description": "Skills de conteudo e copywriting - headlines, hooks, carrosseis, roteiros de Reels, VSLs, paginas de venda, e-mails e newsletters.",
        "keywords": ["copy", "conteudo", "marketing", "headlines", "reels", "email"],
    },
    "Codigo": {
        "slug": "codigo",
        "description": "Skills para desenvolvimento de software - debugging, design de API RESTful, CI/CD, Dockerfile, code review, testes e autenticacao.",
        "keywords": ["codigo", "desenvolvimento", "api", "debug", "testes", "devops"],
    },
    "Design & Branding": {
        "slug": "design-branding",
        "description": "Skills de design e branding - briefing estrategico, proposta comercial, identidade visual, naming, moodboard e precificacao de projetos.",
        "keywords": ["design", "branding", "identidade-visual", "naming", "proposta"],
    },
    "Direcao Criativa": {
        "slug": "direcao-criativa",
        "description": "Skills de direcao criativa - conceito de campanha, direcao de arte, narrativa visual, branding estrategico e portfolio criativo.",
        "keywords": ["criativo", "campanha", "direcao-de-arte", "narrativa", "portfolio"],
    },
    "Financeiro": {
        "slug": "financeiro",
        "description": "Skills financeiros - fluxo de caixa, DRE gerencial, precificacao, contratos, conciliacao bancaria e planejamento tributario.",
        "keywords": ["financeiro", "contratos", "precificacao", "fluxo-de-caixa", "tributario"],
    },
    "Juridico & Advocacia": {
        "slug": "juridico-advocacia",
        "description": "Skills juridicos - peticoes, contestacoes, pareceres, contratos, gestao de escritorio, captacao de clientes e honorarios.",
        "keywords": ["juridico", "advocacia", "peticoes", "contratos", "escritorio"],
    },
    "Lideranca & Equipes": {
        "slug": "lideranca-equipes",
        "description": "Skills de lideranca - OKRs, feedback estruturado, delegacao, onboarding de time, reunioes produtivas e avaliacao de desempenho.",
        "keywords": ["lideranca", "equipes", "okrs", "feedback", "delegacao", "onboarding"],
    },
    "Marketing": {
        "slug": "marketing",
        "description": "Skills de marketing - funis de venda, campanhas Meta/TikTok Ads, propostas comerciais, scripts de reuniao e lancamentos digitais.",
        "keywords": ["marketing", "vendas", "ads", "funil", "lancamento", "proposta"],
    },
    "Operacoes": {
        "slug": "operacoes",
        "description": "Skills de operacoes - SOPs, POPs, delegacao, onboarding, planejamento trimestral, gestao de projetos e diagnostico de gargalos.",
        "keywords": ["operacoes", "sop", "processos", "onboarding", "gestao", "planejamento"],
    },
    "Produto": {
        "slug": "produto",
        "description": "Skills de produto - KPIs, lancamento de produto digital, otimizacao de conversao, analise de churn, SEO e relatorios executivos.",
        "keywords": ["produto", "kpis", "conversao", "churn", "lancamento", "metricas"],
    },
    "Rotina": {
        "slug": "rotina",
        "description": "Skills de rotina e produtividade - planejamento semanal, batching de conteudo, GTD, blocos de foco e revisao semanal.",
        "keywords": ["rotina", "produtividade", "planejamento", "gtd", "foco", "semanal"],
    },
    "SEO": {
        "slug": "seo",
        "description": "Skills de SEO e dados - analise de metricas, pesquisa de mercado, analise de concorrencia, funil de conversao e KPIs.",
        "keywords": ["seo", "metricas", "dados", "mercado", "concorrencia", "kpis"],
    },
}

# Maps CAT_MAP keys to actual folder names on disk
DIR_MAP = {
    "Carreira": "Carreira",
    "Conteudo & Copy": "Conteúdo & Copy",
    "Codigo": "Código",
    "Design & Branding": "Design & Branding",
    "Direcao Criativa": "Direção Criativa",
    "Financeiro": "Financeiro",
    "Juridico & Advocacia": "Jurídico & Advocacia",
    "Lideranca & Equipes": "Liderança & Equipes",
    "Marketing": "Marketing",
    "Operacoes": "Operações",
    "Produto": "Produto",
    "Rotina": "Rotina",
    "SEO": "SEO",
}


def find_src_dir(base, cat_name):
    """Resolve the actual folder name from DIR_MAP."""
    folder = DIR_MAP.get(cat_name, cat_name)
    path = os.path.join(base, folder)
    return path if os.path.isdir(path) else None


def extract_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None, None
    end = content.find("---", 3)
    if end == -1:
        return None, None
    fm = content[3:end]
    name = desc = None
    for line in fm.splitlines():
        if line.startswith("name:"):
            name = line[5:].strip()
        elif line.startswith("description:"):
            desc = line[12:].strip()
    return name, desc


def safe_slug(s):
    """Fallback slug from filename when name: is missing."""
    s = s.lower()
    s = re.sub(r"[\s]+", "-", s)
    s = re.sub(r"[^a-z0-9-]", "", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


# Clean and recreate skills/ and .claude/commands/
skills_root = os.path.join(BASE, "skills")
commands_root = os.path.join(BASE, ".claude", "commands")

if os.path.exists(skills_root):
    shutil.rmtree(skills_root)
if os.path.exists(commands_root):
    shutil.rmtree(commands_root)

os.makedirs(skills_root)
os.makedirs(commands_root)
os.makedirs(os.path.join(BASE, ".claude-plugin"), exist_ok=True)

marketplace_plugins = []
total_skills = 0

for cat_name, cat_info in CAT_MAP.items():
    src_dir = find_src_dir(BASE, cat_name)
    if not src_dir:
        print(f"  [SKIP] Directory not found: {cat_name}")
        continue

    cat_slug = cat_info["slug"]
    cat_desc = cat_info["description"]
    cat_keywords = cat_info["keywords"]

    # Plugin directory: skills/<cat_slug>/
    plugin_dir = os.path.join(skills_root, cat_slug)
    plugin_meta_dir = os.path.join(plugin_dir, ".claude-plugin")
    plugin_skills_dir = os.path.join(plugin_dir, "skills")
    os.makedirs(plugin_meta_dir)
    os.makedirs(plugin_skills_dir)

    # .claude/commands/<cat_slug>/ for slash commands
    cmd_dir = os.path.join(commands_root, cat_slug)
    os.makedirs(cmd_dir)

    # Collect and process skill files
    md_files = sorted(f for f in os.listdir(src_dir) if f.endswith(".md"))
    skill_count = 0

    for fname in md_files:
        fpath = os.path.join(src_dir, fname)
        name, desc = extract_frontmatter(fpath)

        # Skill slug: prefer name: from frontmatter, fall back to filename
        if name:
            skill_slug = name
        else:
            base = os.path.splitext(fname)[0]
            # Strip leading numeric prefix (e.g. "173-Script..." -> "script...")
            base = re.sub(r"^\d+-\s*", "", base)
            skill_slug = safe_slug(base)

        # Create skills/<cat>/<skill-slug>/SKILL.md inside plugin
        skill_dir = os.path.join(plugin_skills_dir, skill_slug)
        os.makedirs(skill_dir, exist_ok=True)
        shutil.copy2(fpath, os.path.join(skill_dir, "SKILL.md"))

        # Create flat .md for slash commands
        shutil.copy2(fpath, os.path.join(cmd_dir, f"{skill_slug}.md"))

        skill_count += 1

    # plugin.json -- required by Claude Code plugin spec
    plugin_json = {
        "name": cat_slug,
        "description": cat_desc,
        "version": "1.0.0",
        "author": {
            "name": "Tiago PGR",
            "email": "tiagopgr22@gmail.com",
        },
        "homepage": "https://github.com/tiagopgr/skills-ia",
        "repository": "https://github.com/tiagopgr/skills-ia",
        "license": "MIT",
        "keywords": cat_keywords,
    }
    plugin_json_path = os.path.join(plugin_meta_dir, "plugin.json")
    with open(plugin_json_path, "w", encoding="utf-8") as f:
        json.dump(plugin_json, f, ensure_ascii=False, indent=2)

    # Marketplace entry for this plugin
    marketplace_plugins.append({
        "name": cat_slug,
        "source": f"./skills/{cat_slug}",
        "description": cat_desc,
        "category": cat_name,
        "keywords": cat_keywords,
    })

    total_skills += skill_count
    print(f"  [OK] {cat_slug}: {skill_count} skills")

# marketplace.json
manifest = {
    "name": "skills-ia",
    "owner": {
        "name": "Tiago PGR",
        "email": "tiagopgr22@gmail.com",
    },
    "description": "+1.100 skills profissionais prontos para usar com Claude Code - 13 categorias.",
    "plugins": marketplace_plugins,
}

out = os.path.join(BASE, ".claude-plugin", "marketplace.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\n[OK] {total_skills} skills processados em {len(marketplace_plugins)} plugins")
print(f"[OK] .claude-plugin/marketplace.json atualizado")
print(f"[OK] skills/ recriado ({len(marketplace_plugins)} plugins por categoria)")
print(f"[OK] .claude/commands/ recriado ({len(marketplace_plugins)} categorias)")
print("\nPara usar localmente:")
print("  /plugin marketplace add ./")
print("  /plugin install carreira@skills-ia")
print("  /plugin install marketing@skills-ia")
print("  # ... (um por categoria)")
