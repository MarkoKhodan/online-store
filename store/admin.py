from django.contrib import admin

from store.models import Item, Employee, Sale


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        update_fields = []

        if change:
            if form.initial["price"] != form.cleaned_data["price"]:
                update_fields.append("price")

            obj.save(update_fields=update_fields)
        else:
            super().save_model(request, obj, form, change)


admin.site.register(Employee)
admin.site.register(Sale)
