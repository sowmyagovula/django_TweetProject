from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.tweet_list, name= "Tweet_list"),
    path('create/', views.tweet_create, name= "Tweet_create"),
    path('<int:tweet_id>/edit/', views.tweet_create, name= "Tweet_edit"),
    path('<int:tweet_id>/delete/', views.tweet_delete, name= "Tweet_delete"),


] 