import "jquery-validation/dist/jquery.validate";


$.validator.addMethod( "maxsize", function( value, element, param ) {
	if ( this.optional( element ) ) {
		return true;
	}

	if ( $( element ).attr( "type" ) === "file" ) {
		if ( element.files && element.files.length ) {
			for ( let i = 0; i < element.files.length; i++ ) {
				if ( element.files[ i ].size > param ) {
					return false;
				}
			}
		}
	}

	return true;
}, $.validator.format( "File size must not exceed {0} bytes each." ) );

function getFilename(str) {
	return str.split(/([\\/])/g).pop();
}

$(function () {
	let contactModal = $("#contactModal");

	if (contactModal.length) {
		let thanksModal = $("#thanksModal");
		let positionForm = contactModal.find(".position-form");
		let cv_button = contactModal.find(".position-cv-button");
		let cv_text = contactModal.find(".position-cv-text");
		let fileInput = contactModal.find("input[name='cv']");

		cv_button.add(cv_text).click(() => {
			contactModal.find(cv_button.data("target")).click();
		});

		fileInput.change(() => {
			const val = fileInput.val();
			if (val){
				cv_text.text(getFilename(val));
			} else {
				cv_text.text("&nbsp;");
			}
		});

		positionForm.validate({
			submitHandler: function (form) {
				const formData = new FormData(form);
				$.ajax({
					url: positionForm.attr("action"),
					method: positionForm.attr("method"),
					data: formData,
					processData: false,
					contentType: false,
					success: response => {
						if (response.success) {
							contactModal.modal("hide");
							thanksModal.modal("show");
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
	}
});