/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Calendar
 */

import {Calendar} from '@fullcalendar/core';
import {Draggable} from '@fullcalendar/interaction';
import interactionPlugin from '@fullcalendar/interaction';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';
import dayGridPlugin from '@fullcalendar/daygrid';

import bootstrapPlugin from '@fullcalendar/bootstrap';
import '@fullcalendar/bootstrap/main.css'
import { Modal } from 'bootstrap';


// EcommerceDashboard
class CalendarApp {
  constructor() {



    this.body = document.body;
    this.modal = new Modal(document.getElementById('event-modal'), { backdrop: 'static' });
    this.calendar = document.getElementById('calendar');
    this.formEvent = document.getElementById('forms-event');
    this.btnNewEvent = document.getElementById('btn-new-event');
    this.btnDeleteEvent = document.getElementById('btn-delete-event');
    this.btnSaveEvent = document.getElementById('btn-save-event');
    this.modalTitle = document.getElementById('modal-title');
    this.calendarObj = null;
    this.selectedEvent = null;
    this.newEventData = null;
  }

  onEventClick(info){
    this.formEvent?.reset();
    this.formEvent.classList.remove('was-validated');

    this.newEventData = null;
    this.btnDeleteEvent.style.display = "block";
    this.modalTitle.text = ('Edit Event');
    this.modal.show();
    this.selectedEvent = info.event;
    document.getElementById('event-title').value = this.selectedEvent.title;
    document.getElementById('event-category').value = (this.selectedEvent.classNames[0]);
  }

  onSelect(info) {
    this.formEvent?.reset();
    this.formEvent?.classList.remove('was-validated');

    this.selectedEvent = null;
    this.newEventData = info;
    this.btnDeleteEvent.style.display = "none";
    this.modalTitle.text = ('Add New Event');
    this.modal.show();
    this.calendarObj.unselect();
  }

  init() {
    /*  Initialize the calendar  */
    const today = new Date();
    const self = this;

    //const Draggable = FullCalendar.Draggable;
    const externalEventContainerEl = document.getElementById('external-events');

    new Draggable(externalEventContainerEl, {
      itemSelector: '.external-event',
      eventData: function (eventEl) {
        return {
          title: eventEl.innerText,
          classNames: eventEl.getAttribute('data-class')
        };
      }
    });

    const defaultEvents = [{
      title: 'Meeting with Mr. Shreyu',
      start: new Date(Date.now() + 158000000),
      end: new Date(Date.now() + 338000000),
      className: 'bg-warning'
    },
      {
        title: 'Interview - Backend Engineer',
        start: today,
        end: today,
        className: 'bg-success'
      },
      {
        title: 'Phone Screen - Frontend Engineer',
        start: new Date(Date.now() + 168000000),
        className: 'bg-info'
      },
      {
        title: 'Buy Design Assets',
        start: new Date(Date.now() + 338000000),
        end: new Date(Date.now() + 338000000 * 1.2),
        className: 'bg-primary',
      }];

    // cal - init
    self.calendarObj = new Calendar(self.calendar, {

      plugins: [ dayGridPlugin, bootstrapPlugin, interactionPlugin, listPlugin, timeGridPlugin],
      slotDuration: '00:15:00', /* If we want to split day time each 15minutes */
      slotMinTime: '08:00:00',
      slotMaxTime: '19:00:00',
      themeSystem: 'bootstrap',
      bootstrapFontAwesome: false,
      buttonText: {
        today: 'Today',
        month: 'Month',
        week: 'Week',
        day: 'Day',
        list: 'List',
        prev: 'Prev',
        next: 'Next'
      },
      initialView: 'dayGridMonth',
      handleWindowResize: true,
      height: window.innerHeight - 200,
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
      },
      initialEvents: defaultEvents,
      editable: true,
      droppable: true, // this allows things to be dropped onto the calendar !!!
      // dayMaxEventRows: false, // allow "more" link when too many events
      selectable: true,
      dateClick: function (info) {
        self.onSelect(info);
      },
      eventClick: function (info) {
        self.onEventClick(info);
      }
    });

    self.calendarObj.render();

    // on new event button click
    self.btnNewEvent.addEventListener('click', function (e) {
      self.onSelect({
        date: new Date(),
        allDay: true
      });
    });

    // save event
    self.formEvent?.addEventListener('submit', function (e) {
      e.preventDefault();
      const form = self.formEvent;

      // validation
      if (form.checkValidity()) {
        if (self.selectedEvent) {
          self.selectedEvent.setProp('title', document.getElementById('event-title')
            .value);
          self.selectedEvent.setProp('classNames',document.getElementById('event-category')
            .value)

        } else {
          const eventData = {
            title: document.getElementById('event-title')
              .value,
            start: self.newEventData.date,
            allDay: self.newEventData.allDay,
            className: document.getElementById('event-category')
              .value
          };
          self.calendarObj.addEvent(eventData);
        }
        self.modal.hide();
      } else {
        e.stopPropagation();
        form.classList.add('was-validated');
      }
    });

    // delete event
    self.btnDeleteEvent.addEventListener('click', function (e) {
      if (self.selectedEvent) {
        self.selectedEvent.remove();
        self.selectedEvent = null;
        self.modal.hide();
      }
    });
  }

}

// init the dashboard
new CalendarApp().init();
