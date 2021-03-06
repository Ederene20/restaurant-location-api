import jwt
from rest_framework_api_key.models import APIKey
from datetime import datetime, timedelta
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.conf import settings
from django.db import models
from abstract.models import AbstractModel

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, name, password=None):

        if username is None:
            raise TypeError("User must have a username")

        if name is None:
            raise TypeError("User must have a name")

        user = self.model(username=username, name=name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, name, password):

        if password is None:
            raise TypeError("User must have a password")

        user = self.create_user(username, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, AbstractModel):
    username = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    @property
    def secret_key(self):
        return self._generate_secret_key()

    @property
    def public_key(self):
        return self._generate_public_key()

    def get_name(self):
        return self.name

    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode(
            {
                "id": self.pk,
                #"exp": int(dt.strftime("%d")),
                "name": self.username,
            }, settings.SECRET_KEY, algorithm="HS256"
        )

        return token

    def _generate_secret_key(self):
        username = str(self.username)
        private_key = APIKey.objects.create_key(name="X-Secret-Key" + "-" + username)
        private_key = private_key[1]
        return private_key

    def _generate_public_key(self):
        username = str(self.username)
        public_key = APIKey.objects.create_key(name="X-Public-Key" + "-" + username)
        public_key = public_key[1]
        return public_key


