const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const argv = require('yargs').argv;
const webpack = require('webpack');

let isProduction = process.env.NODE_ENV === 'production';
if (argv.production) {
    isProduction = true;
}

/**
 * Webpack configuration
 * Run using 'webpack'
 */
module.exports = {
    // Path to the js entry point (source).
    entry: {
        // javascript
        main: `${__dirname}/src/langerak_gkv/js/index.js`,
        // CSS
        'screen-css': `${__dirname}/src/langerak_gkv/sass/screen.scss`
    },

    // Path to the (transpiled) js & CSS
    output: {
        path: `${__dirname}/src/langerak_gkv/static/bundles/`, // directory
        filename: '[name].js', // file
        chunkFilename: '[name].bundle.js',
        publicPath: '/static/bundles',
    },

    plugins: [
        new MiniCssExtractPlugin(),
    ],

    // Add babel (see .babelrc for settings)
    module: {
        rules: [
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: ['file-loader']
            },
            {
                test: /\.js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        cacheDirectory: true
                    }
                }
            },
            {
                test: /\.(woff|woff2|eot|ttf)$/,
                loader: 'url-loader'
            },
            // scss
            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                    // Writes css files.
                    MiniCssExtractPlugin.loader,

                    // Loads CSS files.
                    {
                        loader: "css-loader",
                        options: {
                            url: false
                        }
                    },

                    // Runs postcss configuration (postcss.config.js).
                    {
                        loader: "postcss-loader"
                    },

                    // Compiles .scss to .css.
                    {
                        loader: "sass-loader",
                        options: {
                            sassOptions: {
                                comments: false,
                                style: "compressed"
                            },
                            sourceMap: argv.sourcemap
                        }
                    }
                ]
            }
        ]
    },

    // Use --production to optimize output.
    mode: isProduction ? 'production' : 'development',

    // Use --sourcemap to generate sourcemap.
    devtool: argv.sourcemap ? 'eval-source-map' : false,
}
