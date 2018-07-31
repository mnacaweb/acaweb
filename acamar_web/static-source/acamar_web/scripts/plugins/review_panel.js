const review_refresh_rate = 20000;

$(document).ready(function () {
	$.fn.initReviewCycle = function () {
		let $this = $(this);
		let review_container = $this.find(".review-person");
		let dots_container = $this.find(".dots");
		const url = $this.data("url");
		const reviews = $this.data("reviews");
		let timeout = null;

		dots_container.children().click(function () {
			getIdReview($(this).data("id"));
		});

		function getNextReview() {
			clearTimeout(timeout);
			if ($this.length && Array.isArray(reviews)) {
				const current_id = review_container.children().first().data("id");
				const current_index = reviews.indexOf(current_id);
				if (current_index !== -1) {
					const next_index = reviews.length === current_index + 1 ? 0 : current_index + 1;
					$.ajax({
						url: `${url}${reviews[next_index]}/`,
						method: "GET",
						success: response => {
							let html = $(response).hide();
							html.ready(() => {
								review_container.children().fadeOut("slow", function () {
									$(this).replaceWith(html);
									dots_container.find(".active").removeClass("active");
									dots_container.find(`[data-id="${reviews[next_index]}"]`).addClass("active");
									html.fadeIn("slow");
									timeout = setTimeout(getNextReview, review_refresh_rate);
								});
							});
						}
					});
				}
			}
		}

		function getIdReview(id) {
			clearTimeout(timeout);
			$.ajax({
				url: `${url}${id}/`,
				method: "GET",
				success: response => {
					let html = $(response).hide();
					html.ready(() => {
						review_container.children().fadeOut("slow", function () {
							$(this).replaceWith(html);
							dots_container.find(".active").removeClass("active");
							dots_container.find(`[data-id="${id}"]`).addClass("active");
							html.fadeIn("slow");
							timeout = setTimeout(getNextReview, review_refresh_rate);
						});
					});
				}
			});
		}

		timeout = setTimeout(getNextReview, review_refresh_rate);
		return this;
	};

	let reviews_section = $(".reviews-section");
	if (reviews_section.length) {
		reviews_section.initReviewCycle();
	}
});