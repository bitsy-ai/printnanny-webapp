/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */


import  Chart  from 'chart.js';

class Chartjs {

  constructor() {


  }

  hexToRGB(hex, alpha) {
    var r = parseInt(hex.slice(1, 3), 16),
      g = parseInt(hex.slice(3, 5), 16),
      b = parseInt(hex.slice(5, 7), 16);

    if (alpha) {
      return "rgba(" + r + ", " + g + ", " + b + ", " + alpha + ")";
    } else {
      return "rgb(" + r + ", " + g + ", " + b + ")";
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
        case 'Doughnut':
          chart = new Chart(ctx, { type: 'doughnut', data: data, options: options });
          break;
        case 'Pie':
          chart = new Chart(ctx, { type: 'pie', data: data, options: options });
          break;
        case 'Bar':
          chart = new Chart(ctx, { type: 'bar', data: data, options: options });
          break;
        case 'Radar':
          chart = new Chart(ctx, { type: 'radar', data: data, options: options });
          break;
        case 'PolarArea':
          chart = new Chart(ctx, { data: data, type: 'polarArea', options: options });
          break;
      }
      return chart;
    }

    return generateChart();
  }

  initCharts() {
    var charts = [];
    var defaultColors = ["#727cf5", "#0acf97", "#fa5c7c", "#ffbc00"];

    if (document.querySelectorAll('#line-chart-example').length > 0) {
      var dataColors = document.getElementById('line-chart-example')
        .getAttribute('data-colors');
      var colors = dataColors? dataColors.split(",") : defaultColors.concat();

      var lineChart = {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [{
          label: "Current Week",
          backgroundColor: this.hexToRGB(colors[0], 0.3),
          borderColor: colors[0],
          data: [32, 42, 42, 62, 52, 75, 62]
        }, {
          label: "Previous Week",
          fill: true,
          backgroundColor: 'transparent',
          borderColor: colors[1],
          borderDash: [5, 5],
          data: [42, 58, 66, 93, 82, 105, 92]
        }]
      };

      var lineOpts = {
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
              color: "rgba(0,0,0,0.05)"
            }
          }],
          yAxes: [{
            ticks: {
              stepSize: 20
            },
            display: true,
            borderDash: [5, 5],
            gridLines: {
              color: "rgba(0,0,0,0)",
              fontColor: '#fff'
            }
          }]
        }
      };
      charts.push(this.respChart(document.getElementById("line-chart-example"), 'Line', lineChart, lineOpts));
    }

    //barchart
    if (document.querySelectorAll('#bar-chart-example').length > 0) {
      var dataColors = document.getElementById('bar-chart-example')
        .getAttribute('data-colors');
      var colors = dataColors? dataColors.split(",") : defaultColors.concat();

      // create gradient
      var ctx = document.getElementById('bar-chart-example').getContext("2d");
      var gradientStroke = ctx.createLinearGradient(0, 500, 0, 150);
      gradientStroke.addColorStop(0, colors[0]);
      gradientStroke.addColorStop(1, colors[1]);

      var barChart = {
        // labels: ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [
          {
            label: "Sales Analytics",
            backgroundColor: gradientStroke,
            borderColor: gradientStroke,
            hoverBackgroundColor: gradientStroke,
            hoverBorderColor: gradientStroke,
            data: [65, 59, 80, 81, 56, 89, 40, 32, 65, 59, 80, 81]
          },
          {
            label: "Dollar Rate",
            backgroundColor: "#e3eaef",
            borderColor: "#e3eaef",
            hoverBackgroundColor: "#e3eaef",
            hoverBorderColor: "#e3eaef",
            data: [89, 40, 32, 65, 59, 80, 81, 56, 89, 40, 65, 59]
          }
        ]
      };
      var barOpts = {
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          yAxes: [{
            gridLines: {
              display: false,
              color: "rgba(0,0,0,0.05)"
            },
            stacked: false,
            ticks: {
              stepSize: 20
            }
          }],
          xAxes: [{
            barPercentage: 0.7,
            categoryPercentage: 0.5,
            stacked: false,
            gridLines: {
              color: "rgba(0,0,0,0.01)"
            }
          }]
        }
      };

      charts.push(this.respChart(document.getElementById("bar-chart-example"), 'Bar', barChart, barOpts));
    }

    if (document.querySelectorAll('#donut-chart-example').length > 0) {
      var dataColors = document.getElementById('donut-chart-example')
        .getAttribute('data-colors');
      var colors = dataColors? dataColors.split(",") : defaultColors.concat();
      //donut chart
      var donutChart = {
        labels: [
          "Direct",
          "Affilliate",
          "Sponsored",
          "E-mail"
        ],
        datasets: [
          {
            data: [300, 135, 48, 154],
            backgroundColor: colors,
            borderColor: "transparent",
            borderWidth: "3",
          }]
      };
      var donutOpts = {
        maintainAspectRatio: false,
        cutoutPercentage: 60,
        legend: {
          display: false
        }
      };
      charts.push(this.respChart(document.getElementById("donut-chart-example"), 'Doughnut', donutChart, donutOpts));
    }

    if (document.querySelectorAll('#radar-chart-example').length > 0) {
        var dataColors = document.getElementById('radar-chart-example')
          .getAttribute('data-colors');
        var colors = dataColors ? dataColors.split(",") : defaultColors.concat();

        //radar chart
        var radarChart = {
          labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"],
          datasets: [
            {
              label: "Desktops",
              backgroundColor: this.hexToRGB(colors[0], 0.2),
              borderColor: colors[0],
              pointBackgroundColor: colors[0],
              pointBorderColor: "#fff",
              pointHoverBackgroundColor: "#fff",
              pointHoverBorderColor: colors[0],
              data: [65, 59, 90, 81, 56, 55, 40]
            },
            {
              label: "Tablets",
              backgroundColor: this.hexToRGB(colors[1], 0.2),
              borderColor: colors[1],
              pointBackgroundColor: colors[1],
              pointBorderColor: "#fff",
              pointHoverBackgroundColor: "#fff",
              pointHoverBorderColor: colors[1],
              data: [28, 48, 40, 19, 96, 27, 100]
            }
          ]
        };
        var radarOpts = {
          maintainAspectRatio: false
        };
        charts.push(this.respChart(document.getElementById("radar-chart-example"), 'Radar', radarChart, radarOpts));

    }
    return charts;
  }


  init() {

    const self = this;
    // font
    Chart.defaults.global.defaultFontFamily = '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif';

    // init charts
    self.charts = this.initCharts();

    window.addEventListener('resize',function(e){
      self.charts.forEach(function (chart){
        try{
          chart.destroy();
        }catch (err){

        }
      });
      self.charts = self.initCharts();
    });

    self.initCharts();
  }


}

// init the dashboard
new Chartjs().init();
