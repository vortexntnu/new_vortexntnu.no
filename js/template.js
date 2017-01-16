nav = document.querySelector("nav");
//footer = document.getElementById("footer");

nav.innerHTML = "\
    <div id='core-nav'>\
        <a href='index.html'><img src='img/logo_og_navn.png'></a>\
        <div id='link-wrapper'>\
            <a href='index.html'>HOME</a>\
            <a href='projects.html'>PROJECTS</a>\
            <a href='about.html'>ABOUT</a>\
            <a href='team.html'>TEAM</a>\
            <a href='join.html'>JOIN US</a>\
        </div>\
    </div>";

console.log(nav);