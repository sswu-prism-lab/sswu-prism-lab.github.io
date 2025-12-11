---
title: "PRISM Lab - News"
layout: textlay
excerpt: "PRISM Lab at Sungshin Women's University."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<div class="news-item">
  <span style="font-size: 1.2em; font-weight: bold;">
    {{ article.date }}
  </span>
  <br>
  {{ article.headline | markdownify }}
</div>
{% endfor %}
