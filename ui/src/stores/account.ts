import type { UiError } from "@/types";
import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import * as apiTypes from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import { XIcon } from '@heroicons/vue/solid'

const apiConfig = new api.Configuration({
  basePath: window.location.origin,
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});
const accountsApi = api.AccountsApiFactory(apiConfig);


export const useAccountStore = defineStore({
  id: "accounts",
  state: () => ({
    /** @type { api.User } */
    user: {},
    /** @type { api.RequiredError } */
    apiError: {}
  }),
  actions: {
    async resendVerificationEmail(email: string) {
      console.log("Resending verification email to: ", email)
    },
    /**
     * Attempt to login a user
     * @param {api.LoginRequest} request
     */
    async login(request: api.LoginRequest) {
      try {
        const userData = await accountsApi.accountsLoginCreate(request);
        console.log("User data received", userData);

      }
      catch (e: any) {
        if (e.isAxiosError) {
          const alerts = useAlertStore();
          const alert: UiError = {
            header: e.response.statusText,
            message: e.response.data.detail,
            error: e,
          }

          switch (e.response.data.detail) {
            case 'User account not verified.': {
              let action: AlertAction = {
                color: "indigo",
                text: "📧 Re-send verification email",
                onClick: () => this.resendVerificationEmail(request.email)
              }
              alert.actions = [action]
            }
            default: {
              break;
            }
          }
          alerts.push(alert);
          console.error(e.response)
        } else {
          throw e;
        }
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAccountStore, import.meta.hot));
}
