#all of the auth related function
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_backends
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if '@' in username:
            messages.error(request, "Username can't include @")

        if not '@' in email:
            messages.error(request, "Email must include @!")

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usernaem already taker please choose another one!')
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taker please choose another one or login!')
            return render(request, "register.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            email_verify = False
        )
        user.save()

        # Send verification email
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('activate_mail_send.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_mail(mail_subject, message, 'imhotepfinance@gmail.com', [email], html_message=message)

        messages.success(request, "Account created successfully! Please check your email to verify your account.")
        return redirect("login")

    return render(request, "register.html")

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.email_verify = True
        user.save()

        # Set the backend attribute on the user
        backend = get_backends()[0]
        user.backend = f'{backend.__module__}.{backend.__class__.__name__}'

        login(request, user)
        messages.success(request, "Thank you for your email confirmation. You can now log in to your account.")
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')

def user_login(request):
    if request.method == "POST":
        user_username_mail = request.POST.get('user_username_mail')
        password = request.POST.get('password')

        if '@' not in user_username_mail:
            user = authenticate(request, username=user_username_mail, password=password)
            if user is not None:
                if user.email_verify == True:
                    login(request, user)
                    messages.success(request, "Login successful!")
                    return redirect("dashboard")
                else:
                    messages.error(request, "E-mail not verified!")
            else:
                messages.error(request, "Invalid username or password!")
        else:
            user = User.objects.filter(email=user_username_mail).first()
            if user:
                username = user.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.email_verify == True:
                        login(request, user)
                        messages.success(request, "Login successful!")
                        return redirect("dashboard")
                    else:
                        messages.error(request, "E-mail not verified!")
                else:
                    messages.error(request, "Invalid E-mail or password!")
            else:
                messages.error(request, "Invalid E-mail or password!")

    return render(request, "login.html")

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

# Password reset views
class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'