/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */
import Wizard from '../../components/wizard';

class WizardForm {
  constructor() {

  }

  init() {

    new Wizard({
      elementId:'basicwizard'
    });

    new Wizard({
      elementId:'btnwizard',
      buttonWizard:true
    });
    new Wizard({
      elementId:'progressbarwizard',
      progressBar:true
    });


    new Wizard({
      elementId:'rootwizard',
      formValidation:true
    });


  }
}

// init the dashboard
new WizardForm().init();
