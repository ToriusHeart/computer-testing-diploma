from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username', 'last_name', 'first_name', 'patronym', 'group_number', 'is_active')
    list_filter = ('username', 'last_name', 'first_name', 'patronym', 'group_number', 'is_active')
    fieldsets = (
        (None, {
            'fields': ('last_name', 'first_name', 'patronym', 'username')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff')
        })
    )
    search_fields = ('username', 'last_name', 'group_number')
    ordering = ('last_name', 'last_name', 'group_number')

admin.site.register(User, UserAdmin)