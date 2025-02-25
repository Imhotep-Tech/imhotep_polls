from django.urls import path, include
from . import views, auth, user, user_setting
from allauth.socialaccount.providers.google.views import oauth2_login

# This block of code defines the URL patterns for your Django web application. Each `path` function
# call represents a URL pattern that maps a specific URL to a corresponding view function within your
# Django app. Here's a breakdown of what each URL pattern is doing:
#the urls of the app
urlpatterns = [
    #the main url
    path('', views.index, name="index"),
    #the register url
    path("register/", auth.register, name="register"),
    #login url
    path("login/", auth.user_login, name="login"),
    #logout url
    path("logout/", auth.user_logout, name="logout"),

    #URLs for the forget password
    path('password_reset/', auth.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #URL to activate the users account with the Email
    path('activate/<uidb64>/<token>/', auth.activate, name='activate'),

    #the Users main URLs
    #the dashboard URL
    path("dashboard/",user.dashboard , name="dashboard"),
    #the create Poll URL
    path("create_poll/",user.create_poll , name="create_poll"),
    #the show poll details url
    path("poll_details/",user.poll_details , name="poll_details"),
    #the vote url
    path("vote_to_poll/",user.vote_to_poll , name="vote_to_poll"),
    #the after submit url
    path('vote_to_poll/<int:poll_id>/', user.vote_to_poll, name='vote_to_poll_with_id'),
    #the update url
     path("update_poll/<int:poll_id>",user.update_poll , name="update_poll"),
      path("delete_poll/<int:poll_id>/", user.delete_poll, name="delete_poll"),
    path('password_change/', user_setting.CustomPasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', user_setting.CustomPasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
