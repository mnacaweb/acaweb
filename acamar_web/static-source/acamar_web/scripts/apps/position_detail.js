import "jquery-validation/dist/jquery.validate";

const thanksModalTimeout = 3000;

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

$(function () {
	let contactModal = $("#contactModal");

	if (contactModal.length) {
		let thanksModal = $("#thanksModal");
		let positionForm = contactModal.find(".position-form");

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
							setTimeout(() => {
								thanksModal.modal("hide");
							}, thanksModalTimeout);
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