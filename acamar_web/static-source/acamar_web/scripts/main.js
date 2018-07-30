import "popper.js";
import "bootstrap";
import "../styles/main.scss";

import "./vendor";

import "./plugins/review_panel";
import "./plugins/team_grid";
import "./plugins/map";
import "./plugins/position_search";
import "./plugins/partners";
import "./plugins/jquery.matchHeight-min";

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

	// Email protection
	setTimeout(
		() => {
			$("a[href^='mailto']").click(function (event) {
				event.preventDefault();
				let $this = $(this);
				const mail = $this.attr("href").slice(7);
				const split = mail.split("@");
				let base = (split.length > 2) ? split.slice(0, split.length-1).join("@") : split[0];
				if (base.startsWith("aca")) {
					base = base.substring(3);
				}
				if (base.endsWith("mar")) {
					base = base.substring(0, base.length - 3);
				}
				base = atob(base);
				window.location.href = `mailto:${base}@${split[split.length-1]}`;
			});
		},
		100
	);



	if( $(".card").length ) {
		$(".card-top").matchHeight();
	}



});
