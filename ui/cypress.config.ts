import { defineConfig } from "cypress";

export default defineConfig({
  projectId: "amsn8j",
  chromeWebSecurity: false,
  modifyObstructiveCode: true,
  experimentalModifyObstructiveThirdPartyCode: true,
  blockHosts: [
    "r.stripe.com",
    "m.stripe.com",
    "analytics.google.com",
    "*google.com",
  ],
  includeShadowDom: true,
  e2e: {
    specPattern: "cypress/e2e/**/*.{cy,spec}.{js,jsx,ts,tsx}",
    baseUrl: "http://localhost:8000",
    experimentalSessionAndOrigin: true,
  },
  component: {
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },
});
