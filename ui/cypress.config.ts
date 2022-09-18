import { defineConfig } from "cypress";

export default defineConfig({
  chromeWebSecurity: true,
  modifyObstructiveCode: true,
  experimentalModifyObstructiveThirdPartyCode: true,
  blockHosts: ["r.stripe.com", "m.stripe.com"],
  includeShadowDom: true,
  e2e: {
    specPattern: "cypress/e2e/**/*.{cy,spec}.{js,jsx,ts,tsx}",
    baseUrl: "http://localhost:3000",
    experimentalSessionAndOrigin: true,

  },
  component: {
    devServer: {
      framework: 'vue',
      bundler: 'vite'
    }
  },
});
