import { Promise } from 'bluebird';

import { default as Janus, JanusJS } from '../vendor/janus'

export const JanusAsync = Promise.promisifyAll(Janus);
export type JanusSessionType = Janus;
export type JanusSessionInit = JanusJS.InitOptions;


class JanusSessionAsync extends JanusAsync {

}

export { JanusSessionAsync }