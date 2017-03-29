from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie 
from quotespage.models import Quote
from quotespage.forms import SearchForm

@ensure_csrf_cookie
def permalink(request, quoteid):
	"""Renders a page that lists a single quote."""
	quote_id = int(quoteid) #because Django insists on storing numbers as strings
	quote = get_object_or_404(Quote, id=quote_id)

	search_form = SearchForm()

	context = {'search_form' : search_form, 
			'quote' : quote}

	return render(request, 'quotespage/permalink.html', context)
