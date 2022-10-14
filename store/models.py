from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from tracking_model import TrackingModelMixin


class Item(TrackingModelMixin, models.Model):
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


class PriceChanges(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(
        Item, related_name="price_changes", on_delete=models.CASCADE
    )
    new_price = models.DecimalField(max_digits=6, decimal_places=2)


@receiver(post_save, sender=Item)
def post_save(sender, instance, created, **kwargs):
    if created:
        PriceChanges.objects.create(new_price=instance.price, item_id=instance.id)
    elif "price" in instance.tracker.changed:
        PriceChanges.objects.create(new_price=instance.price, item_id=instance.id)
