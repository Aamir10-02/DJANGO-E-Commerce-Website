from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User



admin.site.register(Category)
admin.site.register(Customer)   
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# Mix Profilr info and user info

class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

# unregister the Old user admin
admin.site.unregister(User)

# Register the new User Admin
admin.site.register(User, UserAdmin)


