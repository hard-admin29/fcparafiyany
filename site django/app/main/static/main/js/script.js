"use strict";


$(document).ready(function () {

    let animation = lottie.loadAnimation({
      container: document.getElementById('lottie-animation'),
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: '/static/main/animations/ban.json'
    });
    let toTopBtn = document.getElementById("toTopBtn");

    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            toTopBtn.style.opacity = "1";
        } else {
            toTopBtn.style.opacity = "0";
        }
    }

    toTopBtn.onclick = function() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }
})