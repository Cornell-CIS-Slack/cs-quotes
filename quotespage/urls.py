from django.conf.urls import patterns, include, url
from quotespage import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<pagenum>\d+)/$', views.index, name='pages'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^submit/success/$', views.success, name='success'),
    url(r'^about/$', views.about, name='about'),
	url(r'^speakers/$', views.speaker_list, name='speaker-list'),
	url(r'^speaker/(?P<speaker>[-,%.\w]+)/$', views.speaker_archive, name='speaker'),
	url(r'^speaker/(?P<speaker>[-,%.\w]+)/(?P<pagenum>\d+)/$', views.speaker_archive, name='speaker-pages'),
	url(r'^byvotes/$', views.top_voted, name='byvotes'),
	url(r'^byvotes/(?P<pagenum>\d+)/$', views.top_voted, name='byvotes-pages'),
	url(r'^api/vote/$', views.vote, name='vote'),
	url(r'^api/random/$', views.random_quote, name='random'),
	url(r'^api/genkey/$', views.generate_api_key, name='genkey'),
	url(r'^api/submit/$', views.remote_submit, name='remote-submit'),
)
