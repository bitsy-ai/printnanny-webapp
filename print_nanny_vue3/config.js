{
  mode: 'development',
  context: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3',
  devtool: 'cheap-module-eval-source-map',
  node: {
    setImmediate: false,
    dgram: 'empty',
    fs: 'empty',
    net: 'empty',
    tls: 'empty',
    child_process: 'empty'
  },
  output: {
    path: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_webapp/static/vue',
    filename: '[name].js',
    publicPath: 'http://localhost:8080/',
    globalObject: 'this'
  },
  resolve: {
    symlinks: false,
    alias: {
      '@': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src',
      vue$: 'vue/dist/vue.runtime.esm.js',
      __STATIC__: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_webapp/static',
      '@src': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src',
      '@router': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/router',
      '@views': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/router/views',
      '@layouts': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/router/layouts',
      '@routes': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/router/routes',
      '@components': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/components',
      '@assets': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/assets',
      '@utils': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/utils',
      '@state': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/state',
      '@store': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/store',
      '@design': '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/design/app.scss',
      '@print-nanny-client': '/home/leigh/projects/octoprint-nanny-webapp/clients/typescript'
    },
    extensions: [
      '.mjs',
      '.js',
      '.jsx',
      '.vue',
      '.json',
      '.wasm'
    ],
    modules: [
      'node_modules',
      '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules',
      '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/@vue/cli-service/node_modules'
    ]
  },
  resolveLoader: {
    modules: [
      '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/@vue/cli-plugin-eslint/node_modules',
      '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/@vue/cli-plugin-babel/node_modules',
      'node_modules',
      '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules',
      '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/@vue/cli-service/node_modules'
    ]
  },
  devServer: {
    'public': 'http://localhost:8080',
    host: 'localhost',
    port: 8080,
    hotOnly: true,
    watchOptions: {
      poll: 1000
    },
    https: false,
    headers: {
      'Access-Control-Allow-Origin': [
        '*'
      ]
    }
  },
  module: {
    noParse: /^(vue|vue-router|vuex|vuex-router-sync)$/,
    rules: [
      /* config.module.rule('vue') */
      {
        test: /\.vue$/,
        use: [
          {
            loader: 'cache-loader',
            options: {
              cacheDirectory: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/.cache/vue-loader',
              cacheIdentifier: '6b9cbc53'
            }
          },
          {
            loader: 'vue-loader',
            options: {
              compilerOptions: {
                preserveWhitespace: false
              },
              cacheDirectory: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/.cache/vue-loader',
              cacheIdentifier: '6b9cbc53'
            }
          }
        ]
      },
      /* config.module.rule('images') */
      {
        test: /\.(png|jpe?g|gif|webp)(\?.*)?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 4096,
              fallback: {
                loader: 'file-loader',
                options: {
                  name: 'img/[name].[ext]'
                }
              }
            }
          }
        ]
      },
      /* config.module.rule('svg') */
      {
        test: /\.(svg)(\?.*)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: 'img/[name].[ext]'
            }
          }
        ]
      },
      /* config.module.rule('media') */
      {
        test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 4096,
              fallback: {
                loader: 'file-loader',
                options: {
                  name: 'media/[name].[ext]'
                }
              }
            }
          }
        ]
      },
      /* config.module.rule('fonts') */
      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/i,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 4096,
              fallback: {
                loader: 'file-loader',
                options: {
                  name: 'fonts/[name].[ext]'
                }
              }
            }
          }
        ]
      },
      /* config.module.rule('pug') */
      {
        test: /\.pug$/,
        oneOf: [
          /* config.module.rule('pug').oneOf('pug-vue') */
          {
            resourceQuery: /vue/,
            use: [
              {
                loader: 'pug-plain-loader'
              }
            ]
          },
          /* config.module.rule('pug').oneOf('pug-template') */
          {
            use: [
              {
                loader: 'raw-loader'
              },
              {
                loader: 'pug-plain-loader'
              }
            ]
          }
        ]
      },
      /* config.module.rule('css') */
      {
        test: /\.css$/,
        oneOf: [
          /* config.module.rule('css').oneOf('vue-modules') */
          {
            resourceQuery: /module/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('css').oneOf('vue') */
          {
            resourceQuery: /\?vue/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('css').oneOf('normal-modules') */
          {
            test: /\.module\.\w+$/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('css').oneOf('normal') */
          {
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          }
        ]
      },
      /* config.module.rule('postcss') */
      {
        test: /\.p(ost)?css$/,
        oneOf: [
          /* config.module.rule('postcss').oneOf('vue-modules') */
          {
            resourceQuery: /module/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('postcss').oneOf('vue') */
          {
            resourceQuery: /\?vue/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('postcss').oneOf('normal-modules') */
          {
            test: /\.module\.\w+$/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('postcss').oneOf('normal') */
          {
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          }
        ]
      },
      /* config.module.rule('scss') */
      {
        test: /\.scss$/,
        oneOf: [
          /* config.module.rule('scss').oneOf('vue-modules') */
          {
            resourceQuery: /module/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  }
                }
              }
            ]
          },
          /* config.module.rule('scss').oneOf('vue') */
          {
            resourceQuery: /\?vue/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  }
                }
              }
            ]
          },
          /* config.module.rule('scss').oneOf('normal-modules') */
          {
            test: /\.module\.\w+$/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  }
                }
              }
            ]
          },
          /* config.module.rule('scss').oneOf('normal') */
          {
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  }
                }
              }
            ]
          }
        ]
      },
      /* config.module.rule('sass') */
      {
        test: /\.sass$/,
        oneOf: [
          /* config.module.rule('sass').oneOf('vue-modules') */
          {
            resourceQuery: /module/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  },
                  indentedSyntax: true
                }
              }
            ]
          },
          /* config.module.rule('sass').oneOf('vue') */
          {
            resourceQuery: /\?vue/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  },
                  indentedSyntax: true
                }
              }
            ]
          },
          /* config.module.rule('sass').oneOf('normal-modules') */
          {
            test: /\.module\.\w+$/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  },
                  indentedSyntax: true
                }
              }
            ]
          },
          /* config.module.rule('sass').oneOf('normal') */
          {
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                  implementation: {
                    run_: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    render: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    renderSync: function(){return b(c,Array.prototype.slice.apply(arguments))},
                    info: 'dart-sass\t1.19.0\t(Sass Compiler)\t[Dart]\ndart2js\t2.2.0\t(Dart Compiler)\t[Dart]',
                    types: {
                      Boolean: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Color: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      List: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Map: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Null: function(){return b(c,Array.prototype.slice.apply(arguments))},
                      Number: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      String: function(){return b(c,this,Array.prototype.slice.apply(arguments))},
                      Error: function Error() { [native code] }
                    }
                  },
                  indentedSyntax: true
                }
              }
            ]
          }
        ]
      },
      /* config.module.rule('less') */
      {
        test: /\.less$/,
        oneOf: [
          /* config.module.rule('less').oneOf('vue-modules') */
          {
            resourceQuery: /module/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'less-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('less').oneOf('vue') */
          {
            resourceQuery: /\?vue/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'less-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('less').oneOf('normal-modules') */
          {
            test: /\.module\.\w+$/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'less-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          },
          /* config.module.rule('less').oneOf('normal') */
          {
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'less-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          }
        ]
      },
      /* config.module.rule('stylus') */
      {
        test: /\.styl(us)?$/,
        oneOf: [
          /* config.module.rule('stylus').oneOf('vue-modules') */
          {
            resourceQuery: /module/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'stylus-loader',
                options: {
                  sourceMap: true,
                  preferPathResolver: 'webpack'
                }
              }
            ]
          },
          /* config.module.rule('stylus').oneOf('vue') */
          {
            resourceQuery: /\?vue/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'stylus-loader',
                options: {
                  sourceMap: true,
                  preferPathResolver: 'webpack'
                }
              }
            ]
          },
          /* config.module.rule('stylus').oneOf('normal-modules') */
          {
            test: /\.module\.\w+$/,
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2,
                  modules: true,
                  localIdentName: '[name]_[local]_[hash:base64:5]'
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'stylus-loader',
                options: {
                  sourceMap: true,
                  preferPathResolver: 'webpack'
                }
              }
            ]
          },
          /* config.module.rule('stylus').oneOf('normal') */
          {
            use: [
              {
                loader: 'vue-style-loader',
                options: {
                  sourceMap: true,
                  shadowMode: false
                }
              },
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true,
                  importLoaders: 2
                }
              },
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true
                }
              },
              {
                loader: 'stylus-loader',
                options: {
                  sourceMap: true,
                  preferPathResolver: 'webpack'
                }
              }
            ]
          }
        ]
      },
      /* config.module.rule('js') */
      {
        test: /\.m?jsx?$/,
        exclude: [
          function () { /* omitted long function */ }
        ],
        use: [
          {
            loader: 'cache-loader',
            options: {
              cacheDirectory: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/.cache/babel-loader',
              cacheIdentifier: '6114ebd5'
            }
          },
          {
            loader: 'babel-loader'
          }
        ]
      },
      /* config.module.rule('eslint') */
      {
        enforce: 'pre',
        test: /\.(vue|(j|t)sx?)$/,
        exclude: [
          /node_modules/,
          '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/@vue/cli-service/lib'
        ],
        use: [
          {
            loader: 'eslint-loader',
            options: {
              extensions: [
                '.js',
                '.jsx',
                '.vue'
              ],
              cache: true,
              cacheIdentifier: '7811395a',
              emitWarning: true,
              emitError: false,
              eslintPath: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/node_modules/eslint/lib/api.js',
              formatter: function () { /* omitted long function */ }
            }
          }
        ]
      },
      /* config.module.rule('ts') */
      {
        use: [
          {
            loader: 'ts-loader'
          }
        ]
      }
    ]
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'chunk-vendors',
          chunks: 'all',
          priority: 1
        }
      }
    }
  },
  plugins: [
    /* config.plugin('vue-loader') */
    new VueLoaderPlugin(),
    /* config.plugin('define') */
    new DefinePlugin(
      {
        'process.env': {
          NODE_ENV: '"development"',
          BASE_URL: '"http://localhost:8080/"'
        }
      }
    ),
    /* config.plugin('case-sensitive-paths') */
    new CaseSensitivePathsPlugin(),
    /* config.plugin('friendly-errors') */
    new FriendlyErrorsWebpackPlugin(
      {
        additionalTransformers: [
          function () { /* omitted long function */ }
        ],
        additionalFormatters: [
          function () { /* omitted long function */ }
        ]
      }
    ),
    /* config.plugin('hmr') */
    new HotModuleReplacementPlugin(),
    /* config.plugin('progress') */
    new ProgressPlugin(),
    /* config.plugin('copy') */
    new CopyWebpackPlugin(
      [
        {
          from: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/public',
          to: '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_webapp/static/vue',
          toType: 'dir',
          ignore: [
            '.DS_Store'
          ]
        }
      ]
    ),
    /* config.plugin('BundleTracker') */
    new BundleTrackerPlugin(
      {
        filename: '../vue_frontend3/webpack-stats.json'
      }
    ),
    /* config.plugin('VueLoaderPlugin') */
    new VueLoaderPlugin()
  ],
  entry: {
    vue_alerts_dropdown: [
      '/home/leigh/projects/octoprint-nanny-webapp/print_nanny_vue3/src/apps/alertsDropdown.js'
    ]
  },
  name: 'Hyper - Vue js Admin Template',
  performance: {
    hints: false
  }
}
