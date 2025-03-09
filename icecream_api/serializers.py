from rest_framework import serializers

from icecream_api.models.command_related import Command
from icecream_api.models.item_related import Batch, Item


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = "__all__"
