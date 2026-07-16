---
title: "PRISM Lab - Playground"
layout: gridlay
excerpt: "PRISM Lab: Playground"
sitemap: false
permalink: /playground/
---

<style>
.pg-intro { margin: 4px 0 16px; line-height: 1.6; }
.studio-frame-wrap {
  position: relative;
  width: 100%;
  height: calc(100vh - 160px);
  min-height: 600px;
  border: 1px solid #e2e2e2;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 34px rgba(0,0,0,.12);
}
html[data-theme="dark"] .studio-frame-wrap { border-color: #333; box-shadow: 0 10px 34px rgba(0,0,0,.45); }
.studio-frame-wrap iframe { width: 100%; height: 100%; border: 0; display: block; }
.pg-fallback { font-size: 13px; margin-top: 12px; color: #888; }
</style>

### Logo Playground

<div class="pg-intro" markdown="1">
Our lab logo is an **impossible object inspired by Penrose triangle** rendered as a rainbow prism.
Play with the palette, presets, center glow, and specular shine below — then export
your own version as **SVG** or **PNG**.
</div>

<div class="studio-frame-wrap">
  <iframe src="{{ site.url }}{{ site.baseurl }}/tools/logo-studio.html"
          title="PRISM Penrose Rainbow Studio" loading="lazy"></iframe>
</div>

<p class="pg-fallback">
  On a narrow screen, we recommend opening the <a href="{{ site.url }}{{ site.baseurl }}/tools/logo-studio.html" target="_blank" rel="noopener">full-screen version in a new tab</a>.
</p>
