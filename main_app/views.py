from django.shortcuts import render

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

# Define the about view function
def about(request):
    # Send about page response
    return render(request, 'about.html')

class Item:
    def __init__(self, name, type, price, description):
        self.name = name
        self.type = type
        self.price = price
        self.description = description

items = [
    Item('Max Steel', 'Toy', 100.00, 'bough when i was a child'),
    Item('Game Boy', 'Video Game', 0.00, 'passed down my my parents'),
    Item('Pokemon Gen 1 Pack', 'Cards', 10.00, 'unopened, bought back in the early 2000s'),
]

def item_index(request):
    return render(request, 'items/index.html', {'items': items})

# Create your views here.