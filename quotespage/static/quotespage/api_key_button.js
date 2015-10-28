django.jQuery(document).ready(function() {
	django.jQuery('#api_key_button').click(function(event) {
		event.preventDefault();
		django.jQuery.ajax({
			type: "GET",
			url: "http://quotes.cs.cornell.edu/api/genkey/",
			dataType: "json"
		}).done(function(response) {
			if(response) {
				django.jQuery('#api_key_input').val(response.token);
			}
		});
	});
});
