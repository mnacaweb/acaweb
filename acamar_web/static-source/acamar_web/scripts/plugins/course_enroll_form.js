import "jquery-validation/dist/jquery.validate";
import "bootstrap-multiselect/dist/js/bootstrap-multiselect";
import "bootstrap-multiselect/dist/css/bootstrap-multiselect.css";


$.validator.addMethod("maxsize", function (value, element, param) {
	if (this.optional(element)) {
		return true;
	}

	if ($(element).attr("type") === "file") {
		if (element.files && element.files.length) {
			for (let i = 0; i < element.files.length; i++) {
				if (element.files[i].size > param) {
					return false;
				}
			}
		}
	}

	return true;
}, $.validator.format("File size must not exceed {0} bytes each."));

function getFilename(str) {
	return str.split(/([\\/])/g).pop();
}

$(function () {
	$(".course-enroll-form").each(function () {
		let $this = $(this);
		let course_input = $this.find(".course-enroll-select");
		let cv_button = $this.find(".course-enroll-cv-button");
		let cv_text = $this.find(".course-enroll-cv-text");
		let fileInput = $this.find("input[name='cv']");
		course_input.multiselect({
			// enableCollapsibleOptGroups: true,
			numberDisplayed: 1,
			buttonContainer: "<div class='form-control'></div>",
			buttonClass: "d-flex justify-content-between align-items-center",
			nonSelectedText: "",
			nSelectedText: ` ${course_input.data("selected-text")}`
			// templates: {
			// }
		});

		cv_button.add(cv_text).click(() => {
			$this.find(cv_button.data("target")).click();
		});

		fileInput.change(() => {
			const val = fileInput.val();
			if (val) {
				cv_text.text(getFilename(val));
			} else {
				cv_text.text("&nbsp;");
			}
		});

		$this.validate({
			ignore: ":hidden:not(\".course-enroll-select\")",
			errorPlacement: function (error, element) {
				if ($(element).hasClass("course-enroll-select")) {
					error.insertAfter(element.siblings("div.form-control"));
				}
				else {
					error.insertAfter(element);
				}
			},
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
							dataLayer.push({"form-nazev": "PrihlaskaKurz", event: "formSent"});
							window.location.href = $this.data("redirect");
						}
					}
				});
			},
			rules: {
				cv: {
					maxsize: 25 * 1024 * 1024
				}
			}
		});
	});
});