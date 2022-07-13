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



class EcommerceProduct {

  constructor() {
  }

  initProducts(){

  var grid = new Grid(
    {
      // columns:[" Name","Position","Office","Age"," Start date","Salary"],
      columns: [
        {
          id: 'rowSelect',
          name: h('input', {
            type: "checkbox",
            className: "form-check-input position-absolute start-50 top-50 translate-middle",
            id: "select-all-checkbox",

          }),
          plugin: {
            component: RowSelection,
            props: {
              id: (row) => row.cell(1).data
            },
          },
          sort: false,
        },
        {
          id: 'id',
          name: 'id',
          hidden: true,
        },
        {
          id: 'name',
          name: 'Product',
         formatter: this.productDetailsFormatter.bind(this),
        },
        {
          id: 'image',
          name: 'Image',
          hidden: true,
        },
        {
          id: 'rating',
          name: 'Rating',
          hidden: true,
        },
        {
          id: 'category',
          name: 'Category'
        }, {
          id: 'added_date',
          name: 'Added Date'
        },
        {
          id: 'price',
          name: 'Price'
        },
        {
          id: 'quantity',
          name: 'Quantity'
        },
        {
          id: 'status',
          name: 'Status',
          formatter: this.productStatusFormatter.bind(this)
        },
        {
          name: 'Action',
          sort: false,
          // width: '85px',
          formatter: this.productActionFormatter.bind(this)
        }],
      // from: table,
      data:[{
        id: 1,
        name: 'G-Series G30',
        category: 'Chevrolet',
        image: '../../images/products/product-1.jpg',
        added_date: '06/26/2019',
        rating: 5,
        price: 992.98,
        quantity: 459,
        status: true
    }, {
        id: 2,
        name: 'Outlook',
        category: 'Saturn',
        image: '../../images/products/product-2.jpg',
        added_date: '02/12/2019',
        rating: 2,
        price: 294.05,
        quantity: 131,
        status: false
    }, {
        id: 3,
        name: 'GL-Class',
        category: 'Mercedes-Benz',
        image: '../../images/products/product-3.jpg',
        added_date: '03/19/2019',
        rating: 5,
        price: 463.28,
        quantity: 188,
        status: true
    }, {
        id: 4,
        name: 'F150',
        category: 'Ford',
        image: '../../images/products/product-4.jpg',
        added_date: '01/24/2019',
        rating: 2,
        price: 667.11,
        quantity: 314,
        status: true
    }, {
        id: 5,
        name: 'S60',
        category: 'Volvo',
        image: '../../images/products/product-5.jpg',
        added_date: '08/15/2019',
        rating: 2,
        price: 542.41,
        quantity: 164,
        status: false
    }, {
        id: 6,
        name: '626',
        category: 'Mazda',
        image: '../../images/products/product-6.jpg',
        added_date: '05/03/2019',
        rating: 2,
        price: 289.99,
        quantity: 492,
        status: true
    }, {
        id: 7,
        name: 'LS',
        category: 'Lexus',
        image: '../../images/products/product-1.jpg',
        added_date: '11/17/2018',
        rating: 3,
        price: 380.42,
        quantity: 144,
        status: false
    }, {
        id: 8,
        name: 'Quattroporte',
        category: 'Maserati',
        image: '../../images/products/product-2.jpg',
        added_date: '12/04/2018',
        rating: 5,
        price: 619.82,
        quantity: 482,
        status: true
    }, {
        id: 9,
        name: 'Firebird',
        category: 'Pontiac',
        image: '../../images/products/product-3.jpg',
        added_date: '10/19/2019',
        rating: 4,
        price: 209.63,
        quantity: 139,
        status: true
    }, {
        id: 10,
        name: 'GS',
        category: 'Lexus',
        image: '../../images/products/product-4.jpg',
        added_date: '10/18/2019',
        rating: 4,
        price: 830.24,
        quantity: 430,
        status: true
    }, {
        id: 11,
        name: 'Excel',
        category: 'Mitsubishi',
        image: '../../images/products/product-5.jpg',
        added_date: '01/24/2019',
        rating: 2,
        price: 290.06,
        quantity: 408,
        status: false
    }, {
        id: 12,
        name: 'XL7',
        category: 'Suzuki',
        image: '../../images/products/product-6.jpg',
        added_date: '12/30/2018',
        rating: 4,
        price: 733.93,
        quantity: 415,
        status: true
    }, {
        id: 13,
        name: 'Cabriolet',
        category: 'Volkswagen',
        image: '../../images/products/product-1.jpg',
        added_date: '12/13/2018',
        rating: 5,
        price: 592.86,
        quantity: 60,
        status: true
    }, {
        id: 14,
        name: 'S-Class',
        category: 'Mercedes-Benz',
        image: '../../images/products/product-2.jpg',
        added_date: '05/06/2019',
        rating: 3,
        price: 601.41,
        quantity: 189,
        status: false
    }, {
        id: 15,
        name: 'Tredia',
        category: 'Mitsubishi',
        image: '../../images/products/product-3.jpg',
        added_date: '07/22/2019',
        rating: 1,
        price: 883.51,
        quantity: 61,
        status: true
    }, {
        id: 16,
        name: 'Escalade ESV',
        category: 'Cadillac',
        image: '../../images/products/product-4.jpg',
        added_date: '05/27/2019',
        rating: 4,
        price: 782.01,
        quantity: 123,
        status: false
    }, {
        id: 17,
        name: 'Mariner',
        category: 'Mercury',
        image: '../../images/products/product-5.jpg',
        added_date: '02/27/2019',
        rating: 4,
        price: 765.89,
        quantity: 399,
        status: false
    }, {
        id: 18,
        name: 'Outback',
        category: 'Subaru',
        image: '../../images/products/product-6.jpg',
        added_date: '11/16/2018',
        rating: 4,
        price: 759.7,
        quantity: 233,
        status: false
    }, {
        id: 19,
        name: 'CX-9',
        category: 'Mazda',
        image: '../../images/products/product-1.jpg',
        added_date: '10/05/2019',
        rating: 4,
        price: 567.08,
        quantity: 236,
        status: true
    }, {
        id: 20,
        name: 'Envoy',
        category: 'GMC',
        image: '../../images/products/product-2.jpg',
        added_date: '12/31/2018',
        rating: 1,
        price: 684.37,
        quantity: 262,
        status: true
    }, {
        id: 21,
        name: '2500',
        category: 'Chevrolet',
        image: '../../images/products/product-3.jpg',
        added_date: '09/19/2019',
        rating: 3,
        price: 917.8,
        quantity: 399,
        status: true
    }, {
        id: 22,
        name: '911',
        category: 'Porsche',
        image: '../../images/products/product-4.jpg',
        added_date: '03/31/2019',
        rating: 2,
        price: 626.21,
        quantity: 361,
        status: true
    }, {
        id: 23,
        name: 'Caliber',
        category: 'Dodge',
        image: '../../images/products/product-5.jpg',
        added_date: '06/30/2019',
        rating: 2,
        price: 797.34,
        quantity: 41,
        status: false
    }, {
        id: 24,
        name: 'Pajero',
        category: 'Mitsubishi',
        image: '../../images/products/product-6.jpg',
        added_date: '11/16/2018',
        rating: 5,
        price: 615.29,
        quantity: 95,
        status: true
    }, {
        id: 25,
        name: 'M5',
        category: 'BMW',
        image: '../../images/products/product-1.jpg',
        added_date: '05/01/2019',
        rating: 5,
        price: 737.74,
        quantity: 251,
        status: true
    }, {
        id: 26,
        name: 'Sienna',
        category: 'Toyota',
        image: '../../images/products/product-2.jpg',
        added_date: '05/31/2019',
        rating: 2,
        price: 416.04,
        quantity: 122,
        status: true
    }, {
        id: 27,
        name: 'Grand Caravan',
        category: 'Dodge',
        image: '../../images/products/product-3.jpg',
        added_date: '02/09/2019',
        rating: 2,
        price: 866.99,
        quantity: 280,
        status: false
    }, {
        id: 28,
        name: 'Taurus',
        category: 'Ford',
        image: '../../images/products/product-4.jpg',
        added_date: '04/18/2019',
        rating: 2,
        price: 551.53,
        quantity: 49,
        status: true
    }, {
        id: 29,
        name: 'Econoline E150',
        category: 'Ford',
        image: '../../images/products/product-5.jpg',
        added_date: '03/17/2019',
        rating: 4,
        price: 197.76,
        quantity: 440,
        status: false
    }, {
        id: 30,
        name: 'Mini Cooper',
        category: 'Austin',
        image: '../../images/products/product-6.jpg',
        added_date: '06/19/2019',
        rating: 3,
        price: 508.98,
        quantity: 221,
        status: false
    }, {
        id: 31,
        name: 'B-Series',
        category: 'Mazda',
        image: '../../images/products/product-1.jpg',
        added_date: '03/11/2019',
        rating: 4,
        price: 463.47,
        quantity: 353,
        status: false
    }, {
        id: 32,
        name: 'Interceptor',
        category: 'Jensen',
        image: '../../images/products/product-2.jpg',
        added_date: '02/19/2019',
        rating: 2,
        price: 753.96,
        quantity: 76,
        status: false
    }, {
        id: 33,
        name: 'Grand Prix',
        category: 'Pontiac',
        image: '../../images/products/product-3.jpg',
        added_date: '05/18/2019',
        rating: 5,
        price: 326.9,
        quantity: 269,
        status: true
    }, {
        id: 34,
        name: '300',
        category: 'Chrysler',
        image: '../../images/products/product-4.jpg',
        added_date: '11/26/2018',
        rating: 3,
        price: 554.84,
        quantity: 212,
        status: true
    }, {
        id: 35,
        name: 'Ram Van 3500',
        category: 'Dodge',
        image: '../../images/products/product-5.jpg',
        added_date: '09/09/2019',
        rating: 2,
        price: 728.15,
        quantity: 223,
        status: true
    }, {
        id: 36,
        name: 'Integra',
        category: 'Acura',
        image: '../../images/products/product-6.jpg',
        added_date: '09/25/2019',
        rating: 2,
        price: 791.85,
        quantity: 21,
        status: true
    }, {
        id: 37,
        name: 'Grand Prix',
        category: 'Pontiac',
        image: '../../images/products/product-1.jpg',
        added_date: '11/07/2019',
        rating: 1,
        price: 109.51,
        quantity: 446,
        status: true
    }, {
        id: 38,
        name: 'Boxster',
        category: 'Porsche',
        image: '../../images/products/product-2.jpg',
        added_date: '11/08/2019',
        rating: 3,
        price: 702.78,
        quantity: 445,
        status: false
    }, {
        id: 39,
        name: 'E-Series',
        category: 'Ford',
        image: '../../images/products/product-3.jpg',
        added_date: '04/02/2019',
        rating: 5,
        price: 752.6,
        quantity: 294,
        status: true
    }, {
        id: 40,
        name: 'Ram',
        category: 'Dodge',
        image: '../../images/products/product-4.jpg',
        added_date: '12/19/2018',
        rating: 1,
        price: 509.55,
        quantity: 142,
        status: false
    }, {
        id: 41,
        name: 'Sorento',
        category: 'Kia',
        image: '../../images/products/product-5.jpg',
        added_date: '05/15/2019',
        rating: 5,
        price: 433.24,
        quantity: 90,
        status: true
    }, {
        id: 42,
        name: 'Sedona',
        category: 'Kia',
        image: '../../images/products/product-6.jpg',
        added_date: '05/23/2019',
        rating: 4,
        price: 407.97,
        quantity: 51,
        status: false
    }, {
        id: 43,
        name: 'RX Hybrid',
        category: 'Lexus',
        image: '../../images/products/product-1.jpg',
        added_date: '05/23/2019',
        rating: 3,
        price: 386.63,
        quantity: 222,
        status: false
    }, {
        id: 44,
        name: 'Altima',
        category: 'Nissan',
        image: '../../images/products/product-2.jpg',
        added_date: '08/22/2019',
        rating: 1,
        price: 692.1,
        quantity: 272,
        status: true
    }, {
        id: 45,
        name: 'Tundra',
        category: 'Toyota',
        image: '../../images/products/product-3.jpg',
        added_date: '11/23/2018',
        rating: 5,
        price: 603.89,
        quantity: 370,
        status: false
    }, {
        id: 46,
        name: 'LTD Crown Victoria',
        category: 'Ford',
        image: '../../images/products/product-4.jpg',
        added_date: '12/30/2018',
        rating: 5,
        price: 834.79,
        quantity: 256,
        status: true
    }, {
        id: 47,
        name: 'Classic',
        category: 'Chevrolet',
        image: '../../images/products/product-5.jpg',
        added_date: '02/05/2019',
        rating: 4,
        price: 341.37,
        quantity: 88,
        status: false
    }, {
        id: 48,
        name: 'S10',
        category: 'Chevrolet',
        image: '../../images/products/product-6.jpg',
        added_date: '02/25/2019',
        rating: 5,
        price: 502.81,
        quantity: 8,
        status: false
    }, {
        id: 49,
        name: 'Monte Carlo',
        category: 'Chevrolet',
        image: '../../images/products/product-1.jpg',
        added_date: '03/15/2019',
        rating: 3,
        price: 675.48,
        quantity: 253,
        status: true
    }, {
        id: 50,
        name: 'Stealth',
        category: 'Dodge',
        image: '../../images/products/product-2.jpg',
        added_date: '06/04/2019',
        rating: 5,
        price: 667.05,
        quantity: 303,
        status: true
    }, {
        id: 51,
        name: 'Grand Vitara',
        category: 'Suzuki',
        image: '../../images/products/product-3.jpg',
        added_date: '08/20/2019',
        rating: 4,
        price: 651.1,
        quantity: 307,
        status: true
    }, {
        id: 52,
        name: 'H3',
        category: 'Hummer',
        image: '../../images/products/product-4.jpg',
        added_date: '09/21/2019',
        rating: 5,
        price: 955.26,
        quantity: 309,
        status: true
    }, {
        id: 53,
        name: 'Santa Fe',
        category: 'Hyundai',
        image: '../../images/products/product-5.jpg',
        added_date: '06/04/2019',
        rating: 3,
        price: 728.71,
        quantity: 12,
        status: true
    }, {
        id: 54,
        name: 'Miata MX-5',
        category: 'Mazda',
        image: '../../images/products/product-6.jpg',
        added_date: '04/15/2019',
        rating: 1,
        price: 844.04,
        quantity: 112,
        status: true
    }, {
        id: 55,
        name: 'L-Series',
        category: 'Saturn',
        image: '../../images/products/product-1.jpg',
        added_date: '04/28/2019',
        rating: 2,
        price: 147.15,
        quantity: 313,
        status: true
    }, {
        id: 56,
        name: 'Excel',
        category: 'Hyundai',
        image: '../../images/products/product-2.jpg',
        added_date: '07/20/2019',
        rating: 3,
        price: 593.89,
        quantity: 168,
        status: true
    }, {
        id: 57,
        name: 'Tribute',
        category: 'Mazda',
        image: '../../images/products/product-3.jpg',
        added_date: '05/17/2019',
        rating: 4,
        price: 333.46,
        quantity: 13,
        status: false
    }, {
        id: 58,
        name: 'Corvette',
        category: 'Chevrolet',
        image: '../../images/products/product-4.jpg',
        added_date: '04/20/2019',
        rating: 3,
        price: 193.54,
        quantity: 72,
        status: false
    }, {
        id: 59,
        name: 'Azera',
        category: 'Hyundai',
        image: '../../images/products/product-5.jpg',
        added_date: '12/21/2018',
        rating: 2,
        price: 677.73,
        quantity: 462,
        status: false
    }, {
        id: 60,
        name: 'Esprit',
        category: 'Lotus',
        image: '../../images/products/product-6.jpg',
        added_date: '08/11/2019',
        rating: 4,
        price: 883.49,
        quantity: 434,
        status: false
    }, {
        id: 61,
        name: 'Trooper',
        category: 'Isuzu',
        image: '../../images/products/product-1.jpg',
        added_date: '06/30/2019',
        rating: 1,
        price: 199.83,
        quantity: 60,
        status: false
    }, {
        id: 62,
        name: 'Tempo',
        category: 'Ford',
        image: '../../images/products/product-2.jpg',
        added_date: '09/08/2019',
        rating: 2,
        price: 872.85,
        quantity: 209,
        status: false
    }, {
        id: 63,
        name: 'Space',
        category: 'Mitsubishi',
        image: '../../images/products/product-3.jpg',
        added_date: '06/15/2019',
        rating: 2,
        price: 250.64,
        quantity: 398,
        status: false
    }, {
        id: 64,
        name: 'Sebring',
        category: 'Chrysler',
        image: '../../images/products/product-4.jpg',
        added_date: '07/31/2019',
        rating: 4,
        price: 782.48,
        quantity: 9,
        status: false
    }, {
        id: 65,
        name: 'Fox',
        category: 'Volkswagen',
        image: '../../images/products/product-5.jpg',
        added_date: '04/04/2019',
        rating: 1,
        price: 431.8,
        quantity: 234,
        status: false
    }, {
        id: 66,
        name: 'Mountaineer',
        category: 'Mercury',
        image: '../../images/products/product-6.jpg',
        added_date: '11/11/2018',
        rating: 1,
        price: 766.91,
        quantity: 228,
        status: false
    }, {
        id: 67,
        name: 'Wrangler',
        category: 'Jeep',
        image: '../../images/products/product-1.jpg',
        added_date: '01/16/2019',
        rating: 5,
        price: 261.51,
        quantity: 222,
        status: false
    }, {
        id: 68,
        name: 'Spectra5',
        category: 'Kia',
        image: '../../images/products/product-2.jpg',
        added_date: '04/08/2019',
        rating: 2,
        price: 677.71,
        quantity: 263,
        status: false
    }, {
        id: 69,
        name: 'GTI',
        category: 'Volkswagen',
        image: '../../images/products/product-3.jpg',
        added_date: '01/20/2019',
        rating: 4,
        price: 472.59,
        quantity: 139,
        status: true
    }, {
        id: 70,
        name: 'Cordia',
        category: 'Mitsubishi',
        image: '../../images/products/product-4.jpg',
        added_date: '03/14/2019',
        rating: 2,
        price: 628.21,
        quantity: 78,
        status: false
    }, {
        id: 71,
        name: 'Pathfinder',
        category: 'Nissan',
        image: '../../images/products/product-5.jpg',
        added_date: '08/30/2019',
        rating: 1,
        price: 169.35,
        quantity: 232,
        status: true
    }, {
        id: 72,
        name: 'Thunderbird',
        category: 'Ford',
        image: '../../images/products/product-6.jpg',
        added_date: '08/14/2019',
        rating: 3,
        price: 676.6,
        quantity: 319,
        status: false
    }, {
        id: 73,
        name: '530',
        category: 'BMW',
        image: '../../images/products/product-1.jpg',
        added_date: '08/18/2019',
        rating: 1,
        price: 500.22,
        quantity: 172,
        status: true
    }, {
        id: 74,
        name: 'Milan',
        category: 'Mercury',
        image: '../../images/products/product-2.jpg',
        added_date: '02/21/2019',
        rating: 1,
        price: 591.49,
        quantity: 485,
        status: true
    }, {
        id: 75,
        name: 'Suburban 2500',
        category: 'Chevrolet',
        image: '../../images/products/product-3.jpg',
        added_date: '10/13/2019',
        rating: 2,
        price: 704.99,
        quantity: 10,
        status: false
    }, {
        id: 76,
        name: 'Forte',
        category: 'Kia',
        image: '../../images/products/product-4.jpg',
        added_date: '10/23/2019',
        rating: 4,
        price: 901.01,
        quantity: 105,
        status: true
    }, {
        id: 77,
        name: 'Riviera',
        category: 'Buick',
        image: '../../images/products/product-5.jpg',
        added_date: '03/23/2019',
        rating: 1,
        price: 837.11,
        quantity: 54,
        status: false
    }, {
        id: 78,
        name: 'Reatta',
        category: 'Buick',
        image: '../../images/products/product-6.jpg',
        added_date: '07/06/2019',
        rating: 3,
        price: 704.59,
        quantity: 193,
        status: true
    }, {
        id: 79,
        name: 'Caravan',
        category: 'Dodge',
        image: '../../images/products/product-1.jpg',
        added_date: '08/04/2019',
        rating: 3,
        price: 621.92,
        quantity: 495,
        status: true
    }, {
        id: 80,
        name: 'Range Rover Classic',
        category: 'Land Rover',
        image: '../../images/products/product-2.jpg',
        added_date: '09/04/2019',
        rating: 3,
        price: 408.1,
        quantity: 126,
        status: true
    }, {
        id: 81,
        name: 'Town Car',
        category: 'Lincoln',
        image: '../../images/products/product-3.jpg',
        added_date: '11/29/2018',
        rating: 1,
        price: 332.5,
        quantity: 300,
        status: true
    }, {
        id: 82,
        name: 'XLR-V',
        category: 'Cadillac',
        image: '../../images/products/product-4.jpg',
        added_date: '07/31/2019',
        rating: 5,
        price: 969.44,
        quantity: 137,
        status: true
    }, {
        id: 83,
        name: 'RX-7',
        category: 'Mazda',
        image: '../../images/products/product-5.jpg',
        added_date: '11/16/2018',
        rating: 3,
        price: 427.01,
        quantity: 193,
        status: false
    }, {
        id: 84,
        name: 'E350',
        category: 'Ford',
        image: '../../images/products/product-6.jpg',
        added_date: '10/05/2019',
        rating: 1,
        price: 401.65,
        quantity: 474,
        status: false
    }, {
        id: 85,
        name: 'Jetta',
        category: 'Volkswagen',
        image: '../../images/products/product-1.jpg',
        added_date: '01/24/2019',
        rating: 5,
        price: 250.91,
        quantity: 213,
        status: true
    }, {
        id: 86,
        name: 'Fusion',
        category: 'Ford',
        image: '../../images/products/product-2.jpg',
        added_date: '07/26/2019',
        rating: 5,
        price: 584.36,
        quantity: 80,
        status: true
    }, {
        id: 87,
        name: 'W201',
        category: 'Mercedes-Benz',
        image: '../../images/products/product-3.jpg',
        added_date: '08/04/2019',
        rating: 2,
        price: 281.65,
        quantity: 263,
        status: true
    }, {
        id: 88,
        name: 'Blazer',
        category: 'Chevrolet',
        image: '../../images/products/product-4.jpg',
        added_date: '01/27/2019',
        rating: 3,
        price: 832.14,
        quantity: 58,
        status: true
    }, {
        id: 89,
        name: 'Accord',
        category: 'Honda',
        image: '../../images/products/product-5.jpg',
        added_date: '03/04/2019',
        rating: 3,
        price: 303.54,
        quantity: 393,
        status: true
    }, {
        id: 90,
        name: 'Biturbo',
        category: 'Maserati',
        image: '../../images/products/product-6.jpg',
        added_date: '03/11/2019',
        rating: 5,
        price: 211.38,
        quantity: 120,
        status: false
    }, {
        id: 91,
        name: 'Dakota Club',
        category: 'Dodge',
        image: '../../images/products/product-1.jpg',
        added_date: '11/23/2018',
        rating: 4,
        price: 783.83,
        quantity: 461,
        status: false
    }, {
        id: 92,
        name: 'Mustang',
        category: 'Ford',
        image: '../../images/products/product-2.jpg',
        added_date: '06/13/2019',
        rating: 5,
        price: 612.92,
        quantity: 382,
        status: true
    }, {
        id: 93,
        name: 'Pilot',
        category: 'Honda',
        image: '../../images/products/product-3.jpg',
        added_date: '11/25/2018',
        rating: 5,
        price: 589.72,
        quantity: 246,
        status: false
    }, {
        id: 94,
        name: 'S80',
        category: 'Volvo',
        image: '../../images/products/product-4.jpg',
        added_date: '02/01/2019',
        rating: 2,
        price: 596.59,
        quantity: 325,
        status: false
    }, {
        id: 95,
        name: 'Grand Marquis',
        category: 'Mercury',
        image: '../../images/products/product-5.jpg',
        added_date: '01/28/2019',
        rating: 3,
        price: 102.64,
        quantity: 471,
        status: true
    }, {
        id: 96,
        name: 'S-Class',
        category: 'Mercedes-Benz',
        image: '../../images/products/product-6.jpg',
        added_date: '11/21/2018',
        rating: 3,
        price: 553.84,
        quantity: 178,
        status: false
    }, {
        id: 97,
        name: 'Freelander',
        category: 'Land Rover',
        image: '../../images/products/product-1.jpg',
        added_date: '09/13/2019',
        rating: 5,
        price: 682.82,
        quantity: 223,
        status: true
    }, {
        id: 98,
        name: 'Crossfire',
        category: 'Chrysler',
        image: '../../images/products/product-2.jpg',
        added_date: '06/26/2019',
        rating: 2,
        price: 696.41,
        quantity: 411,
        status: true
    }, {
        id: 99,
        name: 'Cabriolet',
        category: 'Volkswagen',
        image: '../../images/products/product-3.jpg',
        added_date: '01/11/2019',
        rating: 5,
        price: 667.44,
        quantity: 458,
        status: false
    }, {
        id: 100,
        name: 'Mustang',
        category: 'Ford',
        image: '../../images/products/product-4.jpg',
        added_date: '02/02/2019',
        rating: 3,
        price: 350.01,
        quantity: 295,
        status: false
    }],
      sort: true,
      pagination: {
        enabled: true,
        limit: 10,
        summary: true
      },
      search: {
        enabled: true
      },
      resizable: true,
      className: {
        table: 'table table-centered w-100 dt-responsive nowrap',
        thead: 'table-light',
        search: 'float-end'
      }

    }
  );

  grid.render(document.getElementById('products-datatable-wrapper'));

  document.querySelectorAll('.gridjs .gridjs-search .gridjs-search-input').forEach(function(e){
    e.classList.add('form-control');
    e.classList.remove('gridjs-input');
  });

  grid.on('ready',function(e){
    const checkboxPlugin = grid.config.plugin.get('myCheckbox');
    document.querySelectorAll('.gridjs .gridjs-wrapper .gridjs-table .gridjs-tbody .gridjs-tr .gridjs-td .gridjs-checkbox').forEach(function(e){
        e.classList.add('form-check-input');
      });
  });

  }
  

  init() {
    document.querySelectorAll('[data-toggle="select2"]').forEach(function(element) {
      new Choices(element,{
        itemSelectText:'',
      });
    });
    this.initProducts();


    

  }


    // table product formatter
  productDetailsFormatter(cell, row) {
    let productCell = `
    <img src="${row.cells[3].data}" alt="contact-img" title="contact-img" class="rounded me-3" height="48" />
    <p class='m-0 d-inline-block align-middle font-16'><a href="javascript:void(0)" class='product text-body' id="${row.cells[1].data}"> ${row.cells[2].data} </a><br />`
    for (let i = 0; i < 5; i++) {
      if (i < row.cells[4].data) {
        productCell += `<span class='text-warning mdi mdi-star'></span>`
      }
      else {
        productCell += `<span class='text-warning mdi mdi-star-outline'></span>`
      }
    }
    productCell = productCell + `</p>`

    return (html(productCell))
  }
  
  // table status cell formatter
  productStatusFormatter(cell, row){

    if (row.cells[9].data == true) {
      return (html(
        ` <span class="badge bg-success">Active</span>`
      ));
    }
    else {
      return (html(
        ` <span class="badge bg-danger">Deactive</span>`
      ));
    }

  }


  // table action cell formatter
  productActionFormatter(cell, row) {
    return (html(
      `<a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-eye"></i></a>
            <a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-square-edit-outline"></i></a>
            <a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-delete"></i></a>`
    ))
  }


}         

// init the dashboard
new EcommerceProduct().init();
