from rest_framework import serializers
from .models import *
from datetime import datetime

class DeliverypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverypoint
        fields= ("name",'id')

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields= ("name",'id')

class CounterpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields= "__all__"

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields= ("name",'id')

class DealSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    counterparty = CounterpartySerializer()
    delivery_point = DeliverypointSerializer()
    tool = ToolSerializer()
    class Meta:
        model = Deal
        fields = ('id','type','date_deal','counterparty','delivery_point', 'tool', 'delivery_start','delivery_end', 'volume','cost')

    def create(self, validated_data):
        _name= validated_data.pop('type')
        _counterparty=validated_data.pop('counterparty')
        _delivery_point=validated_data.pop('delivery_point')
        _tool=validated_data.pop('tool')
        type = Type.objects.get(name=_name["name"])
        counterparty = Counterparty.objects.get(name=_counterparty["name"])
        delivery_point = Deliverypoint.objects.get(name=_delivery_point["name"])
        tool = Tool.objects.get(name=_tool["name"])
        instance = Deal.objects.create(
                                        type=type,
                                        counterparty=counterparty,
                                        delivery_point= delivery_point,
                                        tool=tool,
                                        date_deal=validated_data.pop('date_deal'),
                                        delivery_start=validated_data.pop('delivery_start'),
                                        delivery_end=validated_data.pop('delivery_end'),
                                        volume=validated_data.pop('volume'),
                                        cost=validated_data.pop('cost')
                                        )

        return instance


class CounterpartyDealsSerializers(serializers.ModelSerializer):
    type = TypeSerializer()
    counterparty = CounterpartySerializer()
    delivery_point = DeliverypointSerializer()
    tool = ToolSerializer()
    class Meta:
        model = Deal
        fields = ('id','type','date_deal','counterparty','delivery_point', 'tool', 'delivery_start','delivery_end', 'volume','cost')


class ReportSerializers(serializers.ModelSerializer):
    class Meta: 
        model =  Deal
        fields =('volume','cost','delivery_start','delivery_end',)

class UpdateReportSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Report
        fields ='__all__'

    def update(self, instance, validated_data):
         
            instance.score = validated_data['score']
            instance.volume = validated_data['volume']
            instance.cost = validated_data['cost']

            instance.save()

            return instance