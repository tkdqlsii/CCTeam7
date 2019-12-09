from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('melonp', views.index, name='melonp'),
    path('geniep', views.index, name='geniep'),
    path('bugsp', views.index, name='bugsp'),
]
