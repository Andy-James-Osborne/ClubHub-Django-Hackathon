from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('events/', views.event_details, name='event_details'),
    path('events/<slug:slug>/', views.event_details, name='event_details'),
    path('logout/', views.logout_user, name='logout'),
]