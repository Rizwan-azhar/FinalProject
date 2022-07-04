from django.shortcuts import render

def home(request):
 return render(request, 'app/home.html')
def crossbody(request):
 return render(request, 'app/crossbody.html')

def backpack(request):
 return render(request, 'app/backpack.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def orderplaced(request):
 return render(request, 'app/orderplaced.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')



def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def bags(request):
 return render(request, 'app/bags.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
