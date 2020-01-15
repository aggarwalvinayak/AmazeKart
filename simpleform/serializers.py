from rest_framework import serializers
from . models import UserDatabase


class UserDatabaseSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length = 100)
	email = serializers.CharField(max_length = 100)
	date = serializers.DateField()

	def create(self, validated_data):
		return UserDatabase.objects.create(**validated_data)

	class Meta:
		model = UserDatabase

		fields = '__all__'
		# fields = ('name','email')