from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from shop.models import Customer, Product, Category
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class CategoriesListView(ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = "list_of_all_categories"

class CustomersListView(ListView):
    template_name = 'customers.html'
    model = Customer
    context_object_name = "list_of_all_customers"

class ProductListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = "list_of_all_products"