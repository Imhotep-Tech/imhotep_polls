from django.urls import path, include

# the url of the google login but alone to not make a conflict at the future
urlpatterns = [
    path('', include('allauth.socialaccount.providers.google.urls')),
]