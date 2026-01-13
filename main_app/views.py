from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item, Market
from .forms import MarketForm

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

# Define the about view function
def about(request):
    # Send about page response
    return render(request, 'about.html')

def item_index(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', {'items': items})

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    market_form = MarketForm()
    return render(request, 'items/detail.html', {'item': item, 'market_form': market_form})

def add_market(request, item_id):
    form = MarketForm(request.POST)
    if form.is_valid():
        new_market = form.save(commit=False)
        new_market.item_id = item_id
        new_market.save()
    return redirect('item-detail', item_id=item_id)


# Create your views here.

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'item_type', 'price', 'description']

class ItemDelete(DeleteView):
    model = Item
    success_url = '/items/'

class MarketUpdate(UpdateView):
    model = Market
    fields = ['outlet', 'price']

    def get_success_url(self):
        return f"/items/{self.object.item.id}/"

class MarketDelete(DeleteView):
    model = Market
    def get_success_url(self):
        return f"/items/{self.object.item.id}/"
