from django.contrib import admin
from .models import User, User_child

admin.site.register(User)
admin.site.register(User_child)