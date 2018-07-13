import "../styles/main.scss";

import "./vendor";

import "./plugins/review_panel";

$(document).ready(function() {
	$("body").on("click", function() {
		$(".navbar-collapse").removeClass("show");
		$(".site-header").removeClass("open-menu");
		$(".dropdown-menu").removeClass("show");
	});
	$(".site-header").click(function(e) {
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

let map;
function initMap() {
	let map_container = document.getElementById("map");
	if (map_container) {
		const myLatLng = function() {
			if (screen.width <= 768) {
				return { lat: 50.094340, lng: 14.445151 };
			} else {
				return { lat: 50.093933, lng: 14.442251 };
			}
		};

		map = new google.maps.Map(map_container, {
			center: myLatLng(),
			zoom: 17,
			draggable: false
		});

		let marker = new google.maps.Marker({
			position: {lat: 50.094120, lng: 14.445091},
			map: map,
			icon: "static/images/marker.png"
		});

		const content =
			"<div class=\"circle-wrapper\">" +
			"<div class=\"circle-content\">" +
			"<h3 class=\"title-map text-center\">Kanceláře máme<br />v centru Prahy</h3>" +
			"<div>" +
			"<div class=\"d-flex justify-content-center\">" +
			"<div class=\"d-flex align-items-start flex-column pl-2\">" +
			"<div class=\"d-flex align-items-center pb-3\">" +
			"<div>" +
			"<img class=\"pr-2 pr-md-3\" src=\"static/images/small-icons/location2.png\"/>"+
			"</div>"+
			"<div>" +
			"<p class=\"m-0 text-map\"><strong>Karolínská 654/2<br />186 00 Praha</strong></p>"+
			"</div>"+
			"</div>"+
			"<div class=\"d-flex align-items-center pb-3\">" +
			"<img class=\"pr-2 pr-md-3\" src=\"static/images/small-icons/write.png\"/>"+
			"<div>" +
			"<p class=\"m-0 text-map\">IČ: 777 777 777</p>"+
			"<p class=\"m-0 text-map\">DIČ: 777 777 777</p>"+
			"</div>"+
			"</div>"+
			"<div class=\"d-flex align-items-center pb-3\">" +
			"<div>" +
			"<img class=\"pr-2 pr-md-3\" src=\"static/images/small-icons/message.png\"/>"+
			"</div>"+
			"<div>" +
			"<p class=\"m-0 text-map\">Telefon: 731 544 584</p>"+
			"<p class=\"m-0 text-map\">E-mail: info@acamar.cz</p>"+
			"</div>"+
			"</div>"+
			"</div>"+
			"</div>"+
			"</div>"+
			"</div>"+
			"</div>";

		let infowindow = new google.maps.InfoWindow({
			content: content,
			maxWidth: "auto",
			pixelOffset: {
				width: 200,
				height: 200
			}

		});
		infowindow.open(map, marker);
	}
}
window.initMap = initMap;

