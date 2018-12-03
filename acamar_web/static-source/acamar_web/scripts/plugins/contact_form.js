import "jquery-validation/dist/jquery.validate";

$(function () {
	$(".contact-form").each(function () {
		let $this = $(this);

		$this.validate({
			submitHandler: function (form) {
				const formData = new FormData(form);
				$.ajax({
					url: $this.attr("action"),
					method: $this.attr("method"),
					data: formData,
					processData: false,
					contentType: false,
					success: response => {
						if (response.success) {
							dataLayer.push({"form-nazev": "Kontakt", event: "formSent"});
							let thanks = $this.next();
							$this.fadeOut("slow", function () {
								$this.remove();
								thanks.fadeIn("slow");
							});
						}
					}
				});
			}
		});
	});
});