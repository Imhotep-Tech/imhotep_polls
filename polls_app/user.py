from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Poll, Choice, User
from django.contrib import messages

# Create your user views here.
@login_required
def dashboard(request):
    polls = Poll.objects.filter(created_by_id=request.user.id)
    context = {
        "username": request.user.username,
        "polls": polls
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

@login_required
def poll_details(request):
    poll_id = request.GET.get("poll_id")

    poll = Poll.objects.get(id=poll_id)
    choices = Choice.objects.filter(poll_id=poll_id)

    context = {
        "username": request.user.username,
        "poll": poll,
        "choices":choices
    }
    return render(request, "poll_details.html", context)