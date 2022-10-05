from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from store.forms import SaleForm
from store.models import Item, Sale


class IndexView(generic.ListView):
    model = Item
    context_object_name = "items_list"
    template_name = "index.html"


class SaleCreateView(generic.CreateView):
    model = Sale
    success_url = reverse_lazy("store:index")
    template_name = "sale_form.html"
    form_class = SaleForm
    # fields = "__all__"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["item"] = Item.objects.get(id=self.kwargs["pk"])
        return context

    def get_initial(self):
        Item.objects.get(pk=self.kwargs.get("pk"))
        initial = super(SaleCreateView, self).get_initial()
        initial["item"] = Item.objects.get(pk=self.kwargs["pk"])
        return initial


class SaleListView(LoginRequiredMixin, generic.ListView):
    model = Sale
    template_name = "order_list.html"
    ordering = ["-created_at"]
