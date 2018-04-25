from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product

# Create your views here.

class HomeView(TemplateView):
  template_name = "products/home.html"

  def get_context_data(self, *args, **kwargs):
    products = Product.objects.all()
    return { "products" : products }