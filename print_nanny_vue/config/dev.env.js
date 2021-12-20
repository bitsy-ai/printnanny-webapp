'use strict'
const { merge } = require('webpack-merge');
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  BASE_API_URL: '"http://localhost:8000"',
  ALERTS_WEBSOCKET: '"ws://localhost:8000/ws/alerts/"',
  TASKS_WEBSOCKET: '"ws://localhost:8000/ws/alerts/"'
})
