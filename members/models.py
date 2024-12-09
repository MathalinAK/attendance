from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
class membersManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        if username is None:
            username = ""

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if username is None:
            username = ""
        user = self.create_user(email, password, username=username, **extra_fields)
        return user

class members(AbstractBaseUser, PermissionsMixin):
   
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    punch_in = models.DateTimeField(null=True, blank=True) 
    punch_out = models.DateTimeField(null=True, blank=True)  
    IPAddr=models.CharField(max_length=30,default=True )
    location=models.CharField(max_length=100,default=True)


    objects = membersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email if self.email else "No Email Provided"
