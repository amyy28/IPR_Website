from django.urls import path
from . import views

from .views import (
    TeamsCreateView,
    TeamsUpdateView,
    TeamsDeleteView,
    TeamsDetailView,
)

urlpatterns = [
    path('', views.teams, name='teams-list'),
    path('<int:pk>/report', views.PresentationsDetailView.as_view(), name='Report'),
    path('<int:pk>/', TeamsDetailView.as_view(), name='teams-detail'),
    path('<int:pk>/update/', TeamsUpdateView.as_view(), name='teams-update'),
    path('<int:pk>/delete/', TeamsDeleteView.as_view(), name='teams-delete'),
    path('new/', TeamsCreateView.as_view(), name='teams-create'),

]

