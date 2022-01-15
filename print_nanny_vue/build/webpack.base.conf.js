'use strict'
const path = require('path')
const utils = require('./utils')
const config = require('../config')
const vueLoaderConfig = require('./vue-loader.conf')
const BundleTracker = require('webpack-bundle-tracker');

function resolve (dir) {
  return path.join(__dirname, '..', dir)
}

const devMode = process.env.NODE_ENV !== 'production';

const createLintingRule = () => ({
  test: /\.(js|vue)$/,
  loader: 'eslint-loader',
  enforce: 'pre',
  include: [resolve('src'), resolve('test')],
  options: {
    formatter: require('eslint-friendly-formatter'),
    emitWarning: !config.dev.showEslintErrorsInOverlay,
    fix: true
  }
})



module.exports = {
  context: path.resolve(__dirname, '../'),
  entry: {
    index: './src/index.js',
    alerts: './src/apps/AlertsDropdown.js',
    taskStatus: './src/apps/TaskStatus.js',
    webCamStream: './src/apps/WebCamStream.js',
    networkScanner: './src/apps/NetworkScanner.js'
  },
  output: {
    path: config.build.assetsRoot,
    filename: 'js/[name].js',
  },
  optimization: {
    moduleIds: 'named',
    splitChunks: {
      cacheGroups: {
        vendor: {
            test: /[\\/]node_modules[\\/]/,
            name: "chunk-vendors",
            chunks: "all",
            priority: 1
        },
      },
    }
  },
  resolve: {
    extensions: ['.js', '.vue', '.json', '.ts', '.tsx'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      '@': resolve('src'),
      '__STATIC__': resolve('../print_nanny_webapp/static')
    },
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],
  module: {
    rules: [
      ...(config.dev.useEslint ? [createLintingRule()] : []),
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: vueLoaderConfig
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        include: [resolve('src'), resolve('test'), resolve('node_modules/webpack-dev-server/client')],
      },
      { 
        test: /\.tsx?$/, 
        loader: "ts-loader",
        include: [resolve('src'), resolve('test'), resolve('node_modules/webpack-dev-server/client')],
      },
      { test: /\.js$/, loader: "source-map-loader" },
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('img/[name].[hash:7].[ext]')
        }
      },
      {
        test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('media/[name].[hash:7].[ext]')
        }
      },
      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.assetsPath('fonts/[name].[hash:7].[ext]')
        }
      },
    ]
  },
  node: {
    // prevent webpack from injecting useless setImmediate polyfill because Vue
    // source contains it (although only uses it if it's native).
    //setImmediate: false,
    // prevent webpack from injecting mocks to Node native modules
    // that does not make sense for the client
    // dgram: 'empty',
    // fs: 'empty',
    // net: 'empty',
    // tls: 'empty',
    // child_process: 'empty'
  }
}
