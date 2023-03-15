import uuid
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class BaseModel(SafeDeleteModel):
    """ Abstract base model with default safedelete policy
    """
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        abstract = True  # this is an abstract model

    @property
    def is_deleted(self, *args, **kwargs):
        """Property to check if the object is deleted"""
        return self.deleted is not None


class TimeStampedModel(BaseModel):
    """Abstract model with created at and modified at timestamps
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # this is an abstract model


class UUIDTimeStampedModel(TimeStampedModel):
    '''
    Base model that stores created_at, modified_at, and id (which is
    a uuid string).
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True  # this is an abstract model