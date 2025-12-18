from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email is required")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    full_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    address=models.TextField()
    age=models.IntegerField()
    monthly_income=models.DecimalField(max_digits=10,decimal_places=2)

    is_deleted=models.BooleanField(default=False)
    deleted_at=models.DateTimeField(null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    objects=UserManager()


    USERNAME_FIELD='email'


    def __str__(self):
        return self.email