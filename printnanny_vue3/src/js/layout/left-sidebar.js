import { Collapse } from 'bootstrap';
import Utils from '../components/utils';

class LeftSidebar {

  constructor() {
    this.body = document.getElementsByTagName('body')[0];
    this.window = window;
    this.menuContainer = document.getElementById('#left-side-menu-container');
  }

  initMenu = () => {
    var self = this;

    // resets everything

    // click events// sidebar - main menu
    if (document.querySelectorAll('.side-nav').length) {

      var navCollapse = document.querySelectorAll('.side-nav li .collapse');

      var navToggle = document.querySelectorAll('.side-nav li [data-bs-toggle=\'collapse\']');

      navCollapse.forEach(function (element) {
        element.addEventListener('click', function (e) {
        });
      });

      navCollapse.forEach(element => {
        element.addEventListener('show.bs.collapse', function (e) {
          document.querySelectorAll('.side-nav .collapse.show')
            .forEach(function (singleElement) {
              let parents = Utils.getParentsClosestForLeftbar(element, 'collapse', 'side-nav');
              parents.forEach(function (parentElement) {
                if (singleElement.id !== element.id || singleElement.id !== parentElement.id) {
                  new Collapse(singleElement).hide();
                }

              });
            });
        });
      });

      // activate the menu in left side bar (Vertical Menu) based on url
      document.querySelectorAll('.side-nav a')
        .forEach(function (element, index) {
          var pageUrl = window.location.href.split(/[?#]/)[0];
          const target = element;
          if (element.href == pageUrl) {

            target.classList.add('active');
            target.parentNode.classList.add('menuitem-active');
            target.parentNode.parentNode.parentNode.classList.add('show');
            target.parentNode.parentNode.parentNode.parentNode.classList.add('menuitem-active'); // add active to li of the current link

            var firstLevelParent = target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode;
            if (firstLevelParent.getAttribute('id') !== 'sidebar-menu') {
              firstLevelParent.classList.add('show');
            }

            target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.classList.add('menuitem-active');

            var secondLevelParent = target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode;
            if (secondLevelParent && secondLevelParent.getAttribute('id') !== 'wrapper') {
              secondLevelParent.classList.add('show');
            }

            var upperLevelParent = target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode;
            if (upperLevelParent) {
              upperLevelParent = upperLevelParent.parentNode;
            }

            if (upperLevelParent) {
              upperLevelParent.classList.add('menuitem-active');
            }

          }
        });
    }
  };

  initHorizontalMenu() {
    var AllNavs = document.querySelectorAll('ul.navbar-nav .dropdown .dropdown-toggle');

    var isInner = false;

    AllNavs.forEach(function (element) {
      element.addEventListener('hide.bs.dropdown', function (event) {
        if (isInner) {
          event.preventDefault();
          event.stopPropagation();
          isInner = false;
        } else {
          if (element.parentElement.parentElement.parentElement.children[0].classList.contains('nav-link')) {
            isInner = true;
          }
        }
      });

      element.addEventListener('click', function () {
        if (element.parentElement.parentElement.parentElement.children[0].classList.contains('nav-link')) {
          isInner = true;
        }
      });

      element.addEventListener('show.bs.dropdown', function (event) {
        if (element.parentElement.parentElement.parentElement.children[0].classList.contains('nav-link')) {
          isInner = true;
        }
      });
    });

  }

  init = () => {
    this.initMenu();
    //this.initHorizontalMenu();

  }
}

export default LeftSidebar;
