/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: EcommerceDashboard
 */

 import ApexCharts from 'apexcharts/dist/apexcharts';



 import Chart from 'chart.js/dist/Chart';
 
 import { Datepicker, } from 'vanillajs-datepicker';
 import '../../../node_modules/vanillajs-datepicker/dist/css/datepicker-bs4.css';
 import '../../../node_modules/vanillajs-datepicker/dist/css/datepicker.css';
 
 
 // EcommerceDashboard
 class ProjectsDashboard {
   constructor() {
 
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
 
   initCharts(){
 
     const charts = [];
 
     if (document.querySelectorAll('#task-area-chart').length > 0) {
       const dataBgColor = document.getElementById('task-area-chart')
         .getAttribute('data-bgColor');
       const dataBorderColor = document.getElementById('task-area-chart')
         .getAttribute('data-borderColor');
       const bgColor = dataBgColor ? dataBgColor : '#727cf5';
       const borderColor = dataBorderColor ? dataBorderColor : '#727cf5';
 
       const lineChart = {
         labels: [
           'Sprint 1',
           'Sprint 2',
           'Sprint 3',
           'Sprint 4',
           'Sprint 5',
           'Sprint 6',
           'Sprint 7',
           'Sprint 8',
           'Sprint 9',
           'Sprint 10',
           'Sprint 11',
           'Sprint 12',
           'Sprint 13',
           'Sprint 14',
           'Sprint 15',
           'Sprint 16',
           'Sprint 17',
           'Sprint 18',
           'Sprint 19',
           'Sprint 20',
           'Sprint 21',
           'Sprint 22',
           'Sprint 23',
           'Sprint 24'
         ],
         datasets: [
           {
             label: 'This year',
             backgroundColor: bgColor,
             borderColor: borderColor,
             data: [
               16,
               44,
               32,
               48,
               72,
               60,
               84,
               64,
               78,
               50,
               68,
               34,
               26,
               44,
               32,
               48,
               72,
               60,
               74,
               52,
               62,
               50,
               32,
               22
             ]
           }
         ]
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
             barPercentage: 0.7,
             categoryPercentage: 0.5,
             reverse: true,
             gridLines: {
               color: 'rgba(0,0,0,0.05)'
             }
           }],
           yAxes: [{
             ticks: {
               stepSize: 10,
               display: false
             },
             min: 10,
             max: 100,
             display: true,
             borderDash: [5, 5],
             gridLines: {
               color: 'rgba(0,0,0,0)',
               fontColor: '#fff',
             }
           }]
         }
       };
       charts.push(this.respChart(document.getElementById("task-area-chart"), 'Bar', lineChart, lineOpts));
     }
 
     if (document.querySelectorAll('#project-status-chart').length > 0) {
       const dataColors = document.getElementById('project-status-chart')
         .getAttribute('data-colors');
       const colors = dataColors ? dataColors.split(',') : ['#0acf97', '#727cf5', '#fa5c7c'];
       //donut chart
       const donutChart = {
         labels: [
           'Completed',
           'In-progress',
           'Behind'
         ],
         datasets: [
           {
             data: [64, 26, 10],
             backgroundColor: colors,
             borderColor: 'transparent',
             borderWidth: '3',
           }]
       };
       const donutOpts = {
         maintainAspectRatio: false,
         cutoutPercentage: 80,
         legend: {
           display: false
         }
       };
       charts.push(this.respChart(document.getElementById("project-status-chart"), 'Doughnut', donutChart, donutOpts));
     }
     return charts;
   }
 
 
   init() {
 
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
     new Datepicker(document.getElementById('calendar-picker')).setDate(new Date());
   }
 }
 
 // init the dashboard
 new ProjectsDashboard().init();
 