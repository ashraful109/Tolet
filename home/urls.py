# from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('all_house/',views.all_house,name='all_house'),
    path('house/<int:id>',views.single_house,name="single_house"),
   


]

