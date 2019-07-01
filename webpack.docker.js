const merge = require("webpack-merge");
const dev = require("./webpack.dev.js");
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const project_name = "acamar_web";
const _ = require('lodash');

module.exports = merge({
    customizeArray: (a, b, key) => {
        if (key === 'plugins') {
            // replace last
            return [...a.slice(0,a.length-1), ...b]
        }
    },
})(dev, {
    plugins: [
        new BrowserSyncPlugin({
            host: 'localhost',
            port: 3000,
            proxy: 'http://web:8000/',
            files: ["app/*/templates/**/*.html", project_name+"/templates/**/*.html"],
            open: false
        })
    ]
});
