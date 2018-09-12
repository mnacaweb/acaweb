$(function () {
	$(".team-grid-button").each(function () {
		let $this = $(this);
		let container = $this.parent().parent().children(".team-grid");
		$this.click(function (event) {
			event.stopPropagation();
			let hidden = container.children(".member-hidden");
			let buttonHidden = $(".button-hidden");
			hidden.removeClass("member-hidden");
			hidden.find(".card-top").matchHeight();
			buttonHidden.removeClass("button-hidden");

			$(".team-grid-button").hide();

		});
	});
});
