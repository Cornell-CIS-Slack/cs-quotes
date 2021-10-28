from django.urls import path, re_path
from django.views.generic import TemplateView
from quotespage import views

app_name='quotespage'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
	path('speakers/', views.speaker_list, name='speaker-list'),
	re_path(r'^speaker/(?P<speaker>[-,%.\w]+)/$', views.speaker_archive, name='speaker'),
	re_path(r'^speaker/(?P<speaker>[-,%.\w]+)/(?P<pagenum>\d+)/$', views.speaker_archive, name='speaker-pages'),
	path('random/', views.random_quote, name='random'),
	re_path(r'^random/(?P<year>\d{4})/$', views.random_quote, name='random-byyear'),
	path('byvotes/', views.top_voted, name='byvotes'),
	re_path(r'^byvotes/(?P<pagenum>\d+)/$', views.top_voted, name='byvotes-pages'),
    path('about/', TemplateView.as_view(template_name="quotespage/about.html"), name='about'),
	path('search/', views.search, name='search'),
    path('submit/success/', TemplateView.as_view(template_name="quotespage/success.html"), name='success'),
    re_path(r'^page/(?P<pagenum>\d+)/$', views.index, name='pages'),
	re_path(r'^quote/(?P<quoteid>\d+)/$', views.permalink, name='permalink'),
	path('api/vote/', views.vote, name='vote'),
	path('api/random/', views.json_random_quote, name='api-random'),
	path('api/genkey/', views.generate_api_key, name='genkey'),
	path('api/submit/', views.remote_submit, name='remote-submit'),
]


