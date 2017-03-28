from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie 
from quotespage.models import Quote
import datetime
import random

@ensure_csrf_cookie
def index(request, pagenum="0"):
	"""Renders a page of the "home" view, listing quotes in descending date order."""
	QUOTES_PER_PAGE=12
	ipagenum = int(pagenum) #because Django insists on storing numbers as strings
	allquotes = Quote.objects.filter(approved=True).order_by('-date')
	begin_index = ipagenum*QUOTES_PER_PAGE
	end_index = (ipagenum+1)*QUOTES_PER_PAGE
	quotes_on_page = allquotes[begin_index:end_index]
	
	if allquotes[end_index:]:
		morepages = True
	else:
		morepages = False
	
	context = {'quotes_on_page' : quotes_on_page, 'pagenum' : ipagenum, 'morepages' : morepages}
	#On the first page, display a random quote of the day
	if ipagenum == 0:
		todays_quotes = Quote.objects.filter(
							approved=True
						).filter(
							date__month=datetime.date.today().month
						).filter(
							date__day=datetime.date.today().day
						)
		if todays_quotes.count() > 0:
			rand_index = random.randint(0,todays_quotes.count()-1)
			qotd = todays_quotes[rand_index]
			context["qotd"] = qotd

	return render(request, 'quotespage/index.html', context)
