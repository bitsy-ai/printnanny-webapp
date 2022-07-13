/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: EcommerceDashboard
 */

import ApexCharts from 'apexcharts/dist/apexcharts';

import JsVectorMap from 'jsvectormap/src/js/JsVectorMap';
import 'jsvectormap/dist/maps/world';

import { Datepicker, } from 'vanillajs-datepicker';
import '../../../node_modules/vanillajs-datepicker/dist/css/datepicker-bs4.css';
import '../../../node_modules/vanillajs-datepicker/dist/css/datepicker.css';

// EcommerceDashboard
class EcommerceDashboard {
  // init charts
  this;

  constructor() {

  }

  initMaps() {

    new JsVectorMap({
      selector: '#world-map-markers',
      map: 'world',
      backgroundColor: 'transparent',
      zoomOnScroll: false,

      normalizeFunction: 'polynomial',
      hoverOpacity: 0.7,
      hoverColor: false,
      regionStyle: {
        initial: {
          fill: '#e3eaef'
        }
      },
      markerStyle: {
        initial: {
          r: 9,
          'fill': '#727cf5',
          'fill-opacity': 0.9,
          'stroke': '#fff',
          'stroke-width': 7,
          'stroke-opacity': 0.4
        },

        hover: {
          'stroke': '#fff',
          'fill-opacity': 1,
          'stroke-width': 1.5
        }
      },
      markers: [{
        coords: [40.71, -74.00],
        name: 'New York'
      }, {
        coords: [37.77, -122.41],
        name: 'San Francisco'
      }, {
        coords: [-33.86, 151.20],
        name: 'Sydney'
      }, {
        coords: [1.3, 103.8],
        name: 'Singapore'
      }],
    });
  }

  initCharts() {

    window.Apex = {
      chart: {
        parentHeightOffset: 0,
        toolbar: {
          show: false
        }
      },
      grid: {
        padding: {
          left: 0,
          right: 0
        }
      },
      colors: ['#727cf5', '#0acf97', '#fa5c7c', '#ffbc00'],
    };

    var colors = ['#727cf5', '#0acf97', '#fa5c7c', '#ffbc00'];
    var dataColors = document.getElementById('revenue-chart')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(',');
    }

    var options = {
      chart: {
        height: 364,
        type: 'line',
        dropShadow: {
          enabled: true,
          opacity: 0.2,
          blur: 7,
          left: -7,
          top: 7
        }
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth',
        width: 4
      },
      series: [{
        name: 'Current Week',
        data: [10, 20, 15, 25, 20, 30, 20]
      }, {
        name: 'Previous Week',
        data: [0, 15, 10, 30, 15, 35, 25]
      }],
      colors: colors,
      zoom: {
        enabled: false
      },
      legend: {
        show: false
      },
      xaxis: {
        type: 'string',
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        tooltip: {
          enabled: false
        },
        axisBorder: {
          show: false
        }
      },
      yaxis: {
        labels: {
          formatter: function (val) {
            return val + 'k';
          },
          offsetX: -15
        }
      }
    };

    var chart = new ApexCharts(
      document.querySelector('#revenue-chart'),
      options
    );

    chart.render();

    // --------------------------------------------------
    var colors = ['#727cf5', '#e3eaef'];
    var dataColors = document.getElementById('high-performing-product')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(',');
    }

    var options = {
      chart: {
        height: 257,
        type: 'bar',
        stacked: true
      },
      plotOptions: {
        bar: {
          horizontal: false,
          columnWidth: '20%'
        },
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        show: true,
        width: 2,
        colors: ['transparent']
      },
      series: [{
        name: 'Actual',
        data: [65, 59, 80, 81, 56, 89, 40, 32, 65, 59, 80, 81]
      }, {
        name: 'Projection',
        data: [89, 40, 32, 65, 59, 80, 81, 56, 89, 40, 65, 59]
      }],
      zoom: {
        enabled: false
      },
      legend: {
        show: false
      },
      colors: colors,
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        axisBorder: {
          show: false
        },
      },
      yaxis: {
        labels: {
          formatter: function (val) {
            return val + 'k';
          },
          offsetX: -15
        }
      },
      fill: {
        opacity: 1
      },
      tooltip: {
        y: {
          formatter: function (val) {
            return '$' + val + 'k';
          }
        },
      },
    };

    var chart = new ApexCharts(
      document.querySelector('#high-performing-product'),
      options
    );

    chart.render();

    // --------------------------------------------------
    var colors = ['#727cf5', '#0acf97', '#fa5c7c', '#ffbc00'];
    var dataColors = document.getElementById('average-sales')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(',');
    }
    var options = {
      chart: {
        height: 202,
        type: 'donut',
      },
      legend: {
        show: false
      },
      stroke: {
        colors: ['transparent']
      },
      series: [44, 55, 41, 17],
      labels: ['Direct', 'Affilliate', 'Sponsored', 'E-mail'],
      colors: colors,
      responsive: [{
        breakpoint: 480,
        options: {
          chart: {
            width: 200
          },
          legend: {
            position: 'bottom'
          }
        }
      }]
    };

    var chart = new ApexCharts(
      document.querySelector('#average-sales'),
      options
    );

    chart.render();
  }

  init() {

    if (document.getElementById('dash-daterange')) {
      new Datepicker(document.getElementById('dash-daterange')).setDate(new Date());
    }

    this.initCharts();
    this.initMaps();
  }
}

// init the dashboard
new EcommerceDashboard().init();

/**


 /**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: EcommerceDashboard




 class {

   constructor() {
   }

   init(){

   }

}

 new ().init();

 export default ;

 **/
