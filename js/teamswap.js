showTeam(0);

function showTeam(n) {
    var teams = document.getElementsByClassName("team");
    var dots = document.getElementsByClassName("yeardot");
    dots
    
    for (var i = 0; i < teams.length; i++) {
        teams[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" activeyear", "");
    }
    teams[n].style.display = "block";
    dots[dots.length-n-1].className += " activeyear";
}