from django.conf.urls import patterns, url, include
#from labsw.views import search
from search import views
#from . import views
#from search.views import *

urlpatterns = patterns('',
	#url(r'^kekka/$', views.show, name='show'),
	#url(r'search/(?P<book_id>\d+)/$', views.show, name='show'),
	url(r'^search/$', views.search, name='search'),
	url(r'^search/kekka/$', views.show, name='show'),
	#url(r'^search/kekka/(?P<book_id>\d+)/$', views.show, name='show'),
	#url(r'^result/$', views.result, name='result'),
)