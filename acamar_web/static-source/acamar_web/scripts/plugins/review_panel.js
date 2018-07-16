const review_refresh_rate = 20000;

$(document).ready(function () {
	$.fn.initReviewCycle = function () {
		let $this = $(this);
		let review_container = $this.find(".review-person");
		const url = $this.data("url");
		const reviews = $this.data("reviews");

		function getNextReview() {
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

	let reviews_section = $(".reviews-section");
	if (reviews_section.length) {
		reviews_section.initReviewCycle();
	}
});