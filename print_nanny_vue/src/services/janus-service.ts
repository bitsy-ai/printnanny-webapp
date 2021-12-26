import { promisify } from "util";
import Janus from 'janus'
import { InitOptions } from 'janus'

// Janus.init[promisify.custom]: Promise = (options: InitOptions) => {
//     return new Promise((resolve, reject) => {
//         options.callback = (typeof options.callback == "function") ? () => { resolve(options.callback()) } : resolve;
//     });
// };
function initPromise(options: InitOptions) {
    return new Promise((resolve, reject) => {
        options.callback = resolve
        Janus.init(options)
    })
}

Janus.init = initPromise

export default Janus