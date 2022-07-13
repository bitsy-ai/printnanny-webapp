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



class EcommerceOrder {

  constructor() {
      this.orderList = [
        {
            id: 1,
            order_id: '31',
            order_date: '23-May-2019',
            order_time: '1:45 PM',
            payment_status: 'Payment Failed',
            total: '$8361.93',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 2,
            order_id: '060',
            order_date: '01-Feb-2019',
            order_time: '12:10 PM',
            payment_status: 'Unpaid',
            total: '$6219.67',
            payment_method: 'Credit Card',
            order_status: 'Shipped',
        },
        {
            id: 3,
            order_id: '76961',
            order_date: '13-Mar-2019',
            order_time: '2:53 AM',
            payment_status: 'Payment Failed',
            total: '$6695.83',
            payment_method: 'Paypal',
            order_status: 'Shipped',
        },
        {
            id: 4,
            order_id: '59',
            order_date: '02-Feb-2019',
            order_time: '2:53 AM',
            payment_status: 'Paid',
            total: '$8616.73',
            payment_method: 'Visa',
            order_status: 'Delivered',
        },
        {
            id: 5,
            order_id: '93',
            order_date: '15-May-2019',
            order_time: '1:52 PM',
            payment_status: 'Awaiting Authorization',
            total: '$1808.61',
            payment_method: 'Paypal',
            order_status: 'Shipped',
        },
        {
            id: 6,
            order_id: '2164',
            order_date: '22-Feb-2019',
            order_time: '3:59 AM',
            payment_status: 'Paid',
            total: '$9813.57',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 7,
            order_id: '22410',
            order_date: '16-Jan-2019',
            order_time: '7:29 AM',
            payment_status: 'Awaiting Authorization',
            total: '$9457.23',
            payment_method: 'Mastercard',
            order_status: 'Delivered',
        },
        {
            id: 8,
            order_id: '04260',
            order_date: '06-Feb-2019',
            order_time: '5:14 AM',
            payment_status: 'Unpaid',
            total: '$1054.76',
            payment_method: 'Payoneer',
            order_status: 'Processing',
        },
        {
            id: 9,
            order_id: '77',
            order_date: '18-Jan-2019',
            order_time: '9:34 AM',
            payment_status: 'Payment Failed',
            total: '$3526.87',
            payment_method: 'Payoneer',
            order_status: 'Shipped',
        },
        {
            id: 10,
            order_id: '938',
            order_date: '27-Apr-2019',
            order_time: '6:16 PM',
            payment_status: 'Paid',
            total: '$8201.67',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 11,
            order_id: '99',
            order_date: '03-Mar-2019',
            order_time: '11:23 PM',
            payment_status: 'Payment Failed',
            total: '$9557.76',
            payment_method: 'Paypal',
            order_status: 'Processing',
        },
        {
            id: 12,
            order_id: '397',
            order_date: '12-May-2019',
            order_time: '11:18 PM',
            payment_status: 'Unpaid',
            total: '$8391.95',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 13,
            order_id: '4874',
            order_date: '01-Jan-2019',
            order_time: '2:15 PM',
            payment_status: 'Unpaid',
            total: '$3558.36',
            payment_method: 'Paypal',
            order_status: 'Cancelled',
        },
        {
            id: 14,
            order_id: '496',
            order_date: '17-Apr-2019',
            order_time: '7:56 PM',
            payment_status: 'Payment Failed',
            total: '$2871.99',
            payment_method: 'Credit Card',
            order_status: 'Delivered',
        },
        {
            id: 15,
            order_id: '982',
            order_date: '07-May-2019',
            order_time: '7:54 PM',
            payment_status: 'Awaiting Authorization',
            total: '$415.59',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 16,
            order_id: '66303',
            order_date: '14-Mar-2019',
            order_time: '10:47 AM',
            payment_status: 'Paid',
            total: '$9554.21',
            payment_method: 'Credit Card',
            order_status: 'Shipped',
        },
        {
            id: 17,
            order_id: '73',
            order_date: '20-Feb-2019',
            order_time: '4:24 PM',
            payment_status: 'Payment Failed',
            total: '$9766.71',
            payment_method: 'Mastercard',
            order_status: 'Delivered',
        },
        {
            id: 18,
            order_id: '90804',
            order_date: '03-Jun-2019',
            order_time: '5:42 PM',
            payment_status: 'Payment Failed',
            total: '$1194.25',
            payment_method: 'Mastercard',
            order_status: 'Cancelled',
        },
        {
            id: 19,
            order_id: '97489',
            order_date: '09-May-2019',
            order_time: '11:47 PM',
            payment_status: 'Paid',
            total: '$8715.09',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 20,
            order_id: '53577',
            order_date: '14-Jun-2019',
            order_time: '8:47 PM',
            payment_status: 'Unpaid',
            total: '$2836.42',
            payment_method: 'Mastercard',
            order_status: 'Delivered',
        },
        {
            id: 21,
            order_id: '8940',
            order_date: '08-Jun-2019',
            order_time: '6:14 PM',
            payment_status: 'Paid',
            total: '$3552.93',
            payment_method: 'Credit Card',
            order_status: 'Delivered',
        },
        {
            id: 22,
            order_id: '34334',
            order_date: '20-Apr-2019',
            order_time: '7:19 PM',
            payment_status: 'Payment Failed',
            total: '$7487.68',
            payment_method: 'Payoneer',
            order_status: 'Delivered',
        },
        {
            id: 23,
            order_id: '2',
            order_date: '07-Jan-2019',
            order_time: '4:29 AM',
            payment_status: 'Paid',
            total: '$2900.64',
            payment_method: 'Mastercard',
            order_status: 'Delivered',
        },
        {
            id: 24,
            order_id: '478',
            order_date: '19-Jun-2019',
            order_time: '9:29 AM',
            payment_status: 'Unpaid',
            total: '$7589.76',
            payment_method: 'Visa',
            order_status: 'Delivered',
        },
        {
            id: 25,
            order_id: '95',
            order_date: '30-Mar-2019',
            order_time: '9:47 AM',
            payment_status: 'Unpaid',
            total: '$3774.83',
            payment_method: 'Mastercard',
            order_status: 'Delivered',
        },
        {
            id: 26,
            order_id: '160',
            order_date: '05-Jun-2019',
            order_time: '1:39 PM',
            payment_status: 'Paid',
            total: '$2696.43',
            payment_method: 'Paypal',
            order_status: 'Cancelled',
        },
        {
            id: 27,
            order_id: '81338',
            order_date: '19-Jun-2019',
            order_time: '4:59 PM',
            payment_status: 'Unpaid',
            total: '$4720.65',
            payment_method: 'Credit Card',
            order_status: 'Processing',
        },
        {
            id: 28,
            order_id: '75',
            order_date: '31-Jan-2019',
            order_time: '10:24 AM',
            payment_status: 'Unpaid',
            total: '$7674.74',
            payment_method: 'Visa',
            order_status: 'Delivered',
        },
        {
            id: 29,
            order_id: '8',
            order_date: '16-Feb-2019',
            order_time: '5:08 AM',
            payment_status: 'Paid',
            total: '$2399.90',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 30,
            order_id: '99',
            order_date: '19-Jun-2019',
            order_time: '1:33 AM',
            payment_status: 'Payment Failed',
            total: '$2471.31',
            payment_method: 'Visa',
            order_status: 'Cancelled',
        },
        {
            id: 31,
            order_id: '976',
            order_date: '17-Jun-2019',
            order_time: '8:21 AM',
            payment_status: 'Unpaid',
            total: '$8073.28',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 32,
            order_id: '13',
            order_date: '17-Feb-2019',
            order_time: '5:41 AM',
            payment_status: 'Unpaid',
            total: '$4393.62',
            payment_method: 'Payoneer',
            order_status: 'Cancelled',
        },
        {
            id: 33,
            order_id: '8333',
            order_date: '14-Feb-2019',
            order_time: '4:42 AM',
            payment_status: 'Paid',
            total: '$6077.15',
            payment_method: 'Paypal',
            order_status: 'Cancelled',
        },
        {
            id: 34,
            order_id: '21547',
            order_date: '22-Jul-2019',
            order_time: '8:42 PM',
            payment_status: 'Unpaid',
            total: '$5792.53',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 35,
            order_id: '25',
            order_date: '11-Jul-2019',
            order_time: '10:38 PM',
            payment_status: 'Payment Failed',
            total: '$8661.65',
            payment_method: 'Credit Card',
            order_status: 'Cancelled',
        },
        {
            id: 36,
            order_id: '3201',
            order_date: '13-Jun-2019',
            order_time: '9:57 PM',
            payment_status: 'Payment Failed',
            total: '$7795.53',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 37,
            order_id: '797',
            order_date: '09-Mar-2019',
            order_time: '9:53 PM',
            payment_status: 'Paid',
            total: '$9755.20',
            payment_method: 'Mastercard',
            order_status: 'Cancelled',
        },
        {
            id: 38,
            order_id: '7078',
            order_date: '04-Jul-2019',
            order_time: '9:09 AM',
            payment_status: 'Unpaid',
            total: '$2335.70',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 39,
            order_id: '4380',
            order_date: '11-Apr-2019',
            order_time: '5:33 AM',
            payment_status: 'Awaiting Authorization',
            total: '$1342.74',
            payment_method: 'Paypal',
            order_status: 'Shipped',
        },
        {
            id: 40,
            order_id: '4',
            order_date: '23-May-2019',
            order_time: '11:35 AM',
            payment_status: 'Paid',
            total: '$626.28',
            payment_method: 'Payoneer',
            order_status: 'Delivered',
        },
        {
            id: 41,
            order_id: '54',
            order_date: '11-Apr-2019',
            order_time: '1:51 AM',
            payment_status: 'Unpaid',
            total: '$1903.55',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 42,
            order_id: '6084',
            order_date: '01-Jan-2019',
            order_time: '11:08 AM',
            payment_status: 'Unpaid',
            total: '$1671.64',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 43,
            order_id: '7004',
            order_date: '12-Mar-2019',
            order_time: '6:18 AM',
            payment_status: 'Payment Failed',
            total: '$7471.41',
            payment_method: 'Payoneer',
            order_status: 'Shipped',
        },
        {
            id: 44,
            order_id: '00890',
            order_date: '10-Jan-2019',
            order_time: '5:36 AM',
            payment_status: 'Payment Failed',
            total: '$7395.11',
            payment_method: 'Paypal',
            order_status: 'Processing',
        },
        {
            id: 45,
            order_id: '60931',
            order_date: '27-Jan-2019',
            order_time: '11:31 PM',
            payment_status: 'Awaiting Authorization',
            total: '$4022.17',
            payment_method: 'Payoneer',
            order_status: 'Delivered',
        },
        {
            id: 46,
            order_id: '2',
            order_date: '12-Jan-2019',
            order_time: '1:01 PM',
            payment_status: 'Payment Failed',
            total: '$7455.30',
            payment_method: 'Payoneer',
            order_status: 'Shipped',
        },
        {
            id: 47,
            order_id: '92',
            order_date: '20-Jul-2019',
            order_time: '2:48 PM',
            payment_status: 'Unpaid',
            total: '$192.21',
            payment_method: 'Visa',
            order_status: 'Delivered',
        },
        {
            id: 48,
            order_id: '937',
            order_date: '05-Apr-2019',
            order_time: '6:06 PM',
            payment_status: 'Payment Failed',
            total: '$4070.53',
            payment_method: 'Visa',
            order_status: 'Shipped',
        },
        {
            id: 49,
            order_id: '3474',
            order_date: '27-Jan-2019',
            order_time: '8:18 PM',
            payment_status: 'Unpaid',
            total: '$2957.29',
            payment_method: 'Visa',
            order_status: 'Cancelled',
        },
        {
            id: 50,
            order_id: '1419',
            order_date: '10-Feb-2019',
            order_time: '12:58 AM',
            payment_status: 'Unpaid',
            total: '$8052.46',
            payment_method: 'Mastercard',
            order_status: 'Shipped',
        },
        {
            id: 51,
            order_id: '763',
            order_date: '16-Feb-2019',
            order_time: '5:36 AM',
            payment_status: 'Unpaid',
            total: '$1424.77',
            payment_method: 'Visa',
            order_status: 'Delivered',
        },
        {
            id: 52,
            order_id: '2',
            order_date: '12-May-2019',
            order_time: '8:32 PM',
            payment_status: 'Unpaid',
            total: '$2126.47',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 53,
            order_id: '06',
            order_date: '07-Mar-2019',
            order_time: '3:10 AM',
            payment_status: 'Payment Failed',
            total: '$3626.53',
            payment_method: 'Paypal',
            order_status: 'Cancelled',
        },
        {
            id: 54,
            order_id: '29608',
            order_date: '18-Jul-2019',
            order_time: '10:03 PM',
            payment_status: 'Awaiting Authorization',
            total: '$4291.42',
            payment_method: 'Mastercard',
            order_status: 'Cancelled',
        },
        {
            id: 55,
            order_id: '109',
            order_date: '05-Apr-2019',
            order_time: '8:14 AM',
            payment_status: 'Paid',
            total: '$417.32',
            payment_method: 'Mastercard',
            order_status: 'Cancelled',
        },
        {
            id: 56,
            order_id: '700',
            order_date: '08-Apr-2019',
            order_time: '9:49 AM',
            payment_status: 'Payment Failed',
            total: '$1046.92',
            payment_method: 'Visa',
            order_status: 'Cancelled',
        },
        {
            id: 57,
            order_id: '59297',
            order_date: '06-Feb-2019',
            order_time: '8:49 PM',
            payment_status: 'Paid',
            total: '$8722.68',
            payment_method: 'Credit Card',
            order_status: 'Shipped',
        },
        {
            id: 58,
            order_id: '74',
            order_date: '02-Feb-2019',
            order_time: '10:59 PM',
            payment_status: 'Payment Failed',
            total: '$9032.25',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 59,
            order_id: '2',
            order_date: '08-Jun-2019',
            order_time: '10:38 PM',
            payment_status: 'Unpaid',
            total: '$6220.01',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 60,
            order_id: '1375',
            order_date: '12-Jan-2019',
            order_time: '4:07 PM',
            payment_status: 'Unpaid',
            total: '$8482.80',
            payment_method: 'Credit Card',
            order_status: 'Delivered',
        },
        {
            id: 61,
            order_id: '65',
            order_date: '26-Jan-2019',
            order_time: '3:23 PM',
            payment_status: 'Awaiting Authorization',
            total: '$1429.24',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 62,
            order_id: '6158',
            order_date: '24-Jan-2019',
            order_time: '4:33 PM',
            payment_status: 'Awaiting Authorization',
            total: '$6894.72',
            payment_method: 'Visa',
            order_status: 'Cancelled',
        },
        {
            id: 63,
            order_id: '47797',
            order_date: '29-May-2019',
            order_time: '7:05 PM',
            payment_status: 'Paid',
            total: '$6970.59',
            payment_method: 'Mastercard',
            order_status: 'Cancelled',
        },
        {
            id: 64,
            order_id: '7727',
            order_date: '12-Jun-2019',
            order_time: '4:52 AM',
            payment_status: 'Awaiting Authorization',
            total: '$8793.72',
            payment_method: 'Visa',
            order_status: 'Delivered',
        },
        {
            id: 65,
            order_id: '69091',
            order_date: '15-Apr-2019',
            order_time: '2:13 AM',
            payment_status: 'Awaiting Authorization',
            total: '$799.08',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 66,
            order_id: '55320',
            order_date: '29-Jan-2019',
            order_time: '7:47 AM',
            payment_status: 'Payment Failed',
            total: '$8411.65',
            payment_method: 'Mastercard',
            order_status: 'Cancelled',
        },
        {
            id: 67,
            order_id: '334',
            order_date: '15-Jan-2019',
            order_time: '5:15 PM',
            payment_status: 'Payment Failed',
            total: '$885.00',
            payment_method: 'Credit Card',
            order_status: 'Delivered',
        },
        {
            id: 68,
            order_id: '782',
            order_date: '13-Feb-2019',
            order_time: '2:57 PM',
            payment_status: 'Unpaid',
            total: '$8856.16',
            payment_method: 'Mastercard',
            order_status: 'Shipped',
        },
        {
            id: 69,
            order_id: '6036',
            order_date: '30-Apr-2019',
            order_time: '1:29 AM',
            payment_status: 'Unpaid',
            total: '$904.92',
            payment_method: 'Mastercard',
            order_status: 'Shipped',
        },
        {
            id: 70,
            order_id: '2028',
            order_date: '04-Jan-2019',
            order_time: '2:05 PM',
            payment_status: 'Unpaid',
            total: '$4966.59',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 71,
            order_id: '603',
            order_date: '14-Jan-2019',
            order_time: '4:21 AM',
            payment_status: 'Unpaid',
            total: '$2899.05',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 72,
            order_id: '0497',
            order_date: '08-Jun-2019',
            order_time: '2:27 AM',
            payment_status: 'Unpaid',
            total: '$8717.70',
            payment_method: 'Payoneer',
            order_status: 'Shipped',
        },
        {
            id: 73,
            order_id: '635',
            order_date: '15-Jul-2019',
            order_time: '2:51 AM',
            payment_status: 'Paid',
            total: '$5238.61',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 74,
            order_id: '2185',
            order_date: '13-Jan-2019',
            order_time: '8:06 PM',
            payment_status: 'Unpaid',
            total: '$620.06',
            payment_method: 'Visa',
            order_status: 'Shipped',
        },
        {
            id: 75,
            order_id: '235',
            order_date: '28-Jun-2019',
            order_time: '8:22 AM',
            payment_status: 'Paid',
            total: '$8280.55',
            payment_method: 'Paypal',
            order_status: 'Processing',
        },
        {
            id: 76,
            order_id: '121',
            order_date: '09-Apr-2019',
            order_time: '4:41 PM',
            payment_status: 'Payment Failed',
            total: '$8483.16',
            payment_method: 'Payoneer',
            order_status: 'Cancelled',
        },
        {
            id: 77,
            order_id: '9288',
            order_date: '17-Jun-2019',
            order_time: '6:17 PM',
            payment_status: 'Paid',
            total: '$5638.00',
            payment_method: 'Credit Card',
            order_status: 'Delivered',
        },
        {
            id: 78,
            order_id: '4',
            order_date: '27-May-2019',
            order_time: '8:31 PM',
            payment_status: 'Paid',
            total: '$3600.90',
            payment_method: 'Credit Card',
            order_status: 'Cancelled',
        },
        {
            id: 79,
            order_id: '98',
            order_date: '18-Jul-2019',
            order_time: '6:25 AM',
            payment_status: 'Awaiting Authorization',
            total: '$7017.32',
            payment_method: 'Visa',
            order_status: 'Cancelled',
        },
        {
            id: 80,
            order_id: '2',
            order_date: '21-Jul-2019',
            order_time: '11:32 AM',
            payment_status: 'Payment Failed',
            total: '$4923.75',
            payment_method: 'Visa',
            order_status: 'Processing',
        },
        {
            id: 81,
            order_id: '18652',
            order_date: '17-Mar-2019',
            order_time: '5:16 AM',
            payment_status: 'Awaiting Authorization',
            total: '$7781.30',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 82,
            order_id: '2154',
            order_date: '16-Jul-2019',
            order_time: '8:49 PM',
            payment_status: 'Unpaid',
            total: '$7772.35',
            payment_method: 'Credit Card',
            order_status: 'Cancelled',
        },
        {
            id: 83,
            order_id: '127',
            order_date: '18-Apr-2019',
            order_time: '8:00 PM',
            payment_status: 'Unpaid',
            total: '$8074.16',
            payment_method: 'Credit Card',
            order_status: 'Shipped',
        },
        {
            id: 84,
            order_id: '8866',
            order_date: '13-May-2019',
            order_time: '3:53 PM',
            payment_status: 'Unpaid',
            total: '$1769.78',
            payment_method: 'Mastercard',
            order_status: 'Cancelled',
        },
        {
            id: 85,
            order_id: '3',
            order_date: '28-Mar-2019',
            order_time: '9:37 PM',
            payment_status: 'Awaiting Authorization',
            total: '$8387.41',
            payment_method: 'Payoneer',
            order_status: 'Processing',
        },
        {
            id: 86,
            order_id: '9499',
            order_date: '25-Jan-2019',
            order_time: '5:56 PM',
            payment_status: 'Unpaid',
            total: '$1575.43',
            payment_method: 'Credit Card',
            order_status: 'Shipped',
        },
        {
            id: 87,
            order_id: '905',
            order_date: '08-Jun-2019',
            order_time: '1:47 PM',
            payment_status: 'Payment Failed',
            total: '$6732.83',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 88,
            order_id: '3',
            order_date: '11-Jun-2019',
            order_time: '2:29 PM',
            payment_status: 'Unpaid',
            total: '$8606.47',
            payment_method: 'Paypal',
            order_status: 'Cancelled',
        },
        {
            id: 89,
            order_id: '23556',
            order_date: '21-Jan-2019',
            order_time: '5:00 PM',
            payment_status: 'Awaiting Authorization',
            total: '$7765.50',
            payment_method: 'Payoneer',
            order_status: 'Cancelled',
        },
        {
            id: 90,
            order_id: '625',
            order_date: '27-Jan-2019',
            order_time: '12:37 PM',
            payment_status: 'Paid',
            total: '$3732.00',
            payment_method: 'Mastercard',
            order_status: 'Shipped',
        },
        {
            id: 91,
            order_id: '6',
            order_date: '23-Jul-2019',
            order_time: '6:04 PM',
            payment_status: 'Payment Failed',
            total: '$7194.17',
            payment_method: 'Mastercard',
            order_status: 'Delivered',
        },
        {
            id: 92,
            order_id: '2808',
            order_date: '06-Jun-2019',
            order_time: '10:41 PM',
            payment_status: 'Paid',
            total: '$1181.92',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 93,
            order_id: '9313',
            order_date: '08-May-2019',
            order_time: '8:10 AM',
            payment_status: 'Paid',
            total: '$370.72',
            payment_method: 'Paypal',
            order_status: 'Shipped',
        },
        {
            id: 94,
            order_id: '66',
            order_date: '24-Jan-2019',
            order_time: '12:30 AM',
            payment_status: 'Unpaid',
            total: '$3398.52',
            payment_method: 'Paypal',
            order_status: 'Shipped',
        },
        {
            id: 95,
            order_id: '5',
            order_date: '04-Jun-2019',
            order_time: '7:23 PM',
            payment_status: 'Paid',
            total: '$8872.94',
            payment_method: 'Paypal',
            order_status: 'Delivered',
        },
        {
            id: 96,
            order_id: '4',
            order_date: '21-May-2019',
            order_time: '6:13 AM',
            payment_status: 'Payment Failed',
            total: '$6897.83',
            payment_method: 'Mastercard',
            order_status: 'Processing',
        },
        {
            id: 97,
            order_id: '7160',
            order_date: '08-Apr-2019',
            order_time: '10:49 PM',
            payment_status: 'Unpaid',
            total: '$4432.29',
            payment_method: 'Credit Card',
            order_status: 'Cancelled',
        },
        {
            id: 98,
            order_id: '10509',
            order_date: '05-Jun-2019',
            order_time: '7:54 PM',
            payment_status: 'Unpaid',
            total: '$6381.03',
            payment_method: 'Credit Card',
            order_status: 'Shipped',
        },
        {
            id: 99,
            order_id: '025',
            order_date: '31-May-2019',
            order_time: '8:50 PM',
            payment_status: 'Awaiting Authorization',
            total: '$197.45',
            payment_method: 'Payoneer',
            order_status: 'Processing',
        },
        {
            id: 100,
            order_id: '16529',
            order_date: '01-Jul-2019',
            order_time: '6:04 AM',
            payment_status: 'Payment Failed',
            total: '$3337.15',
            payment_method: 'Credit Card',
            order_status: 'Cancelled',
        },
    ];

    this.selectAll = false;
    this.checkboxPlugin;
  }

  initOrders(){
  
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
                id: (row) => {
                  return row.cell(1).data
                }
              },
            },
          },
          {
            id: 'id',
            name: 'Id',
            hidden: true
          },
          {
            id: 'order_id',
            name: 'Order ID',
            sort: {
              enabled: true
            },
            formatter: this.orderIDFormatter.bind(this)
          },
          {
            id: 'order_date',
            name: 'Date',   sort: {
              enabled: true
            },
            formatter: this.orderDateFormatter.bind(this)
          },
          {
            id: 'order_time',
            name: 'Time',   sort: {
              enabled: true
            },
            hidden: true,
          },
          {
            id: 'payment_status',
            name: 'Payment Status',
            sort: {
              enabled: true
            },
            formatter: this.ordePaymentStatusFormatter.bind(this)
          },
          {
            id: 'total',
            name: 'Total',   sort: {
              enabled: true
            },
          }, {
            id: 'payment_method',
            name: 'Payment Method',
            sort: {
              enabled: true
            },
          },
          {
            id: 'order_status',
            name: 'Order Status',
            sort: {
              enabled: true
            },
            formatter: this.orderStatusFormatter.bind(this)
          },
          {
            name: 'Action',
            // width: '85px',
            sort: {
              enabled: false
            },
            formatter: this.orderActionFormatter.bind(this)
          }],
        search: true,
        pagination: {
          enabled: true,
          limit: 10
        },
        data: this.orderList.map((order) => {
          return {
            id: order.id,
            order_id: order.order_id,
            order_date: order.order_date,
            order_time: order.order_time,
            payment_status: order.payment_status,
            total: order.total,
            payment_method: order.payment_method,
            order_status: order.order_status,
          }
        }),
        className: {
          table: 'table table-centered w-100 dt-responsive nowrap',
          thead: 'table-light',
          search: 'float-end'
        }
      }

  );

  grid.render(document.getElementById('orders-datatable-wrapper'));

  document.querySelectorAll('.gridjs .gridjs-search .gridjs-search-input').forEach(function(e){
    e.classList.add('form-control');
    e.classList.remove('gridjs-input');
  });

  grid.on('ready',function(e){
    self.checkboxPlugin = grid.config.plugin.get('rowSelect');

    self.checkboxPlugin.props.store.on('updated', function (state, prevState,e) {
      self.selectAll = !self.selectAll;
    });

    document.querySelectorAll('.gridjs .gridjs-wrapper .gridjs-table .gridjs-tbody .gridjs-tr .gridjs-td .gridjs-checkbox').forEach(function(e){
        e.classList.add('form-check-input');
      });
    });

  }

  updateSelect(params) {
     this.selectAll = !this.selectAll;
     if (this.selectAll) {
       document.querySelectorAll('.gridjs-tbody .gridjs-tr').forEach(function (e) {
         e.classList.add("gridjs-tr-selected");
       });
       document.querySelectorAll('.form-check-input').forEach(function (e) {
         e.setAttribute('checked', "true");
       });
     }
     else {
       document.querySelectorAll('.gridjs-tbody .gridjs-tr').forEach(function (e) {
         e.classList.remove("gridjs-tr-selected");
       });
       document.querySelectorAll('.form-check-input').forEach(function (e) {
         e.removeAttribute('checked');
       });
     }
  }
  

  init() {
    document.querySelectorAll('[data-toggle="select2"]').forEach(function(element) {
      new Choices(element,{
        itemSelectText:'',
      });
    });
    this.initOrders();


    

  }


    // table product formatter
  // formats order ID cell
  orderIDFormatter(cell, row) {
    return (html(
      `<a href="javascript:void(0)" class="order text-body fw-bold" id="${row.cells[1].data}">#BM${row.cells[2].data}</a> `
    ));
  }

  // formats order date cell
  orderDateFormatter(cell, row) {
    return (html(
      `${row.cells[3].data} <small class="text-muted">${row.cells[4].data}</small>`
    ));
  }

  // formats payment status cell
  ordePaymentStatusFormatter(cell, row) {
    if (row.cells[5].data == "Paid") {
      return (html(
        `<h5><span class="badge badge-success-lighten"><i class="mdi mdi-coin"></i> Paid</span></h5>`
      ));
    }
    else if (row.cells[5].data == "Awaiting Authorization") {
      return (html(
        `<h5><span class="badge badge-warning-lighten"><i class="mdi mdi-timer-sand"></i> Awaiting Authorization</span></h5>`
      ));
    }
    else if (row.cells[5].data == "Payment Failed") {
      return (html(
        ` <h5><span class="badge badge-danger-lighten"><i class="mdi mdi-cancel"></i> Payment Failed</span></h5>`
      ));
    }
    else {
      return (html(
        `<h5><span class="badge badge-info-lighten"><i class="mdi mdi-cash"></i> Unpaid</span></h5>`
      ));
    }

  }

  // formats order status
  orderStatusFormatter(cell, row) {
    if (row.cells[8].data == "Processing") {
      return (html(
        `<h5><span class="badge badge-warning-lighten">Processing</span></h5>`
      ));
    }
    else if (row.cells[8].data == "Delivered") {
      return (html(
        `<h5><span class="badge badge-success-lighten">Delivered</span></h5>`
      ));
    }
    else if (row.cells[8].data == "Shipped") {
      return (html(
        `<h5><span class="badge badge-info-lighten">Shipped</span></h5>`
      ));
    }
    else {
      return (html(
        `<h5><span class="badge badge-danger-lighten">Cancelled</span></h5>`
      ));
    }

  }

  // action cell formatter
  orderActionFormatter(cell, row) {
    return (html(
      `<a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-eye"></i></a>
           <a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-square-edit-outline"></i></a>
           <a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-delete"></i></a>`
    ))
  }


}         

// init the dashboard
new EcommerceOrder().init();
