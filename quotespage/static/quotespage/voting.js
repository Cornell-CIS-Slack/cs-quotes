$(document).ready(function() {
	$('a.downvote').click(function(event) {
		event.preventDefault();
		vote(this, $(this).parent().data("quoteid"), false);
	});
	$('a.upvote').click(function(event) {
		event.preventDefault();
		vote(this, $(this).parent().data("quoteid"), true);
	});
});

function vote(caller, quote_id, is_upvote) {
	if( $(caller).parent().data("voted") === true ) {
		return;
	}
	$.ajax({
		type: "POST",
		url: "http://quotes.cs.cornell.edu/api/vote/",
		data: {"id" : quote_id, "upvote" : is_upvote},
		dataType: "json"
	}).done(function(response) {
		if(response.success === true) {
			$(caller).siblings(".tally").text(response.new_count);
			$(caller).parent().data("voted", true);
		}
	});
}
