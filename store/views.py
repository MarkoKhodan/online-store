from django.views import generic

from store.models import Item


class IndexView(generic.ListView):
    model = Item
    context_object_name = "items_list"
    template_name = "index.html"
