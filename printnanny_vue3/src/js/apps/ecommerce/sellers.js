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



class EcommerceSeller {

  constructor() {

    this.charts = [];


    this.chartOptions = {
      chart: {
        type: 'line',
        width: 80,
        height: 35,
        sparkline: {
          enabled: true
        }
      },
      series: [{ 'data': [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54] }],
      stroke: {
        width: 2,
        curve: 'smooth'
      },
      markers: {
        size: 0
      },
      colors: ["#727cf5"],
      tooltip: {
        fixed: {
          enabled: false
        },
        xaxis: {
          show: false
        },
        yaxis: {
          labels: {
            formatter: function (val) {
              return val + "k"
            }
          }

        },
        marker: {
          show: false
        }
      }
    };

      this.sellerList = [{
        id: 1,
        name: 'Vinnie Chicchelli',
        store: 'Caen',
        image: '../../images/users/avatar-1.jpg',
        products: 488,
        balance: '$106.27',
        created_on: '05/04/2019'
    }, {
        id: 2,
        name: 'Archibald Parades',
        store: 'Hengxi',
        image: '../../images/users/avatar-2.jpg',
        products: 51,
        balance: '$36319.37',
        created_on: '06/30/2019'
    }, {
        id: 3,
        name: 'Blair Root',
        store: 'Phu Luang',
        image: '../../images/users/avatar-3.jpg',
        products: 334,
        balance: '$11249.62',
        created_on: '11/28/2018'
    }, {
        id: 4,
        name: 'Mariel Savile',
        store: 'Rio das Pedras',
        image: '../../images/users/avatar-4.jpg',
        products: 10,
        balance: '$16584.31',
        created_on: '08/26/2019'
    }, {
        id: 5,
        name: 'Levon Cowthart',
        store: 'Jiaotang',
        image: '../../images/users/avatar-5.jpg',
        products: 151,
        balance: '$41178.37',
        created_on: '09/16/2019'
    }, {
        id: 6,
        name: 'Darnall Aisman',
        store: 'Kamuli',
        image: '../../images/users/avatar-6.jpg',
        products: 197,
        balance: '$11096.82',
        created_on: '01/11/2019'
    }, {
        id: 7,
        name: 'Fred Willicott',
        store: 'Zhavoronki',
        image: '../../images/users/avatar-7.jpg',
        products: 229,
        balance: '$7143.11',
        created_on: '06/07/2019'
    }, {
        id: 8,
        name: 'Jannelle Tuny',
        store: 'Lewoluo',
        image: '../../images/users/avatar-1.jpg',
        products: 432,
        balance: '$49819.50',
        created_on: '07/04/2019'
    }, {
        id: 9,
        name: 'Dominique Stathers',
        store: 'Vilarinho',
        image: '../../images/users/avatar-2.jpg',
        products: 170,
        balance: '$32533.98',
        created_on: '09/07/2019'
    }, {
        id: 10,
        name: 'Lilas Laytham',
        store: 'New Leyte',
        image: '../../images/users/avatar-3.jpg',
        products: 261,
        balance: '$1631.49',
        created_on: '10/24/2019'
    }, {
        id: 11,
        name: 'Cece McOmish',
        store: 'Toronto',
        image: '../../images/users/avatar-4.jpg',
        products: 195,
        balance: '$38287.45',
        created_on: '02/02/2019'
    }, {
        id: 12,
        name: 'Cordie Domenichini',
        store: 'Fier',
        image: '../../images/users/avatar-5.jpg',
        products: 47,
        balance: '$4046.11',
        created_on: '10/22/2019'
    }, {
        id: 13,
        name: 'Concettina Coite',
        store: 'Tibro',
        image: '../../images/users/avatar-6.jpg',
        products: 9,
        balance: '$8922.46',
        created_on: '01/21/2019'
    }, {
        id: 14,
        name: 'Martica Liffey',
        store: 'Mojkovac',
        image: '../../images/users/avatar-7.jpg',
        products: 386,
        balance: '$30648.35',
        created_on: '06/08/2019'
    }, {
        id: 15,
        name: 'Edna Posselwhite',
        store: 'Macklin',
        image: '../../images/users/avatar-1.jpg',
        products: 126,
        balance: '$41395.98',
        created_on: '06/30/2019'
    }, {
        id: 16,
        name: 'Keelia Hulkes',
        store: 'Chicago',
        image: '../../images/users/avatar-2.jpg',
        products: 343,
        balance: '$20206.14',
        created_on: '11/22/2018'
    }, {
        id: 17,
        name: 'Jeanette Gehringer',
        store: 'Cergy-Pontoise',
        image: '../../images/users/avatar-3.jpg',
        products: 289,
        balance: '$16531.59',
        created_on: '07/16/2019'
    }, {
        id: 18,
        name: 'Steffane Spellissy',
        store: 'Valera',
        image: '../../images/users/avatar-4.jpg',
        products: 179,
        balance: '$11265.30',
        created_on: '08/15/2019'
    }, {
        id: 19,
        name: 'Delcine Cassin',
        store: 'Ferme-Neuve',
        image: '../../images/users/avatar-5.jpg',
        products: 380,
        balance: '$48892.20',
        created_on: '01/20/2019'
    }, {
        id: 20,
        name: 'Bibbie Francescuccio',
        store: 'Mosjøen',
        image: '../../images/users/avatar-6.jpg',
        products: 119,
        balance: '$48382.04',
        created_on: '08/01/2019'
    }, {
        id: 21,
        name: 'Reece Gergler',
        store: 'Naguilian',
        image: '../../images/users/avatar-7.jpg',
        products: 17,
        balance: '$9834.61',
        created_on: '07/08/2019'
    }, {
        id: 22,
        name: 'Felic Gilluley',
        store: 'Neietsu',
        image: '../../images/users/avatar-1.jpg',
        products: 198,
        balance: '$43234.51',
        created_on: '01/18/2019'
    }, {
        id: 23,
        name: 'Jemie Mannooch',
        store: 'Banjarsari',
        image: '../../images/users/avatar-2.jpg',
        products: 105,
        balance: '$21347.58',
        created_on: '10/15/2019'
    }, {
        id: 24,
        name: 'Manny Beaze',
        store: 'Rokiciny',
        image: '../../images/users/avatar-3.jpg',
        products: 246,
        balance: '$9881.89',
        created_on: '01/27/2019'
    }, {
        id: 25,
        name: 'Rubetta Maliphant',
        store: 'Jiaoxie',
        image: '../../images/users/avatar-4.jpg',
        products: 479,
        balance: '$7622.76',
        created_on: '11/11/2018'
    }, {
        id: 26,
        name: 'Dwight Pinnocke',
        store: 'Las Palmas',
        image: '../../images/users/avatar-5.jpg',
        products: 83,
        balance: '$32601.27',
        created_on: '03/24/2019'
    }, {
        id: 27,
        name: 'Wilburt Anyon',
        store: 'Dogonbadan',
        image: '../../images/users/avatar-6.jpg',
        products: 244,
        balance: '$29719.61',
        created_on: '02/14/2019'
    }, {
        id: 28,
        name: 'Dud Deville',
        store: 'Pewel Wielka',
        image: '../../images/users/avatar-7.jpg',
        products: 87,
        balance: '$514.77',
        created_on: '07/22/2019'
    }, {
        id: 29,
        name: 'Alyssa Chalcot',
        store: 'Morohongō',
        image: '../../images/users/avatar-1.jpg',
        products: 111,
        balance: '$7191.85',
        created_on: '03/08/2019'
    }, {
        id: 30,
        name: 'Gawen Placido',
        store: 'Rauco',
        image: '../../images/users/avatar-2.jpg',
        products: 67,
        balance: '$31573.89',
        created_on: '01/21/2019'
    }, {
        id: 31,
        name: 'Gallagher Treweke',
        store: 'Ożarowice',
        image: '../../images/users/avatar-3.jpg',
        products: 91,
        balance: '$21165.83',
        created_on: '06/05/2019'
    }, {
        id: 32,
        name: 'Noelyn Jaulme',
        store: 'Kuršėnai',
        image: '../../images/users/avatar-4.jpg',
        products: 142,
        balance: '$27699.47',
        created_on: '07/01/2019'
    }, {
        id: 33,
        name: 'Neill MacAllester',
        store: 'Hua Sai',
        image: '../../images/users/avatar-5.jpg',
        products: 276,
        balance: '$25345.41',
        created_on: '11/24/2018'
    }, {
        id: 34,
        name: 'Ham Cocklie',
        store: 'Melgar',
        image: '../../images/users/avatar-6.jpg',
        products: 110,
        balance: '$17457.62',
        created_on: '05/31/2019'
    }, {
        id: 35,
        name: 'Brok Bielfelt',
        store: 'Jinshi',
        image: '../../images/users/avatar-7.jpg',
        products: 253,
        balance: '$20281.53',
        created_on: '05/21/2019'
    }, {
        id: 36,
        name: 'Dasha Kirsche',
        store: 'Zhangjiabao',
        image: '../../images/users/avatar-1.jpg',
        products: 482,
        balance: '$44406.71',
        created_on: '09/25/2019'
    }, {
        id: 37,
        name: 'Bobine MacLoughlin',
        store: 'Pomiechówek',
        image: '../../images/users/avatar-2.jpg',
        products: 160,
        balance: '$32807.95',
        created_on: '05/24/2019'
    }, {
        id: 38,
        name: 'Shepperd Wallwork',
        store: 'Barretos',
        image: '../../images/users/avatar-3.jpg',
        products: 352,
        balance: '$40525.09',
        created_on: '04/02/2019'
    }, {
        id: 39,
        name: 'Poppy Ismail',
        store: 'Dapdap',
        image: '../../images/users/avatar-4.jpg',
        products: 374,
        balance: '$12504.53',
        created_on: '12/31/2018'
    }, {
        id: 40,
        name: 'Alethea Sowerby',
        store: 'Jinshiqiao',
        image: '../../images/users/avatar-5.jpg',
        products: 34,
        balance: '$7362.71',
        created_on: '08/06/2019'
    }, {
        id: 41,
        name: 'Rosalinde Deabill',
        store: '‘Ayn al Bayḑā',
        image: '../../images/users/avatar-6.jpg',
        products: 317,
        balance: '$18495.19',
        created_on: '09/22/2019'
    }, {
        id: 42,
        name: 'Alano Klezmski',
        store: 'Donegal',
        image: '../../images/users/avatar-7.jpg',
        products: 379,
        balance: '$9207.95',
        created_on: '02/21/2019'
    }, {
        id: 43,
        name: 'Ennis Pennino',
        store: 'Tucupita',
        image: '../../images/users/avatar-1.jpg',
        products: 432,
        balance: '$10264.67',
        created_on: '01/09/2019'
    }, {
        id: 44,
        name: 'Chrissy Spellward',
        store: 'Chợ Chu',
        image: '../../images/users/avatar-2.jpg',
        products: 239,
        balance: '$22731.79',
        created_on: '08/18/2019'
    }, {
        id: 45,
        name: 'Emlen Catley',
        store: 'Heku',
        image: '../../images/users/avatar-3.jpg',
        products: 442,
        balance: '$41308.68',
        created_on: '01/22/2019'
    }, {
        id: 46,
        name: 'Sorcha Penritt',
        store: 'Bingerville',
        image: '../../images/users/avatar-4.jpg',
        products: 102,
        balance: '$47673.61',
        created_on: '08/08/2019'
    }, {
        id: 47,
        name: 'Ricoriki Fulham',
        store: 'Estacion',
        image: '../../images/users/avatar-5.jpg',
        products: 482,
        balance: '$42290.23',
        created_on: '06/25/2019'
    }, {
        id: 48,
        name: 'Shena Eldred',
        store: 'Qinlan',
        image: '../../images/users/avatar-6.jpg',
        products: 497,
        balance: '$18412.54',
        created_on: '04/04/2019'
    }, {
        id: 49,
        name: 'Lothaire Tingey',
        store: 'Swedru',
        image: '../../images/users/avatar-7.jpg',
        products: 336,
        balance: '$24256.62',
        created_on: '10/29/2019'
    }, {
        id: 50,
        name: 'Adella Ryce',
        store: 'Sapporo',
        image: '../../images/users/avatar-1.jpg',
        products: 6,
        balance: '$33336.89',
        created_on: '01/24/2019'
    }, {
        id: 51,
        name: 'Alina McAloren',
        store: 'Trà Vinh',
        image: '../../images/users/avatar-2.jpg',
        products: 169,
        balance: '$27512.74',
        created_on: '09/09/2019'
    }, {
        id: 52,
        name: 'Danni Hawkins',
        store: 'Jianggao',
        image: '../../images/users/avatar-3.jpg',
        products: 336,
        balance: '$11481.46',
        created_on: '05/16/2019'
    }, {
        id: 53,
        name: 'Bealle Mulvihill',
        store: 'Peishe',
        image: '../../images/users/avatar-4.jpg',
        products: 61,
        balance: '$6137.15',
        created_on: '10/24/2019'
    }, {
        id: 54,
        name: 'Danita Autin',
        store: 'Pirapora do Bom Jesus',
        image: '../../images/users/avatar-5.jpg',
        products: 85,
        balance: '$30630.99',
        created_on: '06/20/2019'
    }, {
        id: 55,
        name: 'Valina Ewbanks',
        store: 'Tamberías',
        image: '../../images/users/avatar-6.jpg',
        products: 222,
        balance: '$14141.87',
        created_on: '07/29/2019'
    }, {
        id: 56,
        name: 'Lian Kinnock',
        store: 'Nāḩiyat as Sab‘ Biyār',
        image: '../../images/users/avatar-7.jpg',
        products: 223,
        balance: '$38191.21',
        created_on: '02/06/2019'
    }, {
        id: 57,
        name: 'Jordain Spadotto',
        store: 'Mashava',
        image: '../../images/users/avatar-1.jpg',
        products: 368,
        balance: '$22344.55',
        created_on: '10/08/2019'
    }, {
        id: 58,
        name: 'Gay Ledley',
        store: 'Potosí',
        image: '../../images/users/avatar-2.jpg',
        products: 58,
        balance: '$3176.67',
        created_on: '02/24/2019'
    }, {
        id: 59,
        name: 'Emanuele Pendrick',
        store: 'Al ‘Āqir',
        image: '../../images/users/avatar-3.jpg',
        products: 299,
        balance: '$8013.45',
        created_on: '04/21/2019'
    }, {
        id: 60,
        name: 'Gabi Smythe',
        store: 'Ambarakaraka',
        image: '../../images/users/avatar-4.jpg',
        products: 215,
        balance: '$22216.80',
        created_on: '10/11/2019'
    }, {
        id: 61,
        name: 'Rick Szepe',
        store: 'Pawitan',
        image: '../../images/users/avatar-5.jpg',
        products: 335,
        balance: '$12939.27',
        created_on: '02/10/2019'
    }, {
        id: 62,
        name: 'Oralle Yakubovics',
        store: 'Sfax',
        image: '../../images/users/avatar-6.jpg',
        products: 421,
        balance: '$22661.70',
        created_on: '08/30/2019'
    }, {
        id: 63,
        name: 'Rainer Sapey',
        store: 'Spanish Town',
        image: '../../images/users/avatar-7.jpg',
        products: 363,
        balance: '$11556.22',
        created_on: '12/11/2018'
    }, {
        id: 64,
        name: 'Malorie Nyland',
        store: 'Baltimore',
        image: '../../images/users/avatar-1.jpg',
        products: 385,
        balance: '$14001.56',
        created_on: '12/01/2018'
    }, {
        id: 65,
        name: 'Madelin Mathiot',
        store: 'Chiryū',
        image: '../../images/users/avatar-2.jpg',
        products: 176,
        balance: '$8423.75',
        created_on: '04/27/2019'
    }, {
        id: 66,
        name: 'Wynn De Hooge',
        store: 'Guyam Malaki',
        image: '../../images/users/avatar-3.jpg',
        products: 49,
        balance: '$379.46',
        created_on: '04/27/2019'
    }, {
        id: 67,
        name: 'Theodora Muggleton',
        store: 'Ban Khlong Bang Sao Thong',
        image: '../../images/users/avatar-4.jpg',
        products: 119,
        balance: '$23141.75',
        created_on: '02/18/2019'
    }, {
        id: 68,
        name: 'Arther Rhubottom',
        store: 'Gorno Orizari',
        image: '../../images/users/avatar-5.jpg',
        products: 411,
        balance: '$1290.09',
        created_on: '06/08/2019'
    }, {
        id: 69,
        name: 'Phillipp Fayne',
        store: 'Yeoju',
        image: '../../images/users/avatar-6.jpg',
        products: 112,
        balance: '$8829.23',
        created_on: '06/14/2019'
    }, {
        id: 70,
        name: 'Reinaldos Mompesson',
        store: 'El Paso',
        image: '../../images/users/avatar-7.jpg',
        products: 187,
        balance: '$7242.50',
        created_on: '07/12/2019'
    }, {
        id: 71,
        name: 'Laverna Devin',
        store: 'Tacuatí',
        image: '../../images/users/avatar-1.jpg',
        products: 320,
        balance: '$6686.58',
        created_on: '03/23/2019'
    }, {
        id: 72,
        name: 'Odo Braga',
        store: 'Xiaxindian',
        image: '../../images/users/avatar-2.jpg',
        products: 51,
        balance: '$43377.42',
        created_on: '07/21/2019'
    }, {
        id: 73,
        name: 'Meggi Gooddy',
        store: 'Panjakent',
        image: '../../images/users/avatar-3.jpg',
        products: 422,
        balance: '$33905.80',
        created_on: '04/16/2019'
    }, {
        id: 74,
        name: 'Shaina Simonnet',
        store: 'Shuangfeng',
        image: '../../images/users/avatar-4.jpg',
        products: 56,
        balance: '$17015.70',
        created_on: '02/28/2019'
    }, {
        id: 75,
        name: 'Hobie Tiffney',
        store: 'Pajala',
        image: '../../images/users/avatar-5.jpg',
        products: 469,
        balance: '$13849.40',
        created_on: '02/18/2019'
    }, {
        id: 76,
        name: 'Matthus Witherspoon',
        store: 'Gabès',
        image: '../../images/users/avatar-6.jpg',
        products: 279,
        balance: '$31329.87',
        created_on: '06/15/2019'
    }, {
        id: 77,
        name: 'Marnie Mattholie',
        store: 'San Francisco',
        image: '../../images/users/avatar-7.jpg',
        products: 88,
        balance: '$20153.32',
        created_on: '11/18/2018'
    }, {
        id: 78,
        name: 'Davine Stollmeier',
        store: 'Sujji',
        image: '../../images/users/avatar-1.jpg',
        products: 408,
        balance: '$46816.18',
        created_on: '07/13/2019'
    }, {
        id: 79,
        name: 'Kimbell Shellsheere',
        store: 'Loja',
        image: '../../images/users/avatar-2.jpg',
        products: 329,
        balance: '$27092.48',
        created_on: '05/03/2019'
    }, {
        id: 80,
        name: 'Berny Humber',
        store: 'Parlilitan',
        image: '../../images/users/avatar-3.jpg',
        products: 89,
        balance: '$32861.20',
        created_on: '03/03/2019'
    }, {
        id: 81,
        name: 'Marrilee Bellie',
        store: 'Batang',
        image: '../../images/users/avatar-4.jpg',
        products: 473,
        balance: '$44680.73',
        created_on: '09/03/2019'
    }, {
        id: 82,
        name: 'Roanne Kenworthy',
        store: 'Maqiu',
        image: '../../images/users/avatar-5.jpg',
        products: 349,
        balance: '$13035.80',
        created_on: '05/28/2019'
    }, {
        id: 83,
        name: 'Heall Bellow',
        store: 'Portel',
        image: '../../images/users/avatar-6.jpg',
        products: 444,
        balance: '$12853.04',
        created_on: '08/11/2019'
    }, {
        id: 84,
        name: 'Abigael Kollas',
        store: 'Ban Mai',
        image: '../../images/users/avatar-7.jpg',
        products: 342,
        balance: '$37565.22',
        created_on: '08/08/2019'
    }, {
        id: 85,
        name: 'Glyn O\'Hengerty',
        store: 'Makapanstad',
        image: '../../images/users/avatar-1.jpg',
        products: 430,
        balance: '$35812.35',
        created_on: '07/01/2019'
    }, {
        id: 86,
        name: 'Elfrida MacLese',
        store: 'Tembilahan',
        image: '../../images/users/avatar-2.jpg',
        products: 185,
        balance: '$44116.11',
        created_on: '12/14/2018'
    }, {
        id: 87,
        name: 'Hamish Rowledge',
        store: 'Kumlinge',
        image: '../../images/users/avatar-3.jpg',
        products: 182,
        balance: '$24597.03',
        created_on: '01/22/2019'
    }, {
        id: 88,
        name: 'Lurleen Hatchman',
        store: 'Carcassonne',
        image: '../../images/users/avatar-4.jpg',
        products: 180,
        balance: '$6133.40',
        created_on: '01/02/2019'
    }, {
        id: 89,
        name: 'Ryley Yedy',
        store: 'Mişrātah',
        image: '../../images/users/avatar-5.jpg',
        products: 225,
        balance: '$47877.45',
        created_on: '03/26/2019'
    }, {
        id: 90,
        name: 'Reggie Jollands',
        store: 'Annecy',
        image: '../../images/users/avatar-6.jpg',
        products: 340,
        balance: '$49164.92',
        created_on: '05/05/2019'
    }, {
        id: 91,
        name: 'Joelly Binns',
        store: 'Kokas',
        image: '../../images/users/avatar-7.jpg',
        products: 240,
        balance: '$30363.88',
        created_on: '08/11/2019'
    }, {
        id: 92,
        name: 'Geri Dignon',
        store: 'Hrtkovci',
        image: '../../images/users/avatar-1.jpg',
        products: 500,
        balance: '$29636.97',
        created_on: '06/16/2019'
    }, {
        id: 93,
        name: 'Kate Gautrey',
        store: 'Winburg',
        image: '../../images/users/avatar-2.jpg',
        products: 396,
        balance: '$9282.90',
        created_on: '11/28/2018'
    }, {
        id: 94,
        name: 'Redford Pautot',
        store: 'Ciganaria',
        image: '../../images/users/avatar-3.jpg',
        products: 219,
        balance: '$28715.97',
        created_on: '01/26/2019'
    }, {
        id: 95,
        name: 'Townie Camamill',
        store: 'Pekuwon',
        image: '../../images/users/avatar-4.jpg',
        products: 55,
        balance: '$38802.54',
        created_on: '06/01/2019'
    }, {
        id: 96,
        name: 'Nancey Capun',
        store: 'Toritama',
        image: '../../images/users/avatar-5.jpg',
        products: 176,
        balance: '$21427.41',
        created_on: '02/25/2019'
    }, {
        id: 97,
        name: 'Garrard Arstingall',
        store: 'Telč',
        image: '../../images/users/avatar-6.jpg',
        products: 309,
        balance: '$46545.94',
        created_on: '04/12/2019'
    }, {
        id: 98,
        name: 'Pren Braznell',
        store: 'Socorro',
        image: '../../images/users/avatar-7.jpg',
        products: 387,
        balance: '$25288.73',
        created_on: '09/17/2019'
    }, {
        id: 99,
        name: 'Stafford Harragin',
        store: 'Paihia',
        image: '../../images/users/avatar-1.jpg',
        products: 339,
        balance: '$21184.13',
        created_on: '04/16/2019'
    }, {
        id: 100,
        name: 'Fleming Rucklesse',
        store: 'Ad Dīwānīyah',
        image: '../../images/users/avatar-2.jpg',
        products: 289,
        balance: '$46811.38',
        created_on: '07/21/2019'
    }];
  }

  initProducts(){
    
    const self = this;


  var grid = new Grid(
    {
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
          sort: false
        },
        {
          id: 'name',
          name: 'Seller',
          formatter: this.sellerNameFormatter.bind(this)
        },
        {
          id: 'image',
          name: 'Image',
          hidden: true
        },
        {
          id: 'store',
          name: 'Store',
          // formatter: this.orderDateFormatter.bind(this)
        },
        {
          id: 'product',
          name: 'Product',
        },
        {
          id: 'balance',
          name: 'Balance',
          // formatter: this.ordePaymentStatusFormatter.bind(this)
        },
        {
          id: 'created_on',
          name: 'Created On'
        },
        {
          id: 'Revenu',
          name: 'Revenue',
          sort: false,
          formatter: this.sellerChartFormatter.bind(this)
        },
        {
          name: 'Action',
          sort: false,
          formatter: this.sellerActionFormatter.bind(this)
        }],
      search: true,
      sort: true,
      pagination: {
        enabled: true,
        limit: this.pageSize
      },
      data: this.sellerList.map((seller) => {
        return {
          id: seller.id,
          name: seller.name,
          store: seller.store,
          product: seller.products,
          balance: seller.balance,
          created_on: seller.created_on,
          image: seller.image
        }
      }),
      className: {
        table: 'table table-centered w-100  nowrap',
        thead: 'table-light',
        search: 'float-end'
      }
    }
  );

  grid.render(document.getElementById('sellers-datatable-wrapper'));

  document.querySelectorAll('.gridjs .gridjs-search .gridjs-search-input').forEach(function(e){
    e.classList.add('form-control');
    e.classList.remove('gridjs-input');
  });

  grid.on('ready',function(e){
  
    const checkboxPlugin = grid.config.plugin.get('myCheckbox');
    document.querySelectorAll('.gridjs .gridjs-wrapper .gridjs-table .gridjs-tbody .gridjs-tr .gridjs-td .gridjs-checkbox').forEach(function(e){
        e.classList.add('form-check-input');
      });


      for (var idx=0; idx<self.charts.length;idx++) {
        try { self.charts[idx].destroy(); } catch (e) {};
      }
      
      self.charts = [];
      

      document.querySelectorAll(".spark-chart").forEach(function (element) {
    
        var d = [];
        for (var idx = 0; idx < 10; idx++) {
            d.push(Math.floor(Math.random() * 90) + 10);
        }
        self.chartOptions['series'] = [{ 'data': d }];
  
        var chart = new ApexCharts(element, self.chartOptions);
        self.charts.push(chart);
        chart.render();
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


  sellerNameFormatter(cell, row) {
    return (html(
      `
      <div class="table-user">
      <img src="${row.cells[2].data}" alt="table-user" class="me-2 rounded-circle">
       <a href="javascript:void(0);" class="text-body fw-semibold">${row.cells[1].data}</a>
       </div>
      `
    ));
  }


  // action cell formatter
  sellerActionFormatter(cell, row) {
    return (html(
      `<a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-square-edit-outline"></i></a>
           <a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-delete"></i></a>`
    ))
  }

  // chart cell formatter
  sellerChartFormatter(cell, row) {

 

    //<div class="spark-chart" data-dataset="[31,47,34,15,28,36,48,33,75,57]"></div>
    //<div class="spark-chart" data-dataset="[25, 66, 41, 34, 63, 25, 34, 12, 434, 9, 54]"></div>

    return (html(
      `<div class="spark-chart"></div>`
    ));
  }


}         

// init the dashboard
new EcommerceSeller().init();
