(function($, conf, undefined) {

    function renderCalendar(lang, feedURL) {
        $('#calendar').fullCalendar({
            events: feedURL,
            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay'
            },
            lang: lang,
            buttonIcons: false,
            editable: true
        });
    }

    // on DOM ready render calendar
    $(function(){
        renderCalendar(conf.lang, conf.feedURL);
    });

})(window.jQuery, window.calendarConf);
