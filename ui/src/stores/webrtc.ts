import * as api from "printnanny-api-client";
import { defineStore, acceptHMRUpdate } from "pinia";
import { ApiConfig } from "@/utils/api";
import Janode from 'janode';
import StreamingPlugin from 'janode/plugins/streaming';


const connection = await Janode.connect({

})
const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWebrtcStore = defineStore({
  id: "webrtc",
  state: () => ({
    streams: [] as Array<api.WebrtcStream>,
    connection: undefined as undefined | Janode.Connection
  }),
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWebrtcStore, import.meta.hot));
}
