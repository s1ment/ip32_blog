from django.urls import path
from login import views

urlpatterns = [
    path('add_user/', views.add_user),
    path('add_role/', views.add_role),
    path('users/', views.users),
    path('', views.index),
    path('login/', views.login),
    path('logout/', views.logout_view),
]