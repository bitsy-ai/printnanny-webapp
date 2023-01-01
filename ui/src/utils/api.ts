import * as api from "printnanny-api-client";
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
    const container = { message: "", error_uuid: "" };
    if (
      e.response?.data.non_field_errors &&
      e.response?.data.non_field_errors.length > 0
    ) {
      message = e.response.data.non_field_errors.join("\n");
      container["message"] = e.response.data.non_field_errors.join("\n");
    } else if (e.response?.data.detail) {
      container["message"] = e.response.data.detail;
    } else if (e.response?.data.error) {
      container["message"] = e.response.data.error;
    } else {
      container["message"] = e.response?.data;
    }

    if (e.response?.data?.error_uuid) {
      container["error_uuid"] = e.response?.data?.error_uuid;
    }
    message = JSON.stringify(container, null, 2);
  }
  const alert: UiAlert = {
    header,
    message,
    error: e,
    actions: [],
  };
  alerts.push(alert);
}

export { handleApiError };
