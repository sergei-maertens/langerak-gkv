+(function($) {
    $(function() {

        // should get this from the settings but meh
        FOOTER_MAP_COORDINATES = {
            lat: 51.9307267,
            lng: 4.8763104
        };

        // map in footer
        L.Icon.Default.imagePath = '/static/leaflet/images/';
        $(window).on('map:init', function (e) {
            var detail = e.originalEvent ? e.originalEvent.detail : e.detail;
            if (detail.id != 'footer-map') {
                return;
            }
            // add marker
            L.marker([FOOTER_MAP_COORDINATES.lat, FOOTER_MAP_COORDINATES.lng]).addTo(detail.map);
        });

        $(window).resize(function() {
            $('.link-height').data('processed', false).height('auto');
            syncHeights();
        });

        // popovers
        $('[data-toggle="popover"]').popover();
        $('.help').popover({
            'placement': 'auto right'
        });


        $('form.dropdown-menu').on('click', ':not([type="submit"])', function(e) {
            if ($(this).is('a')) {
                window.location = $(this).attr('href');
            }
            e.preventDefault();
            return false;
        });
    });

    $(window).on('load', syncHeights);

    function syncHeights() {
        $('.link-height').each(function() {
            if($(this).data('processed')) {
                return;
            }

            var linkID = $(this).data('linkid');
            var set  = $('.link-height[data-linkid="'+linkID+'"]');
            set.data('processed', true);

            var height = $.map(set, function(e) {
                return $(e).height();
            }).reduce(function(prevResult, element, index, input) {
                return Math.max(prevResult, element);
            });
            set.each(function() {
                $(this).height(height);
            });
        });
    }

})(window.jQuery);
