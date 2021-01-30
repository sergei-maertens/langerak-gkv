import { Calendar } from '@fullcalendar/core';
import nlLocale from '@fullcalendar/core/locales/nl';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';


const CALENDAR_CLASS = 'activities-calendar';


const init = () => {
    const nodes = document.querySelectorAll(`.${CALENDAR_CLASS}`);
    Array.from(nodes).forEach(node => {
        const { feed } = node.dataset;
        const calendar = new Calendar(node, {
            plugins: [ dayGridPlugin, timeGridPlugin ],
            events: feed,
            locale: nlLocale,
            header: {
                left: 'prev',
                center: 'title',
                right: 'next',
            },
            editable: false,
            columnHeaderFormat: {
                weekday: 'long',
            },
        });
        calendar.render();
    });
};


init();
