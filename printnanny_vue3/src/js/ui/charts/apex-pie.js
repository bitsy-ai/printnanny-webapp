/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

import ApexCharts from  'apexcharts';

class ApexPie {

  constructor() {
    this.chart;
    this.options;

  }


  appendData() {
    var arr = this.chart.w.globals.series.map(function () {
      return Math.floor(Math.random() * (100 - 1 + 1)) + 1;
    });
    arr.push(Math.floor(Math.random() * (100 - 1 + 1)) + 1);
    return arr;
  }

  removeData() {
    var arr = this.chart.w.globals.series.map(function () {
      return Math.floor(Math.random() * (100 - 1 + 1)) + 1;
    });
    arr.pop();
    return arr;
  }

  randomize() {
    return this.chart.w.globals.series.map(function () {
      return Math.floor(Math.random() * (100 - 1 + 1)) + 1;
    });
  }

  reset() {
    return this.options.series;
  }




  init() {

    this.initCharts();
    const self = this;

    document.querySelector("#randomize").addEventListener("click", function () {
      self.chart.updateSeries(self.randomize());
    });

    document.querySelector("#add").addEventListener("click", function () {
      self.chart.updateSeries(self.appendData());
    });

    document.querySelector("#remove").addEventListener("click", function () {
      self.chart.updateSeries(self.removeData());
    });

    document.querySelector("#reset").addEventListener("click", function () {
      self.chart.updateSeries(self.reset());
    });

  }

  initCharts() {

    var colors = ["#727cf5", "#6c757d","#0acf97", "#fa5c7c","#e3eaef"];
    var dataColors = document.getElementById('simple-pie')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 320,
        type: 'pie',
      },
      series: [44, 55, 41, 17, 15],
      labels: ["Series 1", "Series 2", "Series 3", "Series 4", "Series 5"],
      colors: colors,
      legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        verticalAlign: 'middle',
        floating: false,
        fontSize: '14px',
        offsetX: 0,
        offsetY: 7
      },
      responsive: [{
        breakpoint: 600,
        options: {
          chart: {
            height: 240
          },
          legend: {
            show: false
          },
        }
      }]

    }

    var chart = new ApexCharts(
      document.querySelector("#simple-pie"),
      options
    );

    chart.render();


//
// SIMPLE DONUT CHART
//
    var colors = ["#39afd1", "#ffbc00", "#313a46", "#fa5c7c", "#0acf97"];
    var dataColors = document.getElementById('simple-donut')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 320,
        type: 'donut',
      },
      series: [44, 55, 41, 17, 15],
      legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        verticalAlign: 'middle',
        floating: false,
        fontSize: '14px',
        offsetX: 0,
        offsetY: 7
      },
      labels: ["Series 1", "Series 2", "Series 3", "Series 4", "Series 5"],
      colors: colors,
      responsive: [{
        breakpoint: 600,
        options: {
          chart: {
            height: 240
          },
          legend: {
            show: false
          },
        }
      }]
    }

    var chart = new ApexCharts(
      document.querySelector("#simple-donut"),
      options
    );

    chart.render();


//
// MONOCHROME PIE CHART
//
    var options = {
      chart: {
        height: 320,
        type: 'pie',
      },
      series: [25, 15, 44, 55, 41, 17],
      labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        verticalAlign: 'middle',
        floating: false,
        fontSize: '14px',
        offsetX: 0,
        offsetY: 7
      },
      theme: {
        monochrome: {
          enabled: true
        }
      },
      responsive: [{
        breakpoint: 600,
        options: {
          chart: {
            height: 240
          },
          legend: {
            show: false
          },
        }
      }]
    }

    var chart = new ApexCharts(
      document.querySelector("#monochrome-pie"),
      options
    );

    chart.render();

//
// GRADIENT DONUT CHART
//
    var colors = ["#727cf5", "#6c757d","#0acf97", "#fa5c7c","#e3eaef"];
    var dataColors = document.getElementById('gradient-donut')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 320,
        type: 'donut',
      },
      series: [44, 55, 41, 17, 15],
      legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        verticalAlign: 'middle',
        floating: false,
        fontSize: '14px',
        offsetX: 0,
        offsetY: 7
      },
      labels: ["Series 1", "Series 2", "Series 3", "Series 4", "Series 5"],
      colors: colors,
      responsive: [{
        breakpoint: 600,
        options: {
          chart: {
            height: 240
          },
          legend: {
            show: false
          },
        }
      }],
      fill: {
        type: 'gradient'
      }
    }

    var chart = new ApexCharts(
      document.querySelector("#gradient-donut"),
      options
    );

    chart.render();


//
// PATTERNED DONUT CHART
//
    var colors = ["#39afd1", "#ffbc00", "#313a46", "#fa5c7c", "#0acf97"];
    var dataColors = document.getElementById('patterned-donut')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 320,
        type: 'donut',
        dropShadow: {
          enabled: true,
          color: '#111',
          top: -1,
          left: 3,
          blur: 3,
          opacity: 0.2
        }
      },
      stroke: {
        show: true,
        width: 2,
      },
      series: [44, 55, 41, 17, 15],
      colors: colors,
      labels: ["Comedy", "Action", "SciFi", "Drama", "Horror"],
      dataLabels: {
        dropShadow: {
          blur: 3,
          opacity: 0.8
        }
      },
      fill: {
        type: 'pattern',
        opacity: 1,
        pattern: {
          enabled: true,
          style: ['verticalLines', 'squares', 'horizontalLines', 'circles','slantedLines'],
        },
      },
      states: {
        hover: {
          enabled: false
        }
      },
      legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        verticalAlign: 'middle',
        floating: false,
        fontSize: '14px',
        offsetX: 0,
        offsetY: 7
      },
      responsive: [{
        breakpoint: 600,
        options: {
          chart: {
            height: 240
          },
          legend: {
            show: false
          },
        }
      }]
    }

    var chart = new ApexCharts(
      document.querySelector("#patterned-donut"),
      options
    );

    chart.render();


//
// PIE CHART WITH IMAGE FILL
//
    var colors = ["#39afd1", "#ffbc00", "#727cf5", "#0acf97"];
    var dataColors = document.getElementById('image-pie')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 320,
        type: 'pie',
      },
      labels: ["Series 1", "Series 2", "Series 3", "Series 4"],
      colors: colors,
      series: [44, 33, 54, 45],
      fill: {
        type: 'image',
        opacity: 0.85,
        image: {
          src: ['/images/small/small-1.jpg', '/images/small/small-2.jpg', '/images/small/small-3.jpg', '/images/small/small-4.jpg'],
          width: 25,
          imagedHeight: 25
        },
      },
      stroke: {
        width: 4
      },
      dataLabels: {
        enabled: false
      },
      legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        verticalAlign: 'middle',
        floating: false,
        fontSize: '14px',
        offsetX: 0,
        offsetY: 7
      },
      responsive: [{
        breakpoint: 600,
        options: {
          chart: {
            height: 240
          },
          legend: {
            show: false
          },
        }
      }]
    }

    var chart = new ApexCharts(
      document.querySelector("#image-pie"),
      options
    );

    chart.render();


//
// DONUT UPDATE
//
    var colors = ["#727cf5", "#6c757d","#0acf97", "#fa5c7c"];
    var dataColors = document.getElementById('update-donut')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    this.options = {
      chart: {
        height: 320,
        type: 'donut',
      },
      dataLabels: {
        enabled: false
      },
      series: [44, 55, 13, 33],
      colors: colors,
      legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        verticalAlign: 'middle',
        floating: false,
        fontSize: '14px',
        offsetX: 0,
        offsetY: 7
      },
      responsive: [{
        breakpoint: 600,
        options: {
          chart: {
            height: 240
          },
          legend: {
            show: false
          },
        }
      }]
    }

    this.chart = new ApexCharts(
      document.querySelector("#update-donut"),
      this.options
    );

    this.chart.render();
  }
}

// init the dashboard
new ApexPie().init();
