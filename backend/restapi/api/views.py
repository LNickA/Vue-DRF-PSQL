from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.
class DealApiView(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class CounterPartyApiView(generics.ListCreateAPIView):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartySerializer

class ToolApiView(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class TypeApiView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class DeliverypointApiView(generics.ListCreateAPIView):
    queryset = Deliverypoint.objects.all()
    serializer_class = DeliverypointSerializer

class CounterPartyDealsApiView(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = CounterpartyDealsSerializers
    def get_queryset(self):
        return Deal.objects.filter(counterparty = self.kwargs['id'])

class ReportApiView(generics.ListAPIView):
        queryset = Deal.objects.order_by('-cost')
        serializer_class = ReportSerializers

class UpdateReportApiView(generics.UpdateAPIView):
        queryset = Report.objects.all()
        serializer_class = UpdateReportSerializers
