import * as api from "printnanny-api-client";
import { defineStore, acceptHMRUpdate } from "pinia";
import { ApiConfig, handleApiError } from "@/utils/api";

const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWebrtcStore = defineStore({
  id: "webrtc",
  state: () => ({
    streams: [] as Array<api.WebrtcStream>,
  }),
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWebrtcStore, import.meta.hot));
}
