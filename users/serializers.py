from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('pk', 'name', 'last_name', 'email', 'phone', 'address', 'description')