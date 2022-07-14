import { defineStore } from "pinia";
import * as api from "printnanny-api-client";

const apiConfig = new api.Configuration({
  basePath: window.location.origin,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})
export const userStore = defineStore({
  id: "user",
  state: () => ({}),
  /**
 * Attempt to login a user
 * @param {string} user
 * @param {string} password
 */
  async login(email: str, password: str) {
    const userData = await apiLogin(user, password)

    this.$patch({
      name: user,
      ...userData,
    })
  },
});
