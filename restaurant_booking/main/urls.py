from django.urls import path, re_path
from . import views

app_name = 'main'
urlpatterns = [
    path('restaurants/statistics', views.statistics, name='statistics'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('restaurants/<str:id>', views.restaurants, name='restaurants'),
    re_path(r'[a-zA-Z0-9]*', views.not_found, name='not found')
]