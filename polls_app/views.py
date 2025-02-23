from django.shortcuts import render, redirect

# Create your views here.

#the main URL
def index(request):
    #if the user is logged in redirect to his dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    #if he is not logged in redirect to the login page
    else:
        return redirect('login')