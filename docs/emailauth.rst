diy-django email auth
=====================

Django Username Email Auth User Model
-------------------------------------

Create an email auth user model like this::

    from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
    from django.db import models


    class EmailUserManager(models.Manager):
        def get_by_natural_key(self, email):
            return self.get(email=email)


    class EmailUser(AbstractBaseUser, PermissionsMixin):
        USERNAME_FIELD = 'email'
        email = models.EmailField(unique=True)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        objects = EmailUserManager()

        def get_short_name(self):
            return self.email


Installing the Email Username Auth Model
----------------------------------------

In settings.py, set::

    AUTH_USER_MODEL = 'myapp.EmailUser'
