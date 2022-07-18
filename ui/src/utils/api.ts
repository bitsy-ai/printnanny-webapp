import * as api from "printnanny-api-client";
const ApiConfig = new api.Configuration({
    basePath: import.meta.env.PRINTNANNY_API_URL || window.location.origin,
    baseOptions: {
        xsrfCookieName: "csrftoken",
        xsrfHeaderName: "X-CSRFTOKEN",
        withCredentials: true,
    },
});

export { ApiConfig }