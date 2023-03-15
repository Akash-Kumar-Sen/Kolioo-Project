from django.db import models
from base.models import UUIDTimeStampedModel

class MusicFile(UUIDTimeStampedModel):
    """Django model to store the music file along with Metadata
    """
    title = models.CharField(max_length=200, default='NA')
    file_type = models.CharField(max_length=20, default='NA')
    genre = models.CharField(max_length=50, default='NA')
    audio_length = models.FloatField(null=True, default=None)
    file_size = models.PositiveIntegerField(null=True, default=None)
    file_path = models.FileField(upload_to='music_files')

    def __str__(self) -> str:
        return f'{self.title}.{self.file_type}'