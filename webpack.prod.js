const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const CleanWebpackPlugin = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const BundleTracker = require("./customBundleTracker");
const webpack = require("webpack");
const path = require("path");
const project_name = "acamar_web";

module.exports = merge(common, {
	devtool: "none",
	mode: "production",
	output: {
		filename: "[name]-[hash].bundle.js",
		chunkFilename: "[name]-[hash].bundle.js",
		path: path.resolve(__dirname, project_name, "static-master", project_name),
		publicPath: "/static/acamar_web/"
	},
	plugins: [
		new CleanWebpackPlugin([project_name+"/static-master"]),
		new webpack.DefinePlugin({
			"process.env": {
				"NODE_ENV": JSON.stringify("production")
			}
		}),
		new MiniCssExtractPlugin({
			filename: "[name]-[hash].css",
			chunkFilename: "[id]-[hash].css"
		}),
		new BundleTracker({filename: "./webpack-stats-master.json", indent: 4}),
	]
});
