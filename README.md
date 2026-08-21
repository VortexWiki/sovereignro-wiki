# SovereignRO Wiki

Wiki communautaire pour SovereignRO, construit avec [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) et deploye sur GitHub Pages.

## Developpement local

```bash
pip install -r requirements.txt
mkdocs serve
```

Le site sera accessible sur `http://127.0.0.1:8000`.

## Build

```bash
mkdocs build
```

Le site statique est genere dans `site/`.

## Deploiement

Le deploiement se fait automatiquement via GitHub Actions (voir `.github/workflows/deploy.yml`) a chaque push sur `main`. Le site est publie sur GitHub Pages, puis pointe vers `wiki.sovereignro.com` via un enregistrement DNS CNAME une fois le domaine personnalise configure.

## Structure

```text
sovereignro-wiki/
├── mkdocs.yml
├── requirements.txt
├── docs/              # Contenu du wiki (Markdown)
├── overrides/          # Overrides du theme Material (partials, HTML)
└── .github/workflows/   # CI de deploiement
```

## Contribuer

1. Cree un compte GitHub si tu n'en as pas.
2. Demande a etre invite comme Collaborator sur le depot.
3. Modifie les pages directement depuis l'interface GitHub (ou en local).
4. Ouvre une Pull Request.
5. Une fois validee, le site est republie automatiquement.

Tu peux aussi proposer un guide via Discord ou en Markdown directement, l'equipe l'integrera au depot.

## Logo

Le logo du site (utilise pour `theme.logo` et `theme.favicon` dans `mkdocs.yml`) n'est pas encore ajoute. Il sera partage avec le [MVP Tracker](https://github.com/VortexWiki/sovereignro-mvp-tracker) une fois disponible. Voir `docs/assets/images/` pour l'emplacement prevu.
