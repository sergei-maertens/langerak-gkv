import * as esbuild from 'esbuild';
import {sassPlugin} from 'esbuild-sass-plugin';

await esbuild.build({
  entryPoints: ['src/langerak_gkv/js/index.js'],
  bundle: true,
  minify: true,
  sourcemap: true,
  outfile: 'src/langerak_gkv/static/bundles/main.js',
  plugins: [sassPlugin({
    embedded: true,
  })],
  external: ['*.svg', '*.png'],
})
