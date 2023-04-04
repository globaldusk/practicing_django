from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def contact(request):
    form = ContactForm()
    return render(request, 'form.html', {'form': form})