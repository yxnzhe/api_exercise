from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'name',
            'password',
            'date_updated',
            'last_login',
            'is_deleted'
        )