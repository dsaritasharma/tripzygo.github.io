from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('index', views.index, name="index"),
    path('logout', views.logout, name="logout"),
    path('contacts', views.contacts, name="contacts"),
    ##rest password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>password/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')   
         
  
]