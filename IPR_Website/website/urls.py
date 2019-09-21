from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='about-home'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]