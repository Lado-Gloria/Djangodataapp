from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductUploadForm
from .models import Product

def upload_product(request):
    form = ProductUploadForm()

    if request.method == "POST":
        form = ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "inventory/product_upload.html", {"form": form})

def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html", {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "inventory/product_detail.html", {"product": product})

def edit_product_view(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", id=product.id)
    else:
        form = ProductUploadForm(instance=product)

    return render(request, "inventory/edit_product.html", {"form": form})



# def upload_product(request):
#    if request.method=="POST":
#      form=ProductUploadForm(request.POST,request.FILES)
#      if form.is_valid():
#         form.save()
#    else:
#        form =ProductUploadForm()
#    return render(request, "inventory/product_upload.html",{"form":form})

# def products_list(request):
#    products =Product.objects.all()
#    images = []
#    for product in products:
#         images.append(product.image)
#    return render(request,"inventory/product_list.html",{"products": products, "images": images})

# def products_detail(request,id):
#    product=Product.objects.get(pk=id)
#    return render(request,"inventory/product_detail.html",{"product":product})

#    product=Product.objects.get(id=id)
#    if request.method=="POST":
#       form =ProductUploadForm(request.POST,instance=product)
#       if form.is_valid():
#          form.save()
#          return redirect("product_detail_view",id=product.id)
#       else:
#          form=ProductUploadForm(instance=product)
#          return render(request,"inventory/edit_product.html",{"form":form})
      

