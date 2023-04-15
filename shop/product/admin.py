from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description', 'available']
    list_filter = ['available', 'price']
    list_editable = ['price', 'description', 'available']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
