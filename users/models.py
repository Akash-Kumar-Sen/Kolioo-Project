import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import TimeStampedModel



# Create your models here.
class User(AbstractUser, TimeStampedModel):
    """ User model for authentication
    """
    user_id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False, unique=True)
    username = models.CharField(max_length=50, db_index=True, unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.username