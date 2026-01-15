from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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

@login_required
def item_index(request):
    items = Item.objects.filter(user=request.user)
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('item-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )


# Create your views here.

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'item_type', 'price', 'description']

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/items/'

class MarketUpdate(LoginRequiredMixin, UpdateView):
    model = Market
    fields = ['outlet', 'price']

    def get_success_url(self):
        return f"/items/{self.object.item.id}/"

class MarketDelete(LoginRequiredMixin, DeleteView):
    model = Market
    def get_success_url(self):
        return f"/items/{self.object.item.id}/"

class Home(LoginView):
    template_name = 'home.html'

