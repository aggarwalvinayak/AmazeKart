from rest_framework import serializers
# from . models import User


# class UserSerializer(serializers.ModelSerializer):
# 	name = serializers.CharField(max_length = 100)
# 	email = serializers.CharField(max_length = 100)
# 	date = serializers.DateField()

# 	def create(self, validated_data):
# 		return User.objects.create(**validated_data)

# 	class Meta:
# 		model = User

# 		fields = '__all__'
# 		# fields = ('name','email')