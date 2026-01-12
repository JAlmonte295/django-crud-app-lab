from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item

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
    return render(request, 'items/detail.html', {'item': item})


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

