from rest_framework import serializers
from . models import Product,Image

class ProductSerializer(serializers.ModelSerializer):
    productid = serializers.IntegerField()
    productname = serializers.CharField(max_length = 100)
    price = serializers.IntegerField()
    category = serializers.CharField(max_length = 100)

    description = serializers.CharField(max_length = 200)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product

        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    imageid=serializers.IntegerField()
    imageurl=serializers.URLField()

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    class Meta:
        model = Image

        fields = '__all__'