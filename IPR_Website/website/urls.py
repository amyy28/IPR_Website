from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='about-home'),

    path('new/', views.createteam.as_view(), name='add-team'),
    path('<int:pk>/', views.saveteam.as_view(), name='save-team'),
]