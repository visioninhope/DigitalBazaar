from rest_framework import serializers
from product.models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    
class ProductSerializer(serializers.ModelSerializer):
    getFinalPrice = serializers.ReadOnlyField()
    class Meta:
        model= Product
        fields = "__all__"
        depth = True