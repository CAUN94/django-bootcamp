from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('bears/<int:myval>', views.another),
    path('plantilla', views.plantilla),
    path('name', views.name)
]
