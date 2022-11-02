from rest_framework import serializers
from .models import *

class DeliverypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverypoint
        fields= ("point_name",)

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields= ("type_name",)

class CounterpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields= ("cp_name",'id')

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields= ("tool_name",)

class DealSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    counterparty = CounterpartySerializer()
    delivery_point = DeliverypointSerializer()
    tool = ToolSerializer()
    class Meta:
        model = Deal
        fields = ('id','type','date_deal','counterparty','delivery_point', 'tool', 'delivery_start','delivery_end', 'volume','cost')

class CounterpartyDealsSerializers(serializers.ModelSerializer):
    type = TypeSerializer()
    counterparty = CounterpartySerializer()
    delivery_point = DeliverypointSerializer()
    tool = ToolSerializer()
    class Meta:
        model = Deal
        fields = ('id','type','date_deal','counterparty','delivery_point', 'tool', 'delivery_start','delivery_end', 'volume','cost')