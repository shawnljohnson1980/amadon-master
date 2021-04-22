from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def checkout(request):
    quantity = int(request.POST["quantity"])
    price = float(request.POST["price"])
    total_charge = quantity * price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity, total_price=total_charge)
    return redirect( "/check_out")

def check_out(request):
    products=Product.objects.all()
    order=Order.objects.all()
    context={
        'products':products,
        'orders':order
    }
    return render(request,'checkout.html',context)

def product_create(request):
    
    return render(request,'create_product.html')

def create_product(request):
    product=Product.objects.all()
    price=request.POST['price']
    description=request.POST['description']
    genere=request.POST['genere']
    name=request.POST['name']
    Product.objects.create(
        price=price,
        name=name,
        genere=genere,
        description=description
    )
    return redirect('/')
