$(function () {
	$(".partners-item a").click(function (event) {
		event.preventDefault();
		$(".partners-item a").removeClass("active");
		$(this).addClass("active");

		let $this = $(this);
		const content = $($this.next(".partners-content").html()).hide();
		$this.closest(".container").find(".partners-container").children().fadeOut("slow", function () {
			$(this).replaceWith(content);
			content.fadeIn("slow");
		});
	});
});
