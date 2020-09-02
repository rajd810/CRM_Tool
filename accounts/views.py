from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required #this can use for login all the pages

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # showing register successful msg to after creation

#login information

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':  #which method 
			username = request.POST.get('username')  # get the username with POST
			password = request.POST.get('password')  # get the password with POST

			user = authenticate(request, username=username, password=password)  # need to authenicate with request
			
			# user need to check below login details are correct

			if user is not None: # condn
				login(request, user)
				return redirect('home') # after successsfull to dashboard
			else:
				messages.info(request, "Username or Password is incorrect")

		context ={}
		return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')			
				messages.success(request, "Profile has been created for " + user) # message library
				return redirect('login')

		context = {'form': form}
		return render(request, 'accounts/register.html', context)


#home url function
@login_required(login_url = 'login') # use this decorators from auth
def home(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status ='Pending').count()


	context = {
				'customers': customers,
				 'orders': orders,
				 'total_orders': total_orders,
				 'delivered': delivered,
				 'pending': pending
			}

	return render(request, 'accounts/dashboard.html', context)

#products url function
@login_required(login_url = 'login')
def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products': products})

#customer url function
@login_required(login_url = 'login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	
	orders = customer.order_set.all()
	order_count = orders.count()

	context ={

				'customer': customer,
				'orders': orders,
				'order_count': order_count
	}

	return render(request, 'accounts/customer.html', context)

@login_required(login_url = 'login')
def createOrder(request):

	form = OrderForm()

	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	
	context ={ 'form': form }
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
	return render(request, 'accounts/order_form.html', context)