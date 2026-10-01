
from django.urls import path
from . import views

urlpatterns = [
    path('expenses-list/', views.expenses_list, name='expenses-list' ),
    path('home/', views.Home, name='home' ),

]
