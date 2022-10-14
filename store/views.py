from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from store.forms import SaleForm
from store.models import Item, Sale, PriceChanges


class IndexView(generic.ListView):
    model = Item
    context_object_name = "items_list"
    template_name = "index.html"


class SaleCreateView(generic.CreateView):
    model = Sale
    success_url = reverse_lazy("store:index")
    template_name = "sale_form.html"
    form_class = SaleForm

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=self.kwargs["pk"])
        self.initial["item"] = item
        context = super().get_context_data(**kwargs)
        context["item"] = item
        return context


class SaleListView(LoginRequiredMixin, generic.ListView):
    model = Sale
    template_name = "order_list.html"
    ordering = ["-created_at"]
    paginate_by = 5


class PriceChangesListView(LoginRequiredMixin, generic.ListView):
    template_name = "price-changes_list.html"
    model = PriceChanges
    ordering = ["-created_at"]
