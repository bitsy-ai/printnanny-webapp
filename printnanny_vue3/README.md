# Hyper JS - Saas Demo
We would like to thank you for purchasing Hyper :). The following guideline will help you to get started with the hyper.
 



## Features

- Support **ES6** Syntax (**Babel 7**)
- Webpack production building (**code splitting**, **cache**, **lazy-loading**)

#
## Setup
You'll need to install `Node.js`, `Yarn` and `Git` before using our included gulpfile.js. Note that the detailed instructions are available in `docs/index.html` too.

To install `Node` visit [https://nodejs.org/download](https://nodejs.org/download/).

To install `Yarn`, visit [https://yarnpkg.com/lang/en/](https://yarnpkg.com/lang/en/).

To install `Git`, visit [https://git-scm.com/](https://git-scm.com/).

#
Now you are ready to setup Hyper, just open your terminal, go to the webpack folder and run below command:

```
yarn install
```
#

From here on out, simply run following command to start the development server. It watches for any changes in your code, including your html, javascript, sass, etc. The development server is accessible at `http://localhost:8080`.

```
yarn dev
```

#

In order to make a production ready build, you can run below command. It bundles everything for production use and optimizes the build for the best performance. The build is minified and the filenames include the hashes.

```
yarn build
```
