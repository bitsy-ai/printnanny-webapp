import type { UiError } from "@/types";
import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import * as apiTypes from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import { XIcon } from "@heroicons/vue/solid";

const apiConfig = new api.Configuration({
  basePath: window.location.origin,
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});
const accountsApi = api.AccountsApiFactory(apiConfig);
const alertSettingsApi = api.AlertSettingsApi(apiConfig);

export const useAccountStore = defineStore({
  id: "accounts",
  // persist option provided by: https://github.com/prazdevs/pinia-plugin-persistedstate
  persist: true,
  state: () => ({
    user: null,
    apiError: {},
  }),
  getters: {
    isAuthenticated: (state) => state.user !== null,
  },
  actions: {

    async fetchUser() {
      try {
        const userData = await accountsApi.accountsUserRetrieve();
        const user = userData.data;
        console.log("Authenticated as user", user);
        return this.$patch({
          user: user,
          apiError: {},
        });
      } catch (e: any) {
        console.warn("No authentication data is set", e);
        this.$patch({
          /** @type { api.User } */
          user: null,
          /** @type { api.RequiredError } */
          apiError: e,
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
        await accountsApi.accountsLoginCreate(request);
        await this.fetchUser();
        await this.router.push({ name: "dashboard" });
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
          const alert: UiError = {
            header: e.response.statusText,
            message: msg,
            error: e,
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
      if (this.user == null) {
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
