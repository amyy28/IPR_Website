from django.urls import path
from . import views
from .views import (
    SkitsCreateView,
    SkitsUpdateView,
    SkitsDeleteView,
    SkitsDetailView,
)

urlpatterns = [
    path('', views.skits, name='skits-list'),
    path('<int:pk>/', SkitsDetailView.as_view(), name='skits-detail'),
    path('<int:pk>/update/', SkitsUpdateView.as_view(), name='skits-update'),
    path('<int:pk>/delete/', SkitsDeleteView.as_view(), name='skits-delete'),
    path('new/', SkitsCreateView.as_view(), name='skits-create'),

]