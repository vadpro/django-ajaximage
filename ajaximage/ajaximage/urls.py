from django.conf.urls import url

from .views import ajaximage


urlpatterns = [
    url('^upload/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)/\?upload_to=(?P<upload_to>.*)',
        ajaximage, name='ajaximage'),
]