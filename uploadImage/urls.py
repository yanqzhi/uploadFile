from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.image_list, name='image_list'),
    url(r'^upload/', views.upload, name='uploadImage'),
]
