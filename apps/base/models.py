"""Base models"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.core.mail import send_mail
from django.utils.text import slugify
from django_extensions.db.fields.json import JSONField
from django_extensions.db.models import TimeStampedModel


class Bounty(TimeStampedModel):
    name = models.CharField(max_length=100)
    percent_share = models.FloatField()
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, default='fa-gift')
    intro = models.CharField(max_length=60)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    signup_form = JSONField()
    report_form = JSONField()

    class Meta:
        verbose_name_plural = "Bounties"

    def __str__(self):
        return self.name    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Bounty, self).save(*args, **kwargs)


class Hunt(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='hunts', on_delete=models.CASCADE)
    bounty = models.ForeignKey(
        Bounty, related_name='hunts', on_delete=models.CASCADE)
    details = JSONField()

    class Meta:
        unique_together = ('user', 'bounty')

    def __str__(self):
        return self.user.email


class Report(TimeStampedModel):
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


class UserManager(BaseUserManager):
    def create_user(self, username, email, eth_address, password=None):
        if not email:
            raise ValueError('You must have an email address')

        if not username:
            raise ValueError('You must have a username')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.username = username
        user.eth_address = eth_address
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, eth_address, password):
        user = self.create_user(
            username,
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
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    eth_address = models.CharField(max_length=44, unique=True)
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
