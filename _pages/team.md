---
title: "PRISM Lab - Team"
layout: gridlay
excerpt: "PRISM Lab: Team members"
sitemap: false
permalink: /team/
---

# <span style="color:rgb(188, 90, 93);">P</span><span style="color:rgb(242, 221, 134);">R</span><span style="color:rgb(111, 142, 114);">I</span><span style="color:rgb(75, 85, 210);">S</span><span style="color:rgb(119, 94, 145);">M</span> Lab Members

<!-- #### Sorry, we have now reached full capacity. Currently, we are not seeking any new members ;( -->

#### Currently, we are looking for new <span style="color:rgb(188, 90, 93);">P</span><span style="color:rgb(242, 221, 134);">R</span><span style="color:rgb(111, 142, 114);">I</span><span style="color:rgb(75, 85, 210);">S</span><span style="color:rgb(119, 94, 145);">M</span> members, PhD/Master students or combined B.S.-Master students to join the team!

## Principal Investigator

{% for member in site.data.team_members %}
<div class="row" style="margin-bottom: 20px;">
  <div class="col-sm-12 clearfix">
    <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="15%" style="float: left; margin-right: 20px; border-radius: 4px;" />
    <h4 style="margin-top: 0;">{{ member.name }}</h4>
    <i>{{ member.info }} <br>email: &lt;{{ member.email }}&gt;</i>
    
    <ul style="overflow: hidden; margin-top: 10px; padding-left: 20px;">
      {% if member.number_educ >= 1 %} <li>{{ member.education1 }}</li> {% endif %}
      {% if member.number_educ >= 2 %} <li>{{ member.education2 }}</li> {% endif %}
      {% if member.number_educ >= 3 %} <li>{{ member.education3 }}</li> {% endif %}
      {% if member.number_educ >= 4 %} <li>{{ member.education4 }}</li> {% endif %}
      {% if member.number_educ >= 5 %} <li>{{ member.education5 }}</li> {% endif %}
    </ul>
  </div>
</div>
{% endfor %}

## Students

{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!-- <br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
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

## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row" style="margin-top: 5px; margin-bottom: 5px;">
{% endif %}

<div class="col-sm-6 clearfix" style="margin-bottom: 5px;">
  <h4 style="margin-top: 5px; margin-bottom: 2px;">{{ member.name }}</h4>
  <i style="font-size: 0.95em; color: #555;">{{ member.duration }} <br> Role: {{ member.info }} <br> Performance: {{ member.performance }}</i>
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
