from django.urls import path

from store.views import (
    IndexView,
    SaleCreateView,
    Sale,
    SaleListView,
    PriceChangesListView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("sale/<int:pk>/", SaleCreateView.as_view(), name="sale-create"),
    path("sale/", SaleListView.as_view(), name="sale-list"),
    path("price-changes/", PriceChangesListView.as_view(), name="price-changes-list"),
]

app_name = "store"
