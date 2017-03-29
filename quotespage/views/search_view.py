from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.html import strip_tags, escape
from quotespage.models import Quote
from quotespage.forms import SearchForm
from quotespage import utils

@ensure_csrf_cookie
def search(request):
	search_string = ''
	found_quotes = None
	search_form = SearchForm()
	if('q' in request.GET) and request.GET['q'].strip():
		search_string = strip_tags(request.GET['q'])
		quote_query = utils.get_query(search_string, ['quotation', 'context'])
		found_quotes = Quote.objects.filter(quote_query).order_by('speaker')
		# Before printing the search string on the results page, ensure it is HTML-escaped
		search_string = escape(search_string)
		
	context = { 'search_form' : search_form,
			'query_string' : search_string,
			'quotes_on_page' : found_quotes }
	return render(request, 'quotespage/search_results.html', context)

