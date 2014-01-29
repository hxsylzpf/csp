from django.conf.urls import patterns, url
from geocrowd import views


urlpatterns = patterns('',
    url(r'^geocrowd$', views.geocrowd)
)