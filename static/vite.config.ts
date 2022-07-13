import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

const { resolve } = require("path");

// https://vitejs.dev/config/
// export default defineConfig({
//   base: '/static/bundler/',
//   root: resolve('./src'),
//   server: {
//     host: 'localhost',
//     port: 3000,
//     open: false,
//   },
//   build: {
//     outDir: resolve('./dist'),
//     assetsDir: '',
//     manifest: true,
//     rollupOptions: {
//       input: {
//         main: resolve('./src/main.ts'),
//         bundle: resolve('./src/bundle.ts'),

//       },
//       // output: {
//       //   chunkFileNames: undefined,
//       // },
//     }
//   },
//   plugins: [vue(), vueJsx()],
//   resolve: {
//     alias: {
//       '@': fileURLToPath(new URL('./src', import.meta.url))
//     }
//   }
// })

export default defineConfig({
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
