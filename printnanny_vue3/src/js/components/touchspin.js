/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

class Touchspin {

  constructor() {

  }

  init() {

    document.querySelectorAll('[data-toggle="touchspin"]').forEach(function(touchspin){

      let value = touchspin.getAttribute('value');
      const btsPrefix = touchspin.getAttribute('data-bts-prefix');
      const btsPostfix = touchspin.getAttribute('data-bts-postfix');
      const btsPrefixExtraClass = touchspin.getAttribute('data-bts-prefix-extra-class');
      const btsPostfixExtraClass = touchspin.getAttribute('data-bts-prefix-extra-class');
      const btsBtnDownClass = touchspin.getAttribute('data-bts-button-down-class');
      const btsBtnUpClass = touchspin.getAttribute('data-bts-button-up-class');
      const step = touchspin.getAttribute('data-step')??1;
      const max = touchspin.getAttribute('data-bts-max');
      const decimals = touchspin.getAttribute('data-decimals')??0;
      const longPressInterval = 150;



      const mainContainer = document.createElement('div');
      touchspin.parentNode.appendChild(mainContainer);
      touchspin.classList.add("form-control");



      mainContainer.setAttribute("class","input-group bootstrap-touchspin bootstrap-touchspin-injected");




      const touchDownSpan = document.createElement('span');
      touchDownSpan.setAttribute("class","input-group-btn input-group-prepend");
      const touchDownBtn = document.createElement('button');
      touchDownBtn.setAttribute("class","bootstrap-touchspin-down ".concat(btsBtnDownClass?btsBtnDownClass:"btn btn-primary"));
      touchDownBtn.type = "button";
      touchDownBtn.innerHTML = "-";
      touchDownSpan.appendChild(touchDownBtn);

      let btsPrefixSpan;
      if(btsPrefix){
        btsPrefixSpan = document.createElement('span');
        btsPrefixSpan.setAttribute("class","input-group-addon bootstrap-touchspin-prefix input-group-prepend ".concat(btsPrefixExtraClass?btsPrefixExtraClass:""));
        const btsPrefixInnerText = document.createElement('span');
        btsPrefixInnerText.setAttribute("class","input-group-text");
        btsPrefixInnerText.innerHTML = btsPrefix;
        btsPrefixSpan.appendChild(btsPrefixInnerText);
      }



      let btsPostfixSpan;
      if(btsPostfix){
        btsPostfixSpan = document.createElement('span');
        btsPostfixSpan.setAttribute("class","input-group-addon bootstrap-touchspin-postfix input-group-append ".concat(btsPostfixExtraClass?btsPrefixExtraClass:""));
        const btsPostfixInnerText = document.createElement('span');
        btsPostfixInnerText.setAttribute("class","input-group-text");
        btsPostfixInnerText.innerHTML = btsPostfix;
        btsPostfixSpan.appendChild(btsPostfixInnerText);
      }



      const touchUpSpan = document.createElement('span');
      touchUpSpan.setAttribute("class","input-group-btn input-group-append");
      const touchUpBtn = document.createElement('button');
      touchUpBtn.setAttribute("class","bootstrap-touchspin-up ".concat(btsBtnUpClass?btsBtnUpClass:"btn btn-primary"));
      touchUpBtn.type = "button";
      touchUpBtn.innerHTML = "+";
      touchUpSpan.appendChild(touchUpBtn);



      mainContainer.appendChild(touchDownSpan);
      if(btsPrefixSpan){
        mainContainer.appendChild(btsPrefixSpan);
      }

      mainContainer.appendChild(touchspin);


      if(btsPostfixSpan){
        mainContainer.appendChild(btsPostfixSpan);
      }

      mainContainer.appendChild(touchUpSpan);


      //*-------------------- Click --------------------*//

      var timerDown,timerUp;

      touchDownBtn.addEventListener('click',function (e){
        let value;
        if(isNaN(parseFloat(touchspin.getAttribute('value')))){
          value = 0;
        }else {
          value = parseFloat(touchspin.getAttribute('value'));
        }
        if(value-step>=0) {
          touchspin.setAttribute("value", (value - step).toFixed(decimals));
          touchspin.value = (value - step).toFixed(decimals);
        }else{
          touchspin.setAttribute("value", 0);
          touchspin.value = 0;
        }
      });

      touchDownBtn.addEventListener('mousedown',function (e){


        timerDown = setInterval(function () {
          let value;
          if (isNaN(parseFloat(touchspin.getAttribute('value')))) {
            value = 0;
          } else {
            value = parseFloat(touchspin.getAttribute('value'));
          }
          if (value - step >= 0) {
            touchspin.setAttribute("value", (value - step).toFixed(decimals));
            touchspin.value = (value - step).toFixed(decimals);
          }else{
            touchspin.setAttribute("value", 0);
            touchspin.value = 0;
          }
        }, longPressInterval)


      });
      touchDownBtn.addEventListener('mouseup',function (e){
        clearInterval(timerDown);
      });
      touchDownBtn.addEventListener('mouseleave',function (e){
        clearInterval(timerDown);
      });
      touchDownBtn.addEventListener('mouseout',function (e){
        clearInterval(timerDown);
      });


    touchUpBtn.addEventListener('click',function (e){
        let value;
        if(isNaN(parseFloat(touchspin.getAttribute('value')))){
          value = 0;
        }else {
          value = parseFloat(touchspin.getAttribute('value'));
        }


        if(max==null || (parseFloat(value)+parseFloat(step))<=max) {
          touchspin.setAttribute("value", (parseFloat(value)+parseFloat(step)).toFixed(decimals));

          touchspin.value =  (parseFloat(value)+parseFloat(step)).toFixed(decimals);
        }
      });

      touchUpBtn.addEventListener('mousedown',function (e){

        timerUp=setInterval(function (){
          let value;
          if(isNaN(parseFloat(touchspin.getAttribute('value')))){
            value = 0;
          }else {
            value = parseFloat(touchspin.getAttribute('value'));
          }


          if(max==null || (parseFloat(value)+parseFloat(step))<=max) {
            touchspin.setAttribute("value", (parseFloat(value)+parseFloat(step)).toFixed(decimals));
            touchspin.value =  (parseFloat(value)+parseFloat(step)).toFixed(decimals);
          }
        },longPressInterval)

      });
      touchUpBtn.addEventListener('mouseup',function (e){
        clearInterval(timerUp);
      });
      touchUpBtn.addEventListener('mouseleave',function (e){
        clearInterval(timerUp);
      });
      touchUpBtn.addEventListener('mouseout',function (e){
        clearInterval(timerUp);
      });


      touchspin.addEventListener('input',function (event){
        touchspin.setAttribute('value',touchspin.value);
      });







    });


  }
}

export default Touchspin;
// init the dashboard
//new Touchspin().init();
