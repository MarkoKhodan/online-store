from django.contrib import admin

from store.models import Item, Employee, Sale


admin.site.register(Employee)
admin.site.register(Sale)
admin.site.register(Item)
