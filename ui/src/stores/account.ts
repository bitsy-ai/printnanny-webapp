import type { UiAlert } from "@/types";
import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import { useRouter } from "vue-router";
import { ApiConfig } from "@/utils/api";
const accountsApi = api.AccountsApiFactory(ApiConfig);

export const useAccountStore = defineStore({
  id: "accounts",
  // persist option provided by: https://github.com/prazdevs/pinia-plugin-persistedstate
  persist: true,
  state: () => ({
    user: undefined as api.User | undefined,
  }),
  getters: {
    isAuthenticated: (state) => state.user !== undefined,
  },
  actions: {
    async submitEmailWaitlist(email: string) {
      const alerts = useAlertStore();
      try {
        const req: api.EmailWaitlistRequest = { email };
        const res = await accountsApi.accountsEmailWaitlistCreate(req);
        const alert: UiAlert = {
          header: "Thanks for signing up!",
          error: undefined,
          message: `We'll send an email to ${email} when beta spots open. `,
          actions: []

        };
        alerts.push(alert);
      } catch (e: any) {
        if (e.isAxiosError) {
          let msg;
          if (e.response.data.email && e.response.data.email.length > 0) {
            msg = e.response.data.email.join("\n");
          } else if (e.response.data.detail) {
            msg = e.response.data.detail;
          } else {
            msg = e.response.data;
          }
          const alert: UiAlert = {
            header: e.response.statusText,
            message: msg,
            error: e,
            actions: []

          };
          alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
    },
    async fetchUser() {
      try {
        const userData = await accountsApi.accountsUserRetrieve();
        const user = userData.data;
        console.log("Authenticated as user", user);
        return this.$patch({
          user: user,
        });
      } catch (e: any) {
        console.warn("No authentication data is set", e);
        this.$patch({
          user: undefined,
        });
      }
    },
    async resendVerificationEmail(email: string) {
      console.log("Resending verification email to: ", email);
    },
    /**
     * Attempt to login a user
     * @param {api.LoginRequest} request
     */
    async login(request: api.LoginRequest) {
      try {
        const router = useRouter();
        await accountsApi.accountsLoginCreate(request);
        await this.fetchUser();
        await router.push({ name: "dashboard" });
      } catch (e: any) {
        if (e.isAxiosError) {
          const alerts = useAlertStore();
          let msg;
          if (
            e.response.data.non_field_errors &&
            e.response.data.non_field_errors.length > 0
          ) {
            msg = e.response.data.non_field_errors.join("\n");
          } else if (e.response.data.detail) {
            msg = e.response.data.detail;
          } else {
            msg = e.response.data;
          }
          const alert: UiAlert = {
            header: e.response.statusText,
            message: msg,
            error: e,
            actions: []

          };
          alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
    },
    /**
     * Invalidate current session
     */
    async logout() {
      // nothing to do if user not set
      if (this.user == undefined) {
        console.warn("logout action called without user set");
        return;
      }
      await accountsApi.accountsLogoutCreate();
      this.$reset();
      console.debug("Successfully logged out");
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAccountStore, import.meta.hot));
}
