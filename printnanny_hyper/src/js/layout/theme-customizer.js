class ThemeCustomizer {


    constructor() {
        this.body = document.body;
        this.defaultConfig =
        {
            leftbar: {
                theme: 'light', mode: 'fixed',
            }, layout: {
                color: 'light', mode: 'fluid',
            },
        }

    }

    initConfig() {
        let config = JSON.parse(JSON.stringify(this.defaultConfig));
        config['leftbar']['theme'] = this.body.getAttribute('data-leftbar-theme') ?? this.defaultConfig.leftbar.theme;
        config['leftbar']['mode'] = this.body.getAttribute('data-leftbar-compact-mode') ?? this.defaultConfig.leftbar.mode;
        config['layout']['color'] = this.body.getAttribute('data-layout-color') ?? this.defaultConfig.layout.color;
        config['layout']['mode'] = this.body.getAttribute('data-layout-mode') ?? this.defaultConfig.layout.mode;
        this.defaultConfig = JSON.parse(JSON.stringify(config));
        this.config = config;
        this.setSwitchFromConfig();
    }

    changeLeftbarTheme(theme) {
        this.config.leftbar.theme = theme;
        this.body.setAttribute('data-leftbar-theme', theme);
        this.setSwitchFromConfig();
    }

    changeLeftbarMode(mode) {
        if (this.config.layout.mode != 'fixed') {
            this.config.leftbar.mode = mode;
            this.body.setAttribute('data-leftbar-compact-mode', mode);
            this.setSwitchFromConfig();
        }
    }

    changeLayoutColor(color) {
        this.config.layout.color = color;
        this.body.setAttribute('data-layout-color', color);
        this.setSwitchFromConfig();
    }

    changeLayoutMode(mode) {
        this.config.layout.mode = mode;
        this.body.setAttribute('data-layout-mode', mode);
        if (mode === 'boxed') {
            this.changeLeftbarMode('condensed');
        }
        else {
            this.changeLeftbarMode('fixed');
        }
        this.setSwitchFromConfig();
    }

    resetTheme() {
        this.config = JSON.parse(JSON.stringify(this.defaultConfig));
        this.changeLeftbarTheme(this.config.leftbar.theme);
        this.changeLeftbarMode(this.config.leftbar.mode);
        this.changeLayoutColor(this.config.layout.color);
        this.changeLayoutMode(this.config.layout.mode);
    }

    initSwitchListener() {
        const self = this;
        document.querySelectorAll('input[type=checkbox][name=theme]').forEach(function (element) {
            element.addEventListener('change', function (e) {
                self.changeLeftbarTheme(element.value);
            })
        });
        document.querySelectorAll('input[type=checkbox][name=compact]').forEach(function (element) {
            element.addEventListener('change', function (e) {
                self.changeLeftbarMode(element.value);
            })
        });
        document.querySelectorAll('input[type=checkbox][name=color-scheme-mode]').forEach(function (element) {
            element.addEventListener('change', function (e) {
                self.changeLayoutColor(element.value);
            })
        });

        document.querySelectorAll('input[type=checkbox][name=width]').forEach(function (element) {
            element.addEventListener('change', function (e) {
                self.changeLayoutMode(element.value);
            })
        });
        document.querySelector('#resetBtn')?.addEventListener('click', function (e) {
            self.resetTheme();
        });

        // topbar
        document.querySelector('.button-menu-mobile')?.addEventListener('click', function () {
            if (self.body.getAttribute('data-layout') !== 'full') {
                if (window.innerWidth >= 768 && self.config.leftbar.mode === 'fixed') {
                    self.changeLeftbarMode('condensed');
                } else {
                    self.changeLeftbarMode('fixed');
                }
            }
        });
    }

    initWindowSize() {
        let self = this;
        window.addEventListener('resize', function (e) {
            if (window.innerWidth >= 768 && window.innerWidth <= 1024) {
                self.changeLeftbarMode('condensed');
            } else {
                self.changeLeftbarMode('fixed');

            }
        })
    }

    setSwitchFromConfig() {
        document.querySelectorAll('.end-bar input[type=checkbox]').forEach(function (checkbox) {
            checkbox.checked = false;
        })
        let config = this.config;
        if (config) {
            let leftbarColorSwitch = document.querySelector('input[type=checkbox][name=theme][value=' + config.leftbar.theme + ']');
            let leftbarModeSwitch = document.querySelector('input[type=checkbox][name=compact][value=' + config.leftbar.mode + ']');

            let layoutColorSwitch = document.querySelector('input[type=checkbox][name=color-scheme-mode][value=' + config.layout.color + ']');
            let layoutModeSwitch = document.querySelector('input[type=checkbox][name=width][value=' + config.layout.mode + ']');

            if (leftbarColorSwitch) leftbarColorSwitch.checked = true;
            if (leftbarModeSwitch) leftbarModeSwitch.checked = true;

            if (layoutColorSwitch) layoutColorSwitch.checked = true;
            if (layoutModeSwitch) layoutModeSwitch.checked = true;
        }
    }

    init() {
        this.initConfig();
        this.initSwitchListener();
        this.initWindowSize();
        this.setSwitchFromConfig();
    }
}

export default ThemeCustomizer;