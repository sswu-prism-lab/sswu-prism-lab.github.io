---
title: "PRISM Lab - Team"
layout: gridlay
excerpt: "PRISM Lab: Team members"
sitemap: false
permalink: /team/
---

# <span class="i18n-en"><span class="navbar-rainbow">PRISM</span> Lab Members</span><span class="i18n-ko"><span class="navbar-rainbow">PRISM</span> Lab 구성원</span>

<!-- #### Sorry, we have now reached full capacity. Currently, we are not seeking any new members ;( -->

<!-- #### Currently, we are looking for new <span style="color:rgb(188, 90, 93);">P</span><span style="color:rgb(242, 221, 134);">R</span><span style="color:rgb(111, 142, 114);">I</span><span style="color:rgb(75, 85, 210);">S</span><span style="color:rgb(119, 94, 145);">M</span> members, PhD/Master students or combined B.S.-Master students to join the team! -->

## <span class="i18n-en">Principal Investigator</span><span class="i18n-ko">연구책임자</span>

{% for member in site.data.team_members %}
<div class="row" style="margin-bottom: 20px;">
<div class="col-sm-12 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" style="float: left; width: 15%; min-width: 100px; max-width: 150px; margin-right: 20px; border-radius: 4px;" />
<h4 style="margin-top: 0;">{{ member.name }}</h4>
<i><span class="i18n-en">{{ member.info }}</span><span class="i18n-ko">{{ member.info_ko }}</span></i>
<ul style="overflow: hidden; margin-top: 10px; padding-left: 20px;">
{% if member.number_educ >= 1 %}<li><span class="i18n-en">{{ member.education1 }}</span><span class="i18n-ko">{{ member.education1_ko }}</span></li>{% endif %}
{% if member.number_educ >= 2 %}<li><span class="i18n-en">{{ member.education2 }}</span><span class="i18n-ko">{{ member.education2_ko }}</span></li>{% endif %}
{% if member.number_educ >= 3 %}<li><span class="i18n-en">{{ member.education3 }}</span><span class="i18n-ko">{{ member.education3_ko }}</span></li>{% endif %}
{% if member.number_educ >= 4 %}<li><span class="i18n-en">{{ member.education4 }}</span><span class="i18n-ko">{{ member.education4_ko }}</span></li>{% endif %}
{% if member.number_educ >= 5 %}<li><span class="i18n-en">{{ member.education5 }}</span><span class="i18n-ko">{{ member.education5_ko }}</span></li>{% endif %}
</ul>
</div>
</div>
{% endfor %}

## <span class="i18n-en">Students</span><span class="i18n-ko">참여연구원</span>

{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i><span class="i18n-en">{{ member.info }}</span><span class="i18n-ko">{{ member.info_ko }}</span> <!-- <br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> <span class="i18n-en">{{ member.education1 }}</span><span class="i18n-ko">{{ member.education1_ko }}</span> </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> <span class="i18n-en">{{ member.education1 }}</span><span class="i18n-ko">{{ member.education1_ko }}</span> </li>
  <li> <span class="i18n-en">{{ member.education2 }}</span><span class="i18n-ko">{{ member.education2_ko }}</span> </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> <span class="i18n-en">{{ member.education1 }}</span><span class="i18n-ko">{{ member.education1_ko }}</span> </li>
  <li> <span class="i18n-en">{{ member.education2 }}</span><span class="i18n-ko">{{ member.education2_ko }}</span> </li>
  <li> <span class="i18n-en">{{ member.education3 }}</span><span class="i18n-ko">{{ member.education3_ko }}</span> </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> <span class="i18n-en">{{ member.education1 }}</span><span class="i18n-ko">{{ member.education1_ko }}</span> </li>
  <li> <span class="i18n-en">{{ member.education2 }}</span><span class="i18n-ko">{{ member.education2_ko }}</span> </li>
  <li> <span class="i18n-en">{{ member.education3 }}</span><span class="i18n-ko">{{ member.education3_ko }}</span> </li>
  <li> <span class="i18n-en">{{ member.education4 }}</span><span class="i18n-ko">{{ member.education4_ko }}</span> </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## <span class="i18n-en">Alumni</span><span class="i18n-ko">졸업생</span>

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row" style="margin-top: 5px; margin-bottom: 5px;">
{% endif %}

<div class="col-sm-6 clearfix" style="margin-bottom: 5px;">
  <h4 style="margin-top: 5px; margin-bottom: 2px;">{{ member.name }}</h4>
  <i style="font-size: 0.95em; color: #555;"><span class="i18n-en">{{ member.duration }}</span><span class="i18n-ko">{{ member.duration_ko }}</span> <br> <span class="i18n-en">Role: {{ member.info }}</span><span class="i18n-ko">역할: {{ member.info_ko }}</span> <br> <span class="i18n-en">Achievements: {{ member.performance }}</span><span class="i18n-ko">성과: {{ member.performance_ko }}</span></i>
  <ul style="overflow: hidden; margin-bottom: 0;">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
