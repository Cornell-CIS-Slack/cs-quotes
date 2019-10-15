from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.utils.html import strip_tags, escape
from quotespage.models import Quote, ApiUser
import datetime
import random
import json

def vote(request):
	"""Handles AJAX requests to add an upvote or downvote for a quote."""
	if request.method != 'POST':
		raise Http404("This page cannot be viewed.")
	quoteid = int(request.POST['id'])
	upvote = (request.POST['upvote'].lower() == "true")
	resp_dict = {}
	try:
		quote = Quote.objects.get(id=quoteid)
		quote.votes = (quote.votes + 1 if upvote else quote.votes - 1)
		quote.save()
		resp_dict['success'] = True
		resp_dict['new_count'] = quote.votes
	except Quote.DoesNotExist:
		resp_dict['success']=False

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

def json_random_quote(request):
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

