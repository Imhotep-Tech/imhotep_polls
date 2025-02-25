#all of the auth related function
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_backends
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm

# Password reset views
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    form_class = PasswordChangeForm

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'
