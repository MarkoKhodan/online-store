from django.db import models


class Item(models.Model):
    pass


class Employee(models.Model):
    pass


class Sale(models.Model):
    item = models.ForeignKey(Item, related_name="sales", on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    total_price = models.FloatField()
    seller = models.ForeignKey(Employee, related_name="sales", on_delete=models.CASCADE)




