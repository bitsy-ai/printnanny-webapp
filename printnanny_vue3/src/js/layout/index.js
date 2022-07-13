
import LeftSidebar from './left-sidebar';
import RightSidebar from './right-sidebar';
import Topbar from './topbar';
import ThemeCustomizer from './theme-customizer';

class LayoutThemeApp {

    constructor() {

    }

    /**
     *
     */
    init = () => {

        // topbar
        this.topBar = new Topbar();
        this.topBar.init();
        this.rightBar = new RightSidebar();
        this.rightBar.init();
        this.leftSidebar = new LeftSidebar();
        this.leftSidebar.init();
        this.themeCustomizer = new ThemeCustomizer();
        this.themeCustomizer.init();
    }
}

export default LayoutThemeApp;
