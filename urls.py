
from django.contrib import admin
from django.urls import  path
from . import views


app_name = 'polls'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('<int:user_id>/my_booking/', views.my_booking, name='mybooking'),
    path('<int:user_id>/my_booking/create_booking/',views.create_booking, name='create_booking')
]