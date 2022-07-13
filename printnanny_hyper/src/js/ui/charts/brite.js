/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

import { britecharts,miniTooltip,bar,line,tooltip,donut,legend,brush,step } from 'britecharts';
import { selectAll,select } from 'd3-selection';
import 'britecharts/dist/css/britecharts.css'
import {timeformat } from 'd3';



class Brite {

  constructor() {
    this.defaultColors = ["#727cf5", "#0acf97", "#6c757d", "#fa5c7c", "#ffbc00", "#39afd1", "#e3eaef"];
    this.barData = [
      { name: "Mon", value: 2100 },
      { name: "Tue", value: 5000 },
      { name: "Wed", value: 4000 },
      { name: "Thu", value: 5500 },
      { name: "Fri", value: 6500 },
      { name: "Sat", value: 4500 },
      { name: "Sun", value: 3500 }
    ];

    this.lineData = {
      dataByTopic: [
        {
          topic: 103,
          topicName: "San Francisco",
          dates: [
            {
              date: "2018-06-27T07:00:00.000Z",
              value: 1,
              fullDate: "2018-06-27T07:00:00.000Z"
            },
            {
              date: "2018-06-28T07:00:00.000Z",
              value: 1,
              fullDate: "2018-06-28T07:00:00.000Z"
            },
            {
              date: "2018-06-29T07:00:00.000Z",
              value: 4,
              fullDate: "2018-06-29T07:00:00.000Z"
            },
            {
              date: "2018-06-30T07:00:00.000Z",
              value: 2,
              fullDate: "2018-06-30T07:00:00.000Z"
            },
            {
              date: "2018-07-01T07:00:00.000Z",
              value: 3,
              fullDate: "2018-07-01T07:00:00.000Z"
            },
            {
              date: "2018-07-02T07:00:00.000Z",
              value: 3,
              fullDate: "2018-07-02T07:00:00.000Z"
            },
            {
              date: "2018-07-03T07:00:00.000Z",
              value: 0,
              fullDate: "2018-07-03T07:00:00.000Z"
            },
            {
              date: "2018-07-04T07:00:00.000Z",
              value: 3,
              fullDate: "2018-07-04T07:00:00.000Z"
            },
            {
              date: "2018-07-05T07:00:00.000",
              value: 1,
              fullDate: "2018-07-05T07:00:00.000Z"
            },
            {
              date: "2018-07-06T07:00:00.000Z",
              value: 2,
              fullDate: "2018-07-06T07:00:00.000Z"
            },
            {
              date: "2018-07-07T07:00:00.000Z",
              value: 0,
              fullDate: "2018-07-07T07:00:00.000Z"
            },
            {
              date: "2018-07-08T07:00:00.000Z",
              value: 2,
              fullDate: "2018-07-08T07:00:00.000Z"
            },
            {
              date: "2018-07-09T07:00:00.000Z",
              value: 1,
              fullDate: "2018-07-09T07:00:00.000Z"
            },
            {
              date: "2018-07-10T07:00:00.000Z",
              value: 4,
              fullDate: "2018-07-10T07:00:00.000Z"
            },
            {
              date: "2018-07-11T07:00:00.000Z",
              value: 2,
              fullDate: "2018-07-11T07:00:00.000Z"
            },
            {
              date: "2018-07-12T07:00:00.000Z",
              value: 1,
              fullDate: "2018-07-12T07:00:00.000Z"
            },
            {
              date: "2018-07-13T07:00:00.000Z",
              value: 6,
              fullDate: "2018-07-13T07:00:00.000Z"
            },
            {
              date: "2018-07-14T07:00:00.000Z",
              value: 5,
              fullDate: "2018-07-14T07:00:00.000Z"
            },
            {
              date: "2018-07-15T07:00:00.000Z",
              value: 2,
              fullDate: "2018-07-15T07:00:00.000Z"
            }
          ]
        }
      ]
    };

    this.donutData = [
      { name: "Shiny", id: 1, quantity: 86, percentage: 5 },
      { name: "Blazing", id: 2, quantity: 300, percentage: 18 },
      { name: "Dazzling", id: 3, quantity: 276, percentage: 16 },
      { name: "Radiant", id: 4, quantity: 195, percentage: 11 },
      { name: "Sparkling", id: 5, quantity: 36, percentage: 2 },
      { name: "Other", id: 0, quantity: 814, percentage: 48 }
    ];

    this.brushData = [
      { date: "2018-06-27T07:00:00.000Z", value: 4 },
      { date: "2018-06-28T07:00:00.000Z", value: 12 },
      { date: "2018-06-29T07:00:00.000Z", value: 33 },
      { date: "2018-06-30T07:00:00.000Z", value: 17 },
      { date: "2018-07-01T07:00:00.000Z", value: 17 },
      { date: "2018-07-02T07:00:00.000Z", value: 16 },
      { date: "2018-07-03T07:00:00.000Z", value: 8 },
      { date: "2018-07-04T07:00:00.000Z", value: 14 },
      { date: "2018-07-05T07:00:00.000Z", value: 11 },
      { date: "2018-07-06T07:00:00.000Z", value: 14 },
      { date: "2018-07-07T07:00:00.000Z", value: 25 },
      { date: "2018-07-08T07:00:00.000Z", value: 55 },
      { date: "2018-07-09T07:00:00.000Z", value: 15 },
      { date: "2018-07-10T07:00:00.000Z", value: 26 },
      { date: "2018-07-11T07:00:00.000Z", value: 21 },
      { date: "2018-07-12T07:00:00.000Z", value: 16 },
      { date: "2018-07-13T07:00:00.000Z", value: 20 },
      { date: "2018-07-14T07:00:00.000Z", value: 26 },
      { date: "2018-07-15T07:00:00.000Z", value: 24 },
      { date: "2018-07-16T07:00:00.000Z", value: 29 },
      { date: "2018-07-17T07:00:00.000Z", value: 12 },
      { date: "2018-07-18T07:00:00.000Z", value: 16 },
      { date: "2018-07-19T07:00:00.000Z", value: 11 },
      { date: "2018-07-20T07:00:00.000Z", value: 29 },
      { date: "2018-07-21T07:00:00.000Z", value: 9 },
      { date: "2018-07-22T07:00:00.000Z", value: 26 },
      { date: "2018-07-23T07:00:00.000Z", value: 21 },
      { date: "2018-07-24T07:00:00.000Z", value: 18 },
      { date: "2018-07-25T07:00:00.000Z", value: 15 },
      { date: "2018-07-26T07:00:00.000Z", value: 23 },
      { date: "2018-07-27T07:00:00.000Z", value: 43 },
      { date: "2018-07-28T07:00:00.000Z", value: 44 },
      { date: "2018-07-29T07:00:00.000Z", value: 67 },
      { date: "2018-07-30T07:00:00.000Z", value: 67 },
      { date: "2018-07-31T07:00:00.000Z", value: 0 },
      { date: "2018-08-01T07:00:00.000Z", value: 0 },
      { date: "2018-08-02T07:00:00.000Z", value: 0 }
    ];

    this.stepData = [
      { key: "Appetizer", value: 400 },
      { key: "Soup", value: 300 },
      { key: "Salad", value: 300 },
      { key: "Lunch", value: 250 },
      { key: "Dinner", value: 220 },
      { key: "Dessert", value: 100 },
      { key: "Midnight snack", value: 20 }
    ];
  }


  createBarChart(elementSelector, data) {
    var dataColors = document.querySelector(elementSelector).getAttribute('data-colors');
    var colors = dataColors? dataColors.split(",") : this.defaultColors.concat();

    var chartTooltip =  miniTooltip();
    var _barChart = bar();
    var barContainer = select(elementSelector),
      containerWidth = barContainer.node()
        ? barContainer.node().getBoundingClientRect().width
        : false,
      containerHeight = barContainer.node()
        ? barContainer.node().getBoundingClientRect().height
        : false,
      tooltipContainer = void 0;

    var margin = {
      top: 10,
      left: 55,
      bottom: 20,
      right: 10
    };

    _barChart
      .isAnimated(true)
      .width(containerWidth)
      .height(containerHeight)
      .margin(margin)
      .betweenBarsPadding(0.5)
      .colorSchema(colors)
      .on("customMouseOver", chartTooltip.show)
      .on("customMouseMove", chartTooltip.update)
      .on("customMouseOut", chartTooltip.hide);

    barContainer.datum(data).call(_barChart);
    tooltipContainer = select(elementSelector + " .metadata-group");
    tooltipContainer.datum([]).call(chartTooltip);
  };

  createHorizontalBarChart(elementSelector, data) {
    var dataColors = document.querySelector(elementSelector).getAttribute('data-colors');
    var colors = dataColors? dataColors.split(",") : this.defaultColors.concat();

    var _barChart = bar();

    var barContainer = select(elementSelector),
      containerWidth = barContainer.node()
        ? barContainer.node().getBoundingClientRect().width
        : false,
      containerHeight = barContainer.node()
        ? barContainer.node().getBoundingClientRect().height
        : false,
      tooltipContainer = void 0;

    var margin = {
      top: 10,
      left: 50,
      bottom: 20,
      right: 10
    };

    _barChart
      .colorSchema(colors)
      .isAnimated(true)
      .isHorizontal(true)
      .width(containerWidth)
      .margin(margin)
      .enableLabels(true)
      .percentageAxisToMaxRatio(1.3)
      .labelsNumberFormat(1)
      .height(containerHeight);

    barContainer.datum(data).call(_barChart);
  };

  createLineChart(elementSelector, data) {


    var lineChart = line(),
      chartTooltip = tooltip(),
      lineContainer = select(elementSelector),
      containerWidth = lineContainer.node()
        ? lineContainer.node().getBoundingClientRect().width
        : false,
      tooltipContainer = void 0;

    lineChart
      .isAnimated(true)
      .aspectRatio(0.7)
      .tooltipThreshold(100)
      .grid("horizontal")
      .width(containerWidth)
      .dateLabel("date")
      .valueLabel("value")
      .on("customMouseOver", chartTooltip.show)
      .on("customMouseMove", chartTooltip.update)
      .on("customMouseOut", chartTooltip.hide);

    chartTooltip.title("Sample Data");

    //   .topicsOrder(lineData2.dataByTopic.map(function(topic) {
    //   return topic.topic;
    // }));

    lineContainer.datum(data).call(lineChart);
    tooltipContainer = select(
      elementSelector + " .metadata-group .hover-marker"
    );
    tooltipContainer.datum([]).call(chartTooltip);
  };


  createDonutChart(elementSelector, data) {
    var dataColors =  document.querySelector(elementSelector).getAttribute('data-colors');
    var colors = dataColors? dataColors.split(",") : this.defaultColors.concat();

    var donutChart = donut(),
      legendChart = legend(),
      legendContainer = void 0;

    legendChart
      .width(250)
      .height(200)
      .colorSchema(colors)
      .numberFormat("s");

    donutChart.height(300)
      .highlightSliceById(3)
      .colorSchema(colors)
      .hasFixedHighlightedSlice(true)
      .internalRadius(80)
      .on('customMouseOver', function (data) {
        legendChart.highlight(data.data.id);
      })
      .on('customMouseOut', function () {
        legendChart.clearHighlight();
      });

    select(elementSelector)
      .datum(data)
      .call(donutChart);
    legendContainer = select(".legend-chart-container");
    legendContainer.datum(data).call(legendChart);
  };

  createBrushChart(elementSelector, data) {
    var brushContainer = select(elementSelector);
    var brushChart = brush(),
      containerWidth = brushContainer.node()
        ? brushContainer.node().getBoundingClientRect().width
        : false;

    brushChart
      .height(320)
      .width(containerWidth)
      .on("customBrushStart", function (brushExtent) {

        //   var format = timeFormat("%m/%d/%Y");
      })
      .on("customBrushEnd", function (brushExtent) {});

    brushContainer.datum(data).call(brushChart);

    brushChart.dateRange(["9/15/2015", "1/25/2016"]);
  };

  createStepChart(elementSelector, data) {
    var stepChart = step(),
      chartTooltip = miniTooltip(),
      stepContainer = select(elementSelector),
      containerWidth = stepContainer.node()
        ? stepContainer.node().getBoundingClientRect().width
        : false,
      tooltipContainer = void 0;

    stepChart
      .width(containerWidth)
      .height(320)
      .margin({
        top: 40,
        right: 40,
        bottom: 80,
        left: 50
      })
      .on("customMouseOver", chartTooltip.show)
      .on("customMouseMove", chartTooltip.update)
      .on("customMouseOut", chartTooltip.hide);

    stepContainer.datum(data).call(stepChart);

    chartTooltip.nameLabel("key");

    tooltipContainer = select(
      elementSelector + " .step-chart .metadata-group"
    );
    tooltipContainer.datum([]).call(chartTooltip);
  };


  drawCharts() {
      selectAll('.bar-chart')
        .remove();
    selectAll('.line-chart')
        .remove();
    selectAll('.donut-chart')
        .remove();
    selectAll('.britechart-legend')
        .remove();
    selectAll('.brush-chart')
        .remove();
   selectAll('.step-chart')
        .remove();

    if (document.querySelectorAll(".bar-container").length > 0) {
      this.createBarChart(".bar-container", this.barData);
    }

    if (document.querySelectorAll(".bar-container-horizontal").length > 0) {
      this.createHorizontalBarChart(
        ".bar-container-horizontal",
        this.barData
      );
    }

    if (document.querySelectorAll(".line-container").length > 0) {
      this.createLineChart(".line-container", this.lineData);
    }

    if (document.querySelectorAll(".donut-container").length > 0) {
      this.createDonutChart(".donut-container", this.donutData);
    }

    if (document.querySelectorAll(".brush-container").length > 0) {
      this.createBrushChart(".brush-container", this.brushData);
    }

    if (document.querySelectorAll(".step-container").length > 0) {
      this.createStepChart(".step-container", this.stepData);
    }
  }

  init() {

    this.initCharts();

  }

  initCharts() {

    const self = this;

    window.addEventListener('resize', function (e) {
      e.preventDefault();
      setTimeout(self.drawCharts(), 200);
    });

    window.addEventListener('hyper.setFluid', function (e) {
      e.preventDefault();
      setTimeout(self.drawCharts(), 200);
    });

    window.addEventListener('hyper.setBoxed', function (e) {
      e.preventDefault();
      setTimeout(self.drawCharts(), 200);
    });


    self.drawCharts();

  }
}

// init the dashboard
new Brite().init();
