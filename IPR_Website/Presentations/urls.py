from django.urls import path
from . import views
from .views import (
    PresentationsCreateView,
    PresentationsUpdateView,
    PresentationsDeleteView,
    PresentationsDetailView,
)

urlpatterns = [
    path('', views.presentations, name='presentations'),
    path('<int:pk>/', PresentationsDetailView.as_view(), name='presentations-detail'),
    path('<int:pk>/update/', PresentationsUpdateView.as_view(), name='presentations-update'),
    path('<int:pk>/delete/', PresentationsDeleteView.as_view(), name='presentations-delete'),
    path('new/', PresentationsCreateView.as_view(), name='presentations-create'),

]