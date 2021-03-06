import "./polyfill";

$(function () {
	$.ajaxSetup({
		beforeSend: function (xhr, settings) {
			function getCookie(name) {
				let cookieValue = null;
				if (document.cookie && document.cookie !== "") {
					const cookies = document.cookie.split(";");
					for (let i = 0; i < cookies.length; i++) {
						const cookie = jQuery.trim(cookies[i]);
						// Does this cookie string begin with the name we want?
						if (cookie.substring(0, name.length + 1) === (name + "=")) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
						}
					}
				}
				return cookieValue;
			}

			if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
				// Only send the token to relative URLs i.e. locally.
				xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
			}
		}
	});
});
import "popper.js";
import "bootstrap";
import "jquery-match-height/dist/jquery.matchHeight";
import "waypoints/lib/jquery.waypoints";
import "jquery.counterup";
import "jquery.parallax-scroll/js/jquery.parallax-scroll";
import "../styles/main.scss";
import {WOW} from "wowjs";

window.WOW = WOW;

import "./vendor";

import "./plugins/review_panel";
import "./plugins/team_grid";
import "./plugins/map";
import "./plugins/position_search";
import "./plugins/partners";
import "./plugins/course_enroll_form";
import "./plugins/login";
import "./plugins/contact_form";

import "./apps/position_detail";

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
	$(".dropdown-toggle").on("click", function (e) {
		e.preventDefault();
		if ($(".dropdown-menu").hasClass("show")) {
			$(".dropdown-menu").removeClass("show");
		} else {
			$(".dropdown-menu").addClass("show");
		}
	});

	// Email protection

	$("a[href^='mailto']").click(function (event) {
		let $this = $(this);
		const mail = $this.attr("href").slice(7);
		const split = mail.split("@");
		let base = (split.length > 2) ? split.slice(0, split.length - 1).join("@") : split[0];
		if (base.startsWith("aca") && base.endsWith("mar")) {
			event.preventDefault ? event.preventDefault() : (event.returnValue = false);
			base = base.substring(3);
			base = base.substring(0, base.length - 3);
			base = atob(base);
			window.location.href = `mailto:${base}@${split[split.length - 1]}`;
		}
	});


	if ($(".card").length) {
		$(".card-top").matchHeight();
	}


	new WOW().init();

	window.onscroll = function () {
		if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
			document.getElementById("scroll-totop").style.display = "block";
		} else {
			document.getElementById("scroll-totop").style.display = "none";
		}
	};

	$("#scroll-totop").click(function topFunction() {
		document.body.scrollTop = 0; // For Safari
		document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
	});
});
