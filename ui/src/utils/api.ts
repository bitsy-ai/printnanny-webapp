import * as api from "printnanny-api-client";

console.log("Configuring api url: ", import.meta.env.VITE_PRINTNANNY_API_URL);
const ApiConfig = new api.Configuration({
  basePath: import.meta.env.VITE_PRINTNANNY_API_URL,
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});

import axios from "axios";
import type { AxiosError } from "axios";
import { useAlertStore } from "@/stores/alerts";
import type { UiAlert } from "@/types";

function handleApiError(e: Error | AxiosError) {
  console.error(e);
  // handle actione rror
  const alerts = useAlertStore();
  let message = e.toString();
  const header = "Oops, unexpected error";

  if (axios.isAxiosError(e)) {
    message = JSON.stringify(e)
  }
  const alert: UiAlert = {
    header,
    message,
    error: e,
    actions: [],
  };
  alerts.push(alert);
}

export { ApiConfig, handleApiError };
