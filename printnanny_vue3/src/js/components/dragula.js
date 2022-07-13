
import dragula from 'dragula';

class Dragula {

    constructor() {

    }

    init = function () {

        document.querySelectorAll("[data-plugin=dragula]")
          .forEach(function (element) {

              const containersIds =  JSON.parse( element.getAttribute('data-containers'));
              let containers = [];
              if (containersIds) {
                  for (let i = 0; i < containersIds.length; i++) {
                      containers.push(document.querySelectorAll("#" + containersIds[i])[0]);
                  }
              } else {
                  containers = [element];
              }

              // if handle provided
              const handleClass = element.getAttribute('data-handleclass');

              // init dragula
              if (handleClass) {
                  dragula(containers, {
                      moves: function (el, container, handle) {
                          return handle.classList.contains(handleClass);
                      }
                  });
              } else {
                  dragula(containers);
              }

          });

    }


}

export default Dragula;
