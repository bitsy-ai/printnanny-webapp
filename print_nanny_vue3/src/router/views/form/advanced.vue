<script>
import DatePicker from 'vue2-datepicker'
import Multiselect from 'vue-multiselect'
import Switches from 'vue-switches'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Form Advanced component
 */
export default {
  page: {
    title: 'Form Advanced',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { DatePicker, Multiselect, Switches, Layout, PageHeader },
  data() {
    return {
      title: 'Form Advanced',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Forms',
          href: '/',
        },
        {
          text: 'Form Advanced',
          active: true,
        },
      ],
      options: [
        'Alaska',
        'Hawaii',
        'California',
        'Nevada',
        'Oregon',
        'Washington',
        'Arizona',
        'Colorado',
        'Idaho',
        'Montana',
        'Nebraska',
        'New Mexico',
        'North Dakota',
        'Utah',
        'Wyoming',
        'Alabama',
        'Arkansas',
        'Illinois',
        'Iowa',
      ],
      value: null,
      value1: null,
      enabled: false,
      enabled1: false,
      enabled2: false,
      enabled3: false,
      enabled4: false,
      enabled5: false,
      defaultdate: '',
      autoClose: '',
      daterange: '',
      date: '',
      demoMonth: '',
      demoYear: '',
      demoDate: '',
      hour: '',
      datetime: '',
      zipcode: '',
      crazyzip: '',
      money: '',
      money2: '',
      telephone: '',
      celphone: '',
      ustelephone: '',
      areacode: '',
      ipaddress: '',
      cnpj: '',
      cpf: '',
      maxlen: '',
      data: '',
      option: '',
      textarea: '',
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Select2</h4>
            <p
              class="text-muted font-14"
            >Select2 gives you a customizable select box with support for searching, tagging, remote data sets, infinite scrolling, and many other highly used options.</p>
            <div class="row">
              <div class="col-lg-6">
                <p class="mb-1 font-weight-bold text-muted">Single Select</p>
                <p class="text-muted font-14">Select2 can take a regular select box like this...</p>
                <multiselect v-model="value" :options="options"></multiselect>
              </div>
              <div class="col-lg-6">
                <p class="mb-1 font-weight-bold text-muted">Multiple Select</p>
                <p class="text-muted font-14">Select2 can take a regular select box like this...</p>
                <multiselect v-model="value1" :options="options" :multiple="true"></multiselect>
              </div>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Switch</h4>
            <p class="text-muted font-14">Here are a few types of switches.</p>
            <div class="pt-2">
              <switches v-model="enabled" type-bold="true" class="mb-0"></switches>
              <switches v-model="enabled1" type-bold="false" color="warning" class="ml-1 mb-0"></switches>
              <switches v-model="enabled2" type-bold="false" color="danger" class="ml-1 mb-0"></switches>
              <switches v-model="enabled3" type-bold="false" color="primary" class="ml-1 mb-0"></switches>
              <switches v-model="enabled4" type-bold="false" color="success" class="ml-1 mb-0"></switches>
              <switches v-model="enabled5" type-bold="false" color="info" class="ml-1 mb-0"></switches>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Bootstrap Datepicker</h4>
            <p
              class="text-muted font-14"
            >Bootstrap-datepicker provides a flexible datepicker widget in the Bootstrap style.</p>
            <div class="row">
              <div class="col-lg-6">
                <div class="form-group mb-3">
                  <label>Date Picker</label>
                  <br />
                  <date-picker v-model="defaultdate" :first-day-of-week="1" lang="en" confirm></date-picker>
                </div>
                <div class="form-group mb-3">
                  <label>Auto close</label>
                  <br />
                  <date-picker v-model="autoClose" :first-day-of-week="1" lang="en"></date-picker>
                </div>
                <div class="form-group mb-3">
                  <label>Date Range</label>
                  <br />
                  <date-picker v-model="daterange" range append-to-body lang="en" confirm></date-picker>
                </div>
              </div>
              <div class="col-lg-6">
                <div class="form-group mb-3">
                  <label>Date View</label>
                  <br />
                  <date-picker v-model="date" format="DD-MMM-YYYY" :first-day-of-week="1" lang="en"></date-picker>
                </div>
                <div class="form-group mb-3">
                  <label>Month View</label>
                  <br />
                  <date-picker
                    v-model="demoMonth"
                    type="month"
                    lang="en"
                    confirm
                    placeholder="Select Month"
                  ></date-picker>
                </div>
                <div class="form-group mb-3">
                  <label>Year View</label>
                  <br />
                  <date-picker
                    v-model="demoYear"
                    type="year"
                    lang="en"
                    confirm
                    placeholder="Select Year"
                  ></date-picker>
                </div>
              </div>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Input Masks</h4>
            <p
              class="text-muted font-14"
            >A javascript Plugin to make masks on form fields and HTML elements.</p>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group mb-3">
                  <label for="input-date1">Date</label>
                  <input v-model="demoDate" v-mask="'##/##/####'" type="text" class="form-control" />
                  <span class="font-13 text-muted">e.g "DD/MM/YYYY"</span>
                </div>
                <div class="form-group mb-3">
                  <label>Hour</label>
                  <input v-model="hour" v-mask="'##:##:##'" type="text" class="form-control" />
                  <span class="font-13 text-muted">e.g "HH:MM:SS"</span>
                </div>
                <div class="form-group mb-3">
                  <label>Date & Hour</label>
                  <input
                    v-model="datetime"
                    v-mask="'##/##/#### ##:##:##'"
                    type="text"
                    class="form-control"
                  />
                  <span class="font-13 text-muted">e.g "DD/MM/YYYY HH:MM:SS"</span>
                </div>
                <div class="form-group mb-3">
                  <label>ZIP Code</label>
                  <input v-model="zipcode" v-mask="'#####-###'" type="text" class="form-control" />
                  <span class="font-13 text-muted">e.g "xxxxx-xxx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>Crazy Zip Code</label>
                  <input v-model="crazyzip" v-mask="'#-##-##-##'" type="text" class="form-control" />
                  <span class="font-13 text-muted">e.g "x-xx-xx-xx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>Money</label>
                  <input
                    v-model="money"
                    v-mask="'###.###.###.###.###,##'"
                    type="text"
                    class="form-control"
                  />
                  <span class="font-13 text-muted">e.g "Your money"</span>
                </div>
                <div class="form-group mb-3">
                  <label>Money 2</label>
                  <input v-model="money2" v-mask="'#.##0,00'" type="text" class="form-control" />
                  <span class="font-13 text-muted">e.g "#.##0,00"</span>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group mb-3">
                  <label>Telephone</label>
                  <input v-model="telephone" v-mask="'####-####'" type="text" class="form-control" />
                  <span class="font-13 text-muted">e.g "xxxx-xxxx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>Telephone with Code Area</label>
                  <input
                    v-model="areacode"
                    v-mask="'(##) ####-####'"
                    type="text"
                    class="form-control"
                  />
                  <span class="font-13 text-muted">e.g "(xx) xxxx-xxxx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>US Telephone</label>
                  <input
                    v-model="ustelephone"
                    v-mask="'(###) ###-####'"
                    type="text"
                    class="form-control"
                  />
                  <span class="font-13 text-muted">e.g "(xxx) xxx-xxxx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>São Paulo Celphones</label>
                  <input
                    v-model="celphone"
                    v-mask="'(##) #####-####'"
                    type="text"
                    class="form-control"
                  />
                  <span class="font-13 text-muted">e.g "(xx) xxxxx-xxxx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>CPF</label>
                  <input v-model="cpf" v-mask="'###.###.###-##'" type="text" class="form-control" />
                  <span class="font-13 text-muted">e.g "xxx.xxx.xxxx-xx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>CNPJ</label>
                  <input
                    v-model="cnpj"
                    v-mask="'##.###.###/####-##'"
                    type="text"
                    class="form-control"
                  />
                  <span class="font-13 text-muted">e.g "xx.xxx.xxx/xxxx-xx"</span>
                </div>
                <div class="form-group mb-3">
                  <label>IP Address</label>
                  <input
                    v-model="ipaddress"
                    v-mask="'###.###.###.###'"
                    type="text"
                    class="form-control"
                  />
                  <span class="font-13 text-muted">e.g "xxx.xxx.xxx.xxx"</span>
                </div>
              </div>
            </div>
            <!-- end row -->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Bootstrap Maxlength</h4>
            <p class="text-muted font-14">Specify the maxlength indication on any input.</p>
            <div class="row">
              <div class="col-lg-6">
                <div class="form-group mb-3">
                  <label>Default usage</label>
                  <p
                    class="text-muted font-13"
                  >The badge will show up by default when the remaining chars are 10 or less:</p>
                  <input v-model="maxlen" type="text" class="form-control" :maxlength="10" />
                  <div v-if="maxlen" class="text-center">
                    <p
                      class="badge position-absolute"
                      :class="{ 'badge-success': maxlen.length !== 10,
                            'badge-danger': maxlen.length === 10 }"
                    >{{ maxlen.length }} / 10</p>
                  </div>
                </div>
                <div class="form-group mb-3">
                  <label>Threshold value</label>
                  <p class="text-muted font-13">
                    Do you want the badge to show up when there are 20 chars or less? Use the
                    <code>threshold</code>
                    option:
                  </p>
                  <input v-model="data" type="text" :maxlength="25" class="form-control" />
                  <div class="text-center">
                    <p
                      v-if="data"
                      class="badge position-absolute"
                      :class="{ 'badge-success': data.length !== 25,
                            'badge-danger': data.length === 25 }"
                    >{{ data.length }} / 25</p>
                  </div>
                </div>
              </div>
              <!-- end col -->
              <div class="col-lg-6 mt-3 mt-lg-0">
                <div class="form-group mb-3">
                  <label>All the options</label>
                  <p class="text-muted font-13">Specify the data attribute.</p>

                  <input v-model="option" type="text" class="form-control" :maxlength="25" />
                  <div class="text-center">
                    <p
                      v-if="option"
                      class="badge position-absolute"
                      :class="{ 'badge-success': option.length !== 25,
                            'badge-danger': option.length === 25 }"
                    >
                      You typed
                      {{ option.length }} out of 25 chars available.
                    </p>
                  </div>
                </div>
                <div class="form-group mb-0">
                  <label>Textareas</label>
                  <p
                    class="text-muted font-13"
                  >Bootstrap maxlength supports textarea as well as inputs. Even on old IE.</p>
                  <textarea
                    v-model="textarea"
                    class="form-control"
                    :maxlength="225"
                    rows="3"
                    placeholder="This textarea has a limit of 225 chars."
                  ></textarea>
                  <div class="text-center">
                    <p
                      v-if="textarea"
                      class="badge position-absolute"
                      :class="{ 'badge-success': textarea.length !== 225,
                            'badge-danger': textarea.length === 225 }"
                    >
                      {{ textarea.length }} /
                      225
                    </p>
                  </div>
                </div>
              </div>
              <!-- end col -->
            </div>
            <!-- end row -->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>