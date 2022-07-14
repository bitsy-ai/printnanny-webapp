import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

const { resolve } = require("path");

// https://vitejs.dev/config/
export default defineConfig({
  base: '/static/bundler/',
  root: resolve('./src'),
  server: {
    host: 'localhost',
    port: 3000,
    open: false,
  },
  build: {
    outDir: resolve('./dist'),
    manifest: true,
    rollupOptions: {
      input: {
        landing: resolve('./src/apps/landing.ts'),

      },
      // output: {
      //   chunkFileNames: undefined,
      // },
    }
  },
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})