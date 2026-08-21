/*
 * SovereignRO Wiki - custom JS
 * Powers the patch notes panel on the home page: builds the tab strip
 * (dates) and content panes from window.SR_PATCH_NOTES (defined inline
 * in docs/index.md) and wires up the click-to-switch behavior.
 *
 * The markup is built here in JS rather than written directly as
 * Markdown/HTML in index.md because several near-identical raw HTML
 * blocks in a row tripped up Python-Markdown's md_in_html handling
 * (blocks after the 2nd got wrapped in a code block instead of staying
 * raw HTML). Generating them client-side sidesteps that entirely.
 */

function renderPatchPanels() {
  document.querySelectorAll("[data-sr-patch-body]").forEach((body) => {
    const notes = window.SR_PATCH_NOTES || [];
    if (!notes.length) return;

    body.innerHTML = "";

    const tabs = document.createElement("div");
    tabs.className = "sr-patch-panel-tabs";

    const content = document.createElement("div");
    content.className = "sr-patch-panel-content";

    notes.forEach((note, index) => {
      const tab = document.createElement("button");
      tab.className = "sr-patch-panel-tab" + (index === 0 ? " is-active" : "");
      tab.dataset.target = note.id;
      tab.innerHTML =
        '<span class="sr-patch-panel-tab-date">' + note.label + "</span>" +
        '<span class="sr-patch-panel-tab-year">' + note.year + "</span>";
      tabs.appendChild(tab);

      const pane = document.createElement("div");
      pane.className = "sr-patch-panel-pane" + (index === 0 ? " is-active" : "");
      pane.dataset.pane = note.id;
      pane.innerHTML = note.html;
      content.appendChild(pane);

      tab.addEventListener("click", () => {
        tabs.querySelectorAll(".sr-patch-panel-tab").forEach((t) => {
          t.classList.toggle("is-active", t === tab);
        });
        content.querySelectorAll(".sr-patch-panel-pane").forEach((p) => {
          p.classList.toggle("is-active", p.dataset.pane === note.id);
        });
      });
    });

    body.appendChild(tabs);
    body.appendChild(content);
  });
}

if (typeof document$ !== "undefined") {
  // MkDocs Material's instant loading emits this observable on every
  // page navigation, so re-run each time new content is swapped in.
  document$.subscribe(() => {
    renderPatchPanels();
  });
} else {
  document.addEventListener("DOMContentLoaded", renderPatchPanels);
}
