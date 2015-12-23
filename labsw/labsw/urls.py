"""labsw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', login_required(TemplateView.as_view(template_name='download/index.html')), name="index"),

    #url(r'^$', include('download.urls', namespace="index")),
    url(r'^add_user/$', 'download.views.add_user', name="add_user"),
    url(r'^logout/$', 'download.views.user_logout', name="user_logout"),
    url(r'^login/$', 'download.views.user_login', name="user_login"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^download/', include('download.urls', namespace='download')),  # 追加する

]
