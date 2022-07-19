import { fileURLToPath, URL } from "url";
import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
import { execSync } from "child_process";

// reference: https://stackoverflow.com/questions/71162040/how-to-insert-git-info-in-environment-variables-using-vite
// embed git information in vite build
const commitDate = execSync("git log -1 --format=%cI").toString().trimEnd();
const branchName = execSync("git rev-parse --abbrev-ref HEAD")
  .toString()
  .trimEnd();
const commitHash = execSync("git rev-parse HEAD").toString().trimEnd();
const lastCommitMessage = execSync("git show -s --format=%s")
  .toString()
  .trimEnd();

process.env.VITE_GIT_COMMIT_DATE = commitDate;
process.env.VITE_GIT_BRANCH_NAME = branchName;
process.env.VITE_GIT_COMMIT_HASH = commitHash;
process.env.VITE_GIT_LAST_COMMIT_MESSAGE = lastCommitMessage;

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd());
  return {
    server: {
      fs: {
        // Allow serving files from one level up to the project root
        allow: ["../clients/typescript", "src"],
      },
      host: "0.0.0.0",
      cors: false,
      proxy: {
        "/api": {
          target: env.VITE_PRINTNANNY_API_URL,
          changeOrigin: true,
          secure: false,
          ws: true,
        },
      },
    },
    envDir: ".env",
    plugins: [vue(), vueJsx()],
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
  };
});
