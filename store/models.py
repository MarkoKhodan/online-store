from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title}"


class Employee(models.Model):
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sale(models.Model):
    item = models.ForeignKey(Item, related_name="sales", on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    total_cost = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True, editable=False
    )
    seller = models.ForeignKey(Employee, related_name="sales", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def calc_total(self):
        return self.item.price * self.quantity

    def save(self, *args, **kwargs):
        self.total_cost = self.calc_total()
        super(Sale, self).save()

    def __str__(self):
        return (
            f"{self.created_at} {self.quantity} X {self.item.title} = {self.total_cost}"
        )
