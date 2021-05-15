const appConfig = require('./src/app.config')
const BundleTracker = require("webpack-bundle-tracker");
// const ESLintPlugin = require('eslint-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader')

const path = require('path');
const loader = require('sass-loader');


const pages = {
  'vue_alerts_dropdown': {
      entry: './src/apps/alertsDropdown.js',
      chunks: ['chunk-vendors']
  }
}
/** @type import('@vue/cli-service').ProjectOptions */
module.exports = {
  pages: pages,
  outputDir: '../print_nanny_webapp/static/vue/',
  filenameHashing: false,
  publicPath: process.env.NODE_ENV === 'production'
  ? ''
  : 'http://localhost:8080/',

  configureWebpack: {
    // We provide the app's title in Webpack's name field, so that
    // it can be accessed in index.html to inject the correct title.
    name: appConfig.title,
    // Set up all the aliases we use in our app.
    resolve: {
      alias: require('./aliases.config').webpack,
    },
    performance: {
      // Only enable performance hints for production builds,
      // outside of tests.
      hints:
        process.env.NODE_ENV === 'production' &&
        !process.env.VUE_APP_TEST &&
        'warning',
    },
    // resolve: {
    //   alias: {
    //     '@': path.resolve('src')
    //   }
    // },
  },
  css: {
    // Enable CSS source maps.
    sourceMap: true,
  },

  chainWebpack: config => {

    config.module
    .rule('ts')
    .use('ts-loader')
      .loader('ts-loader')
      .tap(options => {
        // modify the ts options...
        return options
      })
    
    config.module
    .rule('vue')

    .use('vue-loader')
      .loader('vue-loader')
      .tap(options => {
        // modify the options...
        return options
      })

  
    config.optimization
        .splitChunks({
            cacheGroups: {
                vendor: {
                    test: /[\\/]node_modules[\\/]/,
                    name: "chunk-vendors",
                    chunks: "all",
                    priority: 1
                },
            },
        });

    Object.keys(pages).forEach(page => {
        config.plugins.delete(`html-${page}`);
        config.plugins.delete(`preload-${page}`);
        config.plugins.delete(`prefetch-${page}`);
    })

    // config
    //     .plugin('ESLintPlugin')
    //     .use(ESLintPlugin)
    config
        .plugin('BundleTracker')
        .use(BundleTracker, [{filename: '../vue_frontend3/webpack-stats.json'}]);
    // config.plugin('VueLoaderPlugin')
    //     .use(VueLoaderPlugin)
    config.resolve.symlinks(false)
    config.resolve.alias
        .set('__STATIC__', path.resolve(__dirname, '../print_nanny_webapp/static'))


        
    config.devServer
        .public('http://localhost:8080')
        .host('localhost')
        .port(8080)
        .hotOnly(true)
        .watchOptions({poll: 1000})
        .https(false)
        .headers({"Access-Control-Allow-Origin": ["*"]})
  }
}
