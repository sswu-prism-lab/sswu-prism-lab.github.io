---
title: "PRISM Lab - Playground"
layout: gridlay
excerpt: "PRISM Lab: Playground"
sitemap: false
permalink: /playground/
---

# Playground

<iframe id="pgframe" src="{{ site.url }}{{ site.baseurl }}/pg/index.html" title="PRISM Playground"
        style="width:100%;border:0;display:block;height:900px"></iframe>

<script>
(function () {
  var f = document.getElementById('pgframe');
  if (!f) return;
  var ro = null;
  var firstLoad = true;

  function scrollToTop() {
    try {
      var y = f.getBoundingClientRect().top + window.pageYOffset - 64;
      window.scrollTo(0, y < 0 ? 0 : y);
    } catch (e) {}
  }

  function resize() {
    try {
      var d = f.contentWindow.document;
      var h = Math.max(d.body.scrollHeight, d.documentElement.scrollHeight);
      if (h > 60) f.style.height = h + 'px';
    } catch (e) {}
  }

  function hook() {
    resize();
    [120, 350, 800, 1500].forEach(function (t) { setTimeout(resize, t); });
    if (!firstLoad) { scrollToTop(); setTimeout(scrollToTop, 120); }
    firstLoad = false;
    try {
      if (ro) ro.disconnect();
      ro = new ResizeObserver(resize);
      ro.observe(f.contentWindow.document.body);
    } catch (e) {}
  }

  f.addEventListener('load', hook);
  window.addEventListener('resize', resize);
  setInterval(resize, 1000);   // safety net (fonts, late layout, in-iframe navigation)
})();
</script>
