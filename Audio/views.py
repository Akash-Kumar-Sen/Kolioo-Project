from rest_framework.permissions import IsAuthenticated
from base.viewset_wrapper import ModelViewSetWrapper
from Audio.models import MusicFile
from Audio.serializers import MusicFileSerializer

class AudioViewset(ModelViewSetWrapper):
    """Viewset for audio upload and list"""
    queryset = MusicFile.objects.all()
    serializer_class = MusicFileSerializer
    permission_classes = (IsAuthenticated,)
