"use strict";

var gulp = require("gulp"),
    pjson = require("./package.json"),
    browsersync = require("browser-sync"),
    uglify = require("gulp-uglify"),
    sourcemaps = require("gulp-sourcemaps"),
    concat = require("gulp-concat"),
    rename = require("gulp-rename"),
    imagemin = require('gulp-imagemin'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cleanCSS = require('gulp-clean-css'),
    spawn = require('child_process').spawn;


// Relative paths function
var pathsConfig = function (appName) {
    var vendorsRoot = './node_modules/';

    var app = "./" + (appName || pjson.name);

    return {
        bootstrapSass: vendorsRoot + '/bootstrap/scss',
        vendorsJs: [
            vendorsRoot + "jquery/dist/jquery.js",
            vendorsRoot + "bootstrap/dist/js/bootstrap.bundle.js",
            vendorsRoot + "moment/moment.js",
            vendorsRoot + "metismenu/dist/metisMenu.js",
            vendorsRoot + "simplebar/dist/simplebar.min.js",
            vendorsRoot + "daterangepicker/daterangepicker.js",
            vendorsRoot + "jquery-toast-plugin/dist/jquery.toast.min.js",
            vendorsRoot + "select2/dist/js/select2.min.js",
            vendorsRoot + "jquery-mask-plugin/dist/jquery.mask.min.js",
            vendorsRoot + "twitter-bootstrap-wizard/jquery.bootstrap.wizard.min.js",
            vendorsRoot + "bootstrap-timepicker/js/bootstrap-timepicker.min.js",
            vendorsRoot + "bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.js",
            vendorsRoot + "bootstrap-maxlength/dist/bootstrap-maxlength.min.js",
            vendorsRoot + "bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js",
            vendorsRoot + "highlightjs/highlight.pack.min.js",

        ],
        vendorCss: [
            vendorsRoot + "daterangepicker/daterangepicker.css",
            vendorsRoot + "jquery-toast-plugin/dist/jquery.toast.min.css",
            vendorsRoot + "select2/dist/css/select2.min.css",
            vendorsRoot + "bootstrap-timepicker/css/bootstrap-timepicker.min.css",
            vendorsRoot + "bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.css",
            vendorsRoot + "bootstrap-datepicker/dist/css/bootstrap-datepicker.min.css"
        ],

        vendorOptionalCss: [
            vendorsRoot + "admin-resources/jquery.vectormap/jquery-jvectormap-1.2.2.css",
            vendorsRoot + "britecharts/dist/css/britecharts.min.css",
            vendorsRoot + "datatables.net-bs4/css/dataTables.bootstrap4.css",
            vendorsRoot + "datatables.net-responsive-bs4/css/responsive.bootstrap4.css",
            vendorsRoot + "datatables.net-buttons-bs4/css/buttons.bootstrap4.css",
            vendorsRoot + "datatables.net-select-bs4/css/select.bootstrap4.css",
            vendorsRoot + "fullcalendar/dist/fullcalendar.min.css",
            vendorsRoot + "summernote/dist/summernote-bs4.css",
            vendorsRoot + "simplemde/dist/simplemde.min.css",
            vendorsRoot + "frappe-gantt/dist/frappe-gantt.css",
        ],

        vendorOptionalJs: [
            vendorsRoot + "chart.js/dist/Chart.bundle.min.js",
            vendorsRoot + "d3/dist/d3.min.js",
            vendorsRoot + "britecharts/dist/bundled/britecharts.min.js",
            vendorsRoot + "datatables.net/js/jquery.dataTables.js",
            vendorsRoot + "datatables.net-bs4/js/dataTables.bootstrap4.js",
            vendorsRoot + "datatables.net-responsive/js/dataTables.responsive.min.js",
            vendorsRoot + "datatables.net-responsive-bs4/js/responsive.bootstrap4.min.js",
            vendorsRoot + "datatables.net-buttons/js/dataTables.buttons.min.js",
            vendorsRoot + "datatables.net-buttons-bs4/js/buttons.bootstrap4.min.js",
            vendorsRoot + "datatables.net-buttons/js/buttons.html5.min.js",
            vendorsRoot + "datatables.net-buttons/js/buttons.flash.min.js",
            vendorsRoot + "datatables.net-buttons/js/buttons.print.min.js",
            vendorsRoot + "datatables.net-keytable/js/dataTables.keyTable.min.js",
            vendorsRoot + "datatables.net-select/js/dataTables.select.min.js",
            vendorsRoot + "jquery-datatables-checkboxes/js/dataTables.checkboxes.min.js",
            vendorsRoot + "jquery-ui/jquery-ui.min.js",
            vendorsRoot + "fullcalendar/dist/fullcalendar.min.js",
            vendorsRoot + "gmaps/gmaps.min.js",
            vendorsRoot + "admin-resources/jquery.vectormap/jquery-jvectormap-1.2.2.min.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-world-mill-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-us-merc-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-au-mill-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-us-il-chicago-mill-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-in-mill-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-uk-mill-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-ca-lcc-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-europe-mill-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-fr-merc-en.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-es-merc.js",
            vendorsRoot + "admin-resources/jquery.vectormap/maps/jquery-jvectormap-es-mill.js",
            vendorsRoot + "dragula/dist/dragula.min.js",
            vendorsRoot + "dropzone/dist/min/dropzone.min.js",
            vendorsRoot + "apexcharts/dist/apexcharts.min.js",
            vendorsRoot + "summernote/dist/summernote-bs4.min.js",
            vendorsRoot + "simplemde/dist/simplemde.min.js",
            vendorsRoot + "typeahead.js/dist/typeahead.bundle.min.js",
            vendorsRoot + "handlebars/dist/handlebars.min.js",
            vendorsRoot + "jquery-sparkline/jquery.sparkline.min.js",
            vendorsRoot + "ion-rangeslider/js/ion.rangeSlider.min.js",
            vendorsRoot + "frappe-gantt/dist/frappe-gantt.min.js",
            vendorsRoot + "jquery.rateit/scripts/jquery.rateit.min.js"
        ],

        app: app,
        templates: app + '/templates',
        css: app + '/static/css',
        sass: app + '/static/scss',
        fonts: app + '/static/fonts',
        images: app + '/static/images',
        js: app + '/static/js',
        srcJs: app + '/static/js'
    }
};

var paths = pathsConfig();


////////////////////////////////
//Tasks//
////////////////////////////////

// Vendor styles
function copyVendorStyles(done) {
    //copying required assets
    gulp.src(paths.vendorCss)
        .pipe(
            rename({
                // rename aaa.css to _aaa.scss
                prefix: "_",
                extname: ".scss"
            })
        )
        .pipe(gulp.dest(paths.sass + "/vendor"));


    //copying third party assets
    gulp.src(paths.vendorOptionalCss).pipe(gulp.dest(paths.css + "/vendor"));
    done();
}

// Styles autoprefixing and minification
function styles() {
    return gulp
        .src([paths.sass + "/*.scss"])
        .pipe(sourcemaps.init())
        .pipe(sass()) // scss to css
        .pipe(
            autoprefixer({
                overrideBrowserslist: ["last 2 versions"]
            })
        )
        .pipe(gulp.dest(paths.css))
        .pipe(cleanCSS())
        .pipe(
            rename({
                // rename app.css to app.min.css
                suffix: ".min"
            })
        )
        .pipe(sourcemaps.write("./")) // source maps
        .pipe(gulp.dest(paths.css));
}


// Vendor script
function copyVendorScripts(done) {
    //copying third party assets
    gulp.src(paths.vendorOptionalJs).pipe(gulp.dest(paths.js + "/vendor"));
    done();
}

// Javascript minification
function scripts() {
    gulp.src(paths.vendorsJs)
        .pipe(sourcemaps.init())
        .pipe(concat("vendor.js"))
        .pipe(gulp.dest(paths.js))
        .pipe(
            rename({
                // rename app.js to app.min.js
                suffix: ".min"
            })
        )
        .pipe(uglify())
        .on("error", function (err) {
            console.log(err.toString());
        })
        .pipe(sourcemaps.write("./"))
        .pipe(gulp.dest(paths.js));

    return gulp.src([paths.srcJs + "/layout.js", paths.srcJs + "/hyper.js"])
        .pipe(sourcemaps.init())
        .pipe(concat("app.js"))
        .pipe(gulp.dest(paths.js))
        .pipe(
            rename({
                // rename app.js to app.min.js
                suffix: ".min"
            })
        )
        .pipe(uglify())
        .on("error", function (err) {
            console.log(err.toString());
        })
        .pipe(sourcemaps.write("./"))
        .pipe(gulp.dest(paths.js));

}

// Image compression
function imgCompression() {
    return gulp.src(paths.images + '/*')
        .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
        .pipe(gulp.dest(paths.images))
}



// Run django server
// function runServer(cb) {
//     var cmd = spawn('python', ['manage.py', 'runserver'], { stdio: 'inherit' });
//     cmd.on('close', function (code) {
//         console.log('runServer exited with code ' + code);
//         cb(code);
//     });
// }

// live browser loading
function initBrowserSync(done) {
    browsersync.init({
        proxy: "localhost:8000",
        notify: false
    });
    done();
}

function reloadBrowserSync(done) {
    browsersync.reload();
    browsersync.stream({once: true})
    done();
}

function watchFiles() {
    // gulp.watch(paths.app + '/**/*.py', gulp.series(reloadBrowserSync));
    //gulp.watch(paths.templates + '/**/*', gulp.series(reloadBrowserSync));
    gulp.watch(paths.sass + '/**/*.scss', gulp.series(styles));
    gulp.watch(paths.js + '/src/**/*.js', gulp.series(scripts));
    //gulp.watch(paths.images + '/**/*', gulp.series(imgCompression, reloadBrowserSync));
}


// tasks
gulp.task("dev", gulp.parallel(initBrowserSync, watchFiles));

// default
gulp.task('default', gulp.series(gulp.parallel(
    gulp.series(copyVendorStyles, styles),
    gulp.series(copyVendorScripts, scripts),
    imgCompression
), "dev"), function (done) { done(); });


// build
gulp.task("build", gulp.parallel(
    gulp.series(copyVendorStyles, styles),
    gulp.series(copyVendorScripts, scripts),
    imgCompression
));