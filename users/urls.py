from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users-v1')

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]