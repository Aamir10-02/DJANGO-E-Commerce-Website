from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User

# Register model on admin section.

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

#Create an Order Item Inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0 

# Extend Our Order Model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    fields = ["user", "full_name","email", "shipping_address", "amount_paid", "date_ordered", "shipped", "date_shipped"]
    inlines=[OrderItemInline]
# Doing This to merge the order and order items at one place in admin panel
# Unregister Order Model
admin.site.unregister(Order)

# Re-Register our Order and order items
admin.site.register(Order, OrderAdmin)