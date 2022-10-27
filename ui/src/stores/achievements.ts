import { defineStore, acceptHMRUpdate } from "pinia";
import { ApiConfig, handleApiError } from "@/utils/api";
import * as api from "printnanny-api-client";

const achievementsApi = api.AchievementsApiFactory(ApiConfig);

export const useAchievementsStore = defineStore({
  id: "achievements",
  state: () => ({
    achievements: [] as Array<api.Achievement>,
  }),
  actions: {
    async fetchAchievements() {
      const res = await achievementsApi.achievementsList().catch(handleApiError);

      if (res?.data) {
        this.$patch({ achievements: res.data.results });
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(
    acceptHMRUpdate(useAchievementsStore, import.meta.hot)
  );
}
