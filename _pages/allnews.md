---
title: "PRISM Lab - News"
layout: textlay
excerpt: "PRISM Lab at Sungshin Women's University."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }}<br>{{ article.headline | markdownify}}</p>
{% endfor %}
