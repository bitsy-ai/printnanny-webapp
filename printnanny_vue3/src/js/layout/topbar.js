import { Dropdown } from 'bootstrap';

class Topbar {

    constructor() {
        this.body = document.getElementsByTagName("body")[0];
        this.window = window;
    }

    initMenu = () => {
        if (document.querySelectorAll(".topnav-menu").length) {
            document.querySelectorAll('.topnav-menu li a').forEach(function (element, index) {
                var pageUrl = window.location.href.split(/[?#]/)[0];
                if (element.href == pageUrl) {
                    const target = element;
                    target.classList.add('active');
                    target.parentNode.parentNode.classList.add('active'); // add active to li of the current link
                    target.parentNode.parentNode.parentNode.parentNode.classList.add('active');
                    target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.classList.add('active');
                }
            });

            // Topbar - main menu
            document.querySelector('.navbar-toggle').addEventListener("click", function () {
                this.classList.toggle("open");
                //document.getElementById('#navigation').slideToggle(400);
            });
        }

        //Horizontal Menu (For SM Screen)
        var AllNavs = document.querySelectorAll('ul.navbar-nav .dropdown .dropdown-toggle');

        var isInner = false;

        AllNavs.forEach(function (element) {
            element.addEventListener('click', function (event) {
                if (!element.parentElement.classList.contains('nav-item')) {
                    isInner = true;
                    //element.parentElement.parentElement.classList.add('show');
                    var parent = element.parentElement.parentElement.parentElement.querySelector('.nav-link');
                    Dropdown.getInstance(parent).show();
                    if (element.ariaExpanded === "true") {
                        Dropdown.getInstance(element).hide();
                    }
                    else {
                        Dropdown.getInstance(element).show();
                    }
                    isInner = true;
                }
            });

            element.addEventListener('hide.bs.dropdown', function (event) {
                if (isInner) {
                    event.preventDefault();
                    event.stopPropagation();
                    isInner = false;
                }
            });


            element.addEventListener('show.bs.dropdown', function (event) {
                if (!isInner && !element.parentElement.classList.contains('nav-item')) {
                    event.preventDefault();
                    event.stopPropagation();
                    isInner = true;
                }
            });
        });
    }

    // init search
    initSearch = () => {
        // Search Toggle
        var navDropdowns = document.querySelectorAll('.navbar-custom .dropdown:not(.app-search)');

        // hide on other click
        document.addEventListener('click', function (e) {
            if (document.getElementById('search-dropdown')) {
                if (e.target.id == "top-search" || e.target.closest('#search-dropdown')) {
                    document.getElementById('search-dropdown').classList.add('d-block');
                } else {
                    document.getElementById('search-dropdown').classList.remove('d-block');
                }
            }
            return true;
        });

        // hide search on opening other dropdown

        navDropdowns.forEach(element => {
            element.addEventListener('show.bs.dropdown', function () {
                document.getElementById('search-dropdown').classList.remove('d-block');
            })
        });
    }

    init() {
        this.initMenu();
        this.initSearch()
    }
}

export default Topbar;
