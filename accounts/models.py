from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    id_number = models.CharField(max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


