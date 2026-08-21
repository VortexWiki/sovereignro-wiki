<!--
  TEMPLATE : page de type "Troubleshooting" ou FAQ avec un bloc d'alerte
  rouge (icône + texte + liste de conseils) suivi d'une carte d'aide
  centrée avec un bouton (ex: Discord). Voir la vraie page Download pour
  un exemple complet en contexte (docs/download/index.md).
  Voir CONTRIBUTING.md pour le détail de chaque classe.
-->
---
title: Titre de la page
---

<span class="sov-eyebrow">// Ton label</span>

## <span class="sov-heading">Titre de la <span class="sov-accent">Section</span></span>

<div class="sov-troubleshoot" markdown>

<div class="sov-troubleshoot-alert" markdown>
<span class="sov-troubleshoot-alert-icon">
<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 9v4"/><path d="M12 17h.01"/><path d="M10.3 3.8 2 18a2 2 0 0 0 1.7 3h16.6a2 2 0 0 0 1.7-3L13.7 3.8a2 2 0 0 0-3.4 0z"/></svg>
</span>

<div markdown>

### Titre du problème courant

Explication du problème et de sa cause.

<div class="sov-troubleshoot-list" markdown>

- Première solution à essayer.
- Deuxième solution à essayer.
- Troisième solution à essayer.

</div>

</div>
</div>

<div class="sov-troubleshoot-help" markdown>

### Toujours coincé ?

Texte court qui invite à demander de l'aide.

[Rejoindre le Discord](https://discord.com/invite/eog){ .sov-btn-discord .sov-btn-lg }

</div>

</div>

<!--
  Rappel : ne jamais mettre {: .sov-troubleshoot-list } après une liste à
  puces, ça casse le style. Toujours le wrapper <div> comme ci-dessus.
-->
