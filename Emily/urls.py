from django.conf.urls import url
from . import views

app_name = 'Emily'

urlpatterns = [
    # /emily/
    url(r'^$', views.index, name='index'),
    url(r'^json$', views.json, name='json'),

]
