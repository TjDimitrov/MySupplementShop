from django.contrib import admin
from ExamProject.products.models import Product, ProductCategory, Cart, Review


class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(ProductCategory)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Product, SettingAdmin)
