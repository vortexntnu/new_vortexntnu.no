var nav = document.querySelector("nav");
var links = document.getElementById("link-wrapper");
var last_known_scroll_position = 0;
var ticking = false;

nav.style.position = "fixed";

function doSomething(scroll_pos) {
    if (scroll_pos == 0) {
        nav.style.backgroundColor = "transparent";
        nav.style.height = "100px";
        links.style.top = "20px";
    } else {
        nav.style.backgroundColor = "#252525";
        nav.style.height = "50px";
        links.style.top = "7px"
    }
}

window.addEventListener('scroll', function() {
    last_known_scroll_position = window.scrollY;
    if (!ticking) {
        window.requestAnimationFrame(function() {
            doSomething(last_known_scroll_position);
            ticking = false;
        });
    }
    ticking = true;
});