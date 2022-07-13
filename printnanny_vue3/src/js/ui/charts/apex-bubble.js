/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

import ApexCharts from  'apexcharts';

class ApexBubble {

  constructor() {


  }

  generateData(baseval, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;
      var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
      var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

      series.push([x, y, z]);
      baseval += 86400000;
      i++;
    }
    return series;
  }

  generateData1(baseval1, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      //var x =Math.floor(Math.random() * (750 - 1 + 1)) + 1;;
      var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
      var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

      series.push([baseval1, y, z]);
      baseval1 += 86400000;
      i++;
    }
    return series;
  }



  init() {

    this.initCharts();

  }

  initCharts() {

    var colors = ["#727cf5", "#ffbc00", "#fa5c7c"];
    var dataColors =  document.getElementById('simple-bubble')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 380,
        type: 'bubble',
        toolbar: {
          show: false
        }
      },
      dataLabels: {
        enabled: false
      },
      series: [{
        name: 'Bubble 1',
        data: this.generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
          min: 10,
          max: 60
        })
      },
        {
          name: 'Bubble 2',
          data: this.generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
            min: 10,
            max: 60
          })
        },
        {
          name: 'Bubble 3',
          data: this.generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
            min: 10,
            max: 60
          })
        }
      ],
      fill: {
        opacity: 0.8,
        gradient: {
          enabled: false
        }
      },
      colors: colors,
      xaxis: {
        tickAmount: 12,
        type: 'category',
      },
      yaxis: {
        max: 70
      },
      grid: {
        borderColor: '#f1f3fa',
        padding: {
          bottom: 5
        }
      },
      legend: {
        offsetY: 7,
      }
    }

    var chart = new ApexCharts(
      document.querySelector("#simple-bubble"),
      options
    );

    chart.render();


    var colors = ["#727cf5", "#0acf97", "#fa5c7c", "#39afd1"];
    var dataColors =  document.getElementById('second-bubble')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options2 = {
      chart: {
        height: 380,
        type: 'bubble',
        toolbar: {
          show: false
        }
      },
      dataLabels: {
        enabled: false
      },
      series: [{
        name: 'Product 1',
        data: this.generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
          min: 10,
          max: 60
        })
      },
        {
          name: 'Product 2',
          data: this.generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
            min: 10,
            max: 60
          })
        },
        {
          name: 'Product 3',
          data: this.generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
            min: 10,
            max: 60
          })
        },
        {
          name: 'Product 4',
          data: this.generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
            min: 10,
            max: 60
          })
        }
      ],
      fill: {
        type: 'gradient',
      },
      colors: colors,
      xaxis: {
        tickAmount: 12,
        type: 'datetime',

        labels: {
          rotate: 0,
        }
      },
      yaxis: {
        max: 70
      },
      legend: {
        offsetY: 7,
      },
      grid: {
        borderColor: '#f1f3fa',
        padding: {
          bottom: 5
        }
      }
    }

    var chart = new ApexCharts(
      document.querySelector("#second-bubble"),
      options2
    );

    chart.render();

  }
}

// init the dashboard
new ApexBubble().init();
