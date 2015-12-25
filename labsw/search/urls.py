from django.conf.urls import patterns, url, include
#from labsw.views import search
from search import views
#from . import views
#from search.views import *
#from download import views

urlpatterns = patterns('',
	#url(r'^kekka/$', views.show, name='show'),
	#url(r'search/(?P<book_id>\d+)/$', views.show, name='show'),
	#url(r'^search/', views.search, name='search'),
	url(r'^$', views.search, name='search'),
	url(r'^search/(?P<editing_id>\d+)/$', views.download, name='download'),
	#url(r'^search/kekka/$', views.show, name='show'),
	#url(r'^search/kekka/(?P<book_id>\d+)/$', views.show, name='show'),
	#url(r'^result/$', views.result, name='result'),
)
