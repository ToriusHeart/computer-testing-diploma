from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first_name'), max_length=50, help_text="Имя")
    last_name = models.CharField(_('last_name'), max_length=50, help_text="Фамилия")
    patronym = models.CharField(_('patronym'), max_length=50, help_text="Отчество (при отсутствии отметьте символом \"-\")")
    username = models.CharField(_('username'), unique=True, max_length=50, help_text="Юзернейм")
    group_number = models.CharField(_('group_number'), max_length=30, help_text="Номер группы")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'patronym', 'group_number']
    
    objects = CustomUserManager()