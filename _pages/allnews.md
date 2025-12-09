---
title: "News"
layout: textlay
excerpt: "PRISM Lab at Sungshin Women's University."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}

{{ article.date }} <br> {{ article.headline | markdownify}}

{% endfor %}
