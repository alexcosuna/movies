from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('film/', views.film, name='film'),
    path('history/', views.history, name='history'),
]