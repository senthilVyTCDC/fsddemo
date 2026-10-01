from django.urls import include, path
from . import views

urlpatterns = [
    path('user-list/', views.Display, name='user-list' ),
    path('adduser/',views.addUser,name='adduser'),
    path('insertuser/',views.insertUser,name='insertUser'),
    path('edituser/<int:id>',views.editUser,name='editUser'),
    path('updateuser/<int:id>',views.updateUser,name='updateUser'),
    path('deleteuser/<int:id>',views.deleteUser,name='deleteUser')
]