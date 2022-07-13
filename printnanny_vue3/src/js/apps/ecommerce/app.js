/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: E-Commerce
 */

import {DataTable} from 'simple-datatables';
import 'simple-datatables/src/style.css';
import ApexCharts from 'apexcharts/dist/apexcharts';
import Choices from 'choices.js';
import 'choices.js/src/styles/choices.scss';
import {Grid,html,h} from 'gridjs';
import 'gridjs/dist/theme/mermaid.min.css';
import { RowSelection } from "gridjs/plugins/selection";



class EcommerceApp {

  constructor() {

    
  }

  


  init() {
    document.querySelectorAll('[data-toggle="select2"]').forEach(function(element) {
      new Choices(element,{
        itemSelectText:'',
      });
    });


    

  }



}         

// init the dashboard
new EcommerceApp().init();
