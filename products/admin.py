from django.contrib import admin
from products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
  model  = ProductImage

class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  inlines = [
    ProductImageInline
  ]

admin.site.register(Product, ProductAdmin)