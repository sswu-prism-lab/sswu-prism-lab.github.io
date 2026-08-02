---
title: "PRISM Lab - Playground"
layout: gridlay
excerpt: "PRISM Lab: Playground"
sitemap: false
permalink: /playground/
---

# <span class="i18n-en">Playground</span><span class="i18n-ko">놀이터</span>

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


### <span class="i18n-en">You can now enjoy a wider variety of playgrounds in the PRISM Lab app, now available on the App Store.</span><span class="i18n-ko">App Store에 출시된 PRISM Lab 애플리케이션에서 보다 다양한 플레이그라운드를 즐길 수 있습니다.</span>

#### <span class="i18n-en">Developer Contact: dwight1014@gmail.com</span><span class="i18n-ko">개발자 연락처: dwight1014@gmail.com</span>
#### <span class="i18n-en">Explore a wide range of ML/AI concepts — including machine learning and deep learning — hands-on through interactive playgrounds on your iPhone and iPad. The app also covers foundational concepts you'll need before diving into AI, such as basic mathematics and data structures. You can adjust settings yourself to see how the results change, and learn each concept through accompanying explanatory text.</span><span class="i18n-ko">iPhone 및 iPad에서 머신러닝, 딥러닝 등 다양한 ML/AI 개념들에 대해 직접 Playground를 통해 실험해보세요. 기초 수학이나 자료구조 등 AI를 탐구하기 전에 필요한 개념들을 포함하고 있습니다. 직접 설정값들을 조정해서 실험 결과를 바꿀 수 있고, 설명 텍스트를 통해 개념들에 대해 학습할 수 있습니다.</span>
#### <span class="i18n-en">Privacy Policy: We do not collect any personal data or information from our users.</span><span class="i18n-ko">개인정보 처리방침: 저희는 사용자로부터 어떠한 개인정보나 데이터도 수집하지 않습니다.</span>
