# serializers.py
from rest_framework import serializers

from AvantrisAPI.models import User


class ItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(required=True)
    quantity = serializers.IntegerField(min_value=0)
    price = serializers.FloatField(min_value=0)


class UserSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        return data
