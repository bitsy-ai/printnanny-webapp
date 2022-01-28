export const DEVICE_SCAN_RESULT = 'device_scan_result'
export const MQTT_PING_EVENT = 'mqtt_ping_event'
export const MQTT_PING_EVENT_LOG = 'mqtt_ping_event_log'
export const MQTT_PONG_EVENT = 'mqtt_pong_event'
export const MQTT_PONG_EVENT_LOG = 'mqtt_pong_event_log'

export default {
  [DEVICE_SCAN_RESULT]: {},
  [MQTT_PING_EVENT]: { status: 'Waiting' },
  [MQTT_PING_EVENT_LOG]: [],
  [MQTT_PONG_EVENT]: { status: 'Waiting' },
  [MQTT_PONG_EVENT_LOG]: []
}
