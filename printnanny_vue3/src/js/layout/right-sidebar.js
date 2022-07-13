class RightSidebar {

  constructor() {
    this.body = document.body;
    this.window = window;
  }


  toggleRightSideBar = () => {
    var self = this;
    self.body.classList.toggle('end-bar-enabled');
  };

  findAncestor(el, cls) {
    while ((el = el.parentElement) && !el.classList.contains(cls));
    return el;
  }

  init() {

    const self = this;

    if (document.querySelector('.button-menu-mobile')) {

      document.querySelector('.button-menu-mobile')
        .addEventListener('click', function (e) {
          e.preventDefault();

          self.body.classList.toggle('sidebar-enable');

          if (self.body.getAttribute('data-layout') === 'full') {
            self.body.classList.toggle('hide-menu');
          }
        });
    }


    document.querySelectorAll('.end-bar-toggle').forEach(function (element) {
      element.addEventListener('click', function () {
        self.toggleRightSideBar();
      });
    });

    self.body.addEventListener('click', function (e) {
      if (e.target.classList.contains('end-bar-toggle') || self.findAncestor(e.target, 'end-bar-toggle')) {
        return;
      }
      if (e.target.classList.contains('button-menu-mobile') || self.findAncestor(e.target, 'button-menu-mobile')) {
        return;
      }
      if (e.target.classList.contains('end-bar') || self.findAncestor(e.target, 'end-bar')) {
        return;
      }

      self.body.classList.remove('end-bar-enabled');
      self.body.classList.remove('sidebar-enable');
    });
  }

}

export default RightSidebar;
