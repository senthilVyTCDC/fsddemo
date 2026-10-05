from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Users
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def Display(request):
    # user = Users.objects.all()
    # user = [
    #     {
    #     'username': 'David',
    #     'email': 'david@gmail.com',
    #     'contact':987654321
    # },
    # {

    # }
    # ]
    # return render(request, 'users/user-list.html',{'user1':user})
    user = list(Users.objects.values())
    return JsonResponse(user,safe=False)

def addUser(request):
    return render(request,'users/add-user.html')

@csrf_exempt
def insertUser(request):
    data = json.loads(request.body)
    u_name = data.get('username')
    u_email = data.get('email')
    u_password = data.get('password')
    u_contact = data.get('contact')
    user = Users(
        username=u_name,
        email=u_email,
        password=u_password,
        contact=u_contact
    )
    user.save()
    return JsonResponse({'status':'User Added Successfully'})
    # u_name = request.POST.get('uname')
    # u_email = request.POST.get('uemail')
    # u_password = request.POST.get('upassword')
    # u_contact = request.POST.get('ucontact')
    # user = Users(
    #     username=u_name,
    #     email=u_email,
    #     password=u_password,
    #     contact=u_contact
    # )
    # user.save()
    # return redirect('/users/user-list')

def editUser(request,id):
    user = Users.objects.get(id=id)
    return render(request,'users/edit-user.html',{'users':user})

@csrf_exempt
def updateUser(request,id):
    data = json.loads(request.body)
    u_name = data.get('username')
    u_email = data.get('email')
    u_password = data.get('password')
    u_contact = data.get('contact')
    user = Users.objects.get(id=id)
    user.username = u_name
    user.email = u_email
    user.password = u_password
    user.contact = u_contact
    user.save()
    return JsonResponse({'status':'User Updated Successfully'})
    # u_name = request.POST.get('uname')
    # u_email = request.POST.get('uemail')
    # u_password = request.POST.get('upassword')
    # u_contact = request.POST.get('ucontact')
    # user = Users.objects.get(id=id)
    # user.username = u_name
    # user.email = u_email
    # user.password = u_password
    # user.contact = u_contact
    # user.save()
    # return redirect('/users/user-list')

@csrf_exempt
def deleteUser(request,id):
    user = Users.objects.get(id=id)
    user.delete()
    return JsonResponse({'status':'User Deleted Successfully'})
    # user = Users.objects.get(id=id)
    # user.delete()
    # return redirect('/users/user-list')