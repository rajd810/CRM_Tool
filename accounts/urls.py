from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.loginPage, name= 'login'),
	path('logout/', views.logoutUser, name= 'logout'),
	path('register/', views.registerPage, name= 'register'),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('create_order/', views.createOrder, name='create_order'),
   # path('update_order/<str:pk>/', views.update_order, name='update_order'),
]
