from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('restaurants', views.restaurants, name='restaurants'),
    path('restaurants/<str:id>', views.restaurants, name='restaurants'),
    path('restaurants/statistics', views.statistics, name='statistics'),
]