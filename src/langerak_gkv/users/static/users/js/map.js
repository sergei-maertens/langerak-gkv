$(function() {

    var LOCATION = {
        lat: 51.9307267,
        lng: 4.8763104
    };

    $(window).on('map:init', function (e) {
        var detail = e.originalEvent ? e.originalEvent.detail : e.detail;
        // add marker & center
        var latlng = new L.LatLng(LOCATION.lat, LOCATION.lng);
        L.marker(latlng).addTo(detail.map);
        detail.map.panTo(latlng);
    });

});
