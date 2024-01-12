function iniciarMap() {
    var coord = { lat: 19.4123676, lng: -98.927634 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}
