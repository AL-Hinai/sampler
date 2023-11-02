#urls.py

from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('register_sample/', views.register_sample, name='register_sample'),
    path('sample/<str:unique_code>/', views.sample_page, name='sample_page'),
    path('sample_search/', views.sample_search, name='sample_search'),
    path('code_search/', views.code_search, name='code_search'),
]
