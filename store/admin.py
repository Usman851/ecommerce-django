from django.contrib import admin
from .models import Product, Cart, Order, OrderItem

admin.site.register(Product)
admin.site.register(Cart)

admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):   # or StackedInline
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'is_paid', 'created_at']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)