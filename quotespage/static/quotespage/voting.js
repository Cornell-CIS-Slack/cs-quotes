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
	if(typeof Cookies.get('log') !== "undefined") {
		//If the vote-log object has any entry for this quote ID, it's already been voted
		if(Cookies.getJSON('log')[quote_id] !== undefined) {
			return;
		}
	}
	$.ajax({
		type: "POST",
		url: "https://quotes.cs.cornell.edu/api/vote/",
		data: {"id" : quote_id, "upvote" : is_upvote},
		dataType: "json"
	}).done(function(response) {
		if(response.success === true) {
			$(caller).siblings(".tally").text(response.new_count);
			//Update or set the vote-log cookie
			var votelog;
			if(typeof Cookies.get('log') === "undefined") {
				votelog = {};
			} else {
				votelog = Cookies.getJSON('log');
			}
			votelog[quote_id] = true;
			Cookies.set('log', votelog, {expires : 1});
		}
	});
}
