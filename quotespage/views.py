from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.utils.html import strip_tags, escape
from .models import Quote, ApiUser
from .forms import NewQuoteForm
import datetime
import random
import json

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
	

def success(request):
	return render(request, 'quotespage/success.html', {})


def about(request):
	return render(request, 'quotespage/about.html', {})

@ensure_csrf_cookie
def speaker_archive(request, speaker, pagenum="0"):
	"""Renders a page of quotes by a single speaker."""
	QUOTES_PER_PAGE=10
	ipagenum = int(pagenum)
	speaker_spaces = deslugify_name(speaker)
	speaker_quotes = get_list_or_404(Quote.objects.order_by('-date'), 
					speaker__iexact=speaker_spaces,approved=True)
	begin_index = ipagenum*QUOTES_PER_PAGE
	end_index = (ipagenum+1)*QUOTES_PER_PAGE
	quotes_on_page = speaker_quotes[begin_index:end_index]

	if speaker_quotes[end_index:]:
		morepages = True
	else:
		morepages = False

	context = {'quotes_on_page' : quotes_on_page, 
					'pagenum' : ipagenum, 
					'morepages' : morepages,
					'speaker' : speaker,
					'speaker_spaces': speaker_spaces}
	return render(request, 'quotespage/speaker.html', context)
		

def speaker_list(request):
	"""Renders the page listing all known speakers by category."""
	faculty = Quote.objects.order_by('speaker').filter(approved=True,
					speaker_class=Quote.FACULTY).values_list('speaker', flat=True).distinct()
	grads = Quote.objects.order_by('speaker').filter(approved=True,
					speaker_class=Quote.GRAD_STUDENT).values_list('speaker', flat=True).distinct()
	invited = Quote.objects.order_by('speaker').filter(approved=True,
					speaker_class=Quote.INVITED_SPEAKER).values_list('speaker', flat=True).distinct()
	faculty_dashed = [(speaker, slugify_name(speaker)) for speaker in faculty]
	grads_dashed = [(speaker, slugify_name(speaker)) for speaker in grads]
	invited_dashed = [(speaker, slugify_name(speaker)) for speaker in invited]
	context = {'faculty_dashed' : faculty_dashed, 
					'grads_dashed' : grads_dashed, 
					'invited_dashed' : invited_dashed}
	return render(request, 'quotespage/speaker_list.html', context)

def slugify_name(name):
	return name.replace('-','%2D').replace(' ', '-')

def deslugify_name(slug):
	return slug.replace('-',' ').replace('%2D','-')

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


def vote(request):
	"""Handles AJAX requests to add an upvote or downvote for a quote."""
	if request.method != 'POST':
		raise Http404("This page cannot be viewed.")
	quoteid = int(request.POST['id'])
	upvote = (request.POST['upvote'].lower() == "true")
	resp_dict = {}
	quote = Quote.objects.get(id=quoteid)
	if not quote:
		resp_dict['success']=False
	else:
		quote.votes = (quote.votes + 1 if upvote else quote.votes - 1)
		quote.save()
		resp_dict['success'] = True
		resp_dict['new_count'] = quote.votes

	return HttpResponse(json.dumps(resp_dict), content_type="application/javascript")

def generate_api_key(request):
	"""Handles AJAX requests for a new API key."""
	new_key = ApiUser.objects.get_unique_key()
	return HttpResponse(json.dumps({'token' : new_key}), content_type="application/javascript")

@csrf_exempt
def remote_submit(request):
	if request.method != 'POST':
		raise Http404("This page cannot be viewed.")
	if not 'HTTP_TOKEN' in request.META:
		raise PermissionDenied
	token = request.META['HTTP_TOKEN']
	if not ApiUser.objects.filter(api_key=token).exists():
		raise PermissionDenied("Invalid API key")
	if ApiUser.objects.get(api_key=token).key_expires < datetime.date.today():
		raise PermissionDenied("Expired API key")
	new_quote = Quote(
			speaker = request.POST['speaker'],
			speaker_class = Quote.GRAD_STUDENT,
			date = datetime.date.today(),
			quotation = escape(strip_tags(request.POST['quotation'])),
			context = escape(strip_tags(request.POST['context']))
	)
	new_quote.save()
	return HttpResponse(status=201)

def random_quote(request):
	"""Handles AJAX requests for a random quote."""
	quotes = Quote.objects.filter(approved=True)
	if 'speaker' in request.GET:
		quotes = quotes.filter(speaker=request.GET['speaker'])
	if 'year' in request.GET:
		quotes = quotes.filter(date__year=int(request.GET['year']))
	if 'month' in request.GET:
		quotes = quotes.filter(date__month=int(request.GET['month']))
	if 'day' in request.GET:
		quotes = quotes.filter(date__day=int(request.GET['day']))
        if quotes.count() == 0:
                return HttpResponse("", content_type="text/text")
	rand_index = random.randint(0,quotes.count()-1)
	quote = quotes[rand_index]
	return HttpResponse(json.dumps(quote.get_fields_dict(), default=json_patch), content_type="application/javascript")


def json_patch(obj):
	"""Patches the gaping hole in json.dumps by allowing it to serialize Python Datetimes"""
	if isinstance(obj, datetime.datetime) \
			or isinstance(obj, datetime.date) \
			or isinstance(obj, datetime.time):
		return obj.isoformat()
	raise TypeError("Unknown non-serializable type")
