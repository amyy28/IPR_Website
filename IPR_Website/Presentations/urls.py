from django.urls import path
from . import views

urlpatterns = [
    path('', views.presentations, name='presentations'),

]