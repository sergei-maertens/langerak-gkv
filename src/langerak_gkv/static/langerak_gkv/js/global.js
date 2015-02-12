$(function() {

	// should get this from the settings but meh
	FOOTER_MAP_COORDINATES = {
		lat: 51.9307267,
		lng: 4.8763104
	};

	$(window).on('map:init', function (e) {
		var detail = e.originalEvent ? e.originalEvent.detail : e.detail;
		// add marker
		// console.log(detail.map);
		L.marker([FOOTER_MAP_COORDINATES.lat, FOOTER_MAP_COORDINATES.lng]).addTo(detail.map);
	});

});


