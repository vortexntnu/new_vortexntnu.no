var slideIndex1 = 1;
var timer1;

showSlides1(slideIndex1);

function plusSlides1(n) {
    showSlides1(slideIndex1 += n);
}

function currentSlide1(n) {
    showSlides1(slideIndex1 = n);
}

function showSlides1(n) {
    clearTimeout(timer1);
    timer1 = window.setTimeout(function() { plusSlides1(1); },8000);
    
    var i;
    var slides = document.getElementsByClassName("mySlides1");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex1 = 1
    }
    if (n < 1) {
        slideIndex1 = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex1 - 1].style.display = "block";
    dots[slideIndex1 - 1].className += " active";
}