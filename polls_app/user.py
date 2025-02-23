from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
from .models import Poll, Choice, Vote
from django.contrib import messages
from django.db import IntegrityError

# Create your user views here.
@login_required
def dashboard(request):
    polls = Poll.objects.filter(created_by_id=request.user.id)

    for poll in polls:
        poll.shareable_link = poll.generate_link(request)

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
    poll.shareable_link = poll.generate_link(request)
    print(poll.shareable_link)
    choices = Choice.objects.filter(poll_id=poll_id)

    context = {
        "username": request.user.username,
        "poll": poll,
        "choices":choices
    }
    return render(request, "poll_details.html", context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def vote_to_poll(request):

    poll_id = request.GET.get("poll_id")
    poll = Poll.objects.get(id=poll_id)
    choices = Choice.objects.filter(poll_id=poll_id)
    ip_address = get_client_ip(request)

    if request.method == "POST":
        if Vote.objects.filter(poll=poll, ip_address=ip_address):
            messages.error(request, "You have already voted on this poll.")
            return render(request,"vote_submit.html")
        
        selected_choice_id = request.POST.get("selected_choice")

        print("selected_choice_id: ",selected_choice_id)

        print("poll_id: ",poll_id)

        selected_choice = Choice.objects.get(id=selected_choice_id)
        selected_choice.votes += 1

        try:
            Vote.objects.create(poll=poll, ip_address=ip_address)
            selected_choice.save()
            messages.success(request, "Your vote has been recorded!")
        except IntegrityError:
            messages.error(request, "You have already voted on this poll.")

        return render(request,"vote_submit.html")

    # if request.user.is_authenticated:
    #     logout(request)

    context = {
        "poll": poll,
        "choices":choices
    }
    return render(request, "vote_to_poll.html", context)