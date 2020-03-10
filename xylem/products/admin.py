from django.contrib import admin
from .models import Product, Category, Review, CategoryImage


class ReviewInline(admin.TabularInline):
    model = Review

class ProductAdmin(admin.ModelAdmin):
    inlines=[
        ReviewInline,
    ]

class CategoryCoverInline(admin.TabularInline):
    model = CategoryImage

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryCoverInline,]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
