from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

CITY_CHOICES = (
    ('karachi','Karachi'),
    ('lahore','Lahore'),
    ('islamabad','Islamabad'),
    ('sakhar','Sakhar'),
    ('nawabshah','Nawabshah')
)

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email=email),**kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("user must have an is_staff True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("user must have an is_superuser True")
        user = self.create_user(email,password,**extra_fields)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=11,choices=CITY_CHOICES)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    def has_perm(self,perms):
        return self.is_superuser
    
    def has_module_perms(self,app_label):
        return self.is_superuser