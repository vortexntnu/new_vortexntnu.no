var nav = document.querySelector("nav");
var links = document.getElementById("link-wrapper");
var scroll_position = window.scrollY;
var ticking = false;

nav.style.position = "fixed";

if(scroll_position > 0) {
    nav.style.backgroundColor = "#151515";
    nav.style.height = "50px";
    links.style.top = "7px"
}

function sticky_nav(scroll_pos) {
    if (scroll_pos == 0) {
        nav.style.backgroundColor = "transparent";
        nav.style.height = "100px";
        links.style.top = "20px";
    } else {
        nav.style.backgroundColor = "#151515";
        nav.style.height = "50px";
        links.style.top = "7px"
    }
}

function throttle1() {
    scroll_position = window.scrollY;
    if (!ticking) {
        window.requestAnimationFrame(throttle2);
    }
    ticking = true;
}

function throttle2() {
    sticky_nav(scroll_position);
    ticking = false;
}

window.addEventListener('scroll', throttle1);