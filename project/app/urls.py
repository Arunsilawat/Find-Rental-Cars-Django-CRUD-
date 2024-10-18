from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('select/<str:em>', views.select, name='select'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('carinfo/', views.carinfo, name='carinfo'),
    path('datadisplay/', views.datadisplay, name='datadisplay'),
    path('delete/<int:pk><str:em>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('save/<int:pk>', views.save, name='save'),
    path('showdata/<str:em>',views.showdata,name='showdata'),
    path('select/<str:em>', views.select, name='select'),
]