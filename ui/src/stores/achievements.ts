import { defineStore, acceptHMRUpdate } from "pinia";
import { handleApiError } from "@/utils/api";
import type * as api from "printnanny-api-client";
import { useAccountStore } from "./account";

export const useAchievementsStore = defineStore({
  id: "achievements",
  state: () => ({
    achievements: [] as Array<api.Achievement>,
  }),
  actions: {
    async fetchAchievements() {
      const accountStore = useAccountStore();
      const res = await accountStore.achievementsApi
        .achievementsList()
        .catch(handleApiError);
      console.log("Fetched achievements:", res);
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
