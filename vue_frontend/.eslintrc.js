module.exports = {
    root: true,
    extends: ['plugin:vue/vue3-recommended' ],
    rules: {
        "@typescript-eslint/no-unused-vars": "warn",
        // Only allow debugger in development
        'no-debugger': process.env.PRE_COMMIT ? 'error' : 'off',
    },
}