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
    const data = e.response?.data as any;
    if (data.non_field_errors && data?.non_field_errors.length > 0) {
      message = data.non_field_errors.join("\n");
      container["message"] = data.non_field_errors.join("\n");
    } else if (data.detail) {
      container["message"] = data.detail;
    } else if (data.error) {
      container["message"] = data.error;
    } else {
      container["message"] = data;
    }

    if (data.error_uuid) {
      container["error_uuid"] = data.error_uuid;
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
