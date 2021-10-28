from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from quotespage.forms import NewQuoteForm

def submit(request):
	"""Renders the "submit quote" page, and handles form submissions from it."""
	#if this is a POST request, a new quote form was submitted
	if request.method == 'POST':
		form = NewQuoteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('quotespage:success'))
	#if this is a GET request, we need to display the "submit a quote" page
	else:
		form = NewQuoteForm()

	context = {'form': form}

	return render(request, 'quotespage/submit.html', context)
