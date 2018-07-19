$(function () {
	$(".position-search").each(function () {
		let $this = $(this);
		let form = $this.find("form");
		const url = form.attr("action");
		const method = form.attr("method");
		let queryInput = form.find("#queryInput");
		let autocompleteUrl = queryInput.data("url");
		let resultContainer = $this.find(".position-search-results");
		let autocompleteContainer = form.find(".position-search-autocomplete");
		let categories = form.find(".category");
		let pacts = $this.find(".pacts .tab");

		function updateCategoryCount(positions) {
			let category_count = positions.map(function () {return this.dataset.category;}).get().reduce((agg, val) => {
				agg[val] ? agg[val] += 1 : agg[val] = 1;
				return agg;
			}, {});
			categories.each(function () {
				let $this = $(this);
				$this.find(".count").text(category_count[$this.data("id")] | 0);
			});
		}

		function applyCategoryFilter(positions) {
			const filter = categories.filter(".active-count").map(function () {
				return $(this).data("id");
			}).get();
			if (filter.length){
				positions.each(function () {
					$this = $(this);
					if (filter.indexOf($this.data("category")) !== -1) $this.removeClass("cfilter");
					else $this.addClass("cfilter");
				});
			} else {
				positions.removeClass("cfilter");
			}
		}

		function applyPactFilter(positions, pact_id) {
			if (pact_id) {
				positions.each(function () {
					let $this = $(this);
					const position_pacts = $this.data("pact");
					if (position_pacts.indexOf(pact_id) !== -1) $this.removeClass("pfilter");
					else $this.addClass("pfilter");
				});
			} else {
				positions.removeClass("pfilter");
			}
		}

		form.submit((event) => {
			event.preventDefault();
			const value = queryInput.val().trim();
			if (value) {
				$.ajax({
					url: url,
					method: method,
					data: form.serialize(),
					success: response => {
						let html = $(response).hide();
						html.ready(() => {
							resultContainer.children().fadeOut("slow", function () {
								updateCategoryCount(html.find(".position"));
								$(this).replaceWith(html);
								html.fadeIn("slow");
							});
						});
					}
				});
			}
		});

		queryInput.on("keyup", () => {
			const query = queryInput.val();
			if(query.length < 3) {
				return false;
			}

			$.ajax({
				url: autocompleteUrl,
				method: "GET",
				data: form.serialize(),
				success: response => {
					autocompleteContainer.html(response);
				}
			});
		});
		queryInput.on("focusin", () => {
			autocompleteContainer.show();
		});
		queryInput.on("focusout", () => {
			autocompleteContainer.hide();
		});

		categories.each(function () {
			let $this = $(this);
			$this.click( () => {
				$this.toggleClass("active-count");
				applyCategoryFilter(resultContainer.find(".position"));
			});
		});

		pacts.each(function () {
			let $this = $(this);
			$this.click(() => {
				pacts.parent().removeClass("border-active");
				pacts.removeClass("active");
				$this.parent().addClass("border-active");
				$this.addClass("active");
				applyPactFilter(resultContainer.find(".position"), $this.data("id"));
			});
		});
	});
});