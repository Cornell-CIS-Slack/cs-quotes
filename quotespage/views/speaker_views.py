from django.shortcuts import render, get_list_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from quotespage.models import Quote

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
	other = Quote.objects.order_by('speaker').filter(approved=True,
					speaker_class=Quote.OTHER).values_list('speaker', flat=True).distinct()
	faculty_dashed = [(speaker, slugify_name(speaker)) for speaker in faculty]
	grads_dashed = [(speaker, slugify_name(speaker)) for speaker in grads]
	invited_dashed = [(speaker, slugify_name(speaker)) for speaker in invited]
	other_dashed = [(speaker, slugify_name(speaker)) for speaker in other]
	context = {'faculty_dashed' : faculty_dashed, 
					'grads_dashed' : grads_dashed, 
					'invited_dashed' : invited_dashed,
					'other_dashed' : other_dashed}
	return render(request, 'quotespage/speaker_list.html', context)

def slugify_name(name):
	return name.replace('-','%2D').replace(' ', '-')

def deslugify_name(slug):
	return slug.replace('-',' ').replace('%2D','-')

