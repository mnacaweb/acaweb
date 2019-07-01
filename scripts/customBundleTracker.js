const path = require("path");
const BundleTrackerPlugin = require("webpack-bundle-tracker");
const fs = require('fs');
const mkdirp = require('mkdirp');
const extend = require('deep-extend');
const _ = require('lodash');

BundleTrackerPlugin.prototype.writeOutput = function (compiler, contents) {

	const outputDir = this.options.path || ".";
	const outputFilename = path.join(outputDir, this.options.filename || DEFAULT_OUTPUT_FILENAME);
	const publicPath = this.options.publicPath || compiler.options.output.publicPath;
	if (publicPath) {
		contents.publicPath = publicPath;
	}
	mkdirp.sync(path.dirname(outputFilename));

	this.contents = extend(this.contents, contents);
	_.forEach(this.contents.chunks, function (chunk) {
		_.forEach(chunk, function (microchunk) {
			delete microchunk.path
		});
	});
	fs.writeFileSync(
		outputFilename,
		JSON.stringify(this.contents, null, this.options.indent)
	);
};
module.exports = BundleTrackerPlugin;