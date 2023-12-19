from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('display/', views.display_posts, name='display_posts'),
]