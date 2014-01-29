from django.conf.urls import patterns, url
from books import views


urlpatterns = patterns('',
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
)