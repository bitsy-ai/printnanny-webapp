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

export { ApiConfig };
