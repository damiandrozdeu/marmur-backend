from rest_framework import serializers
from .models import Product, OptionValue, Order

class OptionValueSerializer(serializers.ModelSerializer):
    option_type = serializers.StringRelatedField()

    class Meta:
        model = OptionValue
        fields = ['id', 'value', 'price_diff', 'option_type']

class ProductSerializer(serializers.ModelSerializer):
    options = OptionValueSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price', 'description', 'image', 'options']

class OrderSerializer(serializers.ModelSerializer):
    selected_options = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=OptionValue.objects.all()
    )

    class Meta:
        model = Order
        fields = ['id', 'email', 'product', 'selected_options', 'total_price']
