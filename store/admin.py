# from django.contrib import admin
# from .models import Category, Customer, Product, Order, Profile
# from django.contrib.auth.models import User



# admin.site.register(Category)
# admin.site.register(Customer)   
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(Profile)


# # Mix Profilr info and user info

# class ProfileInline(admin.StackedInline):
#     model = Profile

# # Extend User Model
# class UserAdmin(admin.ModelAdmin):
#     model = User
#     field = ['username', 'first_name', 'last_name', 'email']
#     inlines = [ProfileInline]

# # unregister the Old user admin
# admin.site.unregister(User)

# # Register the new User Admin
# admin.site.register(User, UserAdmin)







from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile, ProductImage
from django.contrib.auth.models import User

# ✅ Inline model to allow multiple image uploads
class ProductImageInline(admin.TabularInline):  
    model = ProductImage  
    extra = 3  # Allows adding up to 3 extra images per product

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # Add extra images inside the Product Admin Panel

# Register Models
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)  # ✅ Register Product with custom Admin
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(ProductImage)  # ✅ Register ProductImage separately

# Mix Profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

# Unregister the Old User Admin
admin.site.unregister(User)

# Register the new User Admin
admin.site.register(User, UserAdmin)



