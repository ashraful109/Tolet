from django.urls import path
from . import views

urlpatterns = [
    path('registraion/',views.registraion, name='registraion'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

  

]
