---
title: "PRISM Lab - Playground"
layout: gridlay
excerpt: "PRISM Lab: Playground"
sitemap: false
permalink: /playground/
---

<style>
.pg-frame-wrap {
  position: relative;
  width: 100%;
  height: calc(100vh - 150px);
  min-height: 620px;
  border: 1px solid #e2e2e2;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 34px rgba(0,0,0,.12);
}
html[data-theme="dark"] .pg-frame-wrap { border-color: #26314f; box-shadow: 0 10px 34px rgba(0,0,0,.45); }
.pg-frame-wrap iframe { width: 100%; height: 100%; border: 0; display: block; }
.pg-fallback { font-size: 13px; margin-top: 12px; color: #888; }
</style>

<div class="pg-frame-wrap">
  <iframe src="{{ site.url }}{{ site.baseurl }}/pg/index.html" title="PRISM Playground" loading="lazy"></iframe>
</div>

<p class="pg-fallback">
  On a narrow screen, we recommend opening the <a href="{{ site.url }}{{ site.baseurl }}/pg/index.html" target="_blank" rel="noopener">full playground in a new tab</a>.
</p>
