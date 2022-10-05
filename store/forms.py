from django.forms import ModelForm, Select, HiddenInput

from store.models import Sale


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = Sale
        fields = [
            "item",
            "quantity",
            "seller",
        ]
        widgets = {"item": HiddenInput()}
