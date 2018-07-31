import "jquery-validation/dist/jquery.validate";

$(function () {
	$(".login-form").each(function () {
		let $this = $(this);

		let validator = $this.validate({
			submitHandler: function (form) {
				let data = new FormData(form);
				$.ajax({
					url: $this.attr("action"),
					method: "POST",
					data: data,
					processData: false,
					contentType: false,
					success: response => {
						if (response.success) {
							window.location.href = response.redirect;
						} else {
							validator.showErrors({password: response.data["__all__"][0]});
						}
					}
				});
			}
		});
	});
});