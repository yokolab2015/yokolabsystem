from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^edit/(?P<editing_id>\d+)/$', views.edit, name='edit'),
    url(r'^download/(?P<editing_id>\d+)/$', views.download, name='download'),
    #url(r'^add_user/$',views.add_user, name="add_user"),
    #url(r'^logout/$', views.user_logout, name="user_logout"),
    #url(r'^login/$',views.user_login, name="user_login"),

]
