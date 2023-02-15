from django.shortcuts import render ,redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'index.html',context)

@login_required
def add_product(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ProductForm()
        context={'form':form}
    return render(request,'add_product.html',context)

@login_required
def edit_product(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ProductForm(instance=product)
        context={'form':form}
    return render (request, 'edit_product.html',context)

@login_required
def delete_product(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('index')