const path = require('path')
const fs = require('fs')
const prettier = require('prettier')

const aliases = {
  '@': 'src',
  '@src': 'src',
  '@router': 'src/router',
  '@views': 'src/router/views',
  '@layouts': 'src/router/layouts',
  '@routes': 'src/router/routes',
  '@components': 'src/components',
  '@assets': 'src/assets',
  '@utils': 'src/utils',
  '@state': 'src/state',
  '@store': 'src/store',
  '@design': 'src/design/app.scss',
  '@print-nanny-client': '../clients/typescript'
}

module.exports = {
  webpack: {},
  jest: {},
  jsconfig: {},
}

for (const alias in aliases) {
  const aliasTo = aliases[alias]
  module.exports.webpack[alias] = resolveSrc(aliasTo)
  const aliasHasExtension = /\.\w+$/.test(aliasTo)
  module.exports.jest[`^${alias}$`] = aliasHasExtension
    ? `<rootDir>/${aliasTo}`
    : `<rootDir>/${aliasTo}/index.js`
  module.exports.jest[`^${alias}/(.*)$`] = `<rootDir>/${aliasTo}/$1`
  module.exports.jsconfig[alias + '/*'] = [aliasTo + '/*']
  module.exports.jsconfig[alias] = aliasTo.includes('/index.')
    ? [aliasTo]
    : [
        aliasTo + '/index.js',
        aliasTo + '/index.json',
        aliasTo + '/index.vue',
        aliasTo + '/index.scss',
        aliasTo + '/index.css',
      ]
}



function resolveSrc(_path) {
  return path.resolve(__dirname, _path)
}
