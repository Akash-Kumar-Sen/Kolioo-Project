from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.viewset_wrapper import ModelViewSetWrapper
from base.permissions import IsUserOwner
from users.serializers import UserSerializer

User = get_user_model()

# Create your views here.
class UserViewSet(ModelViewSetWrapper):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'
    permission_classes = []

    def get_permissions(self):
        """Obtaining permissions specific to actions"""
        
        if self.action in ['create']:
            permission_classes = []
        elif self.action in ['retrieve']:
            permission_classes = [IsUserOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        """Overriding create method to get existing users"""

        # User already exists
        username = request.data.get('username')
        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            serialized_data = UserSerializer(user_obj.first()).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        

        # New user created
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)