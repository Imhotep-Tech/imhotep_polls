from django.urls import path, include
from . import views, auth, user
from allauth.socialaccount.providers.google.views import oauth2_login

urlpatterns = [
    path('', views.index, name="index"),
    path("register/", auth.register, name="register"),
    path("login/", auth.user_login, name="login"),
    path("logout/", auth.user_logout, name="logout"),
    path('password_reset/', auth.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('activate/<uidb64>/<token>/', auth.activate, name='activate'),
    path("dashboard/",user.dashboard , name="dashboard"),
    path("create_poll/",user.create_poll , name="create_poll"),
    path("poll_details/",user.poll_details , name="poll_details"),
    path("vote_to_poll/",user.vote_to_poll , name="vote_to_poll"),
    path('vote_to_poll/<int:poll_id>/', user.vote_to_poll, name='vote_to_poll_with_id'),
]
