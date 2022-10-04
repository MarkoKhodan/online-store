from annoying.decorators import render_to

from store.models import Item


@render_to('index.html')
def index(request):
    items = Item.objects.all()
    return {'items': items}

