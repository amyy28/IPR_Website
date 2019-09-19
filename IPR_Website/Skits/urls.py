from django.urls import path
from . import views

urlpatterns = [
    path('', views.skits, name='skits'),

]