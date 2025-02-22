from django.urls import path, include

urlpatterns = [
    path('', include('allauth.socialaccount.providers.google.urls')),
]