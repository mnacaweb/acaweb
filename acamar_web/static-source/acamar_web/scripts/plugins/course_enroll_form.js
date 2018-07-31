import "jquery-validation/dist/jquery.validate";
import "bootstrap-multiselect/dist/js/bootstrap-multiselect";
import "bootstrap-multiselect/dist/css/bootstrap-multiselect.css";
// import "bootstrap-multiselect/dist/js/bootstrap-multiselect-collapsible-groups";


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
	$(".course-enroll-form").each(function () {
		let $this = $(this);
		let course_input = $this.find(".course-enroll-select");
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