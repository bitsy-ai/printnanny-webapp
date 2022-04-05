// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: "@babel/eslint-parser",
  },
  env: {
    browser: true,
  },
  extends: [
    // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
    // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
    'plugin:vue/essential',
    // https://github.com/standard/standard/blob/master/docs/RULES-en.md
    'standard'
  ],
  // required to lint *.vue files
  plugins: [
    'vue'
  ],
  // add your custom rules here
  rules: {
    // allow async-await
    'generator-star-spacing': 'off',
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
  },
  overrides: [{
    files: ["*.ts", "*.tsx"],
    parser: "@typescript-eslint/parser",
    plugins: ["@typescript-eslint"],

    // If need to support jsx
    //     parserOptions: {
    //       ecmaFeatures: { jsx: true }
    //     },

    /**
     * Typescript Rules
     * https://github.com/bradzacher/eslint-plugin-typescript
     * Enable your own typescript rules.
     */
    rules: {
      // Prevent TypeScript-specific constructs from being erroneously flagged as unused
      '@typescript-eslint/no-unused-vars': 'error',
      // Require PascalCased class and interface names
      '@typescript-eslint/class-name-casing': 'error',
      // Require a specific member delimiter style for interfaces and type literals
      // Default Semicolon style
      '@typescript-eslint/member-delimiter-style': 'error',
      // Require a consistent member declaration order
      '@typescript-eslint/member-ordering': 'error',
      // Require consistent spacing around type annotations
      '@typescript-eslint/type-annotation-spacing': 'error',
    },
  }]
}
