from django.contrib import admin
from .models import Poll, Choice, User

# Unregister the models if they are already registered
for model in [Poll, Choice, User]:
    if model in admin.site._registry:
        admin.site.unregister(model)

# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(User)