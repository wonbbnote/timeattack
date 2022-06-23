from rest_framework import serializers

from .models import Category, Item, Order, ItemOrder

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = ["name", "image_url", "category"]

class OrderSerializer(serializers.ModelSerializer):
    item = CategorySerializer(many=True, )
    class Meta:
        model = Order
        fields = ["name", "image_url", "category"]


class ItemOrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, )
    order = OrderSerializer(many=True, )
    class Meta:
        model = ItemOrder
        # 모든 필드 사용하고 싶을 경우 fields = "__all__"
        fields = ["name", "image_url", "category"]