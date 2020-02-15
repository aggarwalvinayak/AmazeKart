from rest_framework import serializers
from . models import Product,Image
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    phoneno= serializers.CharField()

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    class Meta:
        model = CustomUser

        fields = ('email','firstname','lastname','phoneno')

class ImageSerializer(serializers.ModelSerializer):
    imageid=serializers.IntegerField()
    imageurl=serializers.URLField()

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    class Meta:
        model = Image

        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    user = CustomUserSerializer(read_only = True)

    productid = serializers.IntegerField()
    productname = serializers.CharField(max_length = 100)
    price = serializers.IntegerField()
    category = serializers.CharField(max_length = 100)

    description = serializers.CharField(max_length = 200)

    images = ImageSerializer(read_only = True,source="image_set",many = True)


    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product

        fields = '__all__'

