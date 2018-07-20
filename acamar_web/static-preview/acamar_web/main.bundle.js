/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/static/acamar_web/";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./scripts/main.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./scripts/main.js":
/*!*************************!*\
  !*** ./scripts/main.js ***!
  \*************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


__webpack_require__(/*! ../styles/main.scss */ "./styles/main.scss");

__webpack_require__(/*! ./vendor */ "./scripts/vendor.js");

__webpack_require__(/*! ./plugins/review_panel */ "./scripts/plugins/review_panel.js");

__webpack_require__(/*! ./plugins/team_grid */ "./scripts/plugins/team_grid.js");

__webpack_require__(/*! ./plugins/map */ "./scripts/plugins/map.js");

__webpack_require__(/*! ./plugins/position_search */ "./scripts/plugins/position_search.js");

$(document).ready(function () {
	$("body").on("click", function () {
		$(".navbar-collapse").removeClass("show");
		$(".site-header").removeClass("open-menu");
		$(".dropdown-menu").removeClass("show");
	});
	$(".site-header").click(function (e) {
		e.stopPropagation();
	});
	$(".navbar-toggler").on("click", function () {
		if ($(".site-header").hasClass("open-menu")) {
			$(".site-header").removeClass("open-menu");
		} else {
			$(".site-header").addClass("open-menu");
		}
		if ($(".navbar-collapse").hasClass("show")) {
			$(".navbar-collapse").removeClass("show");
		} else {
			$(".navbar-collapse").addClass("show");
		}
	});
	$(".dropdown-toggle").on("click", function () {
		if ($(".dropdown-menu").hasClass("show")) {
			$(".dropdown-menu").removeClass("show");
		} else {
			$(".dropdown-menu").addClass("show");
		}
	});
});

/***/ }),

/***/ "./scripts/plugins/map.js":
/*!********************************!*\
  !*** ./scripts/plugins/map.js ***!
  \********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


// let map;
// function initMap() {
// 	let map_container = document.getElementById("map");
// 	if (map_container) {
// 		const myLatLng = function() {
// 			if (screen.width <= 768) {
// 				return { lat: 50.094340, lng: 14.445151 };
// 			} else {
// 				return { lat: 50.093933, lng: 14.442251 };
// 			}
// 		};
//
// 		map = new google.maps.Map(map_container, {
// 			center: myLatLng(),
// 			zoom: 17,
// 			draggable: false
// 		});
//
// 		let marker = new google.maps.Marker({
// 			position: {lat: 50.094120, lng: 14.445091},
// 			map: map,
// 			icon: "static/images/marker.png"
// 		});
//
// 		const content =
// 			"<div class=\"circle-wrapper\">" +
// 			"<div class=\"circle-content\">" +
// 			"<h3 class=\"title-map text-center\">Kanceláře máme<br />v centru Prahy</h3>" +
// 			"<div>" +
// 			"<div class=\"d-flex justify-content-center\">" +
// 			"<div class=\"d-flex align-items-start flex-column pl-2\">" +
// 			"<div class=\"d-flex align-items-center pb-3\">" +
// 			"<div>" +
// 			"<img class=\"pr-2 pr-md-3\" src=\"static/images/small-icons/location2.png\"/>"+
// 			"</div>"+
// 			"<div>" +
// 			"<p class=\"m-0 text-map\"><strong>Karolínská 654/2<br />186 00 Praha</strong></p>"+
// 			"</div>"+
// 			"</div>"+
// 			"<div class=\"d-flex align-items-center pb-3\">" +
// 			"<img class=\"pr-2 pr-md-3\" src=\"static/images/small-icons/write.png\"/>"+
// 			"<div>" +
// 			"<p class=\"m-0 text-map\">IČ: 777 777 777</p>"+
// 			"<p class=\"m-0 text-map\">DIČ: 777 777 777</p>"+
// 			"</div>"+
// 			"</div>"+
// 			"<div class=\"d-flex align-items-center pb-3\">" +
// 			"<div>" +
// 			"<img class=\"pr-2 pr-md-3\" src=\"static/images/small-icons/message.png\"/>"+
// 			"</div>"+
// 			"<div>" +
// 			"<p class=\"m-0 text-map\">Telefon: 731 544 584</p>"+
// 			"<p class=\"m-0 text-map\">E-mail: info@acamar.cz</p>"+
// 			"</div>"+
// 			"</div>"+
// 			"</div>"+
// 			"</div>"+
// 			"</div>"+
// 			"</div>"+
// 			"</div>";
//
// 		let infowindow = new google.maps.InfoWindow({
// 			content: content,
// 			maxWidth: "auto",
// 			pixelOffset: {
// 				width: 200,
// 				height: 200
// 			}
//
// 		});
// 		infowindow.open(map, marker);
// 	}
// }

function myLatLng() {
	if (screen.width <= 768) {
		return { lat: 50.094340, lng: 14.445151 };
	} else {
		return { lat: 50.093933, lng: 14.442251 };
	}
}

function initMap() {
	$(function () {
		$(".map").each(function () {
			var $this = $(this);
			var content = $this.next().html();
			// const lat = $this.data("lat");
			// const lon = $this.data("lon");
			var icon = $this.data("icon");
			var map = new google.maps.Map(this, {
				center: myLatLng(),
				zoom: 17,
				draggable: false,
				disableDefaultUI: true

			});

			var marker = new google.maps.Marker({
				position: { lat: 50.094120, lng: 14.445091 },
				map: map,
				icon: icon
			});

			var infowindow = new google.maps.InfoWindow({
				content: content,
				maxWidth: "auto",
				pixelOffset: {
					width: 200,
					height: 200
				}
			});
			infowindow.open(map, marker);
		});
	});
}
window.initMap = initMap;

/***/ }),

/***/ "./scripts/plugins/position_search.js":
/*!********************************************!*\
  !*** ./scripts/plugins/position_search.js ***!
  \********************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


$(function () {
	$(".position-search").each(function () {
		var $this = $(this);
		var form = $this.find("form");
		var url = form.attr("action");
		var method = form.attr("method");
		var queryInput = form.find("#queryInput");
		var autocompleteUrl = queryInput.data("url");
		var resultContainer = $this.find(".position-search-results");
		var limit = resultContainer.data("limit");
		var autocompleteContainer = form.find(".position-search-autocomplete");
		var categories = form.find(".category");
		var pacts = $this.find(".pacts .tab");

		function updateCategoryCount(positions) {
			var category_count = positions.map(function () {
				return this.dataset.category;
			}).get().reduce(function (agg, val) {
				agg[val] ? agg[val] += 1 : agg[val] = 1;
				return agg;
			}, {});
			categories.each(function () {
				var $this = $(this);
				$this.find(".count").text(category_count[$this.data("id")] | 0);
			});
		}

		function applyCategoryFilter(positions) {
			var filter = categories.filter(".active-count").map(function () {
				return $(this).data("id");
			}).get();
			if (filter.length) {
				positions.each(function () {
					$this = $(this);
					if (filter.indexOf($this.data("category")) !== -1) $this.removeClass("cfilter");else $this.addClass("cfilter");
				});
			} else {
				positions.removeClass("cfilter");
			}
		}

		function applyPactFilter(positions) {
			var pact_id = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : pacts.filter("active").data("id");

			if (pact_id) {
				positions.each(function () {
					var $this = $(this);
					var position_pacts = $this.data("pact");
					if (position_pacts.indexOf(pact_id) !== -1) $this.removeClass("pfilter");else $this.addClass("pfilter");
				});
			} else {
				positions.removeClass("pfilter");
			}
		}

		function updateMore() {
			var positions = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : resultContainer.find(".position");

			if (limit) {
				var more_button = resultContainer.find(".button-more");
				var dataset = positions.filter(":not(.pfilter,.cfilter)");
				dataset.slice(0, limit).removeClass("more");
				dataset.slice(limit).addClass("more");
				more_button.click(function () {
					dataset.removeClass("more");
					more_button.hide();
				});
			}
		}

		form.submit(function (event) {
			event.preventDefault();
			$.ajax({
				url: url,
				method: method,
				data: form.serialize(),
				success: function success(response) {
					var html = $(response).hide();
					html.ready(function () {
						resultContainer.children().fadeOut("slow", function () {
							var positions = html.find(".position");
							updateCategoryCount(positions);
							applyCategoryFilter(positions);
							applyPactFilter(positions);
							updateMore(positions);
							$(this).replaceWith(html);
							html.fadeIn("slow");
						});
					});
				}
			});
		});

		queryInput.on("keyup", function () {
			var query = queryInput.val();
			if (query.length < 3) {
				return false;
			}

			$.ajax({
				url: autocompleteUrl,
				method: "GET",
				data: form.serialize(),
				success: function success(response) {
					autocompleteContainer.html(response);
				}
			});
		});
		queryInput.on("focusin", function () {
			autocompleteContainer.show();
		});
		queryInput.on("focusout", function () {
			autocompleteContainer.hide();
		});

		categories.each(function () {
			var $this = $(this);
			$this.click(function () {
				$this.toggleClass("active-count");
				var positions = resultContainer.find(".position");
				applyCategoryFilter(positions);
				updateMore(positions);
			});
		});

		pacts.each(function () {
			var $this = $(this);
			$this.click(function () {
				pacts.parent().removeClass("border-active");
				pacts.removeClass("active");
				$this.parent().addClass("border-active");
				$this.addClass("active");
				var positions = resultContainer.find(".position");
				applyPactFilter(positions, $this.data("id"));
				updateMore(positions);
			});
		});

		updateMore();
	});
});

/***/ }),

/***/ "./scripts/plugins/review_panel.js":
/*!*****************************************!*\
  !*** ./scripts/plugins/review_panel.js ***!
  \*****************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var review_refresh_rate = 20000;

$(document).ready(function () {
	$.fn.initReviewCycle = function () {
		var $this = $(this);
		var review_container = $this.find(".review-person");
		var url = $this.data("url");
		var reviews = $this.data("reviews");

		function getNextReview() {
			if ($this.length && Array.isArray(reviews)) {
				var current_id = review_container.children().first().data("id");
				var current_index = reviews.indexOf(current_id);
				if (current_index !== -1) {
					var next_index = reviews.length === current_index + 1 ? 0 : current_index + 1;
					$.ajax({
						url: "" + url + reviews[next_index] + "/",
						method: "GET",
						success: function success(response) {
							var html = $(response).hide();
							html.ready(function () {
								review_container.children().fadeOut("slow", function () {
									$(this).replaceWith(html);
									html.fadeIn("slow");
									setTimeout(getNextReview, review_refresh_rate);
								});
							});
						}
					});
				}
			}
		}

		setTimeout(getNextReview, review_refresh_rate);
		return this;
	};

	var reviews_section = $(".reviews-section");
	if (reviews_section.length) {
		reviews_section.initReviewCycle();
	}
});

/***/ }),

/***/ "./scripts/plugins/team_grid.js":
/*!**************************************!*\
  !*** ./scripts/plugins/team_grid.js ***!
  \**************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


$(function () {
	$(".team-grid-button").each(function () {
		var $this = $(this);
		var container = $this.parent().parent().children(".team-grid");
		var url = $this.data("href");
		$this.click(function (event) {
			event.stopPropagation();
			$.ajax({
				url: url,
				method: "GET",
				success: function success(response) {
					var html = $(response);
					html.hide();
					html.ready(function () {
						container.append(html);
						html.slideDown("slow");
						$this.remove();
					});
				}
			});
		});
	});
});

/***/ }),

/***/ "./scripts/vendor.js":
/*!***************************!*\
  !*** ./scripts/vendor.js ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/* eslint-disable */
/**
 * jQuery.browser.mobile (http://detectmobilebrowser.com/)
 *
 * jQuery.browser.mobile will be true if the browser is a mobile device
 *
 **/
(function (a) {
  (jQuery.browser = jQuery.browser || {}).mobile = /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0, 4));
})(navigator.userAgent || navigator.vendor || window.opera);

/***/ }),

/***/ "./styles/main.scss":
/*!**************************!*\
  !*** ./styles/main.scss ***!
  \**************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ })

/******/ });
//# sourceMappingURL=main.bundle.js.map