import { defineStore, acceptHMRUpdate } from "pinia";
import { handleApiError } from "@/utils/api";
import type { UiAlert } from "@/types";
import { useAccountStore } from "./account";
import type * as api from "printnanny-api-client";
import { success } from "./alerts";

export const useDemoStore = defineStore({
  id: "demo",
  state: () => ({
    demo: undefined as undefined | api.DemoSubmission,
    loading: false,
    saved: false,
  }),
  getters: {},
  actions: {
    async load(demoId: string): Promise<api.DemoSubmission | undefined> {
      const account = useAccountStore();
      const res = await account.demosApi
        .demosRetrieve(demoId)
        .catch(handleApiError);
      if (res) {
        this.$patch({ demo: res.data });
        return res.data;
      }
    },
    async submit(email: string, filename: string) {
      const account = useAccountStore();
      const res = await account.demosApi
        .demosCreate(email, filename)
        .catch(handleApiError);
      if (res) {
        success(
          "Success! Your submission is queued",
          `We'll email you at ${email} when your results are ready.`
        );
      }
    },
    async handleFeedback(
      demoId: string,
      label: string,
      feedback: api.DemoFeedbackEnum
    ) {
      const account = useAccountStore();
      console.debug(`handling label=${label} feedback=${feedback}`);

      const field = `feedback_${label}`;
      this.$patch({
        demo: { ...this.demo, [field]: feedback },
        loading: true,
        saved: false,
      });
      const req = {
        [field]: feedback,
      } as api.PatchedDemoSubmissionFeedbackRequest;
      const res = await account.demosApi.demosFeedbackPartialUpdate(
        demoId,
        req
      );
      if (res) {
        console.log("Success! Feedback submitted", res.data);
        this.$patch({ saved: true });
      }
      this.$patch({ loading: false });
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useDemoStore, import.meta.hot));
}
