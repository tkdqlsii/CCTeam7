from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('melonp/', views.melonp, name='melonp'),
    path('geniep/', views.geniep, name='geniep'),
    path('bugsp/', views.bugsp, name='bugsp'),
]
