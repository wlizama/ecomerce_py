from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from products.models import Product
from comments.forms import CommentForm

# Create your views here.

class HomeView(TemplateView):
  template_name = "products/home.html"

  def get_context_data(self, *args, **kwargs):
    products = Product.objects.all()
    return { "products" : products }


class ProductDetailView(DetailView):
  model = Product

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    comment_form = CommentForm()
    context["comment_form"] = comment_form
    return context