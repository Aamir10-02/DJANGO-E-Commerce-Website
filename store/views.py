from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.db.models import Q
import json
from cart.cart import Cart
def search(request):
    # Determine if the user filled the form
    if request.method == "POST":
        searched = request.POST['searched']
        # Query the database for products

        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        # Return the results for null
        if not searched:
            messages.success(request, "No results found")
            return render(request, 'search.html', {})
        
        else:


         return render(request, 'search.html', {'searched': searched})
    else:

     return render(request, 'search.html', {})



def update_info(request):
    if request.user.is_authenticated:
     # Get current user
     current_user = Profile.objects.get(user__id=request.user.id)
     # get current users shipping address
     shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
     # Get original user form
     form = UserInfoForm(request.POST or None, instance=current_user)
     # Get users shipping form
     shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
     if form.is_valid() or shipping_form.is_valid():
      form.save()#original user form
      shipping_form.save()# Shipping form

      
      messages.success(request, "Your Info Has Been Updated!!")
      return redirect('home')
     return render(request, "update_info.html", {'form':form, 'shipping_form': shipping_form})
    else:
    #  messages.success(request, "You Must Be Logged In To Access That Page!!")
     messages.warning(request, "You Must Be Logged In To Access That Page!!")

     return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user =request.user
        # Did the user submit the form?
        if request.method == 'POST':
        # Do Stuff
          form = ChangePasswordForm(current_user, request.POST)
          # Check if form is valid
          if form.is_valid():
            form.save()
            messages.success(request, "Password Has Been Updated!!")
            login(request, current_user)
            return redirect('update_user')
          
          else:
              for error in list(form.errors.values()):
                  messages.error(request, error)
                  return redirect('update_password')
        
        else:
          form = ChangePasswordForm(current_user)
          return render(request, "update_password.html", {'form': form})
    else:
        # messages.success(request, "You Must Be Logged In To Access That Page!!")
        messages.warning(request, "You Must Be Logged In To Access That Page!!")

        return redirect('home')
    

def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories": categories})

def category(request, foo):
    # Replace hyphens with spaces
    foo = foo.replace('-', ' ')
    # Get the category from url
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})

    except:
        messages.success(request, "Category does not exist!")
        return redirect('home')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Do Some Shopping Cart Stuff

            current_user = Profile.objects.get(user__id=request.user.id)
            # Get their saved cart from db

            saved_cart = current_user.old_cart
            # Convert the string to a dictionary
            if saved_cart:
                # Convert the string to a dictionary using json
                converted_cart = json.loads(saved_cart)
                # Add the loaded cart dictionary to the session
                cart = Cart(request)
                # Loop through the cart and add the items from the dictionary
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)


            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error please try again!")
            return redirect('login')
    else:
    
     return render(request, 'login.html', {})

def logout_user(request):
    messages.success(request, "Logged out successfully!")
    logout(request)
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user =authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("User was created - Please fill the information ") )
            return redirect('update_info')
        else:
            messages.success(request, "There was an error please try again!")
            return redirect('register')
    return render(request, 'register.html', {'form': form})