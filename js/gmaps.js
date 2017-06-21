function initMap() {
        var kontor = {lat: 63.418551, lng: 10.399409};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: kontor
        });
        var marker = new google.maps.Marker({
          position: kontor,
          map: map
        });
}