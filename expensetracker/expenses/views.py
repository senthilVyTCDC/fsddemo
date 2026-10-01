from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

def expenses_list(request):
    person = {
        "name": "John Doe",
    }
    return render(request, 'expenses/expenses-list.html', {"persons": person})

def Home(request):
    # return HttpResponse("Welcome to Expense Tracker Home Page "+str(id))
    # return redirect('/expenses/expenses-list/')
    return JsonResponse({"message": "Welcome to Expense Tracker Home Page "})