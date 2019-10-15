from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie 
from quotespage.models import Quote
from quotespage.forms import SearchForm
import random


@ensure_csrf_cookie
def random_quote(request, year=""):
	"""Renders a page containing a single random quote, optionally from a specific year."""
	search_form = SearchForm()
	context = {'search_form': search_form}

	quotes = Quote.objects.filter(approved=True)
	if year:
		quotes = quotes.filter(date__year=int(year))
		context['year'] = year
	
	if quotes.count() > 0:
		rand_index = random.randint(0, quotes.count()-1)
		context['quote'] = quotes[rand_index]

	return render(request, 'quotespage/random.html', context)
