from django.db import models

# Create your models here.
class Counterparty(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    score = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Deliverypoint(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name 

class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name

class Deal(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    date_deal = models.DateField()
    counterparty = models.ForeignKey(Counterparty,  on_delete=models.CASCADE, null=True)
    delivery_point = models.ForeignKey(Deliverypoint, on_delete=models.CASCADE, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True)
    delivery_start = models.DateField()
    delivery_end = models.DateField()
    volume = models.FloatField()
    cost = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id

class Report(models.Model):
    score = models.CharField(max_length=10)
    volume = models.FloatField(null=True)
    cost = models.FloatField(null=True)

    def __str__(self):
        return self.score