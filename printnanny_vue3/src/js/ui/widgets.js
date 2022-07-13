/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

import 'simplebar/dist/simplebar';
import ApexCharts from 'apexcharts';
import Todo from '../components/todo';
import Chat from '../components/chat';

class Widgets {

  constructor() {
    Apex.grid = {
      padding: {
        right: 0,
        left: 0
      }
    }

    Apex.dataLabels = {
      enabled: false
    }

  }

  randomizeArray(arg) {
    var array = arg.slice();
    var currentIndex = array.length, temporaryValue, randomIndex;

    while (0 !== currentIndex) {

      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;

      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }

    return array;
  }

  initCharts() {

    const sparklineData = [47, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19, 46];

    // the default colorPalette for this dashboard
    const colorPalette = ['#00D8B6', '#008FFB', '#FEB019', '#FF4560', '#775DD0'];

    const labelsSales = [];
    for (let i = 1; i <= 24; i++) {
      labelsSales.push('2018-09-' + i);
    }
    let colors = ['#3688fc'];
    let dataColors = document.getElementById('sales-spark').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const salesspark = {
      chart: {
        type: 'area',
        height: 172,
        sparkline: {
          enabled: true
        },
      },
      stroke: {
        width: 2,
        curve: 'straight'
      },
      fill: {
        opacity: 0.2,
      },
      series: [{
        name: 'Hyper Sales',
        data: this.randomizeArray(sparklineData)
      }],
      xaxis: {
        type: 'datetime',
      },
      yaxis: {
        min: 0
      },
      colors: colors,
      labels: labelsSales,
      title: {
        text: '$424,652',
        offsetX: 20,
        offsetY: 20,
        style: {
          fontSize: '24px'
        }
      },
      subtitle: {
        text: 'Sales',
        offsetX: 20,
        offsetY: 55,
        style: {
          fontSize: '14px'
        }
      }
    };
    new ApexCharts(document.querySelector("#sales-spark"), salesspark).render();

    colors = ['#0acf97'];
    dataColors = document.getElementById('profit-spark').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const profitspark = {
      chart: {
        type: 'bar',
        height: 172,
        sparkline: {
          enabled: true
        },
      },
      stroke: {
        width: 0,
        curve: 'straight'
      },
      fill: {
        opacity: 0.5,
      },
      series: [{
        name: 'Net Profits ',
        data: this.randomizeArray(sparklineData)
      }],
      xaxis: {
        crosshairs: {
          width: 1
        },
      },
      yaxis: {
        min: 0
      },
      colors: colors,
      title: {
        text: '$135,965',
        offsetX: 20,
        offsetY: 20,
        style: {
          fontSize: '24px'
        }
      },
      subtitle: {
        text: 'Profits',
        offsetX: 20,
        offsetY: 55,
        style: {
          fontSize: '14px'
        }
      }
    };

    new ApexCharts(document.querySelector("#profit-spark"), profitspark).render();

    // Other Sparkline

    colors = ['#734CEA'];
    dataColors = document.getElementById('spark1').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const spark1 = {
      chart: {
        type: 'line',
        height: 100,
        sparkline: {
          enabled: true
        },
      },
      series: [{
        data: [25, 66, 41, 59, 25, 44, 12, 36, 9, 21]
      }],
      stroke: {
        width: 4,
        curve: 'smooth'
      },
      markers: {
        size: 0
      },
      colors: colors
    };
    colors = ['#34bfa3'];
    dataColors = document.getElementById('spark2').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const spark2 = {
      chart: {
        type: 'bar',
        height: 100,
        sparkline: {
          enabled: true
        },
      },
      series: [{
        data: [12, 14, 2, 47, 32, 44, 14, 55, 41, 69]
      }],
      stroke: {
        width: 3,
        curve: 'smooth'
      },
      markers: {
        size: 0
      },
      colors: colors
    };
    colors = ['#f4516c'];
    dataColors = document.getElementById('spark3').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const spark3 = {
      chart: {
        type: 'line',
        height: 100,
        sparkline: {
          enabled: true
        },
      },
      series: [{
        data: [47, 45, 74, 32, 56, 31, 44, 33, 45, 19]
      }],
      stroke: {
        width: 4,
        curve: 'smooth'
      },
      markers: {
        size: 0
      },
      colors: colors
    };
    colors = ['#00c5dc'];
    dataColors = document.getElementById('spark4').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const spark4 = {
      chart: {
        type: 'bar',
        height: 100,
        sparkline: {
          enabled: true
        },
      },
      plotOptions: {
        bar: {
          horizontal: false,
          endingShape: 'rounded',
          columnWidth: '55%',
        },
      },
      series: [{
        data: [15, 75, 47, 65, 14, 32, 19, 54, 44, 61]
      }],
      stroke: {
        width: 3,
        curve: 'smooth'
      },
      markers: {
        size: 0
      },
      colors: colors
    };

    new ApexCharts(document.querySelector("#spark1"), spark1).render();
    new ApexCharts(document.querySelector("#spark2"), spark2).render();
    new ApexCharts(document.querySelector("#spark3"), spark3).render();
    new ApexCharts(document.querySelector("#spark4"), spark4).render();

    colors = ['#727cf5'];
    dataColors = document.getElementById('campaign-sent-chart').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const options1 = {
      chart: {
        type: 'bar',
        height: 60,
        sparkline: {
          enabled: true
        }
      },
      plotOptions: {
        bar: {
          columnWidth: '60%'
        }
      },
      colors: colors,
      series: [{
        data: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54]
      }],
      labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
      xaxis: {
        crosshairs: {
          width: 1
        },
      },
      tooltip: {
        fixed: {
          enabled: false
        },
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return '';
            }
          }
        },
        marker: {
          show: false
        }
      }
    };

    new ApexCharts(document.querySelector("#campaign-sent-chart"), options1).render();


    //
    // New Leads Chart
    //
    colors = ['#727cf5'];
    dataColors = document.getElementById('new-leads-chart').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const options2 = {
      chart: {
        type: 'line',
        height: 60,
        sparkline: {
          enabled: true
        }
      },
      series: [{
        data: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54]
      }],
      stroke: {
        width: 2,
        curve: 'smooth'
      },
      markers: {
        size: 0
      },
      colors: colors,
      tooltip: {
        fixed: {
          enabled: false
        },
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return '';
            }
          }
        },
        marker: {
          show: false
        }
      }
    };

    new ApexCharts(document.querySelector("#new-leads-chart"), options2).render();


    //
    // Deals Charts
    //
    colors = ['#727cf5'];
    dataColors = document.getElementById('deals-chart').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const options3 = {
      chart: {
        type: 'bar',
        height: 60,
        sparkline: {
          enabled: true
        }
      },
      plotOptions: {
        bar: {
          columnWidth: '60%'
        }
      },
      colors: colors,
      series: [{
        data: [12, 14, 2, 47, 42, 15, 47, 75, 65, 19, 14]
      }],
      labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
      xaxis: {
        crosshairs: {
          width: 1
        },
      },
      tooltip: {
        fixed: {
          enabled: false
        },
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return '';
            }
          }
        },
        marker: {
          show: false
        }
      }
    };

    new ApexCharts(document.querySelector("#deals-chart"), options3).render();

    //
    // Booked Revenue Chart
    //
    colors = ['#727cf5'];
    dataColors = document.getElementById('booked-revenue-chart').getAttribute('data-colors');
    if (dataColors) {
      colors = dataColors.split(",");
    }
    const options4 = {
      chart: {
        type: 'bar',
        height: 60,
        sparkline: {
          enabled: true
        }
      },
      plotOptions: {
        bar: {
          columnWidth: '60%'
        }
      },
      colors: colors,
      series: [{
        data: [47, 45, 74, 14, 56, 74, 14, 11, 7, 39, 82]
      }],
      labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
      xaxis: {
        crosshairs: {
          width: 1
        },
      },
      tooltip: {
        fixed: {
          enabled: false
        },
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return '';
            }
          }
        },
        marker: {
          show: false
        }
      }
    };

    new ApexCharts(document.querySelector("#booked-revenue-chart"), options4).render();

  }

  init() {

    this.initCharts();
    new Todo().init();
    new Chat().init();

  }
}

// init the dashboard
new Widgets().init();
