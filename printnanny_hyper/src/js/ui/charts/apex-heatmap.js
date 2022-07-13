/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

import ApexCharts from  'apexcharts';

class ApexHeatmap {

  constructor() {


  }

  generateData(count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = (i + 1).toString();
      var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

      series.push({
        x: x,
        y: y
      });
      i++;
    }
    return series;
  }


  init() {

    this.initCharts();

  }

  initCharts() {


    var colors = ["#727cf5"];
    var dataColors = document.getElementById('basic-heatmap')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 380,
        type: 'heatmap',
      },
      dataLabels: {
        enabled: false
      },
      colors: colors,
      series: [{
        name: 'Metric 1',
        data: this.generateData(20, {
          min: 0,
          max: 90
        })
      },
        {
          name: 'Metric 2',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 3',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 4',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 5',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric  6',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 7',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 8',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 9',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        }
      ],
      xaxis: {
        type: 'category',
      },

    }

    var chart = new ApexCharts(
      document.querySelector("#basic-heatmap"),
      options
    );

    chart.render();



    var colors = ["#F3B415", "#F27036", "#663F59", "#6A6E94", "#4E88B4", "#00A7C6", "#18D8D8", '#A9D794','#46AF78'];
    var dataColors =  document.getElementById('multiple-series-heatmap')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 380,
        type: 'heatmap',
      },
      dataLabels: {
        enabled: false
      },
      colors: colors,
      series: [{
        name: 'Metric 1',
        data: this.generateData(20, {
          min: 0,
          max: 90
        })
      },
        {
          name: 'Metric 2',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 3',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 4',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 5',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 6',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 7',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 8',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric 9',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        }
      ],
      xaxis: {
        type: 'category',
      },
    }

    var chart = new ApexCharts(
      document.querySelector("#multiple-series-heatmap"),
      options
    );

    chart.render();



    var colors = ["#fa6767","#f9bc0d","#44badc","#42d29d"];
    var dataColors =  document.getElementById('color-range-heatmap')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 380,
        type: 'heatmap',
      },
      plotOptions: {
        heatmap: {
          shadeIntensity: 0.5,

          colorScale: {
            ranges: [{
              from: -30,
              to: 5,
              name: 'Low',
              color: colors[0]
            },
              {
                from: 6,
                to: 20,
                name: 'Medium',
                color: colors[1]
              },
              {
                from: 21,
                to: 45,
                name: 'High',
                color: colors[2]
              },
              {
                from: 46,
                to: 55,
                name: 'Extreme',
                color: colors[3]
              }
            ]
          }
        }
      },
      dataLabels: {
        enabled: false
      },
      series: [{
        name: 'Jan',
        data: this.generateData(20, {
          min: -30,
          max: 55
        })
      },
        {
          name: 'Feb',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        },
        {
          name: 'Mar',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        },
        {
          name: 'Apr',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        },
        {
          name: 'May',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        },
        {
          name: 'Jun',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        },
        {
          name: 'Jul',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        },
        {
          name: 'Aug',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        },
        {
          name: 'Sep',
          data: this.generateData(20, {
            min: -30,
            max: 55
          })
        }
      ],

    }

    var chart = new ApexCharts(
      document.querySelector("#color-range-heatmap"),
      options
    );

    chart.render();


    var colors = ["#39afd1","#0acf97"];
    var dataColors =  document.getElementById('rounded-heatmap')
      .getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    var options = {
      chart: {
        height: 380,
        type: 'heatmap',
      },
      stroke: {
        width: 0
      },
      plotOptions: {
        heatmap: {
          radius: 30,
          enableShades: false,
          colorScale: {
            ranges: [{
              from: 0,
              to: 50,
              color: colors[0]
            },
              {
                from: 51,
                to: 100,
                color: colors[1]
              },
            ],
          },

        }
      },
      colors: colors,
      dataLabels: {
        enabled: true,
        style: {
          colors: ['#fff']
        }
      },
      series: [{
        name: 'Metric1',
        data: this.generateData(20, {
          min: 0,
          max: 90
        })
      },
        {
          name: 'Metric2',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric3',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric4',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric5',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric6',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric7',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric8',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        },
        {
          name: 'Metric8',
          data: this.generateData(20, {
            min: 0,
            max: 90
          })
        }
      ],

      xaxis: {
        type: 'category',
      },
      grid: {
        borderColor: '#f1f3fa'
      }
    }

    var chart = new ApexCharts(
      document.querySelector("#rounded-heatmap"),
      options
    );

    chart.render();


  }
}

// init the dashboard
new ApexHeatmap().init();
