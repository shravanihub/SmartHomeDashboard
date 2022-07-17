from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    fname = models.CharField(max_length=64, blank=False, verbose_name="First Name")
    lname = models.CharField(max_length=64, blank=False, verbose_name="Last Name")
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=128, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['fname']
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email



    @property
    def is_staff(self):
        return self.is_admin