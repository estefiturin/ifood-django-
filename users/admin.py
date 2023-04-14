from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# hereda de BaseUserAdmin//paso el modelo//aparecen los usuarios en /admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
    
