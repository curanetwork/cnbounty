"""Base models"""

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.core.mail import send_mail


class Bounty(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    signup_fields = JSONField()
    report_fields = JSONField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bounties"


class Hunt(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='hunts', on_delete=models.CASCADE)
    bounty = models.ForeignKey(
        Bounty, related_name='hunts', on_delete=models.CASCADE)
    details = JSONField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'bounty')


class Report(models.Model):
    STATUS = (
        ('approved', 'approved'),
        ('declined', 'declined'),
        ('pending', 'pending')
    )
    hunt = models.ForeignKey(
        Hunt, related_name='reports', on_delete=models.CASCADE)
    details = JSONField()
    num_of_stakes = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class UserManager(BaseUserManager):
    def create_user(self, email, eth_address, password=None):
        if not email:
            raise ValueError('You must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.eth_address = eth_address
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, eth_address, password):
        user = self.create_user(
            email,
            eth_address,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, editable=False)
    email = models.EmailField(unique=True)
    eth_address = models.CharField(max_length=42, unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['email', 'eth_address']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return f'@{self.username}'

    def get_full_name(self):
        return f'@{self.username}'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
