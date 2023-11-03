from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('calculation/', views.calculation, name='calculation'),
    # path('about/',views.about,name="about"),
    ## path('details/', views.details, name="details"),
    # path('thanks/', views.thanks, name="thanks"),

]
