$(function() {
    var map;
    var geocoder = new google.maps.Geocoder();

    $(window).on('map:init', function (e) {
        var detail = e.originalEvent ? e.originalEvent.detail : e.detail;
        if (detail.id != 'user-map') {
            return;
        }
        map = detail.map;
        map.setZoom(15);

        // geocode address
        if (window.address) {
            geocoder.geocode( {'address': window.address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var lat = results[0].geometry.location.lat();
                    var lng = results[0].geometry.location.lng();
                    try {
                        var latlng = new L.LatLng(lat, lng);
                        // add marker & center
                        L.marker(latlng).addTo(detail.map);
                        detail.map.panTo(latlng);
                    } catch (e) {
                        console.log(e); // TODO: sentry
                    }
                } else if (window.console) {
                    console.warn("Geocode was not successful for the following reason: " + status);
                }
            });
        }
    });

});
