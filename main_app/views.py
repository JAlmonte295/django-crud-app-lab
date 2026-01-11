from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'base.html')

# Define the about view function
def about(request):
    # Send about page response
    return render(request, 'about.html')
