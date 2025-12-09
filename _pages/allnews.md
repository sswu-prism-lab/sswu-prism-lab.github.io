---
title: "News"
layout: textlay
excerpt: "PRISM Lab at Sungshin Women's University."
sitemap: false
permalink: /allnews/
---

# News

{% for article in site.data.news %}

{{ article.date }} <br> {{ article.headline | markdownify}}

{% endfor %}
