from django.contrib import admin
from .models import User, User_child

#Registering Two Tables inside the admin Panel
admin.site.register(User)
admin.site.register(User_child)