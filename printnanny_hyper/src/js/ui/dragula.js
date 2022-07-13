/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */
import Dragula from '../components/dragula';

class DragulaExtended {
  constructor() {

  }

  init() {
    new Dragula().init();
  }
}

// init the dashboard
new DragulaExtended().init();
