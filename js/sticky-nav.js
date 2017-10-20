var nav = document.querySelector("nav");
//var links = document.getElementById("link-wrapper");
//var img_link = document.getElementById("img-link");
var ticking = false;

//160,984 / 325,98

function shouldStick() {
    return window.scrollY === 0 || $( window ).width() > 768
}

if(scroll_position > 0) {
    nav.style.backgroundColor = "#151515";
    nav.style.height = "50px";
    links.style.top = "7px";
    img_link.style.width = "160.984px";
}

function sticky_nav() {
    if (shouldStick()) {
        nav.style.backgroundColor = "transparent";
        nav.style.height = "100px";
        links.style.top = "20px";
        img_link.style.width = "325.98px";
    } else {
        nav.style.backgroundColor = "#151515";
        nav.style.height = "50px";
        links.style.top = "7px";
        img_link.style.width = "160.984px";
    }
}

function throttle1() {
    if (!ticking) {
        window.requestAnimationFrame(throttle2);
    }
    ticking = true;
}

function throttle2() {
    sticky_nav();
    ticking = false;
}

window.addEventListener('scroll', throttle1);