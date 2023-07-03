from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-post/', views.crear_post, name='crear-post'),
    path('crear-autor/', views.crear_autor, name='crear-autor'),
]
