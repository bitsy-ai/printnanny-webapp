import replace from 'rollup-plugin-replace';
import * as fs from 'fs';

export default {
    name: 'Janus',
    input: '_module.js',
    output: {
        strict: false,
        format: 'es',
        file: 'janus.js'
    },
    plugins: [
        replace({
            JANUS_CODE: fs.readFileSync('lib.js', 'utf-8'),
            delimiters: ['@','@'],
        })
    ]
};
