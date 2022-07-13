/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: CRM Management
 */

import ApexCharts from 'apexcharts/dist/apexcharts';

import { Datepicker, } from 'vanillajs-datepicker';
import '../../../../node_modules/vanillajs-datepicker/dist/css/datepicker-bs4.css';
import '../../../../node_modules/vanillajs-datepicker/dist/css/datepicker.css';

class CRMManagement {
    constructor() { }

    initCharts() {

        var colors = ["#727cf5", "#0acf97"];
        var dataColors = document.getElementById("revenue-statistics-chart").getAttribute('data-colors');
        if (dataColors) {
            colors = dataColors.split(",");
        }

        var options = {
            chart: {
                height: 361,
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
                name: 'Budget',
                data: [10, 20, 15, 28, 22, 34]
            }, {
                name: 'Revenue',
                data: [2, 26, 10, 38, 30, 48]
            }],
            colors: colors,
            zoom: {
                enabled: false
            },
            xaxis: {
                type: 'string',
                categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
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
                        return val + "k"
                    },
                    offsetX: -15
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#revenue-statistics-chart"),
            options
        );

        chart.render();
    }
    init() {
        this.initCharts();

        new Datepicker(document.getElementById('calendar-widget')).setDate(new Date());

    }

}

new CRMManagement().init();