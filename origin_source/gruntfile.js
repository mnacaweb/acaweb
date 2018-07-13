module.exports = function (grunt) {

    var static_root = {
        'source':  'static-source',
        'master':  'dist/static'
    };

    var copySources = [
        'fonts/*',
        'images/*',
        'images/**/*',
        'videos/*',
        'videos/**/*'
    ];

    var concatSources = [
        "<%= dirs.static.source %>/scripts/bower.js",
        "<%= dirs.static.source %>/scripts/libs/*",
        "<%= dirs.static.source %>/scripts/*"
    ];

    function updateIncludeHtml(content, path) {
        var crypto = require('crypto');

        var jsSrc = path + '/scripts/desktop.js';
        var jsContent = grunt.file.read(jsSrc);
        var jsHash = crypto.createHash('md5').update(jsContent).digest('hex');

        var cssSrc = path + '/styles/desktop.css';
        var cssContent = grunt.file.read(cssSrc);
        var cssHash = crypto.createHash('md5').update(cssContent).digest('hex');

        content = content.split('[jsHash]').join(jsHash);
        content = content.split('[cssHash]').join(cssHash);

        return content;
    }

    grunt.initConfig({
        dirs: {
            static: static_root
        },

        clean: {
            master: ['<%= dirs.static.master %>'],
            html:   ['<%= dirs.static.master %>/html'],
            map:   ['<%= dirs.static.master %>/styles/desktop.css.map']
        },

        copy: {
            master: {
                files: [
                    {
                        expand: true,
                        cwd: '<%= dirs.static.source %>/',
                        src: copySources,
                        dest: '<%= dirs.static.master %>/'
                    }
                ]
            },
            master_html: {
                src: '<%= dirs.static.source %>/html/includes.html',
                dest: '<%= dirs.static.master %>/html/includes.html',
                options: {
                    process: function(content, srcpath) {
                        return updateIncludeHtml(content,static_root.master);
                    }
                }
            }
        },

        bower_concat: {
            common: {
                mainFiles: {},
                exclude: [],
                dependencies: {},
                dest: static_root.source + '/scripts/bower.js'
            }
        },

        concat: {
            master: {
                src: concatSources,
                dest: '<%= dirs.static.master %>/scripts/desktop.js',
                sourceMap: true,
                nonull: true
            }
        },

        sass: {
            master: {
                options: {
                    compress: false,
                    sourceMap: true
                },
                files: {
                    '<%= dirs.static.master %>/styles/desktop.css': '<%= dirs.static.source %>/styles/desktop.scss'
                }
            }
        },

        uglify: {
            master: {
                compress: {
                    drop_console: true
                },
                files: {
                    '<%= dirs.static.master %>/scripts/desktop.js': ['<%= dirs.static.master %>/scripts/desktop.js']
                }
            }
        },

        postcss: {
            options: {
                map: false, // inline sourcemaps

                processors: [
                    require('autoprefixer')({browsers: 'last 2 versions'}), // add vendor prefixes
                ]
            },
            dist: {
                src:  '<%= dirs.static.master %>/styles/desktop.css',
                dest: '<%= dirs.static.master %>/styles/desktop.css',
            }
        },

        cssmin: {
            master: {
                src:  '<%= dirs.static.master %>/styles/desktop.css',
                dest: '<%= dirs.static.master %>/styles/desktop.css',
                options: {
                    rebase: false
                }
            }
        },

        jinja: {
            options: {
                templateDirs: [
                    process.cwd() + '/templates',
                    '<%= dirs.static.master %>/html'
                ]
            },
            master: {
                files: [{
                    expand: true,
                    dest: 'dist/',
                    cwd: 'templates/',
                    src: ['**/!(_)*.html']
                }]
            }
        },

        browserSync: {
            bsFiles: {
                src : 'dist/static/styles/**/*.css',
                src : 'dist/static/scripts/**/*.js',
                src : 'dist/**/*.html'
            },
            options: {
                watchTask: true,
                server: {
                    baseDir: "./dist"
                }
            }
        },

        watch: {
            sass: {
                files: '<%= dirs.static.source %>/styles/**/*.scss',
                tasks: ['copy:master','sass:master','copy:master_html'],
                options: {
                    interval: 2000,
                    spawn: false
                }
            },
            js: {
                files: '<%= dirs.static.source %>/scripts/**/*.js',
                tasks: ['concat:master','copy:master_html']
            },
            html: {
                files: 'templates/**/*.html',
                tasks: ['jinja:master']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-bower-concat');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks("grunt-css-url-rewrite");
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-spritesmith');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-jinja');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-postcss');

    grunt.registerTask('default', ['browserSync', 'watch']);

    grunt.registerTask('preview', [
        'clean:master','copy:master','sass:master','bower_concat',
        'concat:master',/*'uglify:master','cssmin:master',*/'copy:master_html','jinja:master'
    ]);

    grunt.registerTask('master', [
        'clean:master','copy:master','sass:master','bower_concat',
        'concat:master','uglify:master','postcss','cssmin:master','copy:master_html','jinja:master',
        'clean:html','clean:map'
    ]);
};