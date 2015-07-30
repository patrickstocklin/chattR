"""redditscraper URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
#from django.utils import simplejson
#import json as simplejson

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #Home Page
    url(r'^$', 'searchsubreddit.views.home', name='home'),

    #About Page
    url(r'^about/', 'searchsubreddit.views.about', name='about'),

    #Results Page

    #Contact Page
    url(r'^compare/', 'searchsubreddit.views.compare', name='compare'),

    #ProgressBar (issue with importing simplejson )
    #url(r'^progressbarupload/', include('progressbarupload.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)