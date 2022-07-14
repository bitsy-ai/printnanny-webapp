import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import * as apiTypes from "printnanny-api-client";

const apiConfig = new api.Configuration({
  basePath: window.location.origin,
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});
const accountsApi = api.AccountsApiFactory(apiConfig);

export const useUserStore = defineStore({
  id: "accounts",
  state: () => ({
    user?: apiTypes.User,
  }),
  actions: {
    /**
     * Attempt to login a user
     * @param {api.LoginRequest} request
     */
    async login(request: api.LoginRequest) {
      console.log("Sending login request", request);
      console.log("Logging api import", api);
      const userData = await accountsApi.accountsLoginCreate(request);
      console.log("User data received", userData);
      // this.$patch({
      //   ...userData,
      // });
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot));
}
