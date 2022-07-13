/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Form-Wizard
 */

import Tab from 'bootstrap/js/src/tab';

class Wizard {

  constructor({
    elementId,
    buttonWizard = false,
    progressBar = false,
    formValidation = false
  }) {
    this.formValidation = formValidation;
    this.buttonWizard = buttonWizard;
    this.id = elementId;
    this.wizard = document.getElementById(elementId);
    this.navItems = this.wizard.querySelectorAll('ul li.nav-item a');
    this.tabPans = this.wizard.querySelectorAll('.tab-content .tab-pane');

    this.prevBtn = buttonWizard ? this.wizard.querySelector('.tab-content .button-previous') : this.wizard.querySelector('.tab-content .previous a');
    this.nextBtn = buttonWizard ? this.wizard.querySelector('.tab-content .button-next') : this.wizard.querySelector('.tab-content .next a');
    this.firstBtn = buttonWizard ? this.wizard.querySelector('.tab-content .button-first') : this.wizard.querySelector('.tab-content .first a');
    this.lastBtn = buttonWizard ? this.wizard.querySelector('.tab-content .button-last') : this.wizard.querySelector('.tab-content .last a');

    this.progressBar = progressBar ? this.wizard.querySelector('.tab-content .progress .progress-bar') : null;

    this.selectedIndex = 0;

    this.init();

  }

  init() {
    const self = this;

    this.showTabSelectedTab();

    if (this.prevBtn) {
      this.prevBtn.addEventListener('click', function (e) {
        e.preventDefault();
        if (self.selectedIndex > 0 && self.validateForm()) {
          self.selectedIndex--;
          self.showTabSelectedTab();
        }
      });
    }

    if (this.nextBtn) {
      this.nextBtn.addEventListener('click', function (e) {
        e.preventDefault();
        if (self.selectedIndex < self.navItems.length - 1 && self.validateForm()) {
          self.selectedIndex++;
          self.showTabSelectedTab();
        }
      });
    }

    if (this.firstBtn) {
      this.firstBtn.addEventListener('click', function (e) {
        e.preventDefault();
        if (self.selectedIndex !== 0 && self.validateForm()) {
          self.selectedIndex = 0;
          self.showTabSelectedTab();
        }
      });
    }

    if (this.lastBtn) {
      this.lastBtn.addEventListener('click', function (e) {
        e.preventDefault();
        if (self.selectedIndex !== self.navItems.length - 1 && self.validateForm()) {
          self.selectedIndex = self.navItems.length - 1;
          self.showTabSelectedTab();
        }
      });
    }

    this.navItems.forEach(function (element, index) {
      element.addEventListener('click', function (event) {
        self.selectedIndex = index;
        if (self.validateForm()) {

          self.showTabSelectedTab();
        }
      });
    });

  }

  validateForm() {
    if (this.formValidation) {
      const form = this.tabPans[this.selectedIndex].querySelector('form');
      form.classList.add('was-validated');
      return form.checkValidity();
    }
    return true;
  }

  changeBtnStyle() {
    if (this.buttonWizard) {
      this.lastBtn.classList.remove('disabled');
      this.firstBtn.classList.remove('disabled');
      this.nextBtn.classList.remove('disabled');
      this.prevBtn.classList.remove('disabled');
      if (this.selectedIndex === 0) {
        this.prevBtn.classList.add('disabled');
        this.firstBtn.classList.add('disabled');
      } else if (this.selectedIndex === this.navItems.length - 1) {
        this.nextBtn.classList.add('disabled');
        this.lastBtn.classList.add('disabled');
      }
    }
  }

  showTabSelectedTab() {
    new Tab(this.navItems[this.selectedIndex]).show();
    if (this.progressBar) {
      this.progressBar.style.width = ((this.selectedIndex + 1) / this.navItems.length * 100).toString() + '%';
    }
    this.changeBtnStyle();
  }

}

export default Wizard;
