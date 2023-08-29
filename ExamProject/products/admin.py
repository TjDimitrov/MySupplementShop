from django.contrib import admin

from ExamProject.products.models import Product, ProductCategory, Cart

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Cart)
