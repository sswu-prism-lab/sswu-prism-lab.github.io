---
title: "PRISM Lab - News"
layout: textlay
excerpt: "PRISM Lab at Sungshin Women's University."
sitemap: false
permalink: /allnews.html
---

# <span class="i18n-en">News</span><span class="i18n-ko">뉴스</span>

{% for article in site.data.news %}
<div class="news-item" style="text-align: justify; margin-bottom: 20px;">
  
  <span style="font-size: 1.2em; font-weight: bold;">
    {{ article.date }}
  </span>
  <br>
  
  <span class="i18n-en">{{ article.headline | markdownify | remove: '<p>' | remove: '</p>' }}</span><span class="i18n-ko">{{ article.headline_ko | markdownify | remove: '<p>' | remove: '</p>' }}</span>
  
</div>
{% endfor %}
