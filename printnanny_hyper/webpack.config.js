/**
 * Webpack main configuration file
 */
const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const HTMLWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackPartialsPlugin = require('html-webpack-partials-plugin');
const ImageMinimizerPlugin = require('image-minimizer-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const { extendDefaultPlugins } = require('svgo');

const IS_DEV = process.env.NODE_ENV === 'dev';
const environment = require('./configuration/environment');
const HyperConfig = require('./pages.config.js');

const htmlPluginEntries = HyperConfig.pages.map((page) => ([new HTMLWebpackPlugin({
  inject: 'body',
  chunks: page.chunks,
  hash: false,
  chunksSortMode: 'manual',
  filename: page.filename,
  template: path.resolve(environment.paths.source, page.template),
  favicon: path.resolve(environment.paths.source, 'images', 'favicon.ico'),
  minify: !IS_DEV && {
    collapseWhitespace: false,
    preserveLineBreaks: true,
    removeComments: true,
  },
}),
]));
module.exports = {
  entry: HyperConfig.entries,
  output: {
    filename: 'js/[name].js',
    path: environment.paths.output,
  },
  module: {
    rules: [
      {
        test: /\.((c|sa|sc)ss)$/i,
        use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader', 'sass-loader'],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
      {
        test: /\.(png|gif|jpe?g|svg)$/i,
        use: [
          {
            loader: 'url-loader',
            options: {
              name: '[name].[ext]',
              publicPath: '../images',
              limit: environment.limits.images,
            },
          },
        ],
      },
      {
        test: /\.(eot|ttf|woff|woff2)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              name: '[name].[ext]',
              publicPath: '../fonts',
              limit: environment.limits.fonts,
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/[name].css',
    }),
    new ImageMinimizerPlugin({
      test: /\.(jpe?g|png|gif|svg)$/i,
      minimizerOptions: {
        // Lossless optimization with custom option
        // Feel free to experiment with options for better result for you
        plugins: [
          ['gifsicle', { interlaced: true }],
          ['jpegtran', { progressive: true }],
          ['optipng', { optimizationLevel: 5 }],
          [
            'svgo',
            {
              plugins: extendDefaultPlugins([
                {
                  name: 'removeViewBox',
                  active: false,
                },
              ]),
            },
          ],
        ],
      },
    }),
    new CleanWebpackPlugin({
      verbose: true,
      cleanOnceBeforeBuildPatterns: ['*/', '!stats.json'],
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: './src/images',
          to: 'images',
        },
        {
          from: './src/fonts',
          to: 'fonts',
        },
      ],
    }),
  ].concat(...htmlPluginEntries, ...[new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/head-meta.html'),
    priority: 'replace',
    location: 'hyper-head-meta',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/left-sidebar.html'),
    priority: 'replace',
    location: 'hyper-left-sidebar',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/body.html'),
    priority: 'replace',
    location: 'hyper-body',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/footer.html'),
    priority: 'replace',
    location: 'hyper-footer',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/right-sidebar.html'),
    priority: 'replace',
    location: 'hyper-right-sidebar',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/topbar.html'),
    priority: 'replace',
    location: 'hyper-topbar',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/topbar-dark.html'),
    priority: 'replace',
    location: 'hyper-topbar-dark',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/detached-left-sidebar.html'),
    priority: 'replace',
    location: 'hyper-detached-left-sidebar',
    template_filename: '*',
  }),
  new HtmlWebpackPartialsPlugin({
    path: path.join(__dirname, './src/partials/horizontal-nav.html'),
    priority: 'replace',
    location: 'hyper-horizontal-nav',
    template_filename: '*',
  })]),
  target: 'web',
};
