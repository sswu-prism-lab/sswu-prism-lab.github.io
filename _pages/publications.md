---
title: "PRISM Lab - Publications"
layout: gridlay
excerpt: "PRISM Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

## Highlights

**At the end of this page, you can find the [full list of publications, proceedings, and patents](#full-list-of-publications).**

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>

## Full List of publications and proceedings

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}

## Patents
<em>고원준, 강종구, 최정원</em><br />뇌전도 신호를 이용한 자기지도학습 기반 피로 상태 추정 학습 모델 구축 방법 및 이를 이용한 피로 상태 추정 장치<br /> 출원번호: 10-2025-0190652, 출원일자: 2025.12.04

<em>석흥일, 고원준</em><br />딥러닝 기반 유전자형-표현형 데이터 분석 및 질병 진단 방법 및 장치<br /> 등록번호: 10-2747717, 등록일자: 2024.12.24
