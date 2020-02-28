from django.contrib import admin
from .models import Product, Category, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines=[
        ReviewInline,
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
