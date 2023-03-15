import os
import magic
import mutagen
from rest_framework import serializers
from Audio.models import MusicFile
from Audio.exceptions import FileformatNotSupported

class MusicFileSerializer(serializers.ModelSerializer):
    """ Serializer for the uploader music files
    """

    class Meta:
        model = MusicFile
        fields = '__all__'
        read_only_fields = ['id', 'title', 'file_type', 'genre',
                            'audio_length', 'file_size', 'created_at', 'modified_at']
        
    def create(self, validated_data):
        music_file = validated_data.get('file_path')
        file_type = magic.from_buffer(music_file.read(), mime=True)

        if file_type not in ['audio/mpeg', 'audio/wav']:
            raise FileformatNotSupported()

        music_file.seek(0)
        audio = mutagen.File(music_file)
        metadata = {
            'title': music_file.name,
            'file_type': file_type,
            'genre': audio.get('genre', 'NA'),
            'audio_length': audio.info.length,
            'file_path': music_file
        }

        return MusicFile.objects.create(**metadata)