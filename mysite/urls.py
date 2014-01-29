from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from contact import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^books/', include('books.urls', namespace="books")),
    url(r'^geocrowd/', include('geocrowd.urls', namespace="geocrowd")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^contact/', views.contact),
)