---
title: "PRISM Lab - Home"
layout: homelay
excerpt: "PRISM Lab at Sungshin Women's University &rarr; SSWU"
sitemap: false
permalink: /
---

<style>
.rainbow-link {
  background: linear-gradient(90deg,
    rgb(188,90,93), rgb(242,221,134), rgb(111,142,114),
    rgb(75,85,210), rgb(119,94,145), rgb(188,90,93));
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
  text-decoration: underline;
  animation: rainbow-shift 4s linear infinite;
}
.rainbow-link:hover {
  animation-duration: 1.5s;
}
@keyframes rainbow-shift {
  0%   { background-position: 0% center; }
  100% { background-position: 200% center; }
}

/* ---- Dark mode: "Current Open Positions" box ---- */
html[data-theme="dark"] #open-positions {
  background-color: #201a2e !important;
  border-color: #4a3d6b !important;
  color: #d8c9f5 !important;
}
html[data-theme="dark"] #open-positions h4,
html[data-theme="dark"] #open-positions h4 strong {
  color: #ecdfff !important;
}
html[data-theme="dark"] #open-positions a:not(.rainbow-link) {
  color: #b79cf0;
}

/* ---- Light / dark logo swap (bottom of the page) ---- */
.logo-dark { display: none; }
html[data-theme="dark"] .logo-light { display: none; }
html[data-theme="dark"] .logo-dark { display: inline; }
</style>

<div id="open-positions" class="alert" role="alert" style="margin: 20px 0; line-height: 1.6; background-color: #fafdff; border: 1px solid #e9d5ff; color: #5b21b6; border-radius: 6px;">
  <h4 style="margin-top: 0; margin-bottom: 10px; color: #5b21b6;"><strong>📢 <span class="i18n-en">Current Open Positions</span><span class="i18n-ko">현재 모집 중인 자리</span></strong></h4>
  <p style="margin-bottom: 8px;"><span class="i18n-en">We are currently seeking motivated students to join our lab:</span><span class="i18n-ko">우리 연구실에 함께할 열정적인 학생을 모집하고 있습니다:</span></p>
  <ul style="margin-bottom: 0; padding-left: 20px;">
    <li><strong><span class="i18n-en">Prospective Ph.D./Master Student:</span><span class="i18n-ko">박사/석사 과정 지원자:</span></strong> 2
      <ul style="margin-top: 5px; margin-bottom: 0; padding-left: 20px; list-style-type: circle;">
        <li><span class="i18n-en">Topic: Biomedical data representation and/or statistical deep learning</span><span class="i18n-ko">주제: 생체의학 데이터 표현 및/또는 통계적 딥러닝</span></li>
        <li><span class="i18n-en">Required: Experience with PyTorch</span><span class="i18n-ko">필수: PyTorch 사용 경험</span></li>
      </ul>
    </li>
    <li><strong><span class="i18n-en">Undergraduate Intern:</span><span class="i18n-ko">학부 인턴:</span></strong> 1
      <ul style="margin-top: 5px; margin-bottom: 0; padding-left: 20px; list-style-type: circle;">
        <li><span class="i18n-en">Topic: Biosignal representation</span><span class="i18n-ko">주제: 생체신호 표현</span></li>
        <li><span class="i18n-en">Preferred: Experience with PyTorch, Sophomore or Junior student</span><span class="i18n-ko">우대: PyTorch 사용 경험, 2학년 또는 3학년 학생</span></li>
      </ul>
    </li>
  </ul>
  <p style="margin-bottom: 0;"><span class="i18n-en">If you are interested, please contact </span><span class="i18n-ko">관심이 있으시면 </span><a href="mailto:wjko@sungshin.ac.kr" class="rainbow-link">Prof. Wonjun Ko</a><span class="i18n-ko">에게 연락해 주세요</span>😄</p>
</div>

#### <span class="i18n-en">We are Pattern Recognition and Intelligent System Modeling Lab!</span><span class="i18n-ko">우리는 패턴 인식 및 지능형 시스템 모델링 연구실입니다!</span>

<div style="text-align: justify;">

<div class="i18n-en" markdown="1">

In recent, machine learning and deep learning frameworks have become de facto standards in diverse fields, e.g., computer vision, natural language processing, and healthcare, thanks to their unprecedented caliber in data representation. Inter alia, biomedical tasks performed by experts are time-consuming and expensive per se; hence many pioneering studies tried to revolutionize the domain of biomedical artificial intelignece by enjoying the recent advancements of machine learning and deep learning. Nevertheless, room for improvement still exists, especially in the data-oriented viewpoint. 

Our research addresses fundamental problems in developing theoretically sound representation learning algorithms and frameworks for various data modalities such as image, signal, graph, and table in the biomedical artificial intelligence field.

- We aim to develop novel linear representation methods and deep neural network structures in the data-oriented perspective by considering distributional properties of given data.

- We aim to devise novel machine learning and deep learning algorithms and methods, grounded in the principles of Bayesian statistics, topology, and physics.

- We aim to propose biomedical artificial intelligence frameworks for biosignal (e.g., electroencephalogram) processing, neuroimaging (e.g., structural/functional magnetic resonance imaging) analysis, and data mining which can integrate multiple modalities (e.g., gene and neuroimaging).

</div>

<div class="i18n-ko" markdown="1">

최근 머신러닝과 딥러닝 프레임워크는 뛰어난 데이터 표현 능력 덕분에 컴퓨터 비전, 자연어 처리, 헬스케어 등 다양한 분야에서 사실상의 표준으로 자리 잡았습니다. 특히 전문가가 수행하는 생체의학 과제는 그 자체로 많은 시간과 비용이 소요되며, 이에 따라 여러 선구적인 연구들이 머신러닝과 딥러닝의 최근 발전을 활용하여 생체의학 인공지능 분야에 혁신을 일으키고자 하였습니다. 그럼에도 불구하고, 특히 데이터 중심의 관점에서 여전히 개선의 여지가 남아 있습니다. 

우리 연구는 생체의학 인공지능 분야에서 이미지, 신호, 그래프, 테이블 등 다양한 데이터 양식에 대해 이론적으로 견고한 표현 학습 알고리즘과 프레임워크를 개발하는 근본적인 문제를 다룹니다.

- 주어진 데이터의 분포적 특성을 고려하여, 데이터 중심의 관점에서 새로운 선형 표현 기법과 심층 신경망 구조를 개발하고자 합니다.

- 베이지안 통계, 위상수학, 물리학의 원리에 기반한 새로운 머신러닝 및 딥러닝 알고리즘과 기법을 고안하고자 합니다.

- 생체신호(예: 뇌전도) 처리, 신경영상(예: 구조적/기능적 자기공명영상) 분석, 그리고 다중 양식(예: 유전자 및 신경영상)을 통합할 수 있는 데이터 마이닝을 위한 생체의학 인공지능 프레임워크를 제안하고자 합니다.

</div>

<div markdown="0" id="carousel" class="carousel slide" data-ride="carousel" data-interval="4000" data-pause="hover" >
    <!-- Menu -->
    <ol class="carousel-indicators">
        <li data-target="#carousel" data-slide-to="0" class="active"></li>
        <li data-target="#carousel" data-slide-to="1"></li>
        <li data-target="#carousel" data-slide-to="2"></li>
        <li data-target="#carousel" data-slide-to="3"></li>
        <li data-target="#carousel" data-slide-to="4"></li>
        <li data-target="#carousel" data-slide-to="5"></li>
    </ol>

    <!-- Items -->
    <div class="carousel-inner" markdown="0">
        <div class="item active">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/slide10.png" alt="Slide 10" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/slide6.png" alt="Slide 6" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/slide9.png" alt="Slide 9" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/slide2.png" alt="Slide 2" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/slide8.png" alt="Slide 8" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/slide7.png" alt="Slide 7" />
        </div>
    </div>
  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

</div>

<!-- **We are looking for passionate new PhD/Master students to join the team!** -->

<figure class="fifth">
  <img class="logo-light" src="{{ site.url }}{{ site.baseurl }}/images/logopic/sswu_logo.png" style="width: 120px">
  <img class="logo-dark" src="{{ site.url }}{{ site.baseurl }}/images/logopic/sswu_logo_dark.png" style="width: 120px">
  <img class="logo-light" src="{{ site.url }}{{ site.baseurl }}/images/logopic/prism_lockup_h_light.svg" style="width: 300px">
  <img class="logo-dark" src="{{ site.url }}{{ site.baseurl }}/images/logopic/prism_lockup_h_dark.svg" style="width: 300px">
</figure>
