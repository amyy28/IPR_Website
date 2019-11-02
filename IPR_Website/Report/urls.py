from django.urls import path
from . import views


urlpatterns = [

path('<int:pk>/', views.ReportView.as_view(), name='Report'),
]