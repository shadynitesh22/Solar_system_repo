module.exports = function(grunt) {
    grunt.initConfig({
        uncss: {
            dist: {
                files: [{
                    nonull: true,
                    src: ['http://localhost:8000/'],
                    dest: '/static/new/css/bootstrap.min.css'
                }]
            },
            options: {
                ignoreSheets : [/fonts.googleapis/, /cdn.jsdelivr.net/],
                stylesheets: ['/static/new/css/styles.css'],
            }
        }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-uncss');

    // Default tasks.
    grunt.registerTask('default', ['uncss']);

};