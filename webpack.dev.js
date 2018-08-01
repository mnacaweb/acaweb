const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const CleanWebpackPlugin = require("clean-webpack-plugin");
const BundleTracker = require("./customBundleTracker");
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const webpack = require("webpack");
const path = require("path");
const project_name = "acamar_web";

module.exports = merge(common, {
	mode: "development",
	devtool: "source-map",
	output: {
		filename: "[name].bundle.js",
		chunkFilename: "[name].bundle.js",
		path: path.resolve(__dirname, project_name, "static-preview", project_name),
		publicPath: "/static/acamar_web/"
	},
	plugins: [
		new CleanWebpackPlugin([project_name+"/static-preview"], {watch: false}),
		new BundleTracker({filename: "./webpack-stats-preview.json", indent: 4}),
		new MiniCssExtractPlugin({
			filename: "[name].css",
			chunkFilename: "[id].css"
		}),
		new BrowserSyncPlugin({
			host: 'localhost',
			port: 3000,
			proxy: 'http://127.0.0.1:8000/',
			files: ["app/*/templates/**/*.html", project_name+"/templates/**/*.html"],
			open: false
		})
	]
});