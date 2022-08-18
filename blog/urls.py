from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('post_list',views.PostList.as_view(),name="post-list"),
]