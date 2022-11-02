from django.db import models

# Create your models here.
class Counterparty(models.Model):
    cp_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.cp_name

class Deliverypoint(models.Model):
    point_name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.point_name

class Tool(models.Model):
    tool_name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.tool_name 

class Type(models.Model):
    type_name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.type_name

class Deal(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True)
    date_deal = models.DateField()
    counterparty = models.ForeignKey(Counterparty, on_delete=models.PROTECT, null=True)
    delivery_point = models.ForeignKey(Deliverypoint, on_delete=models.PROTECT, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.PROTECT, null=True)
    delivery_start = models.DateField()
    delivery_end = models.DateField()
    volume = models.FloatField()
    cost = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id

