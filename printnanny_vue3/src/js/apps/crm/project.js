/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: CRM Project
 */

import Choices from 'choices.js';
import 'choices.js/src/styles/choices.scss';

import ApexCharts from 'apexcharts/dist/apexcharts';

class CRMProject {
    constructor() {

    }

    initSelect2 = () => {
        document.querySelectorAll('[data-toggle="select2"]').forEach(function (element) {

            if (element.multiple) {
                new Choices(element, {
                    itemSelectText: '',
                    placeholder: true,
                    placeholderValue: 'select',
                    removeItemButton: true,
                    removeItems: true,
                    choices: [
                        { value: 'select', label: "Select", selected: true }
                    ]
                }).setChoiceByValue('select');
            } else {
                new Choices(element, {
                    itemSelectText: '',
                    placeholderValue: 'select',
                    placeholder: true,
                    removeItemButton: false,
                    removeItems: false,

                }).setChoiceByValue('select');
            }

            document.querySelectorAll('.choices__group .choices__heading').forEach(function (element) {
                element.innerHTML == "" ? element.parentElement.classList.add('d-none') : null;
            });
        });
    }

    initCharts() {
        // Project Statistics
        var colors = ["#727cf5", "#0acf97"];
        var dataColors = document.getElementById("crm-project-statistics").getAttribute('data-colors');

        if (dataColors) {
            colors = dataColors.split(",");
        }
        var options = {
            chart: {
                height: 327,
                type: 'bar',
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    endingShape: 'rounded',
                    columnWidth: '25%',
                },
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 3,
                colors: ['transparent']
            },
            colors: colors,
            series: [{
                name: 'Previous Week Sale',
                data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
            }, {
                name: 'This Week Sale',
                data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
            }],
            xaxis: {
                categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            },
            legend: {
                offsetY: 7,
            },
            yaxis: {
                title: {
                    text: '$ (thousands)'
                }
            },
            fill: {
                opacity: 1

            },
            // legend: {
            //     floating: true
            // },
            grid: {
                row: {
                    colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
                    opacity: 0.2
                },
                borderColor: '#f1f3fa',
                padding: {
                    bottom: 5
                }
            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return "$ " + val + "K"
                    }
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#crm-project-statistics"),
            options
        );

        chart.render();


        // Monthly Target

        var colors = ["#727cf5", "#0acf97"];
        var dataColors = document.getElementById("monthly-target").getAttribute('data-colors');
        if (dataColors) {
            colors = dataColors.split(",");
        }
        var options = {
            chart: {
                height: 255,
                type: 'donut',
            },
            legend: {
                show: false
            },
            stroke: {
                colors: ['transparent']
            },
            series: [60, 40],
            labels: ["Panding Projects", "Done Projects"],
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
        }

        var chart = new ApexCharts(
            document.querySelector("#monthly-target"),
            options
        );

        chart.render();


        //
        // project-overview CHART
        //
        var colors = ["#727cf5", "#0acf97", "#fa5c7c", "#ffbc00"];
        var dataColors = document.getElementById("project-overview-chart").getAttribute('data-colors');
        if (dataColors) {
            colors = dataColors.split(",");
        }
        var options = {
            chart: {
                height: 326,
                type: 'radialBar'
            },
            colors: colors,
            series: [85, 70, 80, 65],
            labels: ['Product Design', 'Web Development', 'Illustration Design', 'UI/UX Design'],
            plotOptions: {
                radialBar: {
                    track: {
                        margin: 5,
                    }
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#project-overview-chart"),
            options
        );

        chart.render();

    }

    init() {
        this.initSelect2();
        this.initCharts();
    }
}

new CRMProject().init();
