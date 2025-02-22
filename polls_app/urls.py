from django.urls import path
from . import views, auth

urlpatterns = [
    path('', views.index, name="index"),
    path("register/", auth.register, name="register"),
    path("login/", auth.user_login, name="login"),
    path('password_reset/', auth.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('activate/<uidb64>/<token>/', auth.activate, name='activate'),
]
