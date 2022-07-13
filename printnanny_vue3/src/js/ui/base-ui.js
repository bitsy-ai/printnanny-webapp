/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

import 'simplebar/dist/simplebar';

class BaseUi {
  constructor() {

  }

  init() {

    // Alert
    var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
    var alertTrigger = document.getElementById('liveAlertBtn')

    function alert(message, type) {
      var wrapper = document.createElement('div')
      wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'

      alertPlaceholder.append(wrapper)
    }

    if (alertTrigger) {
      alertTrigger.addEventListener('click', function () {
        alert('Nice, you triggered this alert message!', 'success')
      })
    }


    var toastPlacement = document.getElementById("toastPlacement");
    if (toastPlacement) {
      document.getElementById("selectToastPlacement").addEventListener("change", function () {
        if (!toastPlacement.dataset.originalClass) {
          toastPlacement.dataset.originalClass = toastPlacement.className;
        }
        toastPlacement.className = toastPlacement.dataset.originalClass + " " + this.value;
      });
    }
  }
}

// init the dashboard
new BaseUi().init();
