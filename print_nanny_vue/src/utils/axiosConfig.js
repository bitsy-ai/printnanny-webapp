
import axios from 'axios'
import Vue from 'vue'
const instance = axios.create({
  baseURL: process.env.BASE_API_URL
})

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
instance.defaults.withCredentials = true

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.withCredentials = true

export default instance
