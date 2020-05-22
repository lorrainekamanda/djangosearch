from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$', views.home, name = 'search-home'),
    url('^about/$', views.about, name = 'blog-about')
]