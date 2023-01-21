import type * as api from "printnanny-api-client";
import { toRaw } from "vue";
import { defineStore, acceptHMRUpdate } from "pinia";
import { useAccountStore } from "./account";
import type { VideoRecording } from "printnanny-api-client";
import { handleApiError } from "@/utils/api";

export const useVideoStore = defineStore({
  id: "videos",
  state: () => ({
    loading: false,
    videos: [] as Array<api.VideoRecording>,
  }),
  getters: {
    showEmpty: (state) => state.loading == false && toRaw(state.videos).length === 0
  },
  actions: {
    async load(): Promise<Array<VideoRecording> | undefined> {
      this.$patch({ loading: true });
      const accountStore = useAccountStore();
      const res = await accountStore.videosApi.videoRecordingsList().catch(handleApiError);
      console.debug("videoRecordingsList: ", res);
      if (res?.data.results) {
        this.$patch({
          loading: false,
          videos: res.data.results
        });
        return res.data.results;
      } else {
        this.$patch({
          loading: false,
        });
      }

    }
  }
})