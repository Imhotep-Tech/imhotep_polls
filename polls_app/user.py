from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your user views here.
@login_required
def dashboard(request):
    context = {
        "username": request.user.username,
    }
    return render(request, "dashboard.html", context)