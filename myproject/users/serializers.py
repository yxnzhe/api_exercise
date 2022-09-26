from rest_framework import serializers
from .models import User, ForgotPassword

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

class ForgotPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = ForgotPassword
        fields = (
            'id',
            'user',
            'token',
            'expire_at'
        )