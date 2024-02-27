# pages/urls.py
from django.urls import path
 
from .views import HomePageView, calculate_sum, plot_graph
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('calculate_sum/', calculate_sum, name='calculate_sum'),
    path('plot/', plot_graph, name='plot_graph'),
]