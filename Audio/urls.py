from django.urls import include, path
from rest_framework import routers
from Audio.views import AudioViewset

router = routers.DefaultRouter()
router.register(r'audio', AudioViewset, basename='audio-v1')


app_name = 'audio'

urlpatterns = [
    path('', include(router.urls)),
]