from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Choice, User
from django.contrib import messages

# Create your user views here.
@login_required
def dashboard(request):
    context = {
        "username": request.user.username,
    }
    return render(request, "dashboard.html", context)

@login_required
def create_poll(request):
    if request.method=="POST":
        question = request.POST.get("question")
        choices = request.POST.getlist("choices")

        poll = Poll.objects.create(
            question=question,
            created_by=request.user,
        )

        for choice in choices:
            new_choice = Choice.objects.create(
                poll=poll,
                choice_text=choice,
            )

        messages.success(request, "Poll added successfully!")
        return redirect("dashboard")
    
    context = {
        "username": request.user.username,
    }
    return render(request, "create_poll.html", context)
