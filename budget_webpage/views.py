from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    template = 'home.html'
    context = { "title": 'home'}
    return render(request, template, context)

def ledger(request):
    template = 'ledger.html'
    context = { "title": 'ledger'}
    return render(request, template, context)

def budget(request):
    template = 'budget.html'
    context = { "title": 'budget'}
    return render(request, template, context)

def debt(request):
    template = 'debt.html'
    context = { "title": 'debt'}
    return render(request, template, context)