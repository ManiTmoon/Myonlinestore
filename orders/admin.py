from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'is_paid', 'total_amount', 'status', 'delivery_address']
    list_filter = ['is_paid', 'status', 'created_at']
    search_fields = ['user__username']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
