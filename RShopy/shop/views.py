from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect

from django.contrib.auth import login


from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PrimeForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from.models import Destination



# Create your views here.
@login_required(login_url='login')


def home(request):
    return render(request, 'shop/home.html')


def shop(request):
    
    dest1 = Destination()
    dest1.name = "Iphone pro max 14"
    dest1.price =  "1.5k"
    dest1.img = "Product7.jpg"

    return render(request, 'shop/shop.html',{'dest1':dest1})


def cart(request):
    return render(request, 'shop/cart.html')


def product_details(request):
    return render(request, 'shop/product_details.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def HomePage(request):
    return render (request,'shop/hom.html')



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'shop/signup.html')



def LoginPage(request):
    error_message = None
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."


    
    return render(request, 'shop/login.html', {'error_message': error_message})



def LogoutPage(request):
    logout(request)
   




def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def fibonacci_view(request):
    series = []
    if request.method == 'POST':
        n = int(request.POST.get('number', 0))
        series = fibonacci_series(n)
    return render(request, 'shop/fibonacci.html', {'series': series})




def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def index(request):
    result = None
    if request.method == "POST":
        number = request.POST.get('number')
        try:
            number = int(number)
            result = factorial(number)
        except ValueError as e:
            result = str(e)
    
    return render(request, 'shop/index.html', {'result': result})


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_view(request):
    result = None
    if request.method == 'POST':
        form = PrimeForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            result = is_prime(number)
    else:
        form = PrimeForm()
    
    return render(request, 'shop/prime_check.html', {'form': form, 'result': result})





from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if len(username) < 5:  # Minimum 5 characters for username
            messages.error(request, 'Username must be at least 5 characters.')
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            messages.error(request, 'Invalid credentials.')

    return render(request, 'shop/logins.html')






from django.views.decorators.http import require_POST
from django.shortcuts import redirect

@require_POST
def order_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST['quantity'])
    Order.objects.create(product=product, quantity=quantity)
    return redirect('product_list')






