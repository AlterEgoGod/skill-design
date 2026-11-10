/** Mount optional demo controls; no automatic injection or contrast guarantee. */
export function mountGlassControls(container, root = document.documentElement) {
  if (!(container instanceof Element) || !(root instanceof Element)) throw new TypeError("Expected DOM elements");
  const previous = { mode: root.getAttribute("data-design-glass"), alpha: root.style.getPropertyValue("--design-glass-alpha") };
  const panel = document.createElement("div");
  panel.className = "design-glass-settings";
  panel.innerHTML = '<label class="design-glass-switch"><input type="checkbox" role="switch"><span class="design-glass-track" aria-hidden="true"></span><span>Эффект стекла</span></label><label class="design-glass-range"><span>Прозрачность стекла: <output></output></span><input type="range" min="0" max="40" step="1" aria-label="Прозрачность стекла"></label>';
  container.append(panel);
  const toggle = panel.querySelector('[type="checkbox"]'), range = panel.querySelector('[type="range"]'), output = panel.querySelector("output");
  const currentAlpha = parseFloat(getComputedStyle(root).getPropertyValue("--design-glass-alpha"));
  toggle.checked = root.getAttribute("data-design-glass") === "on";
  range.value = String(Math.max(0, Math.min(40, Math.round((1 - (Number.isFinite(currentAlpha) ? currentAlpha : .88)) * 100))));
  function update() {
    root.setAttribute("data-design-glass", toggle.checked ? "on" : "off");
    root.style.setProperty("--design-glass-alpha", String(1 - Number(range.value) / 100));
    range.disabled = !toggle.checked;
    output.value = range.value + "%";
    range.setAttribute("aria-valuetext", range.value + "%");
  }
  toggle.addEventListener("change", update);
  range.addEventListener("input", update);
  update();
  return () => {
    toggle.removeEventListener("change", update);
    range.removeEventListener("input", update);
    panel.remove();
    if (previous.mode === null) root.removeAttribute("data-design-glass"); else root.setAttribute("data-design-glass", previous.mode);
    if (previous.alpha) root.style.setProperty("--design-glass-alpha", previous.alpha); else root.style.removeProperty("--design-glass-alpha");
  };
}
