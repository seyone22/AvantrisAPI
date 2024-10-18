# serializers.py
from django.utils.dateparse import parse_datetime
from rest_framework import serializers

from AvantrisAPI.models import User, Item
import re

# Serializer, to ensure constraints are maintained
# Checks if items have an id, quantity is 0 or above, and price is 0 or above.
class ItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(required=True)
    quantity = serializers.IntegerField(min_value=0)
    price = serializers.FloatField(min_value=0)

    class Meta:
        model = Item
        fields = ['item_id', 'quantity', 'price']

    def validate_item_id(self, value):
        if not value:
            raise serializers.ValidationError('Item id is required')
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantity must be greater than 0')
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return value

class UserSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = User
        fields = ['user_id', 'email', 'timestamp', 'items']

    def validate_user_id(self, value):
        if not value:
            raise serializers.ValidationError('User id is required')
        return value

    # Check if it aligns with the something@someting.sometig format.
    def validate_email(self, value):
        email_regex = r'^[\w\.-]+@[]w].-]+\.\w+$'
        if not re.match(email_regex, value):
            raise serializers.ValidationError('Invalid email')
        return value

    def vaildate_timestamp(self, value):
        if parse_datetime(value) is None:
            raise serializers.ValidationError('Invalid timestamp')
        return value

    def validate_items(self, data):
        if not data.get('items'):
            raise serializers.ValidationError('No items')
        return data
