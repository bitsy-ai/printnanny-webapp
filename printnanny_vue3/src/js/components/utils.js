/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: CRMDashboard
 */


class Utils {

  static getParents(element,parentClassName){
    var result = [];
    for (var p = element && element.parentElement; p; p = p.parentElement) {
      if(p.classList.contains(parentClassName))
        result.push(p);
    }
    return result;
  }

  static getParentsClosestForLeftbar(element,className,limitClass){
    var result = [];
    for (var p = element && element.parentElement; p; p = p.parentElement) {

      if(limitClass){
        if(p.classList.contains(limitClass)){
          break;
        }
        if( p.children.length>1 &&  p.children[1].classList.contains(className))
          result.push(p.querySelector("."+className));
      }else{
        if( p.children.length>1 && p.children[1].classList.contains(className))
          result.push(p.querySelector("."+className));
      }
    }
    return result;
  }

}

export default Utils;
