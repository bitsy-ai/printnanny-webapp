import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import type * as apiTypes from "printnanny-api-client";
import type { Alert } from "@/types";

const apiConfig = new api.Configuration({
    basePath: window.location.origin,
    baseOptions: {
        xsrfCookieName: "csrftoken",
        xsrfHeaderName: "X-CSRFTOKEN",
        withCredentials: true,
    },
});

export const useAlertStore = defineStore({
    id: "alerts",
    state: () => ({
        /** @type { Alert[] } */
        alerts: []
    }),
    actions: {
        push(alert: Alert) {
            this.alerts.push(alert);
        },
        dismiss(alert: Alert) {
            this.$patch({ alerts: this.alerts.filter(a => a !== alert) });
        }
    },
});

if (import.meta.hot) {
    import.meta.hot.accept(acceptHMRUpdate(useAlertStore, import.meta.hot));
}
