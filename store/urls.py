from django.urls import path

from store.views import IndexView, SaleCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("sale/<int:pk>/", SaleCreateView.as_view(), name="sale"),
]

app_name = "store"
