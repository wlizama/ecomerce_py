from django.contrib import admin
from products.models import Product, ProductImage, ProductCategory, LogBuy


class ProductImageInline(admin.TabularInline):
  model  = ProductImage

class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  inlines = [
    ProductImageInline
  ]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(LogBuy)