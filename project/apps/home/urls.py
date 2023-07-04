from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-post/', views.crear_post, name='crear-post'),
    path('crear-autor/', views.crear_autor, name='crear-autor'),
]
urlpatterns += staticfiles_urlpatterns()