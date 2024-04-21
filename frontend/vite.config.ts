import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig(() => {
  return {
    plugins: [react()],
    build: {
      outDir: "build",
      assetsDir: "assets",
      emptyOutDir: true,
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
    server: {
      // proxy to flask backend
      proxy: {
        "/api": {
          // target: "http://127.0.0.1:5000", // localhost
          target: "http://<docker service name>>:5000", // When using docker-compose
          changeOrigin: true,
        },
      },
    },
  };
});
