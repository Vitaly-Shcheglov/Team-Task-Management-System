from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import bcrypt


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.n


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, extrafields=None):
        if not email:
            raise ValueError("Email должен быть указан")
        email = self.normalize_email(email)
        extrafields = extrafields or {}
        user = self.model(email=email, **extrafields)
        if password:
            hashedpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user.password = hashedpassword.decode('utf-8')
        else:
            user.set_unusable_password()
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, extrafields=None):
        extrafields = extrafields or {}
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        from .models import Role
        extrafields.setdefault('role', Role.objects.filter(name='admin').first())
        return self.create_user(email, password, extrafields)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.email
