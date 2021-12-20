'use strict'
const { merge } = require('webpack-merge');
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  BASE_API_URL: '"http://aurora:8000"',
  BASE_WS_URL: '"ws://aurora:8000/ws/"',
  ALERTS_WS_URL: '"ws://aurora:8000/ws/alerts/"',
  TASKS_WS_URL: '"ws://aurora:8000/ws/tasks/"'
})
