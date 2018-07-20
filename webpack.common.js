const path = require("path");
const webpack = require("webpack");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const SpritesmithPlugin = require("webpack-spritesmith");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const UglifyJSPlugin = require("uglifyjs-webpack-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const project_name = "acamar_web";

module.exports = {
	context: path.resolve(__dirname, project_name, "static-source", project_name),
	entry: {
		main: "./scripts/main.js",
	},
	externals: {
		jquery: "jQuery",
		google: "google"
	},
	optimization: {
		minimizer: [
			new UglifyJSPlugin({
				cache: true,
				parallel: true,
			}),
			new OptimizeCSSAssetsPlugin({})
		]
	},
	plugins: [
		new MiniCssExtractPlugin({
			// Options similar to the same options in webpackOptions.output
			// both options are optional
			filename: "[name].css",
			chunkFilename: "[id].css"
		}),
		new CopyWebpackPlugin([{
			from: "./images",
			to: "./images"
		}]),
		// new webpack.ProvidePlugin({
		// 	"window.$": "jquery",
		// 	$: "jquery",
		// 	jQuery: "jquery",
		// 	"window.jQuery": "jquery",
		// 	_: "lodash"
		// }),
		new SpritesmithPlugin({
			src: {
				cwd: path.resolve(__dirname, project_name, "static-source", project_name, "sprites"),
				glob: "*.png"
			},
			target: {
				image: path.resolve(__dirname, project_name, "static-source", project_name, "styles", "spritesmith/sprite.png"),
				css: path.resolve(__dirname, project_name, "static-source", project_name, "styles", "spritesmith/_sprite.scss")
			},
			apiOptions: {
				cssImageRef: "./styles/spritesmith/sprite.png"
			}
		})
	],
	stats: {
		colors: true
	},
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /(node_modules|bower_components)/,
				use: [{
					loader: "babel-loader",
					options: {
						presets: ["env"]
					}
				}, {
					loader: "eslint-loader"
				}]

			},
			{
				test: /\.(png|svg|jpg|gif)$/,
				use: [{
					loader: "url-loader",
					options: {
						limit: 8192,
						name: "[path][name].[ext]",
						publicPath: "/static/acamar_web/"
					}
				}]
			},
			{
				test: /\.(woff|woff2|eot|ttf|otf)$/,
				use: [{
					loader: "url-loader",
					options: {
						limit: 50000,
						name: "fonts/[name].[ext]",
					}
				}]
			},
			{
				test: /\.(sa|sc|c)ss$/,
				use: [
					{
						loader: MiniCssExtractPlugin.loader,
						options: {
							sourceMap: true
						}
					},
					{
						loader: "css-loader", options: {
							sourceMap: true
						}
					},
					{
						loader: "postcss-loader",
						options: {
							plugins() {
								return [
									require("precss"),
									require("autoprefixer")
								];
							},
							sourceMap: true
						}
					},
					{
						loader: "resolve-url-loader", options: {
							sourceMap: true
						}
					},
					{
						loader: "sass-loader",
						options: {
							sourceMap: true
						}
					}
				],
			}
		]
	}
};
