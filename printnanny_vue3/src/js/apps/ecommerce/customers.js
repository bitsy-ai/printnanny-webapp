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



class EcommerceCustomers {

  constructor() {

    this.customerList = [{
        id: 1,
        name: 'Calhoun Jurisch',
        phone: '237-960-4150',
        email: 'cjurisch0@virginia.edu',
        location: 'Costa Rica',
        created_on: '11/17/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 2,
        name: 'Axe Rulton',
        phone: '793-400-7003',
        email: 'arulton1@google.com.hk',
        location: 'Slovenia',
        created_on: '05/18/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 3,
        name: 'Kalindi Robjant',
        phone: '847-272-2783',
        email: 'krobjant2@networkadvertising.org',
        location: 'Ukraine',
        created_on: '07/21/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 4,
        name: 'Barnabas Dunridge',
        phone: '259-691-9956',
        email: 'bdunridge3@narod.ru',
        location: 'China',
        created_on: '01/25/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 5,
        name: 'Billy Petrus',
        phone: '544-342-6594',
        email: 'bpetrus4@harvard.edu',
        location: 'Mauritius',
        created_on: '11/28/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 6,
        name: 'Karly Gleave',
        phone: '776-411-2058',
        email: 'kgleave5@craigslist.org',
        location: 'Indonesia',
        created_on: '08/29/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 7,
        name: 'Jeffie Kirkland',
        phone: '533-278-3816',
        email: 'jkirkland6@twitter.com',
        location: 'Indonesia',
        created_on: '02/09/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 8,
        name: 'Tierney Iorizzi',
        phone: '914-298-7354',
        email: 'tiorizzi7@ask.com',
        location: 'Macedonia',
        created_on: '06/14/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 9,
        name: 'Brena Fosh',
        phone: '883-143-9328',
        email: 'bfosh8@wikipedia.org',
        location: 'Russia',
        created_on: '08/26/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 10,
        name: 'Caye Maymand',
        phone: '312-776-6360',
        email: 'cmaymand9@freewebs.com',
        location: 'Sweden',
        created_on: '10/15/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 11,
        name: 'Delinda Angove',
        phone: '860-746-2368',
        email: 'dangovea@noaa.gov',
        location: 'China',
        created_on: '01/26/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 12,
        name: 'Dasie Keelin',
        phone: '255-652-9988',
        email: 'dkeelinb@google.co.jp',
        location: 'Sweden',
        created_on: '02/19/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 13,
        name: 'Paule Henderson',
        phone: '895-805-4051',
        email: 'phendersonc@scientificamerican.com',
        location: 'Poland',
        created_on: '12/27/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 14,
        name: 'Erl Mullan',
        phone: '351-466-6655',
        email: 'emulland@sbwire.com',
        location: 'Czech Republic',
        created_on: '05/20/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 15,
        name: 'Oberon McGilvray',
        phone: '877-345-7651',
        email: 'omcgilvraye@parallels.com',
        location: 'China',
        created_on: '07/02/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 16,
        name: 'Jaymee Spittall',
        phone: '131-439-5707',
        email: 'jspittallf@google.es',
        location: 'Russia',
        created_on: '02/03/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 17,
        name: 'Ardine Purvess',
        phone: '378-783-2226',
        email: 'apurvessg@skype.com',
        location: 'Thailand',
        created_on: '02/12/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 18,
        name: 'Berti Schurcke',
        phone: '576-605-1162',
        email: 'bschurckeh@yelp.com',
        location: 'Indonesia',
        created_on: '08/14/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 19,
        name: 'Lois Haggarth',
        phone: '436-665-4335',
        email: 'lhaggarthi@mail.ru',
        location: 'Indonesia',
        created_on: '01/02/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 20,
        name: 'Lidia Catonne',
        phone: '546-678-6108',
        email: 'lcatonnej@wikimedia.org',
        location: 'France',
        created_on: '12/27/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 21,
        name: 'Ilse McSkeagan',
        phone: '912-775-1755',
        email: 'imcskeagank@cbc.ca',
        location: 'Brazil',
        created_on: '12/22/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 22,
        name: 'Shelbi Scoffins',
        phone: '896-107-1331',
        email: 'sscoffinsl@ucoz.com',
        location: 'Brazil',
        created_on: '01/19/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 23,
        name: 'Herschel Richemond',
        phone: '979-268-9701',
        email: 'hrichemondm@hp.com',
        location: 'South Korea',
        created_on: '10/20/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 24,
        name: 'Manda Kidder',
        phone: '408-677-8641',
        email: 'mkiddern@slashdot.org',
        location: 'United States',
        created_on: '03/16/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 25,
        name: 'Carlynne Moffatt',
        phone: '785-944-0565',
        email: 'cmoffatto@google.com.au',
        location: 'China',
        created_on: '07/14/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 26,
        name: 'Chris Hailey',
        phone: '771-443-8390',
        email: 'chaileyp@salon.com',
        location: 'Greece',
        created_on: '01/08/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 27,
        name: 'Ronny Durbyn',
        phone: '481-835-8556',
        email: 'rdurbynq@studiopress.com',
        location: 'Russia',
        created_on: '11/26/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 28,
        name: 'Gale Tunnah',
        phone: '744-794-3069',
        email: 'gtunnahr@nymag.com',
        location: 'Japan',
        created_on: '05/01/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 29,
        name: 'Winnifred Laval',
        phone: '243-155-1749',
        email: 'wlavals@sciencedirect.com',
        location: 'Japan',
        created_on: '11/11/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 30,
        name: 'Kylen Meenan',
        phone: '813-163-5813',
        email: 'kmeenant@mapy.cz',
        location: 'Mongolia',
        created_on: '06/04/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 31,
        name: 'Ethan Boskell',
        phone: '250-811-4195',
        email: 'eboskellu@prlog.org',
        location: 'Colombia',
        created_on: '11/23/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 32,
        name: 'Haslett Lillo',
        phone: '188-768-7390',
        email: 'hlillov@globo.com',
        location: 'Sweden',
        created_on: '12/17/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 33,
        name: 'Onofredo Payn',
        phone: '312-937-6093',
        email: 'opaynw@ted.com',
        location: 'Israel',
        created_on: '05/19/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 34,
        name: 'Maybelle Hallward',
        phone: '959-223-4786',
        email: 'mhallwardx@si.edu',
        location: 'Indonesia',
        created_on: '03/03/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 35,
        name: 'Rourke Winchcombe',
        phone: '725-326-6328',
        email: 'rwinchcombey@cafepress.com',
        location: 'China',
        created_on: '08/04/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 36,
        name: 'Nahum Caps',
        phone: '223-829-1794',
        email: 'ncapsz@businessweek.com',
        location: 'Indonesia',
        created_on: '04/08/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 37,
        name: 'Buddy Langlais',
        phone: '642-402-9216',
        email: 'blanglais10@dedecms.com',
        location: 'Slovenia',
        created_on: '03/13/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 38,
        name: 'Terrell Whichelow',
        phone: '667-300-8162',
        email: 'twhichelow11@bandcamp.com',
        location: 'Czech Republic',
        created_on: '11/16/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 39,
        name: 'Edie Alwen',
        phone: '843-488-3319',
        email: 'ealwen12@instagram.com',
        location: 'Portugal',
        created_on: '12/31/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 40,
        name: 'Shannan Fontelles',
        phone: '157-303-2312',
        email: 'sfontelles13@newyorker.com',
        location: 'China',
        created_on: '07/06/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 41,
        name: 'Eran Beckett',
        phone: '183-885-3780',
        email: 'ebeckett14@mapy.cz',
        location: 'Finland',
        created_on: '08/05/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 42,
        name: 'Cyndie Swigger',
        phone: '606-697-8910',
        email: 'cswigger15@4shared.com',
        location: 'Peru',
        created_on: '01/21/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 43,
        name: 'Hoyt Loudon',
        phone: '408-213-4454',
        email: 'hloudon16@stumbleupon.com',
        location: 'United States',
        created_on: '11/06/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 44,
        name: 'Ned Bygreaves',
        phone: '323-496-9901',
        email: 'nbygreaves17@dmoz.org',
        location: 'Philippines',
        created_on: '05/30/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 45,
        name: 'Kayne Lavers',
        phone: '291-124-4659',
        email: 'klavers18@istockphoto.com',
        location: 'China',
        created_on: '01/23/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 46,
        name: 'Helen Ricardo',
        phone: '914-578-2934',
        email: 'hricardo19@bloglovin.com',
        location: 'Indonesia',
        created_on: '06/28/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 47,
        name: 'Hodge Staunton',
        phone: '263-305-9530',
        email: 'hstaunton1a@tuttocitta.it',
        location: 'Ukraine',
        created_on: '03/22/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 48,
        name: 'Laina Extence',
        phone: '164-944-0339',
        email: 'lextence1b@mail.ru',
        location: 'China',
        created_on: '12/14/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 49,
        name: 'Kirsti Godspede',
        phone: '966-450-2447',
        email: 'kgodspede1c@cdc.gov',
        location: 'France',
        created_on: '03/16/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 50,
        name: 'Alisander Pane',
        phone: '483-378-0064',
        email: 'apane1d@mac.com',
        location: 'Portugal',
        created_on: '09/21/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 51,
        name: 'Xever Faircley',
        phone: '741-905-3979',
        email: 'xfaircley1e@cargocollective.com',
        location: 'Croatia',
        created_on: '07/17/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 52,
        name: 'Matthiew Halms',
        phone: '462-610-2978',
        email: 'mhalms1f@vistaprint.com',
        location: 'Japan',
        created_on: '11/06/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 53,
        name: 'Edlin Kornyakov',
        phone: '560-901-0423',
        email: 'ekornyakov1g@census.gov',
        location: 'Indonesia',
        created_on: '01/08/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 54,
        name: 'Nara Marder',
        phone: '435-664-3795',
        email: 'nmarder1h@symantec.com',
        location: 'China',
        created_on: '01/14/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 55,
        name: 'Elton Falla',
        phone: '843-738-6361',
        email: 'efalla1i@bandcamp.com',
        location: 'Indonesia',
        created_on: '10/10/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 56,
        name: 'Andre Stonary',
        phone: '687-744-0791',
        email: 'astonary1j@prlog.org',
        location: 'China',
        created_on: '02/06/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 57,
        name: 'Elinore Moquin',
        phone: '100-493-5099',
        email: 'emoquin1k@surveymonkey.com',
        location: 'Indonesia',
        created_on: '10/23/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 58,
        name: 'Carla Coddington',
        phone: '294-344-6782',
        email: 'ccoddington1l@studiopress.com',
        location: 'Croatia',
        created_on: '01/31/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 59,
        name: 'Moses Lunk',
        phone: '292-502-1902',
        email: 'mlunk1m@sitemeter.com',
        location: 'Poland',
        created_on: '02/24/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 60,
        name: 'Ginnifer McKyrrelly',
        phone: '322-731-8053',
        email: 'gmckyrrelly1n@is.gd',
        location: 'Portugal',
        created_on: '03/19/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 61,
        name: 'Nicki Ozintsev',
        phone: '382-167-5417',
        email: 'nozintsev1o@mayoclinic.com',
        location: 'Chile',
        created_on: '01/14/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 62,
        name: 'Carlo Nursey',
        phone: '590-342-6954',
        email: 'cnursey1p@msu.edu',
        location: 'Nigeria',
        created_on: '03/08/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 63,
        name: 'Korey Berney',
        phone: '823-383-1005',
        email: 'kberney1q@businessweek.com',
        location: 'Indonesia',
        created_on: '01/11/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 64,
        name: 'Mendie McKillop',
        phone: '133-334-9895',
        email: 'mmckillop1r@netvibes.com',
        location: 'Mexico',
        created_on: '12/19/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 65,
        name: 'Harli Cosser',
        phone: '571-278-6061',
        email: 'hcosser1s@earthlink.net',
        location: 'Egypt',
        created_on: '12/20/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 66,
        name: 'Trude Rusling',
        phone: '383-289-3482',
        email: 'trusling1t@linkedin.com',
        location: 'Kazakhstan',
        created_on: '06/18/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 67,
        name: 'Kele Campling',
        phone: '935-534-6058',
        email: 'kcampling1u@unesco.org',
        location: 'Nigeria',
        created_on: '05/23/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 68,
        name: 'Demeter Hearons',
        phone: '462-678-9546',
        email: 'dhearons1v@timesonline.co.uk',
        location: 'Portugal',
        created_on: '07/08/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 69,
        name: 'Demetria Popov',
        phone: '906-394-8455',
        email: 'dpopov1w@cornell.edu',
        location: 'Japan',
        created_on: '05/12/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 70,
        name: 'Annelise Starmont',
        phone: '695-736-3251',
        email: 'astarmont1x@utexas.edu',
        location: 'Nigeria',
        created_on: '07/27/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 71,
        name: 'Edik Haresign',
        phone: '317-163-6552',
        email: 'eharesign1y@businessinsider.com',
        location: 'China',
        created_on: '01/21/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 72,
        name: 'Leandra Pendergrast',
        phone: '409-475-3428',
        email: 'lpendergrast1z@mediafire.com',
        location: 'Indonesia',
        created_on: '01/17/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 73,
        name: 'Rogerio Wallwork',
        phone: '606-354-5837',
        email: 'rwallwork20@nydailynews.com',
        location: 'South Africa',
        created_on: '11/06/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 74,
        name: 'Cos Mostyn',
        phone: '906-366-4157',
        email: 'cmostyn21@squarespace.com',
        location: 'Indonesia',
        created_on: '03/28/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 75,
        name: 'Randolph Tortice',
        phone: '865-723-6671',
        email: 'rtortice22@odnoklassniki.ru',
        location: 'Poland',
        created_on: '11/07/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 76,
        name: 'Leena Francescotti',
        phone: '817-664-9710',
        email: 'lfrancescotti23@people.com.cn',
        location: 'Ukraine',
        created_on: '09/27/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 77,
        name: 'Elspeth Liven',
        phone: '793-469-6899',
        email: 'eliven24@redcross.org',
        location: 'Philippines',
        created_on: '06/20/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 78,
        name: 'Clair Zoren',
        phone: '601-779-9284',
        email: 'czoren25@biglobe.ne.jp',
        location: 'Philippines',
        created_on: '10/01/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 79,
        name: 'Atlante Renahan',
        phone: '477-537-4015',
        email: 'arenahan26@ifeng.com',
        location: 'Greece',
        created_on: '09/12/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 80,
        name: 'Enrika Lemmertz',
        phone: '441-409-1283',
        email: 'elemmertz27@toplist.cz',
        location: 'Japan',
        created_on: '03/16/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 81,
        name: 'Paige Moral',
        phone: '670-172-7193',
        email: 'pmoral28@ning.com',
        location: 'Philippines',
        created_on: '12/26/2018',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 82,
        name: 'Fayth Dibbin',
        phone: '442-584-6949',
        email: 'fdibbin29@live.com',
        location: 'Myanmar',
        created_on: '10/14/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 83,
        name: 'Gloria Musso',
        phone: '198-187-8880',
        email: 'gmusso2a@wordpress.org',
        location: 'Botswana',
        created_on: '09/17/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 84,
        name: 'Rene Dovington',
        phone: '116-633-6853',
        email: 'rdovington2b@163.com',
        location: 'China',
        created_on: '05/10/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 85,
        name: 'Wilow Brainsby',
        phone: '580-841-0171',
        email: 'wbrainsby2c@ask.com',
        location: 'China',
        created_on: '03/29/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 86,
        name: 'Isidore Borkett',
        phone: '872-725-3021',
        email: 'iborkett2d@umn.edu',
        location: 'China',
        created_on: '03/18/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 87,
        name: 'Jethro Laye',
        phone: '386-684-1566',
        email: 'jlaye2e@oracle.com',
        location: 'Sweden',
        created_on: '06/07/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 88,
        name: 'Grannie Patriche',
        phone: '156-254-2399',
        email: 'gpatriche2f@usatoday.com',
        location: 'Indonesia',
        created_on: '05/11/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 89,
        name: 'Jacynth Goundsy',
        phone: '339-392-1915',
        email: 'jgoundsy2g@goo.ne.jp',
        location: 'Malaysia',
        created_on: '06/12/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 90,
        name: 'Ezechiel Golsthorp',
        phone: '978-712-8471',
        email: 'egolsthorp2h@creativecommons.org',
        location: 'Russia',
        created_on: '06/27/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 91,
        name: 'Ignace O\'Loughane',
        phone: '453-455-7536',
        email: 'ioloughane2i@home.pl',
        location: 'Philippines',
        created_on: '09/21/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 92,
        name: 'Stanleigh Leonarde',
        phone: '689-488-3261',
        email: 'sleonarde2j@nytimes.com',
        location: 'China',
        created_on: '05/16/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 93,
        name: 'Tammy Manhare',
        phone: '517-445-7695',
        email: 'tmanhare2k@g.co',
        location: 'Thailand',
        created_on: '09/18/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }, {
        id: 94,
        name: 'Kingston Bakster',
        phone: '864-603-2366',
        email: 'kbakster2l@mysql.com',
        location: 'Indonesia',
        created_on: '01/16/2019',
        status: 'Active',
        avatar: '../../images/users/avatar-3.jpg'
    }, {
        id: 95,
        name: 'Chip Panchin',
        phone: '848-290-0668',
        email: 'cpanchin2m@goo.gl',
        location: 'Indonesia',
        created_on: '08/30/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-4.jpg'
    }, {
        id: 96,
        name: 'Laurel Cremen',
        phone: '268-241-0447',
        email: 'lcremen2n@moonfruit.com',
        location: 'Guinea',
        created_on: '09/28/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-5.jpg'
    }, {
        id: 97,
        name: 'Cami Enos',
        phone: '851-231-1785',
        email: 'cenos2o@abc.net.au',
        location: 'China',
        created_on: '06/29/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-6.jpg'
    }, {
        id: 98,
        name: 'Dedie Seldon',
        phone: '857-931-8976',
        email: 'dseldon2p@vimeo.com',
        location: 'Indonesia',
        created_on: '07/13/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-7.jpg'
    }, {
        id: 99,
        name: 'Trip Austwick',
        phone: '648-514-6247',
        email: 'taustwick2q@meetup.com',
        location: 'Brazil',
        created_on: '04/28/2019',
        status: 'Blocked',
        avatar: '../../images/users/avatar-1.jpg'
    }, {
        id: 100,
        name: 'Frederich Kettles',
        phone: '703-126-2946',
        email: 'fkettles2r@miitbeian.gov.cn',
        location: 'Peru',
        created_on: '11/09/2018',
        status: 'Active',
        avatar: '../../images/users/avatar-2.jpg'
    }];
  }

  initProducts(){

  var grid = new Grid({
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
          name: 'Customers',
          formatter: this.customerNameFormatter.bind(this)
        },
        {
          id: 'avatar',
          name: 'Avatar',
          hidden: true
        },
        {
          id: 'phone',
          name: 'Phone',
          // formatter: this.orderDateFormatter.bind(this)
        },
        {
          id: 'email',
          name: 'Email',
        },
        {
          id: 'location',
          name: 'Location',
          // formatter: this.ordePaymentStatusFormatter.bind(this)
        },
        {
          id: 'created_on',
          name: 'Created On'
        },
        {
          id: 'status',
          name: 'Status',
          formatter: this.customerStatusFormatter.bind(this)
        },
        {
          name: 'Action',
          sort: false,
          formatter: this.customerActionFormatter.bind(this)
        }],
      search: true,
      sort: true,
      pagination: {
        enabled: true,
        limit: this.pageSize
      },
      data: this.customerList.map((customer) => {
        return {
          id: customer.id,
          name: customer.name,
          phone: customer.phone,
          email: customer.email,
          location: customer.location,
          created_on: customer.created_on,
          status: customer.status,
          avatar: customer.avatar
        }
      }),
      className: {
        table: 'table table-centered w-100 nowrap',
        thead: 'table-light',
        search: 'float-end'
      }
    }
      
  );

  grid.render(document.getElementById('customers-datatable-wrapper'));

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


  customerNameFormatter(cell, row) {
    return (html(
      `
      <div class="table-user">
      <img src="${row.cells[2].data}" alt="table-user" class="me-2 rounded-circle">
       <a href="javascript:void(0);" class="text-body fw-semibold">${row.cells[1].data}</a>
       </div>
      `
    ));
  }

  // formats customer status
  customerStatusFormatter(cell, row) {
    if (row.cells[7].data == "Active") {
      return (html(
        `<h5><span class="badge badge-success-lighten">Active</span></h5>`
      ));
    }
    else {
      return (html(
        `<h5><span class="badge badge-danger-lighten">Blocked</span></h5>`
      ));
    }

  }

  // action cell formatter
  customerActionFormatter(cell, row) {
    return (html(
      `<a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-eye"></i></a>
           <a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-square-edit-outline"></i></a>
           <a href="javascript:void(0);" class="action-icon"> <i class="mdi mdi-delete"></i></a>`
    ))
  }


}         

// init the dashboard
new EcommerceCustomers().init();
