var slideIndex2 = 1;
var timer2;

showSlides2(slideIndex2);

function plusSlides2(n) {
    showSlides2(slideIndex2 += n);
}

function currentSlide2(n) {
    showSlides2(slideIndex2 = n);
}

function showSlides2(n) {
    clearTimeout(timer2);
    timer2 = window.setTimeout(function() { plusSlides2(1); },5000);
    
    var i;
    var slides = document.getElementsByClassName("mySlides2");
    var dots = document.getElementsByClassName("dot2");
    if (n > slides.length) {
        slideIndex2 = 1
    }
    if (n < 1) {
        slideIndex2 = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex2 - 1].style.display = "block";
}