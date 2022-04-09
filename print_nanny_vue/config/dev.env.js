'use strict'
const os = require('os');
const { merge } = require('webpack-merge');
const prodEnv = require('./prod.env')

const PRINTNANNY_API_URL = `http://${os.hostname()}:8000`
const PRINTNANNY_WS_URL = `ws://${os.hostname()}:8000/ws/events/`

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  PRINTNANNY_API_URL: JSON.stringify(PRINTNANNY_API_URL),
  PRINTNANNY_WS_URL: JSON.stringify(PRINTNANNY_WS_URL)
})
