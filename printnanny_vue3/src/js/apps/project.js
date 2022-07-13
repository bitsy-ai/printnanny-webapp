/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Project
 */

import 'simplemde/dist/simplemde.min.css';
import 'frappe-gantt/dist/frappe-gantt.css';
import Chart from 'chart.js';
import Gantt from 'frappe-gantt';
import FileUpload from '../components/file-upload';

import Choices from 'choices.js';
import 'choices.js/src/styles/choices.scss';

import { Datepicker, } from 'vanillajs-datepicker';
import '../../../node_modules/vanillajs-datepicker/dist/css/datepicker-bs4.css';
import '../../../node_modules/vanillajs-datepicker/dist/css/datepicker.css';


class Project {

  constructor() {

  }

  initGantt(){
    if(document.getElementById('tasks-gantt')) {
      const tasks = [{
        id: '1',
        name: 'Draft the new contract document for sales team',
        start: '2019-07-16',
        end: '2019-07-20',
        progress: 55,
      },
        {
          id: '2',
          name: 'Find out the old contract documents',
          start: '2019-07-19',
          end: '2019-07-21',
          progress: 85,
          dependencies: '1'
        },
        {
          id: '3',
          name: 'Organize meeting with sales associates to understand need in detail',
          start: '2019-07-21',
          end: '2019-07-22',
          progress: 80,
          dependencies: '2'
        },
        {
          id: '4',
          name: 'iOS App home page',
          start: '2019-07-15',
          end: '2019-07-17',
          progress: 80
        },
        {
          id: '5',
          name: 'Write a release note',
          start: '2019-07-18',
          end: '2019-07-22',
          progress: 65,
          dependencies: '4'
        },
        {
          id: '6',
          name: 'Setup new sales project',
          start: '2019-07-20',
          end: '2019-07-31',
          progress: 15,
        },
        {
          id: '7',
          name: 'Invite user to a project',
          start: '2019-07-25',
          end: '2019-07-26',
          progress: 99,
          dependencies: '6'
        },
        {
          id: '8',
          name: 'Coordinate with business development',
          start: '2019-07-28',
          end: '2019-07-30',
          progress: 35,
          dependencies: '7'
        },
        {
          id: '9',
          name: 'Kanban board design',
          start: '2019-08-01',
          end: '2019-08-03',
          progress: 25,
          dependencies: '8'
        },
        {
          id: '10',
          name: 'Enable analytics tracking',
          start: '2019-08-05',
          end: '2019-08-07',
          progress: 60,
          dependencies: '9'
        }
      ];
      const gantt = new Gantt('#tasks-gantt', tasks, {
        view_modes: ['Quarter Day', 'Half Day', 'Day', 'Week', 'Month'],
        bar_height: 20,
        padding: 18,
        view_mode: 'Week',
        custom_popup_html: function (task) {

          const progressCls = task.progress >= 60 ? 'bg-success' : (task.progress >= 30 && task.progress < 60 ? 'bg-primary' : 'bg-warning');
          return `<div class="popover fade show bs-popover-right gantt-task-details" role="tooltip">
          <div class="arrow"></div><div class="popover-body">
          <h5>${task.name} </h5><p class="mb-2">Expected to finish by ${task.end}</p>
          <div class="progress mb-2" style="height: 10px;">
          <div class="progress-bar ' + progressCls + '" role="progressbar" style="width: ${task.progress}%;" aria-valuenow="${task.progress}" aria-valuemin="0" aria-valuemax="100">${task.progress}%</div>
          </div></div></div>`;
        }
      });

      // handling the mode changes

      document.querySelectorAll('#modes-filter input')
        .forEach(function (element) {
          element.addEventListener('change', function (event) {
            gantt.change_view_mode(element.value);
          })
        })

      const modesFilterBtn = document.getElementById('modes-filter')
        .querySelectorAll('.btn');
      modesFilterBtn.forEach(function (element) {
        element.addEventListener('click', function () {
          modesFilterBtn.forEach(function (element) {
            element.classList.remove('active');
          });
          element.classList.add('active');
        });
      });
    }

  }


  respChart(selector, type, data, options) {

    //default config
    Chart.defaults.global.defaultFontColor = "#8391a2";
    Chart.defaults.scale.gridLines.color = "#8391a2";

    // get selector by context

    const ctx = selector
      .getContext('2d');
    // pointing parent container to make chart js inherit its width
    const container = selector.parentNode;

    // this function produce the responsive Chart JS
    function generateChart() {
      // make chart width fit with its container
      const ww = selector.width = container.width;
      let chart;
      switch (type) {
        case 'Line':
          chart = new Chart(ctx, { type: 'line', data: data, options: options });
          break;
        case 'Bar':
          chart = new Chart(ctx, { type: 'bar', data: data, options: options });
          break;
        case 'Doughnut':
          chart = new Chart(ctx, { type: 'doughnut', data: data, options: options });
          break;
      }
      return chart;
    }

    return generateChart();
  }

  initCharts() {
    const charts = [];
    if (document.querySelectorAll('#line-chart-example').length > 0) {
      const lineChart = {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
          label: 'Completed Tasks',
          backgroundColor: 'rgba(10, 207, 151, 0.3)',
          borderColor: '#0acf97',
          data: [32, 42, 42, 62, 52, 75, 62]
        }, {
          label: 'Plan Tasks',
          fill: true,
          backgroundColor: 'transparent',
          borderColor: '#727cf5',
          borderDash: [5, 5],
          data: [42, 58, 66, 93, 82, 105, 92]
        }]
      };

      const lineOpts = {
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        tooltips: {
          intersect: false
        },
        hover: {
          intersect: true
        },
        plugins: {
          filler: {
            propagate: false
          }
        },
        scales: {
          xAxes: [{
            reverse: true,
            gridLines: {
              color: 'rgba(0,0,0,0.05)'
            }
          }],
          yAxes: [{
            ticks: {
              stepSize: 20
            },
            display: true,
            borderDash: [5, 5],
            gridLines: {
              color: 'rgba(0,0,0,0)',
              fontColor: '#fff'
            }
          }]
        }
      };
      charts.push(this.respChart(document.getElementById("line-chart-example"), 'Line', lineChart, lineOpts));
    }


    return charts;
  }

  init () {
    const self = this;
    // font
    Chart.defaults.global.defaultFontFamily = '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif';

    // init charts
    self.charts = this.initCharts();

    // enable resizing matter
    window.addEventListener('resize',function(e){
      self.charts.forEach(function (chart,index){
        try{
          chart.destroy();
        }catch (err){

        }
      });
      self.charts = self.initCharts();
    });

    this.initGantt();

    new FileUpload().init();

    const datePicker1 = document.querySelector('#datepicker1 input');
    const datePicker2 = document.querySelector('#datepicker2 input');
    if(datePicker1) {
      new Datepicker(datePicker1, {
        orientation: "bottom"
      });
    }

    if(datePicker2) {
      new Datepicker(datePicker2, {
        orientation: "bottom"
      });
    }


    document.querySelectorAll('[data-toggle="select2"]').forEach(function(element) {
      new Choices(element,{
        itemSelectText:'',
      });
    });

  }



}

// init the dashboard
new Project().init();
