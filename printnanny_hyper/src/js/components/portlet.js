class Portlet {
    constructor() {
        this.body = document.body;
        this.portletIdentifier = ".card";
        this.portletCloser = '.card a[data-toggle="remove"]';
        this.portletRefresher = '.card a[data-toggle="reload"]'
    }
    init = () => {
        this.initRefresher();
        this.initCloser();
    }
    initCloser(){
        const self = this;
        document.querySelectorAll(this.portletCloser).forEach(element => {
            element.addEventListener('click', function (e) {
                e.preventDefault();
                const portlet = element.closest(self.portletIdentifier);
                const portlet_parent = portlet?.parentElement;
                if(portlet)
                    portlet.remove();
                if (portlet_parent?.children.length === 0)
                    portlet_parent?.remove();
                self.init();
            });
        });
    }
    initRefresher(){
        const self = this;
        const elements = document.querySelectorAll(this.portletRefresher);
        elements.forEach(function (element){
            element.addEventListener('click', function (e)  {
                e.preventDefault();
                const portlet = element.closest(self.portletIdentifier);
                if(portlet)
                    portlet.innerHTML += ('<div class="card-disabled"><div class="card-portlets-loader"></div></div>');
                let pd;
                portlet?.children.forEach(element => {
                    if (element.classList.contains('card-disabled'))
                        pd = element;
                });
                setTimeout(function () {
                    pd?.remove();
                    self.init();
                }, 500 + 300 * (Math.random() * 5));
            })
        });
    }
}
export default Portlet;