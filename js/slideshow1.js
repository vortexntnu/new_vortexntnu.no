var slideIndex = 1;
showSlides1(slideIndex);

function plusSlides1(n) {
    showSlides1(slideIndex += n);
}

function currentSlide1(n) {
    showSlides1(slideIndex = n);
}

function showSlides1(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides1");
    var dots = document.getElementsByClassName("dot1");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}