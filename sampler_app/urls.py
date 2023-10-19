from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_sample/', views.register_sample, name='register_sample'),
]
