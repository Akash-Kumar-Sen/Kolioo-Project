# Generated by Django 4.1.7 on 2023-03-15 14:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicFile',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='NA', max_length=200)),
                ('file_type', models.CharField(default='NA', max_length=20)),
                ('genre', models.CharField(default='NA', max_length=50)),
                ('audio_length', models.DurationField(default=None, null=True)),
                ('file_size', models.PositiveIntegerField(default=None, null=True)),
                ('file_path', models.FileField(upload_to='music_files')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]