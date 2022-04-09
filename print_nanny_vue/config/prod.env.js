'use strict'

const PRINTNANNY_API_URL = process.env.PRINTNANNY_API_URL || "https://printnanny.ai"
const PRINTNANNY_WS_URL = process.env.PRINTNANNY_WS_URL || "wss://printnanny.ai/ws/events/"
module.exports = {
  NODE_ENV: '"production"',
  PRINTNANNY_API_URL: JSON.stringify(PRINTNANNY_API_URL),
  PRINTNANNY_WS_URL: JSON.stringify(PRINTNANNY_WS_URL)
}
