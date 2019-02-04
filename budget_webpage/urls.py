from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ledger', views.ledger, name='ledger'),
    path('budget', views.budget, name='budget'),
    path('', views.ledger, name='ledger')
]
