const esbuild = require('esbuild');

esbuild.build({
    entryPoints: ["static/scripts/entry.js"],
    bundle: true,
    outfile: "static/bundle.js",
}).catch(() => process.exit(1));
