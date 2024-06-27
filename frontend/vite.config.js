import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import envCompatible from "vite-plugin-env-compatible";
import md from "vite-plugin-md";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    envCompatible(),
    md({
      // 其他选项...
      markdownItOptions: {
        xhtmlOut: true,
        breaks: true,
        linkify: true,
        typographer: true,
        langPrefix: "language-",
      },
      include: ["./src/posts/*.md"], // 要导入的Markdown文件路径
      wrapperClasses: "markdown-body",
      fileExtensions: ["md", "mdx"],
      evergreen: true,
      headEnabled: true,
      markdownSrcDir: "posts",
      markdownItSetup(md) {
        md.use(require("remark-gfm"));
      },
    }),
  ],
  build: {
    chunkSizeWarningLimit: 2048 * 2048, // 1MB
  },
});
