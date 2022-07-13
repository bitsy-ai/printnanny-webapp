/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Main Js
 */

import {Tooltip,Toast,Popover} from 'bootstrap';
import LayoutThemeApp from './layout/index';
import 'simplebar';

import '../scss/app.scss';
// To enable dark mode, uncomment below line and comment above line
// import '../scss/app-dark.scss';
import '../scss/icons.scss';
import Portlet from "./components/portlet";
import HLJSApi from 'highlight.js';



class App {

    constructor() {
        this.body = document.body;
        this.window = window;
        this.layoutThemeApp = new LayoutThemeApp();

        this.entityMap = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': '&quot;',
            "'": '&#39;',
            "/": '&#x2F;'
        };


    }

    fadeOutEffect(fadeTarget,slow=true)
    {
        if(fadeTarget===null)
            return;
        fadeTarget.style.opacity = 1;

        const opacitySpeed = slow? 0.05 : 0.2;
        const timeSpeed = slow? 80 : 100;

        var fadeEffect = setInterval(function() {
            if (fadeTarget.style.opacity < opacitySpeed)
            {
                fadeTarget.style.display = "none";
                clearInterval(fadeEffect);
            }
            else
            {
                fadeTarget.style.opacity -= opacitySpeed;
            }
        }, timeSpeed);
    }

    init = () => {
        this.layoutThemeApp.init();
        this.initSyntaxHighlight();
        this.initToast();
        this.initPopover();
        this.initTooltip();
        new Portlet().init();
        this.preloader();
        this.loading();
        this.initShowHidePassword();
    }

    loading(){
        const self = this;
        // remove loading
        setTimeout(function () {
            self.body.classList.remove('loading');
        }, 400);
    }

    preloader(){
        const self = this;
        const status = document.getElementById('status');
        this.fadeOutEffect(status);
        setTimeout(function (){
            const preLoader = document.getElementById('preloader');
            self.fadeOutEffect(preLoader,false);
        },1000);
    }

    initSyntaxHighlight() {

        document.querySelectorAll("pre span.escape").forEach(function (element, n) {
            let i;
            let text;
            if (element.classList.contains("escape")) {
                text = element.innerText;
            } else {
                text = element.innerText;
            }
            text = text.replace(/^\n/, '').trimRight();// goodbye starting whitespace
            let to_kill = Infinity;
            let lines = text.split('\n');
            for (i = 0; i < lines.length; i++) {
                if (!lines[i].trim()) { continue; }
                to_kill = Math.min(lines[i].search(/\S/), to_kill);
            }
            const out = [];
            for (i = 0; i < lines.length; i++) {
                out.push(lines[i].replace(new RegExp("^ {" + to_kill + "}", "g"), ""));
            }
            element.innerText = out.join("\n");
        });

        document.querySelectorAll('pre span.escape').forEach(function (block) {
            HLJSApi.highlightElement(block);
        });
    }


    initTooltip(){

        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new Tooltip(tooltipTriggerEl)
        })

    }

    initPopover(){
        var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
        var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
            return new Popover(popoverTriggerEl)
        })
    }

    initToast(){
        var toastElList = [].slice.call(document.querySelectorAll('.toast'))
        var toastList = toastElList.map(function (toastEl) {
            return new Toast(toastEl)
        })
    }


    initShowHidePassword = function () {
        document.querySelectorAll("[data-password]").forEach(function (element){
            element.addEventListener('click',function (event){
               if(element.getAttribute("data-password")=="false"){
                    element.parentElement.querySelector('input').setAttribute("type","text");
                    element.setAttribute("data-password","true");
                    element.classList.add("show-password");
               }else{
                   element.parentElement.querySelector('input').setAttribute("type","password");
                   element.setAttribute("data-password","false");
                   element.classList.remove("show-password");
                }
            });
        });

        // $().on('click', function () {
        //     if ($(this).attr('data-password') == "false") {
        //         $(this).siblings("input").attr("type", "text");
        //         $(this).attr('data-password', 'true');
        //         $(this).addClass("show-password");
        //     } else {
        //         $(this).siblings("input").attr("type", "password");
        //         $(this).attr('data-password', 'false');
        //         $(this).removeClass("show-password");
        //     }
        // });
    }

}


window.addEventListener('load', function () {
    window.app = new App();
    window.app.init();
})
