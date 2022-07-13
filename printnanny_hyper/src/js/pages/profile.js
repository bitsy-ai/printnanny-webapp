import Chart from 'chart.js';

/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Profile
 */

class Profile {

  constructor() {
    this.charts = [];
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

  initCharts(){
    var charts = [];

    //barchart
    if (document.querySelectorAll('#high-performing-product').length > 0) {
      // create gradient
      const ctx = document.getElementById('high-performing-product')
        .getContext('2d');
      const gradientStroke = ctx.createLinearGradient(0, 500, 0, 150);
      gradientStroke.addColorStop(0, "#fa5c7c");
      gradientStroke.addColorStop(1, "#727cf5");

      const barChart = {
        // labels: ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
          {
            label: 'Orders',
            backgroundColor: gradientStroke,
            borderColor: gradientStroke,
            hoverBackgroundColor: gradientStroke,
            hoverBorderColor: gradientStroke,
            data: [65, 59, 80, 81, 56, 89, 40, 32, 65, 59, 80, 81]
          },
          {
            label: 'Revenue',
            backgroundColor: '#e3eaef',
            borderColor: '#e3eaef',
            hoverBackgroundColor: '#e3eaef',
            hoverBorderColor: '#e3eaef',
            data: [89, 40, 32, 65, 59, 80, 81, 56, 89, 40, 65, 59]
          }
        ]
      };
      const barOpts = {
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          yAxes: [{
            gridLines: {
              display: false,
              color: 'rgba(0,0,0,0.05)'
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
              color: 'rgba(0,0,0,0.01)'
            }
          }]
        }
      };

      charts.push(this.respChart(document.getElementById("high-performing-product"), 'Bar', barChart, barOpts));

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
  }

}

// init the dashboard
new Profile().init();
