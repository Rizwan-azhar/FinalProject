from django.shortcuts import render
from django.views import View
from .models import Customer, Product , Orderplaced , Cart
from .forms import CustomerRegistrationForm
from django.contrib import messages

class ProductView(View):
    def get(self, request):
        handbags = Product.objects.filter(category = 'H')
        crossbody = Product.objects.filter(category = 'C')
        backpack = Product.objects.filter(category = 'B')
        return render(request, 'app/home.html', {'handbags':handbags , 'crossbody':crossbody, 'backpack':backpack })




class CrossBodyView(View):
    def get(self, request, data = None):
        
        if data == None:
            crossbody = Product.objects.filter(category = 'C')
        elif data == 'lv' or data == 'mk':
            crossbody = Product.objects.filter(category = 'C').filter(brand = data)

        return render(request, 'app/crossbody.html' , {'crossbody':crossbody})

class BackPackView(View):
    def get(self, request , data = None):
        if data == None:
            backpack = Product.objects.filter(category = 'B')
        elif data == 'lv' or data == 'mk':
            backpack = Product.objects.filter(category = 'B').filter(brand = data)
        return render(request, 'app/backpack.html' , {'backpack': backpack})

class ProductDetailView(View):
    def get(self, request, pk):
       product = Product.objects.get(pk = pk)
       return render(request, 'app/productdetail.html', {'product':product})




def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def profile(request):
 return render(request, 'app/profile.html') 



def address(request):
 return render(request, 'app/address.html')

def orderplaced(request):
 return render(request, 'app/orderplaced.html')

def buy_now(request):
 return render(request, 'app/buynow.html')



def orders(request):
 return render(request, 'app/orders.html')

class BagView(View):
    def get(self, request, data = None):
        
        if data == None:
            handbags = Product.objects.filter(category = 'H')
        elif data == 'lv' or data == 'mk':
            handbags = Product.objects.filter(category = 'H').filter(brand = data)
       
        return render(request, 'app/bags.html', {'handbags':handbags})





class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',  {'form' : form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',  {'form' : form})




def checkout(request):
 return render(request, 'app/checkout.html')
