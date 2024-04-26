from django.contrib import admin
from accounts import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Enregistrement des modèles
admin.site.register(models.Profile)
admin.site.register(models.LoginInfo)
admin.site.register(get_user_model(), UserAdmin)