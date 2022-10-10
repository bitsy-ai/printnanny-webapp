import type { UiAlert } from "@/types";
import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import { ApiConfig, handleApiError } from "@/utils/api";
const accountsApi = api.AccountsApiFactory(ApiConfig);

export const useAccountStore = defineStore({
  id: "accounts",
  // persist option provided by: https://github.com/prazdevs/pinia-plugin-persistedstate
  persist: {
    storage: sessionStorage,
  },
  state: () => ({
    user: undefined as api.User | undefined,
    nkey: undefined as api.NatsOrganizationUser | undefined,
  }),
  getters: {
    isAuthenticated: (state) => state.user !== undefined,
  },
  actions: {
    async submitEmailWaitlist(email: string) {
      const alerts = useAlertStore();
      const req: api.EmailWaitlistRequest = { email };
      const res = await accountsApi
        .accountsEmailWaitlistCreate(req)
        .catch(handleApiError);
      console.debug("accountsEmailWaitlistCreate response", res);
      const alert: UiAlert = {
        header: "Thanks for signing up!",
        error: undefined,
        message: `When beta spots open, we'll send an email to: ${email}`,
        actions: [],
      };
      alerts.push(alert);
    },
    async fetchUserNkey(): Promise<api.NatsOrganizationUser | undefined> {
      const nkeyData = await accountsApi
        .accountsUserNkeyRetrieve()
        .catch(handleApiError);
      console.log("Loaded NATS identity", nkeyData);
      if (nkeyData && nkeyData.data) {
        this.$patch({
          nkey: nkeyData.data,
        });
        return nkeyData.data;
      }
    },
    async fetchUser() {
      const userData = await accountsApi.accountsUserRetrieve().catch(handleApiError);
      if (userData && userData.data) {
        console.log("Authenticated as user", userData.data);
        this.$patch({
          user: userData.data,
        });
        return userData.data;
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
      await accountsApi.accountsLoginCreate(request).catch(handleApiError);
      await this.fetchUser();
      await this.$router.push({ name: "devices" });
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
      await accountsApi.accountsLogoutCreate().catch(handleApiError);
      this.$reset();
      console.info("Successfully logged out");
    },

    async createAccount(
      request: api.RegisterRequest
    ): Promise<undefined | api.User> {
      await accountsApi
        .accountsRegistrationCreate(request)
        .catch(handleApiError);
      await accountsApi
        .accountsLoginCreate({
          email: request.email,
          password: request.password1,
        } as api.LoginRequest)
        .catch(handleApiError);
      const user = await this.fetchUser();
      return user;
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAccountStore, import.meta.hot));
}
