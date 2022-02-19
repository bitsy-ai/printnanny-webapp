import * as api from 'printnanny-api-client'

export const SENT_EVENTS = 'sent_events'
export const RECEIVED_EVENTS = 'received_events'
export default {
  [SENT_EVENTS]: Array<api.PolymorphicEvent>(),
  [RECEIVED_EVENTS]: Array<api.PolymorphicEvent>()
}
