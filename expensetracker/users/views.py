from django.shortcuts import render, redirect
from .models import Users

# Create your views here.

def Display(request):
    user = Users.objects.all()
    # user = [
    #     {
    #     'username': 'David',
    #     'email': 'david@gmail.com',
    #     'contact':987654321
    # },
    # {

    # }
    # ]
    return render(request, 'users/user-list.html',{'user1':user})

def addUser(request):
    return render(request,'users/add-user.html')

def insertUser(request):
    u_name = request.POST.get('uname')
    u_email = request.POST.get('uemail')
    u_password = request.POST.get('upassword')
    u_contact = request.POST.get('ucontact')
    user = Users(
        username=u_name,
        email=u_email,
        password=u_password,
        contact=u_contact
    )
    user.save()
    return redirect('/users/user-list')

def editUser(request,id):
    user = Users.objects.get(id=id)
    return render(request,'users/edit-user.html',{'users':user})

def updateUser(request,id):
    u_name = request.POST.get('uname')
    u_email = request.POST.get('uemail')
    u_password = request.POST.get('upassword')
    u_contact = request.POST.get('ucontact')
    user = Users.objects.get(id=id)
    user.username = u_name
    user.email = u_email
    user.password = u_password
    user.contact = u_contact
    user.save()
    return redirect('/users/user-list')

def deleteUser(request,id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('/users/user-list')