from django.conf.urls import patterns, url, include
#from labsw.views import search
from . import views
#from . import views
#from search.views import *
#from download import views

urlpatterns = patterns('',
	#url(r'^search/', views.search, name='search'),
	url(r'^$', views.search, name='search'),
	url(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
	url(r'^delete/(?P<editing_id>\d+)/$', views.delete, name='delete'),
	url(r'^search/(?P<editing_id>\d+)/$', views.download, name='download'),
	#url(r'^search/kekka/(?P<book_id>\d+)/$', views.show, name='show'),
)
