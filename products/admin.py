from django.contrib import admin
from .models import Category, Product, Discount, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'stock', 'category', 'rating']
    search_fields = ['name', 'brand']
    list_filter = ['category', 'brand']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['product', 'percentage', 'fixed_amount']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    search_fields = ['user__username', 'product__name']
    list_filter = ['rating', 'created_at']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Review, ReviewAdmin)
