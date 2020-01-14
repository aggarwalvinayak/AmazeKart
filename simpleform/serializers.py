from rest_framework import serializers
from . models import UserDatabase


class UserDatabaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDatabase

        fields = '__all__'
        # fields = ('name','email')