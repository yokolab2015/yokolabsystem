from django.conf.urls.defaults import patterns, url, include
from labsw.views import helloworld

urlpatterns = patterns('',
	(r'^helloworld/$', helloworld),
)


