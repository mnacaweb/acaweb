$(function () {
	$(".team-grid-button").each(function () {
		let $this = $(this);
		let container = $this.parent().parent().children(".team-grid");
		const url = $this.data("href");
		$this.click(function (event) {
			event.stopPropagation();
			$.ajax({
				url: url,
				method: "GET",
				success: response => {
					let html = $(response);
					html.hide();
					html.ready(() => {
						container.append(html);
						html.slideDown("slow");
						$this.remove();
					});
				}
			});
		});
	});
});