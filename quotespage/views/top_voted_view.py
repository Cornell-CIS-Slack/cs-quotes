from django.shortcuts import render 
from quotespage.models import Quote 

def top_voted(request, pagenum="0"):
	"""Renders a page of quotes sorted by highest voted"""
	QUOTES_PER_PAGE=15
	ipagenum = int(pagenum)
	quotes_by_vote = Quote.objects.filter(approved=True).filter(votes__gt=0).order_by('-votes', '-date')
	begin_index = ipagenum*QUOTES_PER_PAGE
	end_index = (ipagenum+1)*QUOTES_PER_PAGE
	quotes_on_page = quotes_by_vote[begin_index:end_index]

	if quotes_by_vote[end_index:]:
		morepages = True
	else:
		morepages = False

	context = {'quotes_on_page' : quotes_on_page,
			'pagenum' : ipagenum,
			'morepages' : morepages}
	return render(request, 'quotespage/top_votes.html', context)

