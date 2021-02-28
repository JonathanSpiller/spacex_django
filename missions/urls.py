from django.urls import path
from . import views

#MAPPING BETWEEN ADDRESSES AND FUNCTIONS

urlpatterns = [
    path('home/', views.home, name='home'),
    path('elon/', views.elon, name='elon')
]