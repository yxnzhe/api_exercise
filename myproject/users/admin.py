from django.contrib import admin
from .models import User, ForgotPassword

admin.site.register(User)
admin.site.register(ForgotPassword)