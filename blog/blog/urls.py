from django.urls import path
from login import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('add_user/', views.add_user),
    path('add_role/', views.add_role),
    path('users/', views.users),
    path('roles/', views.roles), 
    path('logout/', views.logout_view),
    path('page1/', views.for_authorized),
    path('page2/', views.for_director),
    path('page3/', views.for_manager),
]