

import Choices from 'choices.js';

import Inputmask from 'inputmask/lib/inputmask';
import 'choices.js/src/styles/choices.scss';
import Touchspin from '../../components/touchspin';

import { Datepicker, DateRangePicker } from 'vanillajs-datepicker';
import '../../../../node_modules/vanillajs-datepicker/dist/css/datepicker-bs4.css';
import '../../../../node_modules/vanillajs-datepicker/dist/css/datepicker.css';




class AdvancedForm {

  constructor() {
    this.body = document.getElementsByTagName("body")[0];
    this.window = window;
  }

  initSelect2 = () => {
    document.querySelectorAll('[data-toggle="select2"]').forEach(function (element) {

      if (element.multiple) {
        new Choices(element, {
          itemSelectText: '',
          placeholderValue: 'select',
          placeholder: true,
          removeItemButton: true,
          removeItems: true,
          choices: [
            { value: 'select', label: "Select", selected: true }
          ]
        }).setChoiceByValue('select');
      } else {
        new Choices(element, {
          itemSelectText: '',
          placeholderValue: 'select',
          placeholder: true,
          removeItemButton: false,
          removeItems: false,

        }).setChoiceByValue('select');
      }


      document.querySelectorAll('.choices__group .choices__heading').forEach(function (element) {
        element.innerHTML == "" ? element.parentElement.classList.add('d-none') : null;
      });



    });
  }

  initMask = () => {
    const self = this;
    document.querySelectorAll('[data-toggle="input-mask"]').forEach(e => {
      const maskFormat = e.getAttribute('data-mask-format').toString().replaceAll('0', '9');
      e.setAttribute("data-mask-format", maskFormat);
      const reverse = e.getAttribute('data-reverse');

      const im = new Inputmask(maskFormat);
      im.mask(e);
    });
  }



  initDatePicker() {

    new Datepicker(document.querySelector('#datepicker1 input'), {
      format: 'd-M-yyyy',
      orientation: "bottom"
    });

    const dateFormatElement = document.querySelector('#datepicker2 input');
    new Datepicker(dateFormatElement, {
      format: dateFormatElement.getAttribute("data-date-format") ?? 'd-M-yyyy',
      clearBtn: true,
      todayBtn: true,
      orientation: "bottom",
    });


    new Datepicker(document.querySelector('#datepicker3 input'), {
      autohide: true,
      format: dateFormatElement.getAttribute("data-date-format") ?? 'd-M-yyyy',
      orientation: "bottom"
    });

    new DateRangePicker(document.getElementById('datepicker4'), {
      orientation: "bottom",
      format: dateFormatElement.getAttribute("data-date-format") ?? 'd-M-yyyy',
    });


    new Datepicker(document.querySelector('[data-provide="datepicker-inline"]'), {
      orientation: "bottom"

    });


  }

  initTypehead() {
  }

  init = () => {
    this.initSelect2();
    this.initMask();
    this.initTypehead();
    this.initDatePicker();
    new Touchspin().init();

  }

}

new AdvancedForm().init();
