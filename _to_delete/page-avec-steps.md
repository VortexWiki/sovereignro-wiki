<!--
  TEMPLATE : page avec un bloc hero centré + une liste d'étapes numérotées
  (numéros rouges). Utile pour des guides "comment faire X en N étapes"
  (ex: Installation, un guide de quête, un setup).
  Voir CONTRIBUTING.md pour le détail de chaque classe.
-->
---
title: Titre de la page
---

<section class="sov-page-hero" markdown>

<span class="sov-eyebrow">// Ton label</span>

# <span class="sov-heading">Comment faire <span class="sov-accent">Ceci</span></span>

<p class="sov-page-intro" markdown>Une courte intro qui explique ce que le guide couvre.</p>

</section>

<span class="sov-eyebrow">// Étapes</span>

## <span class="sov-heading">Les <span class="sov-accent">Étapes</span></span>

<div class="sov-steps" markdown>

1. **Première étape** avec une explication courte.
2. **Deuxième étape** avec une explication. Tu peux inclure `du code inline`
   ou des [liens](https://exemple.com).
3. **Troisième étape**, et ainsi de suite.

</div>

<!--
  Rappel : ne jamais mettre {: .sov-steps } après la liste, ça casse le style.
  Toujours le wrapper <div class="sov-steps" markdown> ... </div> comme ci-dessus.
-->
