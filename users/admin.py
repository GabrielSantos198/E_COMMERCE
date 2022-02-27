from django.contrib import admin
from .models import User
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields":("bio",)}),
    )

