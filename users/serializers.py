from rest_framework import serializers
from .models import User, User_child

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'street_address', 'city_address', 'state_address', 'zip_code']

class User_child_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_child
        fields = ['id' ,'parent', 'child_first_name','child_last_name']

