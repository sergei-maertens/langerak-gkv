(function($, conf, undefined) {

    function renderCalendar(lang, feedURL) {
        $('#calendar').fullCalendar({
            events: feedURL,
            header: {
                left: 'prev',
                center: 'title',
                right: 'next'
            },
            lang: lang,
            buttonIcons: {
                prev: ' fa fa-play fa-flip-horizontal',
                next: ' fa fa-play',
                prevYear: 'left-double-arrow',
                nextYear: 'right-double-arrow'
            },
            editable: false,
            // *** use long day names by using 'dddd' ***
            columnFormat: {
                month: 'dddd',    // Monday, Wednesday, etc
                week: 'dddd, MMM dS', // Monday 9/7
                day: 'dddd, MMM dS'  // Monday 9/7
            },
            timeFormat: ' '
        });
    }

    // on DOM ready render calendar
    $(function(){
        renderCalendar(conf.lang, conf.feedURL);
    });

})(window.jQuery, window.calendarConf);
