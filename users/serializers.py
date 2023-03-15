# Django imports
from django.contrib.auth import get_user_model

# Third party imports
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserBaseSerializer(serializers.ModelSerializer):
    """Reusable base serializer for the user model
    """
    class Meta:
        model = User
        fields = ['user_id', 'username', 'name', 'email', 'phone',
                  'created_at', 'modified_at']
        
class UserSerializer(UserBaseSerializer):
    """Serializer for user viewsets
    """
    access = serializers.SerializerMethodField(method_name='get_access_token', read_only=True)
    refresh = serializers.SerializerMethodField(method_name='get_refresh_token', read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'name', 'email', 'phone',
                  'created_at', 'modified_at', 'access', 'refresh']
        read_only_fields = ['created_at', 'modified_at']
        
    def get_access_token(self, user):
        """Method to get access token
        """
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def get_refresh_token(self, user):
        """Method to generate refresh token
        """
        refresh = RefreshToken.for_user(user)
        return str(refresh)
