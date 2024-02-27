# pages/urls.py
from django.urls import path
 
from .views import HomePageView, calculate_sum
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('calculate_sum/', calculate_sum, name='calculate_sum'),
]